from django.db import models
from DappDbF2cm.models import dct_t_l3f2cm_device_inventory,dct_t_l3f2cm_site_common
# Create your models here.
class dct_t_l3f6pm_perfdata(models.Model):
    sid=models.AutoField(primary_key=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_inventory,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common,on_delete=models.CASCADE)
    createtime=models.DateTimeField(auto_now_add=True)
    restartcnt=models.IntegerField(default=0)
    networkconncnt=models.IntegerField(default=0)
    networkconnfailcnt=models.IntegerField(default=0)
    networkdisccnt=models.IntegerField(default=0)
    socketdisccnt=models.IntegerField(default=0)
    cpuoccupy=models.IntegerField(default=0)
    memoccupy=models.IntegerField(default=0)
    diskoccupy=models.IntegerField(default=0)
    cputemp=models.IntegerField(default=0)
    workcontmins=models.IntegerField(default=0)
    alarmcnt=models.IntegerField(default=0)
    dischomecnt=models.IntegerField(default=0)
    vmerrcnt=models.IntegerField(default=0)

class dct_t_l3f6pm_optkpi(models.Model):
    sid=models.AutoField(primary_key=True)
    createtime=models.DateTimeField(null=True)
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_inventory,on_delete=models.CASCADE)
    ol_score=models.IntegerField(default=0)
    conn_freq=models.FloatField(default=0)