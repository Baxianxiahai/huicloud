from django.db import models

# Create your models here.

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
    
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    emailaddr = models.EmailField(max_length=30)
    ipaddr = models.GenericIPAddressField(max_length=30)
 
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
 
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()






