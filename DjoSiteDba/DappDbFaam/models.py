from django.db import models

# Create your models here.
class UserGroup(models.Model):
    ugId = models.AutoField(primary_key=True)
    #unique
    #caption = models.CharField(max_length=32, unique=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
    userId = models.IntegerField(default=0)