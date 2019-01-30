'''
Created on 2017年12月11日

@author: hitpony
'''

import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  
import urllib   #用于对URL进行编解码  
import http
import socket
from http.server import BaseHTTPRequestHandler

#自定义
from PkgAccessEntry import ModAccessCmdHandler
from PkgAccessEntry import ModAccessCom

# coding:utf-8
# 类继承
class ClassHttpRequestGenernalHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        #print ("Path=", self.path)
        #print ("Header=", self.headers)
        #print ("RequestLine=", self.raw_requestline)
        #print ("Request=", self.request)
        self.send_response(200);
        self.send_header('Content-type','text/html');
        self.end_headers()
        
    def do_Head(self):
        self._writeheaders()
        
    def do_GET(self):
        self._writeheaders()
        self.wfile.write(bytes("""<!DOCTYPE HTML>
        <html lang="en-US">
        <head>
        <meta charset="UTF-8">
        <title>HUIREST SERVICE - GET</title>
        </head>
        <body>
        <p>this is get!</p>
        </body>
        </html>"""+str(self.headers), "UTF-8"))
        
    def do_POST(self):
        self._writeheaders()
        length = self.headers.get('content-length');
        nbytes = int(length)
        inputData = self.rfile.read(nbytes)
        #统一处理入口，需要解码json输入结构
        #print("INPUTDATA = ", type(inputData))
        jsonInput = json.loads(inputData)
        #测试收到的内容
        print("[", time.asctime(time.localtime(time.time())), "HUIREST]: Receiving Post Data Buf = ", jsonInput)
        if(('socketid' in jsonInput) or ('data' in jsonInput)):
            varClassInputHandler = ModAccessCmdHandler.ClassHCUReportDataToDba()
        else:
            if ((("restTag" in jsonInput) == False) or (("actionId" in jsonInput) == False) or (("parFlag" in jsonInput) == False) or (("parContent" in jsonInput) == False)):
                print("HUIREST: Receiving data format error!")
                return
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_PRINTER == True):
                if (jsonInput['restTag'] == 'printer'): 
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestPrinterInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_DBA == True):
                if (jsonInput['restTag'] == 'dba'): 
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestDbaInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_VISION == True):
                if (jsonInput['restTag'] == 'vision'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestVisionInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_AIWGT == True):
                if (jsonInput['restTag'] == 'aiwgt'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestAiwgtInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SENSOR == True):
                if (jsonInput['restTag'] == 'sensor'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestSensorInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SPECIAL == True):
                if (jsonInput['restTag'] == 'special'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestSpecialInputCmdHandler()
            elif (ModAccessCom.GL_PRJ_PAR.PRJ_SER_MDC == True):
                if (jsonInput['restTag'] == 'mdc'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestMdcInputCmdHandler()
            #NOT EXIST OPTION
            else:
                print("HUIREST: Receiving restTag domain error!")
                return
        #准备继续干活
        varProcessResult = varClassInputHandler.inputCmdHandlerEntry(jsonInput)
        strOutputData1 = """<!DOCTYPE HTML>
        <html lang="en-US">
        <head>
        <meta charset="UTF-8">
        <title>HUIREST SERVICE - POST</title>
        </head>
        <body>
        <p>this is post!</p>
        </body>
        </html>"""+str(self.headers)+str(self.command)+str(self.headers.get)+str(varProcessResult)
        strOutputData2 = json.dumps(varProcessResult, ensure_ascii=False)
        print("[", time.asctime(time.localtime(time.time())), "HUIREST]: Sending Post Data Buf = ", strOutputData2)
        self.wfile.write(bytes(strOutputData2, "UTF-8"))
        print("")
        return
        
        
        
        
        
        
        
        