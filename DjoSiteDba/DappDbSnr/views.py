from django.shortcuts import render

# Create your views here.
from DappDbSnr.models import *
import datetime
from DappDbF3dm.models import *
class dct_classDappDbSnr:
    def dft_dbi_all_sensorlist_req(self,inputData):
        type=inputData['type']
        result=dct_t_l2snr_sensor_type.objects.all()
        sensor_list=[]
        if result.exists():
            for line in result:
                type_check=line.snr_code
                type_prefix=type_check[0:2]
                if type_prefix==type:
                    temp={
                        'id':line.snr_code,
                        'name':line.snr_model,
                        'nickname':line.snr_name,
                        'memo':line.snr_vendor,
                        'code':""
                    }
                    sensor_list.append(temp)
        return sensor_list
    
    def dft_dbi_aqyc_dev_sensorinfo_req(self, inputData):
        devCode = inputData['devcode']
        sensorinfo = []
        result = dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode)
        if result.exists():
            for line in result:
                typeid=line.snrtype
                onoff=line.status
                modbus=line.modbus_addr
                period=line.meas_period
                samples=line.rx_interval
                times=line.meas_times
                paralist=[]
                if modbus!="":
                    temp={
                        'name':'MODBUS_Addr',
                        'memo':'MODBUS地址',
                        'value':modbus,
                    }
                    paralist.append(temp)
                if period!="":
                    temp={
                        'name':'Measurement_Period',
                        'memo':'测量周期',
                        'value':period,
                    }
                    paralist.append(temp)
                if samples!="":
                    temp={
                        'name':'Samples_Interval',
                        'memo':'采样间隔',
                        'value':samples,
                    }
                    paralist.append(temp)
                if times!="":
                    temp={
                        'name':'Measurement_Times',
                        'memo':'测量次数',
                        'value':times,
                    }
                    paralist.append(temp)
                if typeid!="" and onoff!="":
                    temp={
                        'id':typeid,
                        'status':onoff,
                        'para':paralist,
                    }
                sensorinfo.append(temp)
        return sensorinfo
    
    def dft_dbi_shyc_old_data_clear(self,inputData):
        delete_days = int(inputData['days'])
        time_now = datetime.date.today()
        time_old = time_now - datetime.timedelta(days=delete_days)
        time_old=str(time_old)
        l3time_old=time_old+" 23:59:59"
        dct_t_l2snr_temperature.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_dust.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_humidity.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_winddir.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_windspd.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_noise.objects.filter(report_data__lte=time_old).delete()
        dct_t_l2snr_picture.objects.filter(report_data__lte=time_old).delete()
        dct_t_l3f3dm_minute_report_aqyc.objects.filter(report_date__lte=l3time_old).delete()