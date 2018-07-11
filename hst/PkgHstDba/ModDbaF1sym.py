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
from DappDbF11faam import views as DappDbF11faam
from django.db import transaction
class ClassDbaF1sym():
    def __init__(self):
        pass
    
    def dft_login_req(self,inputData):
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
    def dft_user_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1sym_view=DappDbF1sym.dct_classDbiL3apF1sym()
                result=DappDbF1sym_view.dft_dbi_userinfo_new(inputData)
                print(result)
        except Exception:
            result={"body":{"key":"","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
        
    def dft_login_req1(self,inputData):
        try:
            with transaction.atomic():
                result=DappDbF11faam.insert(inputData)
                result={'status':'true','auth':"true",'msg':"产品规格信息新建成功"}
#                 result=DappDbF1sym_view.dft_dbi_login_req(name, password)
                print(type(result))    
        except Exception:
            result={'status':'true','auth':"false",'msg':"数据库发生错误，请重试"}
        return result