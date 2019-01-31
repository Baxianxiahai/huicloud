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

#固定定义常量
_HST_ACH_CTRL_FLAG_CONTENT_EXT = 2

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
    achContentResExt=''
    
    def __init__(self):
        self.achCtrlFlag = True
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
    __HUIREST_ACTIONID_DBA_min                      = 2000
    __HUIREST_ACTIONID_DBA_COMM                     = 2000
    __HUIREST_ACTIONID_DBA_F1sym                    = 2100
    __HUIREST_ACTIONID_DBA_F2cm                     = 2200
    __HUIREST_ACTIONID_DBA_F3dm                     = 2300
    __HUIREST_ACTIONID_DBA_F4icm                    = 2400
    __HUIREST_ACTIONID_DBA_F5fm                     = 2500
    __HUIREST_ACTIONID_DBA_F6pm                     = 2600
    __HUIREST_ACTIONID_DBA_F7ads                    = 2700
    __HUIREST_ACTIONID_DBA_F8psm                    = 2800
    __HUIREST_ACTIONID_DBA_F9gism                   = 2900
    __HUIREST_ACTIONID_DBA_F10oam                   = 3000
    __HUIREST_ACTIONID_DBA_F11faam                  = 3100
    __HUIREST_ACTIONID_DBA_Fxprcm                   = 3200
    __HUIREST_ACTIONID_DBA_L2snr                    = 3300
    __HUIREST_ACTIONID_DBA_AQYC                     = 3400
    __HUIREST_ACTIONID_DBA_BFDF                     = 3500
    __HUIREST_ACTIONID_DBA_BFHS                     = 3600
    __HUIREST_ACTIONID_DBA_CCL                      = 3700
    __HUIREST_ACTIONID_DBA_CEBS_env                 = 3800
    __HUIREST_ACTIONID_DBA_CEBS_counter             = 3801
    __HUIREST_ACTIONID_DBA_CEBS_fspc                = 3802
    __HUIREST_ACTIONID_DBA_CEBS_file                = 3803
    __HUIREST_ACTIONID_DBA_FAAM                     = 3900
    __HUIREST_ACTIONID_DBA_FSTT                     = 4000
    __HUIREST_ACTIONID_DBA_TEST                     = 4100
    
    #END FLAG
    __HUIREST_ACTIONID_DBA_max                      = 9999
    
    #Init global control variable
    achCtrlFlag = False
    achContentResExt=''
    
    def __init__(self):
        self.achCtrlFlag = True
        self.achContentResExt = ""

    #HUIREST
    def inputCmdHandlerEntry(self,inputStr):
        if(inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.achCtrlFlag=False
        if((inputStr['actionId'] < self.__HUIREST_ACTIONID_DBA_min) and (inputStr['actionId']>self.__HUIREST_ACTIONID_DBA_max)):
            self.achCtrlFlag=False
        if(inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.achCtrlFlag=False
            
        if self.achCtrlFlag == True:
            if inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_COMM:
                self.achProcResult = False
            if inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F1sym:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F1sym_Send_Message(inputStr['parContent'])  
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F2cm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F2cm_Send_Message(inputStr['parContent'])
            if inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F3dm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F3dm_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F4icm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F4icm_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F5fm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F5fm_Send_Message(inputStr['parContent']) 
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F6pm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F6pm_Send_Message(inputStr['parContent']) 
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F7ads:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F7ads_Send_Message(inputStr['parContent']) 
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F8psm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F8psm_Send_Message(inputStr['parContent'])   
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F9gism:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F9gism_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F10oam:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F10oam_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_F11faam:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_F11Faam_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_Fxprcm:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_Fxprcm_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_L2snr:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_Snr_Send_Message(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_AQYC:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_BFDF:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_BFHS:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CCL:
                self.achProcResult = False
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_env:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_cebs_msg_process_env(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_counter:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                #self.achProcResult = proc.dft_cebs_msg_process_counter(inputStr['parContent'])
                self.achCtrlFlag = _HST_ACH_CTRL_FLAG_CONTENT_EXT
                self.achContentResExt = proc.dft_cebs_msg_process_counter(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_fspc:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_cebs_msg_process_fspc(inputStr['parContent'])
            elif inputStr["actionId"] == self.__HUIREST_ACTIONID_DBA_CEBS_file:
                proc=ModDbaMainEntry.ClassDbaMainEntry()
                self.achProcResult = proc.dft_cebs_msg_process_file(inputStr['parContent'])
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
        elif (self.achCtrlFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.achCtrlFlag == False):
            outputStr['parContent'] = parContentStrErr;
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
    achContentResExt = ""
     
    def __init__(self):
        self.achCtrlFlag = True
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
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
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
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
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
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
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
    achContentResExt=''
     
    def __init__(self):
        self.achCtrlFlag = True
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
                
            
        







    