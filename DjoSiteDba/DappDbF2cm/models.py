from django.db import models
from DappDbF1sym.models import dct_t_l3f1sym_account_primary

# Create your models here.
class dct_t_l3f2cm_pg_common(models.Model):
    pg_code=models.AutoField(primary_key=True)
    pg_name=models.CharField(max_length=20)
    pg_creator=models.CharField(max_length=10)
    create_date=models.DateTimeField(auto_now=True,blank=True)
    superintendent=models.CharField(max_length=20,null=True,blank=True)
    telephone=models.CharField(max_length=15,null=True,blank=True)
    department=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    comments=models.TextField(null=True)
class dct_t_l3f2cm_project_common(models.Model):
    prj_code=models.AutoField(primary_key=True)
    prj_name=models.CharField(max_length=20)
    pg_code=models.ForeignKey(dct_t_l3f2cm_pg_common.pg_code,on_delete=models.CASCADE)
    prj_creator=models.CharField(max_length=10)
    create_date=models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True,blank=True)
    telephone = models.CharField(max_length=15, null=True,blank=True)
    department = models.CharField(max_length=50, null=True,blank=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    comments = models.TextField(null=True)
class dct_t_l3f2cm_site_common(models.Model):
    site_code = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=20)
    prj_code = models.ForeignKey(dct_t_l3f2cm_project_common.prj_code, on_delete=models.CASCADE)
    site_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now=True)
    superintendent = models.CharField(max_length=20, null=True,blank=True)
    telephone = models.CharField(max_length=15, null=True,blank=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    comments = models.TextField(null=True,blank=True)
class dct_t_l3f2cm_device_common(models.Model):
    #null=true显示的是数据库中该字段可以为空，blank=true表示在admin后台管理界面上该字段可以不填
    dev_code=models.CharField(max_length=20,primary_key=True)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now=True)
    socket_id=models.IntegerField(null=True,blank=True)
    hw_type=models.IntegerField(null=True,blank=True)
    hw_ver=models.IntegerField(null=True,blank=True)
    sw_rel=models.IntegerField(null=True,blank=True)
    sw_ver=models.IntegerField(null=True,blank=True)
class dct_t_l3f2cm_favour_site(models.Model):
    sid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(dct_t_l3f1sym_account_primary.uid,on_delete=models.CASCADE)
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common.site_code,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now=True)

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
    dev_code=models.ForeignKey(dct_t_l3f2cm_device_common.dev_code,on_delete=models.CASCADE,primary_key=True)
    ip_addr=models.IPAddressField
    mac_addr=models.CharField(max_length=20)
    cam_url=models.CharField(max_length=100)
    ctrl_url=models.CharField(max_length=100)
    ctrl_port=models.IntegerField
    rtsp_port=models.IntegerField
    service_port=models.IntegerField
    ssh_port=models.IntegerField
    vnc_port=models.IntegerField
    nvr_web_port=models.IntegerField
    nvr_rstp_port=models.IntegerField    
    
class dct_t_l3f2cm_project_fstt(models.Model):
    prj_code=models.OneToOneField(dct_t_l3f2cm_project_common.prj_code,primary_key=True,on_delete=models.CASCADE)
    
class t_l3f2cm_site_fstt(models.Model):
    site_code=models.OneToOneField(dct_t_l3f2cm_site_common.site_code,primary_key=True,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=10)
    tower_sn=models.CharField(max_length=10)
    tower_code=models.CharField(max_length=15)
    tower_type=models.IntegerField(default=0,blank=True)
    tower_conf=models.IntegerField(default=0,blank=True)
    tower_date=models.DateTimeField(default=0,blank=True)
    install_date=models.DateTimeField(default=0,blank=True)   
    
class dct_t_l3f2cm_device_fstt(models.Model):
    dev_code=models.OneToOneField(dct_t_l3f2cm_device_common.dev_code,primary_key=True,on_delete=models.CASCADE)
    cam_url=models.CharField(max_length=100)
    ctrl_url=models.CharField(max_length=100)
    ctrl1_port=models.IntegerField
    rtsp1_port=models.IntegerField
    service_port=models.IntegerField
    ssh_port=models.IntegerField
    vnc_port=models.IntegerField
    ctrl2_port=models.IntegerField(null=True,blank=True)
    rtsp2_port=models.IntegerField(null=True,blank=True)
    ctrl3_port=models.IntegerField(null=True,blank=True)
    rtsp3_port=models.IntegerField(null=True,blank=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    