'''
Created on 2018/4/29

@author: hitpony
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
import hashlib
from ctypes import *

#System lib
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, qApp, QAction, QFileDialog, QTextEdit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

#Form class
from form_qt.cebsmainform import Ui_cebsMainWindow    # 导入生成form.py里生成的类

#Local Class
from PkgCebsHandler import ModCebsCom  #Common Support module
from PkgCebsHandler import ModCebsCtrl


#Main Windows
class cebsMainWindow(QtWidgets.QMainWindow, Ui_cebsMainWindow):
    
    def __init__(self):    
        super(cebsMainWindow, self).__init__()  
        self.setupUi(self)
        self.initUI()
        #self.initCanParameter()
        
#         self.thread = ModCebsCtrl.classCtrlThread()
#         self.thread.setIdentity("thread1")
#         self.thread.sinOut.connect(self.outText)
#         self.thread.setVal(6)

        self.thread = ModCebsCtrl.classCtrlThread()
        self.thread.setIdentity("CtrlThread")
        self.thread.signal_print_log.connect(self.slot_print_trigger)
        self.thread.signal_start.connect(self.thread.start)
        self.thread.signal_stop.connect(self.thread.stop)
        self.thread.setVal(6)
        #self.thread.run();
       
    def initUI(self):
        self.statusBar().showMessage('状态栏: ')
        self.setGeometry(10, 30, 1024, 768)

        exitAction = QAction(QIcon('.\icon_res\q10.ico'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(qApp.quit)
        toolbar = self.addToolBar('EXIT')  
        toolbar.addAction(exitAction)

    def initCanParameter(self):
        pass

    #File Open Method, for reference
    def test_openMsg(self):  
        file, ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")  
        self.statusbar.showMessage(file)

    #核心函数
    def cebs_print_log(self, info):
        strOld = self.textEdit_runProgress.toPlainText()
        strOut = strOld + "\n>> " + time.asctime() + " " + info;
        self.textEdit_runProgress.setText(strOut);
        #sself.textEdit_runProgress.scrollToBottom();
        #time.sleep(1)
        pass

    def slot_print_trigger(self, info):
        self.cebs_print_log(info)

    def slot_ctrl_start(self):
        try:
            res = {}
            #obj = ModCebsCtrl.ClassHandler();
            #res = obj.func_ctrl_start();
            self.thread.signal_start.emit()
        except Exception as err:  
            print("Exec slot_ctrl_start, err = " + str(err))
            self.cebs_print_log("CTRL: Exec slot_ctrl_start, err = " + str(err))
        finally:
            self.cebs_print_log("CTRL: " + str(res))
        
    def slot_ctrl_stop(self):
        try:
            res = {}
            #obj = ModCebsCtrl.ClassHandler();
            #res = obj.func_ctrl_stop();
            self.thread.signal_stop.emit()
        except Exception as err:  
            print("Exec slot_ctrl_stop, err = " + str(err))
            self.cebs_print_log("CTRL: Exec slot_ctrl_stop, err = " + str(err))
        finally:
            self.cebs_print_log("CTRL: " + str(res))



    def slot_runpg_clear(self):
        self.textEdit_runProgress.clear();


    #Test functions
    def slot_runpg_test(self):
        res = {}
        #Trigger print log
        self.cebs_print_log("TEST: " + str(res))


#Main App entry
def main_form():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = cebsMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
    pass

#SYSTEM ENTRY
if __name__ == '__main__':
    print("[CEBS] ", time.asctime(), ", System starting...\n" );
    main_form()
    
    