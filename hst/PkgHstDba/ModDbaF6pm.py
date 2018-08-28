# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

@author: Administrator
'''
import sys
import os
import django
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbF6pm import views as DappDbF6pm
from django.db import transaction
class classDappDbF6pm:
    def __init__(self):
        pass
    def dft_dbi_aqyc_performance_table_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF6pm_view=DappDbF6pm.dct_classDbiL3apF6pm()
        result=DappDbF6pm_view.dft_dbi_aqyc_performance_table_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result