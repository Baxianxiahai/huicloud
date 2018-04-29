'''
Created on 2018/2/23

#
MODDULE: FMPT2 KEY ELEMENT OPERATION

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

#Local include
from fmpt2Main import *
from PkgFmptHandler import ModFmptCom
from PkgFmptHandler import ModFmptIhuCon


#Entry Processing
class ClassHandler(object):
    
    def __init__(self):
        pass

    def func_equLable_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1], ModFmptCom.GL_FMPT_bootcfg_equlabel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_equLable_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_equLable_read'
        except Exception as err:  
            print("Exec Err: func_equLable_read!" + str(err))
            return ("Exec Err: func_equLable_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with length=19
    def func_equLable_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_equlabel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_equLable_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_equLable_write'
        except Exception as err:  
            print("Exec Err: func_equLable_write!" + str(err))
            return ("Exec Err: func_equLable_write!" + str(err))
        finally:
            return res;
  
    def func_hwType_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            res['res'] = 1
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][1], ModFmptCom.GL_FMPT_bootcfg_hw_type)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_hwType_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_hwType_read'
        except Exception as err:  
            print("Exec Err: func_hwType_read!" + str(err))
            return ("Exec Err: func_hwType_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_hwType_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwType'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_hw_type)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_hwType_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_hwType_write'
        except Exception as err:  
            print("Exec Err: func_hwType_write!" + str(err))
            return ("Exec Err: func_hwType_write!" + str(err))
        finally:
            return res;

    def func_hwPemId_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][1], ModFmptCom.GL_FMPT_bootcfg_hw_pem_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_hwPemId_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_hwPemId_read'
        except Exception as err:  
            print("Exec Err: func_hwPemId_read!" + str(err))
            return ("Exec Err: func_hwPemId_read!" + str(err))
        finally:
            return res;
        
    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_hwPemId_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['hwPemId'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_hw_pem_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_hwPemId_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_hwPemId_write'
        except Exception as err:  
            print("Exec Err: func_hwPemId_write!" + str(err))
            return ("Exec Err: func_hwPemId_write!" + str(err))
        finally:
            return res;
                
    def func_swRelId_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][1], ModFmptCom.GL_FMPT_bootcfg_sw_rel_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swRelId_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swRelId_read'
        except Exception as err:  
            print("Exec Err: func_swRelId_read!" + str(err))
            return ("Exec Err: func_swRelId_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_swRelId_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swRelId'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_sw_rel_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swRelId_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swRelId_write'
        except Exception as err:  
            print("Exec Err: func_swRelId_write!" + str(err))
            return ("Exec Err: func_swRelId_write!" + str(err))
        finally:
            return res;

    def func_swVerId_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][1], ModFmptCom.GL_FMPT_bootcfg_sw_ver_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swVerId_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swVerId_read'
        except Exception as err:  
            print("Exec Err: func_swVerId_read!" + str(err))
            return ("Exec Err: func_swVerId_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_swVerId_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swVerId'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_sw_ver_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swVerId_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swVerId_write'
        except Exception as err:  
            print("Exec Err: func_swVerId_write!" + str(err))
            return ("Exec Err: func_swVerId_write!" + str(err))
        finally:
            return res;

    def func_swUpgradeFlag_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][1], ModFmptCom.GL_FMPT_bootcfg_sw_upgrade_flag)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swUpgradeFlag_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swUpgradeFlag_read'
        except Exception as err:  
            print("Exec Err: func_swUpgradeFlag_read!" + str(err))
            return ("Exec Err: func_swUpgradeFlag_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_swUpgradeFlag_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgradeFlag'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_sw_upgrade_flag)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swUpgradeFlag_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swUpgradeFlag_write'
        except Exception as err:  
            print("Exec Err: func_swUpgradeFlag_write!" + str(err))
            return ("Exec Err: func_swUpgradeFlag_write!" + str(err))
        finally:
            return res;
        
    def func_swUpgPollId_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][1], ModFmptCom.GL_FMPT_bootcfg_sw_upgrapoll_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swUpgPollId_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swUpgPollId_read'
        except Exception as err:  
            print("Exec Err: func_swUpgPollId_read!" + str(err))
            return ("Exec Err: func_swUpgPollId_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_swUpgPollId_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['swUpgPollId'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_sw_upgrapoll_id)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_swUpgPollId_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_swUpgPollId_write'
        except Exception as err:  
            print("Exec Err: func_swUpgPollId_write!" + str(err))
            return ("Exec Err: func_swUpgPollId_write!" + str(err))
        finally:
            return res;

    def func_bootIndex_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][1], ModFmptCom.GL_FMPT_bootcfg_boot_index)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_bootIndex_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_bootIndex_read'
        except Exception as err:  
            print("Exec Err: func_bootIndex_read!" + str(err))
            return ("Exec Err: func_bootIndex_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_bootIndex_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootIndex'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_boot_index)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_bootIndex_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_bootIndex_write'
        except Exception as err:  
            print("Exec Err: func_bootIndex_write!" + str(err))
            return ("Exec Err: func_bootIndex_write!" + str(err))
        finally:
            return res;

    def func_bootAreaMax_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][1], ModFmptCom.GL_FMPT_bootcfg_boot_area_max)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_bootAreaMax_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_bootAreaMax_read'
        except Exception as err:  
            print("Exec Err: func_bootAreaMax_read!" + str(err))
            return ("Exec Err: func_bootAreaMax_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_bootAreaMax_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['bootAreaMax'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_boot_area_max)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_bootAreaMax_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_bootAreaMax_write'
        except Exception as err:  
            print("Exec Err: func_bootAreaMax_write!" + str(err))
            return ("Exec Err: func_bootAreaMax_write!" + str(err))
        finally:
            return res;

    def func_cypherKey_read(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][1], ModFmptCom.GL_FMPT_bootcfg_cipher_key)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_cypherKey_read failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_cypherKey_read'
        except Exception as err:  
            print("Exec Err: func_cypherKey_read!" + str(err))
            return ("Exec Err: func_cypherKey_read!" + str(err))
        finally:
            return res;

    #dataValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_cypherKey_write(self, dataValue):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['cipherKey'][1], dataValue, ModFmptCom.GL_FMPT_bootcfg_cipher_key)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_cypherKey_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_cypherKey_write'
        except Exception as err:  
            print("Exec Err: func_cypherKey_write!" + str(err))
            return ("Exec Err: func_cypherKey_write!" + str(err))
        finally:
            return res;

    def func_cfgFile_ReadAllFromHw(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncReadRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN, 1);
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_cfgFile_ReadAllFromHw failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = objConn.FuncLoadIhuReadIntoBootCfg(callRes['value'])
                res['string'] = 'Exec Res - func_cfgFile_ReadAllFromHw'
        except Exception as err:  
            print("Exec Err: func_cfgFile_ReadAllFromHw!" + str(err))
            return ("Exec Err: func_cfgFile_ReadAllFromHw!" + str(err))
        finally:
            return res;
        
    def func_cfgFile_WriteAllToHw(self):
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            res = {}
            callRes = objConn.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_TOTAL_LEN, ModFmptCom.zStrBootCfgEng, ModFmptCom.GL_FMPT_bootcfg_all)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_cfgFile_WriteAllToHw failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_cfgFile_WriteAllToHw'
        except Exception as err:  
            print("Exec Err: func_cfgFile_WriteAllToHw!" + str(err))
            return ("Exec Err: func_cfgFile_WriteAllToHw!" + str(err))
        finally:
            return res;

    #parAddr must be HEX value
    def func_byteopr_read(self, parAddr, parFormat):
        res = {}
        if ((parFormat != 1) and (parFormat != 2) and (parFormat != 4)):
            res['string'] = 'Exec err - func_byteopr_read failure in parameter setting.'
            res['res'] = -1
            return res;
        if ((parAddr[0:2] != '0x') and (parAddr[0:2] != '0X')):
            res['string'] = 'Exec err - func_byteopr_read failure in parameter setting.'
            res['res'] = -2
            return res;
        parAddr = int(parAddr, base = 16);
        
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            callRes = objConn.FuncReadRegister(parAddr, parFormat, ModFmptCom.GL_FMPT_bootcfg_byte_opr);
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_byteopr_read failure in low layer.'
                res['res'] = -3
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_byteopr_read'

        except Exception as err:  
            print("Exec Err: func_byteopr_read!" + str(err))
            return ("Exec Err: func_byteopr_read!" + str(err))
        finally:
            return res;

    #parAddr must be HEX value
    #parValue must be string with 0x prefix, as input for FuncWriteRegister to further decode
    def func_byteopr_write(self, parAddr, parFormat, parValue):
        res = {}
        if ((parFormat != 1) and (parFormat != 2) and (parFormat != 4)):
            res['string'] = 'Exec err - func_byteopr_read failure in parameter setting.'
            res['res'] = -1
            return res;
        if ((parAddr[0:2] != '0x') and (parAddr[0:2] != '0X')):
            res['string'] = 'Exec err - func_byteopr_read failure in parameter setting.'
            res['res'] = -2
            return res;
        if ((parValue[0:2] != '0x') and (parValue[0:2] != '0X')):
            res['string'] = 'Exec err - func_byteopr_read failure in parameter setting.'
            res['res'] = -3
            return res;
        parAddr = int(parAddr, base = 16);
        #parValue = int(parValue, base = 16);
                
        try:
            objConn = ModFmptIhuCon.ClassConnProc();
            callRes = objConn.FuncWriteRegister(parAddr, parFormat, parValue, ModFmptCom.GL_FMPT_bootcfg_byte_opr)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_byteopr_write failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_byteopr_write'

        except Exception as err:  
            print("Exec Err: func_byteopr_write!" + str(err))
            return ("Exec Err: func_byteopr_write!" + str(err))
        finally:
            return res;











