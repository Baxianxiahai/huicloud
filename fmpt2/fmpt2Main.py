'''
Created on 2018/2/23

@author: hitpony
'''

#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

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
from form_qt.fmpt2form import Ui_ObjFmpt2Form    # 导入生成form.py里生成的类
from form_qt.fmpt2mainform import Ui_ObjFmpt2MainForm    # 导入生成form.py里生成的类

#Local Class
from PkgFmptHandler import ModFmptCom  #Common Support module
from PkgFmptHandler import ModFmptKeo  #Key Element Operation
from PkgFmptHandler import ModFmptAim  #App Image Management
from PkgFmptHandler import ModFmptFio  #Full Image Operation
from PkgFmptHandler import ModFmptBbo  #Batch Burn Operation
from PkgFmptHandler import ModFmptCloudCon  #Cloud Connection Data Management
from PkgFmptHandler import ModFmptIhuCon  #Ihu Connection Data Management

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
class fmpt2MainWindow(QtWidgets.QMainWindow, Ui_ObjFmpt2MainForm):
    
    def __init__(self):    
        super(fmpt2MainWindow, self).__init__()  
        self.setupUi(self)
        #self.fileOpen.triggered.connect(self.openMsg) 
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

        #Main function already own .show func, so no need here
        #self.show()

    def initCanParameter(self):
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE  = 3-self.comboBox_ihuConn_canParSet_productType.currentIndex(); #USBDEV=3, USBDEV=2
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND   = self.comboBox_ihuConn_canParSet_index.currentIndex();
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND   = self.comboBox_ihuConn_canParSet_canNbr.currentIndex();
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_RCVCODE   = int(str('0x' + self.lineEdit_ihuConn_canParSet_rcvCode_text.text()), base=16);
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_MASKCODE   = int(str('0x' + self.lineEdit_ihuConn_canParSet_rcvCode_text.text()), base=16);
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_TIMER0   = int(str('0x' + self.lineEdit_ihuConn_canParSet_timer0_text.text()), base=16);
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_TIMER1   = int(str('0x' + self.lineEdit_ihuConn_canParSet_timer1_text.text()), base=16);
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_FILTER   = self.comboBox_ihuConn_canParSet_filter.currentIndex() + 1;
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_WORKMODE   = self.comboBox_ihuConn_canParSet_workMode.currentIndex();
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_REMOTE_FLAG   = self.comboBox_ihuConn_canParSet_frameFormat.currentIndex();
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_EXT_FLAG   = self.comboBox_ihuConn_canParSet_frameType.currentIndex();
        ModFmptCom.GL_FMPT_DEVDRIVE_CAN_ID   = int(str(self.lineEdit_ihuConn_canParSet_frameId_text.text()));
        #print("GL_FMPT_DEVDRIVE_CAN_DEVIND = ", ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND)

    #File Open Method, for reference
    def test_openMsg(self):  
        file, ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")  
        self.statusbar.showMessage(file)

    def slotDialogWinKeo(self):
        #self.statusBar().showMessage('Fetch! Keo')
        fmpt2MainWindow.dialog1.show()
        pass
    
    #核心函数
    def fmpt_print_log(self, info):
        strOld = self.textEdit_OprLogInfo.toPlainText()
        strOut = strOld + info;
        self.textEdit_OprLogInfo.setText(strOut);
        #self.textEdit_OprLogInfo.scrollToBottom();
        
        #光标移动到最后, 并设置拥有焦点
#         c= self.textEdit_OprLogInfo.textCursor();
#         c.movePosition(self.textEdit_OprLogInfo.End, MoveAnchor); 
#         self.textEdit_OprLogInfo.textEdit.setTextCursor(c);    
#         self.textEdit_OprLogInfo.setFocus(MouseFocusReason);        
#         
        #self.textEdit_OprLogInfo.moveCursor(self.textEdit_OprLogInfo.Start)
        
        #time.sleep(1)
        pass

    
    #信号槽处理函数
    def slot_cloudCon_par_set(self):
        try:
            obj = ModFmptCloudCon.ClassHandler();
            applyNum = self.lineEdit_cloudCon_apply_number_text.text();
            cloudIpAddr = self.lineEdit_cloudCon_ipAddr_text.text();
            facCode = self.lineEdit_cloudCon_facCode_text.text();
            pdCode = self.lineEdit_cloudCon_pdCode_text.text();
            pjCode = self.lineEdit_cloudCon_pjCode_text.text();
            pdType = self.lineEdit_cloudCon_pdType_text.text();
            userCode = self.lineEdit_cloudCon_userCode_text.text();
            userAccount = self.lineEdit_cloudCon_userAccount_text.text();
            passwd = self.lineEdit_cloudCon_passwd_text.text();
            formalFlag = self.lineEdit_cloudCon_formalFlag_text.text();
            res = obj.func_par_set(applyNum, cloudIpAddr, facCode, pdCode, pjCode, pdType, userCode, userAccount, passwd, formalFlag);
        except Exception as err:  
            print("Exec slot_cloudCon_par_set, err = " + str(err))
            self.fmpt_print_log("\nCLOUDCONN: Exec slot_cloudCon_par_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nCLOUDCONN: " + str(res))

    def slot_cloudCon_label_apply(self):
        try:
            obj = ModFmptCloudCon.ClassHandler();
            applyNum = self.lineEdit_cloudCon_apply_number_text.text();
            res = obj.func_label_apply(applyNum);
        except Exception as err:  
            print("Exec slot_cloudCon_label_apply, err = " + str(err))
            self.fmpt_print_log("\nCLOUDCONN: Exec slot_cloudCon_label_apply, err = " + str(err))
        finally:
            self.fmpt_print_log("\nCLOUDCONN: " + str(res))


    def slot_ihuCon_conn(self):
        try:
            self.initCanParameter();
            obj = ModFmptIhuCon.ClassHandler();
            radioSps = self.radioButton_ihuCon_port_sps.isChecked();
            radioCan = self.radioButton_ihuCon_port_can.isChecked();
            radioEth = self.radioButton_ihuCon_port_eth.isChecked();
            if (radioSps == 1):
                parFormat = 1;
            elif (radioCan == 1):
                parFormat = 2;
            elif (radioEth == 1):
                parFormat = 3;
            else:
                parFormat = 2;
            res = obj.func_conn(parFormat);
        except Exception as err:  
            print("Exec slot_ihuCon_conn, err = " + str(err))
            self.fmpt_print_log("\nIHUCONN: Exec slot_ihuCon_conn, err = " + str(err))
        finally:
            self.fmpt_print_log("\nIHUCONN: Res with" + str(res))


    def slot_ihuCon_disc(self):
        try:
            self.initCanParameter();
            obj = ModFmptIhuCon.ClassHandler();
            radioSps = self.radioButton_ihuCon_port_sps.isChecked();
            radioCan = self.radioButton_ihuCon_port_can.isChecked();
            radioEth = self.radioButton_ihuCon_port_eth.isChecked();
            if (radioSps == 1):
                parFormat = 1;
            elif (radioCan == 1):
                parFormat = 2;
            elif (radioEth == 1):
                parFormat = 3;
            else:
                parFormat = 2;
            res = obj.func_disc(parFormat);
        except Exception as err:  
            print("Exec slot_ihuCon_disc, err = " + str(err))
            self.fmpt_print_log("\nIHUCONN: Exec slot_ihuCon_disc, err = " + str(err))
        finally:
            self.fmpt_print_log("\nIHUCONN: " + str(res))


    def slot_keo_equLable_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_equLable_read();
            if (res['res'] < 0):
                self.lineEdit_keo_equLable.setText('')
            else:
                self.lineEdit_keo_equLable.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_equLable_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_equLable_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_equLable_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_equLable.text();
            res = obj.func_equLable_write(par);
        except Exception as err:  
            print("Exec slot_keo_equLable_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_equLable_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))
        
    def slot_keo_hwType_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_hwType_read();
            if (res['res'] < 0):
                self.lineEdit_keo_hwType.setText('')
            else:
                self.lineEdit_keo_hwType.setText('0x%x'%(res['value']))
        except Exception as err:
            print("Exec slot_keo_hwType_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_hwType_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))
            pass

    def slot_keo_hwType_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_hwType.text();
            res = obj.func_hwType_write(par);
        except Exception as err:  
            print("Exec slot_keo_hwType_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_hwType_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swUpgradeFlag_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_swUpgradeFlag_read();
            if (res['res'] < 0):
                self.lineEdit_keo_swUpgradeFlag.setText('')
            else:
                self.lineEdit_keo_swUpgradeFlag.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_swUpgradeFlag_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swUpgradeFlag_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swUpgradeFlag_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_swUpgradeFlag.text();
            res = obj.func_swUpgradeFlag_write(par);
        except Exception as err:  
            print("Exec slot_keo_swUpgradeFlag_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swUpgradeFlag_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))
        
    def slot_keo_hwPemId_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_hwPemId_read();
            if (res['res'] < 0):
                self.lineEdit_keo_hwPemId.setText('')
            else:
                self.lineEdit_keo_hwPemId.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_hwPemId_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_hwPemId_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))
        
    def slot_keo_hwPemId_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_hwPemId.text();
            res = obj.func_hwPemId_write(par);
        except Exception as err:  
            print("Exec slot_keo_hwPemId_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_hwPemId_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))
                
    def slot_keo_swRelId_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_swRelId_read();
            if (res['res'] < 0):
                self.lineEdit_keo_swRelId.setText('')
            else:
                self.lineEdit_keo_swRelId.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_swRelId_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swRelId_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))    	

    def slot_keo_swRelId_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_swRelId.text();
            res = obj.func_swRelId_write(par);
        except Exception as err:  
            print("Exec slot_keo_swRelId_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swRelId_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swVerId_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_swVerId_read();
            if (res['res'] < 0):
                self.lineEdit_keo_swVerId.setText('')
            else:
                self.lineEdit_keo_swVerId.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_swVerId_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swVerId_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swVerId_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_swVerId.text();
            res = obj.func_swVerId_write(par);
        except Exception as err:  
            print("Exec slot_keo_swVerId_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swVerId_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swUpgPollId_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_swUpgPollId_read();
            if (res['res'] < 0):
                self.lineEdit_keo_swUpgPollId.setText('')
            else:
                self.lineEdit_keo_swUpgPollId.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_swUpgPollId_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swUpgPollId_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_swUpgPollId_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_swUpgPollId.text();
            res = obj.func_swUpgPollId_write(par);
        except Exception as err:  
            print("Exec slot_keo_swUpgPollId_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_swUpgPollId_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_bootIndex_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_bootIndex_read();
            if (res['res'] < 0):
                self.lineEdit_keo_bootIndex.setText('')
            else:
                self.lineEdit_keo_bootIndex.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_bootIndex_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_bootIndex_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_bootIndex_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_bootIndex.text();
            res = obj.func_bootIndex_write(par);
        except Exception as err:  
            print("Exec slot_keo_bootIndex_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_bootIndex_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_bootAreaMax_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_bootAreaMax_read();
            if (res['res'] < 0):
                self.lineEdit_keo_bootAreaMax.setText('')
            else:
                self.lineEdit_keo_bootAreaMax.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_bootAreaMax_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_bootAreaMax_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_bootAreaMax_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_bootAreaMax.text();
            res = obj.func_bootAreaMax_write(par);
        except Exception as err:  
            print("Exec slot_keo_bootAreaMax_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_bootAreaMax_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cypherKey_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = {}
            res = obj.func_cypherKey_read();
            if (res['res'] < 0):
                self.lineEdit_keo_cypherKey.setText('')
            else:
                self.lineEdit_keo_cypherKey.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_keo_cypherKey_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cypherKey_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cypherKey_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            par = self.lineEdit_keo_cypherKey.text();
            res = obj.func_cypherKey_write(par);
        except Exception as err:  
            print("Exec slot_keo_cypherKey_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cypherKey_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cfgFile_Browse(self):
        try:
            #http://blog.csdn.net/a359680405/article/details/45166271
            ModFmptCom.GL_FMPT_BOOT_CFG_LOCAL_FILE_NAME, ModFmptCom.GL_FMPT_BOOT_CFG_LOCAL_FILE_TYPE = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "Text Files (*.txt);; Config Files (*.cfg);; All Files (*.*)")   #设置文件扩展名过滤,注意用双分号间隔  
            res = self.lineEdit_keo_cfgFile.setText(ModFmptCom.GL_FMPT_BOOT_CFG_LOCAL_FILE_NAME);
        except Exception as err:
            print("Exec slot_keo_cfgFile_Browse, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cfgFile_Browse, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cfgFile_LoadFile(self):
        if (self.lineEdit_keo_cfgFile.text() == ''):
            return;
        try:
            fileName =  self.lineEdit_keo_cfgFile.text();
            FILE = open(fileName, mode='rt')
            coded_data=str(FILE.read())
            bootCfgFileData = json.loads(coded_data)
            #print(bootCfgInput)
            FILE.close()
            objCom = ModFmptCom.ClassComProc();
            res = objCom.FuncLoadBootCfgFileDataIntoMemory(bootCfgFileData);
            if (res > 0):
                res = ModFmptCom.zStrBootCfgEng;
        except Exception as err:  
            print("Exec slot_keo_cfgFile_LoadFile, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cfgFile_LoadFile, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    #fileName, ok2 = QFileDialog.getSaveFileName(self, "文件保存", ModFmptCom.GL_FMPT_BOOT_CFG_LOCAL_FILE_NAME, "All Files (*);;Text Files (*.txt)")
    def slot_keo_cfgFile_SaveFile(self):
        if (self.lineEdit_keo_cfgFile.text() == ''):
            return;
        try:
            fileName =  self.lineEdit_keo_cfgFile.text();
            FILE = open(fileName,'w+b')
            encoded_data = (json.dumps(ModFmptCom.zStrBootCfgEng).encode('utf-8'))
            print(encoded_data)
            res = "File save length = " + str(FILE.write(encoded_data))
            FILE.flush()
            FILE.close()
        except Exception as err:  
            print("Exec slot_keo_cfgFile_SaveFile, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cfgFile_SaveFile, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cfgFile_ReadAllFromHw(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = obj.func_cfgFile_ReadAllFromHw();
        except Exception as err:  
            print("Exec slot_keo_cfgFile_ReadAllFromHw, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cfgFile_ReadAllFromHw, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_cfgFile_WriteAllToHw(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            res = obj.func_cfgFile_WriteAllToHw();
        except Exception as err:
            print("Exec slot_keo_cfgFile_WriteAllToHw, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_cfgFile_WriteAllToHw, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_byteopr_read(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            parAddr = self.lineEdit_keo_byteopr_address.text();
            radioByte = self.radioButton_keo_byteopr_byte.isChecked();
            radioShort = self.radioButton_keo_byteopr_short.isChecked();
            radioInt = self.radioButton_keo_byteopr_int.isChecked();
            if (radioByte == 1):
                parFormat = 1;
            elif (radioShort == 1):
                parFormat = 2;
            elif (radioInt == 1):
                parFormat = 4;
            else:
                parFormat = 1;
            res = obj.func_byteopr_read(parAddr, parFormat);
            if (res['res'] < 0):
                self.lineEdit_keo_byteopr_result.setText('')
            else:
                self.lineEdit_keo_byteopr_result.setText('0x%x'%(res['value']));
        except Exception as err:  
            print("Exec slot_keo_byteopr_read, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_byteopr_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_keo_byteopr_write(self):
        try:
            obj = ModFmptKeo.ClassHandler();
            parAddr = self.lineEdit_keo_byteopr_address.text();
            radioByte = self.radioButton_keo_byteopr_byte.isChecked();
            radioShort = self.radioButton_keo_byteopr_short.isChecked();
            radioInt = self.radioButton_keo_byteopr_int.isChecked();
            if (radioByte == 1):
                parFormat = 1;
            elif (radioShort == 1):
                parFormat = 2;
            elif (radioInt == 1):
                parFormat = 4;
            else:
                parFormat = 1;
            parValue = self.lineEdit_keo_byteopr_result.text();
            res = obj.func_byteopr_write(parAddr, parFormat, parValue);
            print(res)
        except Exception as err:  
            print("Exec slot_keo_byteopr_write, err = " + str(err))
            self.fmpt_print_log("\nKEO: Exec slot_keo_byteopr_write, err = " + str(err))
        finally:
            self.fmpt_print_log("\nKEO: " + str(res))

    def slot_fio_file_browse(self):
        try:
            ModFmptCom.GL_FMPT_FIO_IMAGE_LOCAL_FILE_NAME, ModFmptCom.GL_FMPT_FIO_IMAGE_LOCAL_FILE_TYPE = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "Img Files (*.img);; All Files (*.*)")   #设置文件扩展名过滤,注意用双分号间隔  
            res = self.lineEdit_fio_file_dir.setText(ModFmptCom.GL_FMPT_FIO_IMAGE_LOCAL_FILE_NAME);
        except Exception as err:
            print("Exec slot_keo_cfgFile_Browse, err = " + str(err))
            self.fmpt_print_log("\nFIO: Exec slot_keo_cfgFile_Browse, err = " + str(err))
        finally:
            self.fmpt_print_log("\nFIO: " + str(res))

    #IMAGE FILE
    def slot_fio_file_save(self):
        try:
            obj = ModFmptFio.ClassHandler();
            imageName = self.lineEdit_fio_file_dir.text();
            res = obj.func_file_image_save_to_disk(imageName);
        except Exception as err:  
            print("Exec slot_fio_file_save, err = " + str(err))
            self.fmpt_print_log("\nFIO: Exec slot_fio_file_save, err = " + str(err))
        finally:
            self.fmpt_print_log("\nFIO: " + str(res))

    #IMAGE FILE
    def slot_fio_file_load(self):
        try:
            obj = ModFmptFio.ClassHandler();
            imageName = self.lineEdit_fio_file_dir.text();
            res = obj.func_file_image_load_into_flash(imageName);
        except Exception as err:  
            print("Exec slot_fio_file_load, err = " + str(err))
            self.fmpt_print_log("\nFIO: Exec slot_fio_file_load, err = " + str(err))
        finally:
            self.fmpt_print_log("\nFIO: " + str(res))

    def slot_aim_fac_addr_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_addr_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_addr_text.setText('')
            else:
                self.lineEdit_aim_fac_addr_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_addr_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_addr_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_chk_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_chk_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_chk_text.setText('')
            else:
                self.lineEdit_aim_fac_chk_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_chk_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_chk_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_chk_chk(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_chk_chk();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_chk_text.setText('')
            else:
                self.lineEdit_aim_fac_chk_text.setText('0x%x'%(res['value']))            
        except Exception as err:  
            print("Exec slot_aim_fac_chk_chk, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_chk_chk, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_swRel_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_swRel_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_swRel_text.setText('')
            else:
                self.lineEdit_aim_fac_swRel_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_swRel_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_swRel_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_swRel_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_fac_swRel_text.text();
            res = obj.func_fac_swRel_set(par);
        except Exception as err:  
            print("Exec slot_aim_fac_swRel_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_swRel_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_valid_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_valid_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_valid_text.setText('')
            else:
                self.lineEdit_aim_fac_valid_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_valid_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_valid_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_swVer_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_swVer_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_swVer_text.setText('')
            else:
                self.lineEdit_aim_fac_swVer_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_swVer_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_swVer_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_swVer_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_fac_swVer_text.text();
            res = obj.func_fac_swVer_set(par);
        except Exception as err:  
            print("Exec slot_aim_fac_swVer_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_swVer_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_len_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_fac_len_read();
            if (res['res'] < 0):
                self.lineEdit_aim_fac_len_text.setText('')
            else:
                self.lineEdit_aim_fac_len_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_fac_len_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_len_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_file_browse(self):
        try:
            ModFmptCom.GL_FMPT_AIM_FAC_IMAGE_LOCAL_FILE_NAME, ModFmptCom.GL_FMPT_AIM_FAC_IMAGE_LOCAL_FILE_TYPE = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "Bin Files (*.bin);; All Files (*.*)")   #设置文件扩展名过滤,注意用双分号间隔  
            res = self.lineEdit_aim_fac_file_text.setText(ModFmptCom.GL_FMPT_AIM_FAC_IMAGE_LOCAL_FILE_NAME);
        except Exception as err:  
            print("Exec slot_aim_fac_file_browse, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_file_browse, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_fac_file_update(self):
        try:
            obj = ModFmptAim.ClassHandler();
            facFile = self.lineEdit_aim_fac_file_text.text();
            res = obj.func_fac_file_update(facFile);
        except Exception as err:  
            print("Exec slot_aim_fac_file_update, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_fac_file_update, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_addr_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_addr_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_addr_text.setText('')
            else:
                self.lineEdit_aim_app1_addr_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_addr_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_addr_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_swRel_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_swRel_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_swRel_text.setText('')
            else:
                self.lineEdit_aim_app1_swRel_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_swRel_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_swRel_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_swRel_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_app1_swRel_text.text();
            res = obj.func_app1_swRel_set(par);            
        except Exception as err:  
            print("Exec slot_aim_app1_swRel_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_swRel_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_valid_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_valid_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_valid_text.setText('')
            else:
                self.lineEdit_aim_app1_valid_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_valid_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_valid_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_chk_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_chk_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_chk_text.setText('')
            else:
                self.lineEdit_aim_app1_chk_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_chk_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_chk_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_chk_chk(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_chk_chk();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_chk_text.setText('')
            else:
                self.lineEdit_aim_app1_chk_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_chk_chk, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_chk_chk, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_swVer_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_swVer_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_swVer_text.setText('')
            else:
                self.lineEdit_aim_app1_swVer_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_swVer_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_swVer_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_swVer_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_app1_swVer_text.text();
            res = obj.func_app1_swVer_set(par);            
        except Exception as err:  
            print("Exec slot_aim_app1_swVer_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_swVer_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))
            
    def slot_aim_app1_len_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app1_len_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app1_len_text.setText('')
            else:
                self.lineEdit_aim_app1_len_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app1_len_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_len_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_file_browse(self):
        try:
            ModFmptCom.GL_FMPT_AIM_APP1_IMAGE_LOCAL_FILE_NAME, ModFmptCom.GL_FMPT_AIM_APP1_IMAGE_LOCAL_FILE_TYPE = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "Bin Files (*.bin);; All Files (*.*)")   #设置文件扩展名过滤,注意用双分号间隔  
            res = self.lineEdit_aim_app1_file_text.setText(ModFmptCom.GL_FMPT_AIM_APP1_IMAGE_LOCAL_FILE_NAME);
        except Exception as err:  
            print("Exec slot_aim_app1_file_browse, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_file_browse, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app1_file_update(self):
        try:
            obj = ModFmptAim.ClassHandler();
            app1File = self.lineEdit_aim_app1_file_text.text();           
            res = obj.func_app1_file_update(app1File);
        except Exception as err:  
            print("Exec slot_aim_app1_file_update, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app1_file_update, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_addr_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_addr_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_addr_text.setText('')
            else:
                self.lineEdit_aim_app2_addr_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_addr_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_addr_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_chk_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_chk_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_chk_text.setText('')
            else:
                self.lineEdit_aim_app2_chk_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_chk_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_chk_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_chk_chk(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_chk_chk();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_chk_text.setText('')
            else:
                self.lineEdit_aim_app2_chk_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_chk_chk, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_chk_chk, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))
            
    def slot_aim_app2_swRel_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_swRel_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_swRel_text.setText('')
            else:
                self.lineEdit_aim_app2_swRel_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_swRel_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_swRel_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_swRel_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_app2_swRel_text.text();
            res = obj.func_app2_swRel_set(par);            
        except Exception as err:  
            print("Exec slot_aim_app2_swRel_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_swRel_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_valid_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_valid_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_valid_text.setText('')
            else:
                self.lineEdit_aim_app2_valid_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_valid_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_valid_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_len_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_len_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_len_text.setText('')
            else:
                self.lineEdit_aim_app2_len_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_len_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_len_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_swVer_read(self):
        try:
            obj = ModFmptAim.ClassHandler();
            res = {}
            res = obj.func_app2_swVer_read();
            if (res['res'] < 0):
                self.lineEdit_aim_app2_swVer_text.setText('')
            else:
                self.lineEdit_aim_app2_swVer_text.setText('0x%x'%(res['value']))
        except Exception as err:  
            print("Exec slot_aim_app2_swVer_read, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_swVer_read, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_swVer_set(self):
        try:
            obj = ModFmptAim.ClassHandler();
            par = self.lineEdit_aim_app2_swVer_text.text();
            print(par)
            res = obj.func_app2_swVer_set(par);            
        except Exception as err:  
            print("Exec slot_aim_app2_swVer_set, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_swVer_set, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))
            
    def slot_aim_app2_file_browse(self):
        try:
            ModFmptCom.GL_FMPT_AIM_APP2_IMAGE_LOCAL_FILE_NAME, ModFmptCom.GL_FMPT_AIM_APP2_IMAGE_LOCAL_FILE_TYPE = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "Bin Files (*.bin);; All Files (*.*)")   #设置文件扩展名过滤,注意用双分号间隔  
            res = self.lineEdit_aim_app2_file_text.setText(ModFmptCom.GL_FMPT_AIM_APP2_IMAGE_LOCAL_FILE_NAME);
        except Exception as err:  
            print("Exec slot_aim_app2_file_browse, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_file_browse, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))

    def slot_aim_app2_file_update(self):
        try:
            obj = ModFmptAim.ClassHandler();
            app2File = self.lineEdit_aim_app2_file_text.text();
            res = obj.func_app2_file_update(app2File);
        except Exception as err:  
            print("Exec slot_aim_app2_file_update, err = " + str(err))
            self.fmpt_print_log("\nAIM: Exec slot_aim_app2_file_update, err = " + str(err))
        finally:
            self.fmpt_print_log("\nAIM: " + str(res))


    #无法实现批量处理的动态展示，需要通过模态弹窗实现动态信息的展示，而该模态框必须是另外一个进程
    def slot_bbo_burn_fac_app(self):
        res = {}
        batSel = self.checkBox_bbo_batchModeSelection.isChecked();
        obj = ModFmptBbo.ClassHandler();
        imageName = self.lineEdit_fio_file_dir.text();
        
        if (batSel == False):            
            try:
                res = obj.func_burn_fac_app(imageName);
            except Exception as err:  
                print("Exec slot_bbo_burn_fac_app, err = " + str(err))
                self.fmpt_print_log("\nBBO: Exec slot_bbo_burn_fac_app, err = " + str(err))
            finally:
                self.fmpt_print_log("\nBBO: " + str(res))
                return;
        
        #time.sleep(1)
        #Batch mode
        self.fmpt_print_log("\nBBO: Not yet support batch mode!")
        return;
        
        #Following function still have some issues
        batNumTotal = int(str(self.lineEdit_bbo_maxNumber_text.text()));
        for batIndex in range(0, batNumTotal):
            self.fmpt_print_log("\nBBO: Start batch index = %d" % (batIndex));
            #Apply code from back
            objCloud = ModFmptCloudCon.ClassHandler();
            callRes = objCloud.func_label_apply(1)
            if (callRes['res'] < 0):
                self.lineEdit_bbo_devCode_text.setText('')
                self.fmpt_print_log("\nBBO: Not fetch labels correctly")
                res['res'] = callRes['res'];
                break;
            self.lineEdit_bbo_devCode_text.setText(str(callRes['value']['IeCnt']['labelStart']))
            callRes = obj.func_burn_fac_app_with_new_equLabel(imageName, callRes['value']['IeCnt']['labelStart']);
            if (callRes['res'] < 0):
                self.fmpt_print_log("\nBBO: Not fetch labels correctly")
                res['res'] = callRes['res'];
                break;
        #Finally return back
        self.fmpt_print_log("\nBBO: " + str(res))
        return;
    
    
    #burn with bc+fac+app    
    def slot_bbo_burn_bc_fac_app(self):
        res = {}
        batSel = self.checkBox_bbo_batchModeSelection.isChecked();
        obj = ModFmptBbo.ClassHandler();
        imageName = self.lineEdit_fio_file_dir.text();
        
        if (batSel == False):
            try:
                res = obj.func_burn_bc_fac_app(imageName);
            except Exception as err:  
                print("Exec slot_bbo_burn_bc_fac_app, err = " + str(err))
                self.fmpt_print_log("\nBBO: Exec slot_bbo_burn_bc_fac_app, err = " + str(err))
            finally:
                self.fmpt_print_log("\nBBO: " + str(res))
                return;
        
        #Batch mode
        self.fmpt_print_log("\nBBO: Not yet support batch mode!")
        return;

        #Following function still have some issues
        batNumTotal = int(str(self.lineEdit_bbo_maxNumber_text.text()));
        for batIndex in range(0, batNumTotal):
            self.fmpt_print_log("\nBBO: Start batch index = %d" % (batIndex));
            #Apply code from back
            objCloud = ModFmptCloudCon.ClassHandler();
            callRes = objCloud.func_label_apply(1)
            if (callRes['res'] < 0):
                self.lineEdit_bbo_devCode_text.setText('')
                self.fmpt_print_log("\nBBO: Not fetch labels correctly")
                res['res'] = callRes['res'];
            else:
                self.lineEdit_bbo_devCode_text.setText(str(callRes['value']['IeCnt']['labelStart']))
                res = obj.func_burn_bc_fac_app_with_new_equLabel(imageName, callRes['value']['IeCnt']['labelStart']);
            self.fmpt_print_log("\nBBO: " + str(res))        
            return;

    
    
    def slot_oli_clear(self):
        self.textEdit_OprLogInfo.clear();


    #Test functions
    def slot_oli_test(self):
        res = {"TEST!"}

        #Test1
        #hash = hashlib.md5()
        #hash.update('admin'.encode('utf-8'))
        #res = hash.hexdigest()
        #print(res)
        
        #Test2
        #obj = ModFmptIhuCon.ClassBlockElm();
        #imageName = self.lineEdit_fio_file_dir.text();
        #res = obj.FuncElm_WRITE_FAC_STATUS(imageName);

        #Test3
        #obj = ModFmptIhuCon.ClassBatchOpr();
        #imageName = self.lineEdit_fio_file_dir.text();
        #res = obj.FuncBat_app2_load(imageName);
        #res = obj.FuncBat_load_bootcfg();
        
        #Test4
        #obj = ModFmptIhuCon.ClassBlockElm();
        #res = obj.FuncElm_ERASE_BOOTCFG_STATUS();
        #res = obj.FuncElm_ERASE_FAC_STATUS()
        

        #Test5
        #obj = ModFmptIhuCon.ClassBlockElm();
        #imageName = self.lineEdit_fio_file_dir.text();
        #res = obj.FuncElm_READ_IMAGE2DISK_STATUS(imageName);
        
        #Test6
#         strDllPath = sys.path[0] + str(os.sep) + "DealAndSend.dll"
#         print(strDllPath)
#         #objDll = cdll.LoadLibrary(strDllPath)
#         objDll = CDLL(strDllPath)
#         inputData = "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"
#         print(inputData)
#         api  = objDll.DealStr;
#         api.argtypes = [c_void_p];
#         api.restypes = c_void_p;
#         res = api(inputData);
#         print(res)
        
        #
        #  2018/6/1/ZJL: 去掉TEST.JAR的测试过程，不然会造成实际应用出错，干扰正常使用
        #
        #Test7
#         import jpype
#         jvmPath = jpype.getDefaultJVMPath()       # 默认的JVM路径
#         print(jvmPath)
#         
#         jarpath = os.path.join(os.path.abspath('.'), '')
#         print(jarpath)
#         #开启JVM，且指定jar包位置
#         if not jpype.isJVMStarted():
#             jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'test.jar'))
#         #引入java程序中的类.路径应该是项目中的package包路径
#         javaClass = jpype.JClass('com.chnsce.decoding.TestPHP')
#         jd = javaClass()
#         #decode(String produceNo, String commandNo, String htcs, int meterTypeCode )
#         #这一步就是具体执行类中的函数了
#         produceNo = "1";
#         commandNo = "1";
#         htcs = "AAAA: 3";
#         meterTypeCode = 0xA8;
#         inputData = "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"
#         res = jd.decode(produceNo, commandNo, htcs, meterTypeCode);
#         #print(res)
#         #jpype.shutdownJVM()
#     
#         #Trigger print log
#         self.fmpt_print_log("\nOLI: " + str(res))
        
        #
        #  2018/6/1/ZJL: 无效更新
        #
        #Test8
        self.fmpt_print_log("\nOLI: " + str(res))
    
        

#Widget Windows
class widgetWindowKeo(QtWidgets.QWidget, Ui_ObjFmpt2Form):
    def __init__(self):    
        super(widgetWindowKeo,self).__init__()    
        self.setupUi(self)

    #定义槽函数
    def hello(self):
        self.textEdit_OprLogInfo.setText("hello world")

#Main App entry
def main_form():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = fmpt2MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())    
    pass

#系统入口
if __name__ == '__main__':
    main_form()
    


##################################################################################################
#TEST CODE FOR REFERENCE
##################################################################################################
class FirstWindow(QtWidgets.QWidget):
 
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(FirstWindow, self).__init__(parent)
        self.resize(100, 100)
        self.btn = FirstWindow.QToolButton(self)
        self.btn.setText("click")
 
    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()
 
 
class SecondWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(200, 200)
        self.setStyleSheet("background: black")
 
    def handle_click(self):
        if not self.isVisible():
            self.show()
 
    def handle_close(self):
        self.close()

def dialog_widget():
    app = QtWidgets.QApplication(sys.argv)
    dialog = widgetWindowKeo()
    dialog.show()
    #sys.exit(app.exec_())
    pass
  
  
def main_test():
    App = QtWidgets.QApplication(sys.argv)
    first = FirstWindow()
    second = SecondWindow()
    first.btn.clicked.connect(second.handle_click)
    first.btn.clicked.connect(first.hide)
    first.close_signal.connect(first.close)
    first.show()
    sys.exit(App.exec_())
##################################################################################################
    
    
    