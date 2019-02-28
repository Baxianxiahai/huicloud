'''
Created on 2019年2月28日

@author: Administrator
'''

from ctypes import c_uint8
import random
import sys
import time
import json
import os   #Python的标准库中的os模块包含普遍的操作系统功能  
import re   #引入正则表达式对象  


class ClassModMplayerVrglsCtrl(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, input):
        if ('cmdId' not in input):
            return False
        if (input['cmdId'] == 'PlayRadio'):
            pass
        elif (input['cmdId'] == 'OpenSunroof'):
            pass
        elif (input['cmdId'] == 'CloseSunroof'):
            pass
        elif (input['cmdId'] == 'OpenWindowOnDriverSide'):
            pass
        elif (input['cmdId'] == 'OpenWindowOnPassengerSide'):
            pass
        elif (input['cmdId'] == 'CloseWindowOnDriverSide'):
            pass
        elif (input['cmdId'] == 'CloseWindowOnPassengerSide'):
            pass
        elif (input['cmdId'] == 'AutoAcOn'):
            pass
        elif (input['cmdId'] == 'AutoAcOff'):
            pass
        elif (input['cmdId'] == 'HighestFanSpeed'):
            pass
        elif (input['cmdId'] == 'LowestFanSpeed'):
            pass
        elif (input['cmdId'] == 'PlayGenre'):
            if ('music' not in input):
                return False
        elif (input['cmdId'] == 'PlayFavoriteSong'):
            pass
        elif (input['cmdId'] == 'PlayArtist'):
            if ('name' not in input):
                return False
        elif (input['cmdId'] == 'PlaySong'):
            if ('music' in input) and ('name' in input):
                pass
            if ('music' in input) and ('name' not in input):
                pass
        else:
            return False
        return True
    

class ClassModMplayerVrglsData(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, input):
        return True
















    