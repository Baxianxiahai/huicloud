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
#from http.server import HTTPServer

#自定义
from PkgAccessEntry import ModAccessCmdHandler


class ClassEntryHttpHandler:
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''

# coding:utf-8
# 类继承
class ClassHttpRequestGenernalHandler(BaseHTTPRequestHandler):
    #def __init__(self):
        #print ("调用父类构造函数")    

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
        #print("INPUTDATA = ", inputData)
        jsonInput = json.loads(inputData)
        jsonInput=json.loads(jsonInput)
        #测试收到的内容
        print("[", time.asctime(time.localtime(time.time())), "HUIREST]: Receiving Post Data Buf = ", jsonInput)
        if(('socketid' in jsonInput) or ('data' in jsonInput)):
            varClassInputHandler = ModAccessCmdHandler.ClassHCUReportDataToDba()
        else:
            if ((("restTag" in jsonInput) == False) or (("actionId" in jsonInput) == False) or (("parFlag" in jsonInput) == False) or (("parContent" in jsonInput) == False)):
                print("HUIREST: Receiving data format error!")
                return
            if (jsonInput['restTag'] == 'printer'):
                varClassInputHandler = ModAccessCmdHandler.ClassHuirestPrinterInputCmdHandler()
            elif (jsonInput['restTag'] == 'dba'):
                varClassInputHandler = ModAccessCmdHandler.ClassHuirestDbaInputCmdHandler()
            elif (jsonInput['restTag'] == 'vision'):
                varClassInputHandler = ModAccessCmdHandler.ClassHuirestVisionInputCmdHandler()
            elif (jsonInput['restTag'] == 'sensor'):
                varClassInputHandler = ModAccessCmdHandler.ClassHuirestSensorInputCmdHandler()
            elif (jsonInput['restTag'] == 'special'):
                varClassInputHandler = ModAccessCmdHandler.ClassHuirestSpecialInputCmdHandler()
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