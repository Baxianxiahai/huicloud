# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: Administrator
'''

from PkgHstDba import ModDbaF1sym
from PkgHstDba import ModDbaF11Faam
class ClassDbaMainEntry():
    def __init__(self):
        pass
    
    def dft_F1sym_Send_Message(self,inputData):
        if inputData['action']=='login':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_login_req(inputData['body'])
        if inputData['action']=='Get_user_auth_code':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userauthcode_process(inputData['body'])
        if inputData['action']=='Reset_password':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_reset_password_process(inputData['body'])
        if inputData['action']=='UserInfo':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_req(inputData['body'])
        if inputData['action']=='UserNew':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_new(inputData['body'])
        if inputData['action']=='UserDel':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_delete(inputData['body'])
        if inputData['action']=='getUserLength':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_usernum_inquery()
        if inputData['action']=='sessioncheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_session_check(inputData['body'])
        if inputData['action']=='authcheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_user_authcheck(inputData['body'])
        if inputData['action']=='UserTable':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_usertable_req(inputData['body'])
        if inputData['action']=="UserMod":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_update(inputData['body'])
        return result
    
    def dft_F11Faam_Send_Message(self,inputData):    
        #F11FAAM    
#         if inputData['action']=='getUserLeve':
#             F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
#             result=F11Faam.dft_get_user_lever(inputData['body'])
        if inputData['action']=='FactoryCodeList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_factory_codelist_query(inputData['body'])
        if inputData['action']=="FactoryTable":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_factory_table_query(inputData['body'])
        if inputData['action']=="FactoryMod":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_modify(inputData['body'])
        if inputData['action']=='FactoryNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_new(inputData['body'])
        if inputData['action']=='FactoryDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_delete(inputData['body'])
        if inputData['action']=='getTypeNum':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_num_inqury(inputData['body'])
        if inputData['action']=='SpecificationTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_table_query(inputData['body'])
        if inputData['action']=="SpecificationMod":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_modify(inputData['body'])
        if inputData['action']=="SpecificationNew":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_new(inputData['body'])
        if inputData['action']=="SpecificationDel":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_delete(inputData['body']) 
         
        if inputData['action']=='getEmployeeNum':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_employee_number_inquery(inputData['body']) 
            
        if inputData['action']=='StaffnameList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_namelist_query(inputData['body']) 
            
        if inputData['action']=='StaffTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_query(inputData['body']) 
         
        if inputData['action']=='StaffMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_modify(inputData['body'])  
            
        if inputData['action']=='StaffNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_new(inputData['body'])  
        
        if inputData['action']=='StaffDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_delete(inputData['body'])  
        
        if inputData['action']=='AttendanceHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_history_query(inputData['body'])
        
        if inputData['action']=='AttendanceNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_new(inputData['body'])
        
        if inputData['action']=='AttendanceBatchNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_batch_add(inputData['body'])  
        
        if inputData['action']=='AttendanceDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_recode_delete(inputData['body'])
        
        if inputData['action']=='GetAttendance':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_recode_get(inputData['body'])
        
        if inputData['action']=='AttendanceMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_modify(inputData['body'])
        
        if inputData['action']=='AttendanceAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_history_audit(inputData['body'])
        if inputData['action']=='AssembleHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_production_history_query(inputData['body'])
        if inputData['action']=='AssembleAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_production_history_audit(inputData['body'])
        if inputData['action']=='KPIAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_employee_kpi_audit(inputData['body'])
        if inputData['action']=='ConsumablesPurchaseNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_buy(inputData['body'])
        if inputData['action']=='GetPrint':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
        if inputData['action']=='ConsumablesTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_table()
        if inputData['action']=='ConsumablesHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_history_table(inputData['body'])
        if inputData['action']=='GetConsumablesPurchase':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_consumbales_purchase(inputData['body'])
        if inputData['action']=='ConsumablesPurchaseMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_purchase_mod(inputData['body'])
        if inputData['action']=='ConsumablesPurchaseDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_purchase_del(inputData['body'])
        if inputData['action']=='ProductStockNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_new(inputData['body'])
        if inputData['action']=='GetProductWeightAndSize':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_weight_and_size(inputData['body'])
        if inputData['action']=='GetProductStockList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_list(inputData['body'])
        if inputData['action']=='GetProductEmptyStock':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_empty_stock(inputData['body'])
        if inputData['action']=='ProductStockTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_table(inputData['body'])
        if inputData['action']=='ProductStockDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_del(inputData['body'])
        if inputData['action']=='GetProductStockDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_detail(inputData['body'])
        if inputData['action']=='ProductStockTransfer':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_transfer(inputData['body'])
        if inputData['action']=='ProductStockHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_history(inputData['body'])
        if inputData['action']=='MaterialStockNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_dbi_material_stock_new(inputData['body'])
        if inputData['action']=='GetMaterialStockList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_list(inputData['body'])
        if inputData['action']=='GetMaterialEmptyStock':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_empty_stock(inputData['body'])
        if inputData['action']=='MaterialStockDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_empty_material_stock_del(inputData['body'])
        if inputData['action']=='MaterialStockTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_table(inputData['body'])
        if inputData['action']=='MaterialStockIncomeNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_income_new(inputData['body'])
        if inputData['action']=='MaterialStockRemovalNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_remova_new(inputData['body'])
        if inputData['action']=='MaterialStockHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_history(inputData['body'])
        if inputData['action']=='GetMaterialStockDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_detail(inputData['body'])
        if inputData['action']=='GetMaterialStockHistoryDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_history_deatil(inputData['body'])
        if inputData['action']=='MaterialStockIncomeMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_income_mod(inputData['body'])
        if inputData['action']=='MaterialStockRemovalDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_removal_del(inputData['body'])
        if inputData['action']=='GetProductStockHistoryDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_history_detail(inputData['body'])
        if inputData['action']=='ProductStockRemovalMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_mod(inputData['body'])
        if inputData['action']=='ProductStockRemovalDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_del(inputData['body'])
        if inputData['action']=='ProductStockRemovalNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_new(inputData['body'])
#         if inputData['action']=='GetConsumablesVendorList':
#             F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
#             result=F11Faam.dft_get_print(inputData['body'])
#  
#         if inputData['action']=='GetConsumablesTypeList':
#             F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
#             result=F11Faam.dft_get_print(inputData['body'])
 
        if inputData['action']=='F11TableQuery':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_table_query(inputData['body'])
 
         
         
         
         
         
        if inputData['action']=='SeafoodInfo':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
         
        if inputData['action']=='SeafoodAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
  
        
        return result
        