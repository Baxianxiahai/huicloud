#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# coding=utf-8

import cv2
import numpy as np  
# import matplotlib.pyplot as plt
# import imutils
# from ctypes import c_uint8
# import argparse
# import math
# import random
# import sys
# import time
# import json
# import os   #Python的标准库中的os模块包含普遍的操作系统功能  
# import re   #引入正则表达式对象  
#import Image
import pytesseract
#import pillow
from selenium import webdriver
from PIL import Image


def Original_test(img):
    #创建一个名字加 “ input image ” 的窗口，  
    #窗口可以根据图片大小自动调整
    cv2.namedWindow('input image',cv2.WINDOW_AUTOSIZE)  
    cv2.imshow('input image', img)
    #cv2.imwrite('messigray.png',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def Preprocessing_binvalue_test_plain(img, pattern):
    #生成新图像
    new = np.zeros(img.shape, np.uint8)    

    #灰度化
    for i in range(new.shape[0]):  #Axis-y/height/Rows
        for j in range(new.shape[1]):
            (b,g,r) = img[i,j]
            #加权平均法
            new[i,j] = int(0.3*float(b) + 0.59*float(g) + 0.11*float(r))&0xFF

    #中值滤波
    #blur= cv2.GaussianBlur(new, (3,3), 1)
    midGray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Middle Blur', midGray)
    
    #固定二值化
    if (pattern == 1):
        ret, binGray = cv2.threshold(new, 160, 255, cv2.THRESH_BINARY)
        binGray = cv2.cvtColor(binGray, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('BinValue FixBin Image', binGray)
        cv2.imwrite('mid.jpg', binGray)
    
    #自适应二值化
    elif (pattern == 2):
        binGray = cv2.adaptiveThreshold(midGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 5)   # ADAPTIVE_THRESH_MEAN_C ADAPTIVE_THRESH_GAUSSIAN_C
        #binRes= cv2.GaussianBlur(binGray, (5,5), 1.5) #medianBlur

        #cv2.imshow('BinValue AdaptiveBin Image', binGray)
        cv2.imwrite('mid.jpg', binGray)
    
    #基于直方图统计的二值化
    elif (pattern == 3):
        #ret1,th1 = cv2.threshold(midGray,127,255,cv2.THRESH_BINARY)
        # Otsu's thresholding
        #ret2,th2 = cv2.threshold(midGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(midGray,(3,3),0)
        ret3, binGray = cv2.threshold(blur, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
        #cv2.imshow('BinValue Statistic Image', binGray)
        cv2.imwrite('mid.jpg', binGray)

    return binGray;

def Preprocessing_get_image_position(img):
    # 膨胀+腐蚀等形态学变化  
    kerne1 = np.ones((15, 15), np.uint8)  
    img_erosin = cv2.erode(img, kerne1, iterations=1)
    
    #再次中值滤波
    midFilter= cv2.medianBlur(img_erosin, 3)
    
    #固定二值化
    ret, binImg = cv2.threshold(midFilter, 135, 255, cv2.THRESH_BINARY)
    #cv2.imshow("img_erosin and Noise removal", binImg)
    
    #获得边界
    _, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    (roi_x, roi_y, roi_w, roi_h) = (0, 0, 0, 0)
    for c in contours:
        (x,y,w,h)=cv2.boundingRect(c)
        cArea = cv2.contourArea(c)
        if (cArea>2000) and (x!=0) and (y!= 0):
            print("\nGet favorate area: ", x,y,w,h)
            (roi_x, roi_y, roi_w, roi_h) = (x, y, w, h)
            #cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 1)
    #cv2.rectangle(img, (roi_x,roi_y), (roi_x+roi_w, roi_y+roi_h), (0, 0, 255), 1)
    #cv2.imshow("Bound Image", img)   
    
    #取得目标图象的区域
    targetImg = img[roi_y:(roi_y+roi_h), roi_x:(roi_x+roi_w)]
    #cv2.imshow("Target Image", targetImg)
     
    return targetImg;

def Preprocessing_addon_target_bill(binProcImg, workingImg, StandardCutImg):
    #先找图象位置
    posCutImg = Preprocessing_get_image_position(binProcImg)
    resizeImg = cv2.resize(posCutImg, (StandardCutImg.shape[1], StandardCutImg.shape[0]), interpolation = cv2.INTER_CUBIC)
    #cv2.imshow("Resize Cut Image", resizeImg)
    return resizeImg;

# 输入灰度图，返回hash 
def getHash(image): 
    avreage = np.mean(image) 
    hash = [] 
    for i in range(image.shape[0]): 
        for j in range(image.shape[1]): 
            if image[i,j] > avreage: 
                hash.append(1) 
            else: 
                hash.append(0) 
    return hash
  
  
# 计算汉明距离 
def Hamming_distance(hash1,hash2): 
    num = 0
    for index in range(len(hash1)): 
        if hash1[index] != hash2[index]: 
            num += 1
    return num 

#采用相同位置的方式进行对比
def func_compare_difference(StdImg, WorkImg):
    #找到轮廓
    _, contours, hierarchy = cv2.findContours(StdImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #RETR_TREE, RETR_CCOMP
    cacSize = (16, 16)
    
    #分别分析
    for c in contours:
        newSrc = StdImg.copy()
        newDst = WorkImg.copy()
        #求面积
        cArea = cv2.contourArea(c)
         
        if cArea < 50:
            pass
        elif cArea > 5000:
            pass
        else:
            #外矩形框
            (x,y,w,h)=cv2.boundingRect(c)
            #cv2.rectangle(StdImg, (x,y), (x+w, y+h), (0, 0, 255), 1)
            
            #取得感兴趣的区域
            srcImg = cv2.resize(StdImg[y:(y+h), x:(x+w)], cacSize, interpolation = cv2.INTER_CUBIC) 
            dstImg = cv2.resize(WorkImg[y:(y+h), x:(x+w)], cacSize, interpolation = cv2.INTER_CUBIC)
            #cv2.imshow("Char Src Image", StdImg[y:(y+h), x:(x+w)])
            #cv2.imshow("Char Dst Image", WorkImg[y:(y+h), x:(x+w)])
            hash1 = getHash(srcImg) 
            hash2 = getHash(dstImg ) 
            dis = Hamming_distance(hash1,hash2)
            cv2.imwrite("mid.jpg", StdImg[y:(y+h), x:(x+w)])
            midImg = Image.open("mid.jpg")
            text = pytesseract.image_to_string(midImg)
            a = 'Char=%s, Dis = %d' % (text, dis)
            newSrc = cv2.cvtColor(newSrc, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(newSrc, (x,y), (x+w, y+h), (0, 0, 255), 3)
            cv2.imshow("Src Image", newSrc)
            newDst = cv2.cvtColor(newDst, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(newDst, (x,y), (x+w, y+h), (0, 0, 255), 3)
            cv2.imshow("Dst Image", newDst)            
            print(a)
            cv2.waitKey(0)
            
#采用各自独立搜索的方式，但效果很差            
def func_compare_difference_method2(StdImg, WorkImg):
    #找到轮廓
    _, contoursSrc, hierarchySrc = cv2.findContours(StdImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #RETR_TREE, RETR_CCOMP
    _, contoursDst, hierarchyDst = cv2.findContours(WorkImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #RETR_TREE, RETR_CCOMP
    cacSize = (16, 16)
    
    index = 0
    #分别分析
    while index < len(contoursSrc):
        index += 1;
        newSrc = StdImg.copy()
        newDst = WorkImg.copy()
        #求面积
        cArea = cv2.contourArea(contoursSrc[index])
         
        if cArea < 50:
            pass
        elif cArea > 5000:
            pass
        else:
            #外矩形框
            (x,y,w,h)=cv2.boundingRect(contoursSrc[index])
            (xx, yy, ww, hh)=cv2.boundingRect(contoursDst[index])
            #cv2.rectangle(StdImg, (x,y), (x+w, y+h), (0, 0, 255), 1)
            
            #取得感兴趣的区域
            srcImg = cv2.resize(StdImg[y:(y+h), x:(x+w)], cacSize, interpolation = cv2.INTER_CUBIC) 
            dstImg = cv2.resize(WorkImg[yy:(yy+hh), xx:(xx+ww)], cacSize, interpolation = cv2.INTER_CUBIC)
            print(x, y, w, h)
            print(xx, yy, ww, hh)
            cv2.imshow("Char Src Image", StdImg[y:(y+h), x:(x+w)])
            cv2.imshow("Char Dst Image", WorkImg[yy:(yy+hh), xx:(xx+ww)])
            hash1 = getHash(srcImg) 
            hash2 = getHash(dstImg ) 
            dis = Hamming_distance(hash1,hash2)
            cv2.imwrite("mid.jpg", StdImg[y:(y+h), x:(x+w)])
            midImg = Image.open("mid.jpg")
            text = pytesseract.image_to_string(midImg)
            a = 'Char=%s, Dis = %d' % (text, dis)
            newSrc = cv2.cvtColor(newSrc, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(newSrc, (x,y), (x+w, y+h), (0, 0, 255), 3)
            cv2.imshow("Src Image", newSrc)
            newDst = cv2.cvtColor(newDst, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(newDst, (xx,yy), (xx+ww, yy+hh), (0, 0, 255), 3)
            cv2.imshow("Dst Image", newDst)            
            print(a)
            cv2.waitKey(0)

#文字识别
#https://testerhome.com/topics/4615
def test_identification():
    text = ''
    #text = pytesseract.image_to_string(img, 'chi_sim').decode('utf-8').replace(' ', '')
    img = Image.open("mid.jpg")
    text = pytesseract.image_to_string(img)
    print(text)
    return text;

def func_bill_identification():
    #原始图象
    inImgFile = "b1.jpg"
    orgImg=cv2.imread(inImgFile)
    binImg = Preprocessing_binvalue_test_plain(orgImg, 3)
    print("First Time Identification:")
    test_identification()
    StandardCutImg = Preprocessing_get_image_position(binImg)
    #cv2.imshow("First Time Cut Pic", StandardCutImg)
    
    #待识别图形
    inImgFile = "b2.jpg"
    workingImg=cv2.imread(inImgFile)
    binProcImg = Preprocessing_binvalue_test_plain(workingImg, 3)
    print("\nSecond Time Identification:")
    test_identification()
    TargetCutImg = Preprocessing_addon_target_bill(binProcImg, workingImg, StandardCutImg)
    #cv2.imshow("Second Time Cut Pic", TargetCutImg)
    
    #按照两种目标图，进行对比识别
    func_compare_difference(StandardCutImg, TargetCutImg)
    
    #cv2.imwrite("result_"+inImgFile, orgImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#总入口
if __name__ == "__main__":
    func_bill_identification()












