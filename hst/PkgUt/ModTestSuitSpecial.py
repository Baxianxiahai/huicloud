'''
Created on Mar 9, 2018

@author: hitpony
'''

import unittest
import time
from PkgUt import ModTestSuitComFunc


def hst_testsuite_special():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtSpecial("tc_special_001"))
    suiteTest.addTest(ClassUtSpecial("tc_special_002"))
    #suiteTest.addTest(ClassUtSpecial("tc_special_003"))
    #suiteTest.addTest(ClassUtSpecial("tc_special_004"))
    #suiteTest.addTest(ClassUtSpecial("tc_special_005"))
    #suiteTest.addTest(ClassUtSpecial("tc_special_006"))
    #suiteTest.addTest(ClassUtSpecial("tc_special_007"))
    #print ("hst_testsuite_special 运行")
    return suiteTest

#测试集合
class ClassUtSpecial(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    #No useful function
    def tc_special_001(self):
        ticks = time.time();
        print("tc_special_001, time in second = ", ticks);        
        a = 3
        b = 2
        self.assertEqual(a+b, 5,'Result Fail')

    #Pure test function
    def tc_special_002(self):
        ticks = time.time();
        print("tc_special_002, time in second = ", ticks);
        jsonInputData = {"restTag": "special", "actionId": 6000, "parFlag": 1, "parContent": {"barcode": "12345678", "valvePar": 1, "datetime": "20180314133829"}}
        res = ModTestSuitComFunc.hst_curlib3_client_conn_check_details(self, jsonInputData, 1)
        print("tc_special_002 result = ", res)

    #Encode function
    def tc_special_003(self):
        ticks = time.time();
        print("tc_special_003, time in second = ", ticks);
        jsonInputData = {"restTag": "special", "actionId": 6001, "parFlag": 1, "parContent": {"barcode": "12345678", "valvePar": 0, "datetime": "20180314133829"}}
        res = ModTestSuitComFunc.hst_curlib3_client_conn_check_details(self, jsonInputData, 1)
        print("tc_special_003 result = ", res)
        #RETURN = {'restTag': 'special', 'actionId': 20482, 'parFlag': 1, 'parContent': {'inputBinCode': 'AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB'}}
        
    #Decode function
    def tc_special_004(self):
        ticks = time.time();
        print("tc_special_004, time in second = ", ticks);
        jsonInputData = {"restTag": "special", "actionId": 6002, "parFlag": 1, "parContent": {"inputBinCode": "AA11C538326217CCA301092A0C0E1C1B7E2C01640000002C010000881300000000000024CC1000CC1000000000000100002100000000000000E803000001000D0B191B7E460111176309813D0D00F401C10341BB"}}
        #jsonInputData = {"restTag": "special", "actionId": 20482, "parFlag": 1, "parContent": {"inputBinCode": "FF113312345678003813140318200001000000000000000000000000000000000000000000000000000000000000F2BB"}}
        res = ModTestSuitComFunc.hst_curlib3_client_conn_check_details(self, jsonInputData, 1)
        print("tc_special_004 result = ", res)
        #RETRUN = {"restTag": "special", "actionId": 20482, "parFlag": 1, "parContent": "{\"GPRS\u7d2f\u8ba1\u5145\u503c\u91cf\":4300.0,\"\u7d2f\u8ba1\u9884\u8d2d\u91cf\":1000.0,\"\u5355\u4ef7\":3.0,\"\u4e0a\u4f20\u539f\u56e0\u6807\u5fd7\u4f4d\":\" \",\"\u7d2f\u79ef\u91cf\":1.0,\"\u8d1f\u8ba1\u91d1\u989d\":0.0,\"\u7a0b\u5e8f\u7248\u672c\u53f7\":\"v03C1\",\"\u62a5\u8b66\u6c14\u91cf\":62465,\"\u5269\u4f59\u91d1\u989d\":50.0,\"\u6700\u540e\u4e00\u6b21\u5145\u503c\u91cf\":4300.0,\"\u6b20\u538b\u65f6\u95f4\":\"2017-11-25 11:1300\",\"\u65f6\u95f4\":\"2017-11-28 14:12:42\",\"SIM\u5361\u53f7\":2068914947,\"\u4fe1\u53f7\u5f3a\u5ea6\":36,\"\u542f\u52a8\u65e5\u671f\":\"00-00\",\"\u8868\u7c7b\u578b\":\"CC\",\"\u7d2f\u8ba1\u91d1\u989d\":3.0,\"\u8868\u5185\u8fd0\u884c\u72b6\u6001\":\" \",\"\u7edf\u8ba1\u7d2f\u79ef\u91cf\":256,\"\u7edf\u8ba1\u65e5\u671f\":\"01-09\",\"\u7edf\u8ba1\u5468\u671f\":0.0,\"IC\u5361\u6700\u540e\u4e00\u6b21\u5145\u503c\u91cf\":0.0,\"\u8868\u53f7\":\"38326217\"}"}









   
        
        