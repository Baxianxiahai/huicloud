from django.db import models
# Create your models here.
class dct_t_l3fxprcm_locklog_fhys(models.Model):
    sid=models.AutoField(primary_key=True)
    woid=models.CharField(max_length=10)
    site_code=models.IntegerField(default=0)
    keyid=models.CharField(max_length=10)
    keyname=models.CharField(max_length=20)
    ownerid=models.CharField(max_length=15)
    ownername=models.CharField(max_length=20)
    eventtype=models.CharField(max_length=1)
    createtime=models.DateTimeField(auto_now_add=True)
    picname=models.CharField(max_length=100)