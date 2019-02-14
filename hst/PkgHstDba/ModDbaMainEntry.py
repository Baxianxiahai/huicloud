# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: Administrator
'''
import time,json
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
from PkgHstDba import ModDbaCebs
from PkgAccessEntry.ModAccessDict import *


class ClassDbaMainEntry():
    def __init__(self):
        pass
    
    def dft_F1sym_Send_Message(self, inputData):
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
        elif inputData['action']=="HCU_Login_Binding":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_HCU_Login_Binding(inputData['body'])
        elif inputData['action']=="GetUsrInfo":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_get_user_info(inputData['body'])
        elif inputData['action']=="UpdateTel":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_openid_name_binding(inputData['body'])
        elif inputData['action']=="HCU_Re_Login":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_user_re_login(inputData['body'])
        elif inputData['action']=="HCU_Session_Binding":
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_HCU_Session_Binding(inputData['body'])
        else:
            result=""
        return result
    
    def dft_F2cm_Send_Message(self,inputData): 
        F2cm=ModDbaF2cm.classDappDbF2cm()
        F2cmHCU=ModDbaF2cm.HCUF2cmDataBaseConfirm()
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
        elif inputData['action']=='FSTTDevTable':
            result=F2cm.dft_dbi_fstt_all_hcutable_req(inputData['body'])
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
        elif inputData['action']=='GetDevCali':
            result=F2cm.dft_dbi_get_device_cali(inputData['body'])  
        elif inputData['action']=='SetDevCali':
            result=F2cm.dft_dbi_set_device_cali(inputData['body'])  
        elif inputData['action']=='HCU_CPU_Query':
            result=F2cm.dft_dbi_HCU_CPU_Query(inputData['body'])
        elif inputData['action']=='HCU_CPU_Binding':
            result=F2cm.dft_dbi_HCU_CPU_Binding(inputData['body'])
        elif inputData['action']=='HCUProjectList':
            result=F2cm.dft_dbi_HCU_project_list()
        elif inputData['action']=='HCU_Get_Free_Station':
            result=F2cm.dft_dbi_HCU_Get_Free_Station()
        elif inputData['action']=='HCU_sys_config':
            result=F2cm.dft_dbi_HCU_sys_config(inputData['body'])
        elif inputData['action']=='HCU_sys_config_save':
            result=F2cm.dft_dbi_HCU_sys_config_save(inputData['body'])
        elif inputData['action']=="HCU_Station_Bind":
            result=F2cm.dft_dbi_HCU_Lock_Activate(inputData['body']) 
        elif inputData['action']=="HCU_Get_Binding_Station":
            result=F2cm.dft_dbi_hcu_get_binding_station(inputData['body'])
        elif inputData['action']=="HCU_Station_Unbind":
            result=F2cm.dft_dbi_hcu_station_unbind(inputData['body'])
        elif inputData['action']=="HCU_Loop_Status":
            result=F2cm.dft_dbi_hcu_loop_test(inputData['body'])  
        elif inputData['action']=="GetDevDetail":
            result=F2cm.dft_dbi_get_device_detail(inputData['body']) 
        elif inputData['action']=="HCU_Reboot":
            result=F2cm.dft_dbi_hcu_reboot(inputData['body'])
        elif inputData['action']=="HCU_Start_Loop":
            result=F2cm.dft_dbi_hcu_loop_test_start(inputData['body'])
        elif inputData['action']=="AQYCPointPicture":
            result=F2cm.dft_dbi_aqyc_install_picture_process(inputData['body'])
        elif inputData['action']=="HCU_NGROK":
            result=F2cm.dft_dbi_ngrok_reboot(inputData['body'])
        elif inputData['action']=="HCU_Software_Reboot":
            result=F2cm.dft_dbi_sw_restart(inputData['body'])
        elif inputData['action']=="PointLogin":
            result=F2cm.dft_dbi_fstt_point_login(inputData['body'])
        elif inputData['action']=='GetFreeCpuId':
            result=F2cm.dft_get_free_cpu_id_internal(inputData['body'])
        elif inputData['action']=='GetDeviceDetail':
            result=F2cm.dft_get_device_detail_internal(inputData['body'])
        elif inputData['action']=='SetDevDetail':
            result=F2cm.dft_set_device_detail_internal(inputData['body'])
        elif inputData['action']=='FSTTPointNew':
            result=F2cm.dft_dbi_fstt_site_info_new(inputData['body'])
        elif inputData['action']=='FSTTPointMod':
            result=F2cm.dft_dbi_fstt_site_info_modify(inputData['body'])
        elif inputData['action']=='FSTTDevNew':
            result=F2cm.dft_dbi_fstt_dev_info_new(inputData['body'])
        elif inputData['action']=='FSTTDevMod':
            result=F2cm.dft_dbi_fstt_dev_info_update(inputData['body'])
        
        else:
            result=""
        return result
    
    def dft_F3dm_Send_Message(self,inputData): 
        F3dm=ModDbaF3dm.classDappDbF3dm()
        F3dmHCU=ModDbaF3dm.HCUF3dmDataBaseConfirm()
        if inputData['action']=='MonitorList':
            result=F3dm.dft_dbi_map_active_siteinfo_req(inputData['body'])
        elif inputData['action']=='FSTTMonitorList':
            result=F3dm.dft_dbi_fstt_map_active_siteinfo_req(inputData['body'])
        elif inputData['action']=='FakeMonitorList':
            result=F3dm.dft_dbi_map_inactive_siteinfo_req(inputData['body'])
        elif inputData['action']=='Favourite_list':
            result=F3dm.dft_dbi_favoursite_list_process(inputData['body'])
        elif inputData['action']=='Favourite_count':
            result=F3dm.dft_dbi_favourite_count_process(inputData['body'])
        elif inputData['action']=='GetStaticMonitorTable':
            result=F3dm.dft_dbi_aqyc_user_dataaggregate_req(inputData['body'])
        elif inputData['action']=='FSTTGetStaticMonitorTable':
            result=F3dm.dft_dbi_fstt_user_dataaggregate_req(inputData['body'])
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
        elif inputData['action']=='HCU_Info_Query':
            result=F3dm.dft_dbi_HCU_Info_Query(inputData['body'])
        elif inputData['action']=="CalculationHour":
            result=F3dm.dft_calculation_hour_data()
        else:
            result=""
        return result
    def dft_F4icm_Send_Message(self,inputData): 
        F4icm=ModDbaF4icm.classDappDbF4icm()
        if inputData['action']=='SensorUpdate':
            result=F4icm.dft_dbi_sensor_info_update(inputData['body'])
        elif inputData['action']=='GetVideoCameraWeb':
            result=F4icm.dft_dbi_get_hcu_camweb_link(inputData['body'])
        elif inputData['action']=='FSTTGetVideoCameraWeb':
            result=F4icm.dft_dbi_fstt_get_hcu_camweb_link(inputData['body'])
        elif inputData['action']=='GetVideoList':
            result=F4icm.dft_dbi_hcu_hsmmplist_inquery(inputData['body'])
        elif inputData['action']=='GetCameraStatus':
            result=F4icm.dft_dbi_get_camera_status(inputData['body'])
        elif inputData['action']=='GetThreeCameraStatus':
            result=F4icm.dft_dbi_get_three_camera_status(inputData['body'])
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
        elif inputData['action']=='FSTTDevAlarm':
            result=F5fm.dft_dbi_fstt_dev_currentvalue_req(inputData['body'])
        elif inputData['action']=='AlarmType':
            result=F5fm.dft_dbi_all_alarmtype_req(inputData['body'])
        elif inputData['action']=='AlarmQuery':
            result=F5fm.dft_dbi_aqyc_dev_alarmhistory_req(inputData['body'])
        elif inputData['action']=='AlarmQueryRealtime':
            result=F5fm.dft_dbi_aqyc_dev_alarmhistory_realtime_req(inputData['body'])
        elif inputData['action']=='FSTTAlarmQueryRealtime':
            result=F5fm.dft_dbi_fstt_dev_alarmhistory_realtime_req(inputData['body'])
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
        F10oam=ModDbaF10oam.classDappDbF10oam()
        result=''
        if inputData['action']=="GetZipFileList":
            result=F10oam.dft_dbi_tools_qrcode_filelist(inputData['body'])
        elif inputData['action']=="NewQrcode":
            result=F10oam.dft_dbi_tools_qrcode_newapply(inputData['body'])
        elif inputData['action']=="InsertQrcode":
            result=F10oam.dft_dbi_qrcode_data_insert(inputData['body'])
        elif inputData['action']=="GetSoftwareLoadTable":
            result=F10oam.dft_dbi_tools_swload_table_get(inputData['body'])
        elif inputData['action']=="SoftwareLoadNew":
            result=F10oam.dft_dbi_tools_swload_info_add(inputData['body'])
        elif inputData['action']=="SoftwareLoadDel":
            result=F10oam.dft_dbi_tools_swload_info_delete(inputData['body'])
        elif inputData['action']=="SoftwareLoadStatusChange":
            result=F10oam.dft_dbi_tools_swload_validflag_change(inputData['body'])
        return result
    
    
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
            
        elif inputData['action']=='FAAMSCProcess':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_qrcode_sc_process(inputData['body'])
            
        elif inputData['action']=='FAAMKQProcess':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_qrcode_kq_process(inputData['body'])  
            
        elif inputData['action']=='HuitpXMLMsgUser':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_huitp_xmlmsg_equlable_userlist_report(inputData['body'])  
            
        elif inputData['action']=='HuitpXMLMsgApply':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_huitp_xmlmsg_equlable_apply_report(inputData['body'])  
            
        elif inputData['action']=='SeafoodInfo':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
         
        elif inputData['action']=='SeafoodAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_get_print(inputData['body'])
            
        elif inputData['action']=='QrcodeAudit':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_qrcode_audit(inputData['body'])
        elif inputData['action']=='QrcodeBatch':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_qrcode_batch(inputData['body'])
        else:
            result=''
        return result
    
    def dft_Fxprcm_Send_Message(self,inputData): 
        Fxprcm=ModDbaFxprcm.classDappDbFxprcm()
        if inputData['action']=='GetNeonStatus':
            result=Fxprcm.dft_dbi_fstt_get_neno_status(inputData['body'])
        elif inputData['action']=='SetNeonStatus':
            result=Fxprcm.dft_dbi_fstt_set_neon_status(inputData['body'])
        else:
            result=""
        return result
    
    def dft_Snr_Send_Message(self,inputData): 
        if inputData['action']=='AQYCOldDataClear':
            L2snr=ModDbaSnr.classDappDbSnr()
            result=L2snr.dft_aqyc_old_data_clear(inputData['body'])
        elif inputData['action']=='FAAMOldDataClear':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_faam_old_data_clear(inputData['body'])
        elif inputData['action']=='FAAMDataSta':
            F11Faam=ModDbaF11Faam.ClassDbaF11Faam()
            result=F11Faam.dft_cron_production_and_batch_table_sta()
        else:
            result=""
        return result

    def dft_cebs_msg_process_env(self, inputData):
        if inputData['cmd']=='add':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_env_add(inputData)
        elif inputData['cmd']=='read':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_env_read(inputData)
        elif inputData['cmd']=='modify':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_env_modify(inputData)
        elif inputData['cmd']=='delete':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_env_delete(inputData)
        else:
            result= {'res':False, 'reason':'not exist command'}
        return result

    def dft_cebs_msg_process_counter(self, inputData):
        if inputData['cmd']=='add':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_counter_add(inputData)
        elif inputData['cmd']=='read':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_counter_read(inputData)
        elif inputData['cmd']=='modify':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_env_modify(inputData)
        elif inputData['cmd']=='delete':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_counter_delete(inputData)
        else:
            result= {'res':False, 'reason':'not exist command'}
        return result

    def dft_cebs_msg_process_fspc(self, inputData):
        if inputData['cmd']=='add':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_fspc_add(inputData)
        elif inputData['cmd']=='read':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_fspc_read(inputData)
        elif inputData['cmd']=='modify':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_fspc_modify(inputData)
        elif inputData['cmd']=='delete':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_fspc_delete(inputData)
        else:
            result= {'res':False, 'reason':'not exist command'}
        return result

    def dft_cebs_msg_process_file(self, inputData):
        if inputData['cmd']=='add':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_file_add(inputData)
        elif inputData['cmd']=='read':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_file_read(inputData)
        elif inputData['cmd']=='modify':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_file_modify(inputData)
        elif inputData['cmd']=='delete':
            dbaCebsObj = ModDbaCebs.ClassDbaCebs()
            result=dbaCebsObj.dft_dbi_file_delete(inputData)
        else:
            result= {'res':False, 'reason':'not exist command'}
        return result












#HCU    
class ClassHCUDbaMainEntry():
    def dft_F2cm_Send_Message(self,socketId,inputData): 
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_response_HCU_data(socketId,inputData)
        return result
    
    def dft_F2cm_Heart_Data_Report(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_device_heart_report_data(socketId, inputData)
        return result
    
    def dft_dbi_device_reboot(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_device_reboot(socketId,inputData)
        return result
    def dft_F2cm_Device_Loop_Test(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_device_loop_test(socketId, inputData)
        return result
    
    def dft_F2cm_Ngrok_Restart_Test(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_ngrok_restart(socketId, inputData)
        return result
    
    def dft_F2cm_Hcu_Sw_Restart_Test(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_hcu_sw_restart(socketId, inputData)
        return result
    
    def dft_F2cm_Smart_City_Ctrl_Resp(self,socketId,inputData):
        F2cm=ModDbaF2cm.HCUF2cmDataBaseConfirm()
        result=F2cm.dft_dbi_smart_city_ctrl_resp(socketId, inputData)
        return result
    
    def dft_F3dm_Data_Current_Report(self,socketId,inputData):
        F3dm=ModDbaF3dm.HCUF3dmDataBaseConfirm()
        FrUsr=inputData['FrUsr']
        ToUsr=inputData["ToUsr"]
        dev_code=FrUsr.split("_")
        if dev_code[2]=="AQYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2400ZNXX":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2008SHYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2012NALT":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G1400FSTT":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2008FSTT":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2013SHYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2014SHYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2012SHYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2012SHYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2015XCYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        elif dev_code[1]=="G2013XCYC":
            Msg=F3dm.dft_dbi_aqyc_current_report(socketId, inputData)
            return Msg
        else:
            result={'socketid':socketId,'data':{'ToUsr':FrUsr,'FrUsr':ToUsr,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId': GOLBALVAR.HUITPJSON_MSGID_YCDATACONFIRM,'MsgLn':115,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
            msg_len=len(json.dumps(result))
            Msg_final={'socketid':socketId,'data':{'ToUsr':FrUsr,'FrUsr':ToUsr,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':GOLBALVAR.HUITPJSON_MSGID_YCDATACONFIRM,'MsgLn':msg_len,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
            return Msg_final
    
    def dft_F3dm_smart_city_current_report(self,socketId,inputData):
        F3dm=ModDbaF3dm.HCUF3dmDataBaseConfirm()
        Msg=F3dm.dft_dbi_smart_city_current_report(socketId, inputData)
        return Msg
    
    def dft_F6pm_HCU_Perform_Data_Report(self,socketId,inputData):
        F6pm=ModDbaF6pm.Msg_From_HCU_Report()
        result=F6pm.dft_dbi_accept_performance_table_report(socketId, inputData)
        return result
    
    def dft_F10oam_HCU_Inventory_Report(self,socketId,inputData):
        F10oam=ModDbaF10oam.classDappDbF10oam()
        result=F10oam.dft_dbi_hcu_inventory_confirm(socketId, inputData)
        return result
    

    
            
    
        