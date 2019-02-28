'''
Created on 2017/12/11

@author: hitpony
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
from builtins import int

from PkgAccessEntry import ModAccessCom
from PkgAccessEntry import ModAccessDict
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_PRINTER == True):
    from PkgHstPrinter import ModPrinterGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_DBA == True):
    from PkgHstDba import ModDbaMainEntry
    from PkgHstDba import ModDbaCcl
    from PkgHstDba import ModDbaCebs
    from PkgHstDba import ModDbaF10oam
    from PkgHstDba import ModDbaF11Faam
    from PkgHstDba import ModDbaF1sym
    from PkgHstDba import ModDbaF2cm
    from PkgHstDba import ModDbaF3dm
    from PkgHstDba import ModDbaF4icm
    from PkgHstDba import ModDbaF5fm
    from PkgHstDba import ModDbaF6pm
    from PkgHstDba import ModDbaF7ads
    from PkgHstDba import ModDbaF8psm
    from PkgHstDba import ModDbaF9gism
    from PkgHstDba import ModDbaFaam
    from PkgHstDba import ModDbaFxprcm
    from PkgHstDba import ModDbaGeneral
    from PkgHstDba import ModDbaSnr
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_VISION == True):
    from PkgHstVision import ModVisionGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_AIWGT == True):
    from PkgHstAiwgt import ModAiwgtGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SENSOR == True):
    from PkgHstSensor import ModSensorGeneral    #Sensor access
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SPECIAL == True):
    from PkgHstSpecial import ModSpecialGeneral  #Special Usage
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_MDC == True):
    from PkgHstMdc import ModMdcGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_MPLAYER == True):
    from PkgHstMplayer import ModMplayerGeneral
    from PkgHstMplayer import ModMplayerVrgls
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FACEID == True):
    from PkgHstFaceid import ModFaceidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_CARNUMID == True):
    from PkgHstCarnumid import ModCarnumidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_BILLID == True):
    from PkgHstBillid import ModBillidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_INVOICEID == True):
    from PkgHstInvoiceid import ModInvoiceidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_STEPID == True):
    from PkgHstStepid import ModStepidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_PATID == True):
    from PkgHstPatid import ModPatidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FRUITID == True):
    from PkgHstFruitid import ModFruitidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_VEGID == True):
    from PkgHstVegid import ModVegidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FLOWERID == True):
    from PkgHstFlowerid import ModFloweridGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_ROADWID == True):
    from PkgHstRoadwid import ModRoadwidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_ROADFID == True):
    from PkgHstRoadfid import ModRoadfidGeneral
if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_CEWORM == True):
    from PkgHstCeworm import ModCewormGeneral
    from PkgHstCeworm import ModWhitePicCfy
    from PkgHstCeworm import ModFluPicCfy
    from PkgHstCeworm import ModFccPicCfy
    from PkgHstCeworm import ModWhiteVideoCfy



#固定定义常量
_HST_ACH_CTRL_FLAG_CONTENT_EXT      = 2 #明确有输出内容的，比如READ等指令。这个和自然返回是兼容的，只不过更加明确
_HST_ACH_CTRL_FLAG_MFUN_TREATMENT   = 3 #小丁处理后台服务器MFUN的数据库部分，这样就可以全部兼容了

'''
PRINTER SERVICE
'''
class ClassHuirestPrinterInputCmdHandler:
    __HUIREST_SVTAG = "printer"
    __HUIREST_ACTIONID_PRINTER_min              = 1000
    __HUIREST_ACTIONID_PRINTER_callcell_bfsc    = 1000
    __HUIREST_ACTIONID_PRINTER_callcell_bfdf    = 1001
    __HUIREST_ACTIONID_PRINTER_callcell_bfhs    = 1002
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md1     = 1010
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md2     = 1011
    __HUIREST_ACTIONID_PRINTER_fam_get_mac_addr = 1012
    __HUIREST_ACTIONID_PRINTER_max              = 1999

    
    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
    
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
        
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_PRINTER_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_PRINTER_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfsc):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfsc()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfdf):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfdf()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfhs):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfhs()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_sdqx_md1):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_sdqx_md2):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_get_mac_addr):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            else:
                print("ClassHuirestPrinterInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_PRINTER_min, self.__HUIREST_ACTIONID_PRINTER_max, inputStr['actionId']))
                self.achCtrlFlag = False
        
        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
 


'''

DB ACCESS SERVICE
#对于self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT的处理过程，两种方式是一样的：要么使用True/False来表达，要么直接将json结构封装在返回变量中
#对于这两种方式，最终返回上调用者的消息中，都会封装打包成为完整的带有消息标准头的json结构

'''
class ClassHuirestDbaInputCmdHandler:
    __HUIREST_SVTAG = "dba"
    __HUIREST_ACTIONID_DBA_min                      = 0X07D0
    __HUIREST_ACTIONID_DBA_COMM                     = 0X07D0
    __HUIREST_ACTIONID_DBA_F1sym                    = 0x1100
    __HUIREST_ACTIONID_DBA_F2cm                     = 0x1200
    __HUIREST_ACTIONID_DBA_F3dm                     = 0x1300
    __HUIREST_ACTIONID_DBA_F4icm                    = 0x1400
    __HUIREST_ACTIONID_DBA_F5fm                     = 0x1500
    __HUIREST_ACTIONID_DBA_F6pm                     = 0x1600
    __HUIREST_ACTIONID_DBA_F7ads                    = 0x1700
    __HUIREST_ACTIONID_DBA_F8psm                    = 0x1800
    __HUIREST_ACTIONID_DBA_F9gism                   = 0x1900
    __HUIREST_ACTIONID_DBA_F10oam                   = 0x1A00
    __HUIREST_ACTIONID_DBA_F11faam                  = 0x1B00
    __HUIREST_ACTIONID_DBA_Fxprcm                   = 0x1C00
    __HUIREST_ACTIONID_DBA_F12iwdp                  = 0x1D00
    __HUIREST_ACTIONID_DBA_L2snr                    = 0x1F00

    __HUIREST_ACTIONID_DBA_AQYC                     = 0X0D48
    __HUIREST_ACTIONID_DBA_BFDF                     = 0X0DAC
    __HUIREST_ACTIONID_DBA_BFHS                     = 0X0E10
    __HUIREST_ACTIONID_DBA_CEBS_user_sheet          = 0X0ED7
    __HUIREST_ACTIONID_DBA_CEBS_product_profile     = 0X0ED8
    __HUIREST_ACTIONID_DBA_CEBS_cali_profile        = 0X0ED9
    __HUIREST_ACTIONID_DBA_CEBS_object_profile      = 0X0EDA
    __HUIREST_ACTIONID_DBA_CEBS_config_eleg         = 0X0EDB
    __HUIREST_ACTIONID_DBA_CEBS_config_stackcell    = 0X0EDC
    __HUIREST_ACTIONID_DBA_CEBS_result_eleg         = 0X0EDD
    __HUIREST_ACTIONID_DBA_CEBS_result_stackcell    = 0X0EDE
    __HUIREST_ACTIONID_DBA_FAAM                     = 0X0F3C
    __HUIREST_ACTIONID_DBA_FSTT                     = 0X0FA0
    __HUIREST_ACTIONID_DBA_TEST                     = 0X1004

    __HUIREST_ACTIONID_DBA_CCL                      = 0X0E74
    #END FLAG
    __HUIREST_ACTIONID_DBA_max                      = 0X2000
    
    #Init global control variable
    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
    
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""

    #HUIREST
    def inputCmdHandlerEntry(self,inputStr):
        
        if(inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag=False
        if((inputStr['actionId'] < self.__HUIREST_ACTIONID_DBA_min) and (inputStr['actionId']>self.__HUIREST_ACTIONID_DBA_max)):
            self.achCtrlFlag=False
#         print("this=",inputStr)
#         print(inputStr['restTag'])
#         print(inputStr['actionId'])
#         print(inputStr['parContent'])
         
#         if(inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
#             self.achCtrlFlag=False
        if self.achCtrlFlag == True:
            if inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_COMM:
                self.achProcResult = False
            if inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F1sym:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F1sym_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F2cm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F2cm_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F3dm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F3dm_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F4icm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F4icm_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F5fm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F5fm_Send_Message(inputStr['parContent']) 
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F6pm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F6pm_Send_Message(inputStr['parContent']) 
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F7ads:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F7ads_Send_Message(inputStr['parContent']) 
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F8psm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F8psm_Send_Message(inputStr['parContent'])   
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F9gism:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F9gism_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F10oam:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F10oam_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F11faam:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F11Faam_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_Fxprcm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_Fxprcm_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
                
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F12iwdp:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult=proc.dft_F12Iwdp_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_L2snr:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_Snr_Send_Message(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_MFUN_TREATMENT
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_AQYC:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_BFDF:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_BFHS:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CCL:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_user_sheet:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_user_sheet(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_product_profile:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_product_profile(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_cali_profile:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_cali_profile(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_object_profile:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_object_profile(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_config_eleg:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_config_eleg(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_config_stackcell:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_config_stackcell(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_result_eleg:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_result_eleg(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_result_stackcell:
                if (inputStr['parContent']['cmd']=='read'):
                    self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achContentResExt = proc.dft_cebs_msg_process_result_stackcell(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_FAAM:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_FSTT:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_TEST:
                self.achProcResult = False
            else:
                self.achCtrlFlag=False
        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
            print("output",outputStr)
            return outputStr
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
            return outputStr
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
            return outputStr
        else:
            outputStr['parContent'] = self.achCtrlFlag;
            return outputStr
        #return self.achProcResult
   

'''
#Following part will be surpress for a while, until MATE system solve CV2 and Tensorflow installation issue
VISION SERVICE
'''
class ClassHuirestVisionInputCmdHandler:
    __HUIREST_SVTAG = "vision"
    __HUIREST_ACTIONID_VISION_min                   = 10000
    __HUIREST_ACTIONID_VISION_test1                 = 10001
    __HUIREST_ACTIONID_VISION_test2                 = 10002
    __HUIREST_ACTIONID_VISION_worm_clasify_single   = 10003
    __HUIREST_ACTIONID_VISION_worm_clasify_batch    = 10004
    __HUIREST_ACTIONID_VISION_max                   = 10999
    
    
    achCtrlFlag = False
    achProcResult=''
    achContentResExt = ""
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_VISION_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_VISION_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_test1):
                proc = ModVisionGeneral.ClassModVisionTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_test2):
                proc = ModVisionGeneral.ClassModVisionTest2()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_worm_clasify_single):
                proc = ModVisionGeneral.ClassModVisionWormClasifySingle()
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                self.achContentResExt = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_worm_clasify_batch):
                proc = ModVisionGeneral.ClassModVisionWormClasifyBatch()
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                self.achContentResExt = proc.cmdHandleProcedure(inputStr['parContent'])                
            else:
                print("ClassHuirestVisionInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_VISION_min, self.__HUIREST_ACTIONID_VISION_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
     



'''
AI WEIGHT SERVICE
'''
class ClassHuirestAiwgtInputCmdHandler:
    __HUIREST_SVTAG = "aiwgt"
    __HUIREST_ACTIONID_AIWGT_min                      = 11000
    __HUIREST_ACTIONID_AIWGT_test1                    = 11001
    __HUIREST_ACTIONID_AIWGT_max                      = 11999
    

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_AIWGT_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_AIWGT_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_AIWGT_test1):
                proc = ModAiwgtGeneral.ClassModAiwgtTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestAiwgtInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_AIWGT_min, self.__HUIREST_ACTIONID_AIWGT_max, inputStr['actionId']))
                self.achCtrlFlag = False
        
        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
 
 



'''
SENSOR SERVICE
'''
class ClassHuirestSensorInputCmdHandler:
    __HUIREST_SVTAG = "sensor"
    __HUIREST_ACTIONID_SENSOR_min                      = 12000
    __HUIREST_ACTIONID_SENSOR_test1                    = 12000
    __HUIREST_ACTIONID_SENSOR_max                      = 12999
    
    
    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_SENSOR_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_SENSOR_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_SENSOR_test1):
                proc = ModSensorGeneral.ClassModSensorTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            else:
                print("ClassHuirestSensorInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_SENSOR_min, self.__HUIREST_ACTIONID_SENSOR_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
 

'''
SPECIAL TREATMENT SERVICE
'''
class ClassHuirestSpecialInputCmdHandler:
    __HUIREST_SVTAG = "special"
    __HUIREST_ACTIONID_SPECIAL_min                      = 13000
    __HUIREST_ACTIONID_SPECIAL_test1                    = 13000
    __HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_encode  = 13001
    __HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_decode  = 13002
    __HUIREST_ACTIONID_SPECIAL_max                      = 13999

    
    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_SPECIAL_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_SPECIAL_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_test1):
                proc = ModSpecialGeneral.ClassModSpecialTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_encode):
                proc = ModSpecialGeneral.ClassGtjyWaterMeter()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'], "encoding")
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_decode):
                proc = ModSpecialGeneral.ClassGtjyWaterMeter()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'], "decoding")
            else:
                print("ClassHuirestSpecialInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_SPECIAL_min, self.__HUIREST_ACTIONID_SPECIAL_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
     


'''
MDC SERVICE
'''
class ClassHuirestMdcInputCmdHandler:
    __HUIREST_SVTAG = "mdc"
    __HUIREST_ACTIONID_MDC_min                      = 14000
    __HUIREST_ACTIONID_MDC_test1                    = 14000
    __HUIREST_ACTIONID_MDC_max                      = 14999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_MDC_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_MDC_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_MDC_test1):
                proc = ModMdcGeneral.ClassModMdcTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestMdcInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_MDC_min, self.__HUIREST_ACTIONID_MDC_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
MPLAYER SERVICE
'''
class ClassHuirestMplayerInputCmdHandler:
    __HUIREST_SVTAG = "mplayer"
    __HUIREST_ACTIONID_MPLAYER_min                      = 15000
    __HUIREST_ACTIONID_MPLAYER_play_ctrl                = 15000
    __HUIREST_ACTIONID_MPLAYER_refresh_list             = 15001
    __HUIREST_ACTIONID_MPLAYER_fetch_status             = 15002
    __HUIREST_ACTIONID_MPLAYER_vrgls_ctrl               = 15010
    __HUIREST_ACTIONID_MPLAYER_vrgls_data               = 15011
    __HUIREST_ACTIONID_MPLAYERC_max                     = 15999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_MPLAYER_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_MPLAYERC_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_MPLAYER_play_ctrl):
                proc = ModMplayerGeneral.ClassModMplayerPlayCtrl()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_MPLAYER_refresh_list):
                proc = ModMplayerGeneral.ClassModMplayerRefreshList()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_MPLAYER_fetch_status):
                proc = ModMplayerGeneral.ClassModMplayerFetchStatus()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_MPLAYER_vrgls_data):
                proc = ModMplayerVrgls.ClassModMplayerVrglsData()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestMplayerInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_MPLAYER_min, self.__HUIREST_ACTIONID_MPLAYER_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
FACEID SERVICE
'''
class ClassHuirestFaceidInputCmdHandler:
    __HUIREST_SVTAG = "faceid"
    __HUIREST_ACTIONID_FACEID_min                      = 16000
    __HUIREST_ACTIONID_FACEID_test1                    = 16000
    __HUIREST_ACTIONID_FACEID_max                      = 16999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_FACEID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_FACEID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_FACEID_test1):
                proc = ModFaceidGeneral.ClassModFaceidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestFaceidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_FACEID_min, self.__HUIREST_ACTIONID_FACEID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
CARNUMID SERVICE
'''
class ClassHuirestCarnumidInputCmdHandler:
    __HUIREST_SVTAG = "carmumid"
    __HUIREST_ACTIONID_CARNUMID_min                      = 17000
    __HUIREST_ACTIONID_CARNUMID_test1                    = 17000
    __HUIREST_ACTIONID_CARNUMID_max                      = 17999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_CARNUMID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_CARNUMID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_CARNUMID_test1):
                proc = ModCarnumidGeneral.ClassModCarnumidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestCarnumidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_CARNUMID_min, self.__HUIREST_ACTIONID_CARNUMID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
BILLID SERVICE
'''
class ClassHuirestBillidInputCmdHandler:
    __HUIREST_SVTAG = "billid"
    __HUIREST_ACTIONID_BILLID_min                      = 18000
    __HUIREST_ACTIONID_BILLID_test1                    = 18000
    __HUIREST_ACTIONID_BILLID_max                      = 18999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_BILLID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_BILLID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_BILLID_test1):
                proc = ModBillidGeneral.ClassModBillidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestBillidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_BILLID_min, self.__HUIREST_ACTIONID_BILLID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
INVOICEID SERVICE
'''
class ClassHuirestInvoiceidInputCmdHandler:
    __HUIREST_SVTAG = "invoiceid"
    __HUIREST_ACTIONID_INVOICEID_min                      = 19000
    __HUIREST_ACTIONID_INVOICEID_test1                    = 19000
    __HUIREST_ACTIONID_INVOICEID_max                      = 19999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_INVOICEID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_INVOICEID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_INVOICEID_test1):
                proc = ModInvoiceidGeneral.ClassModInvoiceidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestInvoiceidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_INVOICEID_min, self.__HUIREST_ACTIONID_INVOICEID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
STEPID SERVICE
'''
class ClassHuirestStepidInputCmdHandler:
    __HUIREST_SVTAG = "stepid"
    __HUIREST_ACTIONID_STEPID_min                      = 20000
    __HUIREST_ACTIONID_STEPID_test1                    = 20000
    __HUIREST_ACTIONID_STEPID_max                      = 20999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_STEPID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_STEPID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_STEPID_test1):
                proc = ModStepidGeneral.ClassModStepidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestStepidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_STEPID_min, self.__HUIREST_ACTIONID_STEPID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
PATID SERVICE
'''
class ClassHuirestPatidInputCmdHandler:
    __HUIREST_SVTAG = "patid"
    __HUIREST_ACTIONID_PATID_min                      = 21000
    __HUIREST_ACTIONID_PATID_test1                    = 21000
    __HUIREST_ACTIONID_PATID_max                      = 21999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_PATID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_PATID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_PATID_test1):
                proc = ModPatidGeneral.ClassModPatidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestPatidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_PATID_min, self.__HUIREST_ACTIONID_PATID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
FRUITID SERVICE
'''
class ClassHuirestFruitidInputCmdHandler:
    __HUIREST_SVTAG = "fruitid"
    __HUIREST_ACTIONID_FRUITID_min                      = 22000
    __HUIREST_ACTIONID_FRUITID_test1                    = 22000
    __HUIREST_ACTIONID_FRUITID_max                      = 22999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_FRUITID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_FRUITID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_FRUITID_test1):
                proc = ModFruitidGeneral.ClassModFruitidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestFruitidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_FRUITID_min, self.__HUIREST_ACTIONID_FRUITID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
VEGID SERVICE
'''
class ClassHuirestVegidInputCmdHandler:
    __HUIREST_SVTAG = "vegid"
    __HUIREST_ACTIONID_VEGID_min                      = 23000
    __HUIREST_ACTIONID_VEGID_test1                    = 23000
    __HUIREST_ACTIONID_VEGID_max                      = 23999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_VEGID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_VEGID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_VEGID_test1):
                proc = ModVegidGeneral.ClassModVegidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestVegidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_VEGID_min, self.__HUIREST_ACTIONID_VEGID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
FLOWERID SERVICE
'''
class ClassHuirestFloweridInputCmdHandler:
    __HUIREST_SVTAG = "flowerid"
    __HUIREST_ACTIONID_FLOWERID_min                      = 24000
    __HUIREST_ACTIONID_FLOWERID_test1                    = 24000
    __HUIREST_ACTIONID_FLOWERID_max                      = 24999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_FLOWERID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_FLOWERID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_FLOWERID_test1):
                proc = ModFloweridGeneral.ClassModFloweridTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestFloweridInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_FLOWERID_min, self.__HUIREST_ACTIONID_FLOWERID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
ROADWID SERVICE
'''
class ClassHuirestRoadwidInputCmdHandler:
    __HUIREST_SVTAG = "roadwid"
    __HUIREST_ACTIONID_ROADWID_min                      = 25000
    __HUIREST_ACTIONID_ROADWID_test1                    = 25000
    __HUIREST_ACTIONID_ROADWID_max                      = 25999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_ROADWID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_ROADWID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_ROADWID_test1):
                proc = ModRoadwidGeneral.ClassModRoadwidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestRoadwidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_ROADWID_min, self.__HUIREST_ACTIONID_ROADWID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr


'''
ROADFID SERVICE
'''
class ClassHuirestRoadfidInputCmdHandler:
    __HUIREST_SVTAG = "roadfid"
    __HUIREST_ACTIONID_ROADFID_min                      = 26000
    __HUIREST_ACTIONID_ROADFID_test1                    = 26000
    __HUIREST_ACTIONID_ROADFID_max                      = 26999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_ROADFID_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_ROADFID_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_ROADFID_test1):
                proc = ModRoadfidGeneral.ClassModRoadfidTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestRoadfidInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_ROADFID_min, self.__HUIREST_ACTIONID_ROADFID_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr

'''
CEWORM SERVICE
'''
class ClassHuirestCewormInputCmdHandler:
    __HUIREST_SVTAG = "ceworm"
    __HUIREST_ACTIONID_CEWORM_min                       = 27000
    __HUIREST_ACTIONID_CEWORM_test1                     = 27000
    __HUIREST_ACTIONID_CEWORM_white_pic_cfy             = 27001
    __HUIREST_ACTIONID_CEWORM_flu_pic_cfy               = 27002
    __HUIREST_ACTIONID_CEWORM_fcc_pic_cfy               = 27003
    __HUIREST_ACTIONID_CEWORM_white_video_cfy           = 27004
    __HUIREST_ACTIONID_CEWORM_max                       = 27999

    achCtrlFlag = False
    achProcResult=''
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
        self.achProcResult = ''
        self.achContentResExt = ""
 
    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_CEWORM_min):
            self.achCtrlFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_CEWORM_max):
            self.achCtrlFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag = False;
                     
        #
        if (self.achCtrlFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_CEWORM_test1):
                proc = ModCewormGeneral.ClassModCewormTest1()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_CEWORM_white_pic_cfy):
                proc = ModWhitePicCfy.ClassModCewormWhitePicCfy()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_CEWORM_flu_pic_cfy):
                proc = ModFluPicCfy.ClassModCewormFluPicCfy()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_CEWORM_fcc_pic_cfy):
                proc = ModFccPicCfy.ClassModCewormFccPicCfy()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_CEWORM_white_video_cfy):
                proc = ModWhiteVideoCfy.ClassModCewormWhiteVideoCfy()
                self.achCtrlFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestCewormInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_CEWORM_min, self.__HUIREST_ACTIONID_CEWORM_max, inputStr['actionId']))
                self.achCtrlFlag = False

        #RETURN BACK
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_CONTENT_EXT):
            outputStr['parContent'] = self.achContentResExt;
        elif (self.achCtrlFlag == _HST_ACH_CTRL_FLAG_MFUN_TREATMENT):
            return self.achProcResult
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.achCtrlFlag;
        return outputStr
    
    

    
    


























'''
DBA RELEVANT SERVICE
SPECAL CASE
'''
class ClassHCUReportDataToDba:
    __HCUDATAMSGIDCURRENTREPORT=0X3090
    __HCUDATAMSGIDCPUIDRAND=0X5CFF
    __HCUDATAMSGIDCPUIDREPORT=0XF0C0
    __HCUDATAMSGIDCONFIRM=0XF040

    def __init__(self):
        self.achCtrlFlag = True
    def inputCmdHandlerEntry(self,inputData):
        socketId=inputData['socketid']
        inputData=json.loads(inputData['data'])
        if inputData['ToUsr']!='FSTT' and inputData['ToUsr']!='XHTS':
            self.achCtrlFlag=False
        if self.achCtrlFlag==False:
            return 
        else:
            if inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_YCHOLOPSREPORT:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result = proc.dft_F2cm_Send_Message(socketId,inputData)
                return result
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_YCHEARTREPORT:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F2cm_Heart_Data_Report(socketId, inputData)
                return result
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_NGROKRES_RESP:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F2cm_Ngrok_Restart_Test(socketId, inputData)
                return result
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_SWRESTART_RESP:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F2cm_Hcu_Sw_Restart_Test(socketId, inputData)
                return result
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_LOOP_TEST_RESP:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F2cm_Device_Loop_Test(socketId, inputData)
                return result
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_REBOOT_RESP:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_dbi_device_reboot(socketId, inputData)
                return result  
            
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_YCDATAREPORT:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F3dm_Data_Current_Report(socketId, inputData)
                return result
            
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_SMART_CITY_DATA_REPORT:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F3dm_smart_city_current_report(socketId, inputData)
                return result
            
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_PERFORMANCE_REPORT:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F6pm_HCU_Perform_Data_Report(socketId, inputData)
                return result
            
            elif inputData['MsgId']==ModAccessDict.GOLBALVAR.HUITPJSON_MSGID_INVENTORY_REQ:
                proc=ModDbaMainEntry.ClassHCUDbaMainEntry()
                result=proc.dft_F10oam_HCU_Inventory_Report(socketId, inputData)
                return result

            else:
                return
                
            
        







    