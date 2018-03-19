'''
Created on 2017骞�12鏈�11鏃�

@author: hitpony
'''

import random
import sys
import time
import json
import os   #Python鐨勬爣鍑嗗簱涓殑os妯″潡鍖呭惈鏅亶鐨勬搷浣滅郴缁熷姛鑳�  
import re   #寮曞叆姝ｅ垯琛ㄨ揪寮忓璞�  
import urllib   #鐢ㄤ簬瀵筓RL杩涜缂栬В鐮�  
import http
import socket
#from http.server import BaseHTTPRequestHandler, HTTPServer

#
from PkgHstPrinter import ModPrinterGeneral
from PkgHstDba import ModDbaGeneral
from PkgHstDba import ModDbaCcl
from PkgHstDba import ModDbaFaam
from PkgHstVision import ModVisionGeneral
from PkgHstAiwgt import ModAiwgtGeneral
from PkgHstSensor import ModSensorGeneral    #Sensor access
from PkgHstSpecial import ModSpecialGeneral  #Special Usage

class ClassEntryCmdHandler:
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

#
class ClassHuirestPrinterInputCmdHandler:
    __HUIREST_SVTAG = "printer"
    __HUIREST_ACTIONID_PRINTER_min              = 0x0100
    __HUIREST_ACTIONID_PRINTER_callcell_bfsc    = 0x0100
    __HUIREST_ACTIONID_PRINTER_callcell_bfdf    = 0x0101
    __HUIREST_ACTIONID_PRINTER_callcell_bfhs    = 0x0102
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md1     = 0x0110,
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md2     = 0x0111, 
    __HUIREST_ACTIONID_PRINTER_max     = 0x0112
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST鎸囦护澶勭悊杩囩▼
    def inputCmdHandlerEntry(self, inputStr):
        #鍩虹鏍煎紡鍒ゅ畾
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_PRINTER_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_PRINTER_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
        
        #璋冪敤鍒嗙被澶勭悊杩囩▼
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfsc):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfsc()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfdf):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfdf()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_callcell_bfhs):
                proc = ModPrinterGeneral.ClassPrinterCallcellBfhs()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            else:
                print("ClassHuirestPrinterInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_PRINTER_min, self.__HUIREST_ACTIONID_PRINTER_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #杈撳嚭鍐呭
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.publicOutputResultFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.publicOutputResultFlag;
        return outputStr
 
#鏀跺埌鍚庣殑鎸囦护锛岃繘琛屽鐞嗙殑杩囩▼
class ClassHuirestDbaInputCmdHandler:
    __HUIREST_SVTAG = "dba"
    __HUIREST_ACTIONID_DBA_min                      = 0x1000
    __HUIREST_ACTIONID_DBA_yczx_temp_update         = 0x1000
    __HUIREST_ACTIONID_DBA_django_test_case1        = 0x1001
    
    __HUIREST_ACTIONID_DBA_comm_user_group_access   = 0x1002
    __HUIREST_ACTIONID_DBA_comm_user_account_access = 0x1003

    __HUIREST_ACTIONID_DBA_cebs_customer_mission_access = 0x1004
    __HUIREST_ACTIONID_DBA_cebs_classify_exec_log_access = 0x1005
    
    __HUIREST_ACTIONID_DBA_ccl_water_meter_access = 0x1010
    __HUIREST_ACTIONID_DBA_ccl_gas_meter_access =   0x1011
    __HUIREST_ACTIONID_DBA_ccl_power_meter_access = 0x1012

    __HUIREST_ACTIONID_DBA_faam_user_group_access = 0x1020

    
    #END FLAG
    __HUIREST_ACTIONID_DBA_max                      = 0x1030
    
    #Init global control variable
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST鎸囦护澶勭悊杩囩▼
    def inputCmdHandlerEntry(self, inputStr):
        #鍩虹鏍煎紡鍒ゅ畾
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_DBA_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_DBA_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                
        #璋冪敤鍒嗙被澶勭悊杩囩▼
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_yczx_temp_update):
                proc = ModDbaGeneral.ClassDbaTempUpdate()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])     
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_django_test_case1):
                proc = ModDbaGeneral.ClassDbaDjangoTest()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_comm_user_group_access):
                proc = ModDbaGeneral.ClassDbaCommUserGroup()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_comm_user_account_access):
                proc = ModDbaGeneral.ClassDbaCommUserAccount()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_cebs_customer_mission_access):
                proc = ModDbaGeneral.ClassDbaCebsCustomerMission()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_cebs_classify_exec_log_access):
                proc = ModDbaGeneral.ClassDbaCebsClassifyExecLog()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_water_meter_access):
                proc = ModDbaCcl.ClassDbaCclWaterMeterOpr()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_gas_meter_access):
                proc = ModDbaCcl.ClassDbaCclGasMeterOpr()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_power_meter_access):
                proc = ModDbaCcl.ClassDbaCclPowerMeterOpr()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_faam_user_group_access):
                proc = ModDbaFaam.ClassDbaFaamProductionGoodsOpr()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            else:
                print("ClassHuirestDbaInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_DBA_min, self.__HUIREST_ACTIONID_DBA_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #杈撳嚭鍐呭
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        else:
            outputStr['parContent'] = parContentStrErr;
        return outputStr
    
#鏀跺埌鍚庣殑鎸囦护锛岃繘琛屽鐞嗙殑杩囩▼
class ClassHuirestVisionInputCmdHandler:
    __HUIREST_SVTAG = "vision"
    __HUIREST_ACTIONID_VISION_min     = 0x2000
    __HUIREST_ACTIONID_VISION_test1   = 0x2000
    __HUIREST_ACTIONID_VISION_test2   = 0x2001
    __HUIREST_ACTIONID_VISION_worm_clasify_single   = 0x2002
    __HUIREST_ACTIONID_VISION_worm_clasify_batch    = 0x2003
    __HUIREST_ACTIONID_VISION_max     = 0x2004
    publicOutputResultFlag = False
    parContentStrExt = ""
    
    def __init__(self):
        self.publicOutputResultFlag = True
        self.parContentStrExt = ""

    #HUIREST鎸囦护澶勭悊杩囩▼
    def inputCmdHandlerEntry(self, inputStr):
        #鍩虹鏍煎紡鍒ゅ畾
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_VISION_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_VISION_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #璋冪敤鍒嗙被澶勭悊杩囩▼
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_test1):
                #proc = ClassHuirestVisionActionTest1Handler()
                proc = ModVisionGeneral.ClassModVisionTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_test2):
                proc = ModVisionGeneral.ClassModVisionTest2()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_worm_clasify_single):
                proc = ModVisionGeneral.ClassModVisionWormClasifySingle()
                self.publicOutputResultFlag = 2
                self.parContentStrExt = proc.cmdHandleProcedure(inputStr['parContent'])
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_VISION_worm_clasify_batch):
                proc = ModVisionGeneral.ClassModVisionWormClasifyBatch()
                self.publicOutputResultFlag = 2
                self.parContentStrExt = proc.cmdHandleProcedure(inputStr['parContent'])                
            else:
                print("ClassHuirestVisionInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_VISION_min, self.__HUIREST_ACTIONID_VISION_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #杈撳嚭鍐呭
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == 2):
            outputStr['parContent'] = self.parContentStrExt;
        elif (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        else:
            outputStr['parContent'] = parContentStrErr;
        return outputStr
    
#鏀跺埌鍚庣殑鎸囦护锛岃繘琛屽鐞嗙殑杩囩▼
class ClassHuirestAiwgtInputCmdHandler:
    __HUIREST_SVTAG = "aiwgt"
    __HUIREST_ACTIONID_AIWGT_min                      = 0x3000
    __HUIREST_ACTIONID_AIWGT_test1                    = 0x3000
    __HUIREST_ACTIONID_AIWGT_max                      = 0x3001
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST鎸囦护澶勭悊杩囩▼
    def inputCmdHandlerEntry(self, inputStr):
        #鍩虹鏍煎紡鍒ゅ畾
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_AIWGT_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_AIWGT_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #璋冪敤鍒嗙被澶勭悊杩囩▼
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_AIWGT_test1):
                proc = ModAiwgtGeneral.ClassModAiwgtTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestAiwgtInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_AIWGT_min, self.__HUIREST_ACTIONID_AIWGT_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #杈撳嚭鍐呭
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.publicOutputResultFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.publicOutputResultFlag;
        return outputStr


#鏀跺埌鍚庣殑鎸囦护锛岃繘琛屽鐞嗙殑杩囩▼
class ClassHuirestSensorInputCmdHandler:
    __HUIREST_SVTAG = "sensor"
    __HUIREST_ACTIONID_SENSOR_min                      = 0x4000
    __HUIREST_ACTIONID_SENSOR_test1                    = 0x4000
    __HUIREST_ACTIONID_SENSOR_max                      = 0x400F
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST鎸囦护澶勭悊杩囩▼
    def inputCmdHandlerEntry(self, inputStr):
        #鍩虹鏍煎紡鍒ゅ畾
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_SENSOR_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_SENSOR_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #璋冪敤鍒嗙被澶勭悊杩囩▼
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_SENSOR_test1):
                proc = ModSensorGeneral.ClassModSensorTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestSensorInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_SENSOR_min, self.__HUIREST_ACTIONID_SENSOR_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #杈撳嚭鍐呭
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.publicOutputResultFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.publicOutputResultFlag;
        return outputStr


#
class ClassHuirestSpecialInputCmdHandler:
    __HUIREST_SVTAG = "special"
    __HUIREST_ACTIONID_SPECIAL_min                      = 0x5000
    __HUIREST_ACTIONID_SPECIAL_test1                    = 0x5000
    __HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_encode  = 0x5001
    __HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_decode  = 0x5002
    __HUIREST_ACTIONID_SPECIAL_max                      = 0x500F
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_SPECIAL_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_SPECIAL_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_test1):
                proc = ModSpecialGeneral.ClassModSpecialTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_encode):
                proc = ModSpecialGeneral.ClassGtjyWaterMeter()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'], "encoding")
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_SPECIAL_GTJY_water_meter_decode):
                proc = ModSpecialGeneral.ClassGtjyWaterMeter()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'], "decoding")
            else:
                print("ClassHuirestSpecialInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_SPECIAL_min, self.__HUIREST_ACTIONID_SPECIAL_max, inputStr['actionId']))
                self.publicOutputResultFlag = False
        #
        outputStr= {}
        outputStr['restTag'] = self.__HUIREST_SVTAG;
        outputStr['actionId'] = inputStr["actionId"];
        outputStr['parFlag'] = int(True);
        parContentStrSuc={'sucFlag':int(True), 'errCode':0}
        parContentStrErr={'sucFlag':int(False), 'errCode':1}
        if (self.publicOutputResultFlag == True):
            outputStr['parContent'] = parContentStrSuc;
        elif (self.publicOutputResultFlag == False):
            outputStr['parContent'] = parContentStrErr;
        else:
            outputStr['parContent'] = self.publicOutputResultFlag;
        return outputStr







    
            