'''
Created on 2018年5月2日

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket



#Gllbal set data
GL_CEBS_PIC_PROC_REMAIN_CNT = 0;
GL_CEBS_PIC_PROC_CTRL_FLAG = True;  #True表示可以做图像识别
GL_CEBS_CFG_FILE_NAME = r"cebsConfig.ini";


#以下变量暂时未使用
GL_CEBS_SPS_READ_VALUE = 0;
GL_CEBS_RFID_READ_VALUE = 0;



class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        