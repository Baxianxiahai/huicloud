from django.db import models
from DappDbF2cm.models import dct_t_l3f2cm_device_common,dct_t_l3f2cm_site_common
from netbios import MAX_LANA
# Create your models here.
class dct_t_l3f3dm_current_report_aqyc(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    report_time=models.DateTimeField(auto_now=True)
    tsp=models.FloatField(max_digits=10,decimal_places=4,verbose_name="TSP")
    pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    noise=models.FloatField(max_digits=10,decimal_places=4,verbose_name="噪声")
    temperature=models.FloatField(max_digits=10,decimal_places=4,verbose_name="温度")
    humidity=models.FloatField(max_digits=10,decimal_places=4,verbose_name="湿度")
    winddir=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风向")
    windspd=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风速")
    rain=models.FloatField(max_digits=10,decimal_places=4,verbose_name="雨量")
    airpresure=models.FloatField(max_digits=10,decimal_places=4,verbose_name="气压")
class dct_t_l3f3dm_minute_report_aqyc(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    report_date=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    tsp=models.FloatField(max_digits=10,decimal_places=4,verbose_name="TSP")
    pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    noise=models.FloatField(max_digits=10,decimal_places=4,verbose_name="噪声")
    temperature=models.FloatField(max_digits=10,decimal_places=4,verbose_name="温度")
    humidity=models.FloatField(max_digits=10,decimal_places=4,verbose_name="湿度")
    winddir=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风向")
    windspd=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风速")
    rain=models.FloatField(max_digits=10,decimal_places=4,verbose_name="雨量")
    airpresure=models.FloatField(max_digits=10,decimal_places=4,verbose_name="气压")
class dct_t_l3f3dm_alarm_report_aqyc(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    alarmflag=models.CharField(max_length=1)
    alarmseverity=models.IntegerField
    alarmcontent=models.IntegerField
    alarmtype=models.IntegerField
    clearflag=models.IntegerField
    causeid=models.IntegerField
    tsgen=models.DateTimeField(auto_now_add=True)
    tsclose=models.DateTimeField(null=True,blank=True)
    alarmpic=models.CharField(max_length=100)
    alarmproc=models.TextField(max_length=200)
class dct_t_l3f3dm_current_report_fhys(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    report_time=models.DateTimeField(auto_now=True)
    door_1=models.IntegerField
    door_2=models.IntegerField
    door_3=models.IntegerField
    door_4=models.IntegerField
    lock_1=models.IntegerField
    lock_2=models.IntegerField
    lock_3=models.IntegerField
    lock_4=models.IntegerField
    battstate=models.IntegerField
    waterstate=models.IntegerField
    shakestate=models.IntegerField
    fallstate=models.IntegerField
    smokestate=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    battvalue=models.FloatField(max_digits=5,decimal_places=2,verbose_name="电池电量值")
    fallvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="倾斜角度值")
    tempvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="温度值")
    humidvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="湿度值")
    rssivalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="信号强度值")
    
class dct_t_l3f3dm_minute_report_fhys(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    report_date=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    door_1=models.IntegerField
    door_2=models.IntegerField
    door_3=models.IntegerField
    door_4=models.IntegerField
    lock_1=models.IntegerField
    lock_2=models.IntegerField
    lock_3=models.IntegerField
    lock_4=models.IntegerField
    battstate=models.IntegerField
    waterstate=models.IntegerField
    shakestate=models.IntegerField
    fallstate=models.IntegerField
    smokestate=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    door_1=models.IntegerField
    battvalue=models.FloatField(max_digits=5,decimal_places=2,verbose_name="电池电量值")
    fallvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="倾斜角度值")
    tempvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="温度值")
    humidvalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="湿度值")
    rssivalue=models.FloatField(max_digits=10,decimal_places=4,verbose_name="信号强度值")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    