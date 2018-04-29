'''
Created on 2018/2/23

#批量烧录操作
MODDULE: FMPT2 Batch Burn Operation

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

class ClassHandler(object):

    def __init__(self):
        pass
  
    def func_burn_fac_app(self, imageFile):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_burn_fac_app1_app2_load(imageFile)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_burn_fac_app failure' + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_burn_fac_app' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_burn_fac_app!" + str(err))
            return ("Exec Err: func_burn_fac_app!" + str(err))
        finally:
            return res;
        
    def func_burn_fac_app_with_new_equLabel(self, imageFile, newEquLabel):
        res = {}
        #Update image burn
        objBat = ModFmptIhuCon.ClassBatchOpr();
        callRes = objBat.FuncBat_burn_fac_app1_app2_load(imageFile)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_burn_fac_app_with_new_equLabel failure' + callRes['string']
            res['res'] = callRes['res']
            return res;

        #Update equipment label
        try:
            res['res'] = 0;
            objCon = ModFmptIhuCon.ClassConnProc();
            callRes = objCon.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1], newEquLabel, ModFmptCom.GL_FMPT_bootcfg_equlabel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_burn_fac_app_with_new_equLabel failure'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_burn_fac_app_with_new_equLabel' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_burn_fac_app_with_new_equLabel!" + str(err))
            return ("Exec Err: func_burn_fac_app_with_new_equLabel!" + str(err))
        finally:
            return res;     
    
    #With BootCfg APIs    
    def func_burn_bc_fac_app(self, imageFile):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_burn_bootcfg_fac_app1_app2_load(imageFile)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_burn_bc_fac_app failure' + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_burn_bc_fac_app' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_burn_bc_fac_app!" + str(err))
            return ("Exec Err: func_burn_bc_fac_app!" + str(err))
        finally:
            return res;
        
    def func_burn_bc_fac_app_with_new_equLabel(self, imageFile, newEquLabel):
        res = {}
        #Update image burn
        objBat = ModFmptIhuCon.ClassBatchOpr();
        callRes = objBat.FuncBat_burn_bootcfg_fac_app1_app2_load(imageFile)
        if (callRes['res'] < 0):
            res['string'] = 'Exec err - func_burn_bc_fac_app_with_new_equLabel failure' + callRes['string']
            res['res'] = callRes['res']
            return res;

        #Update equipment label
        try:
            res['res'] = 0;
            objCon = ModFmptIhuCon.ClassConnProc();
            callRes = objCon.FuncWriteRegister(ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][0], ModFmptCom.GL_FMPT_BOOT_CFG_ENG_ADDR['equLable'][1], newEquLabel, ModFmptCom.GL_FMPT_bootcfg_equlabel)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_burn_bc_fac_app_with_new_equLabel failure'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_burn_bc_fac_app_with_new_equLabel' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_burn_bc_fac_app_with_new_equLabel!" + str(err))
            return ("Exec Err: func_burn_bc_fac_app_with_new_equLabel!" + str(err))
        finally:
            return res;     






        
        