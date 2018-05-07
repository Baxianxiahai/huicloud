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
#from form_qt.cebsmainform import Ui_cebsMainWindow


#Entry Processing
#class ClassHandler(object):
class ClassHandler(QtWidgets.QMainWindow, Ui_cebsMainWindow):
    signal_my_print_trigger = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(ClassHandler, self).__init__()
        self.signal_my_print_trigger.connect(cebsMainWindow.slot_print_trigger)
        pass

    def func_ctrl_start(self):
        try:
            res = {}
            res['res'] = 1;
            res['value'] = 33;
        except Exception as err:  
            print("Exec Err: func_ctrl_start!" + str(err))
            return ("Exec Err: func_ctrl_start!" + str(err))
        finally:
            #obj = cebsMainWindow();
            #obj.cebs_print_log("CTRL: This is a test!")
            #self.signal_my_print_trigger.emit("This is a test!");
            return res;
        
    def func_ctrl_stop(self):
        try:
            res = {}
            res['res'] = 2;
            res['value'] = 44;
        except Exception as err:  
            print("Exec Err: func_ctrl_stop!" + str(err))
            return ("Exec Err: func_ctrl_stop!" + str(err))
        finally:
            return res;        
        
        
class classCtrlThread(QThread):
    #sinOut = pyqtSignal(str)
    signal_print_log = pyqtSignal(str)
    signal_start = pyqtSignal()
    signal_stop = pyqtSignal()

    def __init__(self,parent=None):
        super(classCtrlThread,self).__init__(parent)
        self.identity = None;
        self.times = 0;
        self.objInitCfg=ModCebsCfg.ConfigOpr();
        
    def setIdentity(self,text):
        self.identity = text

    def setVal(self,val):
        self.times = int(val)

    def funcStart(self):
        ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX += 1;
        self.times = ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH;
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = False;
        self.signal_print_log.emit("启动拍照： 拍照次数=%d." %(self.times))
        self.objInitCfg.createBatch(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX);

    def funcStop(self):
        self.times = 0
        self.signal_print_log.emit("停止拍照，剩余次数=%d." %(self.times))
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
        self.objInitCfg.updateCtrlCntInfo();
        ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;
        
    def funcCapture(self):
        self.objInitCfg.addBatchFile(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX, self.times)
        pass

    def run(self):
        while True:
            time.sleep(1)
            if (self.times > 0):
                #self.signal_print_log.emit(str(self.identity + "==>" + str(self.times)))
                self.signal_print_log.emit(str("拍照进行时：当前剩余次数=" + str(self.times)))
                self.funcCapture()
                self.times -= 1
                ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT += 1;
                #控制停止的所作所为
                if (self.times == 0):
                    ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX +=1;

        
        
        