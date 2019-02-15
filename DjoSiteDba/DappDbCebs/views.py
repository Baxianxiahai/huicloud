from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib import admin
import random
import datetime
import time
#import pycurl
import io

from DappDbCebs import models

# Create your views here.
class dct_classDbiViewDebs:
    def __init__(self):
        pass

    #输入参数必须是完整的数据集合，并以Json为单位
    def CustomerMission_add(self, request):
        models.t_customer_mission.objects.create(\
            user=request['user'],\
            timeStampSubmit=request['timeStampSubmit'],\
            pageNbr=request['pageNbr'],\
            filePath=request['filePath'],\
            fileName=request['fileName'],\
            );
        return HttpResponse("OK")
    
    def CustomerMission_delete(self, request):
        models.t_customer_mission.objects.filter(user=request['user']).delete()
        return HttpResponse("OK")
    
    #使用UserId，修改其他信息
    def CustomerMission_modify_by_user(self, request):
        models.t_customer_mission.objects.filter(user=request['user']).update(\
            timeStampSubmit=request['timeStampSubmit'],\
            pageNbr=request['pageNbr'],\
            filePath=request['filePath'],\
            fileName=request['fileName'],\
            );
        return HttpResponse("OK")  # 返回字符串
    
    def CustomerMission_inqury(self, request):
        return models.t_customer_mission.objects.get(user=request['user'])
    
    #输入参数必须是完整的数据集合，并以Json为单位
    def ClassifyExecLog_add(self, request):
        models.t_cebs_classify_exec_log.objects.create(\
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
        
    def ClassifyExecLog_delete(self, request):
        models.t_cebs_classify_exec_log.objects.filter(user=request['user']).delete()
        return HttpResponse("OK")
    
    #使用UserId，修改其他信息
    def ClassifyExecLog_modify_by_user(self, request):
        models.t_cebs_classify_exec_log.objects.filter(user=request['user']).update(\
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
    
    def ClassifyExecLog_inqury(self, request):
        return models.t_cebs_classify_exec_log.objects.get(user=request['user']);

    def dft_dbi_env_add(self, inputData):
        #models.t_cebs_env.objects.create(workdir = inputData['tupLable'])
        models.t_cebs_env.objects.create(\
            workdir = inputData['tupLable']['workdir'],\
            pic_origin = inputData['tupLable']['pic_origin'],\
            pic_middle = inputData['tupLable']['pic_middle'],\
            )
        return HttpResponse("OK")

    def dft_dbi_env_read(self, inputData):
        #print(inputData['tupLable']['workdir'])
#         res = models.t_cebs_env.objects.all().values(inputData['tupLable']['workdir']) 
#         res2 = models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_origin']) 
#         res3 = models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_middle']) 
#         print("res=%d,res2%d,res3%d"%(res,res2,res3))
        models.t_cebs_env.objects.all().values(inputData['tupLable']['workdir'])
        models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_origin'])
        #print(res)
        #print(res2)
        return HttpResponse("OK")   
        

    def dft_dbi_env_modify(self, inputData):
        #print(inputData['tupLable']['workdir'])
        models.t_cebs_env.objects.filter().update(workdir=inputData['tupLable']['workdir'])
        return HttpResponse("OK") 

    def dft_dbi_env_delete(self, inputData):
        #print(inputData['tupLable']['workdir'])
        models.t_cebs_env.objects.filter(workdir = inputData['tupLable']['workdir']).delete()
        return HttpResponse("OK")

    def dft_dbi_counter_add(self, inputData):
        return True

    def dft_dbi_counter_read(self, inputData):
        return True

    def dft_dbi_counter_modify(self, inputData):
        return True

    def dft_dbi_counter_delete(self, inputData):
        return True

    def dft_dbi_fspc_add(self, inputData):
        return True

    def dft_dbi_fspc_read(self, inputData):
        return True

    def dft_dbi_fspc_modify(self, inputData):
        return True

    def dft_dbi_fspc_delete(self, inputData):
        return True

    def dft_dbi_file_add(self, inputData):
        return True

    def dft_dbi_file_read(self, inputData):
        return True

    def dft_dbi_file_modify(self, inputData):
        return True

    def dft_dbi_file_delete(self, inputData):
        return True














