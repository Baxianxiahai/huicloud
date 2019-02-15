from django.db import models


# Create your models here.
class dct_t_l3f12iwdp_user(models.Model):
    uid = models.CharField(max_length=40, primary_key=True)
    uname = models.CharField(max_length=14)
    uemail = models.CharField(max_length=40, null=True)
    uavatar=models.TextField(null=True)
    utelephone = models.CharField(max_length=15, null=True)
    ucompanyid = models.CharField(max_length=50, null=True)
    ucompanyname = models.CharField(max_length=50, null=True)
    udepartmentid = models.CharField(max_length=50, null=True)
    udepartmentname = models.CharField(max_length=50, null=True)
    ulevel=models.IntegerField(default=0)


class dct_t_l3f12iwdp_integral_setting(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f12iwdp_user, on_delete=models.CASCADE)
    accept = models.IntegerField(default=0)
    refuse = models.IntegerField(default=0)
    finish = models.IntegerField(default=0)
    unfinish = models.IntegerField(default=0)
    outtime = models.IntegerField(default=0)

class dct_t_l3f12iwdp_task(models.Model):
    taskid=models.CharField(max_length=18,primary_key=True)
    taskname=models.CharField(max_length=25)
    taskdescribe=models.TextField(null=True)
    tasklevel=models.IntegerField(default=0)
    taskstart=models.DateTimeField()
    taskend=models.DateTimeField()
    taskremind=models.DateTimeField(null=True)
    taskendtime=models.DateTimeField(null=True)
    taskenclosure = models.TextField(null=True)
    tasksoundid=models.CharField(max_length=30,null=True)
    taskstate=models.IntegerField(default=0)
    taskreview=models.IntegerField(default=0)
    comment = models.TextField(default='[]')

class dct_t_l3f12iwdp_user_task(models.Model):
    sid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(dct_t_l3f12iwdp_user,on_delete=models.CASCADE)
    taskid=models.ForeignKey(dct_t_l3f12iwdp_task,on_delete=models.CASCADE)
    user_type=models.IntegerField(default=0,db_index=True)
    taskaccept=models.IntegerField(default=0)
    integral=models.IntegerField(default=0)
    show=models.BooleanField(default=False)
    read=models.BooleanField(default=False)

class dct_t_l3f12iwdp_company_jsapi_ticket(models.Model):
    sid=models.AutoField(primary_key=True)
    cordid=models.CharField(max_length=50)
    jsticket=models.TextField(null=False)
    last_time=models.DateTimeField(null=False)
