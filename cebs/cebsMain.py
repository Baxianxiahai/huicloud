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
from PkgCebsHandler import ModCebsVision
from PkgCebsHandler import ModCebsCfg

#Main Windows
class cebsMainWindow(QtWidgets.QMainWindow, Ui_cebsMainWindow):
    
    def __init__(self):    
        super(cebsMainWindow, self).__init__()  
        self.setupUi(self)
        self.initUI()
        
        #固定参数
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
        
        #读取配置文件参数
        objInitCfg=ModCebsCfg.ConfigOpr()
        objInitCfg.readGlobalPar();
        objInitCfg.updateCtrlCntInfo()
        
        #启动第一个干活的子进程
        self.threadCtrl = ModCebsCtrl.classCtrlThread()
        self.threadCtrl.setIdentity("CtrlThread")
        self.threadCtrl.signal_print_log.connect(self.slot_print_trigger)
        self.threadCtrl.signal_start.connect(self.threadCtrl.funcStart)
        self.threadCtrl.signal_stop.connect(self.threadCtrl.funcStop)
        self.threadCtrl.signal_cala.connect(self.threadCtrl.funcCala)
        self.threadCtrl.signal_zero.connect(self.threadCtrl.funcZero)
        self.threadCtrl.start();

        #启动第二个干活的子进程
        self.threadVision = ModCebsVision.classVisionThread()
        self.threadVision.setIdentity("VisionThread")
        self.threadVision.signal_print_log.connect(self.slot_print_trigger)
        self.threadVision.start();
       
    def initUI(self):
        self.statusBar().showMessage('状态栏: ')
        self.setGeometry(10, 30, 1024, 768)

        exitAction = QAction(QIcon('.\icon_res\q10.ico'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用程序')
        exitAction.triggered.connect(qApp.quit)
        toolbar = self.addToolBar('EXIT')  
        toolbar.addAction(exitAction)

    def initParameter(self):
        pass

    #File Open Method, for reference
    def test_openMsg(self):  
        file, ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")  
        self.statusbar.showMessage(file)

    #核心函数
    def cebs_print_log(self, info):
        strOld = self.textEdit_runProgress.toPlainText()
        #采用全局编辑
        #strOut = strOld + "\n>> " + time.asctime() + " " + info;
        #self.textEdit_runProgress.setText(strOut);
        #采用正常的append方法
        strOut = ">> " + time.asctime() + " " + info;
        self.textEdit_runProgress.append(strOut);
        self.textEdit_runProgress.moveCursor(QtGui.QTextCursor.End)
        #后面两个操作不增加也没啥大问题，但给了我们更多的操作线索
        self.textEdit_runProgress.ensureCursorVisible()
        self.textEdit_runProgress.insertPlainText("")

    def slot_print_trigger(self, info):
        self.cebs_print_log(info)

    def slot_ctrl_start(self):
        self.threadCtrl.signal_start.emit()
        
    def slot_ctrl_stop(self):
        self.threadCtrl.signal_stop.emit()

    def slot_ctrl_cala(self):
        self.threadCtrl.signal_cala.emit()

    def slot_ctrl_zero(self):
        self.threadCtrl.signal_zero.emit()

    def slot_ctrl_null(self):
        pass

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
    
    
