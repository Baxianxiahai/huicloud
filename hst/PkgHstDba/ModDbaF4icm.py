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
from DappDbF4icm import views as DappDbF4icm
from django.db import transaction
class classDappDbF4icm:
    def __init__(self):
        pass
    
    def dft_dbi_get_hcu_camweb_link(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_get_hcu_camweb_link(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fstt_get_hcu_camweb_link(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_fstt_get_hcu_camweb_link_view(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_sensor_info_update(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
        result=DappDbF4icm_view.dft_dbi_sensor_info_update(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_hcu_hsmmplist_inquery(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
        result=DappDbF4icm_view.dft_dbi_hcu_hsmmplist_inquery(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_get_camera_status(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_get_camera_status(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    
    
    def dft_dbi_get_three_camera_status(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
        result=DappDbF4icm_view.dft_dbi_get_three_camera_status(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_adjust_camera_vertical(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_adjust_camera_vertical(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_adjust_camera_horizon(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_adjust_camera_horizon(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_adjust_camera_zoom(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_adjust_camera_zoom(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_adjust_camera_reset(self,inputData):
        try:
            with transaction.atomic():
                DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
                result=DappDbF4icm_view.dft_dbi_adjust_camera_reset(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_tbswr_gettempstatus(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
        result=DappDbF4icm_view.dft_dbi_aqyc_tbswr_gettempstatus(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_hcu_lock_compel_open(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF4icm_view=DappDbF4icm.dct_classDbiL3apF4icm()
        result=DappDbF4icm_view.dft_dbi_hcu_lock_compel_open(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    