# -*- coding: utf-8 -*-
'''
Created on 2018年7月12日

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
from DappDbF2cm.models import dct_t_l3f2cm_device_inventory
from DappDbF3dm.models import *
faam1={
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
        'ProductStorageManage':0X0A0B,
        'ProductDeliveryManage':0X0A0C,
        'MaterialStorageManage':0X0A0D,
        'MaterialDeliveryManage':0X0A0E,
        'SeafoodInfo':0X0A0F,
        'SeafoodAudit':0X0A10,
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
        'F2TableQuery':0X0266,
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
        'F11TableQuery':0X0A3C,
        #水产管理
        'SeafoodInfo':0X0B01,
        'SeafoodAudit':0X0B02,
        },
    }
def insert_menu_code_mapping():
    for key,value in faam1['webauth'].items():
        result=dct_t_l3f1sym_menu_code_mapping(menu_code=value,menu_name=key)
        result.save()
    return 
def delete_menu_code_mapping():
    dct_t_l3f1sym_menu_code_mapping.objects.filter().delete()
def insert_action_menu():
    for key,value in faam1['actionauth'].items():
        result=dct_t_l3f1sym_user_right_action.objects.filter(action_code=value)
        if result.exists():
            print(key+' is exited')
        else:
            create=dct_t_l3f1sym_user_right_action(action_code=value,action_name=key,l1_auth=True,l2_auth=False,l3_auth=False,l4_auth=False,l5_auth=False)
            create.save()
def insert_right_menu():
    for key,value in faam1['webauth'].items():
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
            
def dft_select_menu():
    result=dct_t_l3f1sym_user_right_menu.objects.filter(menu_code_id=257)
    if result.exists():
        for line in result:
            print(line.sid)
            print(line.menu_group)
            print(line.menu_name)
            print(line.menu_code_id)
def select_user():
    s='MFUN_WORKING_PROGRAM_NAME_UNIQUE_NBIOT_AGC'
    if s in faam1['group'].keys():
        print('true')
    else:
        print('false')
def show_menu():
    for i in faam1['group'].keys():
        print(i)
        
def insert_type():
    db=pymysql.connect(host='127.0.0.1',user='root',password='xiaohui@naxian',database='bxxhl1l2l3',charset='utf8')
#     db=pymysql.connect('127.0.0.1','root','bxxhbxxh','bxxhl1l2l3')
    cursor=db.cursor()
    sql='SELECT * FROM t_l3f11faam_typesheet'
    cursor.execute(sql)
    results=cursor.fetchall()
    i=0
    for row in results:
        i=i+1
        if dct_t_l3f11faam_type_sheet.objects.filter(typecode=row[2]).exists():
            print(row[2]+"IS EXIST")
        else:
            dct_t_l3f11faam_type_sheet.objects.create(sid=i,pjcode=row[1],typecode=row[2],applenum=row[3],appleweight=row[4],applegrade=row[5],memo=row[6])
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        
def type_del():
    dct_t_l3f11faam_type_sheet.objects.all().delete()
def show_type():
    db=pymysql.connect(host='127.0.0.1',user='root',password='xiaohui@naxian',database='bxxhl1l2l3',charset='utf8')
#     db=pymysql.connect(host='127.0.0.1',user='root',password='bxxhbxxh',database='bxxhl1l2l3',charset='utf8')
    cursor=db.cursor()
    sql='SELECT * FROM t_l3f11faam_typesheet'
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

def insert_factory():
    db=pymysql.connect('127.0.0.1','root','bxxhbxxh','bxxhl1l2l3')
    cursor=db.cursor()
    sql='SELECT * FROM t_l3f11faam_factorysheet'
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        if dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=row[1]).exists():
            pass
        else:
            print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
            #dct_t_l3f11faam_factory_sheet.objects.create(pjcode=row[1],workstart=row[2],workend=row[3],reststart=row[4],restend=row[5],fullwork=row[6],address=row[7],latitude=row[8],longitude=row[9],trafficmoney=row[10],factorybonus=row[11],memo=row[12])
def insert_dev_inventory(dev_code):
    result = dct_t_l3f2cm_device_inventory.objects.all()
    if result.exists():
        for line in result:
            base_port = line.base_port
    resp = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_code)
    if resp.exists():
        print(dev_code + "is exist")
    else:
        dct_t_l3f2cm_device_inventory.objects.create(dev_code=dev_code,
                                                     valid_flag=True,
                                                     create_date=datetime.date.today(),
                                                     hw_type=result[0].hw_type,
                                                     sw_ver=result[0].sw_ver,
                                                     zhb_label=result[0].zhb_label,
                                                     upgradeflag=result[0].upgradeflag,
                                                     rebootflag=result[0].rebootflag,
                                                     base_port=base_port + 1,
                                                     dust_coefmax=result[0].dust_coefmax,
                                                     dust_coefmin=result[0].dust_coefmin,
                                                     dust_coefK=result[0].dust_coefK,
                                                     dust_coefB=result[0].dust_coefB,
                                                     dust_threshold=result[0].dust_threshold,
                                                     temp_coefmax=result[0].temp_coefmax,
                                                     temp_coefmin=result[0].temp_coefmin,
                                                     temp_coefK=result[0].temp_coefK,
                                                     temp_coefB=result[0].temp_coefB,
                                                     humid_coefmax=result[0].humid_coefmax,
                                                     humid_coefmin=result[0].humid_coefmin,
                                                     humid_coefK=result[0].humid_coefK,
                                                     humid_coefB=result[0].humid_coefB,
                                                     noise_coefmax=result[0].noise_coefmax,
                                                     noise_coefmin=result[0].noise_coefmin,
                                                     noise_coefK=result[0].noise_coefK,
                                                     noise_coefB=result[0].noise_coefB,
                                                     windspd_coefmax=result[0].windspd_coefmax,
                                                     windspd_coefmin=result[0].windspd_coefmin,
                                                     windspd_coefK=result[0].windspd_coefK,
                                                     windspd_coefB=result[0].windspd_coefB,
                                                     winddir_coefmax=result[0].winddir_coefmax,
                                                     winddir_coefmin=result[0].winddir_coefmin,
                                                     winddir_coefB=result[0].winddir_coefB,
                                                     winddir_delta=result[0].winddir_delta
                                                     )
def hcu_update(oldDev,newDev,base_Port):
    dct_t_l3f2cm_device_inventory.objects.filter(dev_code=oldDev).update(dev_code=newDev,base_port=base_Port)
def hcu_delete(dev_Code):
    dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_Code).delete()
    print(dev_Code+" is delete")
def hcu_update_hw_type(hw_type):
    dct_t_l3f2cm_device_inventory.objects.filter(dev_code__icontains=str(hw_type)).update(hw_type=hw_type)

def insert_old_hcu_data():
    old_hcu = [
        'HCU_G201_AQYC_SH015',
        'HCU_G201_AQYC_SH016',
        'HCU_G201_AQYC_SH017',
        'HCU_G201_AQYC_SH050',
        'HCU_G201_AQYC_SH051',
        'HCU_G201_AQYC_SH052',
        'HCU_G201_AQYC_SH053',
        'HCU_G201_AQYC_SH054',
        'HCU_G201_AQYC_SH055',
        'HCU_G201_AQYC_SH056',
        'HCU_G201_AQYC_SH057',
        'HCU_G201_AQYC_SH058',
        'HCU_G201_AQYC_SH059',
        'HCU_G201_AQYC_SH060',
        'HCU_G201_AQYC_SH061',
        'HCU_G201_AQYC_SH062',
        'HCU_G201_AQYC_SH063',
        'HCU_G201_AQYC_SH064',
        'HCU_G201_AQYC_SH065',
        'HCU_G201_AQYC_SH066',
        'HCU_G201_AQYC_SH067',
        'HCU_G201_AQYC_SH069',
        'HCU_G201_AQYC_SH070',
        'HCU_G201_AQYC_SH071',
        'HCU_G201_AQYC_SH073',
    ]
    print(len(old_hcu))
    result = dct_t_l3f2cm_device_inventory.objects.all().order_by('-base_port')
    base_port = result[0].base_port
    old_hcu_list=list()
    for i in range(len(old_hcu)):
        old_hcu_list.append(dct_t_l3f2cm_device_inventory(dev_code=old_hcu[i],create_date=datetime.date.today(),valid_flag=1,
                                                          hw_type=2008,sw_ver=375,
                                                          zhb_label='ABCDEF',upgradeflag=1,rebootflag=0,base_port=base_port+i+1,dust_coefmax=700,
                                                          dust_coefmin=10,dust_coefK=1,dust_coefB=0,dust_threshold=30,temp_coefmax=100,temp_coefmin=-40,
                                                          temp_coefK=1,temp_coefB=0,humid_coefmax=100,humid_coefmin=0,humid_coefK=1,humid_coefB=0,
                                                          noise_coefmax=130,noise_coefmin=30,noise_coefK=1,noise_coefB=0,windspd_coefmax=1500,
                                                          windspd_coefmin=0,windspd_coefK=1,windspd_coefB=0,winddir_delta=0,winddir_coefmax=360,
                                                          winddir_coefmin=0,winddir_coefK=1,winddir_coefB=0))
    dct_t_l3f2cm_device_inventory.objects.bulk_create(old_hcu_list)
    print('hello world')

def dft_delete_hcu(a):
    dct_t_l3f2cm_device_inventory.objects.filter(dev_code=a).delete()
    
def dft_dbi_update_inventory():
    dct_t_l3f2cm_device_inventory.objects.all().update(rebootflag=0)
if __name__ == "__main__":
    dft_dbi_update_inventory()
    #insert_old_hcu_data()
    
    
    
    
    
#     resp_dev_data = dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id='HCU_G2400ZNXX_SH003')
#     date_time_now=datetime.datetime.now()
#     report_time=resp_dev_data[0].report_time
#     int_date_time=time.mktime(date_time_now.timetuple())
#     int_report_time=time.mktime(report_time.timetuple())
#     print(date_time_now-report_time)
#     print(int_date_time)
#     print(int_report_time)
    
    
#     insert_menu_code_mapping()
    
#     hcu_update_hw_type(8001)
#     hcu_update_hw_type(8002)
#     hcu_update_hw_type(8100)
#     hcu_update_hw_type(8200)
#     hcu_update_hw_type(2302)
#     hcu_update_hw_type(2013)
#     hcu_update_hw_type(2012)
#     hcu_update_hw_type(2008) 
    
    
    
#     delete_array = [
#         'HCU_G2302ZNXX_SH001',
#         'HCU_G2302ZNXX_SH002',
#         'HCU_G2302ZNXX_SH003',
#         'HCU_G2302ZNXX_SH004',
#         'HCU_G2302ZNXX_SH005',
#         'HCU_G2302ZNXX_SH006',
#         'HCU_G2302ZNXX_SH007',
#         'HCU_G2302ZNXX_SH008',
#         'HCU_G2302ZNXX_SH009',
#         'HCU_G2302ZNXX_SH010',
#     ]
#     for dev in delete_array:
#         hcu_delete(dev)


    # result=dct_t_l3f2cm_device_inventory.objects.latest('base_port')
    # print(result.base_port,result.dev_code)




    # dev_code_array = ['HCU_G2008SHYC_SH001',
    #                   'HCU_G2008SHYC_SH002',
    #                   'HCU_G2008SHYC_SH003',
    #                   'HCU_G2008SHYC_SH004',
    #                   'HCU_G2008SHYC_SH005',
    #
    #                   'HCU_G2008FSTT_SH001',
    #                   'HCU_G2008FSTT_SH002',
    #                   'HCU_G2008FSTT_SH003',
    #                   'HCU_G2008FSTT_SH004',
    #                   'HCU_G2008FSTT_SH005',
    #
    #                   'HCU_G2008XCLH_SH001',
    #                   'HCU_G2008XCLH_SH002',
    #                   'HCU_G2008XCLH_SH003',
    #                   'HCU_G2008XCLH_SH004',
    #                   'HCU_G2008XCLH_SH005',
    #
    #                   'HCU_G2012NALT_SH001',
    #                   'HCU_G2012NALT_SH002',
    #
    #                   'HCU_G2013SHFC_SH001',
    #                   'HCU_G2013SHFC_SH002',
    #                   'HCU_G2013SHFC_SH003',
    #                   'HCU_G2013SHFC_SH004',
    #                   'HCU_G2013SHFC_SH005',
    #
    #                   'HCU_G2013ZNHE_SH001',
    #                   'HCU_G2013ZNHE_SH002',
    #                   'HCU_G2013ZNHE_SH003',
    #                   'HCU_G2013ZNHE_SH004',
    #                   'HCU_G2013ZNHE_SH005',
    #
    #                   'HCU_G2302DAHE_CD001',
    #                   'HCU_G2302DAHE_CD002',
    #                   'HCU_G2302DAHE_CD003',
    #                   'HCU_G2302DAHE_CD004',
    #                   'HCU_G2302DAHE_CD005',
    #
    #                   'HCU_G2302ZNXX_SH001',
    #                   'HCU_G2302ZNXX_SH002',
    #                   'HCU_G2302ZNXX_SH003',
    #                   'HCU_G2302ZNXX_SH004',
    #                   'HCU_G2302ZNXX_SH005',
    #                   'HCU_G2302ZNXX_SH006',
    #                   'HCU_G2302ZNXX_SH007',
    #                   'HCU_G2302ZNXX_SH008',
    #                   'HCU_G2302ZNXX_SH009',
    #                   'HCU_G2302ZNXX_SH010',
    #
    #                   'HCU_G8001BFSC_SH001',
    #                   'HCU_G8001BFSC_SH002',
    #                   'HCU_G8001BFSC_SH003',
    #                   'HCU_G8001BFSC_SH004',
    #                   'HCU_G8001BFSC_SH005',
    #
    #                   'HCU_G8002BFSC_SH001',
    #                   'HCU_G8002BFSC_SH002',
    #                   'HCU_G8002BFSC_SH003',
    #                   'HCU_G8002BFSC_SH004',
    #                   'HCU_G8002BFSC_SH005',
    #
    #                   'HCU_G8100BFDF_SH001',
    #                   'HCU_G8100BFDF_SH002',
    #                   'HCU_G8100BFDF_SH003',
    #                   'HCU_G8100BFDF_SH004',
    #                   'HCU_G8100BFDF_SH005',
    #
    #                   'HCU_G8200BFHS_SH001',
    #                   'HCU_G8200BFHS_SH002',
    #                   'HCU_G8200BFHS_SH003',
    #                   'HCU_G8200BFHS_SH004',
    #                   'HCU_G8200BFHS_SH005',
    #                   ]
    # for dev_code in dev_code_array:
    #     insert_dev_inventory(dev_code)
