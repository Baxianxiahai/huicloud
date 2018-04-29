'''
Created on 2018/2/23

#完整镜像操作管理
MODDULE: FMPT2 Full Image Operation

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

    def func_file_image_save_to_disk(self, imageName):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_save_image_to_disk(imageName)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_file_image_save_to_disk failure' + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_file_image_save_to_disk' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_file_image_save_to_disk!" + str(err))
            return ("Exec Err: func_file_image_save_to_disk!" + str(err))
        finally:
            return res;

    def func_file_image_load_into_flash(self, imageName):
        try:
            objBat = ModFmptIhuCon.ClassBatchOpr();
            res = {}
            callRes = objBat.FuncBat_load_image_to_flash(imageName)
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_file_image_load_into_flash failure' + callRes['string']
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['string'] = 'Exec Res - func_file_image_load_into_flash' + callRes['string']
        except Exception as err:  
            print("Exec Err: func_file_image_load_into_flash!" + str(err))
            return ("Exec Err: func_file_image_load_into_flash!" + str(err))
        finally:
            return res;







        
                