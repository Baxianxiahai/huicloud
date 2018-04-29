'''
Created on 2018年3月29日

@author: hitpony
'''

import sys
import os
import threading
import ctypes 
import struct
import string


from PkgFawsHandler import ModFawsCom  #Common Support module

class ClassInsertHandler(object):

    def __init__(self):
        pass

    def func_judge_rfid_inserted_or_not(self):
        Flag = 0;
        path = '/sys/class/input/'
        for i in os.listdir(path):
            if 'event' in i:
                tmp = open(path + i + '/device/name')
                res = tmp.read()
                if 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader' in res:
                    print("FAWS: Target RFID sensor = ", res)
                    #print("i=", int(i[5:], base=10))
                    ModFawsCom.GL_FAWS_RFID_KB_EVENT_ID = int(i[5:], base=10)
                    Flag = 1;
                    ModFawsCom.GL_FAWS_RFID_CARD_INSERT = True;
#                     if (ModFawsCom.GL_FAWS_RFID_CARD_INSERT == False):
#                         ModFawsCom.GL_FAWS_RFID_CARD_INSERT = True;
#                         ModFawsCom.GL_FAWS_RFID_CARD_PULLIN = True;
                    #print("Insert = %d" %ModFawsCom.GL_FAWS_RFID_CARD_INSERT);
                tmp.close()
        if (Flag == 0):
#             if (ModFawsCom.GL_FAWS_RFID_CARD_INSERT == True):
#                 ModFawsCom.GL_FAWS_RFID_CARD_INSERT = False;
#                 ModFawsCom.GL_FAWS_RFID_CARD_PULLOUT = True;
#             else:
#                 ModFawsCom.GL_FAWS_RFID_CARD_INSERT = False;
            ModFawsCom.GL_FAWS_RFID_CARD_INSERT = False;
            print("RFID not yet inserted, so return back!")
            sys.exit(1)
    
#Use keyboard to simulate
class ClassReadRfidInput(threading.Thread):
#     def __init__(self):
#         self._running = True
#  
#     def terminate(self):
#         self._running = False
    
    def run(self):
        ll = ctypes.cdll.LoadLibrary   
        lib = ll("./libFawsKbCap.so")

        #while (self._running == True):
        while (True):
            #count = ser.in_waiting() #获取接收缓存区的字节数
            #if count!=0: #如果有数据
            #recv = ser.read(count)  #读取数据
            #ser.flushInput()    #清空缓存区            
            #Old mode, actually not really working
            #if (sInput != null):
            outStr = (b'0')*100;
            strLen = lib.kbCapture(ModFawsCom.GL_FAWS_RFID_KB_EVENT_ID, outStr);
            if (strLen > 0):
                output = outStr[:strLen];
                strLen = len(output)
                tmp = ''
                for i in range(strLen):
                    tmp += chr(output[i])
                ModFawsCom.GL_FAWS_RFID_READ_VALUE = tmp
                #ModFawsCom.GL_FAWS_RFID_READ_VALUE = outStr.decode('utf-8');
                ModFawsCom.GL_FAWS_RFID_INPUT_FLAG = True;
            
        #Close port
    
    
    
