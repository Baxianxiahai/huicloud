# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 10:12
# @Author  : DJZ
# @Site    : 
# @File    : DataInsert.py
# @Software: PyCharm
faam1={
    'menu':{
        'menu_user_profile':0X0100,
        'UserManage':0X0200,
        'ParaManage':0X0300,
        'ExportTableManage':0X0400,
        'SoftwareLoadManage':0X0500,
        'PGManage':0X0600,
        'ProjManage':0X0700,
        'MPManage':0X0800,
        'DevManage':0X0900,
        'MPMonitor':0X0A00,
        'MPStaticMonitorTable':0X0B00,
        'MPMonitorCard':0X0C00,
        'WarningCheck':0X0D00,
        'WarningHandle':0X0E00,
        'AuditTarget':0X0F00,
        'AuditStability':0X1000,
        'AuditAvailability':0X1100,
        'AuditError':0X1200,
        'AuditQuality':0X1300,

        'StaffManage':0X1400,
        'AttendanceManage':0X1500,
        'FactoryManage':0X1600,
        'SpecificationManage':0X1700,
        'AssembleManage':0X1800,
        'AssembleAudit':0X1900,
        'AttendanceAudit':0X1A00,
        'KPIAudit':0X1B00,
        'ConsumablesManage':0X1C00,
        'ConsumablesHistory':0X1D00,
        'ProductStorageManage':0X1E00,
        'ProductDeliveryManage':0X1F00,
        'MaterialStorageManage':0X2000,
        'MaterialDeliveryManage':0X2100,

        'SeafoodInfo':0X2200,
        'SeafoodAudit':0X2300,
        'InstConf':0X2400,
        'InstRead':0X2500,
        'InstDesign':0X2600,
        'InstControl':0X2700,
        'InstSnapshot':0X2800,
        'InstVideo':0X2900,
        'GeoInfoQuery':0X2A00,
        'GeoTrendAnalysis':0X2B00,
        'GeoDisaterForecast':0X2C00,
        'GeoEmergencyDirect':0X2D00,
        'GeoDiffusionAnalysis':0X2E00,
        'ADConf':0X2F00,
        'WEBConf':0X3000,
        'KeyManage':0X3100,
        'KeyAuth':0X3200,
        'KeyHistory':0X3300,
        'RTUManage':0X3400,
        'OTDRManage':0X3500,
    },
    'action':{
        'StaffnameList':0X0000,
        'UserInfo':0X0001,
        'GetUserMsg':0X0002,
        'GetUserImg':0X0003,
        'GetGeoList':0X0004,
        'FactoryCodeList':0X0005,
        'SensorList':0X0006,
        'GetCameraUnit':0X0007,
        'ProjectList':0X0008,
        'ProjPoint':0X0009,
        'MonitorList':0X000A,
        'Favourite_list':0X000B,
        'GetProductWeightAndSize':0X000C,
        'GetProductStockList':0X000D,
        'GetMaterialStockList':0X000E,
        'GetConsumablesTypeList':0X000F,
        'GetConsumablesVendorList':0X0010,

        'StaffTable':0X1400,
        'StaffNew':0X1401,
        'StaffMod':0X1402,
        'StaffDel':0X1403,
        'TableQuery':0X1404,

        # 'AttendanceBatchNew':0X1400,
        # 'AttendanceHistory':0X1401,
        # 'AttendanceNew':0X1402,
        # 'AttendanceBatchNew':0X1403,
        # 'AttendanceDel':0X1404,
        # 'GetAttendance':0X1405,
    },
    'common_action':{},
}
# print(len(faam1))
# print(len(faam1['menu']))
# print(len(faam1['action']))
# for key in faam1['menu']:
#     print(key)
#     print(faam1['menu'][key])
import os
import hashlib
os.environ['DJANGO_SETTINGS_MODULE']='xhzn_db_new.settings'
import django
django.setup()
from xhzn.models import t_l3f1sym_menu_code_mapping as map,t_l3f1sym_account_primary as account,t_l3f1sym_user_right_menu as right_menu
def insert_map(code,name):
    Map=map(menu_code=code,menu_name=name)
    Map.save()
    return
def delete_map():
    Map=map.objects.filter().delete()
    return
def insert_user():
    h1=hashlib.md5()
    name='admin'
    str='admin'
    h1.update(str.encode(encoding='utf-8'))
    pwd=h1.hexdigest()
    uid='MID0000002'
    email='111@qq.com'
    grade_level=1
    Account=account(uid=uid,login_name=name,pass_word=pwd,email=email,grade_lever=grade_level)
    Account.save()
def update_user():
    Account=account.objects.get(uid='MID0000001')
    Account.menu_group=1
    Account.save()
def select_menu():
    menu=map.objects.filter().all()
    return menu
def auth_menu(line,group):
    Auth=right_menu(menu_name=line.menu_name,menu_code=line,menu_group=group)
    Auth.save()
if __name__ == '__main__':
    print('Work Start')
    a="admin123"
    hl=hashlib.md5()
    hl.update(a.encode(encoding='utf-8'))
    print(hl.hexdigest())
    # delete_map()
    # for key in faam1['menu']:
    #     print(faam1['menu'][key])
    #     print(key)
    #     insert_map(faam1['menu'][key],key)

    # insert_user()

    # update_user()

    # menu=select_menu()
    # for line in menu:
    #     auth_menu(line,1)
    print('Work End')

# import threading
# from time import ctime,sleep
#
#
# def music(func):
#     for i in range(2):
#         print ("I was listening to %s. %s" %(func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s! %s" %(func,ctime()))
#         sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#
#     print ("all over %s" %ctime())