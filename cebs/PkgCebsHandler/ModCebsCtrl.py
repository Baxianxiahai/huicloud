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
    #sinOut = pyqtSignal(str)
    signal_print_log = pyqtSignal(str)
    signal_start = pyqtSignal()
    signal_stop = pyqtSignal()
    signal_zero = pyqtSignal()
    signal_cala = pyqtSignal()

    def __init__(self,parent=None):
        super(classCtrlThread,self).__init__(parent)
        self.identity = None;
        self.times = 0;
        self.objInitCfg=ModCebsCfg.ConfigOpr();
        self.objMoto=ModCebsMoto.classMotoProcess();
        
    def setIdentity(self,text):
        self.identity = text

    def setVal(self,val):
        self.times = int(val)

    def funcStart(self):
        self.times = ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH;
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = False;
        self.signal_print_log.emit("启动拍照： 拍照次数=%d." %(self.times))
        self.objInitCfg.createBatch(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX);
        self.objMoto.funcMotoMove2Start();

    def funcStop(self):
        self.times = 0
        self.signal_print_log.emit("停止拍照，剩余次数=%d." %(self.times))
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
        ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;
        self.objInitCfg.updateCtrlCntInfo();
        self.objMoto.funcMotoStop();

    def funcCala(self):
        self.signal_print_log.emit("系统校准开始...")
        self.objMoto.funcMotoCalaRun();

    def funcZero(self):
        self.signal_print_log.emit("马达位置归零...")
        self.objMoto.funcMotoBackZero();
        
    def funcCapture(self):
        obj = ModCebsVision.classVisionProcess()
        obj.funcVisionCapture(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX, self.times);
        self.objInitCfg.addBatchFile(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX, self.times)
        self.objMoto.funcMotoMove2Next();
        
    def run(self):
        while True:
            time.sleep(1)
            if (self.times > 0):
                self.signal_print_log.emit(str("拍照进行时：当前剩余次数=" + str(self.times)))
                self.funcCapture();
                self.times -= 1;
                ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT += 1;
                #控制停止的所作所为
                if (self.times == 0):
                    ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;
                    ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
                    self.objInitCfg.updateCtrlCntInfo();
        
        
        