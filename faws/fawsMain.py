'''
Created on 2018/3/28

@author: hitpony
'''

#!/opt/bin/python3.6
# -*- coding: UTF-8 -*-

import datetime
import sys
import time
import json
import os
import re
import urllib
import http
import socket
import hashlib
import ctypes 
import serial
import tty 
import string

#Internal Mod and Class
from PkgFawsHandler import ModFawsCom  #Common Support module
from PkgFawsHandler import ModFawsCloud  #Cloud communication module
from PkgFawsHandler import ModFawsSps  #Sps data read module
from PkgFawsHandler import ModFawsRfid  #RFID read module


#SYSTEM ENTRY
if __name__ == '__main__':
    print("[FAWS] ", time.asctime(), ", System starting...\n" );

    #RFID HW installed
    objRfidInsert = ModFawsRfid.ClassInsertHandler();
    objRfidInsert.func_judge_rfid_inserted_or_not();
    objRfidRead = ModFawsRfid.ClassReadRfidInput();
    objRfidRead.start()
    #cRfid.terminate()  #Terminate this thread
    #cRfid.join()       #Wait this this task end
     
    #Init RFID input control flag
    ModFawsCom.GL_FAWS_RFID_INPUT_FLAG = False;
     
    #Detect SPS port!
    objSps = ModFawsSps.ClassSpsHandler();
    objSps.start()
     
    #Cloud Obj
    objCloud = ModFawsCloud.ClassHandler();
    gpioObj = ModFawsCloud.ClassGpioAccessHandler();
    
    #Blink LED let user aware of sysetm startup
    gpioObj.func_gpio_led_startup_blink();
 
    #Infinate loop
    while True:
        time.sleep(1)
        ModFawsCom.GL_FAWS_GLOBAL_CNT += 1;
         
        #Refresh the sps data read, if true->refresh the global variable, otherwise keep no change
        #Once use different thread, so no need call function but wait thread working alone.
        #objSps.func_read_sps_test();
        
        #Judge whether RFID active to trigger read result
        if (ModFawsCom.GL_FAWS_RFID_INPUT_FLAG == True):
            #print(len(ModFawsCom.GL_FAWS_RFID_READ_VALUE))
            #sStr2 = string(b'0', encoding = 'utf-8');
            #sStr2 = str(b'0');
            #nPos = (ModFawsCom.GL_FAWS_RFID_READ_VALUE).index(sStr2)
            #tmp = (ModFawsCom.GL_FAWS_RFID_READ_VALUE)[:nPos]
            objCloud.func_data_report(ModFawsCom.GL_FAWS_RFID_READ_VALUE, ModFawsCom.GL_FAWS_SPS_READ_VALUE);
            ModFawsCom.GL_FAWS_RFID_INPUT_FLAG = False;
         
        #Trigger for awareness
        #print("Running round = ", ModFawsCom.GL_FAWS_GLOBAL_CNT);
 
    #END
    pass
    




#     #TEST
#     u = [0] * 9
#     flag = False
#     for tt in range(123, 329):
#         #print(tt)
#         o1 = tt * 2
#         o2 = tt * 3
#         u[0] = tt//100
#         u[1] = tt//10 - u[0]*10
#         u[2] = tt - u[0] * 100 - u[1] * 10
#         u[3] = o1//100
#         u[4] = o1//10 - u[3]*10
#         u[5] = o1 - u[3] * 100 - u[4] * 10
#         u[6] = o2//100
#         u[7] = o2//10 - u[6]*10
#         u[8] = o2 - u[6] * 100 - u[7] * 10
#         if ((u[0] <= 0) or (u[0] > 9)):
#             continue;
#         if ((u[1] <= 0) or (u[1] > 9)):
#             continue;
#         if ((u[2] <= 0) or (u[2] > 9)):
#             continue;
#         if ((u[3] <= 0) or (u[3] > 9)):
#             continue;
#         if ((u[4] <= 0) or (u[4] > 9)):
#             continue;
#         if ((u[5] <= 0) or (u[5] > 9)):
#             continue;
#         if ((u[6] <= 0) or (u[6] > 9)):
#             continue;
#         if ((u[7] <= 0) or (u[7] > 9)):
#             continue;
#         if ((u[8] <= 0) or (u[8] > 9)):
#             continue;
#         Flag = True;
#         for i in range (1, 8):
#             for j in range (i):
#                 if (u[j] == u[i]):
#                     Flag = False;
#                     break;
#         if (Flag == False):
#             continue;
#         else:
#             print("Find a good one = ", tt)
                
    
    
