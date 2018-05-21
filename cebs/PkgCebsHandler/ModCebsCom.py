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
GL_CEBS_PIC_PROC_BATCH_INDEX = 0;
GL_CEBS_PIC_PROC_CLAS_INDEX = 0;  #识别到哪一种类别
GL_CEBS_PIC_PROC_REMAIN_CNT = 0;
GL_CEBS_PIC_CLAS_FLAG = False;  #True表示可以做图像识别
GL_CEBS_CFG_FILE_NAME = r"cebsConfig.ini";
GL_CEBS_PIC_ORIGIN_PATH = r"pic_origin";
GL_CEBS_PIC_MIDDLE_PATH = r"pic_middle";
GL_CEBS_PIC_ABS_ORIGIN_PATH = "";
GL_CEBS_PIC_ABS_MIDDLE_PATH = "";
GL_CEBS_PILOT_WOKING_ROUNDS_MAX = 5;

#控制坐标轴及方向
GL_CEBS_HB_TARGET_BOARD_X_MAX = 120000;
GL_CEBS_HB_TARGET_BOARD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_BOARD_BATCH_MAX = 96;
GL_CEBS_HB_TARGET_96_STANDARD = "96_STANDARD";
GL_CEBS_HB_TARGET_96_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_96_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_96_SD_BATCH_MAX = 96;
GL_CEBS_HB_TARGET_48_STANDARD = "48_STANDARD";
GL_CEBS_HB_TARGET_48_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_48_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_48_SD_BATCH_MAX = 48;
GL_CEBS_HB_TARGET_32_STANDARD = "32_STANDARD";
GL_CEBS_HB_TARGET_32_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_32_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_32_SD_BATCH_MAX = 32;
GL_CEBS_HB_TARGET_12_STANDARD = "12_STANDARD";
GL_CEBS_HB_TARGET_12_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_12_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_12_SD_BATCH_MAX = 12;
#实际选择
GL_CEBS_HB_TARGET_TYPE = GL_CEBS_HB_TARGET_96_STANDARD;
GL_CEBS_PIC_ONE_WHOLE_BATCH = GL_CEBS_HB_TARGET_96_SD_BATCH_MAX;
GL_CEBS_HB_HOLE_X_NUM = 0;          #板孔有多少个，X方向
GL_CEBS_HB_HOLE_Y_NUM = 0;          #板孔有多少个，Y方向
GL_CEBS_HB_WIDTH_X_SCALE = 0;       #板孔单个间距有多长，X方向
GL_CEBS_HB_HEIGHT_Y_SCALE = 0;      #板孔单个间距有多长，Y方向
GL_CEBS_HB_POS_IN_UM = [0, 0, 0, 0];  #使用整数表达，um精度，96孔板子的左上右下坐标位置，X1/Y1, X2/Y2
GL_CEBS_CUR_POS_IN_UM = [0, 0];  #使用整数表达，um精度，标识X/Y坐标


