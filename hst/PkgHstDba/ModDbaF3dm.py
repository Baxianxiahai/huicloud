# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

@author: Administrator
'''

import sys
import os,time
import django
import json
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbF3dm import views as DappDbF3dm
from DappDbSnr import views as DappDbSnr
from django.db import transaction
from PkgAccessEntry.ModAccessDict import *
class classDappDbF3dm:
    def __init__(self):
        pass
    def dft_dbi_map_active_siteinfo_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_map_active_siteinfo_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_map_inactive_siteinfo_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_map_inactive_siteinfo_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_favoursite_list_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_favoursite_list_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_favourite_count_process(self,inputData):
        try:
            with transaction.atomic():
                DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
                DappDbF3dm_view.dft_dbi_favourite_count_process(inputData)
                result=True
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_all_sensorlist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbSnr_view=DappDbSnr.dct_classDappDbSnr()
        result=DappDbSnr_view.dft_dbi_all_sensorlist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_dev_sensorinfo_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbSnr_view=DappDbSnr.dct_classDappDbSnr()
        result=DappDbSnr_view.dft_dbi_aqyc_dev_sensorinfo_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_aqyc_user_dataaggregate_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_aqyc_user_dataaggregate_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_bfsc_user_dataaggregate_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_bfsc_user_dataaggregate_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_sensorlist_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbSnr_view=DappDbSnr.dct_classDappDbSnr()
        result=DappDbSnr_view.dft_dbi_all_sensorlist_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_dev_sensorinfo_req(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbSnr_view=DappDbSnr.dct_classDappDbSnr()
        result=DappDbSnr_view.dft_dbi_aqyc_dev_sensorinfo_req(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_fhys_user_dataaggregate_req(self,inputData):
        try:
            with transaction.atomic():
                DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
                result=DappDbF3dm_view.dft_dbi_fhys_user_dataaggregate_req(inputData)
        except Exception:
            result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_key_event_history_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_key_event_history_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_door_open_picture_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_door_open_picture_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    def dft_dbi_point_install_picture_process(self,inputData):
#         try:
#             with transaction.atomic():
        DappDbF3dm_view=DappDbF3dm.dct_classDbiL3apF3dm()
        result=DappDbF3dm_view.dft_dbi_point_install_picture_process(inputData)
#         except Exception:
#             result={"body":{"status":"true","auth":"false","admin":"false"},"msg":"数据库发生错误，请重试"}
        return result
    
    
class HCUF3dmDataBaseConfirm():
    def __init__(self):
        pass
    
    def dft_dbi_aqyc_current_report(self,socketId,inputData):
        try:
            with transaction.atomic():
                DappDbF3dm_view=DappDbF3dm.dct_t_HCU_Data_Report()
                result=DappDbF3dm_view.dft_dbi_aqyc_current_report(socketId, inputData)
        except Exception:
            result={'socketid':socketId,'data':{'ToUsr':"",'FrUsr':"","CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':GOLBALVAR.HUITPJSON_MSGID_YCDATACONFIRM,'MsgLn':115,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
            msg_len=len(json.dumps(result))
            result={'socketid':socketId,'data':{'ToUsr':"",'FrUsr':"","CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':GOLBALVAR.HUITPJSON_MSGID_YCDATACONFIRM,'MsgLn':msg_len,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
        return result
    
    def dft_dbi_HCU_Info_Query(self,inputData):
        try:
            with transaction.atomic():
                DappDbF3dm_view=DappDbF3dm.dct_t_HCU_Data_Report()
                result=DappDbF3dm_view.dft_dbi_HCU_Info_Query(inputData)
        except Exception:
            result={'status':'true','auth':'true','msg':'获取设备状态失败','ret':[]}
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    