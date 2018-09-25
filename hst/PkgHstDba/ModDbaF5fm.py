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
from DappDbF5fm import views as DappDbF5fm
from DappDbF3dm import views as DappDbF3dm
from django.db import transaction

class classDappDbF5fm:
    def __init__(self):
        pass
    
    def dft_dbi_aqyc_dev_currentvalue_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
                result=DappDbF3dm_view.dft_dbi_aqyc_dev_currentvalue_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_dev_alarmhistory_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_dev_alarmhistory_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_dev_alarmhistory_realtime_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
        result=DappDbF5fm_view.dft_dbi_aqyc_dev_alarmhistory_realtime_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_alarmtype_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_all_alarmtype_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_map_alarm_site_info_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
        result=DappDbF5fm_view.dft_dbi_map_alarm_site_info_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_alarm_history_table_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_alarm_history_table_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_alarm_image_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_alarm_image_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_alarm_rstp_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_alarm_rstp_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_alarm_handle_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_alarm_handle_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_alarm_close_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_aqyc_alarm_close_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_alarmtype_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_all_alarmtype_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_dev_currentvalue_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_fhys_dev_currentvalue_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_alarm_history_table_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_fhys_alarm_history_table_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_alarm_handle_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
        result=DappDbF5fm_view.dft_dbi_fhys_alarm_handle_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_alarm_close_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF5fm_view=DappDbF5fm.dct_classDbiL3apF5fm()
                result=DappDbF5fm_view.dft_dbi_fhys_alarm_close_process(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    