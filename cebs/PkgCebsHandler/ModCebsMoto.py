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





        