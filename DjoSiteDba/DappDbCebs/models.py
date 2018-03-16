# coding:utf8
from django.db import models

# Create your models here.

class CustomerMission(models.Model):
    sid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32)
    timeStampSubmit = models.DateTimeField(auto_now=True, null=True)
    pageNbr = models.IntegerField(default=0)
    filePath = models.CharField(max_length=254)
    fileName = models.CharField(max_length=254)    

class ClassifyExecLog(models.Model):
    sid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32)
    timeStampExec = models.DateTimeField(auto_now=True, null=True)
    pageLen = models.IntegerField(default=0)
    pageWidth = models.IntegerField(default=0)
    resTotal = models.IntegerField(default=0)
    resTotalAlive = models.IntegerField(default=0)
    resTotalDead = models.IntegerField(default=0)
    resSmallAlive = models.IntegerField(default=0)
    resSmallDead = models.IntegerField(default=0)
    resMidAlive = models.IntegerField(default=0)
    resMidDead = models.IntegerField(default=0)
    resBigAlive = models.IntegerField(default=0)
    resBigDead = models.IntegerField(default=0)
    resUnclassifyAlive = models.IntegerField(default=0)
    resUnclassifyDead = models.IntegerField(default=0)

    
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     publication_date = models.DateField()






