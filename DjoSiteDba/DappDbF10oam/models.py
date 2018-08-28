from django.db import models

# Create your models here.
class dct_t_l3f10oam_qrcodeinfo(models.Model):
    sid=models.AutoField(primary_key=True)
    pdtype=models.CharField(max_length=3,null=True)
    pdcode=models.CharField(max_length=5,null=True)
    pjcode=models.CharField(max_length=5,null=True)
    dev_code=models.CharField(max_length=20,null=True)
    validflag=models.CharField(max_length=1,default="N")
    validdate=models.DateField(null=True)
    class Meta:
        index_together=['pdtype','pdcode','pjcode']
class dct_t_l3f10oam_regqrcode(models.Model):
    sid=models.AutoField(primary_key=True)
    applytime=models.DateTimeField(auto_now_add=True)
    applyuser=models.CharField(max_length=20)
    faccode=models.CharField(max_length=20)
    pdtype = models.CharField(max_length=3, null=True)
    pdcode = models.CharField(max_length=5, null=True)
    pjcode = models.CharField(max_length=5, null=True)
    usercode=models.CharField(max_length=3,null=True)
    isformal=models.CharField(max_length=1,null=True)
    applynum=models.IntegerField(default=0)
    approvenum=models.IntegerField(default=0)
    digstart=models.IntegerField(default=0)
    digstop=models.IntegerField(default=0)
    zipfile=models.CharField(max_length=30)
    class Meta:
        index_together=['pdtype','pdcode','pjcode']

class dct_t_l3f10oam_swloadinfo(models.Model):
    sid=models.AutoField(primary_key=True)
    equentry=models.IntegerField(default=0)
    validflag=models.IntegerField(default=0)
    upgradeflag=models.IntegerField(default=0)
    hwtype=models.IntegerField(default=0)
    hwid=models.IntegerField(default=0)
    swrel=models.IntegerField(default=0)
    swver=models.IntegerField(default=0)
    dbver=models.IntegerField(default=0)
    filelink=models.CharField(max_length=100)
    filesize=models.IntegerField(default=0)
    checksum=models.IntegerField(default=0)
    createtime=models.DateTimeField(auto_now_add=True)
    note=models.TextField(null=True)
    class Meta:
        index_together=['equentry','upgradeflag','hwtype']