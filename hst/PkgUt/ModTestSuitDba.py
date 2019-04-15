'''
Created on 2017年12月12日

@author: hitpony
'''
import unittest
import time
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
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_001"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_002"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_003"))
        suiteTest.addTest(ClassUtDba("tc_dba_cebs_004"))
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
    
    #delete
    def tc_dba_cebs_002(self):
        ticks = time.time();
        print("tc_dba_cebs_002, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"delete", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        print("tc_dba_cebs_002 result = ", result);
    
    #read
    def tc_dba_cebs_003(self):
        ticks = time.time();
        print("tc_dba_cebs_003, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"read", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        print("tc_dba_cebs_003 result = ", result);
    
    #modify
    def tc_dba_cebs_004(self):
        ticks = time.time();
        print("tc_dba_cebs_004, time in second = ", ticks);
        jsonInputData = {"restTag": "dba","actionId": 0X0ED7,"parFlag": 1,"parContent": \
            {"cmd":"modify", "user":"test222"}}
        result = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   
        print("tc_dba_cebs_004 result = ", result);



























    
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


        
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
#     
    