from django.db import models

# Create your models here.
class UserGroup(models.Model):
    ugId = models.AutoField(primary_key=True)
    #unique可以用来修饰，某个域，只能存储一次
    #caption = models.CharField(max_length=32, unique=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
    userId = models.IntegerField(default=0)
        
class UserAccount(models.Model):
    userId = models.AutoField(primary_key=True)
    userAccount = models.CharField(max_length=32, verbose_name='用户') #用于8001/Admin中显示展示用户的名称
    userPwd = models.CharField(max_length=32, verbose_name='密码')
    nickName = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=40, null=True)
    homeAddress = models.CharField(max_length=50, null=True)
    homeCity = models.CharField(max_length=60, null=True)
    stateProvince = models.CharField(max_length=30, null=True)
    homeCountry = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
    emailaddr = models.EmailField(max_length=30, null=True)
    email = models.EmailField(null=True)
    ipaddr = models.GenericIPAddressField(max_length=30, null=True)    
    
    
    
        
    
    