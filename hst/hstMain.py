'''
Created on 2017骞�12鏈�10鏃�

@author: hitpony
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os   #Python
import re   
import urllib
import http
import socket
#from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from PkgAccessEntry import ModAccessHttpHandler

def hst_start_server(addr, port):
    myServerConnection = HTTPServer(addr, ModAccessHttpHandler.ClassHttpRequestGenernalHandler)
    print("[", time.asctime(), "HUIREST]: Server Starts - %s:%s" % addr)
    try:
        #################
        #Following parameters set, is to solve socket connection 2nd time re-enter issue, but not confirm to solve really. To be study further.
        #Even put here, no impact our normal working
        #Under hstMain.py no reponse, we could use ps -fA | grep python, to kill -9 "python3 hstMain.py", then the socket combination could recover.
        myServerConnection.recSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        myServerConnection.recSocket.settimeout(200)
        myServerConnection.recSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        myServerConnection.recSocket.bind(('', port))
        ##################
        myServerConnection.serve_forever()
    except KeyboardInterrupt:
        pass
    myServerConnection.server_close()
    print("[", time.asctime(), "HUIREST]: Server Stops - %s:%s" % addr)


def main():
    HST_HOST_NAME = "localhost"
    HST_HOST_PORT = 8000
    zHstAddrBind = (HST_HOST_NAME, HST_HOST_PORT)
    hst_start_server(zHstAddrBind, HST_HOST_PORT)

if __name__ == '__main__':
    main()
