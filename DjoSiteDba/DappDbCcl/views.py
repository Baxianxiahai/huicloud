from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import admin
from DappDbCcl import models
#from ipywidgets.widgets.tests.utils import undefined

# Create your views here.
def UserGroup_add(request):
    models.UserGroup.objects.create(\
        caption=request['caption'],\
        ctime= request['ctime'],\
        uptime=request['uptime'],\
        userId=request['userId'],\
        );
    return HttpResponse("OK")