'''
Created on 2018年5月8日

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

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

#Local include
from cebsMain import *
from PkgCebsHandler import ModCebsCom
from PkgCebsHandler import ModCebsCfg

#校准巡视独立的线程
class classCalaPilotThread(QThread):
    signal_print_log = pyqtSignal(str) #申明信号
    signal_moto_pilot = pyqtSignal() #申明给CebsCtrl启动本任务功能的信号

    def __init__(self,parent=None):
        super(classCalaPilotThread,self).__init__(parent)
        self.identity = None;
        self.cntCtrl = 0;
        self.objMotoProc = classMotoProcess();

    def setIdentity(self,text):
        self.identity = text

    def funcMotoCalaPilotSart(self):
        self.cntCtrl = ModCebsCom.GL_CEBS_PILOT_WOKING_ROUNDS_MAX+1;

    def funcMotoCalaPilotWorkingOnces(self):
        #移动到左上
        self.objMotoProc.funcMotoMove2HoleNbr(1);
        #移动到右上
        self.objMotoProc.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_HOLE_X_NUM);
        #移动到左下
        self.objMotoProc.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX - ModCebsCom.GL_CEBS_HB_HOLE_X_NUM + 1);
        #移动到右下
        self.objMotoProc.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX);
                
    def run(self):
        while True:
            time.sleep(1)
            self.cntCtrl -= 1;
            if (self.cntCtrl > 1):
                self.signal_print_log.emit("MOTO: Running Calibration pilot process! roundIndex = %d" % (self.cntCtrl))
                self.funcMotoCalaPilotWorkingOnces();
            elif (self.cntCtrl == 1):
                self.signal_print_log.emit("MOTO: Running Calibration pilot process! roundIndex = %d" % (self.cntCtrl))
                self.funcMotoCalaPilotWorkingOnces();
                ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True #让继续做图像识别    




#约定移动的孔板位置使用： 0 =》 表示复位位置
#               1-96 =》正常的板孔位置
class classMotoProcess(object):
    def __init__(self):
        #先计算基础部分
        if (ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE == 0 or ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE == 0 or ModCebsCom.GL_CEBS_HB_HOLE_X_NUM == 0 or ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM == 0):
            if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 12;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 8;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 8;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 6;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 8;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 4;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 4;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 3;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            else:
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 12;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 8;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
        #再考虑真实情况下的覆盖
        #真正的校准在校准过程中进行更新
        if (ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[3] !=0):
            xWidth = ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[0];
            yHeight = ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[3];
            ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = xWidth / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
            ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = yHeight / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
        else:
            pass
         
    def funcMotoCalaMoveOneStep(self, scale, dir):
        if (scale == 1):
            actualScale = 500;
        elif (scale == 2):
            actualScale = 1000;
        elif (scale == 3):
            actualScale = 5000;
        elif (scale == 4):
            actualScale = 10000;
        elif (scale == 5):
            actualScale = 50000;
        else:
            actualScale = 0;
        if (dir == 1):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] += actualScale;
            if ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_32_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX;
            elif (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_BOARD_Y_MAX):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_Y_MAX;
            else:
                pass
        elif (dir == 2):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] -= actualScale;
            if (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] < 0):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = 0;
        elif (dir == 3):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] -= actualScale;
            if (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] < 0):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = 0;
        elif (dir == 4):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] += actualScale;
            if ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_32_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX;
            elif (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_BOARD_X_MAX):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_X_MAX;
            else:
                pass
        else:
            pass
        print("MOTO: Moving one step! Scale=%d, Dir=%d. New pos X/Y=%d/%d" % (scale, dir, ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1]));
        return 1;
    
    def funcMotoBackZero(self):
        return self.funcMotoMove2HoleNbr(0);
        #print("MOTO: Running Zero Position!")

    def funcMotoMove2Start(self):
        #注意：左上的X轴最小、Y最大。右下的X最大，而Y小
        xWidth = ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[0];
        yHeight = ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[3];
        if (xWidth <= 0 or yHeight <= 0):
            print("MOTO: Error set of calibration, xWidth/yHeight=%d/%d!" %(xWidth, yHeight))
            return -1;
        return self.funcMotoMove2HoleNbr(1);
        #print("MOTO: Running Start Position!")

    def funcMotoMove2HoleNbr(self, holeIndex):
        time.sleep(1)
        #计算新的目标位置
        if (holeIndex == 0):
            xTargetHoleNbr = 0;
            yTargetHoleNbr = 0;
            newPosX = 0;
            newPosY = 0;
        else:
            #行（1-12）, 列（1-8）
            xTargetHoleNbr = ((holeIndex-1) % ModCebsCom.GL_CEBS_HB_HOLE_X_NUM) + 1;
            yTargetHoleNbr = ((holeIndex-1) // ModCebsCom.GL_CEBS_HB_HOLE_X_NUM) + 1;
            newPosX = int(ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] + (xTargetHoleNbr-1)*ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE);
            newPosY = int(ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - (yTargetHoleNbr-1)*ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE);
        print("MOTO: Moving to working hole=%d, newPosX/Y=%d/%d." % (holeIndex, newPosX, newPosY))
        #真实移动过程
        if (self.funcMotoMove2AxisPos(ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], newPosX, newPosY) > 0):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = newPosX;
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = newPosY;
            return 1;
        else:
            return -2;

#     #四周巡视
#     def funcMotoCalaPilot(self):
#         for roundIndex in range (0, ModCebsCom.GL_CEBS_PILOT_WOKING_ROUNDS_MAX):
#             print("MOTO: Running Calibration pilot process! roundIndex = %d" % (roundIndex))
#             #移动到左上
#             self.funcMotoMove2HoleNbr(1);
#             #移动到右上
#             self.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_HOLE_X_NUM);
#             #移动到左下
#             self.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX - ModCebsCom.GL_CEBS_HB_HOLE_X_NUM + 1);
#             #移动到右下
#             self.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX);
#         return 1;

    #暂时不需要的过程
    def funcMotoStop(self):
        print("MOTO: Stop!")
        return 1;
    
    #暂时不需要的过程
    def funcMotoResume(self):
        print("MOTO: Resume action!")
        return 1;
    
    #从当前一个坐标移动到另一个新坐标
    #需要将坐标转换为脉冲数
    def funcMotoMove2AxisPos(self, curPx, curPy, newPx, newPy):
        return 1;
    




        