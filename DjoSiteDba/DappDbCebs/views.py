from django.shortcuts import render, redirect, HttpResponse
from django.contrib import admin
from DappDbCebs import models

# Create your views here.
#输入参数必须是完整的数据集合，并以Json为单位
def CustomerMission_add(request):
    models.CustomerMission.objects.create(\
        user=request['user'],\
        timeStampSubmit=request['timeStampSubmit'],\
        pageNbr=request['pageNbr'],\
        filePath=request['filePath'],\
        fileName=request['fileName'],\
        );
    return HttpResponse("OK")

def CustomerMission_delete(request):
    models.CustomerMission.objects.filter(user=request['user']).delete()
    return HttpResponse("OK")

#使用UserId，修改其他信息
def CustomerMission_modify_by_user(request):
    models.CustomerMission.objects.filter(user=request['user']).update(\
        timeStampSubmit=request['timeStampSubmit'],\
        pageNbr=request['pageNbr'],\
        filePath=request['filePath'],\
        fileName=request['fileName'],\
        );
    return HttpResponse("OK")  # 返回字符串

def CustomerMission_inqury(request):
    return models.CustomerMission.objects.get(user=request['user'])

#输入参数必须是完整的数据集合，并以Json为单位
def ClassifyExecLog_add(request):
    models.ClassifyExecLog.objects.create(\
        user=request['user'],\
        timeStampExec=request['timeStampExec'],\
        pageLen=request['pageLen'],\
        pageWidth=request['pageWidth'],\
        resTotal=request['resTotal'],\
        resTotalAlive=request['resTotalAlive'],\
        resTotalDead=request['resTotalDead'],\
        resSmallAlive=request['resSmallAlive'],\
        resSmallDead=request['resSmallDead'],\
        resMidAlive=request['resMidAlive'],\
        resMidDead=request['resMidDead'],\
        resBigAlive=request['resBigAlive'],\
        resBigDead=request['resBigDead'],\
        resUnclassifyAlive=request['resUnclassifyAlive'],\
        resUnclassifyDead=request['resUnclassifyDead'],\
        );
    return HttpResponse("OK")
    
def ClassifyExecLog_delete(request):
    models.ClassifyExecLog.objects.filter(user=request['user']).delete()
    return HttpResponse("OK")

#使用UserId，修改其他信息
def ClassifyExecLog_modify_by_user(request):
    models.ClassifyExecLog.objects.filter(user=request['user']).update(\
        timeStampExec=request['timeStampExec'],\
        pageLen=request['pageLen'],\
        pageWidth=request['pageWidth'],\
        resTotal=request['resTotal'],\
        resTotalAlive=request['resTotalAlive'],\
        resTotalDead=request['resTotalDead'],\
        resSmallAlive=request['resSmallAlive'],\
        resSmallDead=request['resSmallDead'],\
        resMidAlive=request['resMidAlive'],\
        resMidDead=request['resMidDead'],\
        resBigAlive=request['resBigAlive'],\
        resBigDead=request['resBigDead'],\
        resUnclassifyAlive=request['resUnclassifyAlive'],\
        resUnclassifyDead=request['resUnclassifyDead'],\
        );
    return HttpResponse("OK")  # 返回字符串

def ClassifyExecLog_inqury(request):
    return models.ClassifyExecLog.objects.get(user=request['user']);










