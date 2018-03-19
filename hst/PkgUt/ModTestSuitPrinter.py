'''
Created on 2017年12月12日

@author: hitpony
'''
import unittest
import time
from PkgUt import ModTestSuitComFunc


def hst_testsuite_printer():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(ClassUtPrinter("tc_printer_001"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_002"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_003"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_004"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_005"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_006"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_007"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_007"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_008"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_009"))
    suiteTest.addTest(ClassUtPrinter("tc_printer_010"))    
    suiteTest.addTest(ClassUtPrinter("tc_printer_011"))
    #print ("hst_testsuite_printer 运行")
    return suiteTest

#测试集合
class ClassUtPrinter(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def tc_printer_001(self):
        ticks = time.time();
        print("tc_printer_001, time in second = ", ticks);
        a = 3
        b = 2
        self.assertEqual(a+b, 5,'Result Fail')

    def tc_printer_002(self):
        ticks = time.time();
        print("tc_printer_002, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 255,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 0)

    def tc_printer_003(self):
        ticks = time.time();
        print("tc_printer_003, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 256,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 1)

    def tc_printer_004(self):
        ticks = time.time();
        print("tc_printer_004, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 257,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 1)        

    def tc_printer_005(self):
        ticks = time.time();
        print("tc_printer_005, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 258,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 1)        

    def tc_printer_006(self):
        ticks = time.time();
        print("tc_printer_006, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 262,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 0)     

    def tc_printer_007(self):
        ticks = time.time();
        print("tc_printer_007, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 263,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 0)    

    def tc_printer_008(self):
        ticks = time.time();
        print("tc_printer_008, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 264,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 0)   

    def tc_printer_009(self):
        ticks = time.time();
        print("tc_printer_009, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 256,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 1)   
        
    def tc_printer_010(self):
        ticks = time.time();
        print("tc_printer_010, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 256,"parFlag": 2,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 0)   
 
    #这里的标志位，检查的不够
    def tc_printer_011(self):
        ticks = time.time();
        print("tc_printer_011, time in second = ", ticks);
        jsonInputData = {"restTag": "printer","actionId": 256,"parFlag": 0,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData, 1)    

        
#         pararms = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
#         headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#         conn = http.client.HTTPConnection("localhost:8000")
#         conn.request('POST', '', pararms, headers)
#         response = conn.getresponse()
#         print(response.status, response.reason)
#         data = response.read()
#         print(data)
#         conn.close()        

        #发起请求的url
#         post_url = 'http://localhost:8000';
#         postData  = {'a':'aaa','b':'bbb','c':'ccc','d':'ddd'}
#         #json序列化
#         data = json.dumps(postData)
#         req = urllib.request(post_url)
#         response = urllib.parse(req, urllib.response({'sku_info':data}))
#         #打印返回值
#         print (response)

#         post_url = 'http://localhost:8000';
#         data = urllib.request.urlopen(post_url).read()
#         data = data.decode('UTF-8')
#         print(data)
        
        #ModTestSuitComFunc.hst_curl_connection()
        
        
#         data = urllib.parse.urlencode(\
# {\
#     "restTag": "vision",\
#     "actionId": 8193,\
#     "parFlag": 1,\
#     "parContent": {\
#         "sn": 55,\
#         "sucFlag": 1,\
#         "errCode": 0\
#     }\
# })
#         data = data.encode('utf-8')
# 
#         request = urllib.request.Request("http://localhost:8000")
#         request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
#         f = urllib.request.urlopen(request, data)
#         print(f.read().decode('utf-8'))
# 
#         with urllib.request.urlopen("http://localhost:8000", data) as f:
#             print(f.read().decode('utf-8'))


#         http = urllib3.PoolManager(maxsize=10, block=True)
#         jsonData = {"restTag": "vision","actionId": 8193,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
#         encoded_args = urllib.parse.urlencode(jsonData)
#         print(encoded_args)
#         url = 'http://localhost:8000/post?' + encoded_args
#         #jsonData = {'hello':'world'}
#         #inputFields = json.dumps(jsonData)
#         #print(inputFields)
#         #r = http.request('POST','http://httpbin.org/post', fields = inputFields)
#         r = http.request('POST', url)
#         print(r.data)


#        jsonInputData = {"restTag": "vision","actionId": 8192,"parFlag": 1,"parContent": {"sn": 55,"sucFlag": 1,"errCode": 0}}
#         encoded_data = json.dumps(jsonInputData).encode('utf-8')
#         http = urllib3.PoolManager(maxsize=10, block=True)
#         r = http.request(
#             'POST',
#             'http://localhost:8000/post',
#             body=encoded_data,
#             headers={'Content-Type': 'application/json'})
#         result = json.loads(r.data)
#         self.assertEqual(result['parContent']['sucFlag'], 1, 'Result Failure')
#         pass
#        ModTestSuitComFunc.hst_curlib3_client_connection(self, jsonInputData)


# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()







    