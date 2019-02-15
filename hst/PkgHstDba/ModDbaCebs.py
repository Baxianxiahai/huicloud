'''
Created on 2019年1月30日

@author: Administrator
'''

import sys
import os
import django
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
django.setup()
from django.db import transaction
from DappDbCebs import views as DappDbCebs


class ClassDbaCebs():
    def __init__(self):
        pass

    def dft_dbi_env_add(self, inputData):
        try:
            print("inputData=",inputData)
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_env_add(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_env_modify(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_env_modify(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_env_read(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_env_read(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_env_delete(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_env_delete(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_counter_add(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_counter_add(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_counter_modify(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_counter_modify(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_counter_read(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_counter_read(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_counter_delete(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_counter_delete(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_fspc_add(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_fspc_add(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_fspc_modify(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_fspc_modify(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_fspc_read(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_fspc_read(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_fspc_delete(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_fspc_delete(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_file_add(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_file_add(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_file_modify(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_file_modify(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_file_read(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_file_read(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_file_delete(self, inputData):
        try:
            with transaction.atomic():
                DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
                result = DappDbCebs_view.dft_dbi_file_delete(inputData)
        except Exception:
            result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result











    