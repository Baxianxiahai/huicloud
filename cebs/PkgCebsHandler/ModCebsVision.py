'''
Created on 2018年5月4日

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
from form_qt.cebsmainform import Ui_cebsMainWindow

#主处理任务模块
class classVisionThread(QThread):
    signal_print_log = pyqtSignal(str)
    signal_start = pyqtSignal()
    signal_stop = pyqtSignal()

    def __init__(self,parent=None):
        super(classVisionThread,self).__init__(parent)
        self.identity = None;
        
    def setIdentity(self,text):
        self.identity = text

    def funcVisionProc(self):
        self.signal_print_log.emit("图片识别完成： 还剩照片数量=%d." %(ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT))
        time.sleep(random.random()*10)
        ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT -= 1;
        
    def run(self):
        while True:
            time.sleep(1)
            if ((ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT > 0) and (ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG == True)):
                self.funcVisionProc();
        
        
        
        