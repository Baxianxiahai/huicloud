#from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
#from django.contrib import admin
from DappDbComm import models
#from ipywidgets.widgets.tests.utils import undefined

# Create your views here.
#输入参数必须是完整的数据集合，并以Json为单位
# def UserGroup_add(request):
#     models.UserGroup.objects.create(\
#         caption=request['caption'],\
#         ctime= request['ctime'],\
#         uptime=request['uptime'],\
#         userId=request['userId'],\
#         );
#     return HttpResponse("OK")
#
# def UserGroup_delete(request):
#     models.UserGroup.objects.filter(userId=request['userId']).delete()
#     return HttpResponse("OK")
#
# #使用UserId，修改其他信息
# def UserGroup_modify_by_userId(request):
#     models.UserGroup.objects.filter(userId=request['userId']).update(\
#         caption=request['caption'],\
#         ctime=request['ctime'],\
#         uptime=request['uptime'],\
#         userId=request['userId'],\
#         );
#     return HttpResponse("OK")  # 返回字符串

def det_insert_name():
    return


