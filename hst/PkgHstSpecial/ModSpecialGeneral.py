'''
Created on Mar 9, 2018

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
import jpype

class ClassModSpecialTest1(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, input):
        res = {"test1": "this is my test!", "test2": 0x22}
        return res

class ClassGtjyWaterMeter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def funcEncoding(self, input):
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.join(os.path.abspath('./PkgHstSpecial'), '')
        if not jpype.isJVMStarted():
            jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'ReadMeterData.jar'))
        javaClass = jpype.JClass('com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces')
        jd = javaClass()
        localBarCode = input['barcode'];
        localValvePar = input['valvePar'];
        localDateTime = input['datetime'];
        javaInstance = jd.encoding(localBarCode, localValvePar, localDateTime);
        returnBinCode = {"returnBinCode":str(javaInstance)}
        #jpype.shutdownJVM()
        return returnBinCode

    def funcDecoding(self, input):
        jvmPath = jpype.getDefaultJVMPath()
        jarpath = os.path.join(os.path.abspath('./PkgHstSpecial'), '')
        if not jpype.isJVMStarted():
            jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'ReadMeterData.jar'))
        javaClass = jpype.JClass('com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces')
        jd = javaClass()
        #inputData = "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"
        localInputBinCode = str(input['inputBinCode']);
        javaInstance = jd.decoding(localInputBinCode);
        returnBinCode = {"returnStringCode":str(javaInstance)}
        #jpype.shutdownJVM()
        return returnBinCode
                
    def cmdHandleProcedure(self, input, flag):
        if (flag == "encoding"):
            return self.funcEncoding(input)
        elif (flag == "decoding"):
            return self.funcDecoding(input)
        else:
            return False


# class ClassModSpecialGtjyWaterMeterEncode(object):
#     '''
#     classdocs
#     '''
# 
# 
#     def __init__(self):
#         '''
#         Constructor
#         '''
#     
# 
#     def cmdHandleProcedure(self, input):
#         jvmPath = jpype.getDefaultJVMPath()
#         #print(jvmPath)
# #         jpype.startJVM(jvmPath)
# #         jpype.java.lang.System.out.println("hello world!")
# #         jpype.java.lang.System.out.println("I hate you!")
# #         jpype.shutdownJVM()
#         #
#         #jarpath = os.path.join(os.path.abspath('.'), 'PkgHstSpecial/')
#         #
#         jarpath = os.path.join(os.path.abspath('.'), '')
#         #print(jarpath)
#         #
#         if not jpype.isJVMStarted():
#             jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'ReadMeterData-0.0.1-SNAPSHOT.jar'))
#         #
#         javaClass = jpype.JClass('com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces')
#         jd = javaClass()
#         #
#         #inputData = "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"
#         localBarCode = input['barcode'];
#         localValvePar = input['valvePar'];
#         localDateTime = input['datetime'];
#         javaInstance = jd.encoding(localBarCode, localValvePar, localDateTime);
#         #jpype.shutdownJVM()
#             
#         #Return back
#         return javaInstance
#         pass
# 
# class ClassModSpecialGtjyWaterMeterDecode(object):
#     '''
#     classdocs
#     '''
# 
# 
#     def __init__(self):
#         '''
#         Constructor
#         '''
# 
#     def cmdHandleProcedure(self, input):
#         jvmPath = jpype.getDefaultJVMPath()
#         #print(jvmPath)
# #         jpype.startJVM(jvmPath)
# #         jpype.java.lang.System.out.println("hello world!")
# #         jpype.java.lang.System.out.println("I hate you!")
# #         jpype.shutdownJVM()
#         #
#         #jarpath = os.path.join(os.path.abspath('.'), 'PkgHstSpecial/')
#         #
#         jarpath = os.path.join(os.path.abspath('.'), '')
#         #print(jarpath)
#         #
#         if not jpype.isJVMStarted():
#             jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath + 'ReadMeterData-0.0.1-SNAPSHOT.jar'))
#         #
#         javaClass = jpype.JClass('com.chnsce.zxmeter.impl.ZXNBITOMeterInterfaces')
#         jd = javaClass()
#         #
#         #inputData = "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"
#         localInputBinCode = str(input['inputBinCode']);
#         javaInstance = jd.decoding(localInputBinCode);
#         #jpype.shutdownJVM()
#             
#         #Return back
#         return javaInstance
#         pass





