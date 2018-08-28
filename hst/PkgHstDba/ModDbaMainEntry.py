# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: Administrator
'''

from PkgHstDba import ModDbaF1sym
from PkgHstDba import ModDbaF2cm
from PkgHstDba import ModDbaF3dm
from PkgHstDba import ModDbaF4icm
from PkgHstDba import ModDbaF5fm
from PkgHstDba import ModDbaF6pm
from PkgHstDba import ModDbaF7ads
from PkgHstDba import ModDbaF8psm
from PkgHstDba import ModDbaF9gism
from PkgHstDba import ModDbaF10oam
from PkgHstDba import ModDbaF11Faam
from PkgHstDba import ModDbaFxprcm
from PkgHstDba import ModDbaSnr
class ClassDbaMainEntry():
    def __init__(self):
        pass
    
    def dft_F1sym_Send_Message(self,inputData):
        if inputData['action']=='login':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_login_req(inputData['body'])
        elif inputData['action']=='Get_user_auth_code':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userauthcode_process(inputData['body'])
        elif inputData['action']=='Reset_password':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_reset_password_process(inputData['body'])
        elif inputData['action']=='UserInfo':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_req(inputData['body'])
        elif inputData['action']=='UserNew':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_new(inputData['body'])
        elif inputData['action']=='UserDel':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_delete(inputData['body'])
        elif inputData['action']=='getUserLength':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_usernum_inquery()
        elif inputData['action']=='sessioncheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_session_check(inputData['body'])
        elif inputData['action']=='authcheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_user_authcheck(inputData['body'])
        elif inputData['action']=='UserTable':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_usertable_req(inputData['body'])
        elif inputData['action']=="UserMod":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_update(inputData['body'])
        else:
            result=""
        return result
    
    def dft_F2cm_Send_Message(self,inputData): 
        F2cm=ModDbaF2cm.classDappDbF2cm()
        if inputData['action']=='TableQuery':
            result=F2cm.dft_dbi_print_excel_table_query_process(inputData['body'])
        elif inputData['action']=='ProjectPGList':
            result=F2cm.dft_dbi_user_all_projpglist_req(inputData['body'])
        elif inputData['action']=='ProjectList':
            result=F2cm.dft_dbi_user_all_projlist_req(inputData['body'])
        elif inputData['action']=='UserProj':
            result=F2cm.dft_dbi_user_projpglist_req(inputData['body'])
        elif inputData['action']=='getPGNum':
            result=F2cm.dft_dbi_all_pgnum_inquery()
        elif inputData['action']=='PGTable':
            result=F2cm.dft_dbi_user_pg_table_req(inputData['body'])
        elif inputData['action']=='PGNew':
            result=F2cm.dft_dbi_pginfo_new(inputData['body'])
        elif inputData['action']=='PGMod':
            result=F2cm.dft_dbi_pginfo_modify(inputData['body'])
        elif inputData['action']=='PGDel':
            result=F2cm.dft_dbi_pginfo_delete(inputData['body'])
        elif inputData['action']=='PGProj':
            result=F2cm.dft_dbi_pg_projlist_req(inputData['body'])
        elif inputData['action']=='getProjNum':
            result=F2cm.dft_dbi_project_number_inquery()
        elif inputData['action']=='ProjTable':
            result=F2cm.dft_dbi_all_project_table_req(inputData['body'])
        elif inputData['action']=='ProjNew':
            result=F2cm.dft_dbi_projinfo_new(inputData['body'])
        elif inputData['action']=='ProjMod':
            result=F2cm.dft_dbi_projinfo_modify(inputData['body'])
        elif inputData['action']=='ProjPoint':
            result=F2cm.dft_dbi_user_all_project_sitelist_req(inputData['body'])
        elif inputData['action']=='PointProj':
            result=F2cm.dft_dbi_one_proj_sitelist_req(inputData['body'])
        elif inputData['action']=='getSiteNum':
            result=F2cm.dft_dbi_all_sitenum_inquery()
        elif inputData['action']=='PointTable':
            result=F2cm.dft_dbi_all_sitetable_req(inputData['body'])
        elif inputData['action']=='PointNew':
            result=F2cm.dft_dbi_siteInfo_new(inputData['body'])
        elif inputData['action']=='PointMod':
            result=F2cm.dft_dbi_siteinfo_modify(inputData['body'])
        elif inputData['action']=='PointDev':
            result=F2cm.dft_dbi_site_devlist_req(inputData['body'])
        elif inputData['action']=='getHcuNum':
            result=F2cm.dft_dbi_all_hcunum_inquery()
        elif inputData['action']=='DevTable':
            result=F2cm.dft_dbi_all_hcutable_req(inputData['body'])
        elif inputData['action']=='DevNew':
            result=F2cm.dft_dbi_aqyc_devinfo_new(inputData['body'])
        elif inputData['action']=='DevMod':
            result=F2cm.dft_dbi_aqyc_devinfo_update(inputData['body'])
        elif inputData['action']=='GetStationActiveInfo':
            result=F2cm.dft_dbi_point_get_activeinfo(inputData['body'])
        elif inputData['action']=='StationActive':
            result=F2cm.dft_dbi_point_set_activeinfo(inputData['body'])
        elif inputData['action']=='HCU_AQYC_Activate':
            result=F2cm.dft_dbi_login_req(inputData['body'])
        elif inputData['action']=='AqycDevDel':
            result=F2cm.dft_dbi_aqyc_deviceinfo_delete(inputData['body'])
        elif inputData['action']=='PointDel':
            result=F2cm.dft_dbi_siteinfo_delete(inputData['body'])
        elif inputData['action']=='ProjDel':
            result=F2cm.dft_dbi_projinfo_delete(inputData['body'])
        elif inputData['action']=='FHYSPointDel':
            result=F2cm.dft_dbi_site_keyauth_delete(inputData['body'])
        elif inputData['action']=='FHYSDevDel':
            result=F2cm.dft_dbi_fhys_deviceinfo_delete(inputData['body'])
        elif inputData['action']=='UserKey':
            result=F2cm.dft_dbi_project_userkey_process(inputData['body'])
        elif inputData['action']=='ProjKeyList':
            result=F2cm.dft_dbi_all_projkey_process(inputData['body'])
        elif inputData['action']=='ProjKey':
            result=F2cm.dft_dbi_project_keylist_proces(inputData['body'])
        elif inputData['action']=='ProjUserList':
            result=F2cm.dft_dbi_all_projkeyuser_process(inputData['body'])
        elif inputData['action']=='getKeyNum':
            result=F2cm.dft_dbi_all_keynum_inquiry()
        elif inputData['action']=='KeyTable':
            result=F2cm.dft_dbi_all_keytable_req(inputData['body'])
        elif inputData['action']=='KeyNew':
            result=F2cm.dft_dbi_key_new_process(inputData['body'])
        elif inputData['action']=='KeyMod':
            result=F2cm.dft_dbi_key_mod_process(inputData['body'])
        elif inputData['action']=='KeyDel':
            result=F2cm.dft_dbi_key_del_process(inputData['body'])
        elif inputData['action']=='DomainAuthlist':
            result=F2cm.dft_dbi_obj_authlist_process(inputData['body'])
        elif inputData['action']=='KeyAuthlist':
            result=F2cm.dft_dbi_key_authlist_process(inputData['body'])
        elif inputData['action']=='KeyGrant':
            result=F2cm.dft_dbi_key_grant_process(inputData['body'])
        elif inputData['action']=='KeyAuthNew':
            result=F2cm.dft_dbi_key_authnew_process(inputData['body'])
        elif inputData['action']=='KeyAuthDel':
            result=F2cm.dft_dbi_key_authdel_process(inputData['body'])
        elif inputData['action']=='GetRTUTable':
            result=F2cm.dft_dbi_login_req(inputData['body'])
        elif inputData['action']=='GetOTDRTable':
            result=F2cm.dft_dbi_login_req(inputData['body'])
        elif inputData['action']=='FhysSiteDel':
            result=F2cm.dft_dbi_site_keyauth_delete(inputData['body'])  
        else:
            result=""
        return result
    
    def dft_F3dm_Send_Message(self,inputData): 
        F3dm=ModDbaF3dm.classDappDbF3dm()
        if inputData['action']=='MonitorList':
            result=F3dm.dft_dbi_map_active_siteinfo_req(inputData['body'])
        elif inputData['action']=='FakeMonitorList':
            result=F3dm.dft_dbi_map_inactive_siteinfo_req(inputData['body'])
        elif inputData['action']=='Favourite_list':
            result=F3dm.dft_dbi_favoursite_list_process(inputData['body'])
        elif inputData['action']=='Favourite_count':
            result=F3dm.dft_dbi_favourite_count_process(inputData['body'])
        elif inputData['action']=='GetStaticMonitorTable':
            result=F3dm.dft_dbi_aqyc_user_dataaggregate_req(inputData['body'])
        elif inputData['action']=='GetFhysStaticMonitorTable':
            result=F3dm.dft_dbi_fhys_user_dataaggregate_req(inputData['body'])
        elif inputData['action']=='DevSensor':
            result=F3dm.dft_dbi_aqyc_dev_sensorinfo_req(inputData['body'])
        elif inputData['action']=='SensorList':
            result=F3dm.dft_dbi_all_sensorlist_req(inputData['body'])
        elif inputData['action']=='PointPicture':
            result=F3dm.dft_dbi_point_install_picture_process(inputData['body'])
        elif inputData['action']=='KeyHistory':
            result=F3dm.dft_dbi_key_event_history_process(inputData['body'])
        elif inputData['action']=='GetOpenImg':
            result=F3dm.dft_dbi_door_open_picture_process(inputData['body'])
        else:
            result=""
        return result
    def dft_F4icm_Send_Message(self,inputData): 
        F4icm=ModDbaF4icm.classDappDbF4icm()
        if inputData['action']=='SensorUpdate':
            result=F4icm.dft_dbi_sensor_info_update(inputData['body'])
        elif inputData['action']=='GetVideoCameraWeb':
            result=F4icm.dft_dbi_get_hcu_camweb_link(inputData['body'])
        elif inputData['action']=='GetVideoList':
            result=F4icm.dft_dbi_hcu_hsmmplist_inquery(inputData['body'])
        elif inputData['action']=='GetCameraStatus':
            result=F4icm.dft_dbi_get_camera_status(inputData['body'])
        elif inputData['action']=='CameraVAdj':
            result=F4icm.dft_dbi_adjust_camera_vertical(inputData['body'])
        elif inputData['action']=='CameraHAdj':
            result=F4icm.dft_dbi_adjust_camera_horizon(inputData['body'])
        elif inputData['action']=='CameraZAdj':
            result=F4icm.dft_dbi_adjust_camera_zoom(inputData['body'])
        elif inputData['action']=='CameraReset':
            result=F4icm.dft_dbi_adjust_camera_reset(inputData['body'])
        elif inputData['action']=='OpenLock':
            result=F4icm.dft_dbi_hcu_lock_compel_open(inputData['body'])
        elif inputData['action']=='GetTempStatus':
            result=F4icm.dft_dbi_aqyc_tbswr_gettempstatus(inputData['body'])
        else:
            result=""
        return result
    def dft_F5fm_Send_Message(self,inputData): 
        F5fm=ModDbaF5fm.classDappDbF5fm()
        if inputData['action']=='MonitorAlarmList':
            result=F5fm.dft_dbi_map_alarm_site_info_req(inputData['body'])
        elif inputData['action']=='DevAlarm':
            result=F5fm.dft_dbi_aqyc_dev_currentvalue_req(inputData['body'])
        elif inputData['action']=='AlarmType':
            result=F5fm.dft_dbi_all_alarmtype_req(inputData['body'])
        elif inputData['action']=='AlarmQuery':
            result=F5fm.dft_dbi_aqyc_dev_alarmhistory_req(inputData['body'])
        elif inputData['action']=='AlarmQueryRealtime':
            result=F5fm.dft_dbi_aqyc_dev_alarmhistory_realtime_req(inputData['body'])
        elif inputData['action']=='GetWarningHandleListTable':
            result=F5fm.dft_dbi_aqyc_alarm_history_table_req(inputData['body'])
        elif inputData['action']=='GetHyfsWarningHandleListTable':
            result=F5fm.dft_dbi_fhys_alarm_history_table_req(inputData['body'])
        elif inputData['action']=='GetWarningImg':
            result=F5fm.dft_dbi_aqyc_alarm_image_req(inputData['body'])
        elif inputData['action']=='AlarmHandle':
            result=F5fm.dft_dbi_aqyc_alarm_handle_process(inputData['body'])
        elif inputData['action']=='AlarmClose':
            result=F5fm.dft_dbi_aqyc_alarm_close_process(inputData['body'])
        elif inputData['action']=='GetHistoryRTSP':
            result=F5fm.dft_dbi_aqyc_alarm_rstp_req(inputData['body'])
        elif inputData['action']=='FhysAlarmClose':
            result=F5fm.dft_dbi_fhys_alarm_close_process(inputData['body'])
        else:
            result=""
        return result
    def dft_F6pm_Send_Message(self,inputData): 
        F6pm=ModDbaF6pm.classDappDbF6pm()
        if inputData['action']=='GetAuditStabilityTable':
            result=F6pm.dft_dbi_aqyc_performance_table_req(inputData['body'])
        else:
            result=""
        return result
    def dft_F7ads_Send_Message(self,inputData): 
        return False
    def dft_F8psm_Send_Message(self,inputData): 
        return False
    def dft_F9gism_Send_Message(self,inputData): 
        return False
    def dft_F10oam_Send_Message(self,inputData): 
        return False
    def dft_F11Faam_Send_Message(self,inputData):    
        if inputData['action']=='FactoryCodeList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_factory_codelist_query(inputData['body'])
        elif inputData['action']=="FactoryTable":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_factory_table_query(inputData['body'])
        elif inputData['action']=="FactoryMod":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_modify(inputData['body'])
        elif inputData['action']=='FactoryNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_new(inputData['body'])
        elif inputData['action']=='FactoryDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_factory_table_delete(inputData['body'])
        elif inputData['action']=='getTypeNum':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_num_inqury(inputData['body'])
        elif inputData['action']=='SpecificationTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_table_query(inputData['body'])
        elif inputData['action']=="SpecificationMod":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_modify(inputData['body'])
        elif inputData['action']=="SpecificationNew":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_new(inputData['body'])
        elif inputData['action']=="SpecificationDel":
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_type_delete(inputData['body'])         
        elif inputData['action']=='getEmployeeNum':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_employee_number_inquery(inputData['body'])        
        elif inputData['action']=='StaffnameList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_namelist_query(inputData['body']) 
        elif inputData['action']=='getStaffNum':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_dbi_employee_number_inquery(inputData['body'])   
        elif inputData['action']=='StaffTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_query(inputData['body']) 
        elif inputData['action']=='StaffMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_modify(inputData['body'])    
        elif inputData['action']=='StaffNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_new(inputData['body'])  
        elif inputData['action']=='StaffDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_staff_table_delete(inputData['body'])  
        elif inputData['action']=='AttendanceHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_history_query(inputData['body'])
        elif inputData['action']=='AttendanceNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_new(inputData['body'])
        elif inputData['action']=='AttendanceBatchNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_batch_add(inputData['body'])  
        elif inputData['action']=='AttendanceDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_recode_delete(inputData['body'])
        elif inputData['action']=='GetAttendance':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_recode_get(inputData['body'])
        elif inputData['action']=='AttendanceMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_record_modify(inputData['body'])
        elif inputData['action']=='AttendanceAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_attendance_history_audit(inputData['body'])
        elif inputData['action']=='AssembleHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_production_history_query(inputData['body'])
        elif inputData['action']=='AssembleAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_production_history_audit(inputData['body'])
        elif inputData['action']=='KPIAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_employee_kpi_audit(inputData['body'])
        elif inputData['action']=='ConsumablesPurchaseNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_buy(inputData['body'])
        elif inputData['action']=='GetPrint':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
        elif inputData['action']=='ConsumablesTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_table()
        elif inputData['action']=='ConsumablesHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_history_table(inputData['body'])
        elif inputData['action']=='GetConsumablesPurchase':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_consumbales_purchase(inputData['body'])
        elif inputData['action']=='ConsumablesPurchaseMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_purchase_mod(inputData['body'])
        elif inputData['action']=='ConsumablesPurchaseDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_consumables_purchase_del(inputData['body'])
        elif inputData['action']=='ProductStockNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_new(inputData['body'])
        elif inputData['action']=='GetProductWeightAndSize':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_weight_and_size(inputData['body'])
        elif inputData['action']=='GetProductStockList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_list(inputData['body'])
        elif inputData['action']=='GetProductEmptyStock':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_empty_stock(inputData['body'])
        elif inputData['action']=='ProductStockTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_table(inputData['body'])
        elif inputData['action']=='ProductStockDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_del(inputData['body'])
        elif inputData['action']=='GetProductStockDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_detail(inputData['body'])
        elif inputData['action']=='ProductStockTransfer':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_transfer(inputData['body'])
        elif inputData['action']=='ProductStockHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_history(inputData['body'])
        elif inputData['action']=='MaterialStockNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_dbi_material_stock_new(inputData['body'])
        elif inputData['action']=='GetMaterialStockList':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_list(inputData['body'])
        elif inputData['action']=='GetMaterialEmptyStock':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_empty_stock(inputData['body'])
        elif inputData['action']=='MaterialStockDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_empty_material_stock_del(inputData['body'])
        elif inputData['action']=='MaterialStockTable':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_table(inputData['body'])
        elif inputData['action']=='MaterialStockIncomeNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_income_new(inputData['body'])
        elif inputData['action']=='MaterialStockRemovalNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_remova_new(inputData['body'])
        elif inputData['action']=='MaterialStockHistory':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_history(inputData['body'])
        elif inputData['action']=='GetMaterialStockDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_detail(inputData['body'])
        elif inputData['action']=='GetMaterialStockHistoryDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_material_stock_history_deatil(inputData['body'])
        elif inputData['action']=='MaterialStockIncomeMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_income_mod(inputData['body'])
        elif inputData['action']=='MaterialStockRemovalDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_material_stock_removal_del(inputData['body'])
        elif inputData['action']=='GetProductStockHistoryDetail':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_product_stock_history_detail(inputData['body'])
        elif inputData['action']=='ProductStockRemovalMod':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_mod(inputData['body'])
        elif inputData['action']=='ProductStockRemovalDel':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_del(inputData['body'])
        elif inputData['action']=='ProductStockRemovalNew':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_product_stock_removal_new(inputData['body'])
            
#         elif inputData['action']=='GetConsumablesVendorList':
#             F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
#             result=F11Faam.dft_get_print(inputData['body'])
#  
#         elif inputData['action']=='GetConsumablesTypeList':
#             F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
#             result=F11Faam.dft_get_print(inputData['body'])
 
        elif inputData['action']=='F11TableQuery':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_table_query(inputData['body'])      
        elif inputData['action']=='SeafoodInfo':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
         
        elif inputData['action']=='SeafoodAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
        else:
            result=''
        return result
    def dft_Fxprcm_Send_Message(self,inputData): 
        return False
    def dft_Snr_Send_Message(self,inputData): 
        return False
        