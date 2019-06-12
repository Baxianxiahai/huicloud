'''
Created on 2017年12月12日

@author: hitpony
'''
import pycurl
import urllib
import json
import time
import urllib3
import requests
import socket

class ClassJoinContents:
    def __init__(self):
        self.contents = ''
    def callback(self,curl):
        self.contents = self.contents + curl.decode('utf-8')

#以curl为方式的client连接 - 暂时未用 - 使用pycurl的方式，应该是可信的
def hst_curl_client_connection():
    t = ClassJoinContents()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, t.callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL, "http://localhost:7999")
    c.setopt(pycurl.FORBID_REUSE, 0)
    #self.recSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)      
    c.perform()
    NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)
    CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)
    PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    HTTP_CODE =  c.getinfo(c.HTTP_CODE)
    SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
    print("HTTP状态码：%s" %(HTTP_CODE))
    print("DNS解析时间：%.2f ms"%(NAMELOOKUP_TIME*1000))
    print("建立连接时间：%.2f ms" %(CONNECT_TIME*1000))
    print("准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000))
    print("传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000))
    print("传输结束总时间：%.2f ms" %(TOTAL_TIME*1000))
    print("下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
    print("HTTP头部大小：%d byte" %(HEADER_SIZE))
    print("平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD))
    c.close()

#以curlib3为方式的client连接 - 主要应用模式
def hst_curlib3_client_connection(jsonInputData, logic):
        encoded_data = json.dumps(jsonInputData).encode('utf-8')
        http = urllib3.PoolManager(maxsize=10, timeout=30.0, block=True)
        r = http.request(
            'POST',
            'http://localhost:7999/post',
            body=encoded_data, 
            headers={'Content-Type':'application/json', 'Connection': 'close'}
            )
        # print("r data")
        # print(r.data)
        # result=''
        try:
            result = json.loads(r.data)
            # print(result)
        except Exception:
            print("Test case run error without feedback!")
            result = ''
        #ptr.assertEqual(result['parContent']['sucFlag'], logic, 'Result Failure')
        return result

#带校验的工作模式
def hst_curlib3_client_conn_check_details(ptr, jsonInputData, logic):
        encoded_data = json.dumps(jsonInputData).encode('utf-8')
        http = urllib3.PoolManager(maxsize=10, block=True)
        r = http.request(
            'POST',
            'http://localhost:7999/post',
            body=encoded_data,
            headers={'Content-Type':'application/json'})
        result = json.loads(r.data)
        ptr.assertEqual(result['parFlag'], logic, 'Result Failure')
        #return result['parContent']
        return result


#废弃
# class ClassComFunc:
#     def __init__(self):
#         pass
# 
#     def hst_curlib3_client_connection(self, jsonInputData, logic):
#             encoded_data = json.dumps(jsonInputData).encode('utf-8')
#             http = urllib3.PoolManager(maxsize=10, timeout=30.0)
#             r = http.request('POST', 'http://localhost:7999/post', body = encoded_data)
#             #r = http.request(\
#             #    'POST',\
#             #    'http://localhost:7999/post',\
#             #    body = encoded_data)
#                 #headers={'Content-Type':'application/json', 'Connection': 'close'}
#                 #headers={'Content-Type':'application/json'}, 
#                 #)
#             print(r)
#             result = json.loads(r.data)
#             #ptr.assertEqual(result['parContent']['sucFlag'], logic, 'Result Failure')
#             return result    
#         
#     def hst_socket_test(self, msg):
#         client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
#         client.connect(('127.0.0.1', 7999))
#         #while True:
#         #msg = input(">>>").strip()
#         if len(msg) ==0:
#             return True
#         #client.send(msg.encode("utf-8"))
#         client.send(json.dumps(msg).encode('utf-8'))
#         data = client.recv(1024)#这里是字节1k
#         print("recv:>", data.decode())
#         client.close()
#         return True




