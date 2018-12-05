'''
Created on 2018年12月4日

@author: Administrator
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


#DEFINE ALL PROJECT
GL_PRJ_SET_MFUN_CENTOS      = 1
GL_PRJ_SET_HCU_MATE         = 2
GL_PRJ_SET_CEBS_WIN         = 3

#SET CURRENT WORKING PROJECTS
#GL_PRJ_CUR_SET              = GL_PRJ_SET_MFUN_CENTOS
#GL_PRJ_CUR_SET              = GL_PRJ_SET_HCU_MATE
GL_PRJ_CUR_SET              = GL_PRJ_SET_CEBS_WIN


'''

PART1: 项目级开关控制
全局变量控制配置参数，进行适当封装

'''

class clsL0_PrjCfgPar():
    if GL_PRJ_CUR_SET == GL_PRJ_SET_MFUN_CENTOS:
        PRJ_SER_PRINTER = False
        PRJ_SER_DBA = True
        PRJ_SER_VISION = False
        PRJ_SER_AIWGT = False
        PRJ_SER_SENSOR = False
        PRJ_SER_SPECIAL = False
    if GL_PRJ_CUR_SET == GL_PRJ_SET_HCU_MATE:
        PRJ_SER_PRINTER = True
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_CEBS_WIN:
        PRJ_SER_PRINTER = False
        PRJ_SER_DBA = False
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True
    
    #初始化
    def __init__(self):    
        super(clsL0_PrjCfgPar, self).__init__()  
        pass
    
    def funcTest(self):
        pass
    
GL_PRJ_PAR = clsL0_PrjCfgPar()




'''

PART2: 全局公共参考配置信息


'''
class clsL0_ComCfgPar():
    COM_SER_PRINTER = False
    
    #初始化
    def __init__(self):    
        super(clsL0_ComCfgPar, self).__init__()  
        pass
    
    
GL_COM_PAR = clsL0_ComCfgPar()























        