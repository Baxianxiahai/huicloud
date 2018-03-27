'''
Created on 2017骞�12鏈�11鏃�

@author: hitpony
'''

from ctypes import c_uint8
import sys
import time
import json
import os   #
import re   #

#Django
import django
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbTest import views as DappDbTest_views
from DappDbComm import views as DappDbComm_views
from DappDbCebs import views as DappDbCebs_views
from DappDbBfdf import views as DappDbBfdf_views
from DappDbBfhs import views as DappDbBfhs_views
from DappDbBfhs import views as DappDbCcl_views
from DappDbBfhs import views as DappDbFaam_views

#CLASS
class ClassDbaTempUpdate:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def cmdHandleProcedure(self, input):
        return True
        

class ClassDbaDjangoTest:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    #
    def func_dba_django_test1(self, par):
        #print("par = ", par);
        DappDbTest_views.user_info_add(par)
        pass
            
    def cmdHandleProcedure(self, input):
        #print("input = ", input);
        self.func_dba_django_test1(input)
        return True
    
class ClassDbaCommUserGroup:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_comm_user_group_add(self, par):
        DappDbComm_views.UserGroup_add(par)
        pass

    def func_dba_comm_user_group_delete(self, par):
        DappDbComm_views.UserGroup_delete(par)
        pass

    def func_dba_comm_user_group_modify_by_userid(self, par):
        DappDbComm_views.UserGroup_modify_by_userId(par)
        pass
                
    def cmdHandleProcedure(self, input):
        if (("cmd" in input) == False):
            print("MODDBAGENERAL: Receiving data error!")
            return False
        if (input['cmd'] == 'add'):
            self.func_dba_comm_user_group_add(input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_comm_user_group_delete(input)
            return True    
        elif (input['cmd'] == 'modify_by_userid'):
            self.func_dba_comm_user_group_modify_by_userid(input)
            return True    
        else:
            return False
    
class ClassDbaCommUserAccount:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_comm_user_account_add(self, par):
        pass
            
    def cmdHandleProcedure(self, input):
        #print("input = ", input);
        self.func_dba_comm_user_account_add(input)
        return True

#瀹㈡埛琛ㄥ崟       
class ClassDbaCebsCustomerMission:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_cebs_customer_mission_add(self, par):
        DappDbCebs_views.CustomerMission_add(par)
        pass

    def func_dba_cebs_customer_mission_delete(self, par):
        DappDbCebs_views.CustomerMission_delete(par)
        pass

    def func_dba_cebs_customer_mission_modify_by_user(self, par):
        DappDbCebs_views.CustomerMission_modify_by_user(par)
        pass

    def func_dba_cebs_customer_mission_inqury(self, par):
        return DappDbCebs_views.CustomerMission_inqury(par)
        pass
                
    def cmdHandleProcedure(self, input):
        if (("cmd" in input) == False):
            print("MODDBAGENERAL: Receiving data error!")
            return False
        if (input['cmd'] == 'add'):
            self.func_dba_cebs_customer_mission_add(input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_cebs_customer_mission_delete(input)
            return True    
        elif (input['cmd'] == 'modify_by_user'):
            self.func_dba_cebs_customer_mission_modify_by_user(input)
            return True    
        elif (input['cmd'] == 'inqury'):
            obj = self.func_dba_cebs_customer_mission_inqury(input)
            return obj
        else:
            return False

#浠诲姟鎵цLOG      
class ClassDbaCebsClassifyExecLog:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def func_dba_cebs_classify_exec_log_add(self, par):
        DappDbCebs_views.ClassifyExecLog_add(par)
        pass

    def func_dba_cebs_classify_exec_log_delete(self, par):
        DappDbCebs_views.ClassifyExecLog_delete(par)
        pass

    def func_dba_cebs_classify_exec_log_modify_by_user(self, par):
        DappDbCebs_views.ClassifyExecLog_modify_by_user(par)
        pass

    def func_dba_cebs_classify_exec_log_inqury(self, par):
        return DappDbCebs_views.ClassifyExecLog_inqury(par)
        pass
                
    def cmdHandleProcedure(self, input):
        if (("cmd" in input) == False):
            print("MODDBAGENERAL: Receiving data error!")
            return False
        if (input['cmd'] == 'add'):
            self.func_dba_cebs_classify_exec_log_add(input)
            return True    
        elif (input['cmd'] == 'delete'):
            self.func_dba_cebs_classify_exec_log_delete(input)
            return True    
        elif (input['cmd'] == 'modify_by_user'):
            self.func_dba_cebs_classify_exec_log_modify_by_user(input)
            return True    
        elif (input['cmd'] == 'inqury'):
            obj = self.func_dba_cebs_classify_exec_log_inqury(input)
            return obj
        else:
            return False





            
    
      