# -*- coding: utf-8 -*-
'''
Created on 2018年7月12日

@author: Administrator
'''
import time
import os, sys
import pymysql
import django
import datetime
import numpy as np

# sys.path.append('C:\wamp\www\huicloud\DjoSiteDba')
sys.path.append('/var/www/html/huicloud/DjoSiteDba')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
django.setup()
from DappDbF1sym.models import *
from DappDbF1sym import views
from DappDbF11faam.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbF10oam.models import *
from DappDbSnr.models import *


def clearOldData():
    delete_days = 70
    time_now = datetime.date.today()
    time_old = time_now - datetime.timedelta(days=delete_days)
    time_old = str(time_old)
    print(time_old)
    l3time_old = time_old + " 23:59:59"
    dct_t_l2snr_temperature.objects.filter(report_data__lte=time_old).delete()
    dct_t_l2snr_humidity.objects.filter(report_data__lte=time_old).delete()
    dct_t_l2snr_winddir.objects.filter(report_data__lte=time_old).delete()
    dct_t_l2snr_windspd.objects.filter(report_data__lte=time_old).delete()
    dct_t_l2snr_noise.objects.filter(report_data__lte=time_old).delete()
    dct_t_l2snr_picture.objects.filter(report_data__lte=time_old).delete()
    dct_t_l3f3dm_minute_report_aqyc.objects.filter(report_date__lte=l3time_old).delete()


def dft_dbi_faam_qrcode_sc_process(inputData):
    scanCode = inputData['scanCode']
    nickName = inputData['nickname']
    tiamstamp = int(time.time())
    localTime = time.localtime(tiamstamp)
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    #         if nickName == '李坤洋':
    codeResultLKY = dct_t_l3f11faam_batch_scan.objects.filter(qrcode=scanCode)
    if codeResultLKY.exists():
        for line in codeResultLKY:
            activeTime = line.activetime
            package = line.packagesum
            qrcode_owner = line.owner
            appleGrade = line.typecode
            appleType = dct_t_l3f11faam_type_sheet.objects.filter(typecode=appleGrade)
            if appleType.exists():
                appleNum = appleGrade
            else:
                appleNum = "未知类型"
            #                     if nickName == "李坤洋":
            if activeTime == None:
                dct_t_l3f11faam_batch_scan.objects.filter(qrcode=scanCode).update(activetime=currentTime,
                                                                                  activeman=nickName,
                                                                                  lastactivetime=currentTime)
                resp = {'flag': True, 'employee': qrcode_owner, 'message': '统计成功'}
            else:
                dct_t_l3f11faam_batch_scan.objects.filter(qrcode=scanCode).update(lastactivetime=currentTime)
                resp = {'flag': False, 'employee': qrcode_owner,
                        'message': '箱数：' + str(package) + '；规格：' + appleNum}
    #                     else:
    #                         resp = {'flag': False, 'employee': nickName, 'message': '扫描用户非管理人员'}
    #             else:
    #                 resp = {'flag': False, 'employee': nickName, 'message': '扫垛二维码无效'}
    else:
        codeResult = dct_t_l3f11faam_production.objects.filter(qrcode=scanCode)
        if codeResult.exists():
            for line in codeResult:
                activeTime = line.activetime
                pjCode = line.pjcode
                qrcode_owner = line.owner
                appleGrade = line.typecode
                memberResult = dct_t_l3f11faam_member_sheet.objects.filter(openid=nickName, pjcode=pjCode)
                appleType = dct_t_l3f11faam_type_sheet.objects.filter(typecode=appleGrade)
                if appleType.exists():
                    appleNum = appleType[0].applenum
                else:
                    appleNum = "未知类型"
                if memberResult.exists():
                    for line in memberResult:
                        scan_operator = line.employee
                        if activeTime == None:
                            dct_t_l3f11faam_production.objects.filter(qrcode=scanCode).update(
                                activeman=scan_operator,
                                activetime=currentTime,
                                lastactivetime=currentTime)
                            resp = {'flag': True, 'employee': scan_operator, 'message': '统计成功'}
                        else:
                            dct_t_l3f11faam_production.objects.filter(qrcode=scanCode).update(
                                lastactivetime=currentTime)
                            resp = {'flag': False, 'employee': scan_operator,
                                    'message': '姓名：' + qrcode_owner + '；粒数：' + str(appleNum)}
                else:
                    resp = {'flag': False, 'employee': nickName, 'message': '扫描用户未注册'}
        else:
            resp = {'flag': False, 'employee': nickName, 'message': '二维码无效'}
    return resp


def createDirctKeyAndValue():
    a = {}
    b = "sss"
    a[b] = []
    print(a)
    c = []
    c.append(1)
    a[b].append(c)
    a[b][0].append(2)
    print(a[b][0])


def dft_dbi_aqyc_dev_alarmhistory_realtime_req(inputData):
    # a={"StatCode":"284356971","date":"","AlarmName":"细颗粒物","AlarmUnit":"微克\/立方米","WarningTarget":201,"minute_head":["12:37","12:38","12:39","12:40","12:41","12:42","12:43","12:44","12:45","12:46","12:47","12:48","12:49","12:50","12:51","12:52","12:53","12:54","12:55","12:56","12:57","12:58","12:59","13:00","13:01","13:02","13:03","13:04","13:05","13:06","13:07","13:08","13:09","13:10","13:11","13:12","13:13","13:14","13:15","13:16","13:17","13:18","13:19","13:20","13:21","13:22","13:23","13:24","13:25","13:26","13:27","13:28","13:29","13:30","13:31","13:32","13:33","13:34","13:35","13:36"],"minute_alarm":[{"name":"TSP","color":"","items":[88,77,74,81,79,83,85,69,73,84,73,68,70,67,65,71,60,70,66,66,68,68,69,64,62,64,63,58,66,67,69,72,69,72,64,69,69,69,66,80,67,62,60,68,69,66,69,67,72,68,69,62,64,63,75,75,71,71,72,63]}],"hour_head":["14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00"],"hour_alarm":[{"name":"TSP","color":"","items":[86.4,83.3,89.6,74.1,74.7,68.4,57.6,55.5,51,55.9,64.3,72.1,73.9,80.1,87.8,96.2,104.8,107.1,90,94.9,82.6,74.2,74.3,67.5]}],"Alarm_min":0,"Alarm_max":112.1}
    statcode = inputData['statcode']
    # alarm_type = inputData['alarmtype']
    alarm_name="细颗粒物"
    alarm_unit = '微克/立方米'
    result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
    if result.exists():
        dev_code = result[0].dev_code
    else:
        dev_code = ""
    minute_alarm = []
    minute_head = []
    hour_alarm = []
    hour_head = []
    minute_new = {}
    hour_new = {}
    value = []
    now_time = datetime.datetime.now()
    yesterday_time = datetime.datetime.now() - datetime.timedelta(days=1)
    data_today = now_time.date()
    hour_today = now_time.hour
    minute_today = now_time.minute
    secound_today = now_time.second
    data_yesterday = yesterday_time.date()
    hour_yesterday = yesterday_time.hour
    minute_start = str(data_today) + " " + str(hour_today - 1) + ":" + str(minute_today) + ":" + str(secound_today)
    hour_start = str(data_yesterday) + " " + str(hour_yesterday) + ":00:00"
    minute_end = str(data_today) + " " + str(hour_today) + ":" + str(minute_today) + ":" + str(secound_today)
    hour_end = str(data_today) + " " + str(hour_today) + ":00:00"
    result_min = dct_t_l3f3dm_minute_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                                report_date__range=(minute_start, minute_end))
    result_hour = dct_t_l3f3dm_hour_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                               report_date__range=(hour_start, hour_end))
    if (result_min.exists() and result_hour.exists()):
        for line in result_min:
            NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
            minute_new[NewData] = line.tsp
        for line in result_hour:
            newData = str(line.report_date.hour).zfill(2) + ":00"
            hour_new[newData] = line.tsp
        print(len(minute_new))
        for i in range(60):
            if minute_today + i < 60:
                minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
            else:
                minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
            minute_head.append(minute_head1)
            if minute_head1 in minute_new.keys():
                minute_alarm.append(round(minute_new[minute_head1]), 2)
            else:
                minute_alarm.append(0)
        for i in range(0, 24):
            if hour_today + i < 24:
                hour_head1 = str(hour_today + i).zfill(2) + ":00"
            else:
                hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
            hour_head.append(hour_head1)
            if hour_head1 in hour_new.keys():
                hour_alarm.append(hour_new[hour_head1])
            else:
                hour_alarm.append(0)
        hour_head.append(str(hour_today).zfill(2) + ":00")
        hour_alarm.append(np.mean(value))
        print(minute_new)
        print(minute_head)
        print(len(minute_head))
        print(minute_alarm)
        print(len(minute_alarm))
        # print(i)
        # print(line.report_date)
        # i=i+1
        # result_hour=dct_t_l3f3dm_hour_report_aqyc.
        # print(minute_new)
    else:
        return
    # if result.exists():
    #     for line in result:
    #         devCode = line.dev_code
    # else:
    #     devCode = ""
    # minute_alarm = []
    # minute_head = []
    # hour_alarm = []
    # hour_head = []
    # line_name = ""
    # min = datetime.datetime.now()
    # today = min.date()
    # hour_base = min.hour
    # minute_base = min.minute
    # index_base = (hour_base + 1) * 60
    # hourminindex_now = (min.hour * 60 + min.minute) / 1.0
    # dayStart = datetime.datetime.today() - datetime.timedelta(days=1)
    # grideValue = []
    # alarm_name = ""
    # alarm_unit = ""
    # warning = ""
    # for i in range(1441):
    #     value = {'value': 0}
    #     grideValue.append(value)
    # hourValue = []
    # for j in range(25):
    #     value = {'sum': 0, 'counter': 0, 'average': 0}
    #     hourValue.append(value)
    # if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
    #     alarm_name = '细颗粒物'
    #     alarm_unit = '微克/立方米'
    #     warning = self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
    #     line_name = 'TSP'
    #     result = dct_t_l2snr_dust.objects.filter(Q(dev_code_id=devCode), (
    #                 Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
    #     if result.exists():
    #         for line in result:
    #             value = line.tsp
    #             hourminindex = line.hourminindex
    #             reportDate = line.report_data
    #             hour_index = int((hourminindex * 1.0) / 60)
    #             if reportDate == today and (hourminindex >= hourminindex_now - 60):
    #                 grideValue[hourminindex]['value'] = value
    #             if 'counter' in hourValue[hour_index].keys():
    #                 hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
    #                 hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1
    #
    # if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
    #     alarm_name = '噪声'
    #     alarm_unit = '分贝'
    #     warning = self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
    #     line_name = '噪声'
    #     result = dct_t_l2snr_noise.objects.filter(Q(dev_code_id=devCode), (
    #                 Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
    #     if result.exists():
    #         for line in result:
    #             value = line.noise
    #             hourminindex = line.hourminindex
    #             reportDate = line.report_data
    #             hour_index = int((hourminindex * 1.0) / 60)
    #             if reportDate == today and (hourminindex >= hourminindex_now - 60):
    #                 grideValue[hourminindex]['value'] = value
    #             if 'counter' in hourValue[hour_index].keys():
    #                 hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
    #                 hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1
    #
    # if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
    #     alarm_name = '温度'
    #     alarm_unit = '摄氏度'
    #     warning = self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
    #     line_name = '温度'
    #     result = dct_t_l2snr_temperature.objects.filter(Q(dev_code_id=devCode), (
    #                 Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
    #     if result.exists():
    #         for line in result:
    #             value = line.temperature
    #             hourminindex = line.hourminindex
    #
    #             reportDate = line.report_data
    #             hour_index = int((hourminindex * 1.0) / 60)
    #             if reportDate == today and (hourminindex >= hourminindex_now - 60):
    #                 grideValue[hourminindex]['value'] = value
    #             if 'counter' in hourValue[hour_index].keys():
    #                 hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
    #                 hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1
    #
    # if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
    #     alarm_name = '湿度'
    #     alarm_unit = '%'
    #     warning = self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
    #     line_name = '湿度'
    #     result = dct_t_l2snr_humidity.objects.filter(Q(dev_code_id=devCode), (
    #                 Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
    #     if result.exists():
    #         for line in result:
    #             value = line.humidity
    #             hourminindex = line.hourminindex
    #             reportDate = line.report_data
    #             hour_index = int((hourminindex * 1.0) / 60)
    #             if reportDate == today and (hourminindex >= hourminindex_now - 60):
    #                 grideValue[hourminindex]['value'] = value
    #             if 'counter' in hourValue[hour_index].keys():
    #                 hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
    #                 hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1
    #
    # if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
    #     alarm_name = '风速'
    #     alarm_unit = '米/秒'
    #     warning = self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
    #     line_name = '风速'
    #     result = dct_t_l2snr_windspd.objects.filter(Q(dev_code_id=devCode), (
    #                 Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
    #     if result.exists():
    #         for line in result:
    #             value = line.windspd
    #             hourminindex = line.hourminindex
    #             reportDate = line.report_data
    #             hour_index = int((hourminindex * 1.0) / 60)
    #             if reportDate == today and (hourminindex >= hourminindex_now - 60):
    #                 grideValue[hourminindex]['value'] = value
    #             if 'counter' in hourValue[hour_index].keys():
    #                 hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
    #                 hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1
    # minute_value = []
    # for i in range(60):
    #     if minute_base + i < 60:
    #         minute_head1 = str(hour_base - 1) + ":" + str(minute_base + i).zfill(2)
    #     else:
    #         minute_head1 = str(hour_base) + ":" + str(minute_base - (60 - i)).zfill(2)
    #     minute_value.append(grideValue[int(hourminindex_now - (60 - i))]['value'])
    #     minute_head.append(str(minute_head1))
    #
    # minute_alarm1 = {'name': line_name, 'color': "", 'items': minute_value}
    # minute_alarm.append(minute_alarm1)
    # hour_value = []
    # for j in range(1, 25):
    #     if hour_base + j < 24:
    #         hour_index = hour_base + j
    #     else:
    #         hour_index = hour_base - (24 - j)
    #     if hourValue[hour_index]['counter'] != 0:
    #         hourValue[hour_index]['average'] = hourValue[hour_index]['sum'] / hourValue[hour_index]['counter']
    #         average = round(hourValue[hour_index]['average'], 1)
    #         hour_value.append(average)
    #         hour_head.append(str(hour_index) + ":00")
    #     else:
    #         hour_value.append(0)
    #         hour_head.append(str(hour_index) + ":00")
    # hour_alarm1 = {'name': line_name, 'color': "", 'items': hour_value}
    # hour_alarm.append(hour_alarm1)
    # value_min = 0
    # max_1 = max(minute_value)
    # max_2 = max(hour_value)
    # value_max = max(max_1, max_2) + 5
    # value_temp = {"minute_alarm": minute_alarm, "minute_head": minute_head, "hour_alarm": hour_alarm,
    #               "hour_head": hour_head, "alarm_name": alarm_name, "alarm_unit": alarm_unit, "warning": warning,
    #               'value_min': value_min, "value_max": value_max}
    # return value_temp


# def a():
#     time_old=datetime.datetime.now()-datetime.timedelta(hours=1)
#     print(time_old)
#     print(type(time_old))
#
#     date_old=time_old.date()
#     hour_old=time_old.hour
#     print(date_old)
#     print(hour_old)

def createData():
    pass
    # dct_t_l3f3dm_hour_report_aqyc.objects.create(dev_code_id='HCU_G201_AQYC_SH073', site_code_id='796823451', hourindex=14, report_date='2018-12-01 14:01:00')
    # result=dct_t_l3f3dm_hour_report_aqyc.objects.filter(report_date__range=("2018-12-01 14:00:00","2018-12-01 14:01:00"))
    # print(result)
class aaa:
    __HUITP_IEID_UNI_ALARM_SEVERITY_NONE = 0X00
    __HUITP_IEID_UNI_ALARM_SEVERITY_HIGH = 0X01
    __HUITP_IEID_UNI_ALARM_SEVERITY_MEDIUM = 0X02
    __HUITP_IEID_UNI_ALARM_SEVERITY_MINOR = 0X03
    __HUITP_IEID_UNI_ALARM_SEVERITY_INVALID = 0XFF

    __MFUN_HCU_SITE_PIC_WWW_PATH = "/avorion/picture/"

    __MFUN_L3APL_F3DM_TH_ALARM_NOISE = 70
    __MFUN_L3APL_F3DM_TH_ALARM_HUMID = 80
    __MFUN_L3APL_F3DM_TH_ALARM_TEMP = 45
    __MFUN_L3APL_F3DM_TH_ALARM_PM25 = 201
    __MFUN_L3APL_F3DM_TH_ALARM_WINDSPD = 20
    __MFUN_L3APL_F3DM_TH_ALARM_EMC = 100
    __MFUN_L3APL_F3DM_TH_ALARM_WINDDIR = 360
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW = 15
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH = 70
    __MFUN_L3APL_F3DM_TH_ALARM_BATT = 20
    __MFUN_AQYC_ALARM_CODE = ['工作正常', '颗粒物传感器故障', '温度传感器故障', '湿度传感器故障', '风向传感器故障', '风速传感器故障', '噪声传感器故障', '摄像头故障',
                              '扬尘超标', '噪声超标']
    __MFUN_HCU_FHYS_CMCC_URL = "http://api.sms.heclouds.com/tempsmsSend"
    __MFUN_HCU_FHYS_CMCC_SICODE = "a2bb3546a41649a29e2fcb635e091dd5"
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_PW = "10832"
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM = "10833"

    __MFUN_HCU_ALARM_PROC_FLAG_Y = 'Y'
    __MFUN_HCU_ALARM_PROC_FLAG_N = 'N'
    __MFUN_HCU_ALARM_PROC_FLAG_C = 'C'

    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT = "W"

    __MFUN_L3APL_F3DM_AQYC_STYPE_PREFIX = 'YC'
    __MFUN_L3APL_F3DM_AQYC_STYPE_PM = "YC_001"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD = "YC_002"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDDIR = "YC_003"
    __MFUN_L3APL_F3DM_AQYC_STYPE_EMC = "YC_005"
    __MFUN_L3APL_F3DM_AQYC_STYPE_TEMP = "YC_006"
    __MFUN_L3APL_F3DM_AQYC_STYPE_HUMID = "YC_007"
    __MFUN_L3APL_F3DM_AQYC_STYPE_NOISE = "YC_00A"
    def dft_dbi_aqyc_dev_alarmhistory_realtime_req_1(self,inputData):
        # a={"StatCode":"284356971","date":"","AlarmName":"细颗粒物","AlarmUnit":"微克\/立方米","WarningTarget":201,"minute_head":["12:37","12:38","12:39","12:40","12:41","12:42","12:43","12:44","12:45","12:46","12:47","12:48","12:49","12:50","12:51","12:52","12:53","12:54","12:55","12:56","12:57","12:58","12:59","13:00","13:01","13:02","13:03","13:04","13:05","13:06","13:07","13:08","13:09","13:10","13:11","13:12","13:13","13:14","13:15","13:16","13:17","13:18","13:19","13:20","13:21","13:22","13:23","13:24","13:25","13:26","13:27","13:28","13:29","13:30","13:31","13:32","13:33","13:34","13:35","13:36"],"minute_alarm":[{"name":"TSP","color":"","items":[88,77,74,81,79,83,85,69,73,84,73,68,70,67,65,71,60,70,66,66,68,68,69,64,62,64,63,58,66,67,69,72,69,72,64,69,69,69,66,80,67,62,60,68,69,66,69,67,72,68,69,62,64,63,75,75,71,71,72,63]}],"hour_head":["14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00"],"hour_alarm":[{"name":"TSP","color":"","items":[86.4,83.3,89.6,74.1,74.7,68.4,57.6,55.5,51,55.9,64.3,72.1,73.9,80.1,87.8,96.2,104.8,107.1,90,94.9,82.6,74.2,74.3,67.5]}],"Alarm_min":0,"Alarm_max":112.1}
        statcode = inputData['statcode']
        alarm_type = inputData['alarmtype']
        alarm_name = ""
        alarm_unit = ''
        result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
        if result.exists():
            dev_code = result[0].dev_code
        else:
            dev_code = ""
        value_min=0
        value_max=0
        warning=0
        line_name=""
        minute_alarm = []
        minute_head = []
        hour_alarm = []
        hour_head = []
        minute_new = {}
        hour_new = {}
        now_time = datetime.datetime.now()
        yesterday_time = datetime.datetime.now() - datetime.timedelta(days=1)
        data_today = now_time.date()
        hour_today = now_time.hour
        minute_today = now_time.minute
        secound_today = now_time.second
        data_yesterday = yesterday_time.date()
        hour_yesterday = yesterday_time.hour
        minute_start = str(data_today) + " " + str(hour_today - 1) + ":" + str(minute_today) + ":" + str(secound_today)
        hour_start = str(data_yesterday) + " " + str(hour_yesterday) + ":00:00"
        minute_end = str(data_today) + " " + str(hour_today) + ":" + str(minute_today) + ":" + str(secound_today)
        hour_end = str(data_today) + " " + str(hour_today) + ":00:00"
        result_min = dct_t_l3f3dm_minute_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                                    report_date__range=(minute_start, minute_end))
        result_hour = dct_t_l3f3dm_hour_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                                   report_date__range=(hour_start, hour_end))
        if alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
            alarm_name='细颗粒物'
            alarm_unit='微克/立方米'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
            line_name='TSP'
            if(result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.tsp
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.tsp
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min=0
                max_1=max(minute_alarm)
                max_2=max(hour_alarm)
                value_max=max(max_1,max_2)+5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
            alarm_name = '噪声'
            alarm_unit = '分贝'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
            line_name = '噪声'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.noise
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.noise
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
            alarm_name = '温度'
            alarm_unit = '摄氏度'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
            line_name = '温度'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.temperature
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.temperature
                print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
            alarm_name = '湿度'
            alarm_unit = '%'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
            line_name = '湿度'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.humidity
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.humidity
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1],2))
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
            alarm_name = '风速'
            alarm_unit = '米/秒'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
            line_name = '风速'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.windspd
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.windspd
                print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        value_temp={"minute_alarm":[{'name':line_name,'color':"",'items':minute_alarm}],"minute_head":minute_head,"hour_alarm":[{'name':line_name,'color':"",'items':hour_alarm}],
                    "hour_head":hour_head,"alarm_name":alarm_name,"alarm_unit":alarm_unit,"warning":warning,
                    'value_min':value_min,"value_max":value_max}
        print(value_temp)
        return value_temp
    
    def dft_dbi_fstt_dev_alarmhistory_realtime_req_view(self,inputData):
        # a={"StatCode":"284356971","date":"","AlarmName":"细颗粒物","AlarmUnit":"微克\/立方米","WarningTarget":201,"minute_head":["12:37","12:38","12:39","12:40","12:41","12:42","12:43","12:44","12:45","12:46","12:47","12:48","12:49","12:50","12:51","12:52","12:53","12:54","12:55","12:56","12:57","12:58","12:59","13:00","13:01","13:02","13:03","13:04","13:05","13:06","13:07","13:08","13:09","13:10","13:11","13:12","13:13","13:14","13:15","13:16","13:17","13:18","13:19","13:20","13:21","13:22","13:23","13:24","13:25","13:26","13:27","13:28","13:29","13:30","13:31","13:32","13:33","13:34","13:35","13:36"],"minute_alarm":[{"name":"TSP","color":"","items":[88,77,74,81,79,83,85,69,73,84,73,68,70,67,65,71,60,70,66,66,68,68,69,64,62,64,63,58,66,67,69,72,69,72,64,69,69,69,66,80,67,62,60,68,69,66,69,67,72,68,69,62,64,63,75,75,71,71,72,63]}],"hour_head":["14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00"],"hour_alarm":[{"name":"TSP","color":"","items":[86.4,83.3,89.6,74.1,74.7,68.4,57.6,55.5,51,55.9,64.3,72.1,73.9,80.1,87.8,96.2,104.8,107.1,90,94.9,82.6,74.2,74.3,67.5]}],"Alarm_min":0,"Alarm_max":112.1}
        statcode = inputData['statcode']
        alarm_type = inputData['alarmtype']
        alarm_name = ""
        alarm_unit = ''
        result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
        if result.exists():
            dev_code = result[0].dev_code
        else:
            dev_code = ""
        value_min=0
        value_max=0
        warning=0
        line_name=""
        minute_alarm = []
        minute_head = []
        hour_alarm = []
        hour_head = []
        minute_new = {}
        hour_new = {}
        now_time = datetime.datetime.now()
        yesterday_time = datetime.datetime.now() - datetime.timedelta(days=1)
        data_today = now_time.date()
        hour_today = now_time.hour
        minute_today = now_time.minute
        secound_today = now_time.second
        data_yesterday = yesterday_time.date()
        hour_yesterday = yesterday_time.hour
        minute_start = str(data_today) + " " + str(hour_today - 1) + ":" + str(minute_today) + ":" + str(secound_today)
        hour_start = str(data_yesterday) + " " + str(hour_yesterday) + ":00:00"
        minute_end = str(data_today) + " " + str(hour_today) + ":" + str(minute_today) + ":" + str(secound_today)
        hour_end = str(data_today) + " " + str(hour_today) + ":00:00"
        result_min = dct_t_l3f3dm_minute_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                                    report_date__range=(minute_start, minute_end))
        result_hour = dct_t_l3f3dm_hour_report_aqyc.objects.filter(dev_code_id=dev_code,
                                                                   report_date__range=(hour_start, hour_end))
        if alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
            alarm_name='细颗粒物'
            alarm_unit='微克/立方米'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
            line_name='TSP'
            if(result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.tsp
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.tsp
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min=0
                max_1=max(minute_alarm)
                max_2=max(hour_alarm)
                value_max=max(max_1,max_2)+5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
            alarm_name = '噪声'
            alarm_unit = '分贝'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
            line_name = '噪声'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.noise
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.noise
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
            alarm_name = '温度'
            alarm_unit = '摄氏度'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
            line_name = '温度'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.temperature
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.temperature
                print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
            alarm_name = '湿度'
            alarm_unit = '%'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
            line_name = '湿度'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.humidity
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.humidity
                # print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1],2))
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        elif alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
            alarm_name = '风速'
            alarm_unit = '米/秒'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
            line_name = '风速'
            if (result_min.exists() and result_hour.exists()):
                for line in result_min:
                    NewData = str(line.report_date.hour).zfill(2) + ":" + str(line.report_date.minute).zfill(2)
                    minute_new[NewData] = line.windspd
                for line in result_hour:
                    newData = str(line.report_date.hour).zfill(2) + ":00"
                    hour_new[newData] = line.windspd
                print(len(minute_new))
                for i in range(60):
                    if minute_today + i < 60:
                        minute_head1 = str(hour_today - 1).zfill(2) + ":" + str(minute_today + i).zfill(2)
                    else:
                        minute_head1 = str(hour_today).zfill(2) + ":" + str(minute_today - (60 - i)).zfill(2)
                    minute_head.append(minute_head1)
                    if minute_head1 in minute_new.keys():
                        minute_alarm.append(round(minute_new[minute_head1]), 2)
                    else:
                        minute_alarm.append(0)
                for i in range(0, 24):
                    if hour_today + i < 24:
                        hour_head1 = str(hour_today + i).zfill(2) + ":00"
                    else:
                        hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
                    hour_head.append(hour_head1)
                    if hour_head1 in hour_new.keys():
                        hour_alarm.append(hour_new[hour_head1])
                    else:
                        hour_alarm.append(0)
                value_min = 0
                max_1 = max(minute_alarm)
                max_2 = max(hour_alarm)
                value_max = max(max_1, max_2) + 5
        value_temp={"minute_alarm":[{'name':line_name,'color':"",'items':minute_alarm}],"minute_head":minute_head,"hour_alarm":[{'name':line_name,'color':"",'items':hour_alarm}],
                    "hour_head":hour_head,"alarm_name":alarm_name,"alarm_unit":alarm_unit,"warning":warning,
                    'value_min':value_min,"value_max":value_max}
        return value_temp

    def dft_dbi_faam_qrcode_batch(self, inputData):
        ColumnName = []
        TableData = []
        uid = inputData['uid']
        timeStart = inputData['TimeStart']
        timeEnd = inputData['TimeEnd']
        keyWord = inputData['KeyWord']
        timeStartStr = str(timeStart) + ' 00:00:00'
        timeEndStr = str(timeEnd) + ' 23:59:59'
        ColumnName.append('序号')
        # ColumnName.append('二维码')
        ColumnName.append('负责人')
        ColumnName.append('总箱数')
        ColumnName.append('产品规格')
        ColumnName.append('开始时间')
        ColumnName.append('结束时间')
        i = 1
        totalPackageNum = 0
        totalDict = {}
        #         userLever=self.__dft_get_user_lever(uid)
        pjCode = "HYGS"
        if keyWord == "":
            result = dct_t_l3f11faam_batch_scan.objects.filter(activetime__range=(timeStartStr, timeEndStr),
                                                               pjcode=pjCode)
        else:
            result = dct_t_l3f11faam_batch_scan.objects.filter(activetime__range=(timeStartStr, timeEndStr),
                                                               pjcode=pjCode, typecode__icontains=keyWord)

        if result.exists():
            for line in result:
                totalPackageNum = totalPackageNum + line.packagesum
                if line.owner not in totalDict.keys():
                    totalDict[line.owner] = {}
                    if line.typecode not in totalDict[line.owner].keys():
                        totalDict[line.owner][line.typecode] = line.packagesum
                    else:
                        totalDict[line.owner][line.typecode] = totalDict[line.owner][line.typecode] + line.packagesum
                else:
                    if line.typecode not in totalDict[line.owner].keys():
                        totalDict[line.owner][line.typecode] = line.packagesum
                    else:
                        totalDict[line.owner][line.typecode] = totalDict[line.owner][line.typecode] + line.packagesum
        for key, value in totalDict.items():
            for key_type, value_type in totalDict[key].items():
                history = []
                history.append(i)
                history.append(key)
                # history.append(totalDict[key][key_type])
                history.append(value_type)
                history.append(key_type)
                history.append(timeStart)
                history.append(timeEnd)
                TableData.append(history)
                i=i+1
        #         if result.exists():
        #             for line in result:
        #                 totalPackageNum=totalPackageNum+line.packagesum
        #                 history=[]
        #                 history.append(i)
        #                 history.append(line.qrcode)
        #                 history.append(line.owner)
        #                 history.append(line.packagesum)
        #                 history.append(line.typecode)
        #                 history.append(str(line.applydate))
        #                 history.append(str(line.activetime))
        #                 TableData.append(history)
        #                 i=i+1
        history = []
        history.append(0)
        history.append("----")
        # history.append("----")
        history.append(totalPackageNum)
        history.append("----")
        history.append(timeStart)
        history.append(timeEnd)
        TableData.append(history)
        Table = {'ColumnName': ColumnName, 'TableData': TableData}
        return Table
    def dft_dbi_calculation_hour_data(self):
        time_old = datetime.datetime.now() - datetime.timedelta(hours=1)
        now_date = time_old.date()
        now_hour = time_old.hour
        # time_start=str(now_date)+" "+str(now_hour)+":00:00"
        time_start="2018-12-04 03:00:00"
        # time_end=str(now_date)+" "+str(now_hour)+":59:59"
        time_end="2018-12-04 03:59:59"
        data={}
        hour=list()
        result_min=dct_t_l3f3dm_minute_report_aqyc.objects.filter(report_date__range=(time_start,time_end))
        if result_min.exists():
            for line in result_min:
                print(line.report_date)
                if line.site_code_id not in data.keys():
                    data[line.site_code_id]={}
                    if line.dev_code_id not in data[line.site_code_id].keys():
                        data[line.site_code_id][line.dev_code_id]=[]
                        tsp=[]
                        tsp.append(line.tsp)
                        data[line.site_code_id][line.dev_code_id].append(tsp)
                        pm01 = []
                        pm01.append(line.pm01)
                        data[line.site_code_id][line.dev_code_id].append(pm01)
                        pm25 = []
                        pm25.append(line.pm25)
                        data[line.site_code_id][line.dev_code_id].append(pm25)
                        pm10 = []
                        pm10.append(line.pm10)
                        data[line.site_code_id][line.dev_code_id].append(pm10)
                        noise = []
                        noise.append(line.noise)
                        data[line.site_code_id][line.dev_code_id].append(noise)
                        temperature = []
                        temperature.append(line.temperature)
                        data[line.site_code_id][line.dev_code_id].append(temperature)
                        humidity = []
                        humidity.append(line.humidity)
                        data[line.site_code_id][line.dev_code_id].append(humidity)
                        winddir = []
                        winddir.append(line.winddir)
                        data[line.site_code_id][line.dev_code_id].append(winddir)
                        windspd = []
                        windspd.append(line.windspd)
                        data[line.site_code_id][line.dev_code_id].append(windspd)
                        rain = []
                        rain.append(line.rain)
                        data[line.site_code_id][line.dev_code_id].append(rain)
                        airpresure = []
                        airpresure.append(line.airpresure)
                        data[line.site_code_id][line.dev_code_id].append(airpresure)
                        lightstr = []
                        lightstr.append(line.lightstr)
                        data[line.site_code_id][line.dev_code_id].append(lightstr)
                        so2 = []
                        so2.append(line.so2)
                        data[line.site_code_id][line.dev_code_id].append(so2)
                        co1 = []
                        co1.append(line.co1)
                        data[line.site_code_id][line.dev_code_id].append(co1)
                        no1 = []
                        no1.append(line.no1)
                        data[line.site_code_id][line.dev_code_id].append(no1)
                        h2s = []
                        h2s.append(line.h2s)
                        data[line.site_code_id][line.dev_code_id].append(h2s)
                        hcho = []
                        hcho.append(line.hcho)
                        data[line.site_code_id][line.dev_code_id].append(hcho)
                        toxicgas = []
                        toxicgas.append(line.toxicgas)
                        data[line.site_code_id][line.dev_code_id].append(toxicgas)
                        rssi = []
                        rssi.append(line.rssi)
                        data[line.site_code_id][line.dev_code_id].append(rssi)
                        pwrind = []
                        pwrind.append(line.pwrind)
                        data[line.site_code_id][line.dev_code_id].append(pwrind)
                    else:
                        data[line.site_code_id][line.dev_code_id][0].append(line.tsp)
                        data[line.site_code_id][line.dev_code_id][1].append(line.pm01)
                        data[line.site_code_id][line.dev_code_id][2].append(line.pm25)
                        data[line.site_code_id][line.dev_code_id][3].append(line.pm10)
                        data[line.site_code_id][line.dev_code_id][4].append(line.noise)
                        data[line.site_code_id][line.dev_code_id][5].append(line.temperature)
                        data[line.site_code_id][line.dev_code_id][6].append(line.humidity)
                        data[line.site_code_id][line.dev_code_id][7].append(line.winddir)
                        data[line.site_code_id][line.dev_code_id][8].append(line.windspd)
                        data[line.site_code_id][line.dev_code_id][9].append(line.rain)
                        data[line.site_code_id][line.dev_code_id][10].append(line.airpresure)
                        data[line.site_code_id][line.dev_code_id][11].append(line.lightstr)
                        data[line.site_code_id][line.dev_code_id][12].append(line.so2)
                        data[line.site_code_id][line.dev_code_id][13].append(line.co1)
                        data[line.site_code_id][line.dev_code_id][14].append(line.no1)
                        data[line.site_code_id][line.dev_code_id][15].append(line.h2s)
                        data[line.site_code_id][line.dev_code_id][16].append(line.hcho)
                        data[line.site_code_id][line.dev_code_id][17].append(line.toxicgas)
                        data[line.site_code_id][line.dev_code_id][18].append(line.rssi)
                        data[line.site_code_id][line.dev_code_id][19].append(line.pwrind)
                else:
                    if line.dev_code_id not in data[line.site_code_id].keys():
                        data[line.site_code_id][line.dev_code_id]=[]
                        tsp=[]
                        tsp.append(line.tsp)
                        data[line.site_code_id][line.dev_code_id].append(tsp)
                        pm01 = []
                        pm01.append(line.pm01)
                        data[line.site_code_id][line.dev_code_id].append(pm01)
                        pm25 = []
                        pm25.append(line.pm25)
                        data[line.site_code_id][line.dev_code_id].append(pm25)
                        pm10 = []
                        pm10.append(line.pm10)
                        data[line.site_code_id][line.dev_code_id].append(pm10)
                        noise = []
                        noise.append(line.noise)
                        data[line.site_code_id][line.dev_code_id].append(noise)
                        temperature = []
                        temperature.append(line.temperature)
                        data[line.site_code_id][line.dev_code_id].append(temperature)
                        humidity = []
                        humidity.append(line.humidity)
                        data[line.site_code_id][line.dev_code_id].append(humidity)
                        winddir = []
                        winddir.append(line.winddir)
                        data[line.site_code_id][line.dev_code_id].append(winddir)
                        windspd = []
                        windspd.append(line.windspd)
                        data[line.site_code_id][line.dev_code_id].append(windspd)
                        rain = []
                        rain.append(line.rain)
                        data[line.site_code_id][line.dev_code_id].append(rain)
                        airpresure = []
                        airpresure.append(line.airpresure)
                        data[line.site_code_id][line.dev_code_id].append(airpresure)
                        lightstr = []
                        lightstr.append(line.lightstr)
                        data[line.site_code_id][line.dev_code_id].append(lightstr)
                        so2 = []
                        so2.append(line.so2)
                        data[line.site_code_id][line.dev_code_id].append(so2)
                        co1 = []
                        co1.append(line.co1)
                        data[line.site_code_id][line.dev_code_id].append(co1)
                        no1 = []
                        no1.append(line.no1)
                        data[line.site_code_id][line.dev_code_id].append(no1)
                        h2s = []
                        h2s.append(line.h2s)
                        data[line.site_code_id][line.dev_code_id].append(h2s)
                        hcho = []
                        hcho.append(line.hcho)
                        data[line.site_code_id][line.dev_code_id].append(hcho)
                        toxicgas = []
                        toxicgas.append(line.toxicgas)
                        data[line.site_code_id][line.dev_code_id].append(toxicgas)
                        rssi = []
                        rssi.append(line.rssi)
                        data[line.site_code_id][line.dev_code_id].append(rssi)
                        pwrind = []
                        pwrind.append(line.pwrind)
                        data[line.site_code_id][line.dev_code_id].append(pwrind)
                    else:
                        data[line.site_code_id][line.dev_code_id][0].append(line.tsp)
                        data[line.site_code_id][line.dev_code_id][1].append(line.pm01)
                        data[line.site_code_id][line.dev_code_id][2].append(line.pm25)
                        data[line.site_code_id][line.dev_code_id][3].append(line.pm10)
                        data[line.site_code_id][line.dev_code_id][4].append(line.noise)
                        data[line.site_code_id][line.dev_code_id][5].append(line.temperature)
                        data[line.site_code_id][line.dev_code_id][6].append(line.humidity)
                        data[line.site_code_id][line.dev_code_id][7].append(line.winddir)
                        data[line.site_code_id][line.dev_code_id][8].append(line.windspd)
                        data[line.site_code_id][line.dev_code_id][9].append(line.rain)
                        data[line.site_code_id][line.dev_code_id][10].append(line.airpresure)
                        data[line.site_code_id][line.dev_code_id][11].append(line.lightstr)
                        data[line.site_code_id][line.dev_code_id][12].append(line.so2)
                        data[line.site_code_id][line.dev_code_id][13].append(line.co1)
                        data[line.site_code_id][line.dev_code_id][14].append(line.no1)
                        data[line.site_code_id][line.dev_code_id][15].append(line.h2s)
                        data[line.site_code_id][line.dev_code_id][16].append(line.hcho)
                        data[line.site_code_id][line.dev_code_id][17].append(line.toxicgas)
                        data[line.site_code_id][line.dev_code_id][18].append(line.rssi)
                        data[line.site_code_id][line.dev_code_id][19].append(line.pwrind)
        else:
            return False
        for key, value in data.items():
            for key_dev, value_dev in data[key].items():
                tsp_aveage_3 = round(np.mean(value_dev[0]), 3)
                pm01_aveage_3 = round(np.mean(value_dev[1]), 3)
                pm25_aveage_3 = round(np.mean(value_dev[2]), 3)
                pm10_aveage_3 = round(np.mean(value_dev[3]), 3)
                noise_aveage_3 = round(np.mean(value_dev[4]), 3)
                temperature_aveage_3 = round(np.mean(value_dev[5]), 3)
                humidity_aveage_3 = round(np.mean(value_dev[6]), 3)
                winddir_aveage_3 = round(np.mean(value_dev[7]), 3)
                windspd_aveage_3 = round(np.mean(value_dev[8]), 3)
                rain_aveage_3 = round(np.mean(value_dev[9]), 3)
                airpresure_aveage_3 = round(np.mean(value_dev[10]), 3)
                lightstr_aveage_3 = round(np.mean(value_dev[11]), 3)
                so2_aveage_3 = round(np.mean(value_dev[12]), 3)
                co1_aveage_3 = round(np.mean(value_dev[13]), 3)
                no1_aveage_3 = round(np.mean(value_dev[14]), 3)
                h2s_aveage_3 = round(np.mean(value_dev[15]), 3)
                hcho_aveage_3 = round(np.mean(value_dev[16]), 3)
                toxicgas_aveage_3 = round(np.mean(value_dev[17]), 3)
                rssi_aveage_3 = round(np.mean(value_dev[18]), 3)
                pwrind_aveage_3 = round(np.mean(value_dev[19]), 3)
                hour.append(
                    dct_t_l3f3dm_hour_report_aqyc(dev_code_id=key_dev, site_code_id=key, hourindex=now_hour,report_date=time_start,
                                                  tsp=tsp_aveage_3, pm01=pm01_aveage_3, pm25=pm25_aveage_3,
                                                  pm10=pm10_aveage_3, noise=noise_aveage_3,
                                                  temperature=temperature_aveage_3,
                                                  humidity=humidity_aveage_3, winddir=winddir_aveage_3,
                                                  windspd=windspd_aveage_3,
                                                  rain=rain_aveage_3, airpresure=airpresure_aveage_3,
                                                  lightstr=lightstr_aveage_3,
                                                  so2=so2_aveage_3, co1=co1_aveage_3, no1=no1_aveage_3,
                                                  h2s=h2s_aveage_3, hcho=hcho_aveage_3,
                                                  toxicgas=toxicgas_aveage_3, rssi=rssi_aveage_3,
                                                  pwrind=pwrind_aveage_3))
        dct_t_l3f3dm_hour_report_aqyc.objects.bulk_create(hour)
        return True
    
    def dft_select_serverid(self):
#         token_expires=dct_t_l3f2cm_device_holops.objects.filter(cpu_id="6CR420WJL2")
#         token_expires=dct_t_l3f2cm_nbiot_ctc_token.objects.filter(serviceid="123")
        token_expires=dct_t_l3f2cm_nbiot_ctc_token.objects.create(appid="123",appsecret='123',serviceid='123',accesstoken='123',refreshtoken='123',accexpires='2019-04-18',refexpires='2019-04-18')
#         print(token_expires.exists())
if __name__ == "__main__":
    aaa().dft_select_serverid()
    # a=10
    # print(str(a).zfill(2))
    # a={}
    # a['statcode']='243761589'
    # a["alarmtype"]='YC_007'
    # mm=aaa()
    # mm.dft_dbi_aqyc_dev_alarmhistory_realtime_req_1(a)
    # a=[{'123':2,"234":3,"345":4}]
    # print("567" in a[0].keys())
    # hour_today = 18
    # for i in range(1, 24):
    #     if hour_today + i < 24:
    #         hour_head1 = str(hour_today + i).zfill(2) + ":00"
    #     else:
    #         hour_head1 = str(hour_today - (24 - i)).zfill(2) + ":00"
    #     print(hour_head1)
#     a={"TimeStart":"2008-01-01","TimeEnd":"2018-12-12",'KeyWord':"","uid":""}
#     mm=aaa()
#     ss=mm.dft_dbi_calculation_hour_data()
#     print(ss)