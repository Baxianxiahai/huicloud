'''
Created on 2018/4/30

@author: ZHANG JL
'''

#!/opt/bin/python3.6
# -*- coding: UTF-8 -*-

import datetime
import string
import sys
import time
import json
import os
import re
import socket
import ctypes 
import re
import random
import cv2 as cv
import numpy as np  
#import matplotlib.pyplot as plt
#import imutils
from ctypes import c_uint8
#import argparse
#import math


#SYSTEM ENTRY
if __name__ == '__main__':
    print("[HELLO2MAIN] ", time.asctime(), ", Starting...\n" );
    # 选取摄像头，0为笔记本内置的摄像头，1,2···为外接的摄像头**
    cap = cv.VideoCapture(0)#括号里的数和ls /dev/video*　结果有关
    #定义摄像头的分辨率
    cap.set(4,720)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    #大量的错和坑出现在这里
    #第一个参数是路径和文件名
    #第二个参数是视频格式，“MPEG”是一**种标准格式，百度fourcc可见各种格式
    #第二个参数（fourcc）如果设置为-1，允许实时选择视频格式
    #fourcc = cv.VideoWriter_fourcc(*"MPEG")
    #fourcc=-1**
    # 第三个参数则是镜头快慢的，20为正常，小于二十为慢镜头**
    #out = cv.VideoWriter('c://output.avi',fourcc,20,(640,480))
    
    while True:
        time.sleep(1)
        ret, frame = cap.read()
        if (ret == True):
            frame = cv.flip(frame, 1)# 在帧上进行操作
            frame = cv.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv.INTER_AREA)
            cv.imshow('Input', frame)
            picName = "CEBS采样" + str(time.asctime()) + ".jpg"
            cv.imwrite(picName, frame) #13
            c = cv.waitKey(1)
            if c == 27:
                break
    cap.release()
    cv.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    