'''
Created on 2018年3月29日

@author: hitpony
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
import struct
import string
import datetime  
#import pycurl
import urllib
import json
import time
import urllib3
import socket
import hashlib
import platform
import RPi.GPIO as GPIO



#Local include
from PkgFawsHandler import ModFawsCom  #Common Support module


#class
#有关这个地方的处理，还有问题！
class ClassGpioAccessHandler(object):
    def __init__(self):
        pass
    
    def func_gpio_led_blink(self):
        GPIO_PIN = 0;

        ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = platform.machine()
        if "x86" in ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG:
            ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = False
        else:
            ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = True
        #BCM=12, Port=32(TX)/34(GND)
        GPIO_PIN = 12
        
        if ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG == True:
            #GPIO.setmode(GPIO.BOARD) #板子索引号
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(GPIO_PIN, GPIO.OUT)
            #while True:
            GPIO.output(GPIO_PIN, GPIO.HIGH)
            time.sleep(0.33)
            GPIO.output(GPIO_PIN, GPIO.LOW)
            time.sleep(0.33)
            GPIO.output(GPIO_PIN, GPIO.HIGH)
            time.sleep(0.33)
            GPIO.output(GPIO_PIN, GPIO.LOW)
        else:
            print("FAWS: GPIO RPi not supported in this machine, so here just no output invalid test func!")
            return;

    def func_gpio_led_startup_blink(self):
        GPIO_PIN = 0;

        ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = platform.machine()
        if "x86" in ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG:
            ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = False
        else:
            ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG = True
        #BCM=12, Port=32(TX)/34(GND)
        GPIO_PIN = 12
        
        if ModFawsCom.GL_FAWS_GLOBAL_RPI_FLAG == True:
            #GPIO.setmode(GPIO.BOARD) #板子索引号
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(GPIO_PIN, GPIO.OUT)
            for i in range(5):
                GPIO.output(GPIO_PIN, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(GPIO_PIN, GPIO.LOW)
                time.sleep(0.1)
        else:
            print("FAWS: GPIO RPi not supported in this machine, so here just no output invalid test func!")
            return;
        
class ClassCloudProc(ClassGpioAccessHandler):
    zStrFawsCloudConHuitpJsonDataReport = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "IeCnt": {},\
        "FnFlg": 0\
        }

    zStrFawsCloudConHuitpJsonDataConfirm = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "MsgLn": 0,\
        "IeCnt": {},\
        "FnFlg": 0\
        }
    
    #Init this class
    def __init__(self):
        self.zStrFawsCloudConHuitpJsonDataReport = {\
            "ToUsr": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "FrUsr": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFawsCom.GL_FAWS_HUITP_JSON_MSGID_uni_faws_data_report,\
            "MsgLn": 0,\
            "IeCnt": {\
                "rfidUser": ModFawsCom.GL_FAWS_RFID_READ_VALUE,\
                "spsValue": ModFawsCom.GL_FAWS_SPS_READ_VALUE,\
                      },\
            "FnFlg": 0\
            }
    
        self.zStrFawsCloudConHuitpJsonDataConfirm = {\
            "ToUsr": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "FrUsr": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFawsCom.GL_FAWS_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFawsCom.GL_FAWS_HUITP_JSON_MSGID_uni_faws_data_confirm,\
            "MsgLn": 0,\
            "IeCnt": {\
                    "resFlag": 0,\
                      },\
            "FnFlg": 0\
            }

    #Setup connection with back-hawl
    def FuncCurlib3ClientConnection(self, jsonInputData):
        encoded_data = json.dumps(jsonInputData).encode('utf-8')
        http = urllib3.PoolManager(maxsize=10, block=True)
        timeout = 3
        socket.setdefaulttimeout(timeout)
        r = http.request(
            'POST',
            #'http://' + ModFawsCom.GL_FAWS_CLOUDCON_PAR_IP_ADDR_SET_BY_USER + ':' + ModFawsCom.GL_FAWS_CLOUDCON_HUITP_JSON_PORT + '/',
            'http://' + ModFawsCom.GL_FAWS_CLOUDCON_PAR_IP_ADDR_SET_BY_USER + ':' + '80' + '/mfunhcu/l1mainentry/cloud_callback_faam.php',
            body=encoded_data,
            headers={'Content-Type': 'application/json'})
        res = json.loads(r.data)
        return res
    

    #Send data to backhawl
    def funcSendData2Cloud(self, rfidUser, spsValue): 
        #Formal start
        res = {}
        #sndData = {"UserRfid": rfidUser, "Data": spsValue};
        self.zStrFawsCloudConHuitpJsonDataReport['IeCnt']['rfidUser'] = rfidUser;
        self.zStrFawsCloudConHuitpJsonDataReport['IeCnt']['spsValue'] = spsValue;
        self.zStrFawsCloudConHuitpJsonDataReport['MsgLn'] = len(json.dumps(self.zStrFawsCloudConHuitpJsonDataReport['IeCnt']).encode('utf-8'));
        print(self.zStrFawsCloudConHuitpJsonDataReport)

        #Send to Back-hawl and wait for feedback
        #self.func_gpio_led_blink();
        res['res'] = 1;
        try:
            callRes = self.FuncCurlib3ClientConnection(self.zStrFawsCloudConHuitpJsonDataReport);
        except Exception as err:
            res['res'] = -1;
            print("Send data to back-hawl error: " + str(err))
        finally:
            if (res['res'] == -1):
               return res;
        print("Return Result=", callRes)
        output = callRes;

        #decode feedback
        if (('IeCnt' in output) == True):
            if (('resFlag' in output['IeCnt']) == True):
                self.zStrFawsCloudConHuitpJsonDataConfirm['IeCnt']['resFlag'] = output['IeCnt']['resFlag'];
                if (self.zStrFawsCloudConHuitpJsonDataConfirm['IeCnt']['resFlag'] == True):
                    res['res'] = 1;
                    res['value'] = self.zStrFawsCloudConHuitpJsonDataConfirm;
                    self.func_gpio_led_blink();
                else:
                    res['res'] = -2;
            else:
                res['res'] = -3;
        else:
            res['res'] = -4;
        
        #Return back
        #print(res)
        return res;  

#Entry class
#class ClassHandler(ClassCloudProc):
class ClassHandler(object):
    def __init__(self):
        pass
    
    #UI apply label by batch
    def func_data_report(self, rfidUser, spsValue):
        try:
            #objCloud =  ClassCloudProc();
            res = {}
            res['res'] = 1
            procObj = ClassCloudProc();
            callRes = procObj.funcSendData2Cloud(rfidUser, spsValue);
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_data_report failure in low layer.'
                res['res'] = callRes['res']
                #处罚本地告警.差错报告等方式，待完善
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_data_report'            
        except Exception as err:  
            print("Exec Err: func_data_report!" + str(err))
            return ("Exec Err: func_data_report!" + str(err))
        finally:
            return res;   
    
    
    

        
        
