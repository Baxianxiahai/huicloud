'''
Created on 2017年12月12日

@author: hitpony
'''
import unittest
from PkgUt import ModTestSuitPrinter, ModTestSuitDba, ModTestSuitVision, ModTestSuitAiwgt, ModTestSuitSensor, ModTestSuitSpecial, ModTestSuitMdc,ModTestSuitCeworm

#包含所有的Suite
def hst_all_testsuite():
    allTest = unittest.TestSuite((
        ModTestSuitDba.hst_testsuite_dba(), 
#         ModTestSuitPrinter.hst_testsuite_printer(), 
#         ModTestSuitVision.hst_testsuite_vision(), 
#         ModTestSuitAiwgt.hst_testsuite_aiwgt(),
#         ModTestSuitSensor.hst_testsuite_sensor(),
#         ModTestSuitSpecial.hst_testsuite_special(),
#         ModTestSuitMdc.hst_testsuite_mdc(),
#         ModTestSuitCeworm.hst_testsuite_dba()
        ))
    return allTest

#LB ceworm video Ut
def hst_ceworm_testsuite():
    cewormTest=unittest.TestSuite((
        ModTestSuitCeworm.hst_testsuite_ceworm()
                                   ))
    return cewormTest
#运行的时候，可以根据不同的要求，运行不同的Suite,或者全部运行，这样就方便管理每次运行的case
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
#     runner.run(hst_all_testsuite())
    runner.run(hst_ceworm_testsuite())
    
    
    
    
    
    
    
    