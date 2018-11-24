# -*- coding: utf-8 -*-
'''
Created on 2018年11月24日

@author: Administrator
'''
import time
import os,sys
import pymysql
import django
import datetime
# sys.path.append('C:\wamp\www\huicloud\DjoSiteDba')
sys.path.append('/var/www/html/huicloud/DjoSiteDba')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
django.setup()
from DappDbF1sym.models import dct_t_l3f1sym_menu_code_mapping,dct_t_l3f1sym_user_right_action,dct_t_l3f1sym_user_right_menu,dct_t_l3f1sym_account_primary,dct_t_l3f1sym_account_secondary
from DappDbF1sym import views
from DappDbF11faam.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbF10oam.models import *
from DappDbSnr.models import *
a={
    'webauth':{
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
    "MaterialAudit":0X0A0B,
    "MaterialCheckIn":0X0A0C,
    "MaterialPurchaseDetail":0X0A0D,
    "OtherStorageCheckIn":0X0A0E,
    "MaterialTransfer":0X0A0F,
    "MaterialSale":0X0A10,
    "MaterialConsume":0X0A11,
    "MaterialConsumeBack":0X0A12,
    "DepositaryCheckIn":0X0A13,
    "DepositaryCheckOut":0X0A14,
    "ProductStorageManage":0X0A15,
    "ProductDeliveryManage":0X0A16,
    "ProductWasteDeliver":0X0A17,
    "ContainerStorageManage":0X0A18,
    "ContainerCheckOut":0X0A19,
    "ContainerCheckIn":0X0A20,
    "ContainerSaleBack":0X0A21,
    "ContainerTransferBack":0X0A22,
    "ContainerOtherStorageRefund":0X0A23,
    "SeafoodInfo":0X0A24,
    "SeafoodAudit":0X0A25,
    "QrcodeAudit":0X0A26,
    "QrcodeBatch":0X0A27,
    },
'actionauth':{
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
    'GetPGNum':0X0207,
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
    'GetDevCali':0X02AD,
    'SetDevCali':0X02AE,
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
    'FactoryCodeList':0X0A01,
    'FactoryTable':0X0A02,
    'FactoryMod':0X0A03,
    'FactoryNew':0X0A04,
    'FactoryDel':0X0A05,
    'SpecificationTable':0X0A06,
    'SpecificationMod':0X0A07,
    'SpecificationNew':0X0A08,
    'SpecificationDel':0X0A09,
    'StaffnameList':0X0A0A,
    'StaffTable':0X0A0B,
    'StaffNew':0X0A0C,
    'StaffMod':0X0A0D,
    'StaffDel':0X0A0E,
    'AttendanceHistory':0X0A0F,
    'AttendanceNew':0X0A10,
    'AttendanceBatchNew':0X0A11,
    'AttendanceDel':0X0A12,
    'GetAttendance':0X0A13,
    'AttendanceMod':0X0A14,
    'AttendanceAudit':0X0A15,
    'AssembleHistory':0X0A16,
    'AssembleAudit':0X0A17,
    'KPIAudit':0X0A18,
    'ConsumablesPurchaseNew':0X0A19,
    'ConsumablesTable':0X0A1A,
    'ConsumablesHistory':0X0A1B,
    'GetConsumablesPurchase':0X0A1C,
    'ConsumablesPurchaseMod':0X0A1D,
    'ConsumablesPurchaseDel':0X0A1E,
    'ProductStockNew':0X0A1F,
    'GetProductWeightAndSize':0X0A20,
    'GetProductStockList':0X0A21,
    'GetProductEmptyStock':0X0A22,
    'ProductStockTable':0X0A23,
    'ProductStockDel':0X0A24,
    'GetProductStockDetail':0X0A25,
    'ProductStockTransfer':0X0A26,
    'ProductStockHistory':0X0A27,
    'MaterialStockNew':0X0A28,
    'GetMaterialStockList':0X0A29,
    'GetMaterialEmptyStock':0X0A2A,
    'MaterialStockDel':0X0A2B,
    'MaterialStockTable':0X0A2C,
    'GetMaterialStockDetail':0X0A2D,
    'MaterialStockIncomeNew':0X0A2E,
    'MaterialStockRemovalNew':0X0A2F,
    'MaterialStockHistory':0X0A30,
    'GetMaterialStockHistoryDetail':0X0A31,
    'MaterialStockIncomeMod':0X0A32,
    'MaterialStockRemovalMod':0X0A33,
    'MaterialStockRemovalDel':0X0A34,
    'GetProductStockHistoryDetail':0X0A35,
    'ProductStockRemovalMod':0X0A36,
    'ProductStockRemovalDel':0X0A37,
    'ProductStockRemovalNew':0X0A38,
    'GetPrint':0X0A39,
    'GetConsumablesVendorList':0X0A3A,
    'GetConsumablesTypeList':0X0A3B,
    'TableQuery':0X0A3C,
    'QrcodeBatch':0X0A3D,
    'QrcodeAudit':0X0A3E,
    #水产管理
    'SeafoodInfo':0X0B01,
    'SeafoodAudit':0X0B02,
    
    #FXPRCM
    'PointMaintenanceList':0X0C01,
    'RepairNew':0X0C02,
    'GetNeonStatus':0X0C03,
    'SetNeonStatus':0X0C04,
    },
}
def update_menu_and_action():
    for key,value in a['webauth'].items():
        result=dct_t_l3f1sym_menu_code_mapping.objects.filter(menu_name=key)
        if result.exists():
            pass
        else:
            dct_t_l3f1sym_menu_code_mapping.objects.create(menu_name=key,menu_code=value)
        result=dct_t_l3f1sym_user_right_menu.objects.filter(menu_name=key,menu_group=1)
        if result.exists():
            pass
        else:
            dct_t_l3f1sym_user_right_menu.objects.create(menu_group=1,menu_name=key,menu_code_id=value)
    for key,value in a['actionauth'].items():
        result=dct_t_l3f1sym_user_right_action.objects.filter(action_name=key)
        if result.exists():
            pass
        else:
            dct_t_l3f1sym_user_right_action.objects.create(action_name=key,action_code=value,l1_auth=True)
def clear_menu_and_action():
    dct_t_l3f1sym_menu_code_mapping.objects.filter().delete()
    dct_t_l3f1sym_user_right_menu.objects.filter().delete()
    dct_t_l3f1sym_user_right_action.objects.filter().delete()
def group_2_menu():
    menu=list()
    for key,value in a['webauth'].items():
        if key=="menu_user_profile":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2,menu_name=key,menu_code_id=value))
        elif key=="UserManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="PGManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="ProjManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="MPManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="DevManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="MPMonitor":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="MPStaticMonitorTable":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        elif key=="WarningHandle":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=2,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        else:
            pass
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
    dct_t_l3f1sym_user_right_menu.objects.bulk_create(menu)
def group_3_menu():
    menu=list()
    for key,value in a['webauth'].items():
        if key=="menu_user_profile":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3,menu_name=key,menu_code_id=value))
        elif key=="UserManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        # if key=="PGManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="ProjManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="MPManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="DevManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="MPMonitor":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="MPStaticMonitorTable":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        elif key=="WarningHandle":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=3,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=3, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        else:
            pass
    dct_t_l3f1sym_user_right_menu.objects.bulk_create(menu)
def group_4_menu():
    menu=list()
    for key,value in a['webauth'].items():
        if key=="StaffManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4,menu_name=key,menu_code_id=value))
        elif key=="AttendanceManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="FactoryManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="SpecificationManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="AssembleManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="AssembleAudit":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="AttendanceAudit":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="KPIAudit":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="ConsumablesManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))
        elif key=="ConsumablesHistory":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=4,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=4, menu_name=key, menu_code_id=value))

        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        else:
            pass
    dct_t_l3f1sym_user_right_menu.objects.bulk_create(menu)
def group_5_menu():
    menu=list()
    for key,value in a['webauth'].items():
        if key=="StaffManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=5,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=5,menu_name=key,menu_code_id=value))
        elif key=="AttendanceManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=5,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=5, menu_name=key, menu_code_id=value))
        elif key=="FactoryManage":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=5,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=5, menu_name=key, menu_code_id=value))
        elif key=="AssembleAudit":
            if (dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=5,menu_name=key)):
                pass
            else:
                menu.append(dct_t_l3f1sym_user_right_menu(menu_group=5, menu_name=key, menu_code_id=value))
        # if key=="MPManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="DevManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="MPMonitor":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="MPStaticMonitorTable":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="WarningHandle":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        # if key=="UserManage":
        #     menu.append(dct_t_l3f1sym_user_right_menu(menu_group=2, menu_name=key, menu_code_id=value))
        else:
            pass
    dct_t_l3f1sym_user_right_menu.objects.bulk_create(menu)
def action_2_3_4_5_update():
    for key,values in a['actionauth'].items():
        if key=='login':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='Get_user_auth_code':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='Reset_password':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='UserInfo':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1)
        elif key=='UserNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1)
        elif key=='UserMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='UserDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key=='UserTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='PGNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='PGMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='PGDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key=='PGTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='PGProj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='ProjectPGList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='ProjectList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='UserProj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='ProjTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='ProjPoint':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='ProjNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1)
        elif key=='ProjMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='ProjDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='PointProj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='PointTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='PointNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1)
        elif key=='PointMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='PointDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key=='PointDev':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='DevTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1,l5_auth=1)
        elif key=='DevNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1,l4_auth=1)
        elif key=='DevMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1,l3_auth=1)
        elif key=='DevDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'GetStationActiveInfo':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'StationActive':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'TableQuery':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductModel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'PointConf':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'PointLogin':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'UserKey':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'ProjKeyList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'ProjKey':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'ProjUserList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'DomainAuthlist':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyAuthlist':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyGrant':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyAuthNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'KeyAuthDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'GetDevCali':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SetDevCali':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'DevSensor':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'SensorList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'MonitorList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'FakeMonitorList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'Favourite_list':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'Favourite_count':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetStaticMonitorTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'PointPicture':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'KeyHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'GetOpenImg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'SensorUpdate':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetVideoCameraWeb':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetVideoList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetVideo':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetCameraStatus':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetCameraUnit':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'CameraVAdj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'CameraHAdj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'CameraZAdj':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'CameraReset':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'OpenLock':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'MonitorAlarmList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'DevAlarm':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'AlarmType':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'AlarmQuery':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'AlarmQueryRealtime':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetWarningHandleListTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetWarningImg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'AlarmHandle':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AlarmClose':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetHistoryRTSP':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'GetAuditStabilityTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'SetUserMsg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'GetUserMsg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'ShowUserMsg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'GetUserImg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
                                                                                   l5_auth=1)
        elif key == 'ClearUserImg':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'FactoryCodeList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'FactoryTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'FactoryMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'FactoryNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'FactoryDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SpecificationTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SpecificationMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SpecificationNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SpecificationDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'StaffnameList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'StaffTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'StaffNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'StaffMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'StaffDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'AttendanceHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AttendanceNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AttendanceBatchNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AttendanceDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetAttendance':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AttendanceMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AttendanceAudit':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AssembleHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'AssembleAudit':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'KPIAudit':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ConsumablesPurchaseNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ConsumablesTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ConsumablesHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetConsumablesPurchase':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ConsumablesPurchaseMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ConsumablesPurchaseDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetProductWeightAndSize':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetProductStockList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetProductEmptyStock':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetProductStockDetail':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockTransfer':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetMaterialStockList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetMaterialEmptyStock':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockTable':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetMaterialStockDetail':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockIncomeNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockRemovalNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockHistory':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetMaterialStockHistoryDetail':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockIncomeMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockRemovalMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'MaterialStockRemovalDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetProductStockHistoryDetail':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockRemovalMod':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockRemovalDel':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'ProductStockRemovalNew':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetPrint':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetConsumablesVendorList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'GetConsumablesTypeList':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'F11TableQuery':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1)
        elif key == 'SeafoodInfo':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        elif key == 'SeafoodAudit':
            dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        # elif key == 'login':
        #     dct_t_l3f1sym_user_right_action.objects.filter(action_name=key).update(l2_auth=1, l3_auth=1, l4_auth=1,
        #                                                                            l5_auth=1)
        else:
            pass



if __name__=="__main__":
    group_2_menu()
    group_3_menu()
    group_4_menu()
    group_5_menu()
    action_2_3_4_5_update()