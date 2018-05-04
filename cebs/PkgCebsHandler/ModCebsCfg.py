'''
Created on 2018年5月4日

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-


import configparser
from PkgCebsHandler import ModCebsCom


class ConfigReader(object):
    def __init__(self, path):
        self.filePath = path
        self.CReader=configparser.ConfigParser()
        self.CReader.read(self.filePath, encoding='utf8')

    def getSection(self):
        return self.CReader.sections()

    def getdic(self, section):
        s={}
        for k,v in self.CReader.items(section):
            s[k]=v
        return s
    
    #写入宿舍配置文件
    def writeRoomInfo(self):
        try:
            self.CReader.add_section("School")
            self.CReader.set("School","IP","10.15.40.123")
            self.CReader.set("School","Mask","255.255.255.0")
            self.CReader.set("School","Gateway","10.15.40.1")
            self.CReader.set("School","DNS","211.82.96.1")
        except configparser.DuplicateSectionError:
            print("Section 'School' already exists")
        
    #写入比赛配置文件
    def writeMatchInfo(self):
        try:
            self.CReader.add_section("Match")
            self.CReader.set("Match","IP","172.17.29.120")
            self.CReader.set("Match","Mask","255.255.255.0")
            self.CReader.set("Match","Gateway","172.17.29.1")
            self.CReader.set("Match","DNS","0.0.0.0")
        except configparser.DuplicateSectionError:
            print("Section 'Match' already exists")

    #写入全局控制数据
    def writeCtrlCntInfo(self):
        try:
            self.CReader.add_section("Counter")
            self.CReader.set("Counter","PicRemainCnt", str(ModCebsCom.GL_CEBS_PIC_PROC_REMAIN_CNT))
        except configparser.DuplicateSectionError:
            print("Section 'Counter' already exists")

    #写入配置文件
    def writeCfgInfo(self):        
        self.CReader.write(open(self.filePath, "w"))
        
    #测试读取
    def readCfgInfo(self):         
        ip=self.CReader.get("School","IP")
        mask=self.CReader.get("School","mask")
        gateway=self.CReader.get("School","Gateway")
        dns=self.CReader.get("School","DNS")
        print((ip,mask+"\n"+gateway,dns))
        
    #测试读取
    def readCfgTest(self):
        self.writeRoomInfo()
        self.writeMatchInfo()
        self.writeCfgInfo()
        self.readCfgInfo() 
        
    #正式工作模式
    def readCfgFormal(self):
        self.writeRoomInfo()
        self.writeMatchInfo()
        self.writeCtrlCntInfo()
        self.writeCfgInfo()
        self.readCfgInfo() 
        
        
        
        
                