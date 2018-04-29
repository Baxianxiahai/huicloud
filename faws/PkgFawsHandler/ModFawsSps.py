'''
Created on 2018年3月29日

@author: hitpony
'''
import random
import threading
import time  
import serial  
import string
import sys
import os

from PkgFawsHandler import ModFawsCom  #Common Support module

class ClassSpsHandler(threading.Thread):
    #def __init__(self):
    #    pass
    usbSps = "/dev/ttyUSB0"
    flag = os.path.exists(usbSps)
    if (flag == False):
        print("FAWS: Usb-Sps scale device not yet installed!\n")
        sys.exit(1)
    serSps = serial.Serial(usbSps, 9600,)  #Serial类实例化一个对象
    
    def func_read_sps_test(self):
        ModFawsCom.GL_FAWS_SPS_READ_VALUE = random.random();
        pass
    
    def func_sps_working(self):
        while True:
            count = self.serSps.inWaiting() #获取接收缓存区的字节数
            if count > 0: #如果有数据
                readData = self.serSps.read(count)  #读取数据
                #try:
                #   readData = self.serSps.read(count)  #读取数据
                #except Exception as err:
                #    print("SPS Read error!" + str(err));
                #    sys.exit(1)
                #finally:
                #   pass
                strLen = len(readData)
                tmp = ''
                for i in range(strLen):
                    tmp += chr(readData[i])
                #print("Original value = %s", tmp)
                output = tmp.split("(kg)\r\n");
                for i in range(len(output)):
                    #The formal data shall be =123.456(kg)\r\n
                    if (len(output[i]) != 8):
                        continue;
                    if  ((output[i][0] == "=") and (output[i][4] == ".")):
                        ModFawsCom.GL_FAWS_SPS_READ_VALUE = output[i][1:]
                        #print("Index=%d, String=%s" % (i, ModFawsCom.GL_FAWS_SPS_READ_VALUE))

            #For test purpose. Formal usage shall use last time saved value
            #else:
            #    ModFawsCom.GL_FAWS_SPS_READ_VALUE = int(random.random() * 1000000) / 100;
            self.serSps.flushInput()    #清空缓存区
            #print("test1, counter = %d\n" % (count));
            time.sleep(1)   #延迟1s
    
    #Fetch SPS data
    def func_read_sps_to_get_ws_data(self):
        try:
            self.func_sps_working()
        except KeyboardInterrupt:   #按下ctrl-C时需将串口关闭
            if self.serSps!=None:
                self.serSps.close()
  
    def run(self):
        while (True):
            self.func_read_sps_to_get_ws_data();
            #self.func_sps_working()
  
        
                
        
        
