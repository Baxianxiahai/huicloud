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
from form_qt.cebsmainform import Ui_cebsMainWindow    # 导入生成mainForm.py里生成的类
from form_qt.cebscalaform import Ui_cebsCalaForm      # 导入生成calaForm.py里生成的类

#Local Class
from PkgCebsHandler import ModCebsCom  #Common Support module
from PkgCebsHandler import ModCebsCtrl, ModCebsMoto
from PkgCebsHandler import ModCebsVision
from PkgCebsHandler import ModCebsCfg

#Main Windows
class cebsMainWindow(QtWidgets.QMainWindow, Ui_cebsMainWindow):
    signal_mainwin_visible = pyqtSignal() #申明给主函数使用
    signal_mainwin_unvisible = pyqtSignal()  #申明给主函数使用    
    
    def __init__(self):    
        super(cebsMainWindow, self).__init__()  
        self.setupUi(self)
        self.initUI()
        
        #必须使用成员函数，才能保证子FORM的生命周期
        self.calaForm = cebsCalaForm(self)
        
        #固定信号量设置
        self.signal_mainwin_visible.connect(self.funcMainWinVisible);
        self.signal_mainwin_unvisible.connect(self.funcMainWinUnvisible);
        
        #固定参数
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = True;
        
        #读取配置文件参数
        objInitCfg=ModCebsCfg.ConfigOpr()
        objInitCfg.readGlobalPar();
        objInitCfg.updateCtrlCntInfo()
        
        #启动第一个干活的子进程
        self.threadCtrl = ModCebsCtrl.classCtrlThread()
        self.threadCtrl.setIdentity("CtrlThread")
        self.threadCtrl.signal_print_log.connect(self.slot_print_trigger)  #接收信号
        self.threadCtrl.signal_ctrl_start.connect(self.threadCtrl.funcTakePicStart) #发送信号
        self.threadCtrl.signal_ctrl_stop.connect(self.threadCtrl.funcTakePicStop)  #发送信号
        self.threadCtrl.signal_ctrl_zero.connect(self.threadCtrl.funcCtrlMotoBackZero)  #发送信号
        self.threadCtrl.signal_cala_pilot.connect(self.threadCtrl.funcCalaPilotStart)  #发送信号
        self.threadCtrl.signal_cala_comp.connect(self.threadCtrl.funcCtrlCalaComp)  #发送信号
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
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA != True):
            self.threadCtrl.signal_ctrl_start.emit()
        
    def slot_ctrl_stop(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA != True):
            self.threadCtrl.signal_ctrl_stop.emit()

    def slot_ctrl_zero(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA != True):
            self.threadCtrl.signal_ctrl_zero.emit()

    def slot_ctrl_null(self):
        pass

    def slot_cala_pilot(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA != True):
            ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = False # 不让继续做图像识别
            self.threadCtrl.signal_cala_pilot.emit()

    def slot_cala_start(self):
        ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA = True;
        ModCebsCom.GL_CEBS_PIC_PROC_CTRL_FLAG = False; # 不让继续做图像识别
        self.cebs_print_log("CALA Starting...")

    def slot_cala_move(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA == True):
            #读取运动刻度
            radioCala05mm = self.radioButton_cala_05mm.isChecked();
            radioCala1mm = self.radioButton_cala_1mm.isChecked();
            radioCala5mm = self.radioButton_cala_5mm.isChecked();
            radioCala1cm = self.radioButton_cala_1cm.isChecked();
            radioCala5cm = self.radioButton_cala_5cm.isChecked();
            if (radioCala05mm == 1):
                parMoveScale = 1;
            elif (radioCala1mm == 1):
                parMoveScale = 2;
            elif (radioCala5mm == 1):
                parMoveScale = 3;
            elif (radioCala1cm == 1):
                parMoveScale = 4;
            elif (radioCala5cm == 1):
                parMoveScale = 5;
            else:
                parMoveScale = 1;
            #读取运动方向
            radioCalaUp = self.radioButton_cala_y_plus.isChecked();
            radioCalaDown = self.radioButton_cala_y_minus.isChecked();
            radioCalaLeft = self.radioButton_cala_x_minus.isChecked();
            radioCalaRight = self.radioButton_cala_x_plus.isChecked();
            if (radioCalaUp == 1):
                parMoveDir = 1;
            elif (radioCalaDown == 1):
                parMoveDir = 2;
            elif (radioCalaLeft == 1):
                parMoveDir = 3;
            elif (radioCalaRight == 1):
                parMoveDir = 4;
            else:
                parMoveDir = 1;
            #调用处理函数
            obj = ModCebsMoto.classMotoProcess();
            obj.funcMotoCalaMoveOneStep(parMoveScale, parMoveDir);
            self.cebs_print_log("CALA Moving one step. Current position XY=[%d/%d]." % (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1]))

    def slot_cala_left_up(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA == True):
            ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0];
            ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1];
            iniObj = ModCebsCfg.ConfigOpr();
            iniObj.updateSectionPar();
            self.cebs_print_log("CALA LeftUp Axis set! XY=%d/%d." % (ModCebsCom.GL_CEBS_HB_POS_IN_UM[0], ModCebsCom.GL_CEBS_HB_POS_IN_UM[1]))

    def slot_cala_right_bottom(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA == True):
            ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0];
            ModCebsCom.GL_CEBS_HB_POS_IN_UM[3] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1];
            iniObj = ModCebsCfg.ConfigOpr();
            iniObj.updateSectionPar();
            self.cebs_print_log("CALA RightBottom Axis set!  XY=%d/%d." % (ModCebsCom.GL_CEBS_HB_POS_IN_UM[2], ModCebsCom.GL_CEBS_HB_POS_IN_UM[3]))

    def slot_cala_comp(self):
        if (ModCebsCom.GL_CEBS_CTRL_WORK_MODE_CALA == True):
            self.threadCtrl.signal_cala_comp.emit()
        self.cebs_print_log("CALA Complete!!!")

    def slot_runpg_clear(self):
        self.textEdit_runProgress.clear();

    def funcMainWinVisible(self):
        if not self.isVisible():
            self.show()

    def funcMainWinUnvisible(self):
        if self.isVisible():
            self.hide()

    #Test functions
    def slot_runpg_test(self):
        #res = {}
        #self.cebs_print_log("TEST: " + str(res))
        #self.calaForm = cebsCalaForm()
        if not self.calaForm.isVisible():
            self.signal_mainwin_unvisible.emit()
            self.calaForm.show()
        self.cebs_print_log("TEST WIDGET!")


#Calibration Widget
class cebsCalaForm(QtWidgets.QWidget, Ui_cebsCalaForm):
    signal_mainwin_visible = pyqtSignal() #申明给主函数使用

    def __init__(self, father):    
        super(cebsCalaForm, self).__init__()  
        self.setupUi(self)
        self.mainWin = father
        #self.justDoubleClicked = False

    #重载系统的关闭函数
    def closeEvent(self, event):
        self.mainWin.signal_mainwin_visible.emit()
        self.close()
        
    def slot_cala_close(self):
        self.mainWin.signal_mainwin_visible.emit()
        self.close()

#Main App entry
def main_form():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = cebsMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

#SYSTEM ENTRY
if __name__ == '__main__':
    print("[CEBS] ", time.asctime(), ", System starting...\n" );
    main_form()
    
    
