#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# coding=utf-8

import cv2
import numpy as np  
import matplotlib.pyplot as plt
import imutils
from ctypes import c_uint8
import argparse
import math
import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  


def Original_test(img):
    #创建一个名字加 “ input image ” 的窗口，  
    #窗口可以根据图片大小自动调整
    cv2.namedWindow('input image',cv2.WINDOW_AUTOSIZE)  
    cv2.imshow('input image', img)
    #cv2.imwrite('messigray.png',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def Preprocessing_resize_test(img):
    #img = cv2.resize(img,None,fx=1/2, fy=1/2, interpolation = cv2.INTER_CUBIC)
    height, width = img.shape[:2]
    ratio = 0.5
    res = cv2.resize(img, (int(ratio*width), int(ratio*height)), interpolation = cv2.INTER_CUBIC)
    return res;
    
def func_vision_worm_binvalue_test(img):
    #生成新图像
    #new = res.copy()
    #new = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    new = np.zeros(img.shape, np.uint8)    

    #灰度化
    for i in range(new.shape[0]):  #Axis-y/height/Rows
        for j in range(new.shape[1]):
            (b,g,r) = img[i,j]
            #均值算法
            #new[i,j] = (int(b)+int(g)+int(r))/3
            #最大值法
            #new[i,j] = max(int(b), int(g), int(r))
            #加权平均法
            new[i,j] = int(0.3*float(b) + 0.59*float(g) + 0.11*float(r))&0xFF

    #强制8bit转换
    #new = cv2.convertScaleAbs(new)

    #中值滤波
    blur= cv2.medianBlur(new, 5)
    midGray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('Middle Blur', midGray)

    #固定二值化
    #ret, binNew = cv2.threshold(new, 130, 255, cv2.THRESH_BINARY)

    #自适应二值化
    binGray = cv2.adaptiveThreshold(midGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 43, 5)   # ADAPTIVE_THRESH_MEAN_C ADAPTIVE_THRESH_GAUSSIAN_C
    binRes= cv2.GaussianBlur(binGray, (5,5), 1.5) #medianBlur
    #cv2.imshow('Adaptive Bin', binRes)
    return binRes;

def func_vision_worm_remove_noise_test(img):
    # 膨胀+腐蚀等形态学变化  
    kerne1 = np.ones((7, 7), np.uint8)  
    img_erosin = cv2.erode(img, kerne1, iterations=1)
    
    #图像相与  
    #img_bit = cv2.bitwise_and(img, img, mask=img_erosin)
    #ret, img_threshold = cv2.threshold(img_erosin, 5, 250, cv2.THRESH_BINARY)  # 二值化   
    #img_bit= cv2.cvtColor(img_threshold, cv2.COLOR_BGR2GRAY)

    #再次中值滤波
    midFilter= cv2.medianBlur(img_erosin, 5)
    
    #固定二值化
    ret, binImg = cv2.threshold(midFilter, 130, 255, cv2.THRESH_BINARY)
    #cv2.imshow("img_erosin and Noise removal", binImg)
    
    #其他核的腐蚀膨胀
#     kerne3 = np.ones((51, 51), np.uint8)  
#     img_erosin1 = cv2.erode(img, kerne3, iterations=1)  
#     cv2.imshow("dil", img_erosin1)
#     kerne2 = np.ones((2, 2), np.uint8)  
#     img_dilation = cv2.dilate(img, kerne2, iterations=1)
#     cv2.imshow("ers",img_dilation)
    
    #通过连续腐蚀和膨胀，来降低噪声
#     kerne3 = np.ones((7, 7), np.uint8)  
#     img_dilation1 = cv2.dilate(binImg,kerne3,iterations=1)
#     cv2.imshow("ers",img_dilation1)
    
    return binImg;


#https://www.cnblogs.com/llfisher/p/6557611.html
#https://www.cnblogs.com/nanyangzp/p/3496486.html
#偏心率：以质心为中心，所有点到X轴的长度综合，相比Y周的长度总和，他们之间的比值。
#圆形=1，长条就是斜率
# E = (M20-M02+4M11)/A, Mjk = EE(x-xA)^j * (y-yA)^k, (j+k阶矩)，A为面积
#http://wenku.baidu.com/link?url=4ZSLxGBKE3LBf2mdxDs0VJ1cjJ3hxqeORu-3mfXO23gGBqf5LyjqZ4AHFCMLeP32xEKkoj5tPsWHdvA2ovmuKiRDKN6YHFO9G7JOzBWWrMC

#http://blog.csdn.net/app_12062011/article/details/51953030
#E = sqrt(1-I^2)
#I = (u20+u02-sqrt(4u11*u11(u20-u02)*(u20-u02))/(u20+u02+sqrt(4u11*u11(u20-u02)*(u20-u02))
def func_vision_worm_find_contours(nfImg, orgImg):
    #找到轮廓
    _, contours, hierarchy = cv2.findContours(nfImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #RETR_TREE, RETR_CCOMP
    #contours = contours[0] if imutils.is_cv2() else contours[1]
    
    #绘制轮廓
    #cv2.drawContours(orgImg, contours, -1, (0,0,255), 1)
    #cv2.imshow("contours marked image", orgImg)

    #输出图形
    outputImg = cv2.cvtColor(nfImg, cv2.COLOR_GRAY2BGR)
    outputSta = {'totalNbr':0, 'bigAlive':0, 'bigDead':0, 'middleAlive':0, 'middleDead':0, 'smallAlive':0, 'smallDead':0, 'totalAlive':0, 'totalDead':0}
#     outputImg = np.zeros(orgImg.shape, np.uint8)
#     outputImg = cv2.cvtColor(outputImg, cv2.COLOR_BGR2GRAY)
#     ret, outputImg = cv2.threshold(outputImg, 130, 255, cv2.THRESH_BINARY_INV)
#     outputImg = cv2.cvtColor(outputImg, cv2.COLOR_GRAY2BGR)
    mask = np.zeros((orgImg.shape[0]+2, orgImg.shape[1]+2), np.uint8)
    mask[:] = 1
    #分别分析
    for c in contours:
        #外矩形框
        (x,y,w,h)=cv2.boundingRect(c)
        pointx=x+w/2
        pointy=y+h/2
        # compute the center of the contour
        M = cv2.moments(c)
        cX = int(M["m10"] / (M["m00"]+0.01))
        cY = int(M["m01"] / (M["m00"]+0.01))
        seed_point = (cX, cY)
        #轮廓面积
        cArea = cv2.contourArea(c)
        #轮廓弧长
        cPerimeter = cv2.arcLength(c,True)
        
        #第一种传统计算偏心率：数值无限大，不靠谱
        #E = (M20-M02+4M11)/A
        #cE = float((M["m20"] - M["m02"] + 4.0 * M["m11"]) / (M["m00"]+0.01))
        #I = (u20+u02-sqrt(4u11*u11(u20-u02)*(u20-u02))/(u20+u02+sqrt(4u11*u11(u20-u02)*(u20-u02))
        
        #第二种计算偏心率：使用更复杂的工具，依然不行
#         u20 = M["m20"]
#         u02 = M["m02"]
#         u11 = M["m11"]
#         up = u20+u02
#         um = u20-u02
#         cI = (up- math.sqrt(4*u11*u11 + up*up))/(up + math.sqrt(4*u11*u11 + up*up) + 0.01)
#         cE = math.sqrt(1-cI*cI)
        
        #第三种近似方式，采用面积和周长的比值：强多了，但依然不能很准确的界定
        #cE = cPerimeter / math.sqrt(cArea+0.01) / (2*math.sqrt(3.14))
        
        #第四种方法：
        rect = cv2.minAreaRect(c)
        # 长宽,总有 width>=height  
        width, height = rect[1]
        if (width > height):
            cE = height / width
        else:
            cE = width / height
        cE = round(cE, 2)
        #判定大小
#         if cArea < 400: 
#             pass
#         else:
#             # draw the contour and center of the shape on the image
#             cv2.drawContours(outputImg, [c], -1, (0, 0, 255), 1)
#             cv2.circle(outputImg, (cX, cY), 2, (0, 255, 0), -1)
#             #cv2.putText(orgImg, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        #最终决定不采用flood算法
        if cArea < 600:
            pass
        elif cArea <1500:
            outputSta['totalNbr'] +=1
            #cv2.floodFill(outputImg, mask, seed_point,(0,0,255))
            cv2.drawContours(outputImg, c, -1, (0,0,255), 2)  
            if (cE < 0.5):
                outputSta['smallDead'] +=1
                outputSta['totalDead'] +=1
            else:
                outputSta['smallAlive'] +=1
                outputSta['totalAlive'] +=1               
            cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        elif cArea < 2500:
            outputSta['totalNbr'] +=1
            #cv2.floodFill(outputImg, mask, seed_point,(0,255,0))  
            cv2.drawContours(outputImg, c, -1, (0,255,0), 2)
            if (cE < 0.5):
                outputSta['middleDead'] +=1
                outputSta['totalDead'] +=1
            else:
                outputSta['middleAlive'] +=1
                outputSta['totalAlive'] +=1            
            cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        elif cArea < 5000:
            outputSta['totalNbr'] +=1
            #cv2.floodFill(outputImg, mask, seed_point,(255,0,0))  
            cv2.drawContours(outputImg, c, -1, (255,0,0), 2)
            if (cE < 0.5):
                outputSta['bigDead'] +=1
                outputSta['totalDead'] +=1
            else:
                outputSta['bigAlive'] +=1
                outputSta['totalAlive'] +=1                        
            cv2.putText(outputImg, str(cE), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(outputImg, str(outputSta), (10, 30), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Final output", outputImg)
    
    return outputImg;


def Preprocessing_find_coin_edge(img):
    #硬币求边缘
    #http://www.jianshu.com/p/de81d6029235
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #thresh = func_vision_worm_binvalue_test(img)
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
    cv2.imshow('Noise Removal', opening)
    cv2.waitKey(0)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    cv2.imshow('sure background area', sure_bg)
    cv2.waitKey(0)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    cv2.imshow('Finding sure foreground area', sure_fg)
    cv2.waitKey(0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    cv2.imshow('Finding unknown region', unknown)
    cv2.waitKey(0)
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    cv2.imshow('Marker labelling', markers)
    cv2.waitKey(0)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown==255]=0
    cv2.imshow('Final Result', markers)
    cv2.waitKey(0)




lowThreshold = 0
max_lowThreshold = 100
ratio = 3   
kernel_size = 5

def CannyThreshold(img, lowThreshold, gray):

    detected_edges = cv2.GaussianBlur(gray,(7,7),0)    
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold*ratio,  apertureSize = kernel_size)    
    dst = cv2.bitwise_and(img, img, mask = detected_edges)  # just add some colours to edges from original image.    
    cv2.imshow('canny demo',dst)
    cv2.waitKey(0)


def Canny_test(img):
    #cv2.namedWindow('input image',cv2.WINDOW_AUTOSIZE)
    #cv2.imshow('input image', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    ''' 
    cv2.Canny(image,threshold1 , threshold2[,edges]) 
    作用：根据Canny算法检测边界 
    threshold1:minVal，threshold2：maxVal 
    edges:设置卷积核的大小,L2gradient:默认使用近似值来代替所求的梯度 
    
    '''  
    #方法1
    img = cv2.GaussianBlur(img,(3,3),0) #高斯平滑处理原图像降噪
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = img
    #cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)    
    CannyThreshold(img, 8, gray)  # initialization
    
    #方法２
#     edges = cv2.Canny(img , 0 , 100)
#     plt.subplot(1,2,1) , plt.imshow(img , cmap="gray")  
#     plt.title("Original") , plt.xticks([]) , plt.yticks([])  
#     plt.subplot(1,2,2), plt.imshow(edges , cmap="gray")  
#     plt.title("Cannt") , plt.xticks([])  ,plt.yticks([])  
#     plt.show()

def Laplance_test(img):
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(img,cv2.CV_64F)#拉普拉斯边缘检测
    lap = np.uint8(np.absolute(lap))##对lap去绝对值
    cv2.imshow("Laplacian",lap)
    cv2.waitKey()
    
def Sobel_test(img):
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Sobel边缘检测
    sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)#x方向的梯度
    sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)#y方向的梯度
    
    sobelX = np.uint8(np.absolute(sobelX))#x方向梯度的绝对值
    sobelY = np.uint8(np.absolute(sobelY))#y方向梯度的绝对值
    
    sobelCombined = cv2.bitwise_or(sobelX,sobelY)#
    #cv2.imshow("Sobel X", sobelX)
    #cv2.waitKey()
    #cv2.imshow("Sobel Y", sobelY)
    #cv2.waitKey()
    cv2.imshow("Sobel Combined", sobelCombined)
    cv2.waitKey()
    return sobelCombined

def kmeans_test(img):
    plt.subplot(121)
    plt.imshow(img, 'gray')
    plt.title('original')
    plt.xticks([]),plt.yticks([])
    cv2.waitKey(0)
     
    #change img(2D) to 1D
    img1 = img.reshape((img.shape[0]*img.shape[1],1))
    img1 = np.float32(img1)
    
    #define criteria = (type,max_iter,epsilon)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    
    #set flags: hou to choose the initial center
    #---cv2.KMEANS_PP_CENTERS ; cv2.KMEANS_RANDOM_CENTERS
    flags = cv2.KMEANS_RANDOM_CENTERS
    # apply kmenas
    compactness,labels,centers = cv2.kmeans(img1,4,None,criteria,10,flags)
    
    img2 = labels.reshape((img.shape[0],img.shape[1]))
    plt.subplot(122),plt.imshow(img2,'gray'),plt.title('kmeans')
    plt.xticks([]),plt.yticks([])
    cv2.waitKey(0)

def Preprocessing_find_mouse_edge(img):
    #http://www.jb51.net/article/122475.htm
    #寻找鼠标边缘
    height, width = img.shape[:2]
    ratio = 0.5
    res = cv2.resize(img, (int(ratio*width), int(ratio*height)), interpolation = cv2.INTER_CUBIC)    
    blured = cv2.blur(res,(5,5))    #进行滤波去掉噪声
    #cv2.imshow("Blur", blured)     #显示低通滤波后的图像
    #cv2.waitKey(0)
    gray = cv2.cvtColor(blured,cv2.COLOR_BGR2GRAY) 
    #cv2.imshow("gray", gray)
    #cv2.waitKey(0)
    #定义结构元素 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(20, 20))
    #开闭运算，先开运算去除背景噪声，再继续闭运算填充目标内的孔洞
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel) 
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel) 
    #cv2.imshow("closed", closed)
    #cv2.waitKey(0)
    #二值运算
    #binary = cv2.adaptiveThreshold(closed, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 11)   # ADAPTIVE_THRESH_MEAN_C ADAPTIVE_THRESH_GAUSSIAN_C
    #求二值图
    ret, binary = cv2.threshold(closed,250,255,cv2.THRESH_BINARY) 
    #cv2.imshow("result", binary)
    #cv2.waitKey(0)
    #找到轮廓
    _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    #绘制轮廓
    cv2.drawContours(res,contours,-1,(0,0,255),3) 
    #绘制结果
    cv2.imshow("result", res)
    cv2.waitKey(0)

def func_vision_worm_clasification(batch):
    #img=cv2.imread("./2.jpg", 0)
    inImgFile = "8.jpg"
    orgImg=cv2.imread(inImgFile)
    #Original_test(img)
    #img = Preprocessing_resize_test(orgImg);
    #Canny_test(img)
    #Laplance_test(img)
    #img = Sobel_test(img)
    #kmeans_test(img)
    #Preprocessing_find_coin_edge(img)
    #Preprocessing_find_mouse_edge(img)
    binImg = func_vision_worm_binvalue_test(orgImg)
    nfImg = func_vision_worm_remove_noise_test(binImg)
    conImg = func_vision_worm_find_contours(nfImg, orgImg)
    cv2.imwrite("result_"+inImgFile, conImg)
    # 打开一个文件
    f = open("worm_clas.txt", "a+")
    a = '%s, caculated one time, save new file = result_%s.\n' % (time.asctime(), inImgFile)
    f.write(a)
    # 关闭打开的文件
    f.close()
    if ("batch" in batch):
        cv2.destroyAllWindows()
    else:
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#总入口
if __name__ == "__main__":
    func_vision_worm_clasification("no");  #"batch" or "no"












