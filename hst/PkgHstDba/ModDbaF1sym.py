# -*- coding: utf-8 -*-
'''
Created on 2018年6月30日

@author: Administrator
'''
import sys
import os
import django
import json
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbF1sym import views as DappDbF1sym
from django.db import transaction
class ClassDbaF1sym():
    def __init__(self):
        pass
    def dft_dbi_login_req(self,inputData):
        name=inputData['name']
        password=inputData['password']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_login_req(name, password)
                print(type(result))    
        except Exception:
            result={"body":{"key":"","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_userauthcode_process(self,inputData):
        username=inputData['name']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userauthcode_process(username)
                print(result)
        except Exception:
            result={"body":"","msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_reset_password_process(self,inputData):
        username=inputData['name']
        code=inputData['code']
        password=inputData['password']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_reset_password_process(username, code, password)
        except Exception:
            body={'key':"",'admin':""}
            result={"body":body,"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_session_check(self,inputData):
        session=inputData['sessionid']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_session_check(session)
                print(result)
        except Exception:
            result={"body":"","msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_user_authcheck(self,inputData):
        action=inputData['action']
        sessionid=inputData['sessionid']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_user_authcheck(action, sessionid)
                print(result)
        except Exception:
            result={"body":"","msg":"数据库发生错误，请重试"}
        return result
    def dft_user_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_new(inputData)
                print(result)
        except Exception:
            result={"body":{"key":"","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_userinfo_req(self,inputData):
        session=inputData['sessionid']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_req(session)
                print(result)
        except Exception:
            result={"body":{"key":"","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result