'''
Created on 2018/2/23

#
MODDULE: FMPT2 Ihu Connection Data Management

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
import struct
from ctypes import *
#import numpy as np
import math

#Local include
from PkgFmptHandler import ModFmptCom
from PkgFmptHandler import ModFmptIhuDrv

class ClassConnProc(object):
    
    zStrFmptIhuConL2FrameStdFrame = {\
        "start": 0,\
        "chksum": 0,\
        # the length including the size of header
        "len": 0,\
        "buf": b"01"\
        }
     
    zStrFmptIhuConL2VciCanObj = {\
        "ID": 0,\
        "TimeStamp": 0,\
        "TimeFlag": 0,\
        "SendType": 0,\
        "RemoteFlag": 0,\
        "ExternFlag": 0,\
        "DataLen": 0,\
        #b"01234567"
        "Data": 0,\
        "Reserved": 0\
        }
     
    zStrFmptIhuConL3IapFlashRawCommandReq = {\
        "msgid": 0,\
        "length": 0,\
        "flashRawCommandMode": 0,\
        "flashRawCommand": 0,\
        "flashSectorIdToErase": 0,\
        "flashSectorNumberToErase": 0,\
        "flashAddressToAccess": 0,\
        "flashValidLengthToAccess": 0,\
        "data": 0,\
        }
    
    zStrFmptIhuConL3IapFlashRawCommandResp = {\
        "msgid": 0,\
        "length": 0,\
        "flashRawCommandModeResp": 0,\
        "flashRawCommandResp": 0,\
        "flashSectorIdToErase": 0,\
        "flashSectorNumberToErase": 0,\
        "flashAddressToAccess": 0,\
        "flashValidLengthToAccess": 0,\
        "data": 0\
        }
    
    zStrIhuConL3_L3IapFlashRawCommandReq_fix_len = 16;
    zStrIhuConL3_L3IapFlashRawCommandResp_fix_len = 16;
    zStrIhuConL3_remoteflag = 0;
    zStrIhuConL3_extflag = 0;
    zStrIhuConL3_id = 0;

    '''
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_Transmit(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pSend, UInt32 Len);
    [DllImport("controlcan.dll")]
    static extern UInt32 VCI_Receive(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pReceive, UInt32 Len, Int32 WaitTime);
    '''
    
    #Init this class
    def __init__(self):
        self.zStrFmptIhuConL2FrameStdFrame = {\
            "start": 0,\
            "chksum": 0,\
            # the length including the size of header
            "len": 0,\
            #"buf": np.zeros((1, ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA))\
            "buf": b"01"\
            }
          
        self.zStrFmptIhuConL2VciCanObj = {\
            "ID": 0,\
            "TimeStamp": 0,\
            "TimeFlag": 0,\
            "SendType": 0,\
            "RemoteFlag": 0,\
            "ExternFlag": 0,\
            "DataLen": 0,\
            "Data": [0]*8,\
            "Reserved": [0]*3\
            }
        
        self.zStrFmptIhuConL3IapFlashRawCommandReq = {\
            "msgid": 0,\
            "length": 0,\
            "flashRawCommandMode": 0,\
            "flashRawCommand": 0,\
            "flashSectorIdToErase": 0,\
            "flashSectorNumberToErase": 0,\
            "flashAddressToAccess": 0,\
            "flashValidLengthToAccess": 0,\
            #Same effectiveness as next line clarification
            #"data": [0 for n in range(ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA)],
            "data": [0]*ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA,\
            }
      
        self.zStrFmptIhuConL3IapFlashRawCommandResp = {\
            "msgid": 0,\
            "length": 0,\
            "flashRawCommandModeResp": 0,\
            "flashRawCommandResp": 0,\
            "flashSectorIdToErase": 0,\
            "flashSectorNumberToErase": 0,\
            "flashAddressToAccess": 0,\
            "flashValidLengthToAccess": 0,\
            "data": [0]*ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA,\
            }
        
        self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len = 16;
        self.zStrIhuConL3_L3IapFlashRawCommandResp_fix_len = 16;

    def HUITP_ENDIAN_EXG16(self, x):
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            return (((x & 0x0FF00) >> 8) | ((x & 0x00FF) << 8));
        else:
            return x;

    def HUITP_ENDIAN_EXG32(self, x):
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            return (((x & 0xFF000000) >> 24) | ((x & 0x00FF0000) >> 8) | ((x & 0x0000FF00) << 8) | ((x & 0x000000FF) << 24));
        else:
            return x;

    def FuncCaculate_BufOnly_L3IapFlashRawCommandReq(self):
        return ((ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA + self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len -4)&0xFFFF);

    def FuncCaculate_StrTotal_L3IapFlashRawCommandReq(self):
        return ((self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq() + 4)&0xFFFF);

    def FuncCaculate_L2frameTotal_StdFrame(self):
        return (ModFmptCom.GL_FMPT_MAX_GEN_CONTROL_MSG_LEN & 0xFFFF);


    #Read FLASH buffer function
    #Input funIndex=9999, means test and shall return back immediately
    #return res[]
    def FuncReadRegister(self, flashAddr, dataLen, funIndex):
        res = {}
        res['res'] = 0;
        
        #RETURN test
        if (funIndex == 9999):
            res['res'] = 1;
            res['value'] = [int(random.random()*100)]*dataLen;
            return res;
        
        #check parameters
        if ((dataLen <= 0) or (dataLen > ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA)):
            res['res'] = -1;
            return res

        #L3 message content
        self.zStrFmptIhuConL3IapFlashRawCommandReq['msgid'] = self.HUITP_ENDIAN_EXG16(ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['length'] = self.HUITP_ENDIAN_EXG16(self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq());
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommandMode'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommand'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_READ;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashAddressToAccess'] = self.HUITP_ENDIAN_EXG32(flashAddr);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashValidLengthToAccess'] = self.HUITP_ENDIAN_EXG32(dataLen);
        #L2 Frame header
        self.zStrFmptIhuConL2FrameStdFrame['start'] = ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR;
        self.zStrFmptIhuConL2FrameStdFrame['len'] = (self.FuncCaculate_L2frameTotal_StdFrame());
        self.zStrFmptIhuConL2FrameStdFrame['chksum'] = (self.zStrFmptIhuConL2FrameStdFrame['start']&0xFF) ^ (self.zStrFmptIhuConL2FrameStdFrame['len']&0xFF) ^ ((self.zStrFmptIhuConL2FrameStdFrame['len']>>8)& 0xFF);
        self.zStrFmptIhuConL2FrameStdFrame['buf'] = self.zStrFmptIhuConL3IapFlashRawCommandReq;
        #print("Read Register L2Frame: ", self.zStrFmptIhuConL2FrameStdFrame);
        
        #Small endian to encode all the data part
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = "<BHBHHBBBBII";
        else:
            fmt = ">BHBHHBBBBII";
        byteDataBuf = struct.pack(fmt, \
           self.zStrFmptIhuConL2FrameStdFrame['start'],\
           self.zStrFmptIhuConL2FrameStdFrame['len'],\
           self.zStrFmptIhuConL2FrameStdFrame['chksum'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['msgid'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['length'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommandMode'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommand'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorIdToErase'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorNumberToErase'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashAddressToAccess'],\
           self.zStrFmptIhuConL2FrameStdFrame['buf']['flashValidLengthToAccess'])
        for i in range(0, self.FuncCaculate_L2frameTotal_StdFrame()-self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len-4):
            byteTmp = struct.pack("B", self.zStrFmptIhuConL2FrameStdFrame['buf']['data'][i]&0xFF);
            byteDataBuf += byteTmp;
        #print("Read Reg L2Frame in pack mode: ", byteDataBuf);
        
        #Send data out
        if (self.FuncCanFrameSend(self.zStrFmptIhuConL2FrameStdFrame['len'], byteDataBuf) < 0):
            res['res'] = -2;
            print("CAN Send error, ", res);
            return res
        #Receive feedback from IHU
        if (self.FuncCanFrameReceive() < 0):
            res['res'] = -3;
            print("CAN Receive error, ", res);
            return res
        
        #return int(random.random()*10000);
        #Return back dedicated functions
        if (self.zStrFmptIhuConL3IapFlashRawCommandResp['flashValidLengthToAccess'] == 1):
            res['res'] = 1;
            res['value'] = self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][0];
        elif (self.zStrFmptIhuConL3IapFlashRawCommandResp['flashValidLengthToAccess'] == 2):
            res['res'] = 1;
            res['value'] = self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][0]<<8 + self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][1];
        elif (self.zStrFmptIhuConL3IapFlashRawCommandResp['flashValidLengthToAccess'] == 4):
            res['res'] = 1;
            res['value'] = self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][0]<<24 + self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][1]<<16 + self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][2]<<8 + self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][3];
        else:
            res['res'] = 1;
            res['value'] = {}
            for ii in range(0, dataLen):
                res['value'][ii] = self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][ii];
        
        #Return back
        return res;


    #Write Register
    #return res[]
    #Value could be in binary mode (input from TEXT or array mode (zStrBootCfgEng)
    #In most case, zStrBootCfgEng is in array mode [], after load from image file and after receive from IHU
    #Input - flashAddr: value in HEX or DEC
    #Input - value: string as default, depending on funIndex
    #Normally, value is in byte serials
    #Input - funIndex: int as function index
    def FuncWriteRegister(self, flashAddr, dataLen, value, funIndex):
        res = {}
        res['res'] = 0;

        #check parameters
        if (dataLen <= 0):
            res['res'] = -1;
            return res
        
        #L3 message content
        self.zStrFmptIhuConL3IapFlashRawCommandReq['msgid'] = self.HUITP_ENDIAN_EXG16(ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['length'] = self.HUITP_ENDIAN_EXG16(self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq());
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommandMode'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommand'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_WRITE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashAddressToAccess'] = self.HUITP_ENDIAN_EXG32(flashAddr);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashValidLengthToAccess'] = self.HUITP_ENDIAN_EXG32(dataLen);
        
        #Decode value as input, only accept HEX value
        #print("value = %s, dataLen = %d" % (value, dataLen))
        valueInput = {}
        #Equipment Lable
        if (funIndex == ModFmptCom.GL_FMPT_bootcfg_equlabel):
            if ((dataLen != len(value)) or (len(value) != ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1])):
                res['res'] = -2;
                return res
            for ii in range(0, ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1]):
                valueInput[ii] = ord(value[ii : ii+1])
            #print(valueInput)
        
        #All bootCfg area
        elif (funIndex == ModFmptCom.GL_FMPT_bootcfg_all):
            valueInput = self.FuncRestoreBootCfgIntoIhuData();

        #FLASH APP BODY
        elif (funIndex == ModFmptCom.GL_FMPT_bootcfg_appImage):
            for i in range (0, dataLen):
                valueInput[i] = int(value[i]) & 0xFF            
            #print(valueInput)

        #Other string possibilities
        else:
            hexLen = int((len(value) - 2)/2)
            if (dataLen != hexLen):
                res['res'] = -3;
                return res
            if ((value[0:2] != '0x') and (value[0:2] != '0X')):
                res['res'] = -4;
                return res
            for ii in range (0, dataLen):
                valueTmp = value[(2+ii*2):(4+ii*2)]
                valueInput[ii] = int(valueTmp, base = 16) & 0xFF
        #print("Write Reg content = ", valueInput)
        
        #Write into message body
        if (dataLen == 1):
            self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][0] = valueInput[0];
        elif (dataLen == 2):
            if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][0] = valueInput[1];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][1] = valueInput[0];
            else:
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][0] = valueInput[0];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][1] = valueInput[1];
        elif (dataLen == 4):
            if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][0] = valueInput[3];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][1] = valueInput[2];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][2] = valueInput[1];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][3] = valueInput[0];
            else:
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][0] = valueInput[0];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][1] = valueInput[1];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][2] = valueInput[2];
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][3] = valueInput[3];
        else:
            for ii in range(0, dataLen):
                self.zStrFmptIhuConL3IapFlashRawCommandReq['data'][ii] = valueInput[ii];
        #print("Write Reg Msg Body with dataLen = ", self.zStrFmptIhuConL3IapFlashRawCommandReq['data'], dataLen)
        
        #L2 Frame header
        self.zStrFmptIhuConL2FrameStdFrame['start'] = ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR;
        self.zStrFmptIhuConL2FrameStdFrame['len'] = ((self.FuncCaculate_StrTotal_L3IapFlashRawCommandReq() + 4) & 0xFFFF);
        self.zStrFmptIhuConL2FrameStdFrame['chksum'] = (self.zStrFmptIhuConL2FrameStdFrame['start']&0xFF) ^ (self.zStrFmptIhuConL2FrameStdFrame['len']&0xFF) ^ ((self.zStrFmptIhuConL2FrameStdFrame['len']>>8)& 0xFF);
        self.zStrFmptIhuConL2FrameStdFrame['buf'] = self.zStrFmptIhuConL3IapFlashRawCommandReq;
        #print("Write Reg L2Frame = ", self.zStrFmptIhuConL2FrameStdFrame)
        
        #Small endian to encode all the data part
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = "<BHBHHBBBBII";
        else:
            fmt = ">BHBHHBBBBII";
        byteDataBuf = struct.pack(fmt, \
            self.zStrFmptIhuConL2FrameStdFrame['start'],\
            self.zStrFmptIhuConL2FrameStdFrame['len'],\
            self.zStrFmptIhuConL2FrameStdFrame['chksum'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['msgid'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['length'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommandMode'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommand'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorIdToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorNumberToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashAddressToAccess'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashValidLengthToAccess'])
        for i in range(0, self.FuncCaculate_L2frameTotal_StdFrame()-self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len-4):
            byteTmp = struct.pack("B", self.zStrFmptIhuConL2FrameStdFrame['buf']['data'][i]&0xFF);
            #print(byteTmp)
            byteDataBuf += byteTmp;
        #print("Write Reg Output byte = ", byteDataBuf)
        
        #Send data out
        if (self.FuncCanFrameSend(self.zStrFmptIhuConL2FrameStdFrame['len'], byteDataBuf) < 0):
            res['res'] = -5;
            print("CAN Send error, ", res);
            return res

        #Receive feedback from IHU
        if (self.FuncCanFrameReceive() < 0):
            res['res'] = -6;
            return res
        
        #Formal return
        res['res'] = 1;
        return res

    
    #Unlock Flash
    #return res[]
    def FuncUnlockFlash(self):
        res = {}
        res['res'] = 0;

        #L3 message content
        self.zStrFmptIhuConL3IapFlashRawCommandReq['msgid'] = self.HUITP_ENDIAN_EXG16(ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['length'] = self.HUITP_ENDIAN_EXG16(self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq());
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommandMode'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommand'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_FLASH_UNLOCK;

        #L2 Frame header
        self.zStrFmptIhuConL2FrameStdFrame['start'] = ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR;
        self.zStrFmptIhuConL2FrameStdFrame['len'] = (self.FuncCaculate_L2frameTotal_StdFrame());
        self.zStrFmptIhuConL2FrameStdFrame['chksum'] = (self.zStrFmptIhuConL2FrameStdFrame['start']&0xFF) ^ (self.zStrFmptIhuConL2FrameStdFrame['len']&0xFF) ^ ((self.zStrFmptIhuConL2FrameStdFrame['len']>>8)& 0xFF);
        self.zStrFmptIhuConL2FrameStdFrame['buf'] = self.zStrFmptIhuConL3IapFlashRawCommandReq;
        #print(self.zStrFmptIhuConL2FrameStdFrame);
        
        #Small endian to encode all the data part
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = "<BHBHHBBBBII";
        else:
            fmt = ">BHBHHBBBBII";
        byteDataBuf = struct.pack(fmt, \
            self.zStrFmptIhuConL2FrameStdFrame['start'],\
            self.zStrFmptIhuConL2FrameStdFrame['len'],\
            self.zStrFmptIhuConL2FrameStdFrame['chksum'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['msgid'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['length'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommandMode'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommand'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorIdToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorNumberToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashAddressToAccess'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashValidLengthToAccess'])
        for i in range(0, self.FuncCaculate_L2frameTotal_StdFrame()-self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len-4):
            byteTmp = struct.pack("B", self.zStrFmptIhuConL2FrameStdFrame['buf']['data'][i]&0xFF);
            byteDataBuf += byteTmp;
        
        #Send data out
        if (self.FuncCanFrameSend(self.zStrFmptIhuConL2FrameStdFrame['len'], byteDataBuf) < 0):
            res['res'] = -1;
            return res

        #Receive feedback from IHU
        if (self.FuncCanFrameReceive() < 0):
            res['res'] = -2;
            return res
        
        #Fromal return
        res['res'] = 1;
        return res


    #Lock Flash
    #return res[]
    def FuncLockFlash(self):
        res = {}
        res['res'] = 0;
        
        #L3 message content
        self.zStrFmptIhuConL3IapFlashRawCommandReq['msgid'] = self.HUITP_ENDIAN_EXG16(ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['length'] = self.HUITP_ENDIAN_EXG16(self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq());
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommandMode'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommand'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_FLASH_LOCK;

        #L2 Frame header
        self.zStrFmptIhuConL2FrameStdFrame['start'] = ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR;
        self.zStrFmptIhuConL2FrameStdFrame['len'] = (self.FuncCaculate_L2frameTotal_StdFrame());
        self.zStrFmptIhuConL2FrameStdFrame['chksum'] = (self.zStrFmptIhuConL2FrameStdFrame['start']&0xFF) ^ (self.zStrFmptIhuConL2FrameStdFrame['len']&0xFF) ^ ((self.zStrFmptIhuConL2FrameStdFrame['len']>>8)& 0xFF);
        self.zStrFmptIhuConL2FrameStdFrame['buf'] = self.zStrFmptIhuConL3IapFlashRawCommandReq;
        #print(self.zStrFmptIhuConL2FrameStdFrame);
        
        #Small endian to encode all the data part
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = "<BHBHHBBBBII";
        else:
            fmt = ">BHBHHBBBBII";
        byteDataBuf = struct.pack(fmt, \
            self.zStrFmptIhuConL2FrameStdFrame['start'],\
            self.zStrFmptIhuConL2FrameStdFrame['len'],\
            self.zStrFmptIhuConL2FrameStdFrame['chksum'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['msgid'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['length'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommandMode'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommand'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorIdToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorNumberToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashAddressToAccess'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashValidLengthToAccess'])
        for i in range(0, self.FuncCaculate_L2frameTotal_StdFrame()-self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len-4):
            byteTmp = struct.pack("B", self.zStrFmptIhuConL2FrameStdFrame['buf']['data'][i]&0xFF);
            byteDataBuf += byteTmp;
        
        #Send data out
        if (self.FuncCanFrameSend(self.zStrFmptIhuConL2FrameStdFrame['len'], byteDataBuf) < 0):
            res['res'] = -1;
            return res
        #Receive feedback from IHU
        if (self.FuncCanFrameReceive() < 0):
            res['res'] = -2;
            return res
        #Fromal return
        res['res'] = 1;
        return res


    #Input parameter: Starting of sector and Number of Sectors
    #return res[]
    def FuncEraseFlash(self, startSec, numSec):
        res = {}
        res['res'] = 0;
    
        #L3 message content
        self.zStrFmptIhuConL3IapFlashRawCommandReq['msgid'] = self.HUITP_ENDIAN_EXG16(ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_req);
        self.zStrFmptIhuConL3IapFlashRawCommandReq['length'] = self.HUITP_ENDIAN_EXG16(self.FuncCaculate_BufOnly_L3IapFlashRawCommandReq());
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommandMode'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_MODE_ACTIVE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashRawCommand'] = ModFmptCom.GL_FMPT_IAP_FLASH_RAW_COMMAND_SECTOR_ERASE;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashSectorIdToErase'] = startSec;
        self.zStrFmptIhuConL3IapFlashRawCommandReq['flashSectorNumberToErase'] = numSec;

        #L2 Frame header
        self.zStrFmptIhuConL2FrameStdFrame['start'] = ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR;
        self.zStrFmptIhuConL2FrameStdFrame['len'] = (self.FuncCaculate_L2frameTotal_StdFrame());
        self.zStrFmptIhuConL2FrameStdFrame['chksum'] = (self.zStrFmptIhuConL2FrameStdFrame['start']&0xFF) ^ (self.zStrFmptIhuConL2FrameStdFrame['len']&0xFF) ^ ((self.zStrFmptIhuConL2FrameStdFrame['len']>>8)& 0xFF);
        self.zStrFmptIhuConL2FrameStdFrame['buf'] = self.zStrFmptIhuConL3IapFlashRawCommandReq;
        #print(self.zStrFmptIhuConL2FrameStdFrame);
        
        #Small endian to encode all the data part
        if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
            fmt = "<BHBHHBBBBII";
        else:
            fmt = ">BHBHHBBBBII";
        byteDataBuf = struct.pack(fmt, \
            self.zStrFmptIhuConL2FrameStdFrame['start'],\
            self.zStrFmptIhuConL2FrameStdFrame['len'],\
            self.zStrFmptIhuConL2FrameStdFrame['chksum'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['msgid'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['length'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommandMode'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashRawCommand'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorIdToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashSectorNumberToErase'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashAddressToAccess'],\
            self.zStrFmptIhuConL2FrameStdFrame['buf']['flashValidLengthToAccess'])
        for i in range(0, self.FuncCaculate_L2frameTotal_StdFrame()-self.zStrIhuConL3_L3IapFlashRawCommandReq_fix_len-4):
            byteTmp = struct.pack("B", self.zStrFmptIhuConL2FrameStdFrame['buf']['data'][i]&0xFF);
            byteDataBuf += byteTmp;
        
        #Send data out
        if (self.FuncCanFrameSend(self.zStrFmptIhuConL2FrameStdFrame['len'], byteDataBuf) < 0):
            res['res'] = -1;
            return res
        #Receive feedback from IHU
        if (self.FuncCanFrameReceive() < 0):
            res['res'] = -2;
            return res
        #Fromal return
        res['res'] = 1;
        return res

    
    #CAN Interface send out
    #Error only return -1, else 1
    def FuncCanFrameSend(self, dataLen, dataBuf):
        self.zStrFmptIhuConL2VciCanObj['RemoteFlag'] = ModFmptCom.GL_FMPT_DEVDRIVE_CAN_REMOTE_FLAG;
        self.zStrFmptIhuConL2VciCanObj['ExternFlag'] = ModFmptCom.GL_FMPT_DEVDRIVE_CAN_EXT_FLAG;
        self.zStrFmptIhuConL2VciCanObj['ID'] = ModFmptCom.GL_FMPT_DEVDRIVE_CAN_ID;
        
        #Judge whether this is the last segment
        for ii in range(0, dataLen, 8):
            if ((ii + 8) > dataLen):
                jj = (dataLen % 8);
            else:
                jj = 8;
            
        self.zStrFmptIhuConL2VciCanObj['DataLen'] = jj;

        byteFrame = struct.pack("B", dataBuf[ii]);
        for iii in range(1, jj):
            byteTmp = struct.pack("B", dataBuf[ii+iii]);
            byteFrame += byteTmp;
        self.zStrFmptIhuConL2VciCanObj['Data'] = byteFrame;
        
        #build canFrame
        canFrame = struct.pack("<iiBBBBB", \
            self.zStrFmptIhuConL2VciCanObj['ID'],\
            self.zStrFmptIhuConL2VciCanObj['TimeStamp'],\
            self.zStrFmptIhuConL2VciCanObj['TimeFlag'],\
            self.zStrFmptIhuConL2VciCanObj['SendType'],\
            self.zStrFmptIhuConL2VciCanObj['RemoteFlag'],\
            self.zStrFmptIhuConL2VciCanObj['ExternFlag'],\
            self.zStrFmptIhuConL2VciCanObj['DataLen']);
        canFrame += self.zStrFmptIhuConL2VciCanObj['Data'];
        canFrame += struct.pack("<BBB", 0x00, 0x00, 0x00);
        #print("canFrame = ", canFrame);
        
        #Send to DLL
        if (self.FuncVciTransmit(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND, canFrame, dataLen) < 0):
            return -1;
        #print("frameIndex = %d, string = %s"%(int(ii/8), str(self.zStrFmptIhuConL2VciCanObj)))

        #Finally return back
        print("test")
        return 1;

    #CAN Interface receive and form the whole L3 package
    #Error only return -1, else 1
    def FuncCanFrameReceive(self):
        #Rcv all frames from IHU
        rcvFrameCnt = 0;
        rcvState = 'START';
        rcvFrameLenTotal = 0;
        rcvFrameLenCnt = 0;
        while(rcvFrameCnt < ModFmptCom.GL_FMPT_IHUCON_FRAME_RCV_MAX_LEN):
            rcvFrameCnt += 1;
            #Actively fetch one frame from IHU
            #Time out means over!
            res = self.FuncVciReceive(ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVTYPE, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_DEVIND, ModFmptCom.GL_FMPT_DEVDRIVE_CAN_CANIND);
            if (res['res'] < 0):
                return -1;
            #unpack to variables, with normal endian
            if (ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SET == ModFmptCom.GL_FMPT_HUITP_CURRENT_PROCESSOR_ENDIAN_SMALL):
                fmt = "<IIBBBBBBBBBBBBBBBB";
            else:
                fmt = ">IIBBBBBBBBBBBBBBBB";
            (self.zStrFmptIhuConL2VciCanObj["ID"],\
            self.zStrFmptIhuConL2VciCanObj["TimeStamp"],\
            self.zStrFmptIhuConL2VciCanObj["TimeFlag"],\
            self.zStrFmptIhuConL2VciCanObj["SendType"],\
            self.zStrFmptIhuConL2VciCanObj["RemoteFlag"],\
            self.zStrFmptIhuConL2VciCanObj["ExternFlag"],\
            self.zStrFmptIhuConL2VciCanObj["DataLen"],\
            d0, d1, d2, d3, d4, d5, d6, d7, r0, r1, r2) = struct.unpack(fmt, res['dataFrame']);
            self.zStrFmptIhuConL2VciCanObj["Data"] = {}
            self.zStrFmptIhuConL2VciCanObj["Data"][0] = d0;
            self.zStrFmptIhuConL2VciCanObj["Data"][1] = d1;
            self.zStrFmptIhuConL2VciCanObj["Data"][2] = d2;
            self.zStrFmptIhuConL2VciCanObj["Data"][3] = d3;
            self.zStrFmptIhuConL2VciCanObj["Data"][4] = d4;
            self.zStrFmptIhuConL2VciCanObj["Data"][5] = d5;
            self.zStrFmptIhuConL2VciCanObj["Data"][6] = d6;
            self.zStrFmptIhuConL2VciCanObj["Data"][7] = d7;
            self.zStrFmptIhuConL2VciCanObj["Reserved"] = {}
            self.zStrFmptIhuConL2VciCanObj["Reserved"][0] = r0;
            self.zStrFmptIhuConL2VciCanObj["Reserved"][1] = r1;
            self.zStrFmptIhuConL2VciCanObj["Reserved"][2] = r2;
            #print(self.zStrFmptIhuConL2VciCanObj)
            if (rcvState == 'START'):
                rcvState = 'BODY1'
                #Frame head flag
                if (self.zStrFmptIhuConL2VciCanObj["Data"][0]&0xFF != ModFmptCom.GL_FMPT_IHU_L2PACKET_START_CHAR):
                    return -10;
                #Frame length
                if (self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF != 8):
                    return -11;
                rcvFrameLenCnt += self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF;
                #Frame length: 16+4=20 as minimum length
                rcvFrameLenTotal = self.HUITP_ENDIAN_EXG16((self.zStrFmptIhuConL2VciCanObj["Data"][1]&0xFF)>>8 + (self.zStrFmptIhuConL2VciCanObj["Data"][0]&0xFF));
                if (rcvFrameLenTotal < 20):
                    return -12;
                rcvFrameCksum = self.zStrFmptIhuConL2VciCanObj["Data"][3]&0xFF;
                #Frame checksum confirm
                if (rcvFrameCksum != ((self.zStrFmptIhuConL2VciCanObj["Data"][0]&0xFF) ^ (self.zStrFmptIhuConL2VciCanObj["Data"][1]&0xFF) ^ (self.zStrFmptIhuConL2VciCanObj["Data"][2]&0xF))):
                    return -13;
                #L3 content
                self.zStrFmptIhuConL3IapFlashRawCommandResp['msgid'] = self.HUITP_ENDIAN_EXG16((self.zStrFmptIhuConL2VciCanObj["Data"][4]&0xFF)>>8 + (self.zStrFmptIhuConL2VciCanObj["Data"][5]&0xFF));
                if (self.zStrFmptIhuConL3IapFlashRawCommandResp['msgid'] != ModFmptCom.GL_FMPT_HUITP_MSGID_sui_flash_raw_cmd_rsp):
                    return -14;
                self.zStrFmptIhuConL3IapFlashRawCommandResp['length'] = self.HUITP_ENDIAN_EXG16((self.zStrFmptIhuConL2VciCanObj["Data"][6]&0xFF)>>8 + (self.zStrFmptIhuConL2VciCanObj["Data"][7]&0xFF));
                if (self.zStrFmptIhuConL3IapFlashRawCommandResp['length'] < 12):
                    return -15;
            elif (rcvState == 'BODY1'):
                rcvState = 'BODY2'
                #Frame length
                if (self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF != 8):
                    return -20;
                rcvFrameLenCnt += self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF;
                #L3 content
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashRawCommandModeResp'] = self.zStrFmptIhuConL2VciCanObj["Data"][0]&0xFF;
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashRawCommandResp'] = self.zStrFmptIhuConL2VciCanObj["Data"][1]&0xFF;
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashSectorIdToErase'] = self.zStrFmptIhuConL2VciCanObj["Data"][2]&0xFF;
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashSectorNumberToErase'] = self.zStrFmptIhuConL2VciCanObj["Data"][3]&0xFF;
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashAddressToAccess'] = self.HUITP_ENDIAN_EXG32((self.zStrFmptIhuConL2VciCanObj["Data"][4]&0xFF)>>24 + \
                    (self.zStrFmptIhuConL2VciCanObj["Data"][5]&0xFF)>>16 + (self.zStrFmptIhuConL2VciCanObj["Data"][6]&0xFF)>>8 + self.zStrFmptIhuConL2VciCanObj["Data"][7]&0xFF);
            elif (rcvState == 'BODY2'):
                rcvState = 'BODY3'
                #Frame length
                if (self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF < 4):
                    return -30;
                rcvFrameLenCnt += 4;
                #L3 content
                self.zStrFmptIhuConL3IapFlashRawCommandResp['flashValidLengthToAccess'] = self.HUITP_ENDIAN_EXG32((self.zStrFmptIhuConL2VciCanObj["Data"][0]&0xFF)>>24 + \
                    (self.zStrFmptIhuConL2VciCanObj["Data"][1]&0xFF)>>16 + (self.zStrFmptIhuConL2VciCanObj["Data"][2]&0xFF)>>8 + self.zStrFmptIhuConL2VciCanObj["Data"][3]&0xFF);
                for i in range(0, 4):
                    if (rcvFrameLenTotal > rcvFrameLenCnt):
                        self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][rcvFrameLenCnt - (self.zStrIhuConL3_L3IapFlashRawCommandResp_fix_len + 4)] = self.zStrFmptIhuConL2VciCanObj["Data"][4+i]&0xFF;
                        rcvFrameLenCnt += 1;
            elif (rcvState == 'BODY3'):
                #Frame length
                if (self.zStrFmptIhuConL2VciCanObj["DataLen"]&0xFF <= 0):
                    return -40;
                #L3 content
                for i in range(0, 8):
                    if (rcvFrameLenTotal > rcvFrameLenCnt):
                        self.zStrFmptIhuConL3IapFlashRawCommandResp['data'][rcvFrameLenCnt - (self.zStrIhuConL3_L3IapFlashRawCommandResp_fix_len + 4)] = self.zStrFmptIhuConL2VciCanObj["Data"][i]&0xFF;
                        rcvFrameLenCnt += 1;
                    #Get full message content
                    else:
                        #check message length
                        if ((rcvFrameLenCnt - 4 - 4) != self.zStrFmptIhuConL3IapFlashRawCommandResp['length']):
                            return -13;
                        #Decode further
                        #Let finall function deal with
                        break;
            else:
                return -50;
            
        #Return back
        return 1;
    
        
    #static extern UInt32 VCI_Transmit(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pSend, UInt32 Len);
    #Error only return -1 else 1
    def FuncVciTransmit(self, devType, devInd, canInd, dataFrame, dataLen):
        try:
            strDllPath = sys.path[0] + str(os.sep) + "ControlCAN.dll"
            #objDll = windll.LoadLibrary(strDllPath)
            #objDll = WinDLL(strDllPath)
            objDll = cdll.LoadLibrary(strDllPath)
            #objDll = CDLL(strDllPath)
            api  = objDll.VCI_Transmit;
            api.argtypes = [c_uint, c_uint, c_uint, c_void_p, c_uint];
            api.restypes = c_uint;
            callRes = api(devType, devInd, canInd, dataFrame, dataLen);
            if (callRes == 0):
                #print("CAN nothing send out!")
                res = -1;
            else:
                res = 1;
            
        except Exception as err:  
            print(err)
            res = -2;
            return res;

        finally:
            return res;
    
    #static extern UInt32 VCI_Receive(UInt32 DeviceType, UInt32 DeviceInd, UInt32 CANInd, ref VCI_CAN_OBJ pReceive, UInt32 Len, Int32 WaitTime);
    #Error only res, with (res, dataFrame)
    def FuncVciReceive(self, devType, devInd, canInd):
        try:
            strDllPath = sys.path[0] + str(os.sep) + "ControlCAN.dll"
            #objDll = windll.LoadLibrary(strDllPath)
            #objDll = WinDLL(strDllPath)
            objDll = cdll.LoadLibrary(strDllPath)
            #objDll = CDLL(strDllPath)
            api  = objDll.VCI_Receive;
            api.argtypes = [c_uint, c_uint, c_uint, c_void_p, c_uint, c_uint];
            api.restypes = c_uint;
            dataFrame = b'\xfe\x00\x01\xff\xa2\x90\x00\xf8\x01\x05\x00\x00\x08\xfe\x00\xfe\x00\x00\x00\x02\x00\x00\x00\x00'
            callRes = api(devType, devInd, canInd, dataFrame, ModFmptCom.GL_FMPT_IHUCON_DATA_RCV_MAX_LEN, ModFmptCom.GL_FMPT_IHUCON_WAIT_FB_MAX_IN_MS);
            res = {}
            if (callRes == 0):
                #print("CAN nothing received!")
                res['res'] = -1;
            elif (callRes >= ModFmptCom.GL_FMPT_IHUCON_DATA_RCV_MAX_LEN):
                #print("CAN too much data received!")
                res['res'] = -2;
            else:
                res['res'] = 1;
                res['dataFrame'] = dataFrame;
            #Judge time out, return -1

        except Exception as err:  
            print(err)
            res['res'] = -1;
            return res;
        
        finally:
            return res;

    def FuncLoadIhuReadIntoBootCfg(self, data):
        #Equ-label
        index = 0;
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1];
        ModFmptCom.zStrBootCfgEng['equLable'] = ''
        for i in range(index, length):
            ModFmptCom.zStrBootCfgEng['equLable'] += str(data[i])
        index += length;
        
        #hwType
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][1];
        ModFmptCom.zStrBootCfgEng['hwType'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += len;
        
        #hwPemId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][1];
        ModFmptCom.zStrBootCfgEng['hwPemId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;
        
        #swRelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][1];
        ModFmptCom.zStrBootCfgEng['swRelId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;
        
        #swVerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][1];
        ModFmptCom.zStrBootCfgEng['swVerId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;
        
        #swUpgradeFlag
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][1];
        ModFmptCom.zStrBootCfgEng['swUpgradeFlag'] = data[index]
        index += length;

        #swUpgPollId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][1];
        ModFmptCom.zStrBootCfgEng['swUpgPollId'] = data[index]
        index += length;

        #bootIndex
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][1];
        ModFmptCom.zStrBootCfgEng['bootIndex'] = data[index]
        index += length;

        #bootAreaMax
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][1];
        ModFmptCom.zStrBootCfgEng['bootAreaMax'] = data[index]
        index += length;
    
        #facLoadAddr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadAddr'][1];
        ModFmptCom.zStrBootCfgEng['facLoadAddr'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;    
    
        #facLoadSwRel
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][1];
        ModFmptCom.zStrBootCfgEng['facLoadSwRel'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #facLoadSwVer
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][1];
        ModFmptCom.zStrBootCfgEng['facLoadSwVer'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #facLoadCheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][1];
        ModFmptCom.zStrBootCfgEng['facLoadCheckSum'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #facLoadValid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadValid'][1];
        ModFmptCom.zStrBootCfgEng['facLoadValid'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #facLoadLen
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][1];
        ModFmptCom.zStrBootCfgEng['facLoadLen'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;
                                
        #bootLoad1Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Addr'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1Addr'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;

        #bootLoad1RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1RelId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #bootLoad1VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1VerId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #bootLoad1CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1CheckSum'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #bootLoad1Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Valid'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1Valid'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;

        #bootLoad1Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad1Len'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;
                                
        #bootLoad2Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Addr'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2Addr'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;            

        #bootLoad2RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2RelId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;
        
        #bootLoad2VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2VerId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;        

        #bootLoad2CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2CheckSum'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;           
        
        #bootLoad2Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Valid'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2Valid'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;           

        #bootLoad2Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad2Len'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;
                                
        #bootLoad3Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Addr'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3Addr'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;    

        #bootLoad3RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3RelId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3RelId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;   
        
        #bootLoad3VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3VerId'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3VerId'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;   
        
        #bootLoad3CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3CheckSum'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3CheckSum'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;   
        
        #bootLoad3Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Valid'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3Valid'] = self.HUITP_ENDIAN_EXG16(data[index]<<8 + data[index+1])
        index += length;   
        
        #bootLoad3Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Len'][1];
        ModFmptCom.zStrBootCfgEng['bootLoad3Len'] = self.HUITP_ENDIAN_EXG32(data[index]<<24 + data[index+1]<<16 + data[index+2]<<8 + data[index+3])
        index += length;                

        #cipherKey
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][1];
        ModFmptCom.zStrBootCfgEng['cipherKey'] = {}
        for i in range(index, length):
            ModFmptCom.zStrBootCfgEng['cipherKey'][i-index] = data[i]
        index += length;

        #rsv
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['rsv'][1];
        ModFmptCom.zStrBootCfgEng['rsv'] = {}
        for i in range(index, length):
            ModFmptCom.zStrBootCfgEng['rsv'][i-index] = data[i]
        index += length;
        
        #Show this result into UI
        return ModFmptCom.zStrBootCfgEng;
    
    #Before sending to IHU, all BootCfg info has to convert into HEX mode
    #Transfer ASCII into HEX, we could use function ord()
    def FuncRestoreBootCfgIntoIhuData(self):
        output = {}
        #Equ-label
        index = 0;
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1];
        for i in range(index, length):
            output[i] = ord(ModFmptCom.zStrBootCfgEng['equLable'][i:(i+1)])
        index += length;
        output[index] = 0 #''
        #Special Treatment
        index +=1;
        
        #hwType
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['hwType'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;
        
        #hwPemId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['hwPemId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;
        
        #swRelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['swRelId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;
        
        #swVerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['swVerId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;
        
        #swUpgradeFlag
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][1];
        tmp = ModFmptCom.zStrBootCfgEng['swUpgradeFlag']
        output[index] = (tmp)&0xFF; 
        index += length;

        #swUpgPollId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][1];
        tmp = ModFmptCom.zStrBootCfgEng['swUpgPollId']
        output[index] = (tmp)&0xFF; 
        index += length;

        #bootIndex
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][1];
        tmp = ModFmptCom.zStrBootCfgEng['bootIndex']
        output[index] = (tmp)&0xFF; 
        index += length;

        #bootAreaMax
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][1];
        tmp = ModFmptCom.zStrBootCfgEng['bootAreaMax']
        output[index] = (tmp)&0xFF; 
        index += length;
    
        #facLoadAddr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadAddr'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['facLoadAddr'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF; 
        index += length;    
    
        #facLoadSwRel
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['facLoadSwRel'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #facLoadSwVer
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['facLoadSwVer'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #facLoadCheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['facLoadCheckSum'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #facLoadValid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadValid'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['facLoadValid'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #facLoadLen
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['facLoadLen'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF; 
        index += length;
                                
        #bootLoad1Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Addr'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad1Addr'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF; 
        index += length;

        #bootLoad1RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad1RelId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #bootLoad1VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad1VerId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #bootLoad1CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad1CheckSum'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #bootLoad1Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Valid'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad1Valid'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;

        #bootLoad1Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad1Len'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF;         
        index += length;
                                
        #bootLoad2Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Addr'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad2Addr'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF;   
        index += length;            

        #bootLoad2RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad2RelId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;
        
        #bootLoad2VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad2VerId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;        

        #bootLoad2CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad2CheckSum'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;           
        
        #bootLoad2Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Valid'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad2Valid'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;           

        #bootLoad2Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad2Len'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF;   
        index += length;
                                
        #bootLoad3Addr
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Addr'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad3Addr'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF;   
        index += length;    

        #bootLoad3RelId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3RelId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad3RelId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;   
        
        #bootLoad3VerId
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3VerId'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad3VerId'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;   
        
        #bootLoad3CheckSum
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3CheckSum'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad3CheckSum'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;   
        
        #bootLoad3Valid
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Valid'][1];
        tmp = self.HUITP_ENDIAN_EXG16(ModFmptCom.zStrBootCfgEng['bootLoad3Valid'])
        output[index] = (tmp>>8)&0xFF; 
        output[index+1] = (tmp)&0xFF; 
        index += length;   
        
        #bootLoad3Len
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad3Len'][1];
        tmp = self.HUITP_ENDIAN_EXG32(ModFmptCom.zStrBootCfgEng['bootLoad3Len'])
        output[index] = (tmp>>24)&0xFF; 
        output[index+1] = (tmp>>16)&0xFF; 
        output[index+2] = (tmp>>8)&0xFF; 
        output[index+3] = (tmp)&0xFF;   
        index += length;                

        #cipherKey
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][1];
        for i in range(index, index+length):
            output[i] = ModFmptCom.zStrBootCfgEng['cipherKey'][i-index]
        index += length;

        #rsv
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['rsv'][1];
        for i in range(index, index+length):
            output[i] = ModFmptCom.zStrBootCfgEng['rsv'][i-index]
        index += length;
        
        return output;


    #Find sector Id for a given flash address
    def FuncFindSectorId(self, flashAddr):
        if ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC0) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC1)):
            return ModFmptCom.GL_FMPT_FLASH_SEC0;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC1) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC2)):
            return ModFmptCom.GL_FMPT_FLASH_SEC1;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC2) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC3)):
            return ModFmptCom.GL_FMPT_FLASH_SEC2;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC3) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC4)):
            return ModFmptCom.GL_FMPT_FLASH_SEC3;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC4) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC5)):
            return ModFmptCom.GL_FMPT_FLASH_SEC4;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC5) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC6)):
            return ModFmptCom.GL_FMPT_FLASH_SEC5;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC6) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC7)):
            return ModFmptCom.GL_FMPT_FLASH_SEC6;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC7) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC8)):
            return ModFmptCom.GL_FMPT_FLASH_SEC7;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC8) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC9)):
            return ModFmptCom.GL_FMPT_FLASH_SEC8;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC9) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC10)):
            return ModFmptCom.GL_FMPT_FLASH_SEC9;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC10) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC11)):
            return ModFmptCom.GL_FMPT_FLASH_SEC10;
        elif ((flashAddr >= ModFmptCom.GL_FMPT_FLASH_START_ADDRESS_SEC11) and (flashAddr < ModFmptCom.GL_FMPT_FLASH_MAX_ADDRESS)):
            return ModFmptCom.GL_FMPT_FLASH_SEC11;
        else:
            return 0xFF;
    
    #Find number of sector on one data block covered
    def FuncGetSectorNum(self, flashAddr, dataLen):
        startSector = self.FuncFindSectorId(flashAddr);
        endSector = self.FuncFindSectorId(flashAddr + dataLen -1);
        
        if ((startSector == 0xFF) or (endSector == 0xFF)):
            numSector = 0xFF;
        else:
            numSector = endSector - startSector + 1;
        return numSector;

    #Block Element
class ClassBlockElm(object):
    def __init__(self):
        pass

    #READ FLASH and UPDATE MEMORY
    def FuncElm_READ_BOOTCFG_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN, 1);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_READ_BOOTCFG_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['value'] = objConn.FuncLoadIhuReadIntoBootCfg(callRes['value'])
            res['string'] = 'Exec Res - FuncElm_READ_BOOTCFG_STATUS'
        return res;

    def FuncElm_ERASE_BOOTCFG_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC11, 1);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_BOOTCFG_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_BOOTCFG_STATUS'
        return res;

    #Write FLASH by MEMORY variable
    def FuncElm_WRITE_BOOTCFG_STATU(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN, ModFmptCom.zStrBootCfgEng, ModFmptCom.GL_FMPT_bootcfg_all)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_WRITE_BOOTCFG_STATU failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['value'] = callRes['value']
            res['string'] = 'Exec Res - FuncElm_WRITE_BOOTCFG_STATU'
        return res;

    def FuncElm_ERASE_FAC_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC5, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_FAC_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_FAC_STATUS'
        return res;
    

    def FuncElm_WRITE_BOOTCFG_STATUS(self, bootcfgFile):
        res = {}
        #Open File
        with open(bootcfgFile, 'rb') as f:
            rawData=f.read()
        fileLen = len(rawData)
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(rawData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_SW_CONTROL_TABLE + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_BOOTCFG_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_BOOTCFG_STATUS'
        return res;
        
    #print(f.readline().decode('utf-8'))
    def FuncElm_WRITE_FAC_STATUS(self, facFile):
        res = {}
        #Open File
        with open(facFile, 'rb') as f:
            rawData=f.read()
        fileLen = len(rawData)
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(rawData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_FACTORY_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_FAC_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_FAC_STATUS'
        return res;

    def FuncElm_ERASE_APP1_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC7, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_APP1_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_APP1_STATUS'
        return res;


    def FuncElm_WRITE_APP1_STATUS(self, app1File):
        res = {}
        #Open File
        with open(app1File, 'rb') as f:
            rawData=f.read()
        fileLen = len(rawData)
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(rawData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP1_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_APP1_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_APP1_STATUS'
        return res;


    def FuncElm_ERASE_APP2_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC9, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_APP2_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_APP2_STATUS'
        return res;


    def FuncElm_WRITE_APP2_STATUS(self, app2File):
        res = {}
        #Open File
        with open(app2File, 'rb') as f:
            rawData=f.read()
        fileLen = len(rawData)
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(rawData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP2_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_APP2_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_APP2_STATUS'
        return res;

    def FuncElm_READ_IMAGE2DISK_STATUS(self, imageName):
        res = {}
        totalData = ModFmptCom.GL_FMPT_MAX_FLASH_LEN_IN_BYTES;
        #totalData = 1000;
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(totalData / segLen)
        
        #Save empty file
        fileStream = b''
        with open(imageName, 'wb+') as f:
            f.write(fileStream)

        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            fileStream = b''
            if (segIndex == (segTotal-1)):
                dataLen = totalData - segIndex*segLen;
            else:
                dataLen = segLen;
            segBase = segIndex*segLen
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE + segBase, dataLen, ModFmptCom.GL_FMPT_bootcfg_appImage)
            #print("callRes = ", callRes)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_READ_IMAGE2DISK_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
            else:
                inputData = callRes['value']
                for i in range (0, dataLen):
                    fileStream += struct.pack('B', inputData[i])
                with open(imageName, 'ab') as f:
                    f.write(fileStream)

        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_READ_IMAGE2DISK_STATUS'
        return res;   
    

    def FuncElm_ERASE_FLASHBOOTCFG_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC11, 1);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_FLASHBOOTCFG_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_FLASHBOOTCFG_STATUS'
        return res;

    def FuncElm_ERASE_FLASHFAC_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC5, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_FLASHFAC_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_FLASHFAC_STATUS'
        return res;

    def FuncElm_ERASE_FLASHAPP1_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC7, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_FLASHAPP1_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_FLASHAPP1_STATUS'
        return res;

    def FuncElm_ERASE_FLASHAPP2_STATUS(self):
        res = {}
        objConn = ClassConnProc();
        callRes = objConn.FuncEraseFlash(ModFmptCom.GL_FMPT_FLASH_SEC9, 2);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncElm_ERASE_FLASHAPP2_STATUS failure in low layer.'
            res['res'] = callRes['res']
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncElm_ERASE_FLASHAPP2_STATUS'
        return res;


        
        #with open(imageName, 'rb') as f:
        #    rawData = f.read()
        #bootCfgFile = sys.path[0] + str(os.sep) + "bootCfgFile.img"
        #start = ModFmptCom.GL_FMPT_FLASH_ADDRESS_SW_CONTROL_TABLE - ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE;
        #length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN
        #saveData = rawData[start:start+length];
        #with open(bootCfgFile, 'wb+') as f:
        #    f.write(saveData)
    def FuncElm_WRITE_FLASHBOOTCFG_STATUS(self, imageName):
        res = {}
        with open(imageName, 'rb') as f:
            rawData = f.read()
        start = ModFmptCom.GL_FMPT_FLASH_ADDRESS_SW_CONTROL_TABLE - ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE;
        length = ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN
        loadData = rawData[start:start+length];
        fileLen = length
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(loadData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_SW_CONTROL_TABLE + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_FLASHBOOTCFG_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_FLASHBOOTCFG_STATUS'
        return res;

    def FuncElm_WRITE_FLASHFAC_STATUS(self, imageName):
        res = {}
        with open(imageName, 'rb') as f:
            rawData = f.read()
        start = ModFmptCom.GL_FMPT_FLASH_ADDRESS_FACTORY_LOAD - ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE;
        length = ModFmptCom.GL_FMPT_FLASH_SEC_FAC_SIZE_IN_BYTES
        loadData = rawData[start:start+length];
        fileLen = length
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(loadData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_FACTORY_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_FLASHFAC_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_FLASHFAC_STATUS'
        return res;


    def FuncElm_WRITE_FLASHAPP1_STATUS(self, imageName):
        res = {}
        with open(imageName, 'rb') as f:
            rawData = f.read()
        start = ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP1_LOAD - ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE;
        length = ModFmptCom.GL_FMPT_FLASH_SEC_APP1_SIZE_IN_BYTES
        loadData = rawData[start:start+length];
        fileLen = length
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(loadData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP1_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_FLASHAPP1_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_FLASHAPP1_STATUS'
        return res;


    def FuncElm_WRITE_FLASHAPP2_STATUS(self, imageName):
        res = {}
        with open(imageName, 'rb') as f:
            rawData = f.read()
        start = ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP2_LOAD - ModFmptCom.GL_FMPT_FLASH_ADDRESS_BASE;
        length = ModFmptCom.GL_FMPT_FLASH_SEC_APP2_SIZE_IN_BYTES
        loadData = rawData[start:start+length];
        fileLen = length
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(fileLen / segLen)
        #Prepare to send out
        objConn = ClassConnProc();
        for segIndex in range(0, segTotal):
            if (segIndex == (segTotal-1)):
                dataLen = fileLen - segIndex*segLen;
            else:
                dataLen = segLen;
            outputData = {}
            segBase = segIndex*segLen
            for i in range(0, dataLen):
                outputData[i] = ord(loadData[(segBase+i):(segBase+i+1)])
            #print(outputData)
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP2_LOAD + segBase, dataLen, outputData, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - FuncElm_WRITE_FLASHAPP2_STATUS failure in low layer.'
                res['res'] = callRes['res']
                return res;
        #Send successful
        res['res'] = 1
        res['string'] = 'Exec Res - FuncElm_WRITE_FLASHAPP2_STATUS'
        return res;
    

    def FuncElm_READ_BOOTCFG_ALL_FIELDS_STATUS(self):
        res = {}
        res['res'] = 1
        return res;

    def FuncElm_WRITE_BOOTCFG_SINGLE_FIELD_STATUS(self):
        res = {}
        res['res'] = 1
        return res;


class ClassBatchOpr(object):
    def __init__(self):
        pass
    
    #Not yet used, might replace HwReadAll
    #Read BootCfg All into by using another way to work
    #Read from FLASH and update MEMORY global variables
    def FuncBat_load_bootcfg(self):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_READ_BOOTCFG_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_bootcfg - s1/1 - FuncElm_READ_BOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_load_bootcfg'
            return res;
    
    #Not yet used: might replace HwWriteAll
    #Write/update FLASH form local global variables
    #Taking care: here is the imageFile, but called function need seperate file
    def FuncBat_update_bootcfg(self, bootCfgFile):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_ERASE_BOOTCFG_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_update_bootcfg - s1/2 - FuncElm_ERASE_BOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_BOOTCFG_STATUS(bootCfgFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_update_bootcfg - s2/2 - FuncElm_WRITE_BOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_update_bootcfg'
            return res;

    def FuncBat_fac_load(self, facFile):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_ERASE_FAC_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_fac_load - s1/2 - FuncElm_ERASE_FAC_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_FAC_STATUS(facFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_fac_load - s2/2 - FuncElm_WRITE_FAC_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_fac_load'
            return res;
    
    def FuncBat_app1_load(self, app1File):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_ERASE_APP1_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_app1_load - s1/2 - FuncElm_ERASE_APP1_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_APP1_STATUS(app1File);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_app1_load - s2/2 - FuncElm_WRITE_APP1_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_app1_load'
            return res;

    def FuncBat_app2_load(self, app2File):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_ERASE_APP2_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_app2_load - s1/2 - FuncElm_ERASE_APP2_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_APP2_STATUS(app2File);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_app2_load - s2/2 - FuncElm_WRITE_APP2_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_app2_load'
            return res;

    # imageFile has to split into different file content!
    #
    #  ERROR 1
    #
    def FuncBat_burn_fac_app1_app2_load(self, imageFile):
        res = {}
        callRes = self.FuncBat_fac_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_fac_app1_app2_load - s1/3 - FuncBat_fac_load failure.'
            res['res'] = callRes['res']
            return res;
        callRes = self.FuncBat_app1_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_fac_app1_app2_load - s2/3 - FuncBat_app1_load failure.'
            res['res'] = callRes['res']
            return res;
        callRes = self.FuncBat_app2_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_fac_app1_app2_load - s3/3 - FuncBat_app2_load failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_burn_fac_app1_app2_load'
            return res;

    # imageFile has to split into different file content!
    #
    #  ERROR 2
    #
    def FuncBat_burn_bootcfg_fac_app1_app2_load(self, imageFile):
        res = {}
        callRes = self.FuncBat_update_bootcfg(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_bootcfg_fac_app1_app2_load - s1/4 - FuncElm_UPDATE_BOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = self.FuncBat_fac_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_bootcfg_fac_app1_app2_load - s2/4 - FuncBat_fac_load failure.'
            res['res'] = callRes['res']
            return res;
        callRes = self.FuncBat_app1_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_bootcfg_fac_app1_app2_load - s3/4 - FuncBat_app1_load failure.'
            res['res'] = callRes['res']
            return res;
        callRes = self.FuncBat_app2_load(imageFile);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_burn_bootcfg_fac_app1_app2_load - s4/4 - FuncBat_app2_load failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_burn_bootcfg_fac_app1_app2_load'
            return res;

    #
    #  ERROR 3: Taking care of Equ-label, which shall be 20, iso 19!
    #
    def FuncBat_save_image_to_disk(self, imageName):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_READ_IMAGE2DISK_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_save_image_to_disk - s1/1 - READ_IMAGE2DISK_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_save_image_to_disk'
            return res;

    def FuncBat_load_image_to_flash(self, imageName):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_READ_IMAGE2DISK_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s1/8 - FuncElm_READ_IMAGE2DISK_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_ERASE_FLASHFAC_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s2/8 - FuncElm_ERASE_FLASHFAC_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_ERASE_FLASHAPP1_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s3/8 - FuncElm_ERASE_FLASHAPP1_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_ERASE_FLASHAPP2_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s4/8 - FuncElm_ERASE_FLASHAPP2_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        
        callRes = objElm.FuncElm_WRITE_FLASHBOOTCFG_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s5/8 - FuncElm_WRITE_FLASHBOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_FLASHFAC_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s6/8 - FuncElm_WRITE_FLASHFAC_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_FLASHAPP1_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s7/8 - FuncElm_WRITE_FLASHAPP1_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_FLASHAPP2_STATUS(imageName);
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_load_image_to_flash - s8/8 - FuncElm_WRITE_FLASHAPP2_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_load_image_to_flash'
            return res;

    def FuncBat_write_single_field_status(self):
        objElm = ClassBlockElm();
        res = {}
        callRes = objElm.FuncElm_READ_BOOTCFG_ALL_FIELDS_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_write_single_field_status - s1/3 - FuncElm_READ_BOOTCFG_ALL_FIELDS_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_ERASE_BOOTCFG_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_write_single_field_status - s2/3 - FuncElm_ERASE_BOOTCFG_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        callRes = objElm.FuncElm_WRITE_BOOTCFG_SINGLE_FIELD_STATUS();
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - FuncBat_write_single_field_status - s3/3 - FuncElm_WRITE_BOOTCFG_SINGLE_FIELD_STATUS failure.'
            res['res'] = callRes['res']
            return res;
        else:
            res['res'] = 1
            res['string'] = 'Exec Res - FuncBat_write_single_field_status'
            return res;

#模块处理入口
class ClassHandler(object):

    def __init__(self):
        pass
  
    def func_conn(self, parFormat):
        res = {}
        if ((parFormat != 1) and (parFormat != 2) and (parFormat != 3)):
            res['string'] = 'Exec err - func_conn failure in parameter setting.'
            res['res'] = -1
            return res;
        #SPS
        if (parFormat == 1):
                res['string'] = 'Exec err - func_conn failure.'
                res['res'] = -2
                return res;
        #CAN
        elif (parFormat == 2):
            try:
                objDrv = ModFmptIhuDrv.ClassDrvCan();
                callRes = objDrv.FuncDrvCanInitStart();
                if (callRes < 0):
                    res['string'] = 'Exec err - func_conn failure.'
                    res['res'] = -3
                else:
                    res['res'] = 1
                    res['string'] = 'Exec Res - func_conn'
            except Exception as err:  
                print("Exec Err: func_conn!" + str(err))
                return ("Exec Err: func_conn!" + str(err))
            finally:
                return res;
        #ETH
        elif (parFormat == 3):
                res['string'] = 'Exec err - func_conn failure.'
                res['res'] = -4            
                return res;
        else:
            res['string'] = 'Exec err - func_conn failure.'
            res['res'] = -5
            return res;




    #DISCONNECTION of DRIVER
    def func_disc(self, parFormat):
        res = {}
        if ((parFormat != 1) and (parFormat != 2) and (parFormat != 3)):
            res['string'] = 'Exec err - func_disc failure in parameter setting.'
            res['res'] = -1
            return res;
        #SPS
        if (parFormat == 1):
                res['string'] = 'Exec err - func_disc failure.'
                res['res'] = -2
                return res;
        #CAN
        elif (parFormat == 2):
            try:
                objDrv = ModFmptIhuDrv.ClassDrvCan();
                callRes = objDrv.FuncCanDisconnect();
                if (callRes < 0):
                    res['string'] = 'Exec err - func_disc failure.'
                    res['res'] = -3
                else:
                    res['res'] = 1
                    res['string'] = 'Exec Res - func_disc'
            except Exception as err:
                print("Exec Err: func_disc!" + str(err))
                return ("Exec Err: func_disc!" + str(err))
            finally:
                return res;
        #ETH
        elif (parFormat == 3):
                res['string'] = 'Exec err - func_disc failure.'
                res['res'] = -4          
                return res;
        else:
            res['string'] = 'Exec err - func_disc failure.'
            res['res'] = -5
            return res;







        
        
        
        
        