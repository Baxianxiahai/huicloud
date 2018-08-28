from django.shortcuts import render
import os,glob
from django.db.models import Q
from django.db.models.functions import Concat
from DappDbF1sym.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbFxprcm.models import *
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
        result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code__site_code__dct_t_l3f2cm_device_common=statCode)
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
                noise=line.noise
                winddir=line.winddir
                humidity=line.humidity
                temperature=line.temperature
                tsp=line.pm01
                windspeed=line.windspd
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
        column.append('PM2.5')
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
                    tsp=line.pm01
                    temperature=line.temperature
                    humidity=line.humidity
                    noise=line.noise
                    windspeed=line.windspd
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
                    print("JJJJJJIF")
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