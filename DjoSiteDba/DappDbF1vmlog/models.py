from django.db import models


# Create your models here.

class dct_t_l3f1vm_loginfo(models.Model):
    sid = models.AutoField(primary_key=True)
    sysver = models.CharField(max_length=10)
    syspgm = models.CharField(max_length=50)
    sysprj = models.CharField(max_length=50)
    fromuser = models.CharField(max_length=50)
    srcname = models.CharField(max_length=50)
    destname = models.CharField(max_length=50)
    msgid = models.CharField(max_length=50)
    logtime = models.DateTimeField(auto_now=True)
    logdata = models.TextField(null=True)


class dct_t_l3f1vm_logtracetask(models.Model):
    sid = models.AutoField(primary_key=True)
    taskid = models.IntegerField(default=0)
    allowflag = models.BooleanField(default=False)
    restrictflag = models.BooleanField(default=False)


class dct_t_l3f1vm_logtracemsg(models.Model):
    sid = models.AutoField(primary_key=True)
    msgid = models.IntegerField(default=0)
    allowflag = models.BooleanField(default=False)
    restrictflag = models.BooleanField(default=False)
