'''
Created on Mar 9, 2018

@author: hitpony
'''

import unittest
import time
from PkgUt import ModTestSuitComFunc

def hst_testsuite_sensor():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtSensor("tc_sensor_001"))
    #suiteTest.addTest(ClassUtSensor("tc_sensor_002"))
    #print ("hst_testsuite_sensor 运行")
    return suiteTest

#测试集合
class ClassUtSensor(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def tc_sensor_001(self):
        ticks = time.time();
        print("tc_sensor_001, time in second = ", ticks);        
        a = 3
        b = 2
        self.assertEqual(a+b, 5,'Result Fail')
        
        
        
        
        