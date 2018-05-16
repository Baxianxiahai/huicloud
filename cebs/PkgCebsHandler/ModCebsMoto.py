'''
Created on 2018年5月8日

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

#Local include
from cebsMain import *
from PkgCebsHandler import ModCebsCom
from PkgCebsHandler import ModCebsCfg


class classMotoProcess(object):
    def __init__(self):
        pass
         
    def funcMotoCalaRun(self):
        print("MOTO: Running Calibration!")

    def funcMotoCalaMoveOneStep(self, scale, dir):
        if (scale == 1):
            actualScale = 500;
        elif (scale == 2):
            actualScale = 1000;
        elif (scale == 3):
            actualScale = 5000;
        elif (scale == 4):
            actualScale = 10000;
        elif (scale == 5):
            actualScale = 50000;
        else:
            actualScale = 0;

        if (dir == 1):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] += actualScale;
            if ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_32_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_Y_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX;
            elif (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] > ModCebsCom.GL_CEBS_HB_TARGET_BOARD_Y_MAX):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_Y_MAX;
            else:
                pass
        elif (dir == 2):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] -= actualScale;
            if (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] < 0):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1] = 0;
        elif (dir == 3):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] -= actualScale;
            if (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] < 0):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = 0;
        elif (dir == 4):
            ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] += actualScale;
            if ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_32_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_32_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_32_SD_X_MAX;
            elif ((ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD) and (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX)):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX;
            elif (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] > ModCebsCom.GL_CEBS_HB_TARGET_BOARD_X_MAX):
                ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0] = ModCebsCom.GL_CEBS_HB_TARGET_BOARD_X_MAX;
            else:
                pass
        else:
            pass
        print("MOTO: Moving one step! Scale=%d, Dir=%d. New pos X/Y=%d/%d" % (scale, dir, ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1]));

    def funcMotoBackZero(self):
        print("MOTO: Running Zero Position!")

    def funcMotoMove2Start(self):
        print("MOTO: Running Start Position!")

    def funcMotoMove2Next(self):
        print("MOTO: Running Next Position!")

    def funcMotoStop(self):
        print("MOTO: Stop!")

    def funcMotoResume(self):
        print("MOTO: Resume action!")





        