'''
Created on 2018年12月5日

@author: Administrator
'''

import unittest
import time
from PkgUt import ModTestSuitComFunc

def hst_testsuite_mdc():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtMdc("tc_mdc_001"))
    #suiteTest.addTest(ClassUtMdc("tc_mdc_002"))
    #print ("hst_testsuite_mdc 运行")
    return suiteTest

#测试集合
class ClassUtMdc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def tc_mdc_001(self):
        ticks = time.time();
        print("tc_mdc_001, time in second = ", ticks);        
        a = 3
        b = 2
        self.assertEqual(a+b, 5,'Result Fail')