from django.db import models
from DappDbF2cm.models import dct_t_l3f2cm_device_inventory,dct_t_l3f2cm_site_common

# Create your models here.
class dct_t_l2snr_sensor_type(models.Model):
    snr_code = models.CharField(max_length=10, primary_key=True)
    snr_name = models.CharField(max_length=15)
    value_min = models.FloatField(default=0,blank=True,  verbose_name="量程最小值")
    value_max = models.FloatField(default=0,blank=True,  verbose_name="量程最大值")
    snr_model = models.CharField(max_length=20)
    snr_vendor = models.CharField(max_length=20)

class dct_t_l2snr_sensor_ctrl(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.CharField(max_length=20)
    snrid=models.CharField(max_length=20)
    modbus_addr=models.IntegerField(default=0)
    snrtype=models.CharField(max_length=10)
    meas_period=models.IntegerField(default=0)
    status=models.CharField(max_length=5,default="on")
    rx_interval=models.IntegerField(default=0)
    meas_times=models.IntegerField(default=0)

class dct_t_l2snr_dust(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    tsp = models.FloatField(default=0,blank=True, verbose_name="TSP")
    pm01 = models.FloatField(default=0,blank=True, verbose_name="PM0.1")
    pm25 = models.FloatField(default=0,blank=True, verbose_name="PM2.5")
    pm10 = models.FloatField(default=0,blank=True, verbose_name="PM10")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_noise(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    noise = models.FloatField(default=0,blank=True, verbose_name="噪声")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_temperature(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0,blank=True, verbose_name="温度值")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_humidity(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    humidity = models.FloatField(default=0,blank=True, verbose_name="湿度值")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_winddir(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    windir = models.FloatField(default=0,blank=True, verbose_name="风向")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_windspd(models.Model):
    sid = models.AutoField(primary_key=True)
    dev_code = models.ForeignKey(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE)
    windspd = models.FloatField(default=0,blank=True,  verbose_name="风速")
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)


class dct_t_l2snr_picture(models.Model):
    sid = models.AutoField(primary_key=True)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    file_name = models.TextField(max_length=100)
    file_size = models.IntegerField(default=0)
    description = models.TextField(max_length=100)
    dataflag = models.CharField(max_length=1)
    report_data = models.DateField(auto_now=True)
    hourminindex = models.IntegerField(default=0)