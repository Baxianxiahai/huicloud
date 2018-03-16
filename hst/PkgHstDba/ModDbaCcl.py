'''
Created on 2018/3/14

@author: Administrator
'''

#!/usr/bin/env python
#coding:utf-8

from ctypes import c_uint8
import sys
import time
import json
import os   #
import re   #

#Django
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
sys.path.append('../DjoSiteDba/')
#from DjoSiteDba.wsgi import *
django.setup()

from DappDbComm import views as DappDbComm_views
from DappDbBfhs import views as DappDbCcl_views


class ClassDbaCclWaterMeterOpr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_add(self, par):
        pass

    def func_dba_delete(self, par):
        pass

    def func_dba_modify_by_user(self, par):
        pass

    def func_dba_inqury(self, par):
        pass
                
    def cmdHandleProcedure(self, input):
        if (input['cmd'] == 'add'):
            self.func_dba_add(input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_delete(input)
            return True    
        elif (input['cmd'] == 'modify_by_user'):
            self.func_dba_modify_by_user(input)
            return True    
        elif (input['cmd'] == 'inqury'):
            obj = self.func_dba_inqury(input)
            return obj
        else:
            return False


class ClassDbaCclGasMeterOpr(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_add(self, par):
        pass

    def func_dba_delete(self, par):
        pass

    def func_dba_modify_by_user(self, par):
        pass

    def func_dba_inqury(self, par):
        pass
                
    def cmdHandleProcedure(self, input):
        if (input['cmd'] == 'add'):
            self.func_dba_add(self, input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_delete(self, input)
            return True    
        elif (input['cmd'] == 'modify_by_user'):
            self.func_dba_modify_by_user(self, input)
            return True    
        elif (input['cmd'] == 'inqury'):
            obj = self.func_dba_inqury(self, input)
            return obj
        else:
            return False


class ClassDbaCclPowerMeterOpr(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_add(self, par):
        pass

    def func_dba_delete(self, par):
        pass

    def func_dba_modify_by_user(self, par):
        pass

    def func_dba_inqury(self, par):
        pass
                
    def cmdHandleProcedure(self, input):
        if (input['cmd'] == 'add'):
            self.func_dba_add(self, input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_delete(self, input)
            return True    
        elif (input['cmd'] == 'modify_by_user'):
            self.func_dba_modify_by_user(self, input)
            return True    
        elif (input['cmd'] == 'inqury'):
            obj = self.func_dba_inqury(self, input)
            return obj
        else:
            return False




