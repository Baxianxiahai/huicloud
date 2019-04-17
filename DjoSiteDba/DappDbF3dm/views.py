import os,json,io
import pycurl
import numpy as np
from django.db.models import Q
from django.db.models.functions import Concat
from DappDbSnr.models import *
from DappDbF1sym.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbFxprcm.models import *
from DappDbInsertData.DappDbMsgDefine import *
import datetime
# Create your views here.
class dct_classDbiL3apF3dm():

    __MFUN_HCU_SITE_STATUS_INITIAL='I'
    __MFUN_HCU_SITE_STATUS_ATTACH='A'
    __MFUN_HCU_SITE_STATUS_CONFIRM='C'
    __MFUN_L3APL_F3DM_TH_ALARM_NOISE=70
    __MFUN_L3APL_F3DM_TH_ALARM_HUMID=80
    __MFUN_L3APL_F3DM_TH_ALARM_TEMP=45
    __MFUN_L3APL_F3DM_TH_ALARM_PM25=201
    __MFUN_L3APL_F3DM_TH_ALARM_WINDSPD=20
    __MFUN_L3APL_F3DM_TH_ALARM_EMC=100
    __MFUN_L3APL_F3DM_TH_ALARM_WINDDIR=360
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW=15
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH=22
    __MFUN_L3APL_F3DM_TH_ALARM_BATT=20
    __MFUN_HCU_AQYC_SLEEP_DURATION=3600
    __MFUN_L3APL_F2CM_FAVOURSITE_MAX_NUM=5
    __MFUN_HCU_FHYS_SLEEP_DURATION=180
    __MFUN_HCU_SITE_PIC_FILE_TYPE=".jpg"
    __MFUN_HCU_FHYS_PIC_WWW_FOLDER="/avorion/upload/"
    __MFUN_HCU_SITE_PIC_WWW_PATH="/avorion/picture/"

    #FHYS
    __MFUN_HCU_FHYS_PIC_ABS_FOLDER='/var/www/html/avorion/upload/'
    __MFUN_HCU_SITE_PIC_FILE_TYPE=".jpg"

    #云控锁
    
    #锁状态
    __HUITP_IEID_UNI_LOCK_STATE_NULL=0X00
    __HUITP_IEID_UNI_LOCK_STATE_OPEN=0X01
    __HUITP_IEID_UNI_LOCK_STATE_CLOSE=0X02
    __HUITP_IEID_UNI_LOCK_STATE_ALARM=0X03
    __HUITP_IEID_UNI_LOCK_STATE_INVALID=0XFF
    #门状态
    __HUITP_IEID_UNI_DOOR_STATE_NULL=0X00
    __HUITP_IEID_UNI_DOOR_STATE_OPEN=0X01
    __HUITP_IEID_UNI_DOOR_STATE_CLOSE=0X02
    __HUITP_IEID_UNI_DOOR_STATE_ALARM=0X03
    __HUITP_IEID_UNI_DOOR_STATE_INVALID=0XFF
    #电池状态
    __HUITP_IEID_UNI_BAT_STATE_NULL=0X00
    __HUITP_IEID_UNI_BAT_STATE_NORMAL=0X01
    __HUITP_IEID_UNI_BAT_STATE_WARNING=0X02
    __HUITP_IEID_UNI_BAT_STATE_INVALID=0XFF
    #震动状态
    __HUITP_IEID_UNI_SHAKE_STATE_NULL=0X00
    __HUITP_IEID_UNI_SHAKE_STATE_DEACTIVE=0X01
    __HUITP_IEID_UNI_SHAKE_STATE_ACTIVE=0X02
    __HUITP_IEID_UNI_SHAKE_STATE_INVALID=0XFF
    #烟雾状态
    __HUITP_IEID_UNI_SMOKE_STATE_NULL=0X00
    __HUITP_IEID_UNI_SMOKE_STATE_DEACTIVE=0X01
    __HUITP_IEID_UNI_SMOKE_STATE_ACTIVE=0X02
    __HUITP_IEID_UNI_SMOKE_STATE_INVALID=0XFF
    #水浸状态
    __HUITP_IEID_UNI_WATER_STATE_NULL=0X00
    __HUITP_IEID_UNI_WATER_STATE_DEACTIVE=0X01
    __HUITP_IEID_UNI_WATER_STATE_ACTIVE=0X02
    __HUITP_IEID_UNI_WATER_STATE_INVALID=0XFF
    #倾斜状态
    __HUITP_IEID_UNI_FALL_STATE_NULL=0X00
    __HUITP_IEID_UNI_FALL_STATE_DEACTIVE=0X01
    __HUITP_IEID_UNI_FALL_STATE_ACTIVE=0X02
    __HUITP_IEID_UNI_FALL_STATE_INVALID=0XFF
    #状态报告触发事件
    __HUITP_IEID_UNI_CCL_REPORT_TYPE_NULL=0X00
    __HUITP_IEID_UNI_CCL_REPORT_TYPE_PERIOD_EVENT=0X01
    __HUITP_IEID_UNI_CCL_REPORT_TYPE_CLOSE_EVENT=0X02
    __HUITP_IEID_UNI_CCL_REPORT_TYPE_FAULT_EVENT=0X03
    __HUITP_IEID_UNI_CCL_REPORT_TYPE_INVALID=0XFF
    #开锁鉴权请求类型
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_NULL=0X00
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_LOCK=0X01
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_BLE=0X02
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_RFID=0X03
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_PHONE=0X04
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_PID=0X05
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_REQ_TYPE_INVALID=0XFF
    #开锁鉴权响应
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_RESP_NULL=0X00
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_RESP_YES=0X01
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_RESP_NO=0X02
    __HUITP_IEID_UNI_CCL_LOCK_AUTH_RESP_INVALID=0XFF

    __MFUN_L3APL_F2CM_EVENT_TYPE_RFID='R'
    __MFUN_L3APL_F2CM_EVENT_TYPE_BLE='B'
    __MFUN_L3APL_F2CM_EVENT_TYPE_USER='U'
    __MFUN_L3APL_F2CM_EVENT_TYPE_WECHAT='W'
    __MFUN_L3APL_F2CM_EVENT_TYPE_IDCARD='I'
    __MFUN_L3APL_F2CM_EVENT_TYPE_PHONE='P'
    __MFUN_L3APL_F2CM_EVENT_TYPE_XJ='X'
    __MFUN_L3APL_F2CM_EVENT_TYPE_ALARM='A'

    def __dft_dbi_user_statproj_inquery(self,inputData):
        p_list=[]
        pg_list=[]
        uid=inputData
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        for line in result:
            if line.auth_type==1:
                pg_list.append(line.auth_code)
            elif line.auth_type==2:
                p_list.append(line.auth_code)
        for i in range(len(pg_list)):
            result=dct_t_l3f2cm_project_common.objects.filter(pg_code_id=pg_list[i])
            for line in result:
                p_list.append(line.prj_code)

        auth_list=[]
        for i in range(len(p_list)):
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=p_list[i])
            for line in result:
                temp={'stat_code':line.site_code,'p_code':p_list[i]}
                auth_list.append(temp)

        if len(auth_list)==0:return auth_list
        unique_authlist=[]
        for i in range(len(auth_list)):
            if auth_list[i] not in unique_authlist:
                unique_authlist.append(auth_list[i])

        return unique_authlist

    def __dft_dbi_winddir_convert(self,inputData):
        degree=inputData
        if (degree>=337.5 and degree<360) or degree<22.5:
            winddir='北风'
        elif (degree>=22.5 and degree<67.5):
            winddir='东北风'
        elif (degree>=67.5 and degree<112.5):
            winddir='东风'
        elif (degree>=112.5 and degree<157.5):
            winddir='东南风'
        elif (degree>=157.5 and degree<202.5):
            winddir='南风'
        elif (degree>=202.5 and degree<247.5):
            winddir='西南风'
        elif (degree>=247.5 and degree<292.5):
            winddir='西风'
        elif (degree>=292.5 and degree<337.5):
            winddir='西北风'
        else:
            winddir='未知'
        return winddir

    def dft_dbi_siteinfo_inquery_url(self,inputData):
        deviceid=inputData['deviceid']
        result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=deviceid)
        if result.exists():
            for line in result:
                resp=line.cam_url
        else:
            result=dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=deviceid)
            if result.exists():
                for line in result:
                    resp=line.cam_url
        return resp
    
    def dft_dbi_map_active_siteinfo_req(self,inputData):
        uid=inputData['uid']
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        sitelist=[]
        siteStatus=self.__MFUN_HCU_SITE_STATUS_INITIAL
        for i in range(len(auth_list)):
            statCode=auth_list[i]['stat_code']
            result=dct_t_l3f3dm_current_report_aqyc.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    last_report=line.report_time
                    tsp=line.pm01
                    noise=line.noise
                    if tsp>self.__MFUN_L3APL_F3DM_TH_ALARM_PM25:
                        alarmStatus='alarm'
                    elif noise>self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE:
                        alarmStatus='warning'
                    else:
                        alarmStatus='normal'
                    timestamp=int(time.mktime(last_report.timetuple()))
                    currenttime=int(time.time())
                    if currenttime>timestamp+self.__MFUN_HCU_AQYC_SLEEP_DURATION:
                        alarmStatus='disable'
            else:
                alarmStatus='disable'
            Department=""
            Country=""
            Street=""
            Square=""
            resp=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if resp.exists():
                for line in resp:
                    if line.status!=siteStatus:
                        latitude=str(line.latitude)
                        longitude=str(line.longitude)
                        temp={
                            'StatCode':line.site_code,
                            'StatName':line.site_name,
                            'ChargeMan':line.superintendent,
                            'Telephone':line.telephone,
                            'Department':line.department,
                            'Address':line.address,
                            'Country':line.district,#
                            'Street':line.street,#
                            'Square':line.site_area,#
                            'Flag_la':"N",#
                            'Latitude':str(latitude),
                            'Flag_lo':"E",#
                            'Longitude':str(longitude),
                            'ProStartTime':str(line.create_date),
                            'Stage':line.comments,
                            'Status':alarmStatus,
                        }
                        sitelist.append(temp)
        return sitelist
    
    def dft_dbi_fstt_map_active_siteinfo_req_view(self,inputData):
        uid=inputData['uid']
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        sitelist=[]
        siteStatus=self.__MFUN_HCU_SITE_STATUS_INITIAL
        for i in range(len(auth_list)):
            statCode=auth_list[i]['stat_code']
            result=dct_t_l3f3dm_current_report_smartcity.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    last_report=line.report_time
                    tsp=line.pm01
                    noise=line.noise
                    if tsp>self.__MFUN_L3APL_F3DM_TH_ALARM_PM25:
                        alarmStatus='alarm'
                    elif noise>self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE:
                        alarmStatus='warning'
                    else:
                        alarmStatus='normal'
                    timestamp=int(time.mktime(last_report.timetuple()))
                    currenttime=int(time.time())
                    if currenttime>timestamp+self.__MFUN_HCU_AQYC_SLEEP_DURATION:
                        alarmStatus='disable'
            else:
                alarmStatus='disable'
            Department=""
            Country=""
            Street=""
            Square=""
            resp=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if resp.exists():
                for line in resp:
                    if line.status!=siteStatus:
                        latitude=str(line.latitude)
                        longitude=str(line.longitude)
                        temp={
                            'StatCode':line.site_code,
                            'StatName':line.site_name,
                            'ChargeMan':line.superintendent,
                            'Telephone':line.telephone,
                            'Department':line.department,
                            'Address':line.address,
                            'Country':line.district,#
                            'Street':line.street,#
                            'Square':line.site_area,#
                            'Flag_la':"N",#
                            'Latitude':str(latitude),
                            'Flag_lo':"E",#
                            'Longitude':str(longitude),
                            'ProStartTime':str(line.create_date),
                            'Stage':line.comments,
                            'Status':alarmStatus,
                        }
                        sitelist.append(temp)
        return sitelist
    
    
    def dft_dbi_map_inactive_siteinfo_req(self,inputData):
        uid=inputData['uid']
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        site_list=[]
        siteStatus=self.__MFUN_HCU_SITE_STATUS_INITIAL
        for i in range(len(auth_list)):
            statCode=auth_list[i]['stat_code']
            Department = ""
            Country = ""
            Street = ""
            Square = ""
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode,status=siteStatus)
            if result.exists():
                for line in result:
                    latitude = str(line.latitude / 1000000)
                    longitude = str(line.longitude / 1000000)
                    temp = {
                        'StatCode': line.site_code,
                        'StatName': line.site_name,
                        'ChargeMan': line.superintendent,
                        'Telephone': line.telephone,
                        'Department': line.department,
                        'Address': line.address,
                        'Country': line.district,  #
                        'Street': line.street,  #
                        'Square': line.site_area,  #
                        'Flag_la': "N",  #
                        'Latitude': latitude,
                        'Flag_lo': "E",  #
                        'Longitude': longitude,
                        'ProStartTime': line.create_date,
                        'Stage': line.comments,
                    }
                    site_list.append(temp)
        return site_list

    def dft_dbi_favourite_count_process(self,inputData):
        uid=inputData['uid']
        statCode=inputData['statcode']
        result=dct_t_l3f2cm_favour_site.objects.filter(uid_id=uid)
        total=len(result)
        if (total<self.__MFUN_L3APL_F2CM_FAVOURSITE_MAX_NUM):
            resp=dct_t_l3f2cm_favour_site.objects.filter(uid_id=uid,site_code_id=statCode)
            if len(resp)>0:
                for line in resp:
                    sid=line.sid
                    update=dct_t_l3f2cm_favour_site.objects.get(sid=sid)
                    update.uid_id=uid
                    update.save()
            else:
                dct_t_l3f2cm_favour_site.objects.create(uid_id=uid,site_code_id=statCode)
        else:
            resp=dct_t_l3f2cm_favour_site.objects.filter(uid_id=uid,site_code_id=statCode)
            if len(resp)>0:
                sid=resp[0].sid
                update = dct_t_l3f2cm_favour_site.objects.get(sid=sid)
                update.uid_id = uid
                update.save()
            else:
                update=dct_t_l3f2cm_favour_site.objects.filter(uid_id=uid).order_by('-create_time')
                update[0].uid_id=uid
                update[0].site_code_id=statCode
                update[0].save()

    def dft_dbi_favoursite_list_process(self,inputData):
        uid=inputData['uid']
        sitelist=[]
        result=dct_t_l3f2cm_favour_site.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                statCode=line.site_code
                latitude=str(statCode.latitude)
                longitude=str(statCode.longitude)
                temp={
                    'StatCode': line.site_code_id,
                    'StatName': line.site_code.site_name,
                    'ChargeMan': line.site_code.superintendent,
                    'Telephone': line.site_code.telephone,
                    'Department': line.site_code.department,
                    'Address': line.site_code.address,
                    'Country': line.site_code.district,  #
                    'Street': line.site_code.street,  #
                    'Square': line.site_code.site_area,  #
                    'Flag_la': "N",  #
                    'Latitude': latitude,
                    'Flag_lo': "E",  #
                    'Longitude': longitude,
                    'ProStartTime': str(line.site_code.create_date),
                    'Stage': line.site_code.comments,
                }
                sitelist.append(temp)
        return sitelist

    def dft_dbi_aqyc_dev_currentvalue_req(self,inputData):
        statCode=inputData['statcode']
        vcrname=[]
        vcrlink=[]
        vcrlist=[]
        result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code__site_code__dct_t_l3f2cm_device_inventory=statCode)
        if result.exists():
            for line in result:
                vcrname.append("RTSP")
                vcrname.append("CAMCTRL")
                rtsp=line.cam_url
                cam_ctrl=line.ctrl_url
                vcrlink.append(rtsp)
                vcrlink.append(cam_ctrl)
                vcrlist={"vcrname":vcrname,"vcraddress":vcrlink}
        currentvalue=[]
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                noise=round(line.noise,2)
                winddir=line.winddir
                humidity=round(line.humidity,2)
                temperature=round(line.temperature,2)
                tsp=round(line.tsp,2)
                windspeed=round(line.windspd,2)
                last_report=line.report_time
                time_array=time.strptime(str(last_report),"%Y-%m-%d %H:%M:%S.%f")
                print(time_array)
                timestamp=int(time.mktime(time_array))
                currenttime=int(time.time())
                if(currenttime>timestamp+3600):
                    dev_status="休眠中"
                    alarm='false'
                else:
                    dev_status='运行中'
                    alarm='false'
                temp={"AlarmName":"设备状态","AlarmEName":"AQYC_status","AlarmValue":str(dev_status),"AlarmUnit":" ","WarningTarget":alarm}
                if(tsp!=""):
                    if tsp>self.__MFUN_L3APL_F3DM_TH_ALARM_PM25:
                        alarm="true"
                    else:
                        alarm='false'
                    temp = {"AlarmName": "颗粒物", "AlarmEName": "AQYC_pm2.5", "AlarmValue": str(tsp),
                                "AlarmUnit": "μg/m3", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "颗粒物", "AlarmEName": "AQYC_pm2.5", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (noise != ""):
                    if tsp > self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "噪声", "AlarmEName": "AQYC_noise", "AlarmValue": str(noise),
                            "AlarmUnit": "dB", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "噪声", "AlarmEName": "AQYC_noise", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (windspeed != ""):
                    if windspeed > self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "风速", "AlarmEName": "AQYC_windspeed", "AlarmValue": str(windspeed),
                            "AlarmUnit": "m/s", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "风速", "AlarmEName": "AQYC_windspeed", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (winddir != ""):
                    temp = {"AlarmName": "风向", "AlarmEName": "AQYC_winddir", "AlarmValue": self.__dft_dbi_winddir_convert(winddir),
                            "AlarmUnit": " ", "WarningTarget": "false"}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "风向", "AlarmEName": "AQYC_winddir", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (humidity != ""):
                    if humidity > self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "湿度", "AlarmEName": "AQYC_humi", "AlarmValue": str(humidity),
                            "AlarmUnit": "%", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "湿度", "AlarmEName": "AQYC_humi", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (temperature != ""):
                    if temperature > self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "温度", "AlarmEName": "AQYC_temp", "AlarmValue": str(temperature),
                            "AlarmUnit": "°C", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "温度", "AlarmEName": "AQYC_temp", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)
        else:
            currentvalue=""
        resp={'StatCode':statCode,'alarmlist':currentvalue,'vcr':vcrlist}
        return resp
    
    def dft_dbi_fstt_dev_currentvalue_req_view(self,inputData):
        statCode=inputData['statcode']
        vcrname=[]
        vcrlink=[]
        vcrlist=[]
        result=dct_t_l3f2cm_device_fstt.objects.filter(dev_code__site_code__dct_t_l3f2cm_device_inventory=statCode)
        if result.exists():
            for line in result:
                vcrname.append("RTSP")
                vcrname.append("CAMCTRL")
                rtsp=line.cam_url
                cam_ctrl=line.ctrl_url
                vcrlink.append(rtsp)
                vcrlink.append(cam_ctrl)
                vcrlist={"vcrname":vcrname,"vcraddress":vcrlink}
        currentvalue=[]
        result=dct_t_l3f3dm_current_report_smartcity.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                noise=round(line.noise,2)
                winddir=line.winddir
                humidity=round(line.humidity,2)
                temperature=round(line.temperature,2)
                tsp=round(line.tsp,2)
                windspeed=round(line.windspd,2)
                last_report=line.report_time
                time_array=time.strptime(str(last_report),"%Y-%m-%d %H:%M:%S.%f")
                print(time_array)
                timestamp=int(time.mktime(time_array))
                currenttime=int(time.time())
                if(currenttime>timestamp+3600):
                    dev_status="休眠中"
                    alarm='false'
                else:
                    dev_status='运行中'
                    alarm='false'
                temp={"AlarmName":"设备状态","AlarmEName":"AQYC_status","AlarmValue":str(dev_status),"AlarmUnit":" ","WarningTarget":alarm}
                if(tsp!=""):
                    if tsp>self.__MFUN_L3APL_F3DM_TH_ALARM_PM25:
                        alarm="true"
                    else:
                        alarm='false'
                    temp = {"AlarmName": "颗粒物", "AlarmEName": "AQYC_pm2.5", "AlarmValue": str(tsp),
                                "AlarmUnit": "μg/m3", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "颗粒物", "AlarmEName": "AQYC_pm2.5", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (noise != ""):
                    if tsp > self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "噪声", "AlarmEName": "AQYC_noise", "AlarmValue": str(noise),
                            "AlarmUnit": "dB", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "噪声", "AlarmEName": "AQYC_noise", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (windspeed != ""):
                    if windspeed > self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "风速", "AlarmEName": "AQYC_windspeed", "AlarmValue": str(windspeed),
                            "AlarmUnit": "m/s", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "风速", "AlarmEName": "AQYC_windspeed", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (winddir != ""):
                    temp = {"AlarmName": "风向", "AlarmEName": "AQYC_winddir", "AlarmValue": self.__dft_dbi_winddir_convert(winddir),
                            "AlarmUnit": " ", "WarningTarget": "false"}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "风向", "AlarmEName": "AQYC_winddir", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (humidity != ""):
                    if humidity > self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "湿度", "AlarmEName": "AQYC_humi", "AlarmValue": str(humidity),
                            "AlarmUnit": "%", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "湿度", "AlarmEName": "AQYC_humi", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)

                if (temperature != ""):
                    if temperature > self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP:
                        alarm = "true"
                    else:
                        alarm = 'false'
                    temp = {"AlarmName": "温度", "AlarmEName": "AQYC_temp", "AlarmValue": str(temperature),
                            "AlarmUnit": "°C", "WarningTarget": alarm}
                    currentvalue.append(temp)
                else:
                    temp = {"AlarmName": "温度", "AlarmEName": "AQYC_temp", "AlarmValue": "NULL",
                            "AlarmUnit": " ", "WarningTarget": "true"}
                    currentvalue.append(temp)
        else:
            currentvalue=""
        resp={'StatCode':statCode,'alarmlist':currentvalue,'vcr':vcrlist}
        return resp
    
    
    def dft_dbi_aqyc_user_dataaggregate_req(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]
        column.append('监测点编号')
        column.append('监测点名称')
        column.append('项目单位')
        column.append('区县')
        column.append('地址')
        column.append('负责人')
        column.append('联系电话')
        column.append('上次报告时间')
        column.append('设备状态')
        column.append('TSP')
        column.append('温度')
        column.append('湿度')
        column.append('噪音')
        column.append('风速')
        column.append('风向')
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        for i in range(len(auth_list)):
            one_row=[]
            statCode=auth_list[i]['stat_code']
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    one_row.append(statCode)
                    one_row.append(line.site_name)
                    one_row.append(line.department)
                    one_row.append(line.district)
                    one_row.append(line.address)
                    one_row.append(line.superintendent)
                    one_row.append(line.telephone)

            resp=dct_t_l3f3dm_current_report_aqyc.objects.filter(site_code_id=statCode)
            tsp=0
            temperature=0
            humidity=0
            noise=0
            windspeed=0
            winddir=self.__dft_dbi_winddir_convert(0)
            reportTime='NULL'
            status='休眠中'
            if resp.exists():
                for line in resp:
                    tsp=int(line.tsp)
                    temperature=round(line.temperature,2)
                    humidity=round(line.humidity,2)
                    noise=round(line.noise,2)
                    windspeed=round(line.windspd,2)
                    winddir=self.__dft_dbi_winddir_convert(line.winddir)
                    reportTime=line.report_time#???????????????????????
                    currenttimt=int(time.time())
                    timestamp=time.mktime(reportTime.timetuple())
                    if currenttimt>timestamp+self.__MFUN_HCU_AQYC_SLEEP_DURATION:
                        status='休眠中'
                    else:
                        status='运行中'
            one_row.append(str(reportTime))
            one_row.append(status)
            one_row.append(tsp)
            one_row.append(temperature)
            one_row.append(humidity)
            one_row.append(noise)
            one_row.append(windspeed)
            one_row.append(winddir)
            data.append(one_row)
        table={'column':column,'data':data}
        return table
    
    def dft_dbi_fstt_user_dataaggregate_req_view(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]
        column.append('监测点编号')
        column.append('监测点名称')
        column.append('项目单位')
        column.append('区县')
        column.append('地址')
        column.append('负责人')
        column.append('联系电话')
        column.append('上次报告时间')
        column.append('设备状态')
        column.append('TSP')
        column.append('温度')
        column.append('湿度')
        column.append('噪音')
        column.append('风速')
        column.append('风向')
        column.append('光照强度')
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        for i in range(len(auth_list)):
            one_row=[]
            statCode=auth_list[i]['stat_code']
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    one_row.append(statCode)
                    one_row.append(line.site_name)
                    one_row.append(line.department)
                    one_row.append(line.district)
                    one_row.append(line.address)
                    one_row.append(line.superintendent)
                    one_row.append(line.telephone)

            resp=dct_t_l3f3dm_current_report_smartcity.objects.filter(site_code_id=statCode)
            tsp=0
            temperature=0
            humidity=0
            noise=0
            windspeed=0
            winddir=self.__dft_dbi_winddir_convert(0)
            lightStr=0
            reportTime='NULL'
            status='休眠中'
            if resp.exists():
                for line in resp:
                    tsp=int(line.tsp)
                    temperature=round(line.temperature,2)
                    humidity=round(line.humidity,2)
                    noise=round(line.noise,2)
                    windspeed=round(line.windspd,2)
                    winddir=self.__dft_dbi_winddir_convert(line.winddir)
                    lightStr=round(line.lightstr)
                    reportTime=line.report_time
                    currenttimt=int(time.time())
                    timestamp=time.mktime(reportTime.timetuple())
                    if currenttimt>timestamp+self.__MFUN_HCU_AQYC_SLEEP_DURATION:
                        status='休眠中'
                    else:
                        status='运行中'
            one_row.append(str(reportTime))
            one_row.append(status)
            one_row.append(tsp)
            one_row.append(temperature)
            one_row.append(humidity)
            one_row.append(noise)
            one_row.append(windspeed)
            one_row.append(winddir)
            one_row.append(lightStr)
            data.append(one_row)
        table={'column':column,'data':data}
        return table
    
    

    '''波峰组合秤暂时不做'''
    def dft_dbi_bfsc_user_dataaggregate_req(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]

        return False


    def dft_dbi_fhys_user_dataaggregate_req(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        column.append('站点编号')
        column.append('站点名称')
        column.append('区县')
        column.append('地址')
        column.append('负责人')
        column.append('联系电话')
        column.append('设备状态')
        column.append('上次报告时间')
        column.append('门锁-1状态')
        column.append('门锁-2状态')
        column.append('信号强度')
        column.append('剩余电量')
        column.append('温度')
        column.append('湿度')
        column.append('震动告警')
        column.append('倾斜告警')
        column.append('水浸告警')
        for i in  range(len(auth_list)):
            one_row=[]
            statCode=auth_list[i]['stat_code']
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    one_row.append(statCode)
                    one_row.append(line.site_name)
                    one_row.append(line.district)#乡镇
                    one_row.append(line.address)
                    one_row.append(line.superintendent)
                    one_row.append(line.telephone)
            else:
                table={'column':column,'data':data}
                return table
            resp=dct_t_l3f3dm_current_report_fhys.objects.filter(site_code_id=statCode)
            dev_status='状态未知'
            doorlock_1='状态未知'
            doorlock_2='状态未知'
            batt_level='0%'
            vibr_alarm='未知'
            water_alarm='未知'
            fall_alarm='未知'
            gprs='未知'
            temperature='0'
            humidity='0%'
            last_report="0000-00-00 00:00:00"
            if resp.exists():
                for line in resp:
                    last_report=line.report_time
                    timestamp=time.mktime(last_report.timetuple())
                    currenttime=int(time.time())
                    if currenttime>timestamp+self.__MFUN_HCU_FHYS_SLEEP_DURATION:
                        dev_status='休眠中'
                    else:
                        dev_status='运行中'
                    if (line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN):
                        doorlock_1='门锁打开'
                    elif(line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE):
                        doorlock_1='门锁关闭'
                    elif (line.lock_1 == self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1 == self.__HUITP_IEID_UNI_DOOR_STATE_ALARM):
                        doorlock_1 = '暴力开门'
                    elif (line.lock_1 == self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1 == self.__HUITP_IEID_UNI_DOOR_STATE_OPEN):
                        doorlock_1 = '锁关门开'
                    elif (line.lock_1 == self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1 == self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE):
                        doorlock_1 = '锁开门关'
                    else:
                        doorlock_1='状态异常'

                    if (line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN):
                        doorlock_2='门锁打开'
                    elif(line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE):
                        doorlock_2='门锁关闭'
                    elif (line.lock_2 == self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2 == self.__HUITP_IEID_UNI_DOOR_STATE_ALARM):
                        doorlock_2 = '暴力开门'
                    elif (line.lock_2 == self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2 == self.__HUITP_IEID_UNI_DOOR_STATE_OPEN):
                        doorlock_2 = '锁关门开'
                    elif (line.lock_2 == self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_2 == self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE):
                        doorlock_2 = '锁开门关'
                    else:
                        doorlock_2='状态异常'

                    sig_level=int(line.rssivalue)
                    if sig_level<self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW:
                        gprs='较差'
                    elif sig_level>=self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW and sig_level<=self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH:
                        gprs='一般'
                    else:
                        gprs='良好'
                    if line.battvalue<100:
                        batt_level=str(line.battvalue)+'%'
                    else:
                        batt_level='100%'
                    temperature=str(line.tempvalue)+"℃"
                    humidity=str(line.humidvalue)+"%"
                    if line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_ACTIVE:
                        vibr_alarm='有'
                    elif line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_DEACTIVE:
                        vibr_alarm='无'

                    if line.waterstate==self.__HUITP_IEID_UNI_WATER_STATE_ACTIVE:
                        water_alarm='有'
                    elif line.waterstate==self.__HUITP_IEID_UNI_WATER_STATE_DEACTIVE:
                        water_alarm='无'

                    if line.fallstate==self.__HUITP_IEID_UNI_FALL_STATE_ACTIVE:
                        fall_alarm='有'
                    elif line.fallstate==self.__HUITP_IEID_UNI_FALL_STATE_DEACTIVE:
                        fall_alarm='无'
            one_row.append(dev_status)
            one_row.append(str(last_report))
            one_row.append(doorlock_1)
            one_row.append(doorlock_2)
            one_row.append(gprs)
            one_row.append(batt_level)
            one_row.append(temperature)
            one_row.append(humidity)
            one_row.append(vibr_alarm)
            one_row.append(fall_alarm)
            one_row.append(water_alarm)
            data.append(one_row)
        table={'column':column,'data':data}
        return table
    def __dft_func_fhys_map_currentvalue_build(self,inputData):
        devCode=inputData['devCode']
        result=dct_t_l3f3dm_current_report_fhys.objects.filter(dev_code_id=devCode)
        if result.exists():
            for line in result:
                temperature=line.tempvalue
                humidity=line.humidvalue
                battlevel=line.battvalue
                siglevel=line.rssivalue
                currentvalue=[]
                timestamp=time.mktime(line.report_time.timetuple())
                currenttime=int(time.time())
                if currenttime>timestamp+180:
                    decstat='休眠中'
                    alarm='true'
                else:
                    decstat='运行中'
                    alarm='false'
                temp={
                    'AlarmName':'设备状态：',
                    'AlarmEName':'FHYS_fibbox',
                    'AlarmValue':decstat,
                    'AlarmUnit':'',
                    'WarningTarget':alarm
                }
                currentvalue.append(temp)
                if line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_1_status='门锁打开'
                    doorlock_1_alarm='false'
                    doorlock_1_picname='FHYS_locko'
                elif line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_1_status='门锁关闭'
                    doorlock_1_alarm='false'
                    doorlock_1_picname='FHYS_lockc'
                elif line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_ALARM:
                    doorlock_1_status='暴力开门'
                    doorlock_1_alarm='true'
                    doorlock_1_picname='FHYS_door'
                elif line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_1_status='锁关门开'
                    doorlock_1_alarm='false'
                    doorlock_1_picname='FHYS_lockc'
                elif line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_1_status='锁开门关'
                    doorlock_1_alarm='false'
                    doorlock_1_picname='FHYS_locko'
                else:
                    doorlock_1_status = '状态异常'
                    doorlock_1_alarm = 'true'
                    doorlock_1_picname = 'FHYS_locko'
                temp={
                    'AlarmName':'门锁-1 状态','AlarmEName':str(doorlock_1_picname),'AlarmValue':str(doorlock_1_status),'AlarmUnit':'','WarningTarget':doorlock_1_alarm
                }
                currentvalue.append(temp)

                if line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_2_status='门锁打开'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_locko'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_2_status='门锁关闭'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_lockc'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_ALARM:
                    doorlock_2_status='暴力开门'
                    doorlock_2_alarm='true'
                    doorlock_2_picname='FHYS_door'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_2_status='锁关门开'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_lockc'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_2_status='锁开门关'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_locko'
                temp={
                    'AlarmName':'门锁-1 状态','AlarmEName':str(doorlock_2_picname),'AlarmValue':str(doorlock_2_status),'AlarmUnit':'','WarningTarget':doorlock_2_alarm
                }
                currentvalue.append(temp)
                if siglevel != None:
                    if siglevel<self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW:
                        gprs='较差'
                        alarm='true'
                    elif siglevel<=self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH and siglevel >= self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW:
                        gprs = '一般'
                        alarm = 'false'
                    else:
                        gprs = '良好'
                        alarm = 'false'
                    temp={
                        'AlarmName':"信号强度：",
                        'AlarmEName':'FHYS_sig',
                        'AlarmValue':str(gprs),
                        'AlarmUnit':'',
                        'WarningTarget':alarm,
                    }
                else:
                    temp = {
                        'AlarmName': "信号强度：",
                        'AlarmEName': 'FHYS_sig',
                        'AlarmValue': 'NULL',
                        'AlarmUnit': '',
                        'WarningTarget': 'false',
                    }
                currentvalue.append(temp)
                if battlevel!=None:
                    if battlevel<self.__MFUN_L3APL_F3DM_TH_ALARM_BATT:
                        alarm='true'
                    else:
                        alarm='false'
                    if battlevel>100:battlevel=100
                    temp = {
                        'AlarmName': "剩余电量：",
                        'AlarmEName': 'FHYS_batt',
                        'AlarmValue': str(battlevel),
                        'AlarmUnit': ' %',
                        'WarningTarget': alarm,
                    }
                else:
                    temp = {
                        'AlarmName': "剩余电量：",
                        'AlarmEName': 'FHYS_batt',
                        'AlarmValue': 'NULL',
                        'AlarmUnit': '',
                        'WarningTarget': 'false',
                    }
                currentvalue.append(temp)
                if temperature!=None:
                    if temperature>self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP:
                        alarm='true'
                    else:
                        alarm='false'
                    temp = {
                        'AlarmName': "温度：",
                        'AlarmEName': 'FHYS_temp',
                        'AlarmValue': str(temperature),
                        'AlarmUnit': ' °C',
                        'WarningTarget': alarm,
                    }
                else:
                    temp = {
                        'AlarmName': "温度：",
                        'AlarmEName': 'FHYS_temp',
                        'AlarmValue': 'NULL',
                        'AlarmUnit': '',
                        'WarningTarget': 'false',
                    }
                currentvalue.append(temp)
                if humidity!=None:
                    if humidity>self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID:
                        alarm='true'
                    else:
                        alarm='false'
                    temp = {
                        'AlarmName': "湿度：",
                        'AlarmEName': 'FHYS_humi',
                        'AlarmValue': str(humidity),
                        'AlarmUnit': ' %',
                        'WarningTarget': alarm,
                    }
                else:
                    temp = {
                        'AlarmName': "湿度：",
                        'AlarmEName': 'FHYS_humi',
                        'AlarmValue': 'NULL',
                        'AlarmUnit': '',
                        'WarningTarget': 'false',
                    }
                currentvalue.append(temp)
                if line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_ACTIVE:
                    vibralarm='有'
                    alarm='true'
                elif line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_DEACTIVE:
                    vibralarm='无'
                    alarm='false'
                else:
                    vibralarm = '状态未知'
                    alarm = 'true'
                temp = {
                    'AlarmName': "震动告警：",
                    'AlarmEName': 'FHYS_vibr',
                    'AlarmValue': str(vibralarm),
                    'AlarmUnit': '',
                    'WarningTarget': alarm,
                }
                currentvalue.append(temp)
                if line.waterstate==self.__HUITP_IEID_UNI_WATER_STATE_ACTIVE:
                    wateralarm='有'
                    alarm='true'
                elif line.waterstate==self.__HUITP_IEID_UNI_WATER_STATE_DEACTIVE:
                    wateralarm='无'
                    alarm='false'
                else:
                    wateralarm = '未知'
                    alarm = 'true'
                temp = {
                    'AlarmName': "水浸告警：",
                    'AlarmEName': 'FHYS_water',
                    'AlarmValue': str(wateralarm),
                    'AlarmUnit': '',
                    'WarningTarget': alarm,
                }
                currentvalue.append(temp)
                if line.fallstate==self.__HUITP_IEID_UNI_FALL_STATE_ACTIVE:
                    fallalarm='有'
                    alarm='true'
                elif line.fallstate==self.__HUITP_IEID_UNI_FALL_STATE_DEACTIVE:
                    fallalarm='无'
                    alarm='false'
                else:
                    fallalarm = '未知'
                    alarm = 'true'
                temp = {
                    'AlarmName': "水浸告警：",
                    'AlarmEName': 'FHYS_water',
                    'AlarmValue': str(fallalarm),
                    'AlarmUnit': '',
                    'WarningTarget': alarm,
                }
                currentvalue.append(temp)
        else:
            currentvalue=''
        return currentvalue
    '''gtjy暂时先不做'''
    def __dbi_func_gtjy_map_currentvalue_build(self,inputData):
        devCode=inputData['devcode']
        return False

    '''表中数据暂时无法与原表对应，暂时不做'''
    def dft_dbi_fhys_dev_currentvalue_req(self,inputData):
        statCode=inputData['statcode']
        vcrname=[]
        vcrlink=[]
        vcrlist=[]
        devCode=""
        return False

    # def dft_dbi_point_install_picture_process(self,inputData):
    #     statCode=inputData['statcode']
    #     pic_list=[]
    #     path=self.__MFUN_HCU_FHYS_PIC_ABS_FOLDER+statCode
    #     if os.path.exists(path)==False:
    #         return pic_list
    #     imgFile=glob.glob(path+'/*'+self.__MFUN_HCU_SITE_PIC_FILE_TYPE)
    #     for i in range(len(imgFile)):
    #         file=imgFile[i]
    #         if os.path.isdir(file):
    #             pass
    #         else:
    #             name=(file.split('\\')[len(file.split('\\')) - 1])
    #             url=self.__MFUN_HCU_FHYS_PIC_WWW_FOLDER+statCode+'\\'+name
    #             temp={'name':name,'url':url}
    #             pic_list.append(temp)
    #     return pic_list

    def dft_dbi_key_event_history_process(self,inputData):
        projCode=inputData['projCode']
        duration=inputData['duration']
        keyWord=inputData['keyWord']
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('站点名称')
        ColumnName.append('事件时间')
        ColumnName.append('事件类型')
        ColumnName.append('钥匙编号')
        ColumnName.append('钥匙名称')
        ColumnName.append('使用者工号')
        ColumnName.append('使用者姓名')
        end=datetime.datetime.today()
        start=end
        if duration=='1':
            start=end-datetime.timedelta(days=1)
        elif duration=='7':
            start = end - datetime.timedelta(days=7)
        elif duration=='30':
            start = end - datetime.timedelta(days=30)
        result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=projCode)
        print(result)
        if result.exists():
            for line in result:
                statCode=line.site_code
                statName=line.site_name
                if keyWord!="":
                    resp=dct_t_l3fxprcm_locklog_fhys.objects.filter(site_code=statCode,createtime__gte=start,createtime__lte=end,ownername__icontains=keyWord)
                    if resp.exists():
                        for li in resp:
                            sid=li.sid
                            keyid=li.keyid
                            keyname=li.keyname
                            keyuserid=li.ownerid
                            keyusername=li.ownername
                            eventtype=li.eventtype
                            eventtime=li.createtime
                            if eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_RFID:
                                eventtype='RFID开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_BLE:
                                eventtype='蓝牙开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_USER:
                                eventtype='用户账号开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_IDCARD:
                                eventtype='身份证开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_WECHAT:
                                eventtype='微信开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_PHONE:
                                eventtype='电话号码开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_XJ:
                                eventtype='巡检事件'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_ALARM:
                                eventtype='未授权开锁'
                            else:
                                eventtype = '未知事件'
                            temp=[]
                            temp.append(sid)
                            temp.append(statName)
                            temp.append(str(eventtime))
                            temp.append(eventtype)
                            temp.append(keyid)
                            temp.append(keyname)
                            temp.append(keyuserid)
                            temp.append(keyusername)
                            TableData.append(temp)
                else:
                    print(start)
                    print(end)
                    resp=dct_t_l3fxprcm_locklog_fhys.objects.filter(site_code=statCode,createtime__gte=start,createtime__lte=end)
                    print(resp)
                    if resp.exists():
                        for li in resp:
                            sid=li.sid
                            keyid=li.keyid
                            keyname=li.keyname
                            keyuserid=li.ownerid
                            keyusername=li.ownername
                            eventtype=li.eventtype
                            eventtime=li.createtime
                            if eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_RFID:
                                eventtype='RFID开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_BLE:
                                eventtype='蓝牙开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_USER:
                                eventtype='用户账号开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_IDCARD:
                                eventtype='身份证开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_WECHAT:
                                eventtype='微信开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_PHONE:
                                eventtype='电话号码开锁'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_XJ:
                                eventtype='巡检事件'
                            elif eventtype==self.__MFUN_L3APL_F2CM_EVENT_TYPE_ALARM:
                                eventtype='未授权开锁'
                            else:
                                eventtype = '未知事件'
                            temp=[]
                            temp.append(sid)
                            temp.append(statName)
                            temp.append(str(eventtime))
                            temp.append(eventtype)
                            temp.append(keyid)
                            temp.append(keyname)
                            temp.append(keyuserid)
                            temp.append(keyusername)
                            TableData.append(temp)
        history={"ColumnName":ColumnName,"TableData":TableData}
        return history


    def dft_dbi_door_open_picture_process(self,inputData):
        enventid=inputData['enventid']
        result=dct_t_l3fxprcm_locklog_fhys.objects.filter(sid=enventid)
        pic_result=[]
        if result.exists():
            for line in result:
                file_name=line.picname
                statCode=line.site_code
                if file_name!="":
                    file_url=self.__MFUN_HCU_SITE_PIC_WWW_PATH+str(statCode)+"/"+file_name
                    pic_result={
                        "ifpicture":'true',
                        'picture':file_url,
                    }
                else:
                    pic_result = {
                        "ifpicture": 'false',
                        'picture': "",
                    }
        return pic_result

    def dft_dbi_point_install_picture_process(self,inputData):
        statCode=inputData['statcode']
        pic_list=[]
        path=self.__MFUN_HCU_FHYS_PIC_ABS_FOLDER+statCode
        if os.path.exists(path)==False:
            return pic_list
        for afile in path+"/*"+self.__MFUN_HCU_SITE_PIC_FILE_TYPE:
            if os.path.isdir(afile):
                continue
            else:
                str_arr=afile.split('/')
                file_name=str_arr[len(str_arr)-1]
                file_url=self.__MFUN_HCU_FHYS_PIC_WWW_FOLDER+statCode+'/'+file_name
                temp={'name':file_name,'url':file_url}
                pic_list.append(temp)
        return pic_list
    
    def dft_dbi_HCU_Info_Query(self,inputData):
        dev_code=inputData['key']
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=dev_code)
        resp=dct_t_l3f3dm_current_report_smartcity.objects.filter(dev_code_id=dev_code)
        retlist=[]
        if result.exists():
#             print('dct_t_l3f3dm_current_report_aqyc')
            for line in result:
                map='设备编号：'+str(dev_code)
                retlist.append(map)
                map='最后一次上报时间：'+str(line.report_time)
                retlist.append(map)
                map = 'BASE_PORT：' + str(line.dev_code.base_port).ljust(5).replace(" ",'0') 
                retlist.append(map)
                map = '第三方编号：' + line.dev_code.zhb_label
                retlist.append(map)
                map = '软件版本：' + str(line.dev_code.sw_ver)
                retlist.append(map)
                map = 'TSP：' + str(int(line.tsp))+'μg/m³'
                retlist.append(map)
                map = 'PM01：' + str(round(line.pm01,2))+'μg/m³'
                retlist.append(map)
                map = 'PM2.5：' + str(round(line.pm25,2) )+'μg/m³'
                retlist.append(map)
                map = 'PM10：' + str(round(line.pm10,2))+'μg/m³ '
                retlist.append(map)
                map = '噪音：' + str(round(line.noise,2))+'dB'
                retlist.append(map)
                map = '温度：' + str(round(line.temperature,2) )+"℃"
                retlist.append(map)
                map = '湿度：' + str(round(line.humidity,2) )+"%"
                retlist.append(map)
                map = '风向：' + str(self.__dft_dbi_winddir_convert(line.winddir))
                retlist.append(map)
                map = '风速：' + str(round(line.windspd,2))+"m/s"
                retlist.append(map)
                map = '二氧化氮：：' + str(round(line.no2,4))+"mg/m³"
                retlist.append(map)
        elif resp.exists():
#             print('dct_t_l3f3dm_current_report_smartcity')
            for line in resp:
                map='设备编号：'+str(dev_code)
                retlist.append(map)
                map='最后一次上报时间：'+str(line.report_time)
                retlist.append(map)
                map = 'BASE_PORT：' + str(line.dev_code.base_port).ljust(5).replace(" ",'0') 
                retlist.append(map)
                map = '第三方编号：' + line.dev_code.zhb_label
                retlist.append(map)
                map = '软件版本：' + str(line.dev_code.sw_ver)
                retlist.append(map)
                map = 'TSP：' + str(int(line.tsp))+'μg/m³'
                retlist.append(map)
                map = 'PM01：' + str(round(line.pm01,2))+'μg/m³'
                retlist.append(map)
                map = 'PM2.5：' + str(round(line.pm25,2) )+'μg/m³'
                retlist.append(map)
                map = 'PM10：' + str(round(line.pm10,2))+'μg/m³ '
                retlist.append(map)
                map = '噪音：' + str(round(line.noise,2))+'dB'
                retlist.append(map)
                map = '温度：' + str(round(line.temperature,2) )+"℃"
                retlist.append(map)
                map = '湿度：' + str(round(line.humidity,2) )+"%"
                retlist.append(map)
                map = '风向：' + str(self.__dft_dbi_winddir_convert(line.winddir))
                retlist.append(map)
                map = '风速：' + str(round(line.windspd,2))+"m/s"
                retlist.append(map)
                map = '光照强度：' + str(round(line.lightstr,2))
                retlist.append(map)
                map = '灯带工作模式：' + str(round(line.lampmode,2))
                retlist.append(map)
        retval={'status':'true','auth':'true','msg':'获取设备状态成功','ret':retlist}
        return retval
    
    '''每小时定时计算各个数值的小时平均值'''
    def dft_dbi_calculation_hour_data(self):
        time_old = datetime.datetime.now() - datetime.timedelta(hours=1)
        now_date = time_old.date()
        now_hour = time_old.hour
        time_start=str(now_date)+" "+str(now_hour)+":00:00"
        time_end=str(now_date)+" "+str(now_hour)+":59:59"
        data={}
        hour=list()
        result_min=dct_t_l3f3dm_minute_report_aqyc.objects.filter(report_date__range=(time_start,time_end))
        if result_min.exists():
            for line in result_min:
                # print(line.report_date)
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
                        no2 = []
                        no2.append(line.no2)
                        data[line.site_code_id][line.dev_code_id].append(no2)
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
                        data[line.site_code_id][line.dev_code_id][19].append(line.no2)
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
                        no2 = []
                        no2.append(line.no2)
                        data[line.site_code_id][line.dev_code_id].append(no2)
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
                        data[line.site_code_id][line.dev_code_id][19].append(line.no2)
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
                no2_aveage_3 = round(np.mean(value_dev[20]), 3)
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
                                                  pwrind=pwrind_aveage_3,no2=no2_aveage_3))
        dct_t_l3f3dm_hour_report_aqyc.objects.bulk_create(hour)
        return True

    '''每天定时计算各个数值的小时平均值'''

    def dft_dbi_calculation_day_data(self):
        time_old = datetime.datetime.now() - datetime.timedelta(days=1)
        now_date = time_old.date()
        time_start = str(now_date) + " " +"00:00:00"
        time_end = str(now_date) + " " + "23:59:59"
        data = {}
        day = list()
        result_min = dct_t_l3f3dm_minute_report_aqyc.objects.filter(report_date__range=(time_start, time_end))
        if result_min.exists():
            for line in result_min:
                # print(line.report_date)
                if line.site_code_id not in data.keys():
                    data[line.site_code_id] = {}
                    if line.dev_code_id not in data[line.site_code_id].keys():
                        data[line.site_code_id][line.dev_code_id] = []
                        tsp = []
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
                        no2 = []
                        no2.append(line.no2)
                        data[line.site_code_id][line.dev_code_id].append(no2)
                        # rssi = []
                        # rssi.append(line.rssi)
                        # data[line.site_code_id][line.dev_code_id].append(rssi)
                        # pwrind = []
                        # pwrind.append(line.pwrind)
                        # data[line.site_code_id][line.dev_code_id].append(pwrind)
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
                        data[line.site_code_id][line.dev_code_id][18].append(line.no2)
                        # data[line.site_code_id][line.dev_code_id][18].append(line.rssi)
                        # data[line.site_code_id][line.dev_code_id][19].append(line.pwrind)
                else:
                    if line.dev_code_id not in data[line.site_code_id].keys():
                        data[line.site_code_id][line.dev_code_id] = []
                        tsp = []
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
                        no2 = []
                        no2.append(line.no2)
                        data[line.site_code_id][line.dev_code_id].append(no2)
                        # rssi = []
                        # rssi.append(line.rssi)
                        # data[line.site_code_id][line.dev_code_id].append(rssi)
                        # pwrind = []
                        # pwrind.append(line.pwrind)
                        # data[line.site_code_id][line.dev_code_id].append(pwrind)
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
                        data[line.site_code_id][line.dev_code_id][17].append(line.no2)
                        # data[line.site_code_id][line.dev_code_id][18].append(line.rssi)
                        # data[line.site_code_id][line.dev_code_id][19].append(line.pwrind)
        else:
            return False
        for key, value in data.items():
            for key_dev, value_dev in data[key].items():
                tsp_aveage_3 = round(np.mean(value_dev[0]), 3)
                tsp_max=max(value_dev[0])
                tsp_min=min(value_dev[0])
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
                no2_aveage_3 = round(np.mean(value_dev[18]), 3)
                # rssi_aveage_3 = round(np.mean(value_dev[18]), 3)
                # pwrind_aveage_3 = round(np.mean(value_dev[19]), 3)
                day.append(
                    dct_t_l3f3dm_day_report_aqyc(dev_code_id=key_dev, site_code_id=key,
                                                  report_date=str(now_date),
                                                  tsp=tsp_aveage_3, tsp_max=tsp_max,tsp_min=tsp_min,pm01=pm01_aveage_3, pm25=pm25_aveage_3,
                                                  pm10=pm10_aveage_3, noise=noise_aveage_3,
                                                  temperature=temperature_aveage_3,
                                                  humidity=humidity_aveage_3, winddir=winddir_aveage_3,
                                                  windspd=windspd_aveage_3,
                                                  rain=rain_aveage_3, airpresure=airpresure_aveage_3,
                                                  lightstr=lightstr_aveage_3,
                                                  so2=so2_aveage_3, co1=co1_aveage_3, no1=no1_aveage_3,
                                                  h2s=h2s_aveage_3, hcho=hcho_aveage_3,
                                                  toxicgas=toxicgas_aveage_3,no2=no2_aveage_3
                                                 # ,rssi=rssi_aveage_3, pwrind=pwrind_aveage_3
                                                 ))
        dct_t_l3f3dm_day_report_aqyc.objects.bulk_create(day)
        return True

    def dft_dbi_aqyc_current_report_php_view(self,inputData):
        dev_code=inputData['devCode']
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=dev_code)
        tsp = 0
        pm01 = 0
        pm25 = 0
        pm10 = 0
        noise = 0
        temperature = 0
        humidity = 0
        winddir = 0
        windspd = 0
        rain = 0
        airpresure = 0
        lightstr = 0
        so2 = 0
        co1 = 0
        no1 = 0
        h2s = 0
        hcho = 0
        toxicgas = 0
        rssi = 0
        pwrind=0
        no2 = 0
        report_date=str(datetime.datetime.now())
        status='true'
        if result.exists():
            for line in result:
                report_date=str(line.report_time)
                tsp=line.tsp
                pm01=line.pm01
                pm25=line.pm25
                pm10=line.pm10
                noise=line.noise
                temperature=line.temperature
                humidity=line.humidity
                winddir=line.winddir
                windspd=line.windspd
                rain=line.rain
                airpresure=line.airpresure
                lightstr=line.lightstr
                so2=line.so2
                co1=line.co1
                no1=line.no1
                h2s=line.h2s
                hcho=line.hcho
                toxicgas=line.toxicgas
                rssi=line.rssi
                pwrind=line.pwrind
                no2=line.no2
        else:
            status='false'
        resp_data={'report_time':report_date,
                   'tsp':tsp,
                   'pm01':pm01,
                   'pm25':pm25,
                   'pm10':pm10,
                   'noise':noise,
                   'temperature':temperature,
                   'humidity':humidity,
                   'winddir':winddir,
                   'windspd':windspd,
                   'rain':rain,
                   'airpresure':airpresure,
                   'lightstr':lightstr,
                   'so2':so2,
                   'co1':co1,
                   'no1':no1,
                   'h2s':h2s,
                   'hcho':hcho,
                   'toxicgas':toxicgas,
                   'rssi':rssi,
                   'pwrind':pwrind,
                   'no2':no2,

                   }
        resp={'status':status,'data':resp_data}
        return resp
class dct_t_HCU_Data_Report():
    def __init__(self):
        pass
    
    def dft_dbi_aqyc_current_report(self,socketId,inputData):
        devCode=inputData['FrUsr']
        ServerName=inputData['ToUsr']
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            currentTime=inputData['CrTim']
            currentData = inputData['IeCnt']
            if 'pm1d0Value' in currentData.keys():pm1d0Value = currentData['pm1d0Value']
            else:pm1d0Value=0
            if 'pm2d5Value' in currentData.keys():pm2d5Value = currentData['pm2d5Value']
            else:pm2d5Value=0
            if 'pm10Value' in currentData.keys():pm10Value = currentData['pm10Value']
            else:pm10Value=0
            if 'tspValue' in currentData.keys():tspValue = currentData['tspValue']
            else:tspValue=0
            if 'tempValue' in currentData.keys():tempValue = currentData['tempValue']
            else:tempValue=0
            if 'humidValue' in currentData.keys():humidValue = currentData['humidValue']
            else:humidValue=0
            if 'winddirValue' in currentData.keys():winddirValue = currentData['winddirValue']
            else:winddirValue=0
            if 'windspdValue' in currentData.keys():windspdValue = currentData['windspdValue']
            else:windspdValue=0
            if 'lightstrValue' in currentData.keys():lightstrValue = currentData['lightstrValue']
            else:lightstrValue=0
            if 'so2Value' in currentData.keys():so2Value = currentData['so2Value']
            else:so2Value=0
            if 'co1Value' in currentData.keys():co1Value = currentData['co1Value']
            else:co1Value=0
            if 'co2Value' in currentData.keys():co2Value = currentData['co2Value']
            else:co2Value=0
            if 'no1Value' in currentData.keys():no1Value = currentData['no1Value']
            else:no1Value=0
            if 'hsValue' in currentData.keys():hsValue = currentData['hsValue']
            else:hsValue=0
            if 'hchoValue' in currentData.keys():hchoValue = currentData['hchoValue']
            else:hchoValue=0
            if 'toxicgasValue' in currentData.keys():toxicgasValue = currentData['toxicgasValue']
            else:toxicgasValue=0
            if 'rssiValue' in currentData.keys():rssiValue = currentData['rssiValue']
            else:rssiValue=0
            if 'workContMins' in currentData.keys():workContMins = currentData['workContMins']
            else:workContMins=0
            if 'pwrInd' in currentData.keys():pwrInd = currentData['pwrInd']
            else:pwrInd=0
            if 'noiseValue' in currentData.keys():noiseValue = currentData['noiseValue']
            else:noiseValue=0
            if 'wst' in currentData.keys():wst = currentData['wst']
            else:wst=0
            if 'apr' in currentData.keys():apr = currentData['apr']
            else:apr=0
            if 'atd' in currentData.keys():atd = currentData['atd']
            else:atd=0
            if 'so2' in currentData.keys():so2Value = currentData['so2']
            else:so2Value=0
            if 'no1' in currentData.keys():no1Value = currentData['no1']
            else:no1Value=0
            if 'no2' in currentData.keys():no2 = currentData['no2']
            else:no2=0
            if 'co1' in currentData.keys():co1Value = currentData['co1']
            else:co1Value=0
            if 'co2' in currentData.keys():co2Value = currentData['co2']
            else:co2Value=0
            if 'o3' in currentData.keys():o3 = currentData['o3']
            else:o3=0
            if 'h2s' in currentData.keys():hsValue = currentData['h2s']
            else:hsValue=0
            if 'ph' in currentData.keys():ph = currentData['ph']
            else:ph=0
            if 'ch4' in currentData.keys():ch4 = currentData['ch4']
            else:ch4=0
            if 'ach' in currentData.keys():ph = currentData['ach']
            else:ph=0
            if 'hcho' in currentData.keys():hchoValue = currentData['hcho']
            else:hchoValue=0
            if 'voc' in currentData.keys():voc = currentData['voc']
            else:voc=0
            if 'tox' in currentData.keys():toxicgasValue = currentData['tox']
            else:toxicgasValue=0
            
#             currentTime=inputData['CrTim']
#             currentData = inputData['IeCnt']
#             pm1d0Value = currentData['pm1d0Value']
#             pm2d5Value = currentData['pm2d5Value']
#             pm10Value = currentData['pm10Value']
#             tspValue = currentData['tspValue']
#             tempValue = currentData['tempValue']
#             humidValue = currentData['humidValue']
#             winddirValue = currentData['winddirValue']
#             windspdValue = currentData['windspdValue']
#             noiseValue = currentData['noiseValue']
#             lightstrValue = currentData['lightstrValue']
#             so2Value = currentData["so2Value"]
#             co1Value = currentData["co1Value"]
#             co2Value = currentData["co2Value"]
#             no1Value = currentData["no1Value"]
#             hsValue = currentData["hsValue"]
#             hchoValue = currentData["hchoValue"]
#             toxicgasValue = currentData["toxicgasValue"]
#             rssiValue = currentData["rssiValue"]
#             workContMins = currentData["workContMins"]
#             pwrInd = currentData["pwrInd"]
            timeArray=time.localtime(currentTime)
            hourminindex=timeArray.tm_hour*60+timeArray.tm_min
            dct_t_l3f3dm_minute_report_aqyc.objects.create(dev_code_id=devCode,site_code=result[0].site_code,
                                                           hourminindex=hourminindex,tsp=tspValue,pm01=pm1d0Value,
                                                           pm25=pm2d5Value,pm10=pm10Value,noise=noiseValue,temperature=tempValue,
                                                           humidity=humidValue,winddir=winddirValue,windspd=windspdValue,
                                                           lightstr=lightstrValue,so2=so2Value,co1=co1Value,no1=no1Value,h2s=hsValue,
                                                           hcho=hchoValue,toxicgas=toxicgasValue,rssi=rssiValue,pwrind=pwrInd,no2=no2)
#             dct_t_l2snr_dust.objects.create(dev_code_id=devCode,tsp=tspValue,pm01=pm1d0Value,pm25=pm2d5Value,pm10=pm10Value,hourminindex=hourminindex,dataflag='Y')
#             dct_t_l2snr_windspd.objects.create(dev_code_id=devCode,windspd=windspdValue,dataflag='Y',hourminindex=hourminindex)
#             dct_t_l2snr_noise.objects.create(dev_code_id=devCode,noise=noiseValue,dataflag='Y',hourminindex=hourminindex)
#             dct_t_l2snr_temperature.objects.create(dev_code_id=devCode,temperature=tempValue,dataflag='Y',hourminindex=hourminindex)
#             dct_t_l2snr_humidity.objects.create(dev_code_id=devCode,humidity=humidValue,dataflag='Y',hourminindex=hourminindex)
#             dct_t_l2snr_winddir.objects.create(dev_code_id=devCode,windir=winddirValue,dataflag='Y',hourminindex=hourminindex)
            if dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=devCode).exists():
                dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=devCode).update(site_code=result[0].site_code,report_time=datetime.datetime.now(),tsp=tspValue,pm01=pm1d0Value,
                                                           pm25=pm2d5Value,pm10=pm10Value,noise=noiseValue,temperature=tempValue,
                                                           humidity=humidValue,winddir=winddirValue,windspd=windspdValue,
                                                           lightstr=lightstrValue,so2=so2Value,co1=co1Value,no1=no1Value,h2s=hsValue,
                                                           hcho=hchoValue,toxicgas=toxicgasValue,rssi=rssiValue,pwrind=pwrInd,no2=no2)
            else:
                dct_t_l3f3dm_current_report_aqyc.objects.create(dev_code_id=devCode,site_code=result[0].site_code,tsp=tspValue, pm01=pm1d0Value,pm25=pm2d5Value, pm10=pm10Value, noise=noiseValue, temperature=tempValue,humidity=humidValue, winddir=winddirValue, windspd=windspdValue,
                                                                lightstr=lightstrValue,so2=so2Value,co1=co1Value,no1=no1Value,h2s=hsValue,
                                                                hcho=hchoValue,toxicgas=toxicgasValue,rssi=rssiValue,pwrind=pwrInd,no2=no2)
            result={'socketid':socketId,'data':{'ToUsr':devCode,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0x3010,'MsgLn':115,"IeCnt":{'cfmYesOrNo':1},"FnFlg":0}}
            msg_len=len(json.dumps(result))
            Msg_final={'socketid':socketId,'data':{'ToUsr':devCode,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0x3010,'MsgLn':msg_len,"IeCnt":{'cfmYesOrNo':1},"FnFlg":0}}
        else:
            result={'socketid':socketId,'data':{'ToUsr':devCode,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0x3010,'MsgLn':115,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
            msg_len=len(json.dumps(result))
            Msg_final={'socketid':socketId,'data':{'ToUsr':devCode,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0x3010,'MsgLn':msg_len,"IeCnt":{'cfmYesOrNo':0},"FnFlg":0}}
        return Msg_final
    
    def dft_dbi_smart_city_current_report_view(self, socketId, inputData):
        devCode = inputData['FrUsr']
        ServerName = inputData['ToUsr']
        resp=dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=devCode)
        if resp.exists():
            resp.update(socket_id=socketId)
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            currentTime = inputData['CrTim']
            currentData = inputData['IeCnt']
            pm1d0Value = currentData['pm1d0Value']
            pm2d5Value = currentData['pm2d5Value']
            pm10Value = currentData['pm10Value']
            tspValue = currentData['tspValue']
            tempValue = currentData['tempValue']
            humidValue = currentData['humidValue']
            winddirValue = currentData['winddirValue']
            windspdValue = currentData['windspdValue']
            noiseValue = currentData['noiseValue']
            lightStr = currentData['lightStr']
            lampWorkMode = currentData['lampWorkMode']
#             smartCityRollingPoleVoltageState=currentData['smartCityRollingPoleVoltageState']
            timeArray = time.localtime(currentTime)
            hourminindex = timeArray.tm_hour * 60 + timeArray.tm_min
            dct_t_l3f3dm_minute_report_smartcity.objects.create(dev_code_id=devCode,site_code=result[0].site_code,
                                                                report_date=datetime.datetime.now(),
                                                                hourminindex=hourminindex,tsp=tspValue,pm01=pm1d0Value,pm25=pm2d5Value,pm10=pm10Value,
                                                                noise=noiseValue,temperature=tempValue,humidity=humidValue,winddir=winddirValue,
                                                                windspd=windspdValue,lightstr=lightStr,lampmode=lampWorkMode)
            dct_t_l2snr_dust.objects.create(dev_code_id=devCode, tsp=tspValue, pm01=pm1d0Value, pm25=pm2d5Value,
                                            pm10=pm10Value, hourminindex=hourminindex, dataflag='Y')
            dct_t_l2snr_windspd.objects.create(dev_code_id=devCode, windspd=windspdValue, dataflag='Y',
                                               hourminindex=hourminindex)
            dct_t_l2snr_noise.objects.create(dev_code_id=devCode, noise=noiseValue, dataflag='Y',
                                             hourminindex=hourminindex)
            dct_t_l2snr_temperature.objects.create(dev_code_id=devCode, temperature=tempValue, dataflag='Y',
                                                   hourminindex=hourminindex)
            dct_t_l2snr_humidity.objects.create(dev_code_id=devCode, humidity=humidValue, dataflag='Y',
                                                hourminindex=hourminindex)
            dct_t_l2snr_winddir.objects.create(dev_code_id=devCode, windir=winddirValue, dataflag='Y',
                                               hourminindex=hourminindex)

            if dct_t_l3f3dm_current_report_smartcity.objects.filter(dev_code_id=devCode).exists():
                dct_t_l3f3dm_current_report_smartcity.objects.filter(dev_code_id=devCode).update(
                    site_code=result[0].site_code, report_time=datetime.datetime.now(),
                    tsp=tspValue, pm01=pm1d0Value, pm25=pm2d5Value, pm10=pm10Value,
                    noise=noiseValue, temperature=tempValue, humidity=humidValue, winddir=winddirValue,
                    windspd=windspdValue, lightstr=lightStr, lampmode=lampWorkMode)
            else:
                dct_t_l3f3dm_current_report_smartcity.objects.create(dev_code_id=devCode, site_code=result[0].site_code,report_time=datetime.datetime.now(),
                                                                tsp=tspValue,pm01=pm1d0Value,pm25=pm2d5Value,pm10=pm10Value,
                                                                noise=noiseValue,temperature=tempValue,humidity=humidValue,winddir=winddirValue,
                                                                windspd=windspdValue,lightstr=lightStr,lampmode=lampWorkMode)
            Msg_final = {'socketid': socketId,
                         'data': {'ToUsr': devCode, 'FrUsr': ServerName, "CrTim": int(time.time()),
                                  'MsgTp': 'huitp_json', 'MsgId': GOLBALVAR.HUITPJSON_MSGID_SMART_CITY_DATA_CONFIRM, 'MsgLn': 115, "IeCnt": {'cfmYesOrNo': 1},
                                  "FnFlg": 0}}
        else:
            Msg_final = {'socketid': socketId,
                         'data': {'ToUsr': devCode, 'FrUsr': ServerName, "CrTim": int(time.time()),
                                  'MsgTp': 'huitp_json', 'MsgId': GOLBALVAR.HUITPJSON_MSGID_SMART_CITY_DATA_CONFIRM, 'MsgLn': 115, "IeCnt": {'cfmYesOrNo': 0},
                                  "FnFlg": 0}}
        return Msg_final
    '''系统定时发送告警信息'''
#     def dft_dbi_check_device_status(self):
#         time_now=int(time.time())
#         result_device=dct_t_l3f3dm_current_report_aqyc.objects.all()
#         for line in result_device:
#             report_time=str(line.report_time)
#             response_tsp=line.tsp
#             stand=100
#             timeArray=time.strptime(report_time, "%Y-%m-%d %H:%M:%S.%f")
#             time_report=time.mktime(timeArray)
#             outTimeFlag=line.cmd_flag[0:0]
#             tspErrorFlag=line.cmd_flag[1:1]
#             if(time_now-time_report>1800):
#                 if outTimeFlag=="0":
#                     prj_code=line.site_code.prj_code_id
#                     pg_code=line.site_code.prj_code.pg_code_id
#                 else:
#                     pass
#             if response_tsp>stand:
#                 if tspErrorFlag=="0":
#                     send_msg='true'
#                 else:
#                     pass
#             print(timeArray)
#             print(int(time.mktime(timeArray)))
#     def dft_dbi_send_stand_msg(self,msg):
#         pass



class dct_t_iot_data_report():
    def dft_dbi_nb_iot_curl_token(self,appId,secret,refresh,topken_type):
        print(topken_type)
        if topken_type=="access":
            login_url='https://180.101.147.89:8743/iocm/app/sec/v1.1.0/login'
            login_data = 'appId=' + appId + '&secret=' + secret
        else:
            login_url = 'https://180.101.147.89:8743/iocm/app/sec/v1.1.0/refreshToken'
            data = {"appId":appId,"secret":secret,"refreshToken":refresh}
            login_data=json.dumps(data)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, login_url)
        curl.setopt(pycurl.SSL_VERIFYPEER, False)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.AUTOREFERER, 1)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, login_data)
        curl.setopt(pycurl.TIMEOUT, 30)
        buf = io.BytesIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded'])
        curl.setopt(pycurl.SSLCERT, '/var/www/html/outgoing.CertwithKey.pem')
        curl.setopt(pycurl.SSLCERTPASSWD, "IoM@1234")
        curl.perform()
        curlData = json.loads(buf.getvalue(),encoding='utf8')
        curl.close()
        return curlData
    def dft_dbi_nb_iot_data_report_view(self,serviceId,inputData):
        FrUsr = inputData['FrUsr']
        FnFlg=inputData['FnFlg']
        print(serviceId)
        token_expires=dct_t_l3f2cm_nbiot_ctc_token.objects.filter(serviceid=serviceId)
        print(token_expires)
        if token_expires.exists():
            token=token_expires[0].accesstoken
            accexpires=token_expires[0].accexpires
            if(accexpires<datetime.datetime.now()):
                curl_data=self.dft_dbi_nb_iot_curl_token(token_expires[0].appid,token_expires[0].appsecret,"","access")
                accessToken=curl_data['accessToken']
                refreshToken=curl_data['refreshToken']
                expiresIn=int(curl_data['expiresIn'])-300
                time_expires=datetime.datetime.now()+datetime.timedelta(seconds=expiresIn)
                token_expires.update(accesstoken=accessToken,refreshtoken=refreshToken,accexpires=time_expires,refexpires=time_expires)
                pm2d5Value = inputData['IeCnt']['pm2d5Value']
                resp_dev = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=FrUsr)
                if (resp_dev.exists()):
                    dct_t_l3f3dm_current_report_aqyc.objects.create(dev_code_id=FrUsr, pm25=pm2d5Value,
                                                                    site_code_id=resp_dev[0].site_code_id)
                    hourminindex = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
                    dct_t_l3f3dm_minute_report_aqyc.objects.create(dev_code_id=FrUsr, pm25=pm2d5Value,
                                                                   site_code_id=resp_dev[0].site_code_id,
                                                                   hourminindex=hourminindex)
                    # data = self.dft_dbi_get_aqyc_current_report_view(FrUsr)
                    IeCnt={"cfmYesOrNo":1}
                    strLen=len(json.dumps(IeCnt))
                    data={"ToUsr":FrUsr,"FrUsr":"XHTS","CrTim":int(time.time()),"MsgTp":"huitp_json","MsgId":0X5E90,"MsgLn":strLen,"IeCnt":IeCnt,"FnFlg":FnFlg}
                    result = {'result': 'true', 'token': token, 'data': data}
                else:
                    result = {'result': 'false', 'token': token}
            else:
                pm2d5Value=inputData['IeCnt']['pm2d5Value']
                resp_dev=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=FrUsr)
                if(resp_dev.exists()):
                    dct_t_l3f3dm_current_report_aqyc.objects.create(dev_code_id=FrUsr,pm25=pm2d5Value,site_code_id=resp_dev[0].site_code_id)
                    hourminindex = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
                    dct_t_l3f3dm_minute_report_aqyc.objects.create(dev_code_id=FrUsr,pm25=pm2d5Value,site_code_id=resp_dev[0].site_code_id,hourminindex=hourminindex)
                    IeCnt = {"cfmYesOrNo": 1}
                    strLen = len(json.dumps(IeCnt))
                    data = {"ToUsr": FrUsr, "FrUsr": "XHTS", "CrTim": int(time.time()), "MsgTp": "huitp_json",
                            "MsgId": 0X5E90, "MsgLn": strLen, "IeCnt": IeCnt, "FnFlg": FnFlg}
                    result = {'result': 'true', 'token':token,'data':data}
                else:
                    result = {'result': 'false',  'token':token}
        else:
            result={'result':'false', 'token':"信息未找到"}
        return result

    def dft_dbi_get_aqyc_current_report_view(self,dev_code):
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=dev_code)
        tsp = 0
        pm01 = 0
        pm25 = 0
        pm10 = 0
        noise = 0
        temperature = 0
        humidity = 0
        winddir = 0
        windspd = 0
        rain = 0
        airpresure = 0
        lightstr = 0
        so2 = 0
        co1 = 0
        no1 = 0
        h2s = 0
        hcho = 0
        toxicgas = 0
        rssi = 0
        pwrind=0
        no2 = 0
        report_date=str(datetime.datetime.now())
        if result.exists():
            for line in result:
                report_date=str(line.report_time)
                tsp=line.tsp
                pm01=line.pm01
                pm25=line.pm25
                pm10=line.pm10
                noise=line.noise
                temperature=line.temperature
                humidity=line.humidity
                winddir=line.winddir
                windspd=line.windspd
                rain=line.rain
                airpresure=line.airpresure
                lightstr=line.lightstr
                so2=line.so2
                co1=line.co1
                no1=line.no1
                h2s=line.h2s
                hcho=line.hcho
                toxicgas=line.toxicgas
                rssi=line.rssi
                pwrind=line.pwrind
                no2=line.no2
        resp_data={'report_time':report_date,
                   'tsp':tsp,
                   'pm01':pm01,
                   'pm25':pm25,
                   'pm10':pm10,
                   'noise':noise,
                   'temperature':temperature,
                   'humidity':humidity,
                   'winddir':winddir,
                   'windspd':windspd,
                   'rain':rain,
                   'airpresure':airpresure,
                   'lightstr':lightstr,
                   'so2':so2,
                   'co1':co1,
                   'no1':no1,
                   'h2s':h2s,
                   'hcho':hcho,
                   'toxicgas':toxicgas,
                   'rssi':rssi,
                   'pwrind':pwrind,
                   'no2':no2,
                   }
        return resp_data
    