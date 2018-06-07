'''
Created on 2017年12月11日

@author: hitpony
'''

import uuid

class ClassPrinterCallcellBfdf:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, input):
        return True

class ClassPrinterCallcellBfhs:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def cmdHandleProcedure(self, input):
        return True
    
class ClassPrinterCallcellBfsc:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def cmdHandleProcedure(self, input):
        return True
    
class ClassPrinterFaam:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def func_get_local_mac_addr(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
        macString = ":".join([mac[e:e+2] for e in range(0,11,2)])        
        jsonRes = {"mac": macString}
        print(jsonRes)
        return jsonRes
            
    def func_get_local_cpuid(self):
        jsonRes = {"cpuid": "1234565423424"}
        print(jsonRes)
        return jsonRes

    def cmdHandleProcedure(self, input):
        if (("cmd" in input) == False):
            print("MODPRINTERGENERAL: Receiving data error!")
            return False
        if (input['cmd'] == 'get_mac'):
            return self.func_get_local_mac_addr()
        elif (input['cmd'] == 'get_cpuid'):
            return self.func_get_local_cpuid()
        else:
            return False        
        
   