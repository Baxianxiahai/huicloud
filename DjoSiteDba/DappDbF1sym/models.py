from django.db import models
import datetime
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
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary.uid,on_delete=models.CASCADE,primary_key=True)
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
    menu_code=models.ForeignKey(dct_t_l3f1sym_menu_code_mapping.menu_code,on_delete=models.CASCADE)
    menu_name=models.CharField(max_length=20)
class dct_t_l3f1sym_user_right_action(models.Model):
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
    uid=models.ForeignKey(dct_t_l3f1sym_account_primary.uid,on_delete=models.CASCADE)
    auth_type=models.IntegerField(default=0)
    auth_code=models.IntegerField(default=0)
class dct_t_l3f1sym_user_login_session(models.Model):
    uid=models.OneToOneField(dct_t_l3f1sym_account_primary.uid,primary_key=True,on_delete=models.CASCADE)
    session_id=models.CharField(max_length=10)
    timestamp=models.IntegerField(verbose_name="更新时间戳",default=datetime.datetime.now)