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
from PyQt5 import QtWidgets, QtGui
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
#To be added!

#LOGIN WINDOWS
class Login(QDialog):
    """登录窗口"""
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        loadUi('Login.ui', self)   #看到没，瞪大眼睛看
        self.labelTips.hide()
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.lineEditUser.text() != "admin" or self.lineEditPasswd.text() != "123456":
            self.labelTips.show()
            self.labelTips.setText("用户名或密码错误！")
        else:
            self.accept()

    def slotCancle(self):
        self.reject()


#Main Windows
class cebsMainWindow(QtWidgets.QMainWindow, Ui_cebsMainWindow):
    
    def __init__(self):    
        super(cebsMainWindow, self).__init__()  
        self.setupUi(self)
        self.initUI()
        self.initCanParameter()
       
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
    def fmpt_print_log(self, info):
        strOld = self.textEdit_OprLogInfo.toPlainText()
        strOut = strOld + info;
        self.textEdit_OprLogInfo.setText(strOut);
        #self.textEdit_OprLogInfo.scrollToBottom();
        #time.sleep(1)
        pass

#Widget Windows
class widgetWindowKeo(QtWidgets.QWidget, Ui_cebsMainWindow):
    def __init__(self):    
        super(widgetWindowKeo,self).__init__()    
        self.setupUi(self)

    #定义槽函数
    def hello(self):
        self.textEdit_OprLogInfo.setText("hello world")

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
    
    
