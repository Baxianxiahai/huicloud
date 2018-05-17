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

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

#Local include
from cebsMain import *
from PkgCebsHandler import ModCebsCom
from PkgCebsHandler import ModCebsCfg
from PkgCebsHandler import ModCebsVision
from PkgCebsHandler import ModCebsMoto
#from form_qt.cebsmainform import Ui_cebsMainWindow

class classCtrlThread(QThread):
    signal_print_log = pyqtSignal(str) #申明信号
    signal_ctrl_start = pyqtSignal() #申明给主函数使用
    signal_ctrl_stop = pyqtSignal()  #申明给主函数使用
    signal_ctrl_zero = pyqtSignal()  #申明给主函数使用
    signal_cala_pilot = pyqtSignal() #申明给主函数使用
    signal_cala_comp = pyqtSignal()  #申明给主函数使用

    def __init__(self,parent=None):
        super(classCtrlThread,self).__init__(parent)
        self.identity = None;
        self.times = 0;
        self.objInitCfg=ModCebsCfg.ConfigOpr();
        self.objMoto=ModCebsMoto.classMotoProcess();
        
        #初始化不同目标板子的数量
        if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_BATCH_MAX;
        else:
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_BATCH_MAX;
        
        #启动第三个干活的子进程
        self.threadMotoPilot = ModCebsMoto.classCalaPilotThread()
        self.threadMotoPilot.setIdentity("CalaPilotThread")
        self.threadMotoPilot.signal_print_log.connect(self.transferLogTrace) #接收信号
        self.threadMotoPilot.signal_moto_pilot.connect(self.threadMotoPilot.funcMotoCalaPilotSart) #发送信号
        self.threadMotoPilot.start();
        
    def setIdentity(self,text):
        self.identity = text

    def setTakePicWorkRemainNumber(self, val):
        self.times = int(val)
    
    def transferLogTrace(self, string):
        self.signal_print_log.emit(string)
        
    #拍照
    def funcTakePicStart(self):
        #停止后强制摄像头归零
        if (self.objMoto.funcMotoMove2Start() < 0):
            self.signal_print_log.emit("马达移动错误！")
            return -1;
        self.times = ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH;
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = False;
        self.signal_print_log.emit("启动拍照： 拍照次数=%d." %(self.times))
        self.objInitCfg.createBatch(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX);

    #停止拍照
    def funcTakePicStop(self):
        self.times = 0
        self.signal_print_log.emit("停止拍照，剩余次数=%d." %(self.times))
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
        ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;
        self.objInitCfg.updateCtrlCntInfo();
        #停止后强制摄像头归零
        if (self.objMoto.funcMotoBackZero() < 0):
            self.signal_print_log.emit("系统归位错误！")
            return -1;
        #self.objMoto.funcMotoStop();

    #托盘四周巡游
    def funcCalaPilotStart(self):
        self.signal_print_log.emit("系统校准巡视开始...")
        self.threadMotoPilot.signal_moto_pilot.emit()
        
#         if (self.objMoto.funcMotoCalaPilot() < 0):
#             self.signal_print_log.emit("系统巡视错误！")
#             ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True # 让继续做图像识别
#             return -1;
#         else:
#             self.signal_print_log.emit("系统校准巡视成功结束!")
#             ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True # 让继续做图像识别
    
    
    #托盘归位到初始态
    def funcCtrlMotoBackZero(self):
        self.signal_print_log.emit("马达位置归零...")
        if (self.objMoto.funcMotoBackZero() < 0):
            self.signal_print_log.emit("系统归位错误！")
            return -1;

    #处理校准过程完成的动作
    def funcCtrlCalaComp(self):
        #更新系统级参数
        if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 12;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 8;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 8;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 6;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 8;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 4;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 4;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 3;
        else:
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = 12;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = 8;
        ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = (ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[0]) / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
        ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = (ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[3]) / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
        #控制比特位
        ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA = False;
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True; # 让继续做图像识别
    
    #本地函数    
    def funcCameraCapture(self):
        obj = ModCebsVision.classVisionProcess()
        obj.funcVisionCapture(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX, self.times);
        print("PIC: Taking picture once! Index =%d" % (self.times));
        self.objInitCfg.addBatchFile(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX, self.times)
        #提前移动到下一个干活的位置
        nextOne = ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH - self.times + 2;
        #如果已经是最后一个位置，则归位到零位
        if (nextOne <= ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH):
            if (self.objMoto.funcMotoMove2HoleNbr(nextOne) < 0):
                self.signal_print_log.emit("马达移动错误！")
                return -1;
        else:
            if (self.objMoto.funcMotoBackZero() < 0):
                self.signal_print_log.emit("系统归位错误！")
                return -2;
        
    def run(self):
        while True:
            time.sleep(1)
            if (self.times > 0):
                self.signal_print_log.emit(str("拍照进行时：当前剩余次数=" + str(self.times)))
                self.funcCameraCapture();
                self.times -= 1;
                ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT += 1;
                #控制停止的所作所为
                if (self.times == 0):
                    ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;
                    ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
                    self.objInitCfg.updateCtrlCntInfo();
        
        
        