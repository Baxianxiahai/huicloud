from django.db import models
from DappDbF2cm.models import dct_t_l3f2cm_device_inventory,dct_t_l3f2cm_site_common
from email.policy import default
# Create your models here.
class dct_t_l3f3dm_current_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_time = models.DateTimeField(auto_now=True)
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
    lightstr = models.FloatField(default=0, verbose_name="光照")
    so2 = models.FloatField(default=0, verbose_name="二氧化硫")
    co1 = models.FloatField(default=0, verbose_name="一氧化碳")
    no1 = models.FloatField(default=0, verbose_name="一氧化氮")
    h2s = models.FloatField(default=0, verbose_name="硫化氢")
    hcho = models.FloatField(default=0, verbose_name="酒精")
    toxicgas = models.FloatField(default=0, verbose_name="煤气")
    rssi = models.FloatField(default=0, verbose_name="信号强度")
    pwrind = models.FloatField(default=0, verbose_name="电量强度")
    cmd_flag = models.CharField(default="00",max_length=2, verbose_name="信号标志位")


class dct_t_l3f3dm_minute_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField(default=0)
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
    lightstr = models.FloatField(default=0, verbose_name="光照")
    so2 = models.FloatField(default=0, verbose_name="二氧化硫")
    co1 = models.FloatField(default=0, verbose_name="一氧化碳")
    no1 = models.FloatField(default=0, verbose_name="一氧化氮")
    h2s = models.FloatField(default=0, verbose_name="硫化氢")
    hcho = models.FloatField(default=0, verbose_name="酒精")
    toxicgas = models.FloatField(default=0, verbose_name="煤气")
    rssi = models.FloatField(default=0, verbose_name="信号强度")
    pwrind = models.FloatField(default=0, verbose_name="电量强度")
    

class dct_t_l3f3dm_current_report_smartcity(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_time = models.DateTimeField(auto_now=True)
    tsp = models.FloatField(default=0, verbose_name="TSP")
    pm01 = models.FloatField(default=0, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0, verbose_name="PM10")
    noise = models.FloatField(default=0, verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    lightstr=models.FloatField(default=0,verbose_name='光照强度')
    lampmode=models.IntegerField(default=0,verbose_name='灯带工作模式')

class dct_t_l3f3dm_minute_report_smartcity(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField(default=0)
    tsp = models.FloatField(default=0, verbose_name="TSP")
    pm01 = models.FloatField(default=0, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0, verbose_name="PM10")
    noise = models.FloatField(default=0, verbose_name="噪声")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    winddir = models.FloatField(default=0, verbose_name="风向")
    windspd = models.FloatField(default=0, verbose_name="风速")
    lightstr=models.FloatField(default=0,verbose_name='光照强度')
    lampmode=models.IntegerField(default=0,verbose_name='灯带工作模式')


class dct_t_l3f3dm_alarm_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    alarmflag = models.CharField(max_length=1)
    alarmseverity = models.IntegerField(default=0, blank=True)
    alarmcontent = models.IntegerField(default=0, blank=True)
    alarmtype = models.IntegerField(default=0, blank=True)
    clearflag = models.IntegerField(default=0, blank=True)
    causeid = models.IntegerField(default=0, blank=True)
    tsgen = models.DateTimeField(auto_now_add=True)
    tsclose = models.DateTimeField(null=True, blank=True)
    alarmpic = models.CharField(max_length=100)
    alarmproc = models.TextField(null=True)


class dct_t_l3f3dm_current_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_time = models.DateTimeField(auto_now=True)
    door_1 = models.IntegerField(default=0,null=True)
    door_2 = models.IntegerField(default=0,null=True)
    door_3 = models.IntegerField(default=0,null=True)
    door_4 = models.IntegerField(default=0,null=True)
    lock_1 = models.IntegerField(default=0,null=True)
    lock_2 = models.IntegerField(default=0,null=True)
    lock_3 = models.IntegerField(default=0,null=True)
    lock_4 = models.IntegerField(default=0,null=True)
    battstate = models.IntegerField(default=0,null=True)
    waterstate = models.IntegerField(default=0,null=True)
    shakestate = models.IntegerField(default=0,null=True)
    fallstate = models.IntegerField(default=0,null=True)
    smokestate = models.IntegerField(default=0,null=True)
    battvalue = models.FloatField(default=0, blank=True, verbose_name="电池电量值",null=True)
    fallvalue = models.FloatField(default=0, blank=True, verbose_name="倾斜角度值",null=True)
    tempvalue = models.FloatField(default=0, blank=True, verbose_name="温度值",null=True)
    humidvalue = models.FloatField(default=0, blank=True, verbose_name="湿度值",null=True)
    rssivalue = models.FloatField(default=0, blank=True, verbose_name="信号强度值",null=True)

class dct_t_l3f3dm_minute_report_fhys(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_date = models.DateTimeField(auto_now_add=True)
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
    battvalue = models.FloatField(default=0, blank=True, verbose_name="电池电量值")
    fallvalue = models.FloatField(default=0, blank=True, verbose_name="倾斜角度值")
    tempvalue = models.FloatField(default=0, blank=True, verbose_name="温度值")
    humidvalue = models.FloatField(default=0, blank=True, verbose_name="湿度值")
    rssivalue = models.FloatField(default=0, blank=True, verbose_name="信号强度值")

class dct_t_l3f3dm_alarm_report_fhys(models.Model):
    sid=models.AutoField(primary_key=True)
    dec_code=models.ForeignKey(dct_t_l3f2cm_device_inventory,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common,on_delete=models.CASCADE,null=True)
    alarmflag=models.CharField(max_length=1,null=True)
    alaemseverity=models.IntegerField(default=0)
    alarmcode=models.IntegerField(default=0)
    tsgen=models.DateTimeField(auto_now_add=True)
    tsclose=models.DateTimeField(null=True)
    alarmproc=models.CharField(max_length=200,null=True)


class dct_t_l3f3dm_minute_report_fstt(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_date = models.DateTimeField(auto_now=True)
    hourminindex = models.IntegerField(default=0)
    dataflag=models.CharField(max_length=1,default="Y")
    temperature = models.FloatField(default=0, verbose_name="温度")
    humidity = models.FloatField(default=0, verbose_name="湿度")
    pm25 = models.FloatField(null=True,default=0, verbose_name="PM2.5")
    backlight=models.IntegerField(default=1)
    lampbelt=models.IntegerField(default=1)
    adscreen=models.IntegerField(default=1)
    backtext=models.CharField(max_length=255,null=True)

class dct_t_l3f3dm_hour_report_aqyc(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE,db_index=True)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE,null=True)
    report_date = models.DateTimeField(db_index=True,null=True)
    hourindex = models.IntegerField(default=0,db_index=True)
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
    lightstr = models.FloatField(default=0, verbose_name="光照")
    so2 = models.FloatField(default=0, verbose_name="二氧化硫")
    co1 = models.FloatField(default=0, verbose_name="一氧化碳")
    no1 = models.FloatField(default=0, verbose_name="一氧化氮")
    h2s = models.FloatField(default=0, verbose_name="硫化氢")
    hcho = models.FloatField(default=0, verbose_name="酒精")
    toxicgas = models.FloatField(default=0, verbose_name="煤气")
    rssi = models.FloatField(default=0, verbose_name="信号强度")
    pwrind = models.FloatField(default=0, verbose_name="电量强度")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    