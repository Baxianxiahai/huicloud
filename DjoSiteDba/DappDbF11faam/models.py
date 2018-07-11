from django.db import models
from django.template.defaultfilters import default

# Create your models here.

# class dct_t_l3f11faam_product_stock_sheet(models.Model):
#     sid=models.AutoField(primary_key=True)
#     stockname=models.CharField(max_length=20)
#     stockaddress=models.CharField(max_length=50)
#     stockheader=models.CharField(max_length=10)
#     stocktime=models.DateTimeField(auto_now_add=True)
class dct_t_l3f11faam_typesheet(models.Model):
    sid=models.AutoField(primary_key=True)
    pjcode=models.CharField(max_length=10,default="HYGS")
    typecode=models.CharField(max_length=10,null=True,blank=True,unique=True)
    applenum=models.IntegerField(default=0)
    appleweight=models.IntegerField(default=0)
    applegrade=models.CharField(max_length=1,null=True,blank=True)
    memo=models.CharField(max_length=50,null=True,blank=True)
