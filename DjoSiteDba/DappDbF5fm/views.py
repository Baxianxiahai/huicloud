from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.db.models.functions import Concat
from DappDbF1sym.models import *
from DappDbSnr.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbF5fm.models import *
import DappDbF1sym.views as DappDbF1sym_views
import datetime

class dct_classDbiL3apF5fm:

    __HUITP_IEID_UNI_ALARM_SEVERITY_NONE=0X00
    __HUITP_IEID_UNI_ALARM_SEVERITY_HIGH=0X01
    __HUITP_IEID_UNI_ALARM_SEVERITY_MEDIUM=0X02
    __HUITP_IEID_UNI_ALARM_SEVERITY_MINOR=0X03
    __HUITP_IEID_UNI_ALARM_SEVERITY_INVALID=0XFF

    __MFUN_HCU_SITE_PIC_WWW_PATH="/avorion/picture/"

    __MFUN_L3APL_F3DM_TH_ALARM_NOISE=70
    __MFUN_L3APL_F3DM_TH_ALARM_HUMID=80
    __MFUN_L3APL_F3DM_TH_ALARM_TEMP=45
    __MFUN_L3APL_F3DM_TH_ALARM_PM25=201
    __MFUN_L3APL_F3DM_TH_ALARM_WINDSPD=20
    __MFUN_L3APL_F3DM_TH_ALARM_EMC=100
    __MFUN_L3APL_F3DM_TH_ALARM_WINDDIR=360
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW=15
    __MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH=70
    __MFUN_L3APL_F3DM_TH_ALARM_BATT=20
    __MFUN_AQYC_ALARM_CODE=['工作正常','颗粒物传感器故障','温度传感器故障','湿度传感器故障','风向传感器故障','风速传感器故障','噪声传感器故障','摄像头故障','扬尘超标','噪声超标']
    __MFUN_HCU_FHYS_CMCC_URL="http://api.sms.heclouds.com/tempsmsSend"
    __MFUN_HCU_FHYS_CMCC_SICODE="a2bb3546a41649a29e2fcb635e091dd5"
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_PW="10832"
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM="10833"

    __MFUN_HCU_ALARM_PROC_FLAG_Y='Y'
    __MFUN_HCU_ALARM_PROC_FLAG_N='N'
    __MFUN_HCU_ALARM_PROC_FLAG_C='C'

    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT="W"

    __MFUN_L3APL_F3DM_AQYC_STYPE_PREFIX='YC'
    __MFUN_L3APL_F3DM_AQYC_STYPE_PM="YC_001"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD="YC_002"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDDIR="YC_003"
    __MFUN_L3APL_F3DM_AQYC_STYPE_EMC="YC_005"
    __MFUN_L3APL_F3DM_AQYC_STYPE_TEMP="YC_006"
    __MFUN_L3APL_F3DM_AQYC_STYPE_HUMID= "YC_007"
    __MFUN_L3APL_F3DM_AQYC_STYPE_NOISE="YC_00A"
    def __dft_dbi_user_statproj_inqury(self,uid):
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        p_list=[]
        pg_list=[]
        if result.exists():
            for line in result:
                temp=line.auth_code
                type=line.auth_type
                if type==2:
                    p_list.append(temp)
                elif type==1:
                    pg_list.append(temp)
        for PG_CODE in pg_list:
            resp=dct_t_l3f2cm_project_common.objects.filter(pg_code_id=PG_CODE)
            if resp.exists():
                for line in resp:
                    temp=line.prj_code
                    p_list.append(temp)

        auth_list=[]
        for P_CODE in p_list:
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=P_CODE)
            if result.exists():
                for line in result:
                    temp={"stat_code":line.site_code,'p_code':P_CODE}
                    auth_list.append(temp)
        if len(auth_list)==0:
            return auth_list
        unique_authlist=[]
        for site_info in auth_list:
            if site_info not in unique_authlist:
                unique_authlist.append(site_info)
        return unique_authlist

    def __dft_dbi_site_alarm_check(self,statCode):
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                tsp=line.pm01
                noise=line.noise
        else:
            tsp=0
            noise=0
        if (tsp>self.__MFUN_L3APL_F3DM_TH_ALARM_PM25) or (noise>self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE):
            resp=True
        else:
            resp=False
        return resp

    def dft_dbi_map_alarm_site_info_req(self,inputData):
        uid=inputData['uid']
        auth_list=self.__dft_dbi_user_statproj_inqury(uid)
        sitelist=[]
        for siteInfo in auth_list:
            statCode=siteInfo['stat_code']
            resp=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if resp.exists():
                for line in resp:
                    alarm_check=self.__dft_dbi_site_alarm_check(statCode)
                    if alarm_check:
                        latitude=line.latitude
                        longitude=line.longitude
                        temp={
                            'StatCode' :line.site_code,
                            'StatName':line.statname,
                            'ChargeMan':line.superintendent,
                            'Telephone':line.telephone,
                            'Department':line.department,
                            'Address':line.address,
                            'Country':line.district,
                            "Street":line.street,
                            'Square':line.site_area,
                            'Flag_la':"N",
                            "Latitude":latitude,
                            "Flag_lo":"E",
                            "Longitude":longitude,
                            "ProStartTime":line.create_date,
                            'Stage':line.comments,
                        }
                        sitelist.append(temp)
        return sitelist
    def dft_dbi_all_alarmtype_req(self,inputData):
        type=inputData['type']
        result=dct_t_l2snr_sensor_type.objects.all()
        alarm_type=[]
        if result.exists():
            for line in result:
                type_check=line.snr_code
                type_prefix=type_check[0:2]
                if type_prefix==type:
                    temp={'id':line.snr_code,'name':line.snr_name}
                    alarm_type.append(temp)
        return alarm_type

    def dft_dbi_aqyc_alarm_history_table_req(self,inputData):
        prjCode=inputData['prjcode']
        duration=inputData['duration']
        keyword=inputData['keyword']
        column=[]
        data=[]
        column.append('序号')
        column.append('处理状态')
        column.append('站点编号')
        column.append('设备编号')
        column.append('站点名称')
        column.append('地址')
        column.append('负责人')
        column.append('联系电话')
        column.append('告警级别')
        column.append('告警内容')
        column.append('告警产生时间')
        column.append('告警关闭时间')
        column.append('告警处理')
        end = datetime.date.today()
        endtime=str(end)
        endtime_middle=time.strptime(endtime,'%Y-%m-%d')
        endformat=int(time.strftime("%Y%m%d",endtime_middle))
        start = end
        if duration == '1':
            start = str(end - datetime.timedelta(days=1))
            time_middle = time.strptime(start, '%Y-%m-%d')
            start = int(time.strftime("%Y%m%d", time_middle))
        elif duration == '7':
            start = str(end - datetime.timedelta(days=7))
            time_middle = time.strptime(start, '%Y-%m-%d')
            start = int(time.strftime("%Y%m%d", time_middle))
        elif duration == '30':
            start = str(end - datetime.timedelta(days=30))
            time_middle = time.strptime(start, '%Y-%m-%d')
            start = int(time.strftime("%Y%m%d", time_middle))
        result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=prjCode)
        print(result)
        if result.exists():
            for line in result:
                statCode=line.site_code
                statName=line.site_name
                address=line.address
                charageMan=line.superintendent
                telephone=line.telephone
                alarmFlag="C"
                if keyword=="":
                    resp=dct_t_l3f3dm_alarm_report_aqyc.objects.filter(Q(site_code_id=statCode),~Q(alarmflag=alarmFlag))
                else:
                    resp=dct_t_l3f3dm_alarm_report_aqyc.objects.filter(Q(site_code_id=statCode),~Q(alarmflag=alarmFlag),Q(alarmproc__icontains=keyword))
                print(resp)
                if resp.exists():
                    for line_resp in resp:
                        sid=line_resp.sid
                        site_code=line.site_code
                        devCode=line_resp.dev_code_id
                        alarmflag=line_resp.alarmflag
                        alarmSeverity=line_resp.alarmseverity
                        alarmContent=line_resp.alarmcontent
                        tsgen=str(line_resp.tsgen)
                        tsclose=line_resp.tsclose
                        alarmProc=line_resp.alarmproc
                        time_middle=time.strptime(tsgen,'%Y-%m-%d %H:%M:%S')
                        dateintval=int(time.strftime('%Y%m%d',time_middle))
                        print(int(dateintval))
                        print(type(int(dateintval)))
                        print(type(start))
                        if dateintval<start or dateintval>endformat:
                            continue
                        if alarmSeverity==self.__HUITP_IEID_UNI_ALARM_SEVERITY_HIGH:
                            alarmSeverity='高'
                        elif alarmSeverity==self.__HUITP_IEID_UNI_ALARM_SEVERITY_MEDIUM:
                            alarmSeverity='中'
                        elif alarmSeverity==self.__HUITP_IEID_UNI_ALARM_SEVERITY_MINOR:
                            alarmSeverity='低'
                        else:
                            alarmSeverity='无'
                        alarmDesc=self.__MFUN_AQYC_ALARM_CODE[alarmContent]
                        one_row=[]
                        one_row.append(sid)
                        one_row.append(alarmflag)
                        one_row.append(site_code)
                        one_row.append(devCode)
                        one_row.append(statName)
                        one_row.append(address)
                        one_row.append(charageMan)
                        one_row.append(telephone)
                        one_row.append(alarmSeverity)
                        one_row.append(alarmDesc)
                        one_row.append(tsgen)
                        one_row.append(str(tsclose))
                        one_row.append(alarmProc)
                        data.append(one_row)
        alarm_list={'column':column,'data':data}
        return alarm_list
    def dft_dbi_aqyc_alarm_image_req(self,inputData):
        sid=inputData['sid']
        result=dct_t_l3f3dm_alarm_report_aqyc.objects.filter(sid=sid)
        pic_result=[]
        if result.exists():
            for line in result:
                file_name=line.alarmpic
                statCode=line.site_code
                if file_name!="":
                    file_url=self.__MFUN_HCU_SITE_PIC_WWW_PATH+statCode+'/'+file_name
                    pic_result={'ifpicture':'true','picture':file_url}
                else:
                    pic_result = {'ifpicture': 'false', 'picture': ""}
        return pic_result
    def dft_dbi_aqyc_alarm_rstp_req(self,inputData):
        sid=inputData['sid']
        rtsp_result=[]
        result=dct_t_l3f3dm_alarm_report_aqyc.objects.filter(sid=sid)
        if result.exists():
            for line in result:
                statCode=line.site_code
                devCode=line.dev_code
                alarmReason=self.__MFUN_AQYC_ALARM_CODE[int(line.alarmcontent)]
                alarmDate=line.tsgen
                resp=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
                if resp.exists():
                    for line_info in resp:
                        site_name=line_info.site_name
                else:
                    site_name=""
                resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
                if resp.exists():
                    for line_info in resp:
                        rtsp_url=line_info.video1_url
                        #rtsp_url="rtsp://admin:Bxxh!123@ngrok2.hkrob.com:"+str(port)+"/Streaming/tracks/101/"
                        rtsp_result={"StatCode":statCode,"StatName":site_name,"AlarmReason":alarmReason,"rtspurl":rtsp_url,"AlarmDate":str(alarmDate)}
        return rtsp_result
    def dft_dbi_aqyc_alarm_handle_process(self,inputData):
        uid=inputData['uid']
        statCode=inputData['statcode']
        mobile=inputData['mobile']
        action=inputData['action']
        result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        if result.exists():
            for line in result:
                statname=line.site_name
                url=self.__MFUN_HCU_FHYS_CMCC_SICODE+"?sicode="+self.__MFUN_HCU_FHYS_CMCC_SICODE+"&mobiles"+mobile+"&tempid="+self.__MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM+"&name="+statname+"&action="+action
                DappDbF1sym_views.dct_classDbiL3apF1sym.dft_https_request(url)
                flag_new=self.__MFUN_HCU_ALARM_PROC_FLAG_N
                flag_proc=self.__MFUN_HCU_ALARM_PROC_FLAG_Y
                currenttime=datetime.datetime.now()
                alarmproc=str(currenttime)+"操作员["+uid+']发送信息['+action+"]到手机["+mobile+"]"
                # resp=dct_t_l3f3dm_alarm_report_aqyc.objects.get(site_code_id=statCode,alarmflag=flag_new)
                # resp.alarmflag=flag_proc
                # resp.alarmproc=str(resp.alarmproc)+alarmproc
                # resp.save()
                dct_t_l3f3dm_alarm_report_aqyc.objects.filter(site_code_id=statCode, alarmflag=flag_new).update(
                    alarmflag=flag_proc,alarmproc=Concat('alarmproc', alarmproc))
        return alarmproc

    def dft_dbi_aqyc_alarm_close_process(self,inputData):
        uid=inputData['uid']
        statCode=inputData['statcode']
        currenttime=datetime.datetime.now()
        flag_proc=self.__MFUN_HCU_ALARM_PROC_FLAG_Y
        flag_close=self.__MFUN_HCU_ALARM_PROC_FLAG_C
        alarmproc='操作员['+uid+']关闭警告'
        result=dct_t_l3f3dm_alarm_report_aqyc.objects.filter(site_code_id=statCode,alarmflag=flag_proc)
        if result.exists():
            for line in result:
                alarmproc=line.alarmproc+"；"+alarmproc
        dct_t_l3f3dm_alarm_report_aqyc.objects.filter(site_code_id=statCode,alarmflag=flag_proc).update(alarmflag=flag_close,tsclose=currenttime,alarmproc=alarmproc)
        return True

    def dft_dbi_aqyc_dev_alarmhistory_req(self,inputData):
        statCode=inputData['statcode']
        inputDate=inputData['inputDate']
        inputDate=datetime.datetime.strptime(inputDate,"%Y-%m-%d")
        alarmtype=inputData['alarmtype']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            devCode=""
        monthStart=inputDate-datetime.timedelta(days=30)
        monthStartInt=time.strptime(str(monthStart),"%Y-%m-%d %H:%M:%S")
        monthStartInt=int(time.mktime(monthStartInt))
        
        dayValue=[]
        for dayIndex in range(0,31):
            a={'sum':0,'counter':0,'average':0}
            dayValue.append(a)
        if alarmtype==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
            alarm_name='细颗粒物'
            alarm_unit='微克/立方米'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
            line_name='TSP'
            result=dct_t_l2snr_dust.objects.filter(dev_code_id=devCode,report_data__range=(monthStart,inputDate)).order_by('sid')
            if result.exists():
                for line in result:
                    value=float(line.pm01)
                    reportDate=str(line.report_data)
                    dateInt = time.strptime(reportDate, "%Y-%m-%d")
                    dateInt = int(time.mktime(dateInt))
                    if dateInt>=monthStartInt:
                        day_index=int((dateInt-monthStartInt)/86400)-1
                        if 'sum' in dayValue[day_index].keys():
                            dayValue[day_index]['sum']=dayValue[day_index]['sum']+value
                            dayValue[day_index]['counter']=dayValue[day_index]['counter']+1
                        else:
                            dayValue[day_index]['sum']=value
                            dayValue[day_index]['counter']=1
        elif alarmtype==self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
            alarm_name='风速'
            alarm_unit='米/秒'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
            line_name='风速'
            result=dct_t_l2snr_windspd.objects.filter(dev_code_id=devCode,report_data__range=(monthStart,inputDate)).order_by('sid')
            if result.exists():
                for line in result:
                    value=float(line.windspd)
                    reportDate=str(line.report_data)
                    dateInt = time.strptime(reportDate, "%Y-%m-%d")
                    dateInt = int(time.mktime(dateInt))
                    if dateInt>=monthStartInt:
                        day_index=int((dateInt-monthStartInt)/86400)-1
                        if 'sum' in dayValue[day_index].keys():
                            dayValue[day_index]['sum']=dayValue[day_index]['sum']+value
                            dayValue[day_index]['counter']=dayValue[day_index]['counter']+1
                        else:
                            dayValue[day_index]['sum']=value
                            dayValue[day_index]['counter']=1
        elif alarmtype==self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
            alarm_name='温度'
            alarm_unit='摄氏度'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
            line_name='温度'
            result=dct_t_l2snr_temperature.objects.filter(dev_code_id=devCode,report_data__range=(monthStart,inputDate)).order_by('sid')
            if result.exists():
                for line in result:
                    value=float(line.temperature)
                    reportDate=str(line.report_data)
                    dateInt = time.strptime(reportDate, "%Y-%m-%d")
                    dateInt = int(time.mktime(dateInt))
                    if dateInt>=monthStartInt:
                        day_index=int((dateInt-monthStartInt)/86400)-1
                        if 'sum' in dayValue[day_index].keys():
                            dayValue[day_index]['sum']=dayValue[day_index]['sum']+value
                            dayValue[day_index]['counter']=dayValue[day_index]['counter']+1
                        else:
                            dayValue[day_index]['sum']=value
                            dayValue[day_index]['counter']=1
        elif alarmtype==self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
            alarm_name='湿度'
            alarm_unit='%'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
            line_name='湿度'
            result=dct_t_l2snr_humidity.objects.filter(dev_code_id=devCode,report_data__range=(monthStart,inputDate)).order_by('sid')
            if result.exists():
                for line in result:
                    value=float(line.humidity)
                    reportDate=str(line.report_data)
                    dateInt = time.strptime(reportDate, "%Y-%m-%d")
                    dateInt = int(time.mktime(dateInt))
                    if dateInt>=monthStartInt:
                        day_index=int((dateInt-monthStartInt)/86400)-1
                        if 'sum' in dayValue[day_index].keys():
                            dayValue[day_index]['sum']=dayValue[day_index]['sum']+value
                            dayValue[day_index]['counter']=dayValue[day_index]['counter']+1
                        else:
                            dayValue[day_index]['sum']=value
                            dayValue[day_index]['counter']=1
        elif alarmtype==self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
            alarm_name='噪声'
            alarm_unit='分贝'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
            line_name='噪声'
            result=dct_t_l2snr_noise.objects.filter(dev_code_id=devCode,report_data__range=(monthStart,inputDate)).order_by('sid')
            if result.exists():
                for line in result:
                    value=float(line.noise)
                    reportDate=str(line.report_data)
                    dateInt = time.strptime(reportDate, "%Y-%m-%d")
                    dateInt = int(time.mktime(dateInt))
                    if dateInt>=monthStartInt:
                        day_index=int((dateInt-monthStartInt)/86400)-1
                        if 'sum' in dayValue[day_index].keys():
                            dayValue[day_index]['sum']=dayValue[day_index]['sum']+value
                            dayValue[day_index]['counter']=dayValue[day_index]['counter']+1
                        else:
                            dayValue[day_index]['sum']=value
                            dayValue[day_index]['counter']=1
        day_alarm=[]
        day_head=[]
        day_value=[]
        for day_index in range(31):
            if dayValue[day_index]['counter']!=0:
                dayValue[day_index]['average']=dayValue[day_index]['sum']/dayValue[day_index]['counter']
            else:
                dayValue[day_index]['average']=0
            date_index_int=monthStartInt+day_index*24*3600
            time_array=time.localtime(date_index_int)
            date_index=time.strftime("%Y-%m-%d",time_array)
            average=round(dayValue[day_index]['average'],1)
            day_value.append(average)
            day_head.append(date_index)
        day_alarm1={'name':line_name,'color':"",'items':day_value}
        day_alarm.append(day_alarm1)
        value_min=0
        value_max=max(day_value)
        resp={'alarm_name':alarm_name,'alarm_unit':alarm_unit,'warning':warning,'day_head':day_head,'day_alarm':day_alarm,"value_min":value_min,"value_max":value_max}
        return resp
    def dft_dbi_fstt_dev_alarmhistory_realtime_req_view(self,inputData):
        statcode=inputData['statcode']
        alarm_type=inputData['alarmtype']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            devCode=""
        minute_alarm=[]
        minute_head=[]
        hour_alarm=[]
        hour_head=[]
        line_name=""
        min=datetime.datetime.now()
        today=min.date()
        hour_base=min.hour
        minute_base=min.minute
        index_base=(hour_base+1)*60
        hourminindex_now=(min.hour*60+min.minute)/1.0
        dayStart=datetime.datetime.today()-datetime.timedelta(days=1)
        grideValue=[]
        alarm_name=""
        alarm_unit=""
        warning=""
        for i in range (1441):
            value={'value':0}
            grideValue.append(value)
        hourValue=[]
        for j in range(25):
            value={'sum':0,'counter':0,'average':0}
            hourValue.append(value)
        if alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
            alarm_name='细颗粒物'
            alarm_unit='微克/立方米'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
            line_name='TSP'
            result=dct_t_l2snr_dust.objects.filter(Q(dev_code_id=devCode),(Q(report_data=today)|Q(report_data=dayStart,hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value=line.tsp
                    hourminindex=line.hourminindex
                    reportDate=line.report_data
                    hour_index=int((hourminindex*1.0)/60)
                    if reportDate==today and (hourminindex>=hourminindex_now-60):
                        grideValue[hourminindex]['value']=value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum']=hourValue[hour_index]['sum']+value
                        hourValue[hour_index]['counter']=hourValue[hour_index]['counter'] +1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
            alarm_name = '噪声'
            alarm_unit = '分贝'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
            line_name = '噪声'
            result = dct_t_l2snr_noise.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.noise
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
            alarm_name = '温度'
            alarm_unit = '摄氏度'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
            line_name = '温度'
            result = dct_t_l2snr_temperature.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.temperature
                    hourminindex = line.hourminindex

                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
            alarm_name = '湿度'
            alarm_unit = '%'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
            line_name = '湿度'
            result = dct_t_l2snr_humidity.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.humidity
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
            alarm_name = '风速'
            alarm_unit = '米/秒'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
            line_name = '风速'
            result = dct_t_l2snr_windspd.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.windspd
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1
        minute_value=[]
        for i in range (60):
            if minute_base+i<60:
                minute_head1=str(hour_base-1)+":"+str(minute_base+i).zfill(2)
            else:
                minute_head1 = str(hour_base) + ":" + str(minute_base-(60-i)).zfill(2)
            minute_value.append(grideValue[int(hourminindex_now-(60-i))]['value'])
            minute_head.append(str(minute_head1))
            
        minute_alarm1={'name':line_name,'color':"",'items':minute_value}
        minute_alarm.append(minute_alarm1)
        hour_value=[]
        for j in range(1,25):
            if hour_base+j<24:
                hour_index=hour_base+j
            else:
                hour_index=hour_base-(24-j)
            if hourValue[hour_index]['counter']!=0:
                hourValue[hour_index]['average']=hourValue[hour_index]['sum']/hourValue[hour_index]['counter']
                average=round(hourValue[hour_index]['average'],1)
                hour_value.append(average)
                hour_head.append(str(hour_index)+":00")
            else:
                hour_value.append(0)
                hour_head.append(str(hour_index) + ":00")
        hour_alarm1={'name':line_name,'color':"",'items':hour_value}
        hour_alarm.append(hour_alarm1)
        value_min=0
        max_1=max(minute_value)
        max_2=max(hour_value)
        value_max=max(max_1,max_2)+5
        value_temp={"minute_alarm":minute_alarm,"minute_head":minute_head,"hour_alarm":hour_alarm,
                    "hour_head":hour_head,"alarm_name":alarm_name,"alarm_unit":alarm_unit,"warning":warning,
                    'value_min':value_min,"value_max":value_max}
        return value_temp

    def dft_dbi_aqyc_dev_alarmhistory_realtime_req(self,inputData):
        statcode=inputData['statcode']
        alarm_type=inputData['alarmtype']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            devCode=""
        minute_alarm=[]
        minute_head=[]
        hour_alarm=[]
        hour_head=[]
        line_name=""
        min=datetime.datetime.now()
        today=min.date()
        hour_base=min.hour
        minute_base=min.minute
        index_base=(hour_base+1)*60
        hourminindex_now=(min.hour*60+min.minute)/1.0
        dayStart=datetime.datetime.today()-datetime.timedelta(days=1)
        grideValue=[]
        alarm_name=""
        alarm_unit=""
        warning=""
        for i in range (1441):
            value={'value':0}
            grideValue.append(value)
        hourValue=[]
        for j in range(25):
            value={'sum':0,'counter':0,'average':0}
            hourValue.append(value)
        if alarm_type==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
            alarm_name='细颗粒物'
            alarm_unit='微克/立方米'
            warning=self.__MFUN_L3APL_F3DM_TH_ALARM_PM25
            line_name='TSP'
            result=dct_t_l2snr_dust.objects.filter(Q(dev_code_id=devCode),(Q(report_data=today)|Q(report_data=dayStart,hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value=line.tsp
                    hourminindex=line.hourminindex
                    reportDate=line.report_data
                    hour_index=int((hourminindex*1.0)/60)
                    if reportDate==today and (hourminindex>=hourminindex_now-60):
                        grideValue[hourminindex]['value']=value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum']=hourValue[hour_index]['sum']+value
                        hourValue[hour_index]['counter']=hourValue[hour_index]['counter'] +1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
            alarm_name = '噪声'
            alarm_unit = '分贝'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_NOISE
            line_name = '噪声'
            result = dct_t_l2snr_noise.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.noise
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
            alarm_name = '温度'
            alarm_unit = '摄氏度'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP
            line_name = '温度'
            result = dct_t_l2snr_temperature.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.temperature
                    hourminindex = line.hourminindex

                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter'] + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
            alarm_name = '湿度'
            alarm_unit = '%'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID
            line_name = '湿度'
            result = dct_t_l2snr_humidity.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.humidity
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1

        if alarm_type == self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
            alarm_name = '风速'
            alarm_unit = '米/秒'
            warning = self.__MFUN_L3APL_F3DM_TH_ALARM_WINDSPD
            line_name = '风速'
            result = dct_t_l2snr_windspd.objects.filter(Q(dev_code_id=devCode), (Q(report_data=today) | Q(report_data=dayStart, hourminindex__gte=index_base))).order_by('-sid')
            if result.exists():
                for line in result:
                    value = line.windspd
                    hourminindex = line.hourminindex
                    reportDate = line.report_data
                    hour_index = int((hourminindex * 1.0) / 60)
                    if reportDate == today and (hourminindex >= hourminindex_now - 60):
                        grideValue[hourminindex]['value'] = value
                    if 'counter' in hourValue[hour_index].keys():
                        hourValue[hour_index]['sum'] = hourValue[hour_index]['sum'] + value
                        hourValue[hour_index]['counter'] = hourValue[hour_index]['counter']  + 1
        minute_value=[]
        for i in range (60):
            if minute_base+i<60:
                minute_head1=str(hour_base-1)+":"+str(minute_base+i).zfill(2)
            else:
                minute_head1 = str(hour_base) + ":" + str(minute_base-(60-i)).zfill(2)
            minute_value.append(grideValue[int(hourminindex_now-(60-i))]['value'])
            minute_head.append(str(minute_head1))
            
        minute_alarm1={'name':line_name,'color':"",'items':minute_value}
        minute_alarm.append(minute_alarm1)
        hour_value=[]
        for j in range(1,25):
            if hour_base+j<24:
                hour_index=hour_base+j
            else:
                hour_index=hour_base-(24-j)
            if hourValue[hour_index]['counter']!=0:
                hourValue[hour_index]['average']=hourValue[hour_index]['sum']/hourValue[hour_index]['counter']
                average=round(hourValue[hour_index]['average'],1)
                hour_value.append(average)
                hour_head.append(str(hour_index)+":00")
            else:
                hour_value.append(0)
                hour_head.append(str(hour_index) + ":00")
        hour_alarm1={'name':line_name,'color':"",'items':hour_value}
        hour_alarm.append(hour_alarm1)
        value_min=0
        max_1=max(minute_value)
        max_2=max(hour_value)
        value_max=max(max_1,max_2)+5
        value_temp={"minute_alarm":minute_alarm,"minute_head":minute_head,"hour_alarm":hour_alarm,
                    "hour_head":hour_head,"alarm_name":alarm_name,"alarm_unit":alarm_unit,"warning":warning,
                    'value_min':value_min,"value_max":value_max}
        return value_temp
    def dft_dbi_fhys_alarm_history_table_req(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]
        auth_list=self.__dft_dbi_user_statproj_inqury(uid)
        column.append("站点编号")
        column.append("处理状态")
        column.append("设备编号")
        column.append("站点名称")
        column.append("地址")
        column.append("负责人")
        column.append("联系电话")
        column.append("告警级别")
        column.append("告警产生时间")
        column.append("告警关闭时间")
        column.append("告警内容及处理")
        statname=""
        address=""
        chargeman=""
        telephone=""
        for auth_info in auth_list:
            statCode=auth_info['stat_code']
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    statname=line.site_name
                    address=line.address
                    chargeman=line.superintendent
                    telephone=line.telephone
            alarmflag="C"
            resp=dct_t_l3f3dm_alarm_report_fhys.objects.filter(Q(site_code_id=statCode),~Q(alarmflag=alarmflag))
            if resp.exists():
                for line_resp in resp:
                    one_row=[]
                    devCode=line_resp.dec_code_id
                    alarmflag=line_resp.alarmflag
                    alarmseverity=line_resp.alaemseverity
                    tsgen=line_resp.tsgen
                    tsclose=line_resp.tsclose
                    alarmproc=line_resp.alarmproc
                    one_row.append(statCode)
                    one_row.append(alarmflag)
                    one_row.append(devCode)
                    one_row.append(statname)
                    one_row.append(address)
                    one_row.append(chargeman)
                    one_row.append(telephone)
                    one_row.append(alarmseverity)
                    one_row.append(str(tsgen))
                    one_row.append(str(tsclose))
                    one_row.append(alarmproc)
                    data.append(one_row)
        history={'column':column,'data':data}
        return history
    def dft_dbi_fhys_alarm_handle_process(self,inputData):
        uid=inputData['uid']
        statCode=inputData['statCode']
        mobile=inputData['mobile']
        action=inputData['action']
        timestamp=int(time.time())
        result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        if result.exists():
            for line in result:
                projcode=line.prj_code_id
                statname=line.site_name
                chargeman=line.superintendent
                telephone=line.telephone
                url=self.__MFUN_HCU_FHYS_CMCC_URL+"?sicode="+self.__MFUN_HCU_FHYS_CMCC_SICODE+"&mobiles="+mobile+"&tempid="+self.__MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM+"&name="+statname+"&action="+action
                DappDbF1sym_views.dct_classDbiL3apF1sym.dft_https_request(url)

                flag_new=self.__MFUN_HCU_ALARM_PROC_FLAG_N
                flag_proc=self.__MFUN_HCU_ALARM_PROC_FLAG_Y
                currenttime=time.localtime(timestamp)
                currenttime=time.strptime("%Y-%m-%d %H:%M:%S",currenttime)
                key_type=self.__MFUN_L3APL_F2CM_KEY_TYPE_WECHAT
                resp=dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=projcode,keytype=key_type)
                if resp.exists():
                    for line in resp:
                        wx_touser=line.hwcode
                        template={'touser':wx_touser,
                                  'template_id':'JtIqUduhqFSJYRbnBLQnlSri7gT6NRkLKgzohHyDUrs',
                                  'topcolor':'#7B68EE',
                                  'data':{'first':{'value':'您好，光交箱智能管理平台告警通知!','color':'#743A3A'}},
                                  'keyword1':{'value':statname,'color':'#0000FF'},
                                  'keyword2':{'value':action,'color':'#FF0000'},
                                  'keyword3':{'value':currenttime,'color':'#0000FF'},
                                  'keyword4':{'value':chargeman,'color':'#0000FF'},
                                  'keyword5':{'value':telephone,'color':'#0000FF'},
                                  'remark':{'value':'请及时联系相关人员处理该告警','color':'#0000FF'},
                                  }
                        status='true'
                else:
                    status = 'false'
                    template={}
                alarmproc=str(currenttime)+"操作员["+uid+"]发送信息["+action+"]到手机["+mobile+"]"
                dct_t_l3f3dm_alarm_report_fhys.objects.filter(site_code_id=statCode,alarmflag=flag_new).update(alarmflag=flag_proc,alarmproc=Concat('alarmproc',alarmproc))
        else:
            template={}
            alarmproc=""
            status="false"
        send_data={'template':template,'alarmproc':alarmproc,'status':status}
        return send_data
    def dft_dbi_fhys_alarm_close_process(self,inputData):
        uid=inputData['uid']
        statcode=inputData['statcode']
        currenttime = datetime.datetime.now()
        flag_proc = self.__MFUN_HCU_ALARM_PROC_FLAG_Y
        flag_close = self.__MFUN_HCU_ALARM_PROC_FLAG_C
        alarmproc="操作员["+uid+"]关闭警告"
        result=dct_t_l3f3dm_alarm_report_fhys.objects.filter(site_code_id=statcode, alarmflag=flag_proc)
        if result.exists():
            alarmproc_table=result[0].alarmproc
            if alarmproc_table==None:
                pass
            else:
                alarmproc=alarmproc_table+alarmproc
            result.update(alarmflag=flag_close, alarmproc=alarmproc,tsclose=currenttime )
        return True
    
    def __dft_func_fhys_map_currentvalue_build(self,inputData):
        devcode=inputData
        result=dct_t_l3f3dm_current_report_fhys.objects.filter(dev_code_id=devcode)
        if result.exists():
            for line in result:
                temperature=line.tempvalue
                humidity=line.humidvalue
                battlevel=line.battvalue
                siglevel=line.rssivalue
                currentvalue=[]
                TimeS=str(line.report_time)
                timestamp=int(time.mktime(time.strptime(TimeS,"%Y-%m-%d %H:%M:%S.%f")))
                currenttime=int(time.time())
                if currenttime>timestamp+180:
                    devstat="休眠中"
                    alarm='true'
                else:
                    devstat='运行中'
                    alarm='false'
                temp={
                    'AlarmName':'设备状态：',
                    'AlarmEName':'FHYS_fibbox',
                    'AlarmValue':devstat,
                    'AlarmUnit':'',
                    'WarningTarget':alarm,
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
                if line.lock_1==self.__HUITP_IEID_UNI_LOCK_STATE_NULL or line.door_1==self.__HUITP_IEID_UNI_DOOR_STATE_NULL:
                    doorlock_1_status = '未安装'
                    doorlock_1_alarm = 'true'
                    doorlock_1_picname = 'FHYS_lockc'
                temp={
                    "AlarmName":"门锁-1 状态：",
                    "AlarmEName":str(doorlock_1_picname),
                    "AlarmValue":str(doorlock_1_status),
                    "AlarmUnit":"",
                    "WarningTarget":doorlock_1_alarm,
                }
                currentvalue.append(temp)

                if line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_2_status='门锁打开'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_locko'

                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_2_status='门锁关闭'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_lockc'

                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_ALARM:
                    doorlock_2_status='暴力开门'
                    doorlock_2_alarm='true'
                    doorlock_2_picname='FHYS_door'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_CLOSE and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_OPEN:
                    doorlock_2_status='锁关门开'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_lockc'
                elif line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_OPEN and line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_CLOSE:
                    doorlock_2_status='锁开门关'
                    doorlock_2_alarm='false'
                    doorlock_2_picname='FHYS_locko'
                else:
                    doorlock_2_status = '状态异常'
                    doorlock_2_alarm = 'true'
                    doorlock_2_picname = 'FHYS_locko'
                if line.lock_2==self.__HUITP_IEID_UNI_LOCK_STATE_NULL or line.door_2==self.__HUITP_IEID_UNI_DOOR_STATE_NULL:
                    doorlock_2_status = '未安装'
                    doorlock_2_alarm = 'true'
                    doorlock_2_picname = 'FHYS_lockc'
                temp={
                    "AlarmName":"门锁-2 状态：",
                    "AlarmEName":str(doorlock_2_picname),
                    "AlarmValue":str(doorlock_2_status),
                    "AlarmUnit":"",
                    "WarningTarget":doorlock_2_alarm,
                }
                currentvalue.append(temp)
                if siglevel!=None:
                    if siglevel<self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW:
                        gprs='较差'
                        alarm='true'
                    elif (siglevel>=self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_LOW) and siglevel<=self.__MFUN_L3APL_F3DM_TH_ALARM_GPRS_HIGH:
                        gprs='一般'
                        alarm='false'
                    else:
                        gprs='良好'
                        alarm='false'
                    temp = {
                        "AlarmName": "信号强度：",
                        "AlarmEName": 'FHYS_sig',
                        "AlarmValue": str(gprs),
                        "AlarmUnit": "",
                        "WarningTarget": alarm,
                    }
                else:
                    temp = {
                        "AlarmName": "信号强度：",
                        "AlarmEName": 'FHYS_sig',
                        "AlarmValue": 'NULL',
                        "AlarmUnit": "",
                        "WarningTarget": 'false',
                    }
                currentvalue.append(temp)
                if battlevel!=None:
                    if battlevel<self.__MFUN_L3APL_F3DM_TH_ALARM_BATT:
                        alarm='true'
                    else:
                        alarm='false'
                    if battlevel>100:
                        battlevel=100
                    temp = {
                        "AlarmName": "剩余电量：",
                        "AlarmEName": 'FHYS_batt',
                        "AlarmValue": str(battlevel),
                        "AlarmUnit": "",
                        "WarningTarget": alarm,
                    }
                else:
                    temp = {
                        "AlarmName": "剩余电量：",
                        "AlarmEName": 'FHYS_batt',
                        "AlarmValue": 'NULL',
                        "AlarmUnit": "",
                        "WarningTarget": alarm,
                    }
                currentvalue.append(temp)
                if temperature!=None:
                    if temperature>self.__MFUN_L3APL_F3DM_TH_ALARM_TEMP:
                        alarm='true'
                    else:
                        alarm='false'
                    temp = {
                        "AlarmName": "温度：",
                        "AlarmEName": 'FHYS_temp',
                        "AlarmValue": str(temperature),
                        "AlarmUnit": " ℃",
                        "WarningTarget": alarm,
                    }
                else:
                    temp = {
                        "AlarmName": "温度：",
                        "AlarmEName": 'FHYS_temp',
                        "AlarmValue": "NULL",
                        "AlarmUnit": "",
                        "WarningTarget": 'false',
                    }
                currentvalue.append(temp)
                if humidity!=None:
                    if humidity>self.__MFUN_L3APL_F3DM_TH_ALARM_HUMID:
                        alarm='true'
                    else:
                        alarm='false'
                    temp = {
                        "AlarmName": "湿度：",
                        "AlarmEName": 'FHYS_humi',
                        "AlarmValue": str(humidity),
                        "AlarmUnit": " %",
                        "WarningTarget": alarm,
                    }
                else:
                    temp = {
                        "AlarmName": "湿度：",
                        "AlarmEName": 'FHYS_humi',
                        "AlarmValue": "NULL",
                        "AlarmUnit": "",
                        "WarningTarget": 'false',
                    }
                currentvalue.append(temp)
                if line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_ACTIVE:
                    vibralarm='有'
                    alarm='true'
                elif line.shakestate==self.__HUITP_IEID_UNI_SHAKE_STATE_DEACTIVE:
                    vibralarm='无'
                    alarm='false'
                else:
                    vibralarm='状态未知'
                    alarm='true'
                temp = {
                    "AlarmName": "震动告警：",
                    "AlarmEName": 'FHYS_vibr',
                    "AlarmValue": str(vibralarm),
                    "AlarmUnit": "",
                    "WarningTarget": alarm,
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
                    "AlarmName": "水浸告警：",
                    "AlarmEName": 'FHYS_water',
                    "AlarmValue": str(wateralarm),
                    "AlarmUnit": "",
                    "WarningTarget": alarm,
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
                    "AlarmName": "倾斜告警：",
                    "AlarmEName": 'FHYS_smok',
                    "AlarmValue": str(fallalarm),
                    "AlarmUnit": "",
                    "WarningTarget": alarm,
                }
                currentvalue.append(temp)
        else:
            currentvalue=""
        return currentvalue
    def dft_dbi_fhys_dev_currentvalue_req(self,inputData):
        statCode=inputData['statCode']
        vcrname=[]
        vcrlink=[]
        vcrlist=[]
        devCode=""
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
                vcrname.append("RTSP")
                vcrname.append("CAMCTRL")
                rtsp=""
                cam_ctrl=""
                vcrlink.append(rtsp)
                vcrlink.append(cam_ctrl)
                vcrlist={'vcrname':vcrname,'vcraddress':vcrlink}
        currentvalue=self.__dft_func_fhys_map_currentvalue_build(devCode)
        resp={'StatCode':statCode,'alarmlist':currentvalue,'vcr':vcrlist}
        return resp







































