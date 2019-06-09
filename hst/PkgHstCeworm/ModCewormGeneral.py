'''
Created on 2019年2月1日

@author: Administrator
'''

from ctypes import c_uint8
import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  
import imutils
import cv2
import argparse

class ClassModCewormTest1():
    '''
    classdocs
    '''
    
    HST_VIDEO_WORM_CALCULATION_pic_sta_output = {'totalNbr':0, 'bigAlive':0, 'bigDead':0, 'middleAlive':0, 'middleDead':0, 'smallAlive':0, 'smallDead':0, 'totalAlive':0, 'totalDead':0}
    
    def __init__(self):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, inputData):
        print(inputData,inputData['cmd'],inputData['data']['file_name'])
#         video_file="d:\\Video\A1.mp4"
        video_file=inputData['data']['file_name']
        # 创建参数解析器并解析参数，通过命令行的方式进行调用的时候可以序列化参数
#         ap = argparse.ArgumentParser()
#         ap.add_argument("-v", "--video", help="path of the video")
#         # 待检测目标的最小面积，该值需根据实际应用情况进行调整(原文为500)
#         ap.add_argument("-a", "--min-area", type=int, default=2000, help="minimum area size")
#         args = vars(ap.parse_args())    #@
#          
#         # 如果video参数为空，则从自带摄像头获取数据
#         if args.get("video") == None:
#             camera = cv2.VideoCapture(0)
#         # 否则读取指定的视频
#         else:
#             camera = cv2.VideoCapture(args["video"])
        
        camera = cv2.VideoCapture(video_file)
        #"D:\opencv_proj\A1.mp4")
        # 开始之前先暂停一下,以便跑路(离开本本摄像头拍摄区域^_^)
        print("Ready?")
        time.sleep(1)
        print("Action!")
        
        # 初始化视频第一帧
        firstRet, firstFrame = camera.read()
        if not firstRet:
            print("Load video error!")
            exit(0)
        
        # 对第一帧进行预处理
        firstFrame = imutils.resize(firstFrame, width=500)  # 尺寸缩放，width=500
        gray_firstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY) # 灰度化
        firstFrame = cv2.GaussianBlur(gray_firstFrame, (21, 21), 0) #高斯模糊，用于去噪   
        
        # 遍历视频的每一帧
        max_worm_num = 0 
        while True:
            (ret, frame) = camera.read()
            # 如果没有获取到数据，则结束循环
            if not ret:
                break
            # 对获取到的数据进行预处理
            frame = imutils.resize(frame, width=500)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)  #'''(21, 21)需要输入的参数'''
            # cv2.imshow('video', firstFrame)
            # 计算第一帧和其他帧的差别
            frameDiff = cv2.absdiff(firstFrame, gray_frame)
            # 忽略较小的差别
            #retVal, thresh = cv2.threshold(frameDiff, 25, 255, cv2.THRESH_BINARY)
            retVal, thresh = cv2.threshold(frameDiff, 10, 255, cv2.THRESH_BINARY) #10需要配置的参数
        
            # 对阈值图像进行填充补洞
        #    thresh = cv2.dilate(thresh, None, iterations=2)
            image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
            text = "caculating..."
            worm_cnt = 0
            # 遍历轮廓
            for contour in contours:
                # if contour is too small, just ignore it
        #        if cv2.contourArea(contour) < args["min_area"]:
                if cv2.contourArea(contour) < 15:  #15 需要配置的参数
                    continue
        
                # 计算最小外接矩形（非旋转）
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                #text = len(contours)
                worm_cnt = worm_cnt+1 
            if max_worm_num < worm_cnt:
                max_worm_num = worm_cnt   
            cv2.putText(frame, "MAX number: {}    Dynamic count number: {}".format(max_worm_num,worm_cnt), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
            cv2.imshow('frame', frame)
            cv2.imshow('thresh', thresh)
            cv2.imshow('frameDiff', frameDiff)
            # 处理按键效果
            key = cv2.waitKey(60) & 0xff
            if key == 27:   # 按下ESC时，退出
                break
            elif key == ord(' '):   # 按下空格键时，暂停
                cv2.waitKey(0)
        
        # 释放资源并关闭所有窗口
        camera.release()
        cv2.destroyAllWindows()
        self.HST_VIDEO_WORM_CALCULATION_pic_sta_output['totalNbr']=max_worm_num
        return self.HST_VIDEO_WORM_CALCULATION_pic_sta_output


    
    


    






















        
    