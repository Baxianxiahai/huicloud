# -*- coding: UTF-8 -*-
'''
Created on 2019年6月9日

@author: Administrator
'''

import unittest
import time
from PkgUt import ModTestSuitComFunc


def hst_testsuite_ceworm():
    suiteTest = unittest.TestSuite()
    #性能评估：如果设置为1，表示只跑一次，相当于普通的功能验证。设置为100就是跑100次
#     Flag=True
#     if (Flag == True):
    PerformanceMax = 1;
    ticks = time.time();
    print("Test Start, index = %d, time = %f" % (0, ticks));
    for i in range(0, PerformanceMax):
        suiteTest.addTest(ClassUtCeworm("tc_ceworm_test_001")) #CustomerMission add
        ticks = time.time();
        print("Test Start, index = %d, time = %f" % (i, ticks));
    return suiteTest


class ClassUtCeworm(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def tc_ceworm_test_001(self):
        ticks = time.time();
        print("tc_dba_test_001, time in second = ", ticks);
        jsonInputData = {
            "restTag": "ceworm","actionId": 27000,"parFlag": 1,
            "parContent":{'cmd':"non_real_field",'data':{"file_name":'d:\\Video\\A1.mp4'}}}
        ModTestSuitComFunc.hst_curlib3_client_connection(jsonInputData, 1)   