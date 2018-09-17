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
from DappDbFxprcm import views as DappDbFxprcm
from django.db import transaction
class classDappDbFxprcm:
    def __init__(self):
        pass
    
    def dft_dbi_fstt_neno_status(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbFxprcm_view=DappDbFxprcm.dct_classDbiL3apFxPrcm()
        result=DappDbFxprcm_view.dft_dbi_fstt_neno_status(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_set_neon_status(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbFxprcm_view=DappDbFxprcm.dct_classDbiL3apFxPrcm()
        result=DappDbFxprcm_view.dft_dbi_fstt_set_neon_status(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_app_monitor_list(self):
#         try:
#             with transaction.atomic():
        DappDbFxprcm_view=DappDbFxprcm.dct_classDbiL3apFxPrcm()
        result=DappDbFxprcm_view.dft_dbi_fstt_app_monitor_list()
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_app_dev_alarm(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbFxprcm_view=DappDbFxprcm.dct_classDbiL3apFxPrcm()
        result=DappDbFxprcm_view.dft_dbi_fstt_app_dev_alarm(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result