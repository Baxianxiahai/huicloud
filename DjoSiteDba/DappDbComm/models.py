from django.db import models
import datetime
# Create your models here.
# class UserGroup(models.Model):
#     ugId = models.AutoField(primary_key=True)
#     #unique可以用来修饰，某个域，只能存储一次
#     #caption = models.CharField(max_length=32, unique=True)
#     caption = models.CharField(max_length=32)
#     ctime = models.DateTimeField(auto_now_add=True, null=True)
#     uptime = models.DateTimeField(auto_now=True, null=True)
#     userId = models.IntegerField(default=0)
#
# class UserAccount(models.Model):
#     userId = models.AutoField(primary_key=True)
#     userAccount = models.CharField(max_length=32, verbose_name='用户') #用于8001/Admin中显示展示用户的名称
#     userPwd = models.CharField(max_length=32, verbose_name='密码')
#     nickName = models.CharField(max_length=30, null=True)
#     first_name = models.CharField(max_length=30, null=True)
#     last_name = models.CharField(max_length=40, null=True)
#     homeAddress = models.CharField(max_length=50, null=True)
#     homeCity = models.CharField(max_length=60, null=True)
#     stateProvince = models.CharField(max_length=30, null=True)
#     homeCountry = models.CharField(max_length=50, null=True)
#     website = models.URLField(null=True)
#     emailaddr = models.EmailField(max_length=30, null=True)
#     email = models.EmailField(null=True)
#     ipaddr = models.GenericIPAddressField(max_length=30, null=True)



#DJZ Start Write


# Create your models here.
class dct_t_l3f1sym_account_primary(models.Model):
    uid=models.CharField(max_length=15,primary_key=True)
    login_name=models.CharField(max_length=20,db_index=True)
    pass_word=models.CharField(max_length=100)
    email=models.EmailField(null=True,blank=True)
    menu_group=models.IntegerField(default=0)
    grade_lever=models.IntegerField(null=True,blank=True)
    red_date=models.DateTimeField(auto_now_add=True)
class dct_t_l3f1sym_account_secondary(models.Model):
    CHOICES=((1,'男'),(2,'女'),(3,'第三人'))
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary,on_delete=models.CASCADE,primary_key=True)
    nick_name=models.CharField(max_length=20,null=True,blank=True)
    true_name=models.CharField(max_length=20,null=True,blank=True)
    gender=models.IntegerField(choices=CHOICES)
    age=models.IntegerField(null=True,blank=True)
    telephone=models.CharField(max_length=11,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
class dct_t_l3f1sym_menu_code_mapping(models.Model):
    menu_code=models.IntegerField(primary_key=True)
    menu_name=models.CharField(max_length=20)
class dct_t_l3f1sym_user_right_menu(models.Model):
    sid=models.AutoField(primary_key=True)
    menu_group=models.IntegerField(default=0)
    menu_code=models.ForeignKey(dct_t_l3f1sym_menu_code_mapping,on_delete=models.CASCADE)
    menu_name=models.CharField(max_length=20)
class dct_t_l3f1sym_user_action(models.Model):
    sid=models.AutoField(primary_key=True)
    action_code = models.IntegerField(unique=True)
    action_name=models.CharField(max_length=20)
    l1_auth = models.BooleanField(default=0,blank=True)
    l2_auth = models.BooleanField(default=0,blank=True)
    l3_auth = models.BooleanField(default=0,blank=True)
    l4_auth = models.BooleanField(default=0,blank=True)
    l5_auth = models.BooleanField(default=0,blank=True)
class dct_t_l3f1sym_user_right_project(models.Model):
    sid=models.AutoField(primary_key=True)
    uid=models.ForeignKey(dct_t_l3f1sym_account_primary,on_delete=models.CASCADE)
    auth_type=models.IntegerField(default=0)
    auth_code=models.IntegerField(default=0)
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
    pg_code=models.ForeignKey(dct_t_l3f2cm_pg_common,on_delete=models.CASCADE)
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
    prj_code = models.ForeignKey(dct_t_l3f2cm_project_common, on_delete=models.CASCADE)
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
    site_code=models.ForeignKey(dct_t_l3f2cm_site_common,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now=True)
    socket_id=models.IntegerField(null=True,blank=True)
    hw_type=models.IntegerField(null=True,blank=True)
    hw_ver=models.IntegerField(null=True,blank=True)
    sw_rel=models.IntegerField(null=True,blank=True)
    sw_ver=models.IntegerField(null=True,blank=True)
class dct_t_l3f1sym_user_login_session(models.Model):
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary,primary_key=True,on_delete=models.CASCADE)
    session_id=models.CharField(max_length=10)
    timestamp=models.IntegerField(verbose_name="更新时间戳",default=datetime.datetime.now)

    
    
    
        
    
    