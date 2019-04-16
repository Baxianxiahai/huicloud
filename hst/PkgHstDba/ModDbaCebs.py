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

    def dft_dbi_user_sheet_add(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_user_sheet_add(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_user_sheet_modify(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_user_sheet_modify(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_user_sheet_read(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_user_sheet_read(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_user_sheet_delete(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_user_sheet_delete(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_product_profile_add(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_product_profile_add(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_product_profile_modify(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_product_profile_modify(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_product_profile_read(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_product_profile_read(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_product_profile_delete(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_product_profile_delete(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_cali_profile_add(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_cali_profile_add(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_cali_profile_modify(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_cali_profile_modify(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_cali_profile_read(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_cali_profile_read(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_cali_profile_delete(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_cali_profile_delete(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_object_profile_add(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_object_profil_add(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result
    
    def dft_dbi_object_profile_modify(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_object_profile_modify(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_object_profile_read(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_object_profile_read(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result

    def dft_dbi_object_profile_delete(self, inputData):
#         try:
#             with transaction.atomic():
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_object_profile_delete(inputData)
#         except Exception:
#             result={'status':'false','auth':'true','data':{},'msg':'登录失败，请稍后重试'}
        return result



    def dft_dbi_config_eleg_add(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_eleg_add(inputData)
        return result
    
    def dft_dbi_config_eleg_modify(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_eleg_modify(inputData)
        return result

    def dft_dbi_config_eleg_read(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_eleg_read(inputData)
        return result

    def dft_dbi_config_eleg_delete(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_eleg_delete(inputData)
        return result

    def dft_dbi_config_stackcell_add(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_stackcell_add(inputData)
        return result
    
    def dft_dbi_config_stackcell_modify(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_stackcell_modify(inputData)
        return result

    def dft_dbi_config_stackcell_read(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_stackcell_read(inputData)
        return result

    def dft_dbi_config_stackcell_delete(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_config_stackcell_delete(inputData)
        return result
    
    def dft_dbi_result_eleg_add(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_eleg_add(inputData)
        return result
    
    def dft_dbi_result_eleg_modify(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_eleg_modify(inputData)
        return result

    def dft_dbi_result_eleg_read(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_eleg_read(inputData)
        return result

    def dft_dbi_result_eleg_delete(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_eleg_delete(inputData)

    def dft_dbi_result_stackcell_add(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_stackcell_add(inputData)
        return result
    
    def dft_dbi_result_stackcell_modify(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_stackcell_modify(inputData)
        return result

    def dft_dbi_result_stackcell_read(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_stackcell_read(inputData)
        return result

    def dft_dbi_result_stackcell_delete(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_result_stackcell_delete(inputData)

    def dft_dbi_cebs_init_config_read(self, inputData):
        DappDbCebs_view = DappDbCebs.dct_classDbiViewDebs()
        result = DappDbCebs_view.dft_dbi_cebs_init_config_read(inputData)
        return result
        
        





    
