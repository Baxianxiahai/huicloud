'''
Created on 2019年4月17日

@author: Administrator
'''

import sys
import os
import django
import json
from unittest.test.test_program import RESULT
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from django.db import transaction
from DappDbF13phos import views as DappDbF13Phos

class classDappDbF13Phos:
    def __init__(self):
        pass
    def dft_dbi_check_openid(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_check_openid_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_user_telphone_register(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_user_telphone_register_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_get_coampany_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_coampany_list_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_upload_user_location(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_upload_user_location_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_driver_information_submit(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_driver_information_submit_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_task_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_task_list_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_user_accept_task_info(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_user_accept_task_info_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_get_contract_information(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_contract_information_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_user_refuse_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_user_refuse_task_view(inputData)
        except Exception:
            result={"status":"false","msg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_user_accept_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_user_accept_task_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_user_accepted_task_info(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_user_accepted_task_info_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_upload_picture_infomation(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_upload_picture_infomation_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_upload_video(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_upload_video_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_video_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_video_list_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    def dft_dbi_video_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_video_delete_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_task_done(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_task_done_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_task_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_task_detail_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_user_information(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_get_user_information_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_car_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_car_list_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_binding_license_plate(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_binding_license_plate_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_manage_information_submit(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_manage_information_submit_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_free_plate_list(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_get_free_plate_list_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_goods_list(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_get_goods_list_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_get_account_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
                result=DappDbF13phos_view.dft_dbi_get_account_list_view(inputData)
        except Exception:
            result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_manage_release_task(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_manage_release_task_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    def dft_dbi_get_refuse_task_list(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_get_refuse_task_list_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_delete_task_info(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_delete_task_info_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result
    
    def dft_dbi_task_reselection(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF13phos_view=DappDbF13Phos.dct_classDbiL3apF13Phos()
        result=DappDbF13phos_view.dft_dbi_task_reselection_view(inputData)
#         except Exception:
#             result={"status":"false","msg":"信息更新失败"}
        return result