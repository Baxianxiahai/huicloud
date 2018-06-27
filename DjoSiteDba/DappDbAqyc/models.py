from django.db import models
from DappDbComm.models import dct_t_l3f2cm_project_common
from DappDbComm.models import dct_t_l3f2cm_site_common
# Create your models here.
class dct_t_l3f2cm_project_aqyc(models.Model):
    prj_code=models.OneToOneField(dct_t_l3f2cm_project_common,on_delete=models.CASCADE,primary_key=True)
    eng_code=models.CharField(max_length=50)
    eng_name=models.CharField(max_length=50,null=True,blank=True)
    prj_type=models.IntegerField
    prj_category=models.IntegerField
    prj_period=models.IntegerField
    district=models.CharField(max_length=5)
    region=models.IntegerField
    street=models.CharField(max_length=50,null=True,blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    contractors=models.CharField(max_length=50,null=True,blank=True)
    eng_addr=models.CharField(max_length=50,null=True,blank=True)
    site_area=models.FloatField(null=True,blank=True)
    building_area=models.FloatField(null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    stage=models.CharField(max_length=2,null=True,blank=True)
    is_completed=models.BooleanField(default=0,blank=True)
    eng_status=models.BooleanField(default=1,blank=True)
class dct_t_l3f2cm_device_aqyc(models.Model):
    dev_code=models.CharField(max_length=20,primary_key=True)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common,on_delete=models.CASCADE)