'''
Created on 2017年12月12日

@author: hitpony
'''
import unittest
import time
from PkgUt import ModTestSuitComFunc

def hst_testsuite_vision():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtVision("tc_vision_001"))
    suiteTest.addTest(ClassUtVision("tc_vision_002"))
    suiteTest.addTest(ClassUtVision("tc_vision_003"))
    suiteTest.addTest(ClassUtVision("tc_vision_004"))
    suiteTest.addTest(ClassUtVision("tc_vision_005"))
    #suiteTest.addTest(ClassUtVision("tc_vision_006"))
    #suiteTest.addTest(ClassUtVision("tc_vision_007"))
    #suiteTest.addTest(ClassUtVision("tc_vision_008"))
    #suiteTest.addTest(ClassUtVision("tc_vision_009"))
    print ("hst_testsuite_vision 运行")
    return suiteTest

#测试集合
class ClassUtVision(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass

    def tc_vision_001(self):
        ticks = time.time();
        print("tc_vision_001, time in second = ", ticks);        
        a = 3
        b = 2
        self.assertEqual(a+b, 5,'Result Fail')

    def tc_vision_002(self):
        ticks = time.time();
        print("tc_vision_002, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10001,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 0)

    def tc_vision_003(self):
        ticks = time.time();
        print("tc_vision_003, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10002,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)

    def tc_vision_004(self):
        ticks = time.time();
        print("tc_vision_004, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10003,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)        
    
    #测试__HUIREST_ACTIONID_VISION_worm_clasify_single的正常情况
    def tc_vision_005(self):
        ticks = time.time();
        print("tc_vision_005, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10004,"parFlag": 1,"parContent": {"fileName":"11.JPG", "cfBase":600, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":5000}}
        res = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)
        try:
            totalNbr = res['totalNbr']
        except Exception:
            totalNbr = 0
        if (totalNbr) > 0:
            print("tc_vision_005: Total classified number = ", totalNbr)
        else:
            print("tc_vision_005: Failure to fetch result")

    def tc_vision_006(self):
        ticks = time.time();
        print("tc_vision_006, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10004,"parFlag": 1,"parContent": {"fileName":"12.JPG", "cfBase":500, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":3500}}
        res = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)     
        if (res['totalNbr']) > 0:
            print("tc_vision_006: Total classified number = ", res['totalNbr'])
        else:
            print("tc_vision_006: Failure to fetch result")

    def tc_vision_007(self):
        ticks = time.time();
        print("tc_vision_007, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10004,"parFlag": 1,"parContent": {"fileName":"3.JPG", "cfBase":500, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":3500}}
        res = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)     
        if (res['totalNbr']) > 0:
            print("tc_vision_007: Total classified number = ", res['totalNbr'])
        else:
            print("tc_vision_007: Failure to fetch result")

    def tc_vision_008(self):
        ticks = time.time();
        print("tc_vision_008, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10004,"parFlag": 1,"parContent": {"fileName":"4.JPG", "cfBase":500, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":3500}}
        res = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)     
        if (res['totalNbr']) > 0:
            print("tc_vision_008: Total classified number = ", res['totalNbr'])
        else:
            print("tc_vision_008: Failure to fetch result")

    def tc_vision_009(self):
        ticks = time.time();
        print("tc_vision_009, time in second = ", ticks);
        jsonInputData = {"restTag": "vision","actionId": 10004,"parFlag": 1,"parContent": {"fileName":"5.JPG", "cfBase":500, "cfSmall2MidIndex":1500, "cfMid2BigIndex":2500, "cfBig2TopIndex":3500}}
        res = ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)     
        if (res['totalNbr']) > 0:
            print("tc_vision_009: Total classified number = ", res['totalNbr'])
        else:
            print("tc_vision_009: Failure to fetch result")








# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
    
    
    
    