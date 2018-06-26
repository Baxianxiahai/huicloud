from django.db import models
from DappDbComm.models import dct_t_l3f2cm_project_common,dct_t_l3f2cm_device_common as device,dct_t_l3f2cm_site_common as site
# Create your models here.
# class dct_t_l3f2cm_project_fstt(models.Model):
#     prj_code=models.OneToOneField(dct_t_l3f2cm_project_common,primary_key=True,on_delete=models.CASCADE)
class t_l3f2cm_device_fstt(models.Model):
    dev_code=models.OneToOneField(device,primary_key=True,on_delete=models.CASCADE)
    site_code=models.ForeignKey(site,on_delete=models.CASCADE)
    cam_ctrl=models.CharField(max_length=50)
    video_ctrl=models.CharField(max_length=50)
class t_l3f2cm_site_fstt(models.Model):
    site_code=models.OneToOneField(site,primary_key=True,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=10)
    tower_sn=models.CharField(max_length=10)
    tower_code=models.CharField(max_length=15)
    tower_type=models.IntegerField(default=0,blank=True)
    tower_conf=models.IntegerField(default=0,blank=True)
    tower_date=models.DateTimeField(default=0,blank=True)
    install_date=models.DateTimeField(default=0,blank=True)