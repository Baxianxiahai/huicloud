from django.db import models
from DappDbF1sym.models import dct_t_l3f1sym_account_primary
from django.template.defaultfilters import default

# Create your models here.
class dct_t_l3f2cm_pg_common(models.Model):
    pg_code = models.AutoField(primary_key=True)
    pg_name = models.CharField(max_length=20)
    pg_creator = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(null=True)


class dct_t_l3f2cm_project_common(models.Model):
    prj_code = models.AutoField(primary_key=True)
    prj_name = models.CharField(max_length=20)
    pg_code = models.ForeignKey(dct_t_l3f2cm_pg_common, on_delete=models.SET_NULL,null=True)
    prj_creator = models.CharField(max_length=10)
    create_date = models.DateField(null=True,blank=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(null=True)


class dct_t_l3f2cm_site_common(models.Model):
    site_code = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=20)
    prj_code = models.ForeignKey(dct_t_l3f2cm_project_common, on_delete=models.CASCADE,null=True)
    site_creator = models.CharField(max_length=10)
    status=models.CharField(max_length=2,null=True)
    create_date = models.DateField(null=True,blank=True)
    superintendent = models.CharField(max_length=20, null=True, blank=True)
    department=models.CharField(max_length=50,null=True,blank=True)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    district=models.CharField(max_length=15,null=True)
    site_area = models.FloatField(null=True, default=0,blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=6,default=0)
    comments = models.TextField(null=True, blank=True)
    

class dct_t_l3f2cm_device_inventory(models.Model):
    # null=true显示的是数据库中该字段可以为空，blank=true表示在admin后台管理界面上该字段可以不填
    dev_code = models.CharField(max_length=20, primary_key=True)
    valid_flag = models.BooleanField(default=False)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE, null=True)
    create_date = models.DateField(null=True, blank=True)
    hw_type = models.IntegerField(default=0, blank=True)
    sw_ver = models.IntegerField(null=True, blank=True)
    zhb_label = models.CharField(max_length=50, null=True)
    upgradeflag = models.IntegerField(default=0)
    rebootflag = models.IntegerField(default=0)
    base_port = models.IntegerField(default=0)
    cus_info=models.CharField(max_length=50,null=True)
    eccport=models.IntegerField(default=0)
    username=models.CharField(max_length=50,null=True)
    userpswd=models.CharField(max_length=100,null=True)
    userdef1=models.CharField(max_length=100,null=True)
    userdef2=models.CharField(max_length=100,null=True)
    userdef3=models.CharField(max_length=100,null=True)
    userdef4=models.CharField(max_length=100,null=True)

class dct_t_l3f2cm_device_cail(models.Model):
    dev_code=models.OneToOneField(dct_t_l3f2cm_device_inventory,on_delete=models.CASCADE)
    dust_coefmax = models.FloatField(default=700)
    dust_coefmin = models.FloatField(default=10)
    dust_coefK = models.FloatField(default=1)
    dust_coefB = models.FloatField(default=0)
    dust_threshold = models.FloatField(default=30)
    temp_coefmax = models.FloatField(default=100)
    temp_coefmin = models.FloatField(default=-40)
    temp_coefK = models.FloatField(default=1)
    temp_coefB = models.FloatField(default=0)
    humid_coefmax = models.FloatField(default=100)
    humid_coefmin = models.FloatField(default=0)
    humid_coefK = models.FloatField(default=1)
    humid_coefB = models.FloatField(default=0)
    noise_coefmax = models.FloatField(default=130)
    noise_coefmin = models.FloatField(default=30)
    noise_coefK = models.FloatField(default=1)
    noise_coefB = models.FloatField(default=0)
    windspd_coefmax = models.FloatField(default=35)
    windspd_coefmin = models.FloatField(default=0)
    windspd_coefK = models.FloatField(default=1)
    windspd_coefB = models.FloatField(default=0)
    winddir_coefmax = models.FloatField(default=360)
    winddir_coefmin = models.FloatField(default=0)
    winddir_coefK = models.FloatField(default=1)
    winddir_coefB = models.FloatField(default=0)
    winddir_delta = models.FloatField(default=0)
    dust_cannon=models.FloatField(default=200)

class dct_t_l3f2cm_device_holops(models.Model):
    cpu_id=models.CharField(primary_key=True,max_length=50)
    valid_flag=models.BooleanField(default=False)
    last_update=models.DateTimeField(null=True)
    dev_code=models.CharField(max_length=20,null=True)
    socket_id=models.IntegerField(default=0)
    cmd_flag=models.IntegerField(default=0)
    prjid=models.IntegerField(default=0)
    prjname=models.CharField(max_length=50,null=True)
    
class dct_t_l3f2cm_favour_site(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f1sym_account_primary, on_delete=models.CASCADE)
    site_code = models.ForeignKey(dct_t_l3f2cm_site_common, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)

class dct_t_l3f2cm_project_aqyc(models.Model):
    prj_code = models.OneToOneField(dct_t_l3f2cm_project_common, on_delete=models.CASCADE, primary_key=True)
    eng_code = models.CharField(max_length=50)
    eng_name = models.CharField(max_length=50, null=True, blank=True)
    prj_type = models.IntegerField(default=0)
    prj_category = models.IntegerField(default=0)
    prj_period = models.IntegerField(default=0)
    district = models.CharField(max_length=5)
    region = models.IntegerField(default=0)
    street = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    contractors = models.CharField(max_length=50, null=True, blank=True)
    eng_addr = models.CharField(max_length=50, null=True, blank=True)
    site_area = models.FloatField(null=True, blank=True)
    building_area = models.FloatField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    stage = models.CharField(max_length=2, null=True, blank=True)
    is_completed = models.BooleanField(default=0, blank=True)
    eng_status = models.BooleanField(default=1, blank=True)


class dct_t_l3f2cm_device_aqyc(models.Model):
    dev_code = models.OneToOneField(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE, primary_key=True)
    ip_addr = models.GenericIPAddressField(null=True)
    mac_addr = models.CharField(null=True,max_length=20)
    web_url=models.CharField(null=True,max_length=100)
    pic1_url = models.CharField(null=True,max_length=100)
    ctrl1_url = models.CharField(null=True,max_length=100)
    video1_url = models.CharField(null=True,max_length=100)


class dct_t_l3f2cm_project_fstt(models.Model):
    prj_code = models.OneToOneField(dct_t_l3f2cm_project_common, primary_key=True, on_delete=models.CASCADE)


class dct_t_l3f2cm_site_fstt(models.Model):
    site_code = models.OneToOneField(dct_t_l3f2cm_site_common, primary_key=True, on_delete=models.CASCADE)
    order_no = models.CharField(max_length=10)
    tower_sn = models.CharField(max_length=10)
    tower_code = models.CharField(max_length=15)
    tower_type = models.IntegerField(default=0, blank=True)
    tower_conf = models.IntegerField(default=0, blank=True)
    tower_date = models.DateField(default=0, blank=True)
    install_date = models.DateTimeField(auto_now=True, blank=True)
    lamp_start = models.TimeField(null=True, default="00:00:00")
    lamp_stop = models.TimeField(null=True, default="00:00:00")
    lamp_th=models.IntegerField(default=0)
    lamp_mode = models.IntegerField(default=0, null=True)
    snr_light = models.IntegerField(default=0)


class dct_t_l3f2cm_device_fstt(models.Model):
    dev_code = models.OneToOneField(dct_t_l3f2cm_device_inventory, on_delete=models.CASCADE, primary_key=True)
    socket_id=models.IntegerField(default=0)
    ip_addr = models.GenericIPAddressField(null=True)
    mac_addr = models.CharField(null=True, max_length=20)
    web_url = models.CharField(null=True, max_length=100)
    pic1_url = models.CharField(null=True, max_length=100)
    ctrl1_url = models.CharField(null=True, max_length=100)
    video1_url = models.CharField(null=True, max_length=100)
    pic2_url = models.CharField(null=True, max_length=100)
    ctrl2_url = models.CharField(null=True, max_length=100)
    video2_url = models.CharField(null=True, max_length=100)
    pic3_url = models.CharField(null=True, max_length=100)
    ctrl3_url = models.CharField(null=True, max_length=100)
    video3_url = models.CharField(null=True, max_length=100)

class dct_t_l3f2cm_virtual_key_fhys(models.Model):
    keyid=models.CharField(primary_key=True,max_length=10)
    keyname=models.CharField(max_length=20)
    prj_code=models.ForeignKey(dct_t_l3f2cm_project_common,on_delete=models.CASCADE)
    ownerid=models.CharField(null=True,max_length=15)
    ownername=models.CharField(null=True,max_length=20)
    keystatus=models.CharField(max_length=1)
    keytype=models.CharField(max_length=1)
    hwcode=models.CharField(max_length=50)
    memo=models.TextField(null=True)
    class Meta:
        index_together=['keytype']

class dct_t_l3f2cm_key_auth_fhys(models.Model):
    sid=models.AutoField(primary_key=True)
    keyid=models.ForeignKey(dct_t_l3f2cm_virtual_key_fhys,on_delete=models.CASCADE)
    authlevel=models.CharField(max_length=1)
    authobj=models.IntegerField(default=0)
    authtype=models.CharField(max_length=1)
    validnum=models.IntegerField(default=0)
    validstart=models.DateField(null=True)
    validend=models.DateField(null=True)