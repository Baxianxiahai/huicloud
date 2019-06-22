# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

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
from django.db import transaction
from DappDbF10oam import views as DappDbF10oam
class classDappDbF10oam:
    def __init__(self):
        pass
    
    def dft_dbi_tools_qrcode_filelist(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_qrcode_filelist(inputData)
        except Exception:
            result=""
        return result
    def dft_dbi_tools_qrcode_newapply(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_qrcode_newapply(inputData)
        except Exception:
            result=""
        return result
    def dft_dbi_qrcode_data_insert(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_qrcode_data_insert(inputData)
        except Exception:
            result=""
        return result
    def dft_dbi_tools_swload_table_get(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_swload_table_get(inputData)
        except Exception:
            result={'ColumnName':[],'TableData':[]}
        return result
    
    def dft_dbi_tools_swload_info_add(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_swload_info_add(inputData)
        except Exception:
            result={'auth': 'false', 'msg': "添加新的SW Load信息失败"}
        return result
    
    def dft_dbi_tools_swload_info_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_swload_info_delete(inputData)
        except Exception:
            result=False
        return result
    
    def dft_dbi_tools_swload_validflag_change(self,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_tools_swload_validflag_change(inputData)
        except Exception:
            result=False
        return result
    
    '''从下位机发上来的消息处理'''
    def dft_dbi_hcu_inventory_confirm(self,socketId,inputData):
        try:
            with transaction.atomic():
                DappDbF10oam_view=DappDbF10oam.dct_DappF10Class()
                result=DappDbF10oam_view.dft_dbi_hcu_inventory_confirm_view(socketId, inputData)
        except Exception:
            result=None
        return result