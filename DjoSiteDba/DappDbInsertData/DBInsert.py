# -*- coding: utf-8 -*-
'''
Created on 2018年7月12日

@author: Administrator
'''

import os
os.environ['DJANGO_SETTINGS_MODULE']='DjoSiteDba.settings'
import django
django.setup()
from DappDbF1sym.models import dct_t_l3f1sym_menu_code_mapping,dct_t_l3f1sym_user_right_action,dct_t_l3f1sym_user_right_menu,dct_t_l3f1sym_account_primary,dct_t_l3f1sym_account_secondary
from DappDbF1sym import views
faam1={
    'menu':{
        #FUM1SYM
        'menu_user_profile':0X0101,
        'UserManage':0X0102,
        'ParaManage':0X0103,
        'ExportTableManage':0X0104,
        'SoftwareLoadManage':0X0105,

        #FUM2CM
        'PGManage':0X0201,
        'ProjManage':0X0202,
        'MPManage':0X0203,
        'DevManage':0X0204,
        'KeyManage':0X0205,
        'KeyAuth':0X0206,
        'KeyHistory':0X0207,

        #FUM3DM
        'MPMonitor':0X0301,
        'MPStaticMonitorTable':0X0302,
        'MPMonitorCard':0X0303,

        #FUM4ICM
        'InstConf':0X0401,
        'InstRead':0X0402,
        'InstDesign':0X0403,
        'InstControl':0X0404,
        'InstSnapshot':0X0405,
        'InstVideo':0X0406,

        #FUM5FM
        'WarningCheck':0X0501,
        'WarningHandle':0X0502,
        'WarningLimit':0X0503,

        #FUM6PM
        'AuditTarget':0X0601,
        'AuditStability':0X0602,
        'AuditAvailability':0X0603,
        'AuditError':0X0604,
        'AuditQuality':0X0605,

        #FUM6ADS
        'ADConf':0X0701,
        'ADManage':0X0702,
        "WEBConf":0X0703,

        #FUM8PSM

        #FUM9GISM
        'GeoInfoQuery':0X0901,
        'GeoTrendAnalysis':0X0902,
        'GeoDisaterForecast':0X0903,
        'GeoEmergencyDirect':0X0904,
        'GeoDiffusionAnalysis':0X0905,

        #FUM11FAAM
        'StaffManage':0X0A01,
        'AttendanceManage':0X0A02,
        'FactoryManage':0X0A03,
        'SpecificationManage':0X0A04,
        'AssembleManage':0X0A05,
        'AssembleAudit':0X0A06,
        'AttendanceAudit':0X0A07,
        'KPIAudit':0X0A08,
        'ConsumablesManage':0X0A09,
        'ConsumablesHistory':0X0A0A,
        'ProductStorageManage':0X0A0B,
        'ProductDeliveryManage':0X0A0C,
        'MaterialStorageManage':0X0A0D,
        'MaterialDeliveryManage':0X0A0E,
        'SeafoodInfo':0X0A0F,
        'SeafoodAudit':0X0A10,
        },
    'action':{
        #FUM1SYM
        'login':0X0101,
        'Get_user_auth_code':0X0102,
        'Reset_password':0X0103,
        'UserInfo':0X0120,
        'UserNew':0X0121,
        'UserMod':0X0122,
        'UserDel':0X0123,
        'UserTable':0X0124,
        #FUM2CM
        'PGNew':0X0201,
        'PGMod':0X0202,
        'PGDel':0X0203,
        'PGTable':0X0204,
        'PGProj':0X0205,
        'ProjectPGList':0X0206,
        'ProjectList':0X0220,
        'UserProj':0X0221,
        'ProjTable':0X0222,
        'ProjPoint':0X0223,
        'ProjNew':0X0224,
        'ProjMod':0X0225,
        'ProjDel':0X0226,
        'PointProj':0X0240,
        'PointTable':0X0241,
        'PointNew':0X0242,
        'PointMod':0X0243,
        'PointDel':0X0244,
        'PointDev':0X0245,
        'DevTable':0X0260,
        'DevNew':0X0261,
        'DevMod':0X0262,
        'DevDel':0X0263,
        'GetStationActiveInfo':0X0264,
        'StationActive':0X0265,
        'TableQuery':0X0266,
        'ProductModel':0X0267,
        'PointConf':0X0268,
        'PointLogin':0X0269,
        'UserKey':0X02A0,
        'ProjKeyList':0X02A1,
        'ProjKey':0X02A2,
        'ProjUserList':0X02A3,
        'KeyTable':0X02A4,
        'KeyNew':0X02A5,
        'KeyMod':0X02A6,
        'KeyDel':0X02A7,
        'DomainAuthlist':0X02A8,
        'KeyAuthlist':0X02A9,
        'KeyGrant':0X02AA,
        'KeyAuthNew':0X02AB,
        'KeyAuthDel':0X02AC,
        #FUM3DMA
        'DevSensor':0X0301,
        'SensorList':0X0302,
        'MonitorList':0X0303,
        'FakeMonitorList':0X0304,
        'Favourite_list':0X0305,
        'Favourite_count':0X0306,
        'GetStaticMonitorTable':0X0307,
        'PointPicture':0X0308,
        'KeyHistory':0X0320,
        'GetOpenImg':0X0321,
        #FUM4ICM
        'SensorUpdate':0X0401,
        'GetVideoCameraWeb':0X0402,
        'GetVideoList':0X0403,
        'GetVideo':0X0404,
        'GetCameraStatus':0X0405,
        'GetCameraUnit':0X0406,
        'CameraVAdj':0X0407,
        'CameraHAdj':0X0408,
        'CameraZAdj':0X0409,
        'CameraReset':0X040A,
        'GetCameraStatus':0X040B,
        'OpenLock':0X040C,
        #FUM5FM
        'MonitorAlarmList':0x0501,
        'DevAlarm':0x0502,
        'AlarmType':0x0503,
        'AlarmQuery':0x0504,
        'AlarmQueryRealtime':0x0505,
        'GetWarningHandleListTable':0x0506,
        'GetWarningImg':0x0507,
        'AlarmHandle':0x0508,
        'AlarmClose':0x0509,
        'GetHistoryRTSP':0x050A,
        #FUM6PM
        'GetAuditStabilityTable':0x0601,
        #FUM7ADS
        'SetUserMsg':0X0701,
        'GetUserMsg':0X0702,
        'ShowUserMsg':0X0703,
        'GetUserImg':0X0704,
        'ClearUserImg':0X0705,
        #FUM11FAAM
        'AttendanceAudit':0x0A01,
        'AttendanceMod':0x0A02,
        'KPIAudit':0x0A03,
        'StaffDel':0x0A04,
        'ConsumablesPurchaseNew':0x0A05,
        'ConsumablesTable':0x0A06,
        'ConsumablesHistory':0x0A07,
        'GetConsumablesPurchase':0x0A08,
        'ConsumablesPurchaseMod':0x0A09,
        'ConsumablesPurchaseDel':0x0A0A,
        'ProductStockNew':0x0A0B,
        'GetProductWeightAndSize':0x0A0C,
        'GetProductStockList':0x0A0D,
        'GetProductEmptyStock':0x0A0E,
        'ProductStockTable':0x0A0F,
        'ProductStockDel':0x0A10,
        'GetProductStockDetail':0x0A11,
        'ProductStockTransfer':0x0A12,
        'ProductStockHistory':0x0A13,
        'MaterialStockNew':0x0A14,
        'GetMaterialStockList':0x0A15,
        'GetMaterialEmptyStock':0x0A16,
        'MaterialStockDel':0x0A17,
        'MaterialStockTable':0x0A18,
        'GetMaterialStockDetail':0x0A19,
        'MaterialStockIncomeNew':0x0A1A,
        'MaterialStockRemovalNew':0x0A1B,
        'MaterialStockHistory':0x0A1C,
        'GetMaterialStockHistoryDetail':0x0A1D,
        'MaterialStockIncomeMod':0x0A1E,
        'MaterialStockRemovalMod':0x0A1F,
        'MaterialStockRemovalDel':0x0A20,
        'GetProductStockHistoryDetail':0x0A21,
        'ProductStockRemovalMod':0x0A22,
        'ProductStockRemovalDel':0x0A23,
        'ProductStockRemovalNew':0x0A24,
        'TableQuery':0X0A25,
        'SeafoodInfo':0x0A30,
        'SeafoodAudit':0x0A31,
        },
    }
def insert_menu_code_mapping():
    for key,value in faam1['menu'].items():
        result=dct_t_l3f1sym_menu_code_mapping(menu_code=value,menu_name=key)
        result.save()
    return 
def delete_menu_code_mapping():
    dct_t_l3f1sym_menu_code_mapping.objects.filter().delete()
def insert_action_menu():
    i=0
    for key,value in faam1['action'].items():
        print(str(key)+'\t'+str(value)+'\t'+str(i))
        i=i+1
        result=dct_t_l3f1sym_user_right_action.objects.get(action_code=value)
        if result:
            print(key+'is exited')
        else:
            create=dct_t_l3f1sym_user_right_action(action_code=value,action_name=key,l1_auth=True,l2_auth=False,l3_auth=False,l4_auth=False,l5_auth=False)
            create.save()
def insert_right_menu():
    for key,value in faam1['menu'].items():
        menu=dct_t_l3f1sym_menu_code_mapping.objects.get(menu_code=value)
        right_menu=dct_t_l3f1sym_user_right_menu(menu_group=0X0001,menu_code=menu,menu_name=key)
        right_menu.save()
def select_menu():
    result = dct_t_l3f1sym_user_right_action.objects.filter(l1_auth=1)
    for i in range(200):
        if result[i]:
            print(result[i].action_name)
        else:
            print('Error')
        
def select_user():
    s='MFUN_WORKING_PROGRAM_NAME_UNIQUE_NBIOT_AGC'
    if s in faam1['group'].keys():
        print('true')
    else:
        print('false')
def show_menu():
    for i in faam1['group'].keys():
        print(i)
if __name__=="__main__":
    insert_action_menu()