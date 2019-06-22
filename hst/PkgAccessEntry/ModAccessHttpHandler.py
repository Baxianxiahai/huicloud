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
import urllib
import urllib3
import requests
import socket
import pycurl
import io
import certifi  #导入根证书集合，用于验证SSL证书可信和TLS主机身份
from io import BytesIO
from urllib.parse import urlencode

from http.server import BaseHTTPRequestHandler

#自定义
from PkgAccessEntry import ModAccessCmdHandler
from PkgAccessEntry import ModAccessCom

# coding:utf-8
# 类继承
class ClassHttpRequestGenernalHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
#         print ("Path=", self.path)
#         print ("Header=", self.headers)
#         print ("RequestLine=", self.raw_requestline)
#         print ("Request=", self.request)
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
        jsonInput = ''
        try:
            jsonInput = json.loads(inputData)
            jsonInput = json.loads(jsonInput,strict=False)
        except Exception:
            #jsonInput = urllib.parse.unquote(bytes(inputData))\
            #jsonInput = urllib.parse.urlurlopen(inputData)
            pass
        
        #测试收到的内容
        print("[", time.asctime(time.localtime(time.time())), "HUIREST]: Receiving Post Data Buf = ", str(jsonInput))
#         print(type(jsonInput))
        if(('socketid' in jsonInput) or ('data' in jsonInput)):
            varClassInputHandler = ModAccessCmdHandler.ClassHCUReportDataToDba()
        elif(('serviceId') in jsonInput):
            varClassInputHandler = ModAccessCmdHandler.ClassNbiotReportDataToDba()
        else:
            if ((("restTag" in jsonInput) == False) or (("actionId" in jsonInput) == False) or (("parFlag" in jsonInput) == False) or (("parContent" in jsonInput) == False)):
                print("HUIREST: Receiving data format error!")
                return
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_PRINTER == True):
                if (jsonInput['restTag'] == 'printer'): 
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestPrinterInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_DBA == True):
                if (jsonInput['restTag'] == 'dba'): 
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestDbaInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_VISION == True):
                if (jsonInput['restTag'] == 'vision'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestVisionInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_AIWGT == True):
                if (jsonInput['restTag'] == 'aiwgt'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestAiwgtInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SENSOR == True):
                if (jsonInput['restTag'] == 'sensor'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestSensorInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_SPECIAL == True):
                if (jsonInput['restTag'] == 'special'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestSpecialInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_MDC == True):
                if (jsonInput['restTag'] == 'mdc'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestMdcInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_MPLAYER == True):
                if (jsonInput['restTag'] == 'mplayer'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestMplayerInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FACEID == True):
                if (jsonInput['restTag'] == 'faceid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestFaceidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_CARNUMID == True):
                if (jsonInput['restTag'] == 'carnumid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestCarnumidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_BILLID == True):
                if (jsonInput['restTag'] == 'billid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestBillidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_INVOICEID == True):
                if (jsonInput['restTag'] == 'involiceid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestInvoiceidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_STEPID == True):
                if (jsonInput['restTag'] == 'stepid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestStepidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_PATID == True):
                if (jsonInput['restTag'] == 'patid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestPatidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FRUITID == True):
                if (jsonInput['restTag'] == 'fruitid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestFruitidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_VEGID == True):
                if (jsonInput['restTag'] == 'vegid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestVegidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_FLOWERID == True):
                if (jsonInput['restTag'] == 'flowerid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestFloweridInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_ROADWID == True):
                if (jsonInput['restTag'] == 'roadwid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestRoadwidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_ROADFID == True):
                if (jsonInput['restTag'] == 'roadfid'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestRoadfidInputCmdHandler()
            if (ModAccessCom.GL_PRJ_PAR.PRJ_SER_CEWORM == True):
                if (jsonInput['restTag'] == 'ceworm'):
                    varClassInputHandler = ModAccessCmdHandler.ClassHuirestCewormInputCmdHandler()
            #NOT EXIST OPTION
#             else:
#                 print("HUIREST: Receiving restTag domain error!")
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
        
        
        
        