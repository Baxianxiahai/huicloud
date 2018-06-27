from django.db import models
from DappDbF2cm.models import dct_t_l3f2cm_device_common,dct_t_l3f2cm_site_common
# Create your models here.
class dct_t_l3f3dm_current_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_time = models.DateTimeField(auto_now=True)
    tsp = models.FloatField(default=0,verbose_name="TSP")
    pm01 = models.FloatField(default=0,verbose_name="PM0.1")
    pm25 = models.FloatField(default=0,verbose_name="PM2.5")
    pm10 = models.FloatField(default=0,verbose_name="PM10")
    noise = models.FloatField(default=0,verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    rain = models.FloatField(default=0, verbose_name="雨量")
    airpresure = models.FloatField(default=0, verbose_name="气压")


class dct_t_l3f3dm_minute_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField
    tsp = models.FloatField(default=0, verbose_name="TSP")
    pm01 = models.FloatField(default=0, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0, verbose_name="PM10")
    noise = models.FloatField(default=0, verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    rain = models.FloatField(default=0, verbose_name="雨量")
    airpresure = models.FloatField(default=0, verbose_name="气压")


class dct_t_l3f3dm_alarm_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    alarmflag = models.CharField(max_length=1)
    alarmseverity = models.IntegerField(default=0,blank=True)
    alarmcontent = models.IntegerField(default=0,blank=True)
    alarmtype = models.IntegerField(default=0,blank=True)
    clearflag = models.IntegerField(default=0,blank=True)
    causeid = models.IntegerField(default=0,blank=True)
    tsgen = models.DateTimeField(auto_now_add=True)
    tsclose = models.DateTimeField(null=True, blank=True)
    alarmpic = models.CharField(max_length=100)
    alarmproc = models.TextField(max_length=200)


class dct_t_l3f3dm_current_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_time = models.DateTimeField(auto_now=True)
    door_1 = models.IntegerField(default=0)
    door_2 = models.IntegerField(default=0)
    door_3 = models.IntegerField(default=0)
    door_4 = models.IntegerField(default=0)
    lock_1 = models.IntegerField(default=0)
    lock_2 = models.IntegerField(default=0)
    lock_3 = models.IntegerField(default=0)
    lock_4 = models.IntegerField(default=0)
    battstate = models.IntegerField(default=0)
    waterstate = models.IntegerField(default=0)
    shakestate = models.IntegerField(default=0)
    fallstate = models.IntegerField(default=0)
    smokestate = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    battvalue = models.FloatField(default=0,blank=True, verbose_name="电池电量值")
    fallvalue = models.FloatField(default=0,blank=True, verbose_name="倾斜角度值")
    tempvalue = models.FloatField(default=0,blank=True, verbose_name="温度值")
    humidvalue = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    rssivalue = models.FloatField(default=0,blank=True, verbose_name="信号强度值")


class dct_t_l3f3dm_minute_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_common, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_2 = models.IntegerField(default=0)
    door_3 = models.IntegerField(default=0)
    door_4 = models.IntegerField(default=0)
    lock_1 = models.IntegerField(default=0)
    lock_2 = models.IntegerField(default=0)
    lock_3 = models.IntegerField(default=0)
    lock_4 = models.IntegerField(default=0)
    battstate = models.IntegerField(default=0)
    waterstate = models.IntegerField(default=0)
    shakestate = models.IntegerField(default=0)
    fallstate = models.IntegerField(default=0)
    smokestate = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    door_1 = models.IntegerField(default=0)
    battvalue = models.FloatField(default=0,blank=True, verbose_name="电池电量值")
    fallvalue = models.FloatField(default=0,blank=True, verbose_name="倾斜角度值")
    tempvalue = models.FloatField(default=0,blank=True, verbose_name="温度值")
    humidvalue = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    rssivalue = models.FloatField(default=0,blank=True, verbose_name="信号强度值")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    