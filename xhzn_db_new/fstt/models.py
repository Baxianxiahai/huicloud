from django.db import models
from xhzn.models import t_l3f2cm_device_common as device,t_l3f2cm_site_common as site
# Create your models here.
class t_l3f2cm_device_fstt(models.Model):
    dev_code=models.OneToOneField(device,primary_key=True,on_delete=models.CASCADE)
    site_code=models.ForeignKey(site)
    cam_ctrl=models.CharField(max_length=50)
    video_ctrl=models.CharField(max_length=50)
class t_l3f2cm_site_fstt(models.Model):
    site_code=models.OneToOneField(site,primary_key=True,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=10)
    tower_sn=models.CharField(max_length=10)
    tower_code=models.CharField(max_length=15)
    tower_type=models.IntegerField(default=0)
    tower_conf=models.IntegerField(default=0)
    tower_date=models.DateTimeField(default=0)
    install_date=models.DateTimeField(default=0)