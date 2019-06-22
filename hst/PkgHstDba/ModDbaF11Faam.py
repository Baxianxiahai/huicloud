# -*- coding: utf-8 -*-
'''
Created on 2018年7月14日

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
from DappDbF11faam import views as DappDbF11Faam
class ClassDbaF11Faam:
    def __init__(self):
        pass
#     def dft_get_user_lever(self,inputData):
#         try:
#             with transaction.atomic():
#                 DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
#                 result=DappDbF11Faam_view.dft_getUserLever(inputData)
#                 print(result)
#         except Exception:
#             result={"status":"true","auth":"false","msg":"数据库发生错误，请重试"}
#         return result
    def dft_faam_factory_codelist_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_factory_codelist_query(inputData)
                print(result)
        except Exception:
            result=""
        return result
    def dft_faam_factory_table_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_factory_table_query(inputData)
                print(result)
        except Exception:
            result=""
        return result
    def dft_factory_table_modify(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_factory_table_modify(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_factory_table_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_factory_table_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_factory_table_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_factory_table_delete(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_type_num_inqury(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_type_num_inquery(inputData)
        except Exception:
            result=0
        return result
    
    def dft_product_type_table_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_type_table_query(inputData)
        except Exception:
            result={}
        return result
    def dft_product_type_modify(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_type_modify(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_type_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_type_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_type_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_type_delete(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_staff_table_modify(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_staff_table_modify(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_staff_table_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_staff_table_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_staff_table_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_staff_table_delete(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_staff_namelist_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_staff_namelist_query(inputData)
        except Exception:
            result=0
        return result
    
    def dft_dbi_employee_number_inquery(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_employee_number_inquery(inputData)
        except Exception:
            result=[]
        return result
    
    def dft_employee_number_inquery(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_employee_number_inquery(inputData)
        except Exception:
            result=0
        return result
        
    def dft_staff_table_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_staff_table_query(inputData)
        except Exception:
            result=[]
        return result
    
    def dft_attendance_history_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_attendance_history_query(inputData)
        except Exception:
            result = {'Result': False, 'ColumnName': [], 'TableData':[]}
        return result
    
    def dft_attendance_record_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_attendance_record_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_attendance_record_batch_add(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_attendance_record_batch_add(inputData)
        except Exception:
            result=False
        return result
    
    def dft_attendance_recode_delete(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_attendance_recode_delete(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_attendance_recode_get(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_attendance_recode_get(inputData)
        except Exception:
            result={}
        return result
    
    def dft_attendance_record_modify(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_attendance_record_modify(inputData)
        except Exception:
            result=False
        return result
    
    def dft_attendance_history_audit(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_attendance_history_audit(inputData)
        except Exception:
            result={'ColumnName':[],'TableData':[],'Result':False}
        return result
    
    def dft_production_history_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_production_history_query(inputData)
        except Exception:
            result={'ColumnName':[],'TableData':[],'Flag':"false"}
        return result
    
    def dft_production_history_audit(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_production_history_audit(inputData)
        except Exception:
            result={'ColumnName':[],'TableData':[],'Result':False,'Flag':"false"}
        return result
    
    def dft_employee_kpi_audit(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_employee_kpi_audit(inputData)
        except Exception:
            result={'ColumnName':[],'TableData':[],'Result':False}
        return result
    
    def dft_consumables_buy(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_consumables_buy(inputData)
        except Exception:
            result={}
        return result
    
    def dft_get_print(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_print(inputData)
        except Exception:
            result={}
        return result
    
    def dft_consumables_table(self):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_consumables_table()
        except Exception:
            ColumnName=[]
            TableData=[]
            ColumnName.append("序号")
            ColumnName.append("名称")
            ColumnName.append("历史总量")
            ColumnName.append("历史总价")
            ColumnName.append("历史平均价格")
            ColumnName.append("最后一次入库时间")
            result={'ColumnName':ColumnName,'TableData':TableData}
        return result
    def dft_consumables_history_table(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_consumables_history_table(inputData)
        except Exception:
            ColumnName=[]
            TableData=[]
            ColumnName.append('序号')
            ColumnName.append('名称')
            ColumnName.append('单价')
            ColumnName.append('数量')
            ColumnName.append('总价')
            ColumnName.append('规格')
            ColumnName.append('供应商')
            ColumnName.append('入库时间')
            result={'ColumnName':ColumnName,'TableData':TableData}
        return result
    
    def dft_get_consumbales_purchase(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_consumbales_purchase(inputData)
        except Exception:
            result={}
        return result
    
    def dft_consumables_purchase_mod(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_consumables_purchase_mod(inputData)
        except Exception:
            result=False
        return result
    def dft_consumables_purchase_del(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_consumables_purchase_del(inputData)
        except Exception:
            result=False
        return result
    
    def dft_product_stock_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_stock_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    
    def dft_get_product_weight_and_size(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_product_weight_and_size()
        except Exception:
            result={}
        return result
    
    def dft_get_product_stock_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_product_stock_list()
        except Exception:
            result={}
        return result
    def dft_get_product_empty_stock(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_product_empty_stock()
        except Exception:
            result={}
        return result
    
    def dft_product_stock_del(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_stock_del(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_stock_table(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_stock_table(inputData)
        except Exception:
            result={}
        return result
    def dft_get_product_stock_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_product_stock_detail(inputData)
        except Exception:
            result={}
        return result
    def dft_product_stock_transfer(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_stock_transfer(inputData)
        except Exception:
            result=False
        return result
    def dft_product_stock_removal_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_stock_removal_new(inputData)
        except Exception:
            result=False
        return result
    def dft_product_stock_history(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_product_stock_history(inputData)
        except Exception:
            result={}
        return result
    def dft_get_product_stock_history_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_product_stock_history_detail(inputData)
        except Exception:
            result={}
        return result
    def dft_dbi_material_stock_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_material_stock_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_get_material_stock_list(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_material_stock_list()
        except Exception:
            result={}
        return result
    def dft_get_material_empty_stock(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_material_empty_stock()
        except Exception:
            result={}
        return result
    def dft_empty_material_stock_del(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_empty_material_stock_del(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_material_stock_table(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_material_stock_table(inputData)
        except Exception:
            result={}
        return result
    def dft_get_material_stock_detail(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_material_stock_detail(inputData)
        except Exception:
            result={}
        return result
    def dft_material_stock_income_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_material_stock_income_new(inputData)
        except Exception:
            result=False
        return result
    def dft_material_stock_remova_new(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_material_stock_remova_new(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_material_stock_history(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_material_stock_history(inputData)
        except Exception:
            result={}
        return result
    def dft_get_material_stock_history_deatil(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_get_material_stock_history_deatil(inputData)
        except Exception:
            result={}
        return result
    def dft_material_stock_income_mod(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_material_stock_income_mod(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_material_stock_removal_mod(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_material_stock_removal_mod(inputData)
        except Exception:
            result=False
        return result
    def dft_material_stock_removal_del(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_material_stock_removal_del(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_stock_removal_mod(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_stock_removal_mod(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_product_stock_removal_del(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_product_stock_removal_del(inputData)
                result=True
        except Exception:
            result=False
        return result
    def dft_faam_table_query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_table_query(inputData)
        except Exception:
            result={}
        return result
    
    def dft_faam_qrcode_audit(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_qrcode_audit(inputData)
        except Exception:
            result={}
        return result

    def dft_faam_qrcode_batch(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_qrcode_batch(inputData)
        except Exception:
            result={}
        return result
    
    def dft_faam_qrcode_kq_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_qrcode_kq_process(inputData)
        except Exception:
            result={'employee': "", 'message': '数据异常'}
        return result
    def dft_faam_qrcode_sc_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_qrcode_sc_process(inputData)
        except Exception:
            result= {'flag': False, 'employee': "", 'message': '数据异常'}
        return result
    def dft_huitp_xmlmsg_equlable_apply_report(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_huitp_xmlmsg_equlable_apply_report(inputData)
        except Exception:
            result={'start':0,'end':0,'allocateResp':1,'comConfirm':0X02}
        return result
    def dft_huitp_xmlmsg_equlable_userlist_report(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_huitp_xmlmsg_equlable_userlist_report(inputData)
        except Exception:
            result={'comConfirm':0X02,'userList':"",'currrntNum':0,'totalNum':0}
        return result
    
    def dft_faam_old_data_clear(self,inputData):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                result=DappDbF11Faam_view.dft_dbi_faam_old_data_clear(inputData)
        except Exception:
            result={'status':'false'}
        return result
    
    def dft_cron_production_and_batch_table_sta(self):
        try:
            with transaction.atomic():
                DappDbF11Faam_view=DappDbF11Faam.dct_classDbiL3apF11Faam()
                DappDbF11Faam_view.dft_dbi_cron_production_table_sta()
                DappDbF11Faam_view.dft_dbi_cron_batch_scan_table_sta()
                result={'status':'true'}
        except Exception:
            result={'status':'false'}
        return result