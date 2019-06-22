'''
Created on 2019年2月15日

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
from DappDbF12iwdp import views as DappDbF12iwdp
class classDappDbF12Iwap:
    def __init__(self):
        pass
    
    def dft_dbi_insert_employee(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                DappDbF12iwdp_view.dft_dbi_insert_employee_view(inputData)
                result={"errcode":"0","errmsg":"插入成功"}
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_employee_integral_setting(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                DappDbF12iwdp_view.dft_dbi_employee_integral_setting_view(inputData)
                result={"errcode":"0","errmsg":"插入成功"}
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_integral_get(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_intergral_get_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_employee_user_info(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_employee_user_info_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_company_jsapi_ticket(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_company_jsapi_ticket_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_set_company_jsapi_ticket(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_set_company_jsapi_ticket_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_employee_release_or_save_task(self,inputData,save):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_release_or_save_task_view(inputData,save)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_employee_all_task_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_employee_all_task_list_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_get_task_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_task_detail_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_employee_task_click(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_task_click_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_employee_delete_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_delete_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_accept_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_accept_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_refuse_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_refuse_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_success_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_success_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_fail_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_fail_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_superior_adopt_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_superior_adopt_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_superior_refuse_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_superior_refuse_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_finance_adopt_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_finance_adopt_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_finance_refuse_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_finance_refuse_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_search_task(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_search_task_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_get_employee_integral_all(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_employee_integral_all_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
     
    def dft_dbi_get_employee_integral_day(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_get_employee_integral_day_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    def dft_dbi_employee_get_comments(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_get_comments_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result
    
    def dft_dbi_employee_publish_comment(self,inputData):
        try:
            with transaction.atomic():
                DappDbF12iwdp_view=DappDbF12iwdp.dct_classDbiL3apF12Iwdp()
                result=DappDbF12iwdp_view.dft_dbi_employee_publish_comment_view(inputData)
        except Exception:
            result={"errcode":"1","errmsg":"数据库出现错误，插入失败"}
        return result