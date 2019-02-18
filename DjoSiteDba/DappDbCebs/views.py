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
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        print(bufferdata['workdir'])
        if "tupLable" in bufferdata.keys():
            tup_lable = bufferdata['tupLable']
        else:
            tup_lable = 0
        if "workdir" in bufferdata.keys():
            workdir_val = bufferdata['workdir']
        else:
            workdir_val = ''
        if "pic_origin" in bufferdata.keys():
            pic_origin_val = bufferdata['pic_origin']
        else:
            pic_origin_val = ''
        if "pic_middle" in bufferdata.keys():
            pic_middle_val = bufferdata['pic_middle']
        else:
            pic_middle_val = ''
        if "holeboard_type" in bufferdata.keys():
            holeboard_type_val = bufferdata['holeboard_type']
        else:
            holeboard_type_val = ''
        if "holeboard_left_bot_x" in bufferdata.keys():
            holeboard_left_bot_x_val = bufferdata['holeboard_left_bot_x']
        else:
            holeboard_left_bot_x_val = 0
        if "holeboard_left_bot_y" in bufferdata.keys():
            holeboard_left_bot_y_val = bufferdata['holeboard_left_bot_y']
        else:
            holeboard_left_bot_y_val = 0
        if "holeboard_right_up_x" in bufferdata.keys():
            holeboard_right_up_x_val = bufferdata['holeboard_right_up_x']
        else:
            holeboard_right_up_x_val = 0        
        if "holeboard_right_up_y" in bufferdata.keys():
            holeboard_right_up_y_val = bufferdata['holeboard_right_up_y']
        else:
            holeboard_right_up_y_val = 0
        if "pic_take_fix_point_set" in bufferdata.keys():
            pic_take_fix_point_set_val = bufferdata['pic_take_fix_point_set']
        else:
            pic_take_fix_point_set_val = False
        if "pic_classification_set" in bufferdata.keys():
            pic_classification_set_val = bufferdata['pic_classification_set']
        else:
            pic_classification_set_val = False
        if "pic_auto_work_after_start_set" in bufferdata.keys():
            pic_auto_work_after_start_set_val = bufferdata['pic_auto_work_after_start_set']
        else:
            pic_auto_work_after_start_set_val = False
        if "pic_auto_work_tti" in bufferdata.keys():
            pic_auto_work_tti_val = bufferdata['pic_auto_work_tti']
        else:
            pic_auto_work_tti_val = 0
        if "vis_small_low_limit" in bufferdata.keys():
            vis_small_low_limit_val = bufferdata['vis_small_low_limit']
        else:
            vis_small_low_limit_val = 0
        if "vis_small_mid_limit" in bufferdata.keys():
            vis_small_mid_limit_val = bufferdata['vis_small_mid_limit']
        else:
            vis_small_mid_limit_val = 0
        if "vis_mid_big_limit" in bufferdata.keys():
            vis_mid_big_limit_val = bufferdata['vis_mid_big_limit']
        else:
            vis_mid_big_limit_val = 0
        if "vis_big_upper_limit" in bufferdata.keys():
            vis_big_upper_limit_val = bufferdata['vis_big_upper_limit']
        else:
            vis_big_upper_limit_val = 0
        if "vis_res_addup_set" in bufferdata.keys():
            vis_res_addup_set_val = bufferdata['vis_res_addup_set']
        else:
            vis_res_addup_set_val = False
        if "vis_cap_enable_set" in bufferdata.keys():
            vis_cap_enable_set_val = bufferdata['vis_cap_enable_set']
        else:
            vis_cap_enable_set_val = False
        if "vis_cap_dur_in_sec" in bufferdata.keys():
            vis_cap_dur_in_sec_val = bufferdata['vis_cap_dur_in_sec']
        else:
            vis_cap_dur_in_sec_val = 3
        if "vis_clfy_gen_par1" in bufferdata.keys():
            vis_clfy_gen_par1_val = bufferdata['vis_clfy_gen_par1']
        else:
            vis_clfy_gen_par1_val = 0 
        if "vis_clfy_gen_par2" in bufferdata.keys():
            vis_clfy_gen_par2_val = bufferdata['vis_clfy_gen_par2']
        else:
            vis_clfy_gen_par2_val = 0
        if "vis_clfy_gen_par3" in bufferdata.keys():
            vis_clfy_gen_par3_val = bufferdata['vis_clfy_gen_par3']
        else:
            vis_clfy_gen_par3_val = 0
        if "vis_clfy_gen_par4" in bufferdata.keys():
            vis_clfy_gen_par4_val = bufferdata['vis_clfy_gen_par4']
        else:
            vis_clfy_gen_par4_val = 0 
        models.t_cebs_env.objects.create(\
            tup_lable = tup_lable,                           
            workdir = workdir_val,pic_origin = pic_origin_val,pic_middle = pic_middle_val,holeboard_type = holeboard_type_val,\
            holeboard_left_bot_x = holeboard_left_bot_x_val,holeboard_left_bot_y = holeboard_left_bot_y_val,holeboard_right_up_x = holeboard_right_up_x_val,\
            holeboard_right_up_y = holeboard_right_up_y_val,pic_take_fix_point_set = pic_take_fix_point_set_val,pic_classification_set = pic_classification_set_val,\
            pic_auto_work_after_start_set = pic_auto_work_after_start_set_val,pic_auto_work_tti = pic_auto_work_tti_val,vis_small_low_limit = vis_small_low_limit_val,\
            vis_small_mid_limit = vis_small_mid_limit_val,vis_mid_big_limit = vis_mid_big_limit_val,vis_big_upper_limit = vis_big_upper_limit_val,vis_res_addup_set = vis_res_addup_set_val,\
            vis_cap_enable_set = vis_cap_enable_set_val,vis_cap_dur_in_sec = vis_cap_dur_in_sec_val,vis_clfy_gen_par1 = vis_clfy_gen_par1_val,vis_clfy_gen_par2 = vis_clfy_gen_par2_val,\
            vis_clfy_gen_par3 = vis_clfy_gen_par3_val,vis_clfy_gen_par4 = vis_clfy_gen_par4_val,\
            )
        return True
    #read 操作不太好复用
    def dft_dbi_env_read(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'])
        bufferout= {}
        if "workdir" in bufferdata.keys():
            bufferout['workdir'] = res[0].workdir;
        else:
            pass
        if "pic_origin" in bufferdata.keys():
            bufferout['pic_origin'] = res[0].pic_origin;
        else:
            pass
        if "pic_middle" in bufferdata.keys():
            bufferout['pic_middle'] = res[0].pic_middle;
        else:
            pass
        if "holeboard_type" in bufferdata.keys():
            bufferout['holeboard_type'] = res[0].holeboard_type;
        else:
            pass
        if "holeboard_left_bot_x" in bufferdata.keys():
            bufferout['holeboard_left_bot_x'] = res[0].holeboard_left_bot_x;
        else:
            pass
        if "holeboard_left_bot_y" in bufferdata.keys():
            bufferout['holeboard_left_bot_y'] = res[0].holeboard_left_bot_y;
        else:
            pass
        if "holeboard_right_up_x" in bufferdata.keys():
            bufferout['holeboard_right_up_x'] = res[0].holeboard_right_up_x;
        else:
            pass
        if "holeboard_right_up_y" in bufferdata.keys():
            bufferout['holeboard_right_up_y'] = res[0].holeboard_right_up_y;
        else:
            pass
        if "pic_take_fix_point_set" in bufferdata.keys():
            bufferout['pic_take_fix_point_set'] = res[0].pic_take_fix_point_set;
        else:
            pass
        if "pic_classification_set" in bufferdata.keys():
            bufferout['pic_classification_set'] = res[0].pic_classification_set;
        else:
            pass
        if "pic_auto_work_after_start_set" in bufferdata.keys():
            bufferout['pic_auto_work_after_start_set'] = res[0].pic_auto_work_after_start_set;
        else:
            pass
        if "pic_auto_work_tti" in bufferdata.keys():
            bufferout['pic_auto_work_tti'] = res[0].pic_auto_work_tti;
        else:
            pass
        if "vis_small_low_limit" in bufferdata.keys():
            bufferout['vis_small_low_limit'] = res[0].vis_small_low_limit;
        else:
            pass
        if "vis_small_mid_limit" in bufferdata.keys():
            bufferout['vis_small_mid_limit'] = res[0].vis_small_mid_limit;
        else:
            pass
        if "vis_mid_big_limit" in bufferdata.keys():
            bufferout['vis_mid_big_limit'] = res[0].vis_mid_big_limit;
        else:
            pass
        if "vis_big_upper_limit" in bufferdata.keys():
            bufferout['vis_big_upper_limit'] = res[0].vis_big_upper_limit;
        else:
            pass
        if "vis_res_addup_set" in bufferdata.keys():
            bufferout['vis_res_addup_set'] = res[0].vis_res_addup_set;
        else:
            pass
        if "vis_cap_enable_set" in bufferdata.keys():
            bufferout['vis_cap_enable_set'] = res[0].vis_cap_enable_set;
        else:
            pass
        if "vis_cap_dur_in_sec" in bufferdata.keys():
            bufferout['vis_cap_dur_in_sec'] = res[0].vis_cap_dur_in_sec;
        else:
            pass
        if "vis_clfy_gen_par1" in bufferdata.keys():
            bufferout['vis_clfy_gen_par1'] = res[0].vis_clfy_gen_par1;
        else:
            pass
        if "vis_clfy_gen_par2" in bufferdata.keys():
            bufferout['vis_clfy_gen_par2'] = res[0].vis_clfy_gen_par2;
        else:
            pass
        if "vis_clfy_gen_par3" in bufferdata.keys():
            bufferout['vis_clfy_gen_par3'] = res[0].vis_clfy_gen_par3;
        else:
            pass
        if "vis_clfy_gen_par4" in bufferdata.keys():
            bufferout['vis_clfy_gen_par4'] = res[0].vis_clfy_gen_par4;
        else:
            pass
        print(bufferout)
        return True
        #if "tup_lable" in bufferdata.keys():
        #要知道才能查      
#         res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'])
#         print(res)
#         for line in res:
#             print(line.tup_lable)
#             print(line.workdir)  
#             print(line.pic_origin)
#             print(line.pic_middle)
#             print(line.holeboard_type)
#             print(line.holeboard_left_bot_x)
#             print(line.holeboard_left_bot_y)
#             print(line.holeboard_right_up_x)
#             print(line.holeboard_right_up_y)
#             print(line.pic_take_fix_point_set)
#             print(line.pic_classification_set)
#             print(line.pic_auto_work_after_start_set)
#             print(line.pic_auto_work_tti)
#             print(line.vis_small_low_limit)
#             print(line.vis_small_mid_limit)
#             print(line.vis_mid_big_limit)
#             print(line.vis_big_upper_limit)
#             print(line.vis_res_addup_set)
#             print(line.vis_cap_enable_set)
#             print(line.vis_cap_dur_in_sec)
#             print(line.vis_clfy_gen_par1)
#             print(line.vis_clfy_gen_par2)
#             print(line.vis_clfy_gen_par3)
#             print(line.vis_clfy_gen_par4)
#         for line in res:
#             print(line.workdir)
#             
#         if "tupLable" in bufferdata.keys():
            
        #print(inputData['tupLable']['workdir'])
#         res = models.t_cebs_env.objects.all().values(inputData['tupLable']['workdir']) 
#         res2 = models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_origin']) 
#         res3 = models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_middle']) 
#         print("res=%d,res2%d,res3%d"%(res,res2,res3))

#         models.t_cebs_env.objects.all().values(inputData['tupLable']['workdir'])
#         models.t_cebs_env.objects.all().values(inputData['tupLable']['pic_origin'])
        #print(res)
        #print(res2)
        
        

    def dft_dbi_env_modify(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata) 
        
        res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'])
        for line in res:
            res.tup_lable = line.tup_lable
            res.workdir = line.workdir  
            res.pic_origin = line.pic_origin
            res.pic_middle = line.pic_middle
            res.holeboard_type = line.holeboard_type
            res.holeboard_left_bot_x = line.holeboard_left_bot_x
            res.holeboard_left_bot_y = line.holeboard_left_bot_y
            res.holeboard_right_up_x = line.holeboard_right_up_x
            res.holeboard_right_up_y = line.holeboard_right_up_y
            res.pic_take_fix_point_set = line.pic_take_fix_point_set
            res.pic_classification_set = line.pic_classification_set
            res.pic_auto_work_after_start_set = line.pic_auto_work_after_start_set
            res.pic_auto_work_tti = line.pic_auto_work_tti
            res.vis_small_low_limit = line.vis_small_low_limit
            res.vis_small_mid_limit = line.vis_small_mid_limit
            res.vis_mid_big_limit = line.vis_mid_big_limit
            res.vis_big_upper_limit = line.vis_big_upper_limit
            res.vis_res_addup_set = line.vis_res_addup_set
            res.vis_cap_enable_set = line.vis_cap_enable_set
            res.vis_cap_dur_in_sec = line.vis_cap_dur_in_sec
            res.vis_clfy_gen_par1 = line.vis_clfy_gen_par1
            res.vis_clfy_gen_par2 = line.vis_clfy_gen_par2
            res.vis_clfy_gen_par3 = line.vis_clfy_gen_par3
            res.vis_clfy_gen_par4 = line.vis_clfy_gen_par4
            
#         print(res.tup_lable)
#         print(bufferdata['tupLable'])   
        if "tupLable" in bufferdata.keys():
            if (res.tup_lable == bufferdata['tupLable']):
                tup_lable_val = res.tup_lable
            else:
                tup_lable_val = bufferdata['tupLable'] 
        else:
            tup_lable_val = res.tup_lable
        if "workdir" in bufferdata.keys():
            if (res.workdir == bufferdata['workdir']):
                workdir_val = res.workdir
            else:
                workdir_val = bufferdata['workdir']
        else:
            
            workdir_val = res.workdir
            print(res.workdir)
            print(workdir_val)
        if "pic_origin" in bufferdata.keys():
            if (res.pic_origin == bufferdata['pic_origin']):
                pic_origin_val = res.pic_origin
            else:
                pic_origin_val = bufferdata['pic_origin']
        else:
            pic_origin_val = res.pic_origin
        if "pic_middle" in bufferdata.keys():
            if (res.pic_middle == bufferdata['pic_middle']):
                pic_middle_val = res.pic_middle
            else:
                pic_middle_val = bufferdata['pic_middle']
        else:
            pic_middle_val = res.pic_middle
        if "holeboard_type" in bufferdata.keys():
            if (res.holeboard_type == bufferdata['holeboard_type']):
                holeboard_type_val = res.holeboard_type
            else:
                holeboard_type_val = bufferdata['holeboard_type']
        else:
            holeboard_type_val = res.holeboard_type
        if "holeboard_left_bot_x" in bufferdata.keys():
            if (res.holeboard_left_bot_x == bufferdata['holeboard_left_bot_x']):
                holeboard_left_bot_x_val = res.holeboard_left_bot_x
            else:
                holeboard_left_bot_x_val = bufferdata['holeboard_left_bot_x']
        else:
            holeboard_left_bot_x_val = res.holeboard_left_bot_x 
        if "holeboard_left_bot_y" in bufferdata.keys():
            if (res.holeboard_left_bot_y == bufferdata['holeboard_left_bot_y']):
                holeboard_left_bot_y_val = res.holeboard_left_bot_y
            else:
                holeboard_left_bot_y_val = bufferdata['holeboard_left_bot_y']
        else:
            holeboard_left_bot_y_val = res.holeboard_left_bot_y
        if "holeboard_right_up_x" in bufferdata.keys():
            if (res.holeboard_right_up_x == bufferdata['holeboard_right_up_x']):
                holeboard_right_up_x_val = res.holeboard_right_up_x
            else:
                holeboard_right_up_x_val = bufferdata['holeboard_right_up_x']        
        else:
            holeboard_right_up_x_val = res.holeboard_right_up_x
        if "holeboard_right_up_y" in bufferdata.keys():
            if (res.holeboard_right_up_y == bufferdata['holeboard_right_up_y']):
                holeboard_right_up_y_val = res.holeboard_right_up_y
            else:
                holeboard_right_up_y_val = bufferdata['holeboard_right_up_y']
        else:
            holeboard_right_up_y_val = res.holeboard_right_up_y
        if "pic_take_fix_point_set" in bufferdata.keys():
            if (res.pic_take_fix_point_set == bufferdata['pic_take_fix_point_set']):
                pic_take_fix_point_set_val = res.pic_take_fix_point_set
            else:
                pic_take_fix_point_set_val = bufferdata['pic_take_fix_point_set']
        else:
            pic_take_fix_point_set_val = res.pic_take_fix_point_set
        if "pic_classification_set" in bufferdata.keys():
            if (res.pic_classification_set == bufferdata['pic_classification_set']):
                pic_classification_set_val = res.pic_classification_set
            else:
                pic_classification_set_val = bufferdata['pic_classification_set']
        else:
            pic_classification_set_val = res.pic_classification_set
        if "pic_auto_work_after_start_set" in bufferdata.keys():
            if (res.pic_auto_work_after_start_set == bufferdata['pic_auto_work_after_start_set']):
                pic_auto_work_after_start_set_val = res.pic_auto_work_after_start_set
            else:
                pic_auto_work_after_start_set_val = bufferdata['pic_auto_work_after_start_set']
        else:
            pic_auto_work_after_start_set_val = res.pic_auto_work_after_start_set
        if "pic_auto_work_tti" in bufferdata.keys():
            if (res.pic_auto_work_tti == bufferdata['pic_auto_work_tti']):
                pic_auto_work_tti_val = res.pic_auto_work_tti
            else:
                pic_auto_work_tti_val = bufferdata['pic_auto_work_tti']
        else:
            pic_auto_work_tti_val = res.pic_auto_work_tti
        if "vis_small_low_limit" in bufferdata.keys():
            if (res.vis_small_low_limit == bufferdata['vis_small_low_limit']):
                vis_small_low_limit_val = res.vis_small_low_limit
            else:
                vis_small_low_limit_val = bufferdata['vis_small_low_limit']
        else:
            vis_small_low_limit_val = res.vis_small_low_limit
        if "vis_small_mid_limit" in bufferdata.keys():
            if (res.vis_small_mid_limit == bufferdata['vis_small_mid_limit']):
                vis_small_mid_limit_val = res.vis_small_mid_limit
            else:
                vis_small_mid_limit_val = bufferdata['vis_small_mid_limit']
        else:
            vis_small_mid_limit_val = res.vis_small_mid_limit
        if "vis_mid_big_limit" in bufferdata.keys():
            if (res.vis_mid_big_limit == bufferdata['vis_mid_big_limit']):
                vis_mid_big_limit_val = res.vis_mid_big_limit
            else:
                vis_mid_big_limit_val = bufferdata['vis_mid_big_limit']
        else:
            vis_mid_big_limit_val = res.vis_mid_big_limit
        if "vis_big_upper_limit" in bufferdata.keys():
            if (res.vis_big_upper_limit == bufferdata['vis_big_upper_limit']):
                vis_big_upper_limit_val = res.vis_big_upper_limit
            else:
                vis_big_upper_limit_val = bufferdata['vis_big_upper_limit']
        else:
            vis_big_upper_limit_val = res.vis_big_upper_limit
        if "vis_res_addup_set" in bufferdata.keys():
            if (res.vis_res_addup_set == bufferdata['vis_res_addup_set']):
                vis_res_addup_set_val = res.vis_res_addup_set
            else:
                vis_res_addup_set_val = bufferdata['vis_res_addup_set']
        else:
            vis_res_addup_set_val = res.vis_res_addup_set
        if "vis_cap_enable_set" in bufferdata.keys():
            if (res.vis_cap_enable_set == bufferdata['vis_cap_enable_set']):
                vis_cap_enable_set_val = res.vis_cap_enable_set
            else:
                vis_cap_enable_set_val = bufferdata['vis_cap_enable_set']
        else:
            vis_cap_enable_set_val = res.vis_cap_enable_set
        if "vis_cap_dur_in_sec" in bufferdata.keys():
            if (res.vis_cap_dur_in_sec == bufferdata['vis_cap_dur_in_sec']):
                vis_cap_dur_in_sec_val = res.vis_cap_dur_in_sec
            else:
                vis_cap_dur_in_sec_val = bufferdata['vis_cap_dur_in_sec']
        else:
            vis_cap_dur_in_sec_val = res.vis_cap_dur_in_sec
        if "vis_clfy_gen_par1" in bufferdata.keys():
            if (res.vis_clfy_gen_par1 == bufferdata['vis_clfy_gen_par1']):
                vis_clfy_gen_par1_val = res.vis_clfy_gen_par1
            else:
                vis_clfy_gen_par1_val = bufferdata['vis_clfy_gen_par1'] 
        else:
            vis_clfy_gen_par1_val = res.vis_clfy_gen_par1
        if "vis_clfy_gen_par2" in bufferdata.keys():
            if (res.vis_clfy_gen_par2 == bufferdata['vis_clfy_gen_par2']):
                vis_clfy_gen_par2_val = res.vis_clfy_gen_par2
            else:
                vis_clfy_gen_par2_val = bufferdata['vis_clfy_gen_par2']
        else:
            vis_clfy_gen_par2_val = res.vis_clfy_gen_par2
        if "vis_clfy_gen_par3" in bufferdata.keys():
            if (res.vis_clfy_gen_par3 == bufferdata['vis_clfy_gen_par3']):
                vis_clfy_gen_par3_val = res.vis_clfy_gen_par3
            else:
                vis_clfy_gen_par3_val = bufferdata['vis_clfy_gen_par3']
        else:
            vis_clfy_gen_par3_val = res.vis_clfy_gen_par3
        if "vis_clfy_gen_par4" in bufferdata.keys():
            if (res.vis_clfy_gen_par4 == bufferdata['vis_clfy_gen_par4']):
                vis_clfy_gen_par4_val = res.vis_clfy_gen_par4
            else:
                vis_clfy_gen_par4_val = bufferdata['vis_clfy_gen_par4']
        else:
            vis_clfy_gen_par4_val = res. vis_clfy_gen_par4   
        models.t_cebs_env.objects.filter(tup_lable = tup_lable_val).update(                       
            workdir = workdir_val,pic_origin = pic_origin_val,pic_middle = pic_middle_val,holeboard_type = holeboard_type_val,\
            holeboard_left_bot_x = holeboard_left_bot_x_val,holeboard_left_bot_y = holeboard_left_bot_y_val,holeboard_right_up_x = holeboard_right_up_x_val,\
            holeboard_right_up_y = holeboard_right_up_y_val,pic_take_fix_point_set = pic_take_fix_point_set_val,pic_classification_set = pic_classification_set_val,\
            pic_auto_work_after_start_set = pic_auto_work_after_start_set_val,pic_auto_work_tti = pic_auto_work_tti_val,vis_small_low_limit = vis_small_low_limit_val,\
            vis_small_mid_limit = vis_small_mid_limit_val,vis_mid_big_limit = vis_mid_big_limit_val,vis_big_upper_limit = vis_big_upper_limit_val,vis_res_addup_set = vis_res_addup_set_val,\
            vis_cap_enable_set = vis_cap_enable_set_val,vis_cap_dur_in_sec = vis_cap_dur_in_sec_val,vis_clfy_gen_par1 = vis_clfy_gen_par1_val,vis_clfy_gen_par2 = vis_clfy_gen_par2_val,\
            vis_clfy_gen_par3 = vis_clfy_gen_par3_val,vis_clfy_gen_par4 = vis_clfy_gen_par4_val)         
        return True 

    def dft_dbi_env_delete(self, inputData):
        #print(inputData['tupLable']['workdir'])\
        bufferdata = inputData['tupLable']
        print(bufferdata)
        models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable']).delete()
        return True

    def dft_dbi_counter_add(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        print(bufferdata['picbatchcnt'])
        if "tupLable" in bufferdata.keys():
            tup_lable = bufferdata['tupLable']
        else:
            tup_lable = 0
        if "picbatchcnt" in bufferdata.keys():
            picbatchcnt_val = bufferdata['picbatchcnt']
        else:
            picbatchcnt_val = 0
        if "picbatchclas" in bufferdata.keys():
            picbatchclas_val = bufferdata['picbatchclas']
        else:
            picbatchclas_val = 0
        if "picremaincnt" in bufferdata.keys():
            picremaincnt_val = bufferdata['picremaincnt']
        else:
            picremaincnt_val = 0
        if "picbatfluclas" in bufferdata.keys():
            picbatfluclas_val = bufferdata['picbatfluclas']
        else:
            picbatfluclas_val = 0
        if "picremflucnt" in bufferdata.keys():
            picremflucnt_val = bufferdata['picremflucnt']
        else:
            picremflucnt_val = 0
        
        models.t_cebs_counter.objects.create(\
            tup_lable=tup_lable,
            picbatchcnt = picbatchcnt_val,picbatchclas = picbatchclas_val,\
            picremaincnt = picremaincnt_val,picbatfluclas = picbatfluclas_val,\
            picremflucnt = picremflucnt_val
            )
        return True

    def dft_dbi_counter_read(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        res = models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable'])
        bufferout= {}
        if "picbatchcnt" in bufferdata.keys():
            bufferout['picbatchcnt'] = res[0].picbatchcnt;
        else:
            pass
        if "picbatchclas" in bufferdata.keys():
            bufferout['picbatchclas'] = res[0].picbatchclas;
        else:
            pass
        if "picremaincnt" in bufferdata.keys():
            bufferout['picremaincnt'] = res[0].picremaincnt;
        else:
            pass
        if "picbatfluclas" in bufferdata.keys():
            bufferout['picbatfluclas'] = res[0].picbatfluclas;
        else:
            pass
        if "picremflucnt" in bufferdata.keys():
            bufferout['picremflucnt'] = res[0].picremflucnt;
        else:
            pass
        
        print(bufferout)
        return True

    def dft_dbi_counter_modify(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata) 
        
        res = models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable']) 
        for line in res:
            res.tup_lable = line.tup_lable
            res.picbatchcnt = line.picbatchcnt  
            res.picbatchclas = line.picbatchclas
            res.picremaincnt = line.picremaincnt
            res.picbatfluclas = line.picbatfluclas
            res.picremflucnt = line.picremflucnt
        
               
        if "tupLable" in bufferdata.keys():
            if (res.tup_lable == bufferdata['tupLable']):
                tup_lable_val = res.tup_lable
            else:
                tup_lable_val = bufferdata['tupLable'] 
        else:
            tup_lable_val = res.tup_lable
        if "picbatchcnt" in bufferdata.keys():
            if (res.picbatchcnt == bufferdata['picbatchcnt']):
                picbatchcnt_val = res.picbatchcnt
            else:
                picbatchcnt_val = bufferdata['picbatchcnt']
        else:
            picbatchcnt_val = res.picbatchcnt
        if "picbatchclas" in bufferdata.keys():
            if (res.picbatchclas == bufferdata['picbatchclas']):
                picbatchclas_val = res.picbatchclas
            else:
                picbatchclas_val = bufferdata['picbatchclas']
        else:
            picbatchclas_val = res.picbatchclas
        if "picremaincnt" in bufferdata.keys():
            if (res.picremaincnt == bufferdata['picremaincnt']):
                picremaincnt_val = res.picremaincnt
            else:
                picremaincnt_val = bufferdata['picremaincnt']
        else:
            picremaincnt_val = res.picremaincnt
        if "picbatfluclas" in bufferdata.keys():
            if (res.picbatfluclas == bufferdata['picbatfluclas']):
                picbatfluclas_val = res.picbatfluclas
            else:
                picbatfluclas_val = bufferdata['picbatfluclas']
        else:
            picbatfluclas_val = res.picbatfluclas
        if "picremflucnt" in bufferdata.keys():
            if (res.picremflucnt == bufferdata['picremflucnt']):
                picremflucnt_val = res.picremflucnt
            else:
                picremflucnt_val = bufferdata['picremflucnt']
        else:
            picremflucnt_val = res.picremflucnt 
       
        models.t_cebs_counter.objects.filter(tup_lable = tup_lable_val).update(\
            tup_lable=tup_lable_val,
            picbatchcnt = picbatchcnt_val,picbatchclas = picbatchclas_val,\
            picremaincnt = picremaincnt_val,picbatfluclas = picbatfluclas_val,\
            picremflucnt = picremflucnt_val
            )
        return True 

    def dft_dbi_counter_delete(self, inputData):
        bufferdata = inputData['tupLable']
        print(bufferdata)
        models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable']).delete()
        return True

    def dft_dbi_fspc_add(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        if "tupLable" in bufferdata.keys():
            tup_lable = bufferdata['tupLable']
        else:
            tup_lable = 0
        if "mark_line" in bufferdata.keys():
            mark_line_val = bufferdata['mark_line']
        else:
            mark_line_val = 0
        if "mark_width" in bufferdata.keys():
            mark_width_val = bufferdata['mark_width']
        else:
            mark_width_val = 0
        if "mark_area" in bufferdata.keys():
            mark_area_val = bufferdata['mark_area']
        else:
            mark_area_val = 0
        if "mark_dilate" in bufferdata.keys():
            mark_dilate_val = bufferdata['mark_dilate']
        else:
            mark_dilate_val = 0
        if "area_square_min" in bufferdata.keys():
            area_square_min_val = bufferdata['area_square_min']
        else:
            area_square_min_val = 0
        if "area_squre_max" in bufferdata.keys():
            area_squre_max_val = bufferdata['area_squre_max']
        else:
            area_squre_max_val = 0
        if "area_dilate" in bufferdata.keys():
            area_dilate_val = bufferdata['area_dilate']
        else:
            area_dilate_val = 0        
        if "area_erode" in bufferdata.keys():
            area_erode_val = bufferdata['area_erode']
        else:
            area_erode_val = 0
        if "cell_square_min" in bufferdata.keys():
            cell_square_min_val = bufferdata['cell_square_min']
        else:
            cell_square_min_val = 0
        if "cell_square_max" in bufferdata.keys():
            cell_square_max_val = bufferdata['cell_square_max']
        else:
            cell_square_max_val = 0
        if "cell_raduis_min" in bufferdata.keys():
            cell_raduis_min_val = bufferdata['cell_raduis_min']
        else:
            cell_raduis_min_val = 0
        if "cell_raduis_max" in bufferdata.keys():
            cell_raduis_max_val = bufferdata['cell_raduis_max']
        else:
            cell_raduis_max_val = 0
        if "cell_dilate" in bufferdata.keys():
            cell_dilate_val = bufferdata['cell_dilate']
        else:
            cell_dilate_val = 0
        if "cell_erode" in bufferdata.keys():
            cell_erode_val = bufferdata['cell_erode']
        else:
            cell_erode_val = 0
        if "cell_ce" in bufferdata.keys():
            cell_ce_val = bufferdata['cell_ce']
        else:
            cell_ce_val = 0
        if "cell_distance" in bufferdata.keys():
            cell_distance_val = bufferdata['cell_distance']
        else:
            cell_distance_val = 0
        if "pic_train_delay" in bufferdata.keys():
            pic_train_delay_val = bufferdata['pic_train_delay']
        else:
            pic_train_delay_val = 0
        if "addup_set" in bufferdata.keys():
            addup_set_val = bufferdata['addup_set']
        else:
            addup_set_val = False
        
        models.t_cebs_fspc.objects.create(\
            tup_lable = tup_lable,
            mark_line = mark_line_val,mark_width = mark_width_val,mark_area = mark_area_val,mark_dilate = mark_dilate_val,\
            area_square_min = area_square_min_val,area_squre_max = area_squre_max_val,area_dilate = area_dilate_val,area_erode = area_erode_val,\
            cell_square_min = cell_square_min_val,cell_square_max = cell_square_max_val,cell_raduis_min = cell_raduis_min_val,cell_raduis_max = cell_raduis_max_val,\
            cell_dilate = cell_dilate_val,cell_erode = cell_erode_val,cell_ce = cell_ce_val,cell_distance = cell_distance_val,pic_train_delay = pic_train_delay_val,addup_set = addup_set_val)
        return True

    def dft_dbi_fspc_read(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        res = models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable'])
        bufferout= {}
        if "mark_line" in bufferdata.keys():
            bufferout['mark_line'] = res[0].mark_line;
        else:
            pass
        if "mark_width" in bufferdata.keys():
            bufferout['mark_width'] = res[0].mark_width;
        else:
            pass
        if "mark_area" in bufferdata.keys():
            bufferout['mark_area'] = res[0].mark_area;
        else:
            pass
        if "mark_dilate" in bufferdata.keys():
            bufferout['mark_dilate'] = res[0].mark_dilate;
        else:
            pass
        if "area_square_min" in bufferdata.keys():
            bufferout['area_square_min'] = res[0].area_square_min;
        else:
            pass
        if "area_squre_max" in bufferdata.keys():
            bufferout['area_squre_max'] = res[0].area_squre_max;
        else:
            pass
        if "area_dilate" in bufferdata.keys():
            bufferout['area_dilate'] = res[0].area_dilate;
        else:
            pass
        if "area_erode" in bufferdata.keys():
            bufferout['area_erode'] = res[0].area_erode;
        else:
            pass
        if "cell_square_min" in bufferdata.keys():
            bufferout['cell_square_min'] = res[0].cell_square_min;
        else:
            pass
        if "cell_square_max" in bufferdata.keys():
            bufferout['cell_square_max'] = res[0].cell_square_max;
        else:
            pass
        if "cell_raduis_min" in bufferdata.keys():
            bufferout['cell_raduis_min'] = res[0].cell_raduis_min;
        else:
            pass
        if "cell_raduis_max" in bufferdata.keys():
            bufferout['cell_raduis_max'] = res[0].cell_raduis_max;
        else:
            pass
        if "cell_dilate" in bufferdata.keys():
            bufferout['cell_dilate'] = res[0].cell_dilate;
        else:
            pass
        if "cell_erode" in bufferdata.keys():
            bufferout['cell_erode'] = res[0].cell_erode;
        else:
            pass
        if "cell_ce" in bufferdata.keys():
            bufferout['cell_ce'] = res[0].cell_ce;
        else:
            pass
        if "cell_distance" in bufferdata.keys():
            bufferout['cell_distance'] = res[0].cell_distance;
        else:
            pass
        if "pic_train_delay" in bufferdata.keys():
            bufferout['pic_train_delay'] = res[0].pic_train_delay;
        else:
            pass
        if "addup_set" in bufferdata.keys():
            bufferout['addup_set'] = res[0].addup_set;
        else:
            pass
        
        print(bufferout)
        return True

    def dft_dbi_fspc_modify(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata) 
        
        res = models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable'])
        for line in res:
            res.tup_lable = line.tup_lable
            res.mark_line = line.mark_line  
            res.mark_width = line.mark_width
            res.mark_area = line.mark_area
            res.mark_dilate = line.mark_dilate
            res.area_square_min = line.area_square_min
            res.area_squre_max = line.area_squre_max
            res.area_dilate = line.area_dilate
            res.area_erode = line.area_erode
            res.cell_square_min = line.cell_square_min
            res.cell_square_max = line.cell_square_max
            res.cell_raduis_min = line.cell_raduis_min
            res.cell_raduis_max = line.cell_raduis_max
            res.cell_dilate = line.cell_dilate
            res.cell_erode = line.cell_erode
            res.cell_ce = line.cell_ce
            res.cell_distance = line.cell_distance
            res.pic_train_delay = line.pic_train_delay
            res.addup_set = line.addup_set
            
  
        if "tupLable" in bufferdata.keys():
            if (res.tup_lable == bufferdata['tupLable']):
                tup_lable_val = res.tup_lable
            else:
                tup_lable_val = bufferdata['tuplable'] 
        else:
            tup_lable_val = res.tup_lable
        if "mark_line" in bufferdata.keys():
            if (res.mark_line == bufferdata['mark_line']):
                mark_line_val = res.mark_line
            else:
                mark_line_val = bufferdata['mark_line']
        else:
            mark_line_val = res.mark_line
        if "mark_width" in bufferdata.keys():
            if (res.mark_width == bufferdata['mark_width']):
                mark_width_val = res.mark_width
            else:
                mark_width_val = bufferdata['mark_width']
        else:
            mark_width_val = res.mark_width
        if "mark_area" in bufferdata.keys():
            if (res.mark_area == bufferdata['mark_area']):
                mark_area_val = res.mark_area
            else:
                mark_area_val = bufferdata['mark_area']
        else:
            mark_area_val = res.mark_area
        if "mark_dilate" in bufferdata.keys():
            if (res.mark_dilate == bufferdata['mark_dilate']):
                mark_dilate_Val = res.mark_dilate
            else:
                mark_dilate_val = bufferdata['mark_dilate']
        else:
            mark_dilate_val = res.mark_dilate
        if "area_square_min" in bufferdata.keys():
            if (res.area_square_min == bufferdata['area_square_min']):
                area_square_min_val = res.area_square_min
            else:
                area_square_min_val = bufferdata['area_square_min']
        else:
            area_square_min_val = res.area_square_min 
        if "area_squre_max" in bufferdata.keys():
            if (res.area_squre_max == bufferdata['area_squre_max']):
                area_squre_max_val = res.area_squre_max
            else:
                area_squre_max_val = bufferdata['area_squre_max']
        else:
            area_squre_max_val = res.area_squre_max
        if "area_dilate" in bufferdata.keys():
            if (res.area_dilate == bufferdata['area_dilate']):
                area_dilate_val = res.area_dilate
            else:
                area_dilate_val = bufferdata['area_dilate']        
        else:
            area_dilate_val = res.area_dilate
        if "area_erode" in bufferdata.keys():
            if (res.area_erode == bufferdata['area_erode']):
                area_erode_val = res.area_erode
            else:
                area_erode_val = bufferdata['area_erode']
        else:
            area_erode_val = res.area_erode
        if "cell_square_min" in bufferdata.keys():
            if (res.cell_square_min == bufferdata['cell_square_min']):
                cell_square_min_val = res.cell_square_min
            else:
                cell_square_min_val = bufferdata['cell_square_min']
        else:
            cell_square_min_val = res.cell_square_min
        if "cell_square_max" in bufferdata.keys():
            if (res.cell_square_max == bufferdata['cell_square_max']):
                cell_square_max_val = res.cell_square_max
            else:
                cell_square_max_val = bufferdata['cell_square_max']
        else:
            cell_square_max_val = res.cell_square_max
        if "cell_raduis_min" in bufferdata.keys():
            if (res.cell_raduis_min == bufferdata['cell_raduis_min']):
                cell_raduis_min_val = res.cell_raduis_min
            else:
                cell_raduis_min_val = bufferdata['cell_raduis_min']
        else:
            cell_raduis_min_val = res.cell_raduis_min
        if "cell_raduis_max" in bufferdata.keys():
            if (res.cell_raduis_max == bufferdata['cell_raduis_max']):
                cell_raduis_max_val = res.cell_raduis_max
            else:
                cell_raduis_max_val = bufferdata['cell_raduis_max']
        else:
            cell_raduis_max_val = res.cell_raduis_max
        if "cell_dilate" in bufferdata.keys():
            if (res.cell_dilate == bufferdata['cell_dilate']):
                cell_dilate_val = res.cell_dilate
            else:
                cell_dilate_val = bufferdata['cell_dilate']
        else:
            cell_dilate_val = res.cell_dilate
        if "cell_erode" in bufferdata.keys():
            if (res.cell_erode == bufferdata['cell_erode']):
                cell_erode_val = res.cell_erode
            else:
                cell_erode_val = bufferdata['cell_erode']
        else:
            cell_erode_val = res.cell_erode
        if "cell_ce" in bufferdata.keys():
            if (res.cell_ce == bufferdata['cell_ce']):
                cell_ce_val = res.cell_ce
            else:
                cell_ce_val = bufferdata['cell_ce']
        else:
            cell_ce_val = res.cell_ce
        if "cell_distance" in bufferdata.keys():
            if (res.cell_distance == bufferdata['cell_distance']):
                cell_distance_val = res.cell_distance
            else:
                cell_distance_val = bufferdata['cell_distance']
        else:
            cell_distance_val = res.cell_distance
        if "pic_train_delay" in bufferdata.keys():
            if (res.vis_res_addup_set == bufferdata['pic_train_delay']):
                pic_train_delay_val = res.pic_train_delay
            else:
                pic_train_delay_val = bufferdata['pic_train_delay']
        else:
            pic_train_delay_val = res.pic_train_delay
        if "addup_set" in bufferdata.keys():
            if (res.addup_set == bufferdata['addup_set']):
                addup_set_val = res.addup_set
            else:
                addup_set_val = bufferdata['addup_set']
        else:
            addup_set_val = res.addup_set
          
        models.t_cebs_fspc.objects.filter(tup_lable = tup_lable_val).update(                       
            mark_line = mark_line_val,mark_width = mark_width_val,mark_area = mark_area_val,mark_dilate = mark_dilate_val,\
            area_square_min = area_square_min_val,area_squre_max = area_squre_max_val,area_dilate = area_dilate_val,area_erode = area_erode_val,\
            cell_square_min = cell_square_min_val,cell_square_max = cell_square_max_val,cell_raduis_min = cell_raduis_min_val,cell_raduis_max = cell_raduis_max_val,\
            cell_dilate = cell_dilate_val,cell_erode = cell_erode_val,cell_ce = cell_ce_val,cell_distance = cell_distance_val,pic_train_delay = pic_train_delay_val,addup_set = addup_set_val)         
        return True 

    def dft_dbi_fspc_delete(self, inputData):
        bufferdata = inputData['tupLable']
        print(bufferdata)
        models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable']).delete()
        return True

    def dft_dbi_file_add(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        if "batch_no" in bufferdata.keys():
            batch_no_val = bufferdata['batch_no']
        else:
            batch_no_val = 0
        if "hole_no" in bufferdata.keys():
            hole_no_val = bufferdata['hole_no']
        else:
            hole_no_val = 0
        if "hole_name" in bufferdata.keys():
            hole_name_val = bufferdata['hole_name']
        else:
            hole_name_val = ''
        if "pic_file_name" in bufferdata.keys():
            pic_file_name_val = bufferdata['pic_file_name']
        else:
            pic_file_name_val = 0
        if "file_att" in bufferdata.keys():
            file_att_val = bufferdata['file_att']
        else:
            file_att_val = 'normal'
        if "vid_file_name" in bufferdata.keys():
            vid_file_name_val = bufferdata['vid_file_name']
        else:
            vid_file_name_val = 0
        if "classified_flag" in bufferdata.keys():
            classified_flag_val = bufferdata['classified_flag']
        else:
            classified_flag_val = False
        if "video_flag" in bufferdata.keys():
            video_flag_val = bufferdata['video_flag']
        else:
            video_flag_val = False
        if "cfy_res" in bufferdata.keys():
            cfy_res_val = bufferdata['cfy_res']
        else:
            cfy_res_val = ''
        models.t_cebs_batch_file.objects.create(\
            batch_no = batch_no_val,hole_no = hole_no_val,hole_name = hole_name_val,pic_file_name = pic_file_name_val,\
            file_att = file_att_val,vid_file_name = vid_file_name_val,classified_flag = classified_flag_val,video_flag = video_flag_val,cfy_res = cfy_res_val
            )
        return True

    def dft_dbi_file_read(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata)
        res = models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no'])
        bufferout= {}
#         for line in res:
#             print(line.hole_no)

        if "hole_no" in bufferdata.keys():
            bufferout['hole_no'] = res[0].hole_no;

        else:
            pass
        if "hole_name" in bufferdata.keys():
            bufferout['hole_name'] = res[0].hole_name;
        else:
            pass
        if "pic_file_name" in bufferdata.keys():
            bufferout['pic_file_name'] = res[0].pic_file_name;
        else:
            pass
        if "file_att" in bufferdata.keys():
            bufferout['file_att'] = res[0].file_att;
        else:
            pass
        if "vid_file_name" in bufferdata.keys():
            bufferout['vid_file_name'] = res[0].vid_file_name;
        else:
            pass
        if "classified_flag" in bufferdata.keys():
            bufferout['classified_flag'] = res[0].classified_flag;
        else:
            pass
        if "video_flag" in bufferdata.keys():
            bufferout['video_flag'] = res[0].video_flag;
        else:
            pass
        if "cfy_res" in bufferdata.keys():
            bufferout['cfy_res'] = res[0].cfy_res;
        else:
            pass
        print(bufferout)
        return True


    def dft_dbi_file_modify(self, inputData):
        print(inputData)
        bufferdata = inputData['tupLable']
        print(bufferdata) 
        
        res = models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no'])
        for line in res:
            res.batch_no = line.batch_no
            res.hole_no = line.hole_no  
            res.hole_name = line.hole_name
            res.pic_file_name = line.pic_file_name
            res.file_att = line.file_att
            res.vid_file_name = line.vid_file_name
            res.classified_flag = line.classified_flag
            res.video_flag = line.video_flag
            res.cfy_res = line.cfy_res
 
        if "batch_no" in bufferdata.keys():
            if (res.batch_no == bufferdata['batch_no']):
                batch_no_val = res.batch_no
            else:
                batch_no_val = bufferdata['batch_no'] 
        else:
            batch_no_val = res.batch_no
        if "hole_no" in bufferdata.keys():
            if (res.hole_no == bufferdata['hole_no']):
                hole_no_val = res.hole_no
            else:
                hole_no_val = bufferdata['hole_no']
        else:
            hole_no_val = res.hole_no
        if "hole_name" in bufferdata.keys():
            if (res.hole_name == bufferdata['hole_name']):
                hole_name_val = res.hole_name
            else:
                hole_name_val = bufferdata['hole_name']
        else:
            hole_name_val = res.hole_name
        if "pic_file_name" in bufferdata.keys():
            if (res.pic_file_name == bufferdata['pic_file_name']):
                pic_file_name_val = res.pic_file_name
            else:
                pic_file_name_val = bufferdata['pic_file_name']
        else:
            pic_file_name_val = res.pic_file_name
        if "file_att" in bufferdata.keys():
            if (res.file_att == bufferdata['file_att']):
                file_att_val = res.file_att
            else:
                file_att_val = bufferdata['file_att']
        else:
            file_att_val = res.file_att
        if "vid_file_name" in bufferdata.keys():
            if (res.vid_file_name == bufferdata['vid_file_name']):
                vid_file_name_val = res.vid_file_name
            else:
                vid_file_name_val = bufferdata['vid_file_name']
        else:
            vid_file_name_val = res.vid_file_name 
        if "classified_flag" in bufferdata.keys():
            if (res.classified_flag == bufferdata['classified_flag']):
                classified_flag_val = res.classified_flag
            else:
                classified_flag_val = bufferdata['classified_flag']
        else:
            classified_flag_val = res.classified_flag
        if "video_flag" in bufferdata.keys():
            if (res.video_flag == bufferdata['video_flag']):
                video_flag_val = res.video_flag
            else:
                video_flag_val = bufferdata['video_flag']        
        else:
            video_flag_val = res.video_flag
        if "cfy_res" in bufferdata.keys():
            if (res.cfy_res == bufferdata['cfy_res']):
                cfy_res_val = res.cfy_res
            else:
                cfy_res_val = bufferdata['cfy_res']
        else:
            cfy_res_val = res.cfy_res
        models.t_cebs_batch_file.objects.filter(batch_no = batch_no_val).update(                       
            hole_no = hole_no_val,hole_name = hole_name_val,pic_file_name = pic_file_name_val,\
            file_att = file_att_val,vid_file_name = vid_file_name_val,classified_flag = classified_flag_val,video_flag = video_flag_val,cfy_res = cfy_res_val)         
        return True 

    def dft_dbi_file_delete(self, inputData):
        bufferdata = inputData['tupLable']
        print(bufferdata)
        models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no']).delete()
        return True














