'''
Created on 2018/2/23

#
MODDULE: FMPT2 Ihu Connection Data Management

@author: Administrator
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
import struct
from ctypes import *
#import numpy as np
import math


#Local include
from PkgFmptHandler import ModFmptCom

class ClassDrvSps(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
        '''
        Constructor
        '''



class ClassDrvCan(object):
    '''
    classdocs
    '''
    '''
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_OpenDevice(UInt32 DeviceType, UInt32 DeviceInd, UInt32 Reserved);
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_CloseDevice(UInt32 DeviceType, UInt32 DeviceInd);
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_InitCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_INIT_CONFIG pInitConfig);
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_StartCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd);
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_ResetCAN(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd);
    '''
    zStrFmptCanVciInitConfig = {\
        "AccCode": 0,\
        "AccMask": 0,\
        "Reserved": 0,\
        "Filter": 0,\
        "Timing0": 0,\
        "Timing1": 0,\
        "Mode": 0\
    }
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.zStrFmptCanVciInitConfig = {\
            "AccCode": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_RCVCODE,\
            "AccMask": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_MASKCODE,\
            "Reserved": 0,\
            "Filter": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_FILTER,\
            "Timing0": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_TIMER0,\
            "Timing1": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_TIMER1,\
            "Mode": ModFmptCom.GL_FMPT_DEVDRIVE_CAN_WORKMODE\
        }
        
        
    #Starting to connect
    def FuncDrvCanInitStart(self):
        res = 0;

        #Open
        strDllPath = sys.path[0] + str(os.sep) + "ControlCAN.dll"
        print("strDllPath = ", strDllPath)
        objDll = cdll.LoadLibrary(strDllPath)
        api  = objDll.VCI_OpenDevice;
        api.argtypes = [c_uint, c_uint, c_uint];
        api.restypes = c_uint;
        #callRes = api(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND);
        for port1 in range(1, 33):
            for index in range(0, 10):
                callRes = api(port1, index, 0);
                print("Dev=%d, Index=%d, callRes=%d" % (port1, index, callRes))
                if callRes == 1:
                    print("Result find!")
        
        if (callRes == 0):
            res = -1;
            return res;

        #Microsoft API use small endian
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = ">IIIBBBB";  #Small ones
        else:
            fmt = "<IIIBBBB";  #Big ones
        vciConfigData = struct.pack(fmt, \
           self.zStrFmptCanVciInitConfig['AccCode'],\
           self.zStrFmptCanVciInitConfig['AccMask'],\
           self.zStrFmptCanVciInitConfig['Reserved'],\
           self.zStrFmptCanVciInitConfig['Filter'],\
           self.zStrFmptCanVciInitConfig['Timing0'],\
           self.zStrFmptCanVciInitConfig['Timing1'],\
           self.zStrFmptCanVciInitConfig['Mode'])
        print(vciConfigData)
                
        #Config
        api  = objDll.VCI_InitCAN;
        api.argtypes = [c_uint, c_uint, c_uint, c_void_p];
        api.restypes = c_uint;
        callRes = api(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND, vciConfigData);
        if (callRes == 0):
            res = -2;
            return res;
        
        #StartCan
        api  = objDll.VCI_StartCAN;
        api.argtypes = [c_uint, c_uint, c_uint];
        api.restypes = c_uint;
        callRes = api(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND);
        if (callRes == 0):
            res = -3;
            return res;
        
        #Finally feedback
        res = 1;
        return res;

            
    #DISCONNECT
    def FuncCanDisconnect(self):
        try:
            strDllPath = sys.path[0] + str(os.sep) + "ControlCAN.dll"
            objDll = cdll.LoadLibrary(strDllPath)
            api  = objDll.VCI_CloseDevice;
            api.argtypes = [c_uint, c_uint];
            api.restypes = c_uint;
            callRes = api(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND);
            if (callRes == 0):
                res = -1;
            else:
                res = 1;
        except Exception as err:  
            print(err)
            res = -2;
            return res;
        finally:
            return res;


    #DISCONNECT
    def FuncCanReset(self):
        try:
            strDllPath = sys.path[0] + str(os.sep) + "ControlCAN.dll"
            objDll = cdll.LoadLibrary(strDllPath)
            api  = objDll.VCI_ResetCAN;
            api.argtypes = [c_uint, c_uint, c_uint];
            api.restypes = c_uint;
            callRes = api(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND);
            if (callRes == 0):
                res = -1;
            else:
                res = 1;
        except Exception as err:  
            print(err)
            res = -2;
            return res;
        finally:
            return res;

class ClassDrvEth(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
        '''
        Constructor
        '''









    
    