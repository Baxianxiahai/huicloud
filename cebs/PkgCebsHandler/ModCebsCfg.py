'''
Created on 2018年5月4日

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-


import configparser
import os
import platform
from PkgCebsHandler import ModCebsCom


class ConfigOpr(object):
    def __init__(self):
        self.filePath = ModCebsCom.GL_CEBS_CFG_FILE_NAME
        self.initGlobalPar()

    #初始化所有的存储区
    def initGlobalPar(self):
        #判定捕获图像的工作文件目录
        ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH = os.getcwd()+ self.osDifferentStr() + ModCebsCom.GL_CEBS_PIC_ORIGIN_PATH
        flag = os.path.exists(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH)
        if (flag == False):
            os.mkdir(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH)
        ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH += self.osDifferentStr()
        #判定中间图像的工作文件目录
        ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH = os.getcwd()+ self.osDifferentStr() + ModCebsCom.GL_CEBS_PIC_MIDDLE_PATH
        flag = os.path.exists(ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH)
        if (flag == False):
            os.mkdir(ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH)
        ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH += self.osDifferentStr()
        #判定是否需要创建ini文件
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')
        flag = os.path.exists(self.filePath)
        if (flag == False):
            self.CReader.add_section("Env")
            self.CReader.set("Env","workdir", str(os.getcwd()+ self.osDifferentStr()))
            self.CReader.set("Env","pic_origin", str(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH))
            self.CReader.set("Env","pic_middle", str(ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH))
            self.CReader.add_section("Counter")
            self.CReader.set("Counter","PicBatchCnt", "0")
            self.CReader.set("Counter","PicBatchClas", "0")
            self.CReader.set("Counter","PicRemainCnt", "0")
            self.CReader.write(open(self.filePath, "w"))
        #为了防止ini文件中信息错误，重新写入
        if (self.CReader['Env']['workdir'] != str(os.getcwd()+ self.osDifferentStr())):
            self.updateSectionPar()

    def readGlobalPar(self):
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')        
        ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX = int(self.CReader['Counter']['PicBatchCnt']);
        ModCebsCom.GL_CEBS_PIC_PROC_CLAS_INDEX = int(self.CReader['Counter']['PicBatchClas']);
        ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT = int(self.CReader['Counter']['PicRemainCnt']);

    def getSection(self):
        return self.CReader.sections()

    def getdic(self, section):
        s={}
        for k,v in self.CReader.items(section):
            s[k]=v
        return s

    def osDifferentStr(self):
        sysstr = platform.system()
        if(sysstr =="Windows"):
            return '\\'
        elif(sysstr == "Linux"):
            return '/'
        else:
            return '/'

    def updateSectionPar(self):
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')        
        if (self.CReader.has_section("Env") == False):
            self.CReader.add_section("Env")
            self.CReader.set("Env","workdir", str(os.getcwd()+ self.osDifferentStr()))
            self.CReader.set("Env","pic_origin", str(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH))
            self.CReader.set("Env","pic_middle", str(ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH))
        else:
            self.CReader.remove_section("Env")
            self.CReader.add_section("Env")        
            self.CReader.set("Env","workdir", str(os.getcwd()+ self.osDifferentStr()))
            self.CReader.set("Env","pic_origin", str(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH))
            self.CReader.set("Env","pic_middle", str(ModCebsCom.GL_CEBS_PIC_ABS_MIDDLE_PATH))
        fd = open(self.filePath, 'w')
        self.CReader.write(fd)
        fd.close()
                
    #写入全局控制数据
    def updateCtrlCntInfo(self):
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')
        if (self.CReader.has_section("Counter") == False):
            self.CReader.add_section("Counter")
            self.CReader.set("Counter","PicBatchCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX))
            self.CReader.set("Counter","PicBatchClas", str(ModCebsCom.GL_CEBS_PIC_PROC_CLAS_INDEX))
            self.CReader.set("Counter","PicRemainCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT))
            
        else:
            self.CReader.remove_section("Counter")
            self.CReader.add_section("Counter")
            self.CReader.set("Counter","PicBatchCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_BATCH_INDEX))
            self.CReader.set("Counter","PicBatchClas", str(ModCebsCom.GL_CEBS_PIC_PROC_CLAS_INDEX))
            self.CReader.set("Counter","PicRemainCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT))
        fd = open(self.filePath, 'w')
        self.CReader.write(fd)
        fd.close()

    def createBatch(self, batch):
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')
        batchStr = "batch#" + str(batch)
        if (self.CReader.has_section(batchStr) == True):
            self.CReader.remove_section(batchStr)
            self.CReader.add_section(batchStr)
        else:
            self.CReader.add_section(batchStr)
        self.CReader.set(batchStr, "batch_number", str(batch))
        fd = open(self.filePath, 'w')
        self.CReader.write(fd)
        fd.close()

    def addBatchFile(self, batch, fileNbr):
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')
        batchStr = "batch#" + str(batch)
        fileName = str("batchFileName#" + str(fileNbr))
        fileClas = str("batchFileClas#" + str(fileNbr))
        self.CReader.set(batchStr, fileName, str(ModCebsCom.GL_CEBS_PIC_ABS_ORIGIN_PATH) + fileName + '.jpg')
        self.CReader.set(batchStr, fileClas, 'no')
        fd = open(self.filePath, 'w')
        self.CReader.write(fd)
        fd.close()

    def getUnclasBatchFile(self, batch):
        pass

    def updateBatchFile(self, batch, fileNbr):
        batchStr = "batch#" + str(batch)
        if (self.CReader.has_section(batchStr) == True):
            self.CReader.remove_section(batchStr)
            self.CReader.add_section(batchStr)
        self.CReader.set(batchStr,"PicRemainCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT))
        fd = open(self.filePath, 'w')
        self.CReader.write(fd)
        fd.close()







