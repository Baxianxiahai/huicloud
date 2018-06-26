from django.db import models
from test.test_functools import decimal
from DappDbF2cm.models import dct_t_l3f2cm_device_common,dct_t_l3f2cm_site_common

# Create your models here.
class dct_t_l2snr_sensor_type(models.Model):
    snr_code=models.CharField(max_length=10,primary_key=True,on_delete=models.CASCADE)
    snr_name=models.CharField(max_length=15)
    value_min=models.FloatField(max_digits=10,decimal_places=4,verbose_name="量程最小值")
    value_max=models.FloatField(max_digits=10,decimal_places=4,verbose_name="量程最大值")
    snr_model=models.CharField(max_length=20)
    snr_vendor=models.CharField(max_length=20)
class dct_l2snr_dust(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    tsp=models.FloatField(max_digits=10,decimal_places=4,verbose_name="TSP")
    pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
    pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
    pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
class dct_l2snr_noise(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    noise=models.FloatField(max_digits=10,decimal_places=4,verbose_name="噪声")
#     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
#     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
#     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    
class dct_l2snr_temperature(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    temperature=models.FloatField(max_digits=10,decimal_places=4,verbose_name="温度值")
#     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
#     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
#     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    
class dct_l2snr_humidity(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    humidity=models.FloatField(max_digits=10,decimal_places=4,verbose_name="湿度值")
#     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
#     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
#     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    
class dct_l2snr_winddir(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    windir=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风向")
#     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
#     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
#     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    
class dct_l2snr_windspd(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE)
    windspd=models.FloatField(max_digits=10,decimal_places=4,verbose_name="风速")
#     pm01=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM0.1")
#     pm25=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM2.5")
#     pm10=models.FloatField(max_digits=10,decimal_places=4,verbose_name="PM10")
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField
    
class dct_l2snr_picture(models.Model):
    sid=models.AutoField(primary_key=True)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    file_name=models.TextField(max_length=100)
    file_size=models.IntegerField
    description=models.TextField(max_length=100)
    dataflag=models.CharField(max_length=1)
    report_data=models.DateTimeField(auto_now=True)
    hourminindex=models.IntegerField