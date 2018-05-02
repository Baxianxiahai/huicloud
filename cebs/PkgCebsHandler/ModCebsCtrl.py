'''
Created on 2018年5月2日

@author: Administrator
'''

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
        self.identity = None

    def setIdentity(self,text):
        self.identity = text

    def setVal(self,val):
        self.times = int(val)
        # 执行线程的run方法
        self.start()

    def start(self):
        self.signal_print_log.emit("This is starting!")
        self.signal_print_log.emit("This is 2nd time starting!")
        self.signal_print_log.emit("This is 3rd time starting!")
        pass

    def stop(self):
        self.signal_print_log.emit("This is stopping!")
        pass

    def run(self):
        while self.times > 0 and self.identity:
            time.sleep(1)
            # 发射信号
            self.sinOut.emit(self.identity + "==>"+str(self.times))
            self.times -= 1

        
        
        