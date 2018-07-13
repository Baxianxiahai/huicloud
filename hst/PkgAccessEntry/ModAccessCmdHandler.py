'''
Created on 2017骞�12鏈�11鏃�

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
#from http.server import BaseHTTPRequestHandler, HTTPServer

#
from PkgHstPrinter import ModPrinterGeneral
from PkgHstDba import ModDbaMainEntry
from PkgHstVision import ModVisionGeneral
from PkgHstAiwgt import ModAiwgtGeneral
from PkgHstSensor import ModSensorGeneral    #Sensor access
from PkgHstSpecial import ModSpecialGeneral  #Special Usage
from builtins import int

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
    __HUIREST_ACTIONID_PRINTER_min              = 1000
    __HUIREST_ACTIONID_PRINTER_callcell_bfsc    = 1000
    __HUIREST_ACTIONID_PRINTER_callcell_bfdf    = 1001
    __HUIREST_ACTIONID_PRINTER_callcell_bfhs    = 1002
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md1     = 1010
    __HUIREST_ACTIONID_PRINTER_fam_sdqx_md2     = 1011
    __HUIREST_ACTIONID_PRINTER_fam_get_mac_addr = 1012
    __HUIREST_ACTIONID_PRINTER_max     = 1020
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_PRINTER_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_PRINTER_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
        
        #
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
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_sdqx_md1):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_sdqx_md2):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_PRINTER_fam_get_mac_addr):
                proc = ModPrinterGeneral.ClassPrinterFaam()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])                
            else:
                print("ClassHuirestPrinterInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_PRINTER_min, self.__HUIREST_ACTIONID_PRINTER_max, inputStr['actionId']))
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
 
#
class ClassHuirestDbaInputCmdHandler:
    __HUIREST_SVTAG = "dba"
    __HUIREST_ACTIONID_DBA_min                      = 0x1000
    __HUIREST_ACTIONID_DBA_F1sym                    = 0x1100
    __HUIREST_ACTIONID_DBA_F2cm                     = 0x1200
    __HUIREST_ACTIONID_DBA_F3dm                     = 0x1300
    __HUIREST_ACTIONID_DBA_F4icm                    = 0x1400
    __HUIREST_ACTIONID_DBA_F5fm                     = 0x1500
    __HUIREST_ACTIONID_DBA_F6pm                     = 0x1600
    __HUIREST_ACTIONID_DBA_F7ads                    = 0x1700
    __HUIREST_ACTIONID_DBA_F8psm                    = 0x1800
    __HUIREST_ACTIONID_DBA_F9gism                   = 0x1900
    __HUIREST_ACTIONID_DBA_F11faam                  = 0x1B00
    __HUIREST_ACTIONID_DBA_L2snr                    = 0x1F00
    #END FLAG
    __HUIREST_ACTIONID_DBA_max                      = 0X2000
    
    #Init global control variable
    publicOutputResultFlag = False
    publicReturnResult=''
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST
    def inputCmdHandlerEntry(self,inputStr):
        if(inputStr['restTag']!=self.__HUIREST_SVTAG):
            self.publicOutputResultFlag=False
        if((inputStr['actionId']<self.__HUIREST_ACTIONID_DBA_min)and (inputStr['actionId']>self.__HUIREST_ACTIONID_DBA_max)):
            self.publicOutputResultFlag=False
        if(inputStr['parFlag']!=int(True) and inputStr['parFlag']!=int(False)):
            self.publicOutputResultFlag=False
        if self.publicOutputResultFlag==True:
            if inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F1sym:
                proc=ModDbaMainEntry.ClassDbaF1symMainEntry()
                self.publicReturnResult = proc.dft_F1sym_Send_Message(inputStr['parContent'])    
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F2cm:
                pass
            if inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F3dm:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F4icm:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F5fm:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F6pm:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F7ads:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F8psm:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F9gism:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_F11faam:
                pass
            elif inputStr["actionId"]==self.__HUIREST_ACTIONID_DBA_L2snr:
                pass
        else:
            self.publicOutputResultFlag==False
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
        return self.publicReturnResult
#         return outputStr
   
#     def inputCmdHandlerEntry(self, inputStr):
#         #
#         print(inputStr)
#         if (inputStr['restTag'] != self.__HUIREST_SVTAG):
#             self.publicOutputResultFlag = False;
#         if (inputStr['actionId'] < self.__HUIREST_ACTIONID_DBA_min):
#             self.publicOutputResultFlag = False;
#         if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_DBA_max):
#             self.publicOutputResultFlag = False;
#         if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
#             self.publicOutputResultFlag = False;
#                 
#         #
#         if (self.publicOutputResultFlag == True):
#             if (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_F1sym):
#                 proc = ModDbaGeneral.ClassDbaTempUpdate()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])     
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_django_test_case1):
#                 proc = ModDbaGeneral.ClassDbaDjangoTest()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_comm_user_group_access):
#                 proc = ModDbaGeneral.ClassDbaCommUserGroup()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_comm_user_account_access):
#                 proc = ModDbaGeneral.ClassDbaCommUserAccount()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_cebs_customer_mission_access):
#                 proc = ModDbaGeneral.ClassDbaCebsCustomerMission()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_cebs_classify_exec_log_access):
#                 proc = ModDbaGeneral.ClassDbaCebsClassifyExecLog()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_water_meter_access):
#                 proc = ModDbaCcl.ClassDbaCclWaterMeterOpr()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_gas_meter_access):
#                 proc = ModDbaCcl.ClassDbaCclGasMeterOpr()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_ccl_power_meter_access):
#                 proc = ModDbaCcl.ClassDbaCclPowerMeterOpr()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             elif (inputStr['actionId'] == self.__HUIREST_ACTIONID_DBA_faam_user_group_access):
#                 proc = ModDbaFaam.ClassDbaFaamProductionGoodsOpr()
#                 self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])
#             else:
#                 print("ClassHuirestDbaInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_DBA_min, self.__HUIREST_ACTIONID_DBA_max, inputStr['actionId']))
#                 self.publicOutputResultFlag = False
#         #
#         outputStr= {}
#         outputStr['restTag'] = self.__HUIREST_SVTAG;
#         outputStr['actionId'] = inputStr["actionId"];
#         outputStr['parFlag'] = int(True);
#         parContentStrSuc={'sucFlag':int(True), 'errCode':0}
#         parContentStrErr={'sucFlag':int(False), 'errCode':1}
#         if (self.publicOutputResultFlag == True):
#             outputStr['parContent'] = parContentStrSuc;
#         else:
#             outputStr['parContent'] = parContentStrErr;
#         return outputStr
    
#
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

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_VISION_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_VISION_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #
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
        #
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
    
#
class ClassHuirestAiwgtInputCmdHandler:
    __HUIREST_SVTAG = "aiwgt"
    __HUIREST_ACTIONID_AIWGT_min                      = 0x3000
    __HUIREST_ACTIONID_AIWGT_test1                    = 0x3000
    __HUIREST_ACTIONID_AIWGT_max                      = 0x3001
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_AIWGT_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_AIWGT_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_AIWGT_test1):
                proc = ModAiwgtGeneral.ClassModAiwgtTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestAiwgtInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_AIWGT_min, self.__HUIREST_ACTIONID_AIWGT_max, inputStr['actionId']))
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


#
class ClassHuirestSensorInputCmdHandler:
    __HUIREST_SVTAG = "sensor"
    __HUIREST_ACTIONID_SENSOR_min                      = 0x4000
    __HUIREST_ACTIONID_SENSOR_test1                    = 0x4000
    __HUIREST_ACTIONID_SENSOR_max                      = 0x400F
    publicOutputResultFlag = False
    
    def __init__(self):
        self.publicOutputResultFlag = True

    #HUIREST
    def inputCmdHandlerEntry(self, inputStr):
        #
        if (inputStr['restTag'] != self.__HUIREST_SVTAG):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] < self.__HUIREST_ACTIONID_SENSOR_min):
            self.publicOutputResultFlag = False;
        if (inputStr['actionId'] >= self.__HUIREST_ACTIONID_SENSOR_max):
            self.publicOutputResultFlag = False;
        if (inputStr['parFlag'] != int(True) and inputStr['parFlag'] != int(False)):
            self.publicOutputResultFlag = False;
                    
        #
        if (self.publicOutputResultFlag == True):
            if (inputStr['actionId'] == self.__HUIREST_ACTIONID_SENSOR_test1):
                proc = ModSensorGeneral.ClassModSensorTest1()
                self.publicOutputResultFlag = proc.cmdHandleProcedure(inputStr['parContent'])          
            else:
                print("ClassHuirestSensorInputCmdHandler: Error ActionId Received! Min-Max=(%d, %d) while actual=%d" % (self.__HUIREST_ACTIONID_SENSOR_min, self.__HUIREST_ACTIONID_SENSOR_max, inputStr['actionId']))
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







    