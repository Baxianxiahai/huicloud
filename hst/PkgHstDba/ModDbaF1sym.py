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
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
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
    def dft_dbi_userinfo_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_new(inputData['userinfo'])
                print(result)
        except Exception:
            result=''
        if result!='':
            result=True
        else:
            result=False
        return result
    def dft_dbi_userinfo_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_delete(inputData)
        except Exception:
            result=""
        if result!='':
            return True
        else:
            return False 
    def dft_dbi_usernum_inquery(self):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_usernum_inquery()
        except Exception:
            result=0
        return result
    def dft_dbi_userinfo_req(self,inputData):
        session=inputData['sessionid']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_req(session)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_usertable_req(self,inputData):
        uid=inputData['uid']
        keyword=inputData['keyword']
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_usertable_req(uid, keyword)
                print(result)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    def dft_dbi_userinfo_update(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                DappDbF1sym_view.dft_dbi_userinfo_update(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_dbi_test_response_msg(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                DappDbF1sym_view.dft_dbi_test_response_msg(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_dbi_HCU_Login_Binding(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_HCU_Login_Binding(inputData)
        except Exception:
            result={'status':"false",'auth':'true','ret':{},'msg':"数据库发生错误，请稍后"}
        return result