'''
Created on 2017年12月27日

@author: hitpony
'''

import unittest
import time

def hst_testsuite_aiwgt():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtAiwgt("tc_aiwgt_001"))
    #print ("hst_suite_printer 运行")
    return suiteTest

#测试集合
class ClassUtAiwgt(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def tc_aiwgt_001(self):
        ticks = time.time();
        print("tc_aiwgt_001, time in second = ", ticks);
        pass






# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()
#     




