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


#DEFINE ALL PROJECT AS TEST
GL_PRJ_SET_HCU_TEST_WIN     = 1     #HCU测试-WINDOWS
GL_PRJ_SET_HCU_TEST_MATE    = 2     #HCU测试-MATE
GL_PRJ_SET_TUP_TEST_WIN     = 3     #TUP测试-WIN
GL_PRJ_SET_TUP_TEST_UBUNTU  = 4     #TUP测试-UBUNTU
#后台服务
GL_PRJ_SET_MFUN_CENTOS      = 10     #后台服务
#流水线
GL_PRJ_SET_BFSL_UBUNTU      = 20    #波峰流水线测试系统
GL_PRJ_SET_HESL_MATE        = 21    #自有流水线测试系统
#定制服务
GL_PRJ_SET_GTJY_CENTOS      = 30    #国通教育转码
#工厂烧录工具系列
GL_PRJ_SET_FMPT_WIN         = 40    #PC版FMPT工具
GL_PRJ_SET_FMPT_MATE        = 41    #树莓派版FMPT工具
#CEBS滑台
GL_PRJ_SET_CEBS_WIN         = 50    #CEBS滑台在WINDOWS上的应用
GL_PRJ_SET_CEBS_MATE        = 51    #CEBS滑台在MATE上的应用
#媒体播放器
GL_PRJ_SET_FSTT_MP_WIN      = 60    #复珊媒体播放器-WIN
GL_PRJ_SET_FSTT_MP_ANDROID  = 61    #复珊媒体播放器-Andriod
GL_PRJ_SET_FSTT_MP_MATE     = 62    #复珊媒体播放器-Andriod
#人脸识别项目
GL_PRJ_SET_FACEID_WIN       = 70    #人脸识别-WIN
GL_PRJ_SET_FACEID_ANDROID   = 71    #人脸识别-ANDROID
GL_PRJ_SET_FACEID_UBUNTU    = 72    #人脸识别-UBUNTU
#发票识别
GL_PRJ_SET_INVOICE_WIN      = 80    #发票识别-WIN
#小票识别
GL_PRJ_SET_BILL_SMALL_WIN   = 90    #小票识别-WIN
#蔬菜识别
GL_PRJ_SET_VEGTABLE_WIN     = 100   #蔬菜识别-WIN
#花卉识别
GL_PRJ_SET_FLOWER_WIN       = 110   #花卉识别-WIN
#道路积水识别
GL_PRJ_SET_ROAD_WATER_WIN   = 120   #道路积水识别-WIN
#病例卡识别
GL_PRJ_SET_PATIENT_BILL_WIN = 130   #病例卡识别-WIN
#车牌识别
GL_PRJ_SET_CAR_ID_WIN       = 140   #车牌识别-WIN
#步态异常识别
GL_PRJ_SET_HUMAN_STEP_WIN   = 150   #步态异常识别-WIN




#SET CURRENT WORKING PROJECTS
GL_PRJ_CUR_SET              = GL_PRJ_SET_CEBS_WIN


'''

PART1: 项目级开关控制
全局变量控制配置参数，进行适当封装

'''

class clsL0_PrjCfgPar():
    #GLOBAL DEFINATION
    PRJ_SER_PRINTER = False     #打印机服务
    PRJ_SER_DBA = False         #数据库服务
    PRJ_SER_VISION = False      #图像抓取识别服务
    PRJ_SER_AIWGT = False       #AI称重算法服务
    PRJ_SER_SENSOR = False      #传感器读取服务
    PRJ_SER_SPECIAL = False     #三表转码服务
    PRJ_SER_MDC = False         #马达驱控服务
    PRJ_SER_MPLAYER = False     #媒体播放器服务
    PRJ_SER_FACEID = False      #人脸识别
    PRJ_SER_CARNUMID = False    #车牌识别
    PRJ_SER_BILLID = False      #餐厅小票识别
    PRJ_SER_INVOICEID = False   #发票识别
    PRJ_SER_STEPID = False      #步态识别
    PRJ_SER_PATID = False       #病例卡识别
    PRJ_SER_FRUITID = False     #水果识别
    PRJ_SER_VEGID = False       #蔬菜识别
    PRJ_SER_FLOWERID = False    #花卉识别
    PRJ_SER_ROADWID = False     #路面积水识别
    PRJ_SER_ROADFID = False     #路边花草识别
    PRJ_SER_CEWORM = True      #白光线虫照片识别
    
    #DIFFERENT PROJECT DEFINE
    if GL_PRJ_CUR_SET == GL_PRJ_SET_MFUN_CENTOS:
        PRJ_SER_DBA = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_HCU_TEST_MATE:
        PRJ_SER_PRINTER = True
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True
        PRJ_SER_MDC = True        
        PRJ_SER_MPLAYER = True        
    if GL_PRJ_CUR_SET == GL_PRJ_SET_HCU_TEST_WIN:
        PRJ_SER_PRINTER = True
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True        
        PRJ_SER_MDC = True        
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_TUP_TEST_WIN:
        PRJ_SER_PRINTER = True
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True        
        PRJ_SER_MDC = True        
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_TUP_TEST_UBUNTU:
        PRJ_SER_PRINTER = True
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_AIWGT = True
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True        
        PRJ_SER_MDC = True        
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_BFSL_UBUNTU:
        PRJ_SER_PRINTER = True
        PRJ_SER_AIWGT = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_HESL_MATE:
        PRJ_SER_PRINTER = True
        PRJ_SER_AIWGT = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_GTJY_CENTOS:
        PRJ_SER_SENSOR = True
        PRJ_SER_SPECIAL = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FMPT_WIN:
        PRJ_SER_PRINTER = True 
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FMPT_MATE:
        PRJ_SER_PRINTER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_CEBS_WIN:
        PRJ_SER_DBA = True
        PRJ_SER_VISION = True
        PRJ_SER_MDC = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_CEBS_MATE:
        PRJ_SER_VISION = True
        PRJ_SER_MDC = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FSTT_MP_WIN:
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FSTT_MP_ANDROID:
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FSTT_MP_MATE:
        PRJ_SER_MPLAYER = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FACEID_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FACEID_ANDROID:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FACEID_UBUNTU:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_INVOICE_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_BILL_SMALL_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_VEGTABLE_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_FLOWER_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_ROAD_WATER_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_PATIENT_BILL_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_CAR_ID_WIN:
        PRJ_SER_VISION = True
    if GL_PRJ_CUR_SET == GL_PRJ_SET_HUMAN_STEP_WIN:
        PRJ_SER_VISION = True
    
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
    COM_TEST1 = 1
    
    #初始化
    def __init__(self):    
        super(clsL0_ComCfgPar, self).__init__()  
        pass
    
    
GL_COM_PAR = clsL0_ComCfgPar()























        