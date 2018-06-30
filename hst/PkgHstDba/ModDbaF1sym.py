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
from DappDbF1sym import views
class ClassDbaF1sym():
    def dft_login_req(self,inputData):
        name=inputData['name']
        password=inputData['password']
        DappDbF1sym_view=views.dct_classDbiL3apF1sym()
        result=DappDbF1sym_view.dft_dbi_login_req(name, password)
        return json.dumps(result)