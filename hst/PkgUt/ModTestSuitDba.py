'''
Created on 2017年12月12日

@author: hitpony
'''
import unittest
import time
import django
import sys
import os

sys.path.append('../../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
django.setup()
from django.db import transaction
from DappDbCebs import views as DappDbCebs

from DappDbCebs import models

from PkgUt import ModTestSuitComFunc

def hst_testsuite_dba():
    suiteTest = unittest.TestSuite()
    Flag=False
    if (Flag == True):
        suiteTest.addTest(ClassUtDba("tc_dba_test_001"))
        suiteTest.addTest(ClassUtDba("tc_dba_com_001")) #UserGroup add
        suiteTest.addTest(ClassUtDba("tc_dba_com_002")) #UserGroup del
        suiteTest.addTest(ClassUtDba("tc_dba_com_001")) #UserGroup add
        suiteTest.addTest(ClassUtDba("tc_dba_com_003")) #UserGroup modify

    #性能评估：如果设置为1，表示只跑一次，相当于普通的功能验证。设置为100就是跑100次
    Flag=False
    if (Flag == True):
        PerformanceMax = 1;
        ticks = time.time();
        print("Test Start, index = %d, time = %f" % (0, ticks));
        for i in range(1, PerformanceMax):
            suiteTest.addTest(ClassUtDba("tc_dba_cebs_001")) #CustomerMission add
            suiteTest.addTest(ClassUtDba("tc_dba_cebs_002")) #CustomerMission del
            suiteTest.addTest(ClassUtDba("tc_dba_cebs_001")) #CustomerMission add
            suiteTest.addTest(ClassUtDba("tc_dba_cebs_003")) #CustomerMission modify
            ticks = time.time();
            print("Test Start, index = %d, time = %f" % (i, ticks));    
    
    #继续普通测试
    Flag=True
    if (Flag == True):
        #suiteTest.addTest(ClassUtDba("tc_dba_cebs_001"))
        #suiteTest.addTest(ClassUtDba("tc_dba_cebs_002"))
        #suiteTest.addTest(ClassUtDba("tc_dba_cebs_003"))
        #suiteTest.addTest(ClassUtDba("tc_dba_cebs_004"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_005"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_006"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_007"))
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_002")) #CustomerMission del
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_001")) #CustomerMission add
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_003")) #CustomerMission modify
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_004")) #CustomerMission inqury
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_005")) #ClassifyExecLog add
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_006")) #ClassifyExecLog del
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_005")) #ClassifyExecLog add
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_007")) #ClassifyExecLog modify
#         suiteTest.addTest(ClassUtDba("tc_dba_cebs_008")) #ClassifyExecLog inqury
        print ("hst_suite_printer 运行")
    
    #继续普通测试
    Flag=False
    if (Flag == True):
        suiteTest.addTest(ClassUtDba("tc_dba_faam_001")) #CustomerMission add
    
    return suiteTest
    pass

#测试集合
class ClassUtDba(unittest.TestCase):
    #DJANGO TEST DB part
    def tc_dba_test_001(self):
        ticks = time.time();
        print("tc_dba_test_001, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0x1001,"parFlag": 1,"parContent":\
            {"user": "test999","pwd": "abcdef"}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   

    #COM DB part
    #UserGroup add
    def tc_dba_com_001(self):
        ticks = time.time();
        print("tc_dba_com_001, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0x1002,"parFlag": 1,"parContent": \
            {"cmd":"add", "caption":"test222", "ctime":"1234", "uptime":"5678", "userId":123}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   

    #UserGroup delete
    def tc_dba_com_002(self):
        ticks = time.time();
        print("tc_dba_com_002, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0x1002,"parFlag": 1,"parContent": \
            {"cmd":"delete", "userId":123}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
    
    #UserGroup modify
    def tc_dba_com_003(self):
        ticks = time.time();
        print("tc_dba_com_003, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0x1002,"parFlag": 1,"parContent": \
            {"cmd":"modify_by_userid", "caption":"test111", "ctime":"2018-02-20 06:58:55.840896", "uptime":"2018-02-20 06:58:55.840896", "userId":123}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   


    #CEBS DB part
    #add
    def tc_dba_cebs_001(self):
        ticks = time.time();
        
        print("tc_dba_cebs_001, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent":{'cmd':'add', 'uid':250, 'login_name':'admin', 'pass_word':'13456', 'grade_level':1,'email':'13525@.com', 'memo':'this'}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        print("tc_dba_cebs_001 result = ", result);
    
   
    #read
    def tc_dba_cebs_002(self):
        ticks = time.time();
        print("tc_dba_cebs_001, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"read", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        print("tc_dba_cebs_001 result = ", result);
    
    #modify
    def tc_dba_cebs_003(self):
        ticks = time.time();
        print("tc_dba_cebs_003, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"modify", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        print("tc_dba_cebs_003 result = ", result);

        #delete
    def tc_dba_cebs_004(self):
        ticks = time.time();
        print("tc_dba_cebs_004, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"delete", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        print("tc_dba_cebs_004 result = ", result);


        

    def tc_dba_cebs_005(self):
        ticks = time.time();

        print("tc_dba_cebs_005, time in second = ", ticks);
        uid=models.t_cebs_user_sheet.objects.all().last().uid

        #jsonInputData = {"restTag": "dba","actionId": 0X0ED9,"parFlag": 7,"parContent": {"cmd": "add", "platetype": 1, "uid": "UID3982146", "left_bot_x": 9, "left_bot_y": 9, "right_up_x": 9, "right_up_y": 9}}
        jsonInputData = {"restTag": "dba","actionId": 0X0ED9,"parFlag": 7,'parContent': {'cmd': 'add', 'platetype': 1, 'left_bot_x': 19, 'left_bot_y': 19, 'right_up_x': 19, 'right_up_y': 19}}
        jsonInputData['parContent'].update({"uid": uid})

        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        print(models.t_cebs_cali_profile.objects.all().last().id)
        newId=models.t_cebs_cali_profile.objects.all().last().id
      
        jsonInputData1 ='{"restTag": "dba","actionId": 3801,"parFlag": 1,"parContent" : {"cmd": "read", "id":'+str(newId)+'}}'
        #print(jsonInputData)
        result=ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData1, 1)
        subdict=result['parContent']
        testResult='OK'
        for item in subdict:
            if item!="calitime":
                if subdict[item]!=jsonInputData['parContent'][item]:
                    testResult='NOK'
                    print("Table Field : "+item)
                    print("Test data "+ jsonInputData['parContent'][item] + " is not equal database data " + subdict[item])
                    break
        print("test tc_dba_cebs_005 result is "+testResult)



    def tc_dba_cebs_006(self):
        ticks = time.time();

        print("tc_dba_cebs_006, time in second = ", ticks);
        uid=models.t_cebs_user_sheet.objects.all().last().uid

        #jsonInputData = {"restTag": "dba","actionId": 0X0ED9,"parFlag": 7,"parContent": {"cmd": "add", "platetype": 1, "uid": "UID3982146", "left_bot_x": 9, "left_bot_y": 9, "right_up_x": 9, "right_up_y": 9}}
        jsonInputData = {"restTag": "dba","actionId": 0X0EDA,"parFlag": 7,'parContent': {'cmd':'add', 'objname':'xianchong','objtype':1, 'dir_origin':'/var/www/origin', 'dir_middle':'/var/www/middle', 'memo':'varcebs', 'defaultflag': 0}}
        jsonInputData['parContent'].update({"uid": uid})

        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        print(models.t_cebs_object_profile.objects.all().last().objid)
        newId=models.t_cebs_object_profile.objects.all().last().objid
      
        jsonInputData1 ='{"restTag": "dba","actionId": 3802,"parFlag": 1,"parContent" : {"cmd": "read", "objid":'+str(newId)+'}}'
        #print(jsonInputData)
        result=ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData1, 1)
        subdict=result['parContent']
        testResult='OK'
        for item in subdict:
            if subdict[item]!=jsonInputData['parContent'][item]:
                testResult='NOK'
                print("Table Field : "+item)
                print("Test data "+ jsonInputData['parContent'][item] + " is not equal database data " + subdict[item])
                break
        print("test tc_dba_cebs_006 result is "+testResult)


    def tc_dba_cebs_007(self):
        ticks = time.time();

        print("tc_dba_cebs_007, time in second = ", ticks);
        objid=models.t_cebs_object_profile.objects.all().last().objid

        #jsonInputData = {"restTag": "dba","actionId": 0X0ED9,"parFlag": 7,"parContent": {"cmd": "add", "platetype": 1, "uid": "UID3982146", "left_bot_x": 9, "left_bot_y": 9, "right_up_x": 9, "right_up_y": 9}}
        jsonInputData = {"restTag": "dba","actionId": 0X0EDB,"parFlag": 7,'parContent': {'cmd':'add', 'fixpoint':0, 'autovideo':0, 'autodist':0, 'addset':1, 'autocap':0, 'autoperiod':60, 'videotime':3, 'slimit':200,'smlimit':500, 'mblimit':2000, 'blimit':5000, 'accspeed':20, 'decspeed':20, 'movespeed':20, 'zero_spd':20, 'zero_dec':20, 'back_step':12800}}
        jsonInputData['parContent'].update({"objid": objid})

        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        print(models.t_cebs_config_eleg.objects.all().last().confid)
        newId=models.t_cebs_config_eleg.objects.all().last().confid
      
        jsonInputData1 ='{"restTag": "dba","actionId": 3803,"parFlag": 1,"parContent" : {"cmd": "read", "confid":'+str(newId)+'}}'
        #print(jsonInputData)
        result=ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData1, 1)
        subdict=result['parContent']
        testResult='OK'
        for item in subdict:
            if subdict[item]!=jsonInputData['parContent'][item]:
                testResult='NOK'
                print("Table Field : "+item)
                print("Test data "+ jsonInputData['parContent'][item] + " is not equal database data " + subdict[item])
                break
        print("test tc_dba_cebs_007 result is "+testResult)




















    
#     #ClassifyExecLog add
#     def tc_dba_cebs_005(self):
#         ticks = time.time();
#         print("tc_dba_cebs_005, time in second = ", ticks);
#         jsonInputData = {"restTag": "dba","actionId": 3801,"parFlag": 1,"parContent": \
#             {"cmd":"add", "user":"test222", "timeStampExec":"2018-02-20 06:58:55.840896", "pageLen":2, "pageWidth":3, "resTotal":3, "resTotalAlive":3, "resTotalDead":3, \
#             "resSmallAlive":3,  "resSmallDead":3,  "resMidAlive":3,  "resMidDead":3,  "resBigAlive":3,  "resBigDead":3,  "resUnclassifyAlive":3,  "resUnclassifyDead":3}}
#         ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
#             
#     #ClassifyExecLog delete
#     def tc_dba_cebs_006(self):
#         ticks = time.time();
#         print("tc_dba_cebs_006, time in second = ", ticks);
#         jsonInputData = {"restTag": "dba","actionId": 0x1005,"parFlag": 1,"parContent": \
#             {"cmd":"delete", "user":"test222"}}
#         ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
#         pass
#     
#     #ClassifyExecLog modify
#     def tc_dba_cebs_007(self):
#         ticks = time.time();
#         print("tc_dba_cebs_007, time in second = ", ticks);
#         jsonInputData = {"restTag": "dba","actionId": 0x1005,"parFlag": 1,"parContent": \
#             {"cmd":"modify_by_user", "user":"test222", "timeStampExec":"2018-02-20 06:58:55.840896", "pageLen":3, "pageWidth":4, "resTotal":4, "resTotalAlive":4, "resTotalDead":4, \
#             "resSmallAlive":4,  "resSmallDead":4,  "resMidAlive":4,  "resMidDead":4,  "resBigAlive":4,  "resBigDead":4,  "resUnclassifyAlive":4,  "resUnclassifyDead":4}}
#         ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
#         pass
#     
#     #ClassifyExecLog inqury
#     def tc_dba_cebs_008(self):
#         ticks = time.time();
#         print("tc_dba_cebs_008, time in second = ", ticks);
#         result = jsonInputData = {"restTag": "dba","actionId": 0x1005,"parFlag": 1,"parContent": \
#             {"cmd":"inqury", "user":"test222"}}
#         print("tc_dba_cebs_008 inqury ClassifyExecLog = ", result);
#         ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 0)   
#         pass
    

    #FAAM DB part
    #CustomerMission add
    def tc_dba_faam_001(self):
        ticks = time.time();
        print("tc_dba_faam_001, time in second = ", ticks);
        jsonInputData = {"restTag": "dba", "actionId": 4128, "parFlag": 1, "parContent":{"cmd":"add", "caption": "TEST111", "ctime": "12345", "uptime": "12131414", "userId": "111"}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        pass


        
if __name__ == "__main__":
    test_case_class=ClassUtDba()
    test_case_class.tc_dba_cebs_001()
    