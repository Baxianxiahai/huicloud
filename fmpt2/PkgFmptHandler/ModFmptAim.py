'''
Created on 2018/2/23

#应用程序下载烧录
MODDULE: FMPT2 App Image Management

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
import math

#Local include
from fmpt2Main import *
from PkgFmptHandler import ModFmptCom
from PkgFmptHandler import ModFmptIhuCon

class ClassHandler(object):

    def __init__(self):
        pass
  
    def func_fac_addr_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadAddr'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadAddr'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadAddr)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_addr_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_addr_read'
        except Exception as err:  
            print("Exec Err: func_fac_addr_read!" + str(err))
            return ("Exec Err: func_fac_addr_read!" + str(err))
        finally:
            return res;

    def func_fac_chk_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadCheckSum)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_chk_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_chk_read'
        except Exception as err:  
            print("Exec Err: func_fac_chk_read!" + str(err))
            return ("Exec Err: func_fac_chk_read!" + str(err))
        finally:
            return res;
        
    def func_fac_chk_chk(self):
        objConn = ModFmptIhuCon.ClassConnProc();
        res = {}
        res['res'] = 1
        oldChecksum = 0;
        newChecksum = 0;
        swLen = 0;
        
        #Firstly read old checksum
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadCheckSum)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_fac_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            oldChecksum = callRes['value']
        
        #Secondly read SW len
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadLen)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_fac_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            swLen = callRes['value']
        
        #Thirdly read sw-body and caculate current checksum
        newCheckSum = 0;
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(swLen / segLen);
        for segIndex in range(0, segTotal):
            outputData = {}
            if (segIndex == (segTotal-1)):
                dataLen = swLen - segIndex*segLen;
            else:
                dataLen = segLen;
            segBase = segIndex*segLen
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_FACTORY_LOAD + segBase, dataLen, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_chk_chk failure in low layer.'
                res['res'] = callRes['res']
                return res;
            else:
                outputData = callRes['value']
                for i in range (0, dataLen):
                    newChecksum = (newChecksum + int(outputData[i], base=16)) & 0xFFFF;
        
        #Forthly write back
        try:
            if (newCheckSum != oldChecksum):
                callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadCheckSum'][1], newCheckSum, ModFmptCom.GL_FMPT_bootcfg_facLoadCheckSum)
                if (callRes['res'] < 0):
                    res['string'] = 'Exec err - func_fac_chk_chk failure in low layer.'
                    res['res'] = callRes['res']
                else:
                    res['res'] = 1
                    res['value'] = callRes['value']
                    res['string'] = 'Exec Res - func_fac_chk_chk, new checksum rewrite!'
            else:
                res['res'] = 1
                res['value'] = newCheckSum
                res['string'] = 'Exec Res - func_fac_chk_chk, same checksum!'
        except Exception as err:  
            print("Exec Err: func_fac_chk_chk!" + str(err))
            return ("Exec Err: func_fac_chk_chk!" + str(err))
        finally:
            return res;

    def func_fac_swRel_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadSwRel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_swRel_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_swRel_read'
        except Exception as err:  
            print("Exec Err: func_fac_swRel_read!" + str(err))
            return ("Exec Err: func_fac_swRel_read!" + str(err))
        finally:
            return res;
        
    def func_fac_swRel_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwRel'][1], par, ModFmptCom.GL_FMPT_bootcfg_facLoadSwRel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_swRel_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_swRel_set'
        except Exception as err:  
            print("Exec Err: func_fac_swRel_set!" + str(err))
            return ("Exec Err: func_fac_swRel_set!" + str(err))
        finally:
            return res;

    def func_fac_valid_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadValid'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadValid'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadValid)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_valid_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_valid_read'
        except Exception as err:  
            print("Exec Err: func_fac_valid_read!" + str(err))
            return ("Exec Err: func_fac_valid_read!" + str(err))
        finally:
            return res;
        
    def func_fac_swVer_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadSwVer)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_swVer_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_swVer_read'
        except Exception as err:  
            print("Exec Err: func_fac_swVer_read!" + str(err))
            return ("Exec Err: func_fac_swVer_read!" + str(err))
        finally:
            return res;

    def func_fac_swVer_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadSwVer'][1], par, ModFmptCom.GL_FMPT_bootcfg_facLoadSwVer)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_swVer_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_swVer_set'
        except Exception as err:  
            print("Exec Err: func_fac_swVer_set!" + str(err))
            return ("Exec Err: func_fac_swVer_set!" + str(err))
        finally:
            return res;

    def func_fac_len_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['facLoadLen'][1], ModFmptCom.GL_FMPT_bootcfg_facLoadLen)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_len_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_fac_len_read'
        except Exception as err:  
            print("Exec Err: func_fac_len_read!" + str(err))
            return ("Exec Err: func_fac_len_read!" + str(err))
        finally:
            return res;

    def func_fac_file_update(self, facFile):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_fac_load(facFile)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_fac_file_update failure' + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_fac_file_update' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_fac_file_update!" + str(err))
            return ("Exec Err: func_fac_file_update!" + str(err))
        finally:
            return res;

    def func_app1_addr_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Addr'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Addr'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1Addr)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_addr_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_addr_read'
        except Exception as err:  
            print("Exec Err: func_app1_addr_read!" + str(err))
            return ("Exec Err: func_app1_addr_read!" + str(err))
        finally:
            return res;
        
    def func_app1_swRel_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1RelId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_swRel_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_swRel_read'
        except Exception as err:  
            print("Exec Err: func_app1_swRel_read!" + str(err))
            return ("Exec Err: func_app1_swRel_read!" + str(err))
        finally:
            return res;
        
    def func_app1_swRel_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1RelId'][1], par, ModFmptCom.GL_FMPT_bootcfg_bootLoad1RelId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_swRel_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_swRel_set'
        except Exception as err:  
            print("Exec Err: func_app1_swRel_set!" + str(err))
            return ("Exec Err: func_app1_swRel_set!" + str(err))
        finally:
            return res;

    def func_app1_swVer_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1VerId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_swVer_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_swVer_read'
        except Exception as err:  
            print("Exec Err: func_app1_swVer_read!" + str(err))
            return ("Exec Err: func_app1_swVer_read!" + str(err))
        finally:
            return res;

    def func_app1_swVer_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1VerId'][1], par, ModFmptCom.GL_FMPT_bootcfg_bootLoad1VerId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_swVer_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_swVer_set'
        except Exception as err:  
            print("Exec Err: func_app1_swVer_set!" + str(err))
            return ("Exec Err: func_app1_swVer_set!" + str(err))
        finally:
            return res;

    def func_app1_valid_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Valid'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Valid'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1Valid)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_valid_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_valid_read'
        except Exception as err:  
            print("Exec Err: func_app1_valid_read!" + str(err))
            return ("Exec Err: func_app1_valid_read!" + str(err))
        finally:
            return res;

    def func_app1_chk_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1CheckSum)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_chk_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_chk_read'
        except Exception as err:  
            print("Exec Err: func_app1_chk_read!" + str(err))
            return ("Exec Err: func_app1_chk_read!" + str(err))
        finally:
            return res;
        
        
    def func_app1_chk_chk(self):
        objConn = ModFmptIhuCon.ClassConnProc();
        res = {}
        res['res'] = 1
        oldChecksum = 0;
        newChecksum = 0;
        swLen = 0;
        
        #Firstly read old checksum
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1CheckSum)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_app1_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            oldChecksum = callRes['value']
        
        #Secondly read SW len
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1Len)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_app1_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            swLen = callRes['value']
        
        #Thirdly read sw-body and caculate current checksum
        newCheckSum = 0;
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(swLen / segLen);
        for segIndex in range(0, segTotal):
            outputData = {}
            if (segIndex == (segTotal-1)):
                dataLen = swLen - segIndex*segLen;
            else:
                dataLen = segLen;
            segBase = segIndex*segLen
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP1_LOAD + segBase, dataLen, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_chk_chk failure in low layer.'
                res['res'] = callRes['res']
                return res;
            else:
                outputData = callRes['value']
                for i in range (0, dataLen):
                    newChecksum = (newChecksum + int(outputData[i], base=16)) & 0xFFFF;
        
        #Forthly write back
        try:
            if (newCheckSum != oldChecksum):
                callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1CheckSum'][1], newCheckSum, ModFmptCom.GL_FMPT_bootcfg_bootLoad1CheckSum)
                if (callRes['res'] < 0):
                    res['string'] = 'Exec err - func_app1_chk_chk failure in low layer.'
                    res['res'] = callRes['res']
                else:
                    res['res'] = 1
                    res['value'] = callRes['value']
                    res['string'] = 'Exec Res - func_app1_chk_chk, new checksum rewrite!'
            else:
                res['res'] = 1
                res['value'] = newCheckSum
                res['string'] = 'Exec Res - func_app1_chk_chk, same checksum!'
        except Exception as err:  
            print("Exec Err: func_app1_chk_chk!" + str(err))
            return ("Exec Err: func_app1_chk_chk!" + str(err))
        finally:
            return res;

    def func_app1_len_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad1Len'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad1Len)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_len_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app1_len_read'
        except Exception as err:  
            print("Exec Err: func_app1_len_read!" + str(err))
            return ("Exec Err: func_app1_len_read!" + str(err))
        finally:
            return res;

    def func_app1_file_update(self, app1File):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_app1_load(app1File)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app1_file_update failure'  + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_app1_file_update' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_app1_file_update!" + str(err))
            return ("Exec Err: func_app1_file_update!" + str(err))
        finally:
            return res;

    def func_app2_addr_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Addr'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Addr'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2Addr)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_addr_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_addr_read'
        except Exception as err:  
            print("Exec Err: func_app2_addr_read!" + str(err))
            return ("Exec Err: func_app2_addr_read!" + str(err))
        finally:
            return res;

    def func_app2_chk_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2CheckSum)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_chk_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_chk_read'
        except Exception as err:  
            print("Exec Err: func_app2_chk_read!" + str(err))
            return ("Exec Err: func_app2_chk_read!" + str(err))
        finally:
            return res;

    #Checksum function
    def func_app2_chk_chk(self):
        objConn = ModFmptIhuCon.ClassConnProc();
        res = {}
        res['res'] = 1
        oldChecksum = 0;
        newChecksum = 0;
        swLen = 0;
        
        #Firstly read old checksum
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2CheckSum)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_app2_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            oldChecksum = callRes['value']
        
        #Secondly read SW len
        callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2Len)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_app2_chk_chk failure in low layer.'
            res['res'] = callRes['res']
            return res;
        else:
            swLen = callRes['value']
        
        #Thirdly read sw-body and caculate current checksum
        newCheckSum = 0;
        segLen = ModFmptCom.GL_FMPT_MAX_LEN_FLASH_RAW_COMMAND_DATA;
        segTotal = math.ceil(swLen / segLen);
        for segIndex in range(0, segTotal):
            outputData = {}
            if (segIndex == (segTotal-1)):
                dataLen = swLen - segIndex*segLen;
            else:
                dataLen = segLen;
            segBase = segIndex*segLen
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_FLASH_ADDRESS_APP1_LOAD + segBase, dataLen, ModFmptCom.GL_FMPT_bootcfg_appImage)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_chk_chk failure in low layer.'
                res['res'] = callRes['res']
                return res;
            else:
                outputData = callRes['value']
                for i in range (0, dataLen):
                    newChecksum = (newChecksum + int(outputData[i], base=16)) & 0xFFFF;
        
        #Forthly write back
        try:
            if (newCheckSum != oldChecksum):
                callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2CheckSum'][1], newCheckSum, ModFmptCom.GL_FMPT_bootcfg_bootLoad2CheckSum)
                if (callRes['res'] < 0):
                    res['string'] = 'Exec err - func_app2_chk_chk failure in low layer.'
                    res['res'] = callRes['res']
                else:
                    res['res'] = 1
                    res['value'] = callRes['value']
                    res['string'] = 'Exec Res - func_app2_chk_chk, new checksum rewrite!'
            else:
                res['res'] = 1
                res['value'] = newCheckSum
                res['string'] = 'Exec Res - func_app2_chk_chk, same checksum!'
        except Exception as err:  
            print("Exec Err: func_app2_chk_chk!" + str(err))
            return ("Exec Err: func_app2_chk_chk!" + str(err))
        finally:
            return res;
    
    def func_app2_swRel_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2RelId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_swRel_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_swRel_read'
        except Exception as err:  
            print("Exec Err: func_app2_swRel_read!" + str(err))
            return ("Exec Err: func_app2_swRel_read!" + str(err))
        finally:
            return res;

    def func_app2_swRel_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2RelId'][1], par, ModFmptCom.GL_FMPT_bootcfg_bootLoad2RelId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_swRel_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_swRel_set'
        except Exception as err:  
            print("Exec Err: func_app2_swRel_set!" + str(err))
            return ("Exec Err: func_app2_swRel_set!" + str(err))
        finally:
            return res;

    def func_app2_valid_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Valid'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Valid'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2Valid)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_valid_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_valid_read'
        except Exception as err:  
            print("Exec Err: func_app2_valid_read!" + str(err))
            return ("Exec Err: func_app2_valid_read!" + str(err))
        finally:
            return res;

    def func_app2_swVer_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2VerId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_swVer_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_swVer_read'
        except Exception as err:  
            print("Exec Err: func_app2_swVer_read!" + str(err))
            return ("Exec Err: func_app2_swVer_read!" + str(err))
        finally:
            return res;

    def func_app2_swVer_set(self, par):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2VerId'][1], par, ModFmptCom.GL_FMPT_bootcfg_bootLoad2VerId)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_swVer_set failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_swVer_set'
        except Exception as err:  
            print("Exec Err: func_app2_swVer_set!" + str(err))
            return ("Exec Err: func_app2_swVer_set!" + str(err))
        finally:
            return res;

    def func_app2_len_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootLoad2Len'][1], ModFmptCom.GL_FMPT_bootcfg_bootLoad2Len)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_len_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_app2_len_read'
        except Exception as err:  
            print("Exec Err: func_app2_len_read!" + str(err))
            return ("Exec Err: func_app2_len_read!" + str(err))
        finally:
            return res;
        
    def func_app2_file_update(self, app2File):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_app2_load(app2File)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_app2_file_update failure'  + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_app2_file_update' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_app2_file_update!" + str(err))
            return ("Exec Err: func_app2_file_update!" + str(err))
        finally:
            return res;

        







                