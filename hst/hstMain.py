#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
 
import random
import sys
import time
import json
import os  # Python
import re   
import urllib
import http
import socket
from http.server import HTTPServer
from PkgAccessEntry import ModAccessHttpHandler

 
# MAIN SERVICE FUNCTIONS
def hst_start_server(addr, port):
    mySvrConn = HTTPServer(addr, ModAccessHttpHandler.ClassHttpRequestGenernalHandler)
    print("[", time.asctime(), "HUIREST]: Server Starts - %s:%s" % addr)
    try:
        mySvrConn.recSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM  #SOCK_DGRAM
        mySvrConn.recSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_STREAM  #SOCK_DGRAM
        mySvrConn.recSocket.settimeout(200)
        mySvrConn.recSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#         mySvrConn.recSocket.bind(('', 7999))
        mySvrConn.serve_forever()
    except KeyboardInterrupt as e:
        print("Exit = ", e)
    mySvrConn.server_close()
    print("[", time.asctime(), "HUIREST]: Server Stops - %s:%s" % addr)

 
def main():
    HST_HOST_NAME = "0.0.0.0"
    HST_HOST_PORT = 7999
    zHstAddrBind = (HST_HOST_NAME, HST_HOST_PORT)
    hst_start_server(zHstAddrBind, HST_HOST_PORT)


if __name__ == '__main__':
    main()
