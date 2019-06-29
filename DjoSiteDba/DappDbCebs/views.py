from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib import admin
import random
import datetime
import time
#import pycurl
import io
from DappDbCebs import models
from django.template.defaultfilters import length
from DappDbInsertData.CheckoutMenuAndAction import update_menu_and_action
from numpy import append
#from test.badsyntax_future3 import result

# Create your views here.
class dct_classDbiViewDebs:
    def __init__(self):
        pass

#     #输入参数必须是完整的数据集合，并以Json为单位
#     def CustomerMission_add(self, request):
#         models.t_customer_mission.objects.create(\
#             user=request['user'],\
#             timeStampSubmit=request['timeStampSubmit'],\
#             pageNbr=request['pageNbr'],\
#             filePath=request['filePath'],\
#             fileName=request['fileName'],\
#             );
#         return HttpResponse("OK")
#     
#     def CustomerMission_delete(self, request):
#         models.t_customer_mission.objects.filter(user=request['user']).delete()
#         return HttpResponse("OK")
#     
#     #使用UserId，修改其他信息
#     def CustomerMission_modify_by_user(self, request):
#         models.t_customer_mission.objects.filter(user=request['user']).update(\
#             timeStampSubmit=request['timeStampSubmit'],\
#             pageNbr=request['pageNbr'],\
#             filePath=request['filePath'],\
#             fileName=request['fileName'],\
#             );
#         return HttpResponse("OK")  # 返回字符串
#     
#     def CustomerMission_inqury(self, request):
#         return models.t_customer_mission.objects.get(user=request['user'])
#     
#     #输入参数必须是完整的数据集合，并以Json为单位
#     def ClassifyExecLog_add(self, request):
#         models.t_cebs_classify_exec_log.objects.create(\
#             user=request['user'],\
#             timeStampExec=request['timeStampExec'],\
#             pageLen=request['pageLen'],\
#             pageWidth=request['pageWidth'],\
#             resTotal=request['resTotal'],\
#             resTotalAlive=request['resTotalAlive'],\
#             resTotalDead=request['resTotalDead'],\
#             resSmallAlive=request['resSmallAlive'],\
#             resSmallDead=request['resSmallDead'],\
#             resMidAlive=request['resMidAlive'],\
#             resMidDead=request['resMidDead'],\
#             resBigAlive=request['resBigAlive'],\
#             resBigDead=request['resBigDead'],\
#             resUnclassifyAlive=request['resUnclassifyAlive'],\
#             resUnclassifyDead=request['resUnclassifyDead'],\
#             );
#         return HttpResponse("OK")
#         
#     def ClassifyExecLog_delete(self, request):
#         models.t_cebs_classify_exec_log.objects.filter(user=request['user']).delete()
#         return HttpResponse("OK")
#     
#     #使用UserId，修改其他信息
#     def ClassifyExecLog_modify_by_user(self, request):
#         models.t_cebs_classify_exec_log.objects.filter(user=request['user']).update(\
#             timeStampExec=request['timeStampExec'],\
#             pageLen=request['pageLen'],\
#             pageWidth=request['pageWidth'],\
#             resTotal=request['resTotal'],\
#             resTotalAlive=request['resTotalAlive'],\
#             resTotalDead=request['resTotalDead'],\
#             resSmallAlive=request['resSmallAlive'],\
#             resSmallDead=request['resSmallDead'],\
#             resMidAlive=request['resMidAlive'],\
#             resMidDead=request['resMidDead'],\
#             resBigAlive=request['resBigAlive'],\
#             resBigDead=request['resBigDead'],\
#             resUnclassifyAlive=request['resUnclassifyAlive'],\
#             resUnclassifyDead=request['resUnclassifyDead'],\
#             );
#         return HttpResponse("OK")  # 返回字符串
#     
#     def ClassifyExecLog_inqury(self, request):
#         return models.t_cebs_classify_exec_log.objects.get(user=request['user']);

#     def dft_dbi_env_add(self, inputData):
#         #models.t_cebs_env.objects.create(workdir = inputData['tupLable'])
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         print(bufferdata['workdir'])
#         if "tupLable" in bufferdata.keys():
#             tup_lable = bufferdata['tupLable']
#         else:
#             tup_lable = 0
#         if "workdir" in bufferdata.keys():
#             workdir_val = bufferdata['workdir']
#         else:
#             workdir_val = ''
#         if "pic_origin" in bufferdata.keys():
#             pic_origin_val = bufferdata['pic_origin']
#         else:
#             pic_origin_val = ''
#         if "pic_middle" in bufferdata.keys():
#             pic_middle_val = bufferdata['pic_middle']
#         else:
#             pic_middle_val = '' 
#         if "holeboard_type" in bufferdata.keys():
#             holeboard_type_val = bufferdata['holeboard_type']
#         else:
#             holeboard_type_val = ''
#         if "holeboard_left_bot_x" in bufferdata.keys():
#             holeboard_left_bot_x_val = bufferdata['holeboard_left_bot_x']
#         else:
#             holeboard_left_bot_x_val = 0
#         if "holeboard_left_bot_y" in bufferdata.keys():
#             holeboard_left_bot_y_val = bufferdata['holeboard_left_bot_y']
#         else:
#             holeboard_left_bot_y_val = 0
#         if "holeboard_right_up_x" in bufferdata.keys():
#             holeboard_right_up_x_val = bufferdata['holeboard_right_up_x']
#         else:
#             holeboard_right_up_x_val = 0        
#         if "holeboard_right_up_y" in bufferdata.keys():
#             holeboard_right_up_y_val = bufferdata['holeboard_right_up_y']
#         else:
#             holeboard_right_up_y_val = 0
#         if "pic_take_fix_point_set" in bufferdata.keys():
#             pic_take_fix_point_set_val = bufferdata['pic_take_fix_point_set']
#         else:
#             pic_take_fix_point_set_val = False
#         if "pic_classification_set" in bufferdata.keys():
#             pic_classification_set_val = bufferdata['pic_classification_set']
#         else:
#             pic_classification_set_val = False
#         if "pic_auto_work_after_start_set" in bufferdata.keys():
#             pic_auto_work_after_start_set_val = bufferdata['pic_auto_work_after_start_set']
#         else:
#             pic_auto_work_after_start_set_val = False
#         if "pic_auto_work_tti" in bufferdata.keys():
#             pic_auto_work_tti_val = bufferdata['pic_auto_work_tti']
#         else:
#             pic_auto_work_tti_val = 0
#         if "vis_small_low_limit" in bufferdata.keys():
#             vis_small_low_limit_val = bufferdata['vis_small_low_limit']
#         else:
#             vis_small_low_limit_val = 0
#         if "vis_small_mid_limit" in bufferdata.keys():
#             vis_small_mid_limit_val = bufferdata['vis_small_mid_limit']
#         else:
#             vis_small_mid_limit_val = 0
#         if "vis_mid_big_limit" in bufferdata.keys():
#             vis_mid_big_limit_val = bufferdata['vis_mid_big_limit']
#         else:
#             vis_mid_big_limit_val = 0
#         if "vis_big_upper_limit" in bufferdata.keys():
#             vis_big_upper_limit_val = bufferdata['vis_big_upper_limit']
#         else:
#             vis_big_upper_limit_val = 0
#         if "vis_res_addup_set" in bufferdata.keys():
#             vis_res_addup_set_val = bufferdata['vis_res_addup_set']
#         else:
#             vis_res_addup_set_val = False
#         if "vis_cap_enable_set" in bufferdata.keys():
#             vis_cap_enable_set_val = bufferdata['vis_cap_enable_set']
#         else:
#             vis_cap_enable_set_val = False
#         if "vis_cap_dur_in_sec" in bufferdata.keys():
#             vis_cap_dur_in_sec_val = bufferdata['vis_cap_dur_in_sec']
#         else:
#             vis_cap_dur_in_sec_val = 3
#         if "vis_clfy_gen_par1" in bufferdata.keys():
#             vis_clfy_gen_par1_val = bufferdata['vis_clfy_gen_par1']
#         else:
#             vis_clfy_gen_par1_val = 0 
#         if "vis_clfy_gen_par2" in bufferdata.keys():
#             vis_clfy_gen_par2_val = bufferdata['vis_clfy_gen_par2']
#         else:
#             vis_clfy_gen_par2_val = 0
#         if "vis_clfy_gen_par3" in bufferdata.keys():
#             vis_clfy_gen_par3_val = bufferdata['vis_clfy_gen_par3']
#         else:
#             vis_clfy_gen_par3_val = 0
#         if "vis_clfy_gen_par4" in bufferdata.keys():
#             vis_clfy_gen_par4_val = bufferdata['vis_clfy_gen_par4']
#         else:
#             vis_clfy_gen_par4_val = 0 
#         models.t_cebs_env.objects.create(\
#             tup_lable = tup_lable,                           
#             workdir = workdir_val,pic_origin = pic_origin_val,pic_middle = pic_middle_val,holeboard_type = holeboard_type_val,\
#             holeboard_left_bot_x = holeboard_left_bot_x_val,holeboard_left_bot_y = holeboard_left_bot_y_val,holeboard_right_up_x = holeboard_right_up_x_val,\
#             holeboard_right_up_y = holeboard_right_up_y_val,pic_take_fix_point_set = pic_take_fix_point_set_val,pic_classification_set = pic_classification_set_val,\
#             pic_auto_work_after_start_set = pic_auto_work_after_start_set_val,pic_auto_work_tti = pic_auto_work_tti_val,vis_small_low_limit = vis_small_low_limit_val,\
#             vis_small_mid_limit = vis_small_mid_limit_val,vis_mid_big_limit = vis_mid_big_limit_val,vis_big_upper_limit = vis_big_upper_limit_val,vis_res_addup_set = vis_res_addup_set_val,\
#             vis_cap_enable_set = vis_cap_enable_set_val,vis_cap_dur_in_sec = vis_cap_dur_in_sec_val,vis_clfy_gen_par1 = vis_clfy_gen_par1_val,vis_clfy_gen_par2 = vis_clfy_gen_par2_val,\
#             vis_clfy_gen_par3 = vis_clfy_gen_par3_val,vis_clfy_gen_par4 = vis_clfy_gen_par4_val,\
#             )
#         return True
#     
#     def dft_dbi_env_read(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         print(bufferdata['tupLable'])
#         
#         res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'])
#             
#         bufferout= {}
#         if res.exists():
#             for line in res:
#                 res.workdir = line.workdir  
#                 res.pic_origin = line.pic_origin
#                 res.pic_middle = line.pic_middle
#                 res.holeboard_type = line.holeboard_type
#                 res.holeboard_left_bot_x = line.holeboard_left_bot_x
#                 res.holeboard_left_bot_y = line.holeboard_left_bot_y
#                 res.holeboard_right_up_x = line.holeboard_right_up_x
#                 res.holeboard_right_up_y = line.holeboard_right_up_y
#                 res.pic_take_fix_point_set = line.pic_take_fix_point_set
#                 res.pic_classification_set = line.pic_classification_set
#                 res.pic_auto_work_after_start_set = line.pic_auto_work_after_start_set
#                 res.pic_auto_work_tti = line.pic_auto_work_tti
#                 res.vis_small_low_limit = line.vis_small_low_limit
#                 res.vis_small_mid_limit = line.vis_small_mid_limit
#                 res.vis_mid_big_limit = line.vis_mid_big_limit
#                 res.vis_big_upper_limit = line.vis_big_upper_limit
#                 res.vis_res_addup_set = line.vis_res_addup_set
#                 res.vis_cap_enable_set = line.vis_cap_enable_set
#                 res.vis_cap_dur_in_sec = line.vis_cap_dur_in_sec
#                 res.vis_clfy_gen_par1 = line.vis_clfy_gen_par1
#                 res.vis_clfy_gen_par2 = line.vis_clfy_gen_par2
#                 res.vis_clfy_gen_par3 = line.vis_clfy_gen_par3
#                 res.vis_clfy_gen_par4 = line.vis_clfy_gen_par4
#         else:
#             return False   
#         
#         if "workdir" in bufferdata.keys():
#             bufferout['workdir'] = res.workdir;
#         else:
#             pass
#         if "pic_origin" in bufferdata.keys():
#             bufferout['pic_origin'] = res.pic_origin;
#         else:
#             pass
#         if "pic_middle" in bufferdata.keys():
#             bufferout['pic_middle'] = res.pic_middle;
#         else:
#             pass
#         if "holeboard_type" in bufferdata.keys():
#             bufferout['holeboard_type'] = res.holeboard_type;
#         else:
#             pass
#         if "holeboard_left_bot_x" in bufferdata.keys():
#             bufferout['holeboard_left_bot_x'] = res.holeboard_left_bot_x;
#         else:
#             pass
#         if "holeboard_left_bot_y" in bufferdata.keys():
#             bufferout['holeboard_left_bot_y'] = res.holeboard_left_bot_y;
#         else:
#             pass
#         if "holeboard_right_up_x" in bufferdata.keys():
#             bufferout['holeboard_right_up_x'] = res.holeboard_right_up_x;
#         else:
#             pass
#         if "holeboard_right_up_y" in bufferdata.keys():
#             bufferout['holeboard_right_up_y'] = res.holeboard_right_up_y;
#         else:
#             pass
#         if "pic_take_fix_point_set" in bufferdata.keys():
#             bufferout['pic_take_fix_point_set'] = res.pic_take_fix_point_set;
#         else:
#             pass
#         if "pic_classification_set" in bufferdata.keys():
#             bufferout['pic_classification_set'] = res.pic_classification_set;
#         else:
#             pass
#         if "pic_auto_work_after_start_set" in bufferdata.keys():
#             bufferout['pic_auto_work_after_start_set'] = res.pic_auto_work_after_start_set;
#         else:
#             pass
#         if "pic_auto_work_tti" in bufferdata.keys():
#             bufferout['pic_auto_work_tti'] = res.pic_auto_work_tti;
#         else:
#             pass
#         if "vis_small_low_limit" in bufferdata.keys():
#             bufferout['vis_small_low_limit'] = res.vis_small_low_limit;
#         else:
#             pass
#         if "vis_small_mid_limit" in bufferdata.keys():
#             bufferout['vis_small_mid_limit'] = res.vis_small_mid_limit;
#         else:
#             pass
#         if "vis_mid_big_limit" in bufferdata.keys():
#             bufferout['vis_mid_big_limit'] = res.vis_mid_big_limit;
#         else:
#             pass
#         if "vis_big_upper_limit" in bufferdata.keys():
#             bufferout['vis_big_upper_limit'] = res.vis_big_upper_limit;
#         else:
#             pass
#         if "vis_res_addup_set" in bufferdata.keys():
#             bufferout['vis_res_addup_set'] = res.vis_res_addup_set;
#         else:
#             pass
#         if "vis_cap_enable_set" in bufferdata.keys():
#             bufferout['vis_cap_enable_set'] = res.vis_cap_enable_set;
#         else:
#             pass
#         if "vis_cap_dur_in_sec" in bufferdata.keys():
#             bufferout['vis_cap_dur_in_sec'] = res.vis_cap_dur_in_sec;
#         else:
#             pass
#         if "vis_clfy_gen_par1" in bufferdata.keys():
#             bufferout['vis_clfy_gen_par1'] = res.vis_clfy_gen_par1;
#         else:
#             pass
#         if "vis_clfy_gen_par2" in bufferdata.keys():
#             bufferout['vis_clfy_gen_par2'] = res.vis_clfy_gen_par2;
#         else:
#             pass
#         if "vis_clfy_gen_par3" in bufferdata.keys():
#             bufferout['vis_clfy_gen_par3'] = res.vis_clfy_gen_par3;
#         else:
#             pass
#         if "vis_clfy_gen_par4" in bufferdata.keys():
#             bufferout['vis_clfy_gen_par4'] = res.vis_clfy_gen_par4;
#         else:
#             pass
#             
#         return bufferout
# 
#     #read LC：这里留下一个读取多行的demo  以后按照需要来进行完善   其他read都是读取一行
#     def dft_dbi_env_read_multi(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         print(bufferdata['tupLable'])
#         datalength = len(bufferdata['tupLable'])
# 
#         
#         for i in range (0,datalength,1):
#             res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'][i])
#             
#             bufferout= {}
#             data = {}
#             if res.exists():
#                 for line in res:
#                     res.workdir = line.workdir  
#                     res.pic_origin = line.pic_origin
#                     res.pic_middle = line.pic_middle
#                     res.holeboard_type = line.holeboard_type
#                     res.holeboard_left_bot_x = line.holeboard_left_bot_x
#                     res.holeboard_left_bot_y = line.holeboard_left_bot_y
#                     res.holeboard_right_up_x = line.holeboard_right_up_x
#                     res.holeboard_right_up_y = line.holeboard_right_up_y
#                     res.pic_take_fix_point_set = line.pic_take_fix_point_set
#                     res.pic_classification_set = line.pic_classification_set
#                     res.pic_auto_work_after_start_set = line.pic_auto_work_after_start_set
#                     res.pic_auto_work_tti = line.pic_auto_work_tti
#                     res.vis_small_low_limit = line.vis_small_low_limit
#                     res.vis_small_mid_limit = line.vis_small_mid_limit
#                     res.vis_mid_big_limit = line.vis_mid_big_limit
#                     res.vis_big_upper_limit = line.vis_big_upper_limit
#                     res.vis_res_addup_set = line.vis_res_addup_set
#                     res.vis_cap_enable_set = line.vis_cap_enable_set
#                     res.vis_cap_dur_in_sec = line.vis_cap_dur_in_sec
#                     res.vis_clfy_gen_par1 = line.vis_clfy_gen_par1
#                     res.vis_clfy_gen_par2 = line.vis_clfy_gen_par2
#                     res.vis_clfy_gen_par3 = line.vis_clfy_gen_par3
#                     res.vis_clfy_gen_par4 = line.vis_clfy_gen_par4
#             else:
#                 return False   
#             
#             if "workdir" in bufferdata.keys():
#                 bufferout['workdir'] = res.workdir;
#             else:
#                 pass
#             if "pic_origin" in bufferdata.keys():
#                 bufferout['pic_origin'] = res.pic_origin;
#             else:
#                 pass
#             if "pic_middle" in bufferdata.keys():
#                 bufferout['pic_middle'] = res.pic_middle;
#             else:
#                 pass
#             if "holeboard_type" in bufferdata.keys():
#                 bufferout['holeboard_type'] = res.holeboard_type;
#             else:
#                 pass
#             if "holeboard_left_bot_x" in bufferdata.keys():
#                 bufferout['holeboard_left_bot_x'] = res.holeboard_left_bot_x;
#             else:
#                 pass
#             if "holeboard_left_bot_y" in bufferdata.keys():
#                 bufferout['holeboard_left_bot_y'] = res.holeboard_left_bot_y;
#             else:
#                 pass
#             if "holeboard_right_up_x" in bufferdata.keys():
#                 bufferout['holeboard_right_up_x'] = res.holeboard_right_up_x;
#             else:
#                 pass
#             if "holeboard_right_up_y" in bufferdata.keys():
#                 bufferout['holeboard_right_up_y'] = res.holeboard_right_up_y;
#             else:
#                 pass
#             if "pic_take_fix_point_set" in bufferdata.keys():
#                 bufferout['pic_take_fix_point_set'] = res.pic_take_fix_point_set;
#             else:
#                 pass
#             if "pic_classification_set" in bufferdata.keys():
#                 bufferout['pic_classification_set'] = res.pic_classification_set;
#             else:
#                 pass
#             if "pic_auto_work_after_start_set" in bufferdata.keys():
#                 bufferout['pic_auto_work_after_start_set'] = res.pic_auto_work_after_start_set;
#             else:
#                 pass
#             if "pic_auto_work_tti" in bufferdata.keys():
#                 bufferout['pic_auto_work_tti'] = res.pic_auto_work_tti;
#             else:
#                 pass
#             if "vis_small_low_limit" in bufferdata.keys():
#                 bufferout['vis_small_low_limit'] = res.vis_small_low_limit;
#             else:
#                 pass
#             if "vis_small_mid_limit" in bufferdata.keys():
#                 bufferout['vis_small_mid_limit'] = res.vis_small_mid_limit;
#             else:
#                 pass
#             if "vis_mid_big_limit" in bufferdata.keys():
#                 bufferout['vis_mid_big_limit'] = res.vis_mid_big_limit;
#             else:
#                 pass
#             if "vis_big_upper_limit" in bufferdata.keys():
#                 bufferout['vis_big_upper_limit'] = res.vis_big_upper_limit;
#             else:
#                 pass
#             if "vis_res_addup_set" in bufferdata.keys():
#                 bufferout['vis_res_addup_set'] = res.vis_res_addup_set;
#             else:
#                 pass
#             if "vis_cap_enable_set" in bufferdata.keys():
#                 bufferout['vis_cap_enable_set'] = res.vis_cap_enable_set;
#             else:
#                 pass
#             if "vis_cap_dur_in_sec" in bufferdata.keys():
#                 bufferout['vis_cap_dur_in_sec'] = res.vis_cap_dur_in_sec;
#             else:
#                 pass
#             if "vis_clfy_gen_par1" in bufferdata.keys():
#                 bufferout['vis_clfy_gen_par1'] = res.vis_clfy_gen_par1;
#             else:
#                 pass
#             if "vis_clfy_gen_par2" in bufferdata.keys():
#                 bufferout['vis_clfy_gen_par2'] = res.vis_clfy_gen_par2;
#             else:
#                 pass
#             if "vis_clfy_gen_par3" in bufferdata.keys():
#                 bufferout['vis_clfy_gen_par3'] = res.vis_clfy_gen_par3;
#             else:
#                 pass
#             if "vis_clfy_gen_par4" in bufferdata.keys():
#                 bufferout['vis_clfy_gen_par4'] = res.vis_clfy_gen_par4;
#             else:
#                 pass
#             #data = f'bufferout'
#             #data.append(bufferout[i])
#         print("data",data)    
#         return bufferout
#     
#        
#         
# 
#     def dft_dbi_env_modify(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata) 
#         
#         res = models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable'])
#         if res.exists():
#             for line in res:
#                 res.tup_lable = line.tup_lable
#                 res.workdir = line.workdir  
#                 res.pic_origin = line.pic_origin
#                 res.pic_middle = line.pic_middle
#                 res.holeboard_type = line.holeboard_type
#                 res.holeboard_left_bot_x = line.holeboard_left_bot_x
#                 res.holeboard_left_bot_y = line.holeboard_left_bot_y
#                 res.holeboard_right_up_x = line.holeboard_right_up_x
#                 res.holeboard_right_up_y = line.holeboard_right_up_y
#                 res.pic_take_fix_point_set = line.pic_take_fix_point_set
#                 res.pic_classification_set = line.pic_classification_set
#                 res.pic_auto_work_after_start_set = line.pic_auto_work_after_start_set
#                 res.pic_auto_work_tti = line.pic_auto_work_tti
#                 res.vis_small_low_limit = line.vis_small_low_limit
#                 res.vis_small_mid_limit = line.vis_small_mid_limit
#                 res.vis_mid_big_limit = line.vis_mid_big_limit
#                 res.vis_big_upper_limit = line.vis_big_upper_limit
#                 res.vis_res_addup_set = line.vis_res_addup_set
#                 res.vis_cap_enable_set = line.vis_cap_enable_set
#                 res.vis_cap_dur_in_sec = line.vis_cap_dur_in_sec
#                 res.vis_clfy_gen_par1 = line.vis_clfy_gen_par1
#                 res.vis_clfy_gen_par2 = line.vis_clfy_gen_par2
#                 res.vis_clfy_gen_par3 = line.vis_clfy_gen_par3
#                 res.vis_clfy_gen_par4 = line.vis_clfy_gen_par4
#         else:
#             return False    
# #         print(res.tup_lable)
# #         print(bufferdata['tupLable'])   
#         if "tupLable" in bufferdata.keys():
#             if (res.tup_lable == bufferdata['tupLable']):
#                 tup_lable_val = res.tup_lable
#             else:
#                 tup_lable_val = bufferdata['tupLable'] 
#         else:
#             tup_lable_val = res.tup_lable
#         if "workdir" in bufferdata.keys():
#             if (res.workdir == bufferdata['workdir']):
#                 workdir_val = res.workdir
#             else:
#                 workdir_val = bufferdata['workdir']
#         else:
#             workdir_val = res.workdir
#         if "pic_origin" in bufferdata.keys():
#             if (res.pic_origin == bufferdata['pic_origin']):
#                 pic_origin_val = res.pic_origin
#             else:
#                 pic_origin_val = bufferdata['pic_origin']
#         else:
#             pic_origin_val = res.pic_origin
#         if "pic_middle" in bufferdata.keys():
#             if (res.pic_middle == bufferdata['pic_middle']):
#                 pic_middle_val = res.pic_middle
#             else:
#                 pic_middle_val = bufferdata['pic_middle']
#         else:
#             pic_middle_val = res.pic_middle
#         if "holeboard_type" in bufferdata.keys():
#             if (res.holeboard_type == bufferdata['holeboard_type']):
#                 holeboard_type_val = res.holeboard_type
#             else:
#                 holeboard_type_val = bufferdata['holeboard_type']
#         else:
#             holeboard_type_val = res.holeboard_type
#         if "holeboard_left_bot_x" in bufferdata.keys():
#             if (res.holeboard_left_bot_x == bufferdata['holeboard_left_bot_x']):
#                 holeboard_left_bot_x_val = res.holeboard_left_bot_x
#             else:
#                 holeboard_left_bot_x_val = bufferdata['holeboard_left_bot_x']
#         else:
#             holeboard_left_bot_x_val = res.holeboard_left_bot_x 
#         if "holeboard_left_bot_y" in bufferdata.keys():
#             if (res.holeboard_left_bot_y == bufferdata['holeboard_left_bot_y']):
#                 holeboard_left_bot_y_val = res.holeboard_left_bot_y
#             else:
#                 holeboard_left_bot_y_val = bufferdata['holeboard_left_bot_y']
#         else:
#             holeboard_left_bot_y_val = res.holeboard_left_bot_y
#         if "holeboard_right_up_x" in bufferdata.keys():
#             if (res.holeboard_right_up_x == bufferdata['holeboard_right_up_x']):
#                 holeboard_right_up_x_val = res.holeboard_right_up_x
#             else:
#                 holeboard_right_up_x_val = bufferdata['holeboard_right_up_x']        
#         else:
#             holeboard_right_up_x_val = res.holeboard_right_up_x
#         if "holeboard_right_up_y" in bufferdata.keys():
#             if (res.holeboard_right_up_y == bufferdata['holeboard_right_up_y']):
#                 holeboard_right_up_y_val = res.holeboard_right_up_y
#             else:
#                 holeboard_right_up_y_val = bufferdata['holeboard_right_up_y']
#         else:
#             holeboard_right_up_y_val = res.holeboard_right_up_y
#         if "pic_take_fix_point_set" in bufferdata.keys():
#             if (res.pic_take_fix_point_set == bufferdata['pic_take_fix_point_set']):
#                 pic_take_fix_point_set_val = res.pic_take_fix_point_set
#             else:
#                 pic_take_fix_point_set_val = bufferdata['pic_take_fix_point_set']
#         else:
#             pic_take_fix_point_set_val = res.pic_take_fix_point_set
#         if "pic_classification_set" in bufferdata.keys():
#             if (res.pic_classification_set == bufferdata['pic_classification_set']):
#                 pic_classification_set_val = res.pic_classification_set
#             else:
#                 pic_classification_set_val = bufferdata['pic_classification_set']
#         else:
#             pic_classification_set_val = res.pic_classification_set
#         if "pic_auto_work_after_start_set" in bufferdata.keys():
#             if (res.pic_auto_work_after_start_set == bufferdata['pic_auto_work_after_start_set']):
#                 pic_auto_work_after_start_set_val = res.pic_auto_work_after_start_set
#             else:
#                 pic_auto_work_after_start_set_val = bufferdata['pic_auto_work_after_start_set']
#         else:
#             pic_auto_work_after_start_set_val = res.pic_auto_work_after_start_set
#         if "pic_auto_work_tti" in bufferdata.keys():
#             if (res.pic_auto_work_tti == bufferdata['pic_auto_work_tti']):
#                 pic_auto_work_tti_val = res.pic_auto_work_tti
#             else:
#                 pic_auto_work_tti_val = bufferdata['pic_auto_work_tti']
#         else:
#             pic_auto_work_tti_val = res.pic_auto_work_tti
#         if "vis_small_low_limit" in bufferdata.keys():
#             if (res.vis_small_low_limit == bufferdata['vis_small_low_limit']):
#                 vis_small_low_limit_val = res.vis_small_low_limit
#             else:
#                 vis_small_low_limit_val = bufferdata['vis_small_low_limit']
#         else:
#             vis_small_low_limit_val = res.vis_small_low_limit
#         if "vis_small_mid_limit" in bufferdata.keys():
#             if (res.vis_small_mid_limit == bufferdata['vis_small_mid_limit']):
#                 vis_small_mid_limit_val = res.vis_small_mid_limit
#             else:
#                 vis_small_mid_limit_val = bufferdata['vis_small_mid_limit']
#         else:
#             vis_small_mid_limit_val = res.vis_small_mid_limit
#         if "vis_mid_big_limit" in bufferdata.keys():
#             if (res.vis_mid_big_limit == bufferdata['vis_mid_big_limit']):
#                 vis_mid_big_limit_val = res.vis_mid_big_limit
#             else:
#                 vis_mid_big_limit_val = bufferdata['vis_mid_big_limit']
#         else:
#             vis_mid_big_limit_val = res.vis_mid_big_limit
#         if "vis_big_upper_limit" in bufferdata.keys():
#             if (res.vis_big_upper_limit == bufferdata['vis_big_upper_limit']):
#                 vis_big_upper_limit_val = res.vis_big_upper_limit
#             else:
#                 vis_big_upper_limit_val = bufferdata['vis_big_upper_limit']
#         else:
#             vis_big_upper_limit_val = res.vis_big_upper_limit
#         if "vis_res_addup_set" in bufferdata.keys():
#             if (res.vis_res_addup_set == bufferdata['vis_res_addup_set']):
#                 vis_res_addup_set_val = res.vis_res_addup_set
#             else:
#                 vis_res_addup_set_val = bufferdata['vis_res_addup_set']
#         else:
#             vis_res_addup_set_val = res.vis_res_addup_set
#         if "vis_cap_enable_set" in bufferdata.keys():
#             if (res.vis_cap_enable_set == bufferdata['vis_cap_enable_set']):
#                 vis_cap_enable_set_val = res.vis_cap_enable_set
#             else:
#                 vis_cap_enable_set_val = bufferdata['vis_cap_enable_set']
#         else:
#             vis_cap_enable_set_val = res.vis_cap_enable_set
#         if "vis_cap_dur_in_sec" in bufferdata.keys():
#             if (res.vis_cap_dur_in_sec == bufferdata['vis_cap_dur_in_sec']):
#                 vis_cap_dur_in_sec_val = res.vis_cap_dur_in_sec
#             else:
#                 vis_cap_dur_in_sec_val = bufferdata['vis_cap_dur_in_sec']
#         else:
#             vis_cap_dur_in_sec_val = res.vis_cap_dur_in_sec
#         if "vis_clfy_gen_par1" in bufferdata.keys():
#             if (res.vis_clfy_gen_par1 == bufferdata['vis_clfy_gen_par1']):
#                 vis_clfy_gen_par1_val = res.vis_clfy_gen_par1
#             else:
#                 vis_clfy_gen_par1_val = bufferdata['vis_clfy_gen_par1'] 
#         else:
#             vis_clfy_gen_par1_val = res.vis_clfy_gen_par1
#         if "vis_clfy_gen_par2" in bufferdata.keys():
#             if (res.vis_clfy_gen_par2 == bufferdata['vis_clfy_gen_par2']):
#                 vis_clfy_gen_par2_val = res.vis_clfy_gen_par2
#             else:
#                 vis_clfy_gen_par2_val = bufferdata['vis_clfy_gen_par2']
#         else:
#             vis_clfy_gen_par2_val = res.vis_clfy_gen_par2
#         if "vis_clfy_gen_par3" in bufferdata.keys():
#             if (res.vis_clfy_gen_par3 == bufferdata['vis_clfy_gen_par3']):
#                 vis_clfy_gen_par3_val = res.vis_clfy_gen_par3
#             else:
#                 vis_clfy_gen_par3_val = bufferdata['vis_clfy_gen_par3']
#         else:
#             vis_clfy_gen_par3_val = res.vis_clfy_gen_par3
#         if "vis_clfy_gen_par4" in bufferdata.keys():
#             if (res.vis_clfy_gen_par4 == bufferdata['vis_clfy_gen_par4']):
#                 vis_clfy_gen_par4_val = res.vis_clfy_gen_par4
#             else:
#                 vis_clfy_gen_par4_val = bufferdata['vis_clfy_gen_par4']
#         else:
#             vis_clfy_gen_par4_val = res. vis_clfy_gen_par4   
#         models.t_cebs_env.objects.filter(tup_lable = tup_lable_val).update(                       
#             workdir = workdir_val,pic_origin = pic_origin_val,pic_middle = pic_middle_val,holeboard_type = holeboard_type_val,\
#             holeboard_left_bot_x = holeboard_left_bot_x_val,holeboard_left_bot_y = holeboard_left_bot_y_val,holeboard_right_up_x = holeboard_right_up_x_val,\
#             holeboard_right_up_y = holeboard_right_up_y_val,pic_take_fix_point_set = pic_take_fix_point_set_val,pic_classification_set = pic_classification_set_val,\
#             pic_auto_work_after_start_set = pic_auto_work_after_start_set_val,pic_auto_work_tti = pic_auto_work_tti_val,vis_small_low_limit = vis_small_low_limit_val,\
#             vis_small_mid_limit = vis_small_mid_limit_val,vis_mid_big_limit = vis_mid_big_limit_val,vis_big_upper_limit = vis_big_upper_limit_val,vis_res_addup_set = vis_res_addup_set_val,\
#             vis_cap_enable_set = vis_cap_enable_set_val,vis_cap_dur_in_sec = vis_cap_dur_in_sec_val,vis_clfy_gen_par1 = vis_clfy_gen_par1_val,vis_clfy_gen_par2 = vis_clfy_gen_par2_val,\
#             vis_clfy_gen_par3 = vis_clfy_gen_par3_val,vis_clfy_gen_par4 = vis_clfy_gen_par4_val)         
#         return True 
# 
#     def dft_dbi_env_delete(self, inputData):
#         #print(inputData['tupLable']['workdir'])\
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         models.t_cebs_env.objects.filter(tup_lable = bufferdata['tupLable']).delete()
#         return True
# 
#     def dft_dbi_counter_add(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         print(bufferdata['picbatchcnt'])
#         if "tupLable" in bufferdata.keys():
#             tup_lable = bufferdata['tupLable']
#         else:
#             tup_lable = 0
#         if "picbatchcnt" in bufferdata.keys():
#             picbatchcnt_val = bufferdata['picbatchcnt']
#         else:
#             picbatchcnt_val = 0
#         if "picbatchclas" in bufferdata.keys():
#             picbatchclas_val = bufferdata['picbatchclas']
#         else:
#             picbatchclas_val = 0
#         if "picremaincnt" in bufferdata.keys():
#             picremaincnt_val = bufferdata['picremaincnt']
#         else:
#             picremaincnt_val = 0
#         if "picbatfluclas" in bufferdata.keys():
#             picbatfluclas_val = bufferdata['picbatfluclas']
#         else:
#             picbatfluclas_val = 0
#         if "picremflucnt" in bufferdata.keys():
#             picremflucnt_val = bufferdata['picremflucnt']
#         else:
#             picremflucnt_val = 0
#         
#         models.t_cebs_counter.objects.create(\
#             tup_lable=tup_lable,
#             picbatchcnt = picbatchcnt_val,picbatchclas = picbatchclas_val,\
#             picremaincnt = picremaincnt_val,picbatfluclas = picbatfluclas_val,\
#             picremflucnt = picremflucnt_val
#             )
#         return True
# 
#     def dft_dbi_counter_read(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         res = models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable'])
#         if res.exists():     
#             for line in res:
#                 res.tup_lable = line.tup_lable
#                 res.picbatchcnt = line.picbatchcnt  
#                 res.picbatchclas = line.picbatchclas
#                 res.picremaincnt = line.picremaincnt
#                 res.picbatfluclas = line.picbatfluclas
#                 res.picremflucnt = line.picremflucnt
#         else:
#             return False
#         bufferout= {}
#         if "picbatchcnt" in bufferdata.keys():
#             bufferout['picbatchcnt'] = res.picbatchcnt;
#         else:
#             pass
#         if "picbatchclas" in bufferdata.keys():
#             bufferout['picbatchclas'] = res.picbatchclas;
#         else:
#             pass
#         if "picremaincnt" in bufferdata.keys():
#             bufferout['picremaincnt'] = res.picremaincnt;
#         else:
#             pass
#         if "picbatfluclas" in bufferdata.keys():
#             bufferout['picbatfluclas'] = res.picbatfluclas;
#         else:
#             pass
#         if "picremflucnt" in bufferdata.keys():
#             bufferout['picremflucnt'] = res.picremflucnt;
#         else:
#             pass
#         
#         print(bufferout)
#         return bufferout
# 
#     def dft_dbi_counter_modify(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata) 
#         
#         res = models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable']) 
#         if res.exists():     
#             for line in res:
#                 res.tup_lable = line.tup_lable
#                 res.picbatchcnt = line.picbatchcnt  
#                 res.picbatchclas = line.picbatchclas
#                 res.picremaincnt = line.picremaincnt
#                 res.picbatfluclas = line.picbatfluclas
#                 res.picremflucnt = line.picremflucnt
#         else:
#             return False
#                
#         if "tupLable" in bufferdata.keys():
#             if (res.tup_lable == bufferdata['tupLable']):
#                 tup_lable_val = res.tup_lable
#             else:
#                 tup_lable_val = bufferdata['tupLable'] 
#         else:
#             tup_lable_val = res.tup_lable
#         if "picbatchcnt" in bufferdata.keys():
#             if (res.picbatchcnt == bufferdata['picbatchcnt']):
#                 picbatchcnt_val = res.picbatchcnt
#             else:
#                 picbatchcnt_val = bufferdata['picbatchcnt']
#         else:
#             picbatchcnt_val = res.picbatchcnt
#         if "picbatchclas" in bufferdata.keys():
#             if (res.picbatchclas == bufferdata['picbatchclas']):
#                 picbatchclas_val = res.picbatchclas
#             else:
#                 picbatchclas_val = bufferdata['picbatchclas']
#         else:
#             picbatchclas_val = res.picbatchclas
#         if "picremaincnt" in bufferdata.keys():
#             if (res.picremaincnt == bufferdata['picremaincnt']):
#                 picremaincnt_val = res.picremaincnt
#             else:
#                 picremaincnt_val = bufferdata['picremaincnt']
#         else:
#             picremaincnt_val = res.picremaincnt
#         if "picbatfluclas" in bufferdata.keys():
#             if (res.picbatfluclas == bufferdata['picbatfluclas']):
#                 picbatfluclas_val = res.picbatfluclas
#             else:
#                 picbatfluclas_val = bufferdata['picbatfluclas']
#         else:
#             picbatfluclas_val = res.picbatfluclas
#         if "picremflucnt" in bufferdata.keys():
#             if (res.picremflucnt == bufferdata['picremflucnt']):
#                 picremflucnt_val = res.picremflucnt
#             else:
#                 picremflucnt_val = bufferdata['picremflucnt']
#         else:
#             picremflucnt_val = res.picremflucnt 
#        
#         models.t_cebs_counter.objects.filter(tup_lable = tup_lable_val).update(\
#             tup_lable=tup_lable_val,
#             picbatchcnt = picbatchcnt_val,picbatchclas = picbatchclas_val,\
#             picremaincnt = picremaincnt_val,picbatfluclas = picbatfluclas_val,\
#             picremflucnt = picremflucnt_val
#             )
#         return True 
# 
#     def dft_dbi_counter_delete(self, inputData):
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         models.t_cebs_counter.objects.filter(tup_lable = bufferdata['tupLable']).delete()
#         return True
# 
#     def dft_dbi_fspc_add(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         if "tupLable" in bufferdata.keys():
#             tup_lable = bufferdata['tupLable']
#         else:
#             tup_lable = 0
#         if "mark_line" in bufferdata.keys():
#             mark_line_val = bufferdata['mark_line']
#         else:
#             mark_line_val = 0
#         if "mark_width" in bufferdata.keys():
#             mark_width_val = bufferdata['mark_width']
#         else:
#             mark_width_val = 0
#         if "mark_area" in bufferdata.keys():
#             mark_area_val = bufferdata['mark_area']
#         else:
#             mark_area_val = 0
#         if "mark_dilate" in bufferdata.keys():
#             mark_dilate_val = bufferdata['mark_dilate']
#         else:
#             mark_dilate_val = 0
#         if "area_square_min" in bufferdata.keys():
#             area_square_min_val = bufferdata['area_square_min']
#         else:
#             area_square_min_val = 0
#         if "area_squre_max" in bufferdata.keys():
#             area_squre_max_val = bufferdata['area_squre_max']
#         else:
#             area_squre_max_val = 0
#         if "area_dilate" in bufferdata.keys():
#             area_dilate_val = bufferdata['area_dilate']
#         else:
#             area_dilate_val = 0        
#         if "area_erode" in bufferdata.keys():
#             area_erode_val = bufferdata['area_erode']
#         else:
#             area_erode_val = 0
#         if "cell_square_min" in bufferdata.keys():
#             cell_square_min_val = bufferdata['cell_square_min']
#         else:
#             cell_square_min_val = 0
#         if "cell_square_max" in bufferdata.keys():
#             cell_square_max_val = bufferdata['cell_square_max']
#         else:
#             cell_square_max_val = 0
#         if "cell_raduis_min" in bufferdata.keys():
#             cell_raduis_min_val = bufferdata['cell_raduis_min']
#         else:
#             cell_raduis_min_val = 0
#         if "cell_raduis_max" in bufferdata.keys():
#             cell_raduis_max_val = bufferdata['cell_raduis_max']
#         else:
#             cell_raduis_max_val = 0
#         if "cell_dilate" in bufferdata.keys():
#             cell_dilate_val = bufferdata['cell_dilate']
#         else:
#             cell_dilate_val = 0
#         if "cell_erode" in bufferdata.keys():
#             cell_erode_val = bufferdata['cell_erode']
#         else:
#             cell_erode_val = 0
#         if "cell_ce" in bufferdata.keys():
#             cell_ce_val = bufferdata['cell_ce']
#         else:
#             cell_ce_val = 0
#         if "cell_distance" in bufferdata.keys():
#             cell_distance_val = bufferdata['cell_distance']
#         else:
#             cell_distance_val = 0
#         if "pic_train_delay" in bufferdata.keys():
#             pic_train_delay_val = bufferdata['pic_train_delay']
#         else:
#             pic_train_delay_val = 0
#         if "addup_set" in bufferdata.keys():
#             addup_set_val = bufferdata['addup_set']
#         else:
#             addup_set_val = False
#         
#         models.t_cebs_fspc.objects.create(\
#             tup_lable = tup_lable,
#             mark_line = mark_line_val,mark_width = mark_width_val,mark_area = mark_area_val,mark_dilate = mark_dilate_val,\
#             area_square_min = area_square_min_val,area_squre_max = area_squre_max_val,area_dilate = area_dilate_val,area_erode = area_erode_val,\
#             cell_square_min = cell_square_min_val,cell_square_max = cell_square_max_val,cell_raduis_min = cell_raduis_min_val,cell_raduis_max = cell_raduis_max_val,\
#             cell_dilate = cell_dilate_val,cell_erode = cell_erode_val,cell_ce = cell_ce_val,cell_distance = cell_distance_val,pic_train_delay = pic_train_delay_val,addup_set = addup_set_val)
#         return True
# 
#     def dft_dbi_fspc_read(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         res = models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable'])
#         
#         bufferout= {}
#         if "mark_line" in bufferdata.keys():
#             bufferout['mark_line'] = res[0].mark_line;
#         else:
#             pass
#         if "mark_width" in bufferdata.keys():
#             bufferout['mark_width'] = res[0].mark_width;
#         else:
#             pass
#         if "mark_area" in bufferdata.keys():
#             bufferout['mark_area'] = res[0].mark_area;
#         else:
#             pass
#         if "mark_dilate" in bufferdata.keys():
#             bufferout['mark_dilate'] = res[0].mark_dilate;
#         else:
#             pass
#         if "area_square_min" in bufferdata.keys():
#             bufferout['area_square_min'] = res[0].area_square_min;
#         else:
#             pass
#         if "area_squre_max" in bufferdata.keys():
#             bufferout['area_squre_max'] = res[0].area_squre_max;
#         else:
#             pass
#         if "area_dilate" in bufferdata.keys():
#             bufferout['area_dilate'] = res[0].area_dilate;
#         else:
#             pass
#         if "area_erode" in bufferdata.keys():
#             bufferout['area_erode'] = res[0].area_erode;
#         else:
#             pass
#         if "cell_square_min" in bufferdata.keys():
#             bufferout['cell_square_min'] = res[0].cell_square_min;
#         else:
#             pass
#         if "cell_square_max" in bufferdata.keys():
#             bufferout['cell_square_max'] = res[0].cell_square_max;
#         else:
#             pass
#         if "cell_raduis_min" in bufferdata.keys():
#             bufferout['cell_raduis_min'] = res[0].cell_raduis_min;
#         else:
#             pass
#         if "cell_raduis_max" in bufferdata.keys():
#             bufferout['cell_raduis_max'] = res[0].cell_raduis_max;
#         else:
#             pass
#         if "cell_dilate" in bufferdata.keys():
#             bufferout['cell_dilate'] = res[0].cell_dilate;
#         else:
#             pass
#         if "cell_erode" in bufferdata.keys():
#             bufferout['cell_erode'] = res[0].cell_erode;
#         else:
#             pass
#         if "cell_ce" in bufferdata.keys():
#             bufferout['cell_ce'] = res[0].cell_ce;
#         else:
#             pass
#         if "cell_distance" in bufferdata.keys():
#             bufferout['cell_distance'] = res[0].cell_distance;
#         else:
#             pass
#         if "pic_train_delay" in bufferdata.keys():
#             bufferout['pic_train_delay'] = res[0].pic_train_delay;
#         else:
#             pass
#         if "addup_set" in bufferdata.keys():
#             bufferout['addup_set'] = res[0].addup_set;
#         else:
#             pass
#         
#         print(bufferout)
#         return bufferout
# 
#     def dft_dbi_fspc_modify(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata) 
#         
#         res = models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable'])
#         if res.exists():
#             for line in res:
#                 res.tup_lable = line.tup_lable
#                 res.mark_line = line.mark_line  
#                 res.mark_width = line.mark_width
#                 res.mark_area = line.mark_area
#                 res.mark_dilate = line.mark_dilate
#                 res.area_square_min = line.area_square_min
#                 res.area_squre_max = line.area_squre_max
#                 res.area_dilate = line.area_dilate
#                 res.area_erode = line.area_erode
#                 res.cell_square_min = line.cell_square_min
#                 res.cell_square_max = line.cell_square_max
#                 res.cell_raduis_min = line.cell_raduis_min
#                 res.cell_raduis_max = line.cell_raduis_max
#                 res.cell_dilate = line.cell_dilate
#                 res.cell_erode = line.cell_erode
#                 res.cell_ce = line.cell_ce
#                 res.cell_distance = line.cell_distance
#                 res.pic_train_delay = line.pic_train_delay
#                 res.addup_set = line.addup_set
#         else:
#             return False    
#   
#         if "tupLable" in bufferdata.keys():
#             if (res.tup_lable == bufferdata['tupLable']):
#                 tup_lable_val = res.tup_lable
#             else:
#                 tup_lable_val = bufferdata['tuplable'] 
#         else:
#             tup_lable_val = res.tup_lable
#         if "mark_line" in bufferdata.keys():
#             if (res.mark_line == bufferdata['mark_line']):
#                 mark_line_val = res.mark_line
#             else:
#                 mark_line_val = bufferdata['mark_line']
#         else:
#             mark_line_val = res.mark_line
#         if "mark_width" in bufferdata.keys():
#             if (res.mark_width == bufferdata['mark_width']):
#                 mark_width_val = res.mark_width
#             else:
#                 mark_width_val = bufferdata['mark_width']
#         else:
#             mark_width_val = res.mark_width
#         if "mark_area" in bufferdata.keys():
#             if (res.mark_area == bufferdata['mark_area']):
#                 mark_area_val = res.mark_area
#             else:
#                 mark_area_val = bufferdata['mark_area']
#         else:
#             mark_area_val = res.mark_area
#         if "mark_dilate" in bufferdata.keys():
#             if (res.mark_dilate == bufferdata['mark_dilate']):
#                 mark_dilate_Val = res.mark_dilate
#             else:
#                 mark_dilate_val = bufferdata['mark_dilate']
#         else:
#             mark_dilate_val = res.mark_dilate
#         if "area_square_min" in bufferdata.keys():
#             if (res.area_square_min == bufferdata['area_square_min']):
#                 area_square_min_val = res.area_square_min
#             else:
#                 area_square_min_val = bufferdata['area_square_min']
#         else:
#             area_square_min_val = res.area_square_min 
#         if "area_squre_max" in bufferdata.keys():
#             if (res.area_squre_max == bufferdata['area_squre_max']):
#                 area_squre_max_val = res.area_squre_max
#             else:
#                 area_squre_max_val = bufferdata['area_squre_max']
#         else:
#             area_squre_max_val = res.area_squre_max
#         if "area_dilate" in bufferdata.keys():
#             if (res.area_dilate == bufferdata['area_dilate']):
#                 area_dilate_val = res.area_dilate
#             else:
#                 area_dilate_val = bufferdata['area_dilate']        
#         else:
#             area_dilate_val = res.area_dilate
#         if "area_erode" in bufferdata.keys():
#             if (res.area_erode == bufferdata['area_erode']):
#                 area_erode_val = res.area_erode
#             else:
#                 area_erode_val = bufferdata['area_erode']
#         else:
#             area_erode_val = res.area_erode
#         if "cell_square_min" in bufferdata.keys():
#             if (res.cell_square_min == bufferdata['cell_square_min']):
#                 cell_square_min_val = res.cell_square_min
#             else:
#                 cell_square_min_val = bufferdata['cell_square_min']
#         else:
#             cell_square_min_val = res.cell_square_min
#         if "cell_square_max" in bufferdata.keys():
#             if (res.cell_square_max == bufferdata['cell_square_max']):
#                 cell_square_max_val = res.cell_square_max
#             else:
#                 cell_square_max_val = bufferdata['cell_square_max']
#         else:
#             cell_square_max_val = res.cell_square_max
#         if "cell_raduis_min" in bufferdata.keys():
#             if (res.cell_raduis_min == bufferdata['cell_raduis_min']):
#                 cell_raduis_min_val = res.cell_raduis_min
#             else:
#                 cell_raduis_min_val = bufferdata['cell_raduis_min']
#         else:
#             cell_raduis_min_val = res.cell_raduis_min
#         if "cell_raduis_max" in bufferdata.keys():
#             if (res.cell_raduis_max == bufferdata['cell_raduis_max']):
#                 cell_raduis_max_val = res.cell_raduis_max
#             else:
#                 cell_raduis_max_val = bufferdata['cell_raduis_max']
#         else:
#             cell_raduis_max_val = res.cell_raduis_max
#         if "cell_dilate" in bufferdata.keys():
#             if (res.cell_dilate == bufferdata['cell_dilate']):
#                 cell_dilate_val = res.cell_dilate
#             else:
#                 cell_dilate_val = bufferdata['cell_dilate']
#         else:
#             cell_dilate_val = res.cell_dilate
#         if "cell_erode" in bufferdata.keys():
#             if (res.cell_erode == bufferdata['cell_erode']):
#                 cell_erode_val = res.cell_erode
#             else:
#                 cell_erode_val = bufferdata['cell_erode']
#         else:
#             cell_erode_val = res.cell_erode
#         if "cell_ce" in bufferdata.keys():
#             if (res.cell_ce == bufferdata['cell_ce']):
#                 cell_ce_val = res.cell_ce
#             else:
#                 cell_ce_val = bufferdata['cell_ce']
#         else:
#             cell_ce_val = res.cell_ce
#         if "cell_distance" in bufferdata.keys():
#             if (res.cell_distance == bufferdata['cell_distance']):
#                 cell_distance_val = res.cell_distance
#             else:
#                 cell_distance_val = bufferdata['cell_distance']
#         else:
#             cell_distance_val = res.cell_distance
#         if "pic_train_delay" in bufferdata.keys():
#             if (res.vis_res_addup_set == bufferdata['pic_train_delay']):
#                 pic_train_delay_val = res.pic_train_delay
#             else:
#                 pic_train_delay_val = bufferdata['pic_train_delay']
#         else:
#             pic_train_delay_val = res.pic_train_delay
#         if "addup_set" in bufferdata.keys():
#             if (res.addup_set == bufferdata['addup_set']):
#                 addup_set_val = res.addup_set
#             else:
#                 addup_set_val = bufferdata['addup_set']
#         else:
#             addup_set_val = res.addup_set
#           
#         models.t_cebs_fspc.objects.filter(tup_lable = tup_lable_val).update(                       
#             mark_line = mark_line_val,mark_width = mark_width_val,mark_area = mark_area_val,mark_dilate = mark_dilate_val,\
#             area_square_min = area_square_min_val,area_squre_max = area_squre_max_val,area_dilate = area_dilate_val,area_erode = area_erode_val,\
#             cell_square_min = cell_square_min_val,cell_square_max = cell_square_max_val,cell_raduis_min = cell_raduis_min_val,cell_raduis_max = cell_raduis_max_val,\
#             cell_dilate = cell_dilate_val,cell_erode = cell_erode_val,cell_ce = cell_ce_val,cell_distance = cell_distance_val,pic_train_delay = pic_train_delay_val,addup_set = addup_set_val)         
#         return True 
# 
#     def dft_dbi_fspc_delete(self, inputData):
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         models.t_cebs_fspc.objects.filter(tup_lable = bufferdata['tupLable']).delete()
#         return True
# 
#     def dft_dbi_file_add(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         if "batch_no" in bufferdata.keys():
#             batch_no_val = bufferdata['batch_no']
#         else:
#             batch_no_val = 0
#         if "hole_no" in bufferdata.keys():
#             hole_no_val = bufferdata['hole_no']
#         else:
#             hole_no_val = 0
#         if "hole_name" in bufferdata.keys():
#             hole_name_val = bufferdata['hole_name']
#         else:
#             hole_name_val = ''
#         if "pic_file_name" in bufferdata.keys():
#             pic_file_name_val = bufferdata['pic_file_name']
#         else:
#             pic_file_name_val = 0
#         if "file_att" in bufferdata.keys():
#             file_att_val = bufferdata['file_att']
#         else:
#             file_att_val = 'normal'
#         if "vid_file_name" in bufferdata.keys():
#             vid_file_name_val = bufferdata['vid_file_name']
#         else:
#             vid_file_name_val = 0
#         if "classified_flag" in bufferdata.keys():
#             classified_flag_val = bufferdata['classified_flag']
#         else:
#             classified_flag_val = False
#         if "video_flag" in bufferdata.keys():
#             video_flag_val = bufferdata['video_flag']
#         else:
#             video_flag_val = False
#         if "cfy_res" in bufferdata.keys():
#             cfy_res_val = bufferdata['cfy_res']
#         else:
#             cfy_res_val = ''
#         models.t_cebs_batch_file.objects.create(\
#             batch_no = batch_no_val,hole_no = hole_no_val,hole_name = hole_name_val,pic_file_name = pic_file_name_val,\
#             file_att = file_att_val,vid_file_name = vid_file_name_val,classified_flag = classified_flag_val,video_flag = video_flag_val,cfy_res = cfy_res_val
#             )
#         return True
# 
#     def dft_dbi_file_read(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         res = models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no'],hole_no = bufferdata['hole_no'])
#         bufferout= {}
#         if res.exists():
#             for line in res:
# #                 res.batch_no = line.batch_no
# #                 res.hole_no = line.hole_no
#                 res.hole_name = line.hole_name
#                 res.pic_file_name = line.pic_file_name
#                 res.file_att = line.file_att
#                 res.vid_file_name = line.vid_file_name
#                 res.classified_flag = line.classified_flag
#                 res.video_flag = line.video_flag
#                 res.cfy_res = line.cfy_res
#                 
#                 print(line.pic_file_name)
#                 print(res.pic_file_name)
#         else:
#             return False
# #         if "batch_no" in bufferdata.keys():
# #             bufferout['batch_no'] = res.batch_no;
# #         else:
# #             pass
# #         if "hole_no" in bufferdata.keys():
# #             bufferout['hole_no'] = res.hole_no;
# #         else:
# #             pass
#         if "hole_name" in bufferdata.keys():
#             bufferout['hole_name'] = res.hole_name
#         else:
#             pass
#         if "pic_file_name" in bufferdata.keys():
#             bufferout['pic_file_name'] = res.pic_file_name
#         else:
#             pass
#         if "file_att" in bufferdata.keys():
#             bufferout['file_att'] = res.file_att
#         else:
#             pass
#         if "vid_file_name" in bufferdata.keys():
#             bufferout['vid_file_name'] = res.vid_file_name
#         else:
#             pass
#         if "classified_flag" in bufferdata.keys():
#             bufferout['classified_flag'] = res.classified_flag
#         else:
#             pass
#         if "video_flag" in bufferdata.keys():
#             bufferout['video_flag'] = res.video_flag
#         else:
#             pass
#         if "cfy_res" in bufferdata.keys():
#             bufferout['cfy_res'] = res.cfy_res
#         else:
#             pass
#         
#         print(bufferout)
#         return bufferout
# 
# 
#     def dft_dbi_file_modify(self, inputData):
#         print(inputData)
#         bufferdata = inputData['tupLable']
#         print(bufferdata) 
#         
#         res = models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no'],hole_no = bufferdata['hole_no'])
#         if res.exists():
#             for line in res:
#                 res.batch_no = line.batch_no
#                 res.hole_no = line.hole_no  
#                 res.hole_name = line.hole_name
#                 res.pic_file_name = line.pic_file_name
#                 res.file_att = line.file_att
#                 res.vid_file_name = line.vid_file_name
#                 res.classified_flag = line.classified_flag
#                 res.video_flag = line.video_flag
#                 res.cfy_res = line.cfy_res
#         else:
#             return False
#         
#         if "batch_no" in bufferdata.keys():
#             if (res.batch_no == bufferdata['batch_no']):
#                 batch_no_val = res.batch_no
#             else:
#                 batch_no_val = bufferdata['batch_no'] 
#         else:
#             batch_no_val = res.batch_no
#         if "hole_no" in bufferdata.keys():
#             if (res.hole_no == bufferdata['hole_no']):
#                 hole_no_val = res.hole_no
#             else:
#                 hole_no_val = bufferdata['hole_no']
#         else:
#             hole_no_val = res.hole_no
#         if "hole_name" in bufferdata.keys():
#             if (res.hole_name == bufferdata['hole_name']):
#                 hole_name_val = res.hole_name
#             else:
#                 hole_name_val = bufferdata['hole_name']
#         else:
#             hole_name_val = res.hole_name
#         if "pic_file_name" in bufferdata.keys():
#             if (res.pic_file_name == bufferdata['pic_file_name']):
#                 pic_file_name_val = res.pic_file_name
#             else:
#                 pic_file_name_val = bufferdata['pic_file_name']
#         else:
#             pic_file_name_val = res.pic_file_name
#         if "file_att" in bufferdata.keys():
#             if (res.file_att == bufferdata['file_att']):
#                 file_att_val = res.file_att
#             else:
#                 file_att_val = bufferdata['file_att']
#         else:
#             file_att_val = res.file_att
#         if "vid_file_name" in bufferdata.keys():
#             if (res.vid_file_name == bufferdata['vid_file_name']):
#                 vid_file_name_val = res.vid_file_name
#             else:
#                 vid_file_name_val = bufferdata['vid_file_name']
#         else:
#             vid_file_name_val = res.vid_file_name 
#         if "classified_flag" in bufferdata.keys():
#             if (res.classified_flag == bufferdata['classified_flag']):
#                 classified_flag_val = res.classified_flag
#             else:
#                 classified_flag_val = bufferdata['classified_flag']
#         else:
#             classified_flag_val = res.classified_flag
#         if "video_flag" in bufferdata.keys():
#             if (res.video_flag == bufferdata['video_flag']):
#                 video_flag_val = res.video_flag
#             else:
#                 video_flag_val = bufferdata['video_flag']        
#         else:
#             video_flag_val = res.video_flag
#         if "cfy_res" in bufferdata.keys():
#             if (res.cfy_res == bufferdata['cfy_res']):
#                 cfy_res_val = res.cfy_res
#             else:
#                 cfy_res_val = bufferdata['cfy_res']
#         else:
#             cfy_res_val = res.cfy_res
#         models.t_cebs_batch_file.objects.filter(batch_no = batch_no_val,hole_no = hole_no_val).update(                       
#             hole_name = hole_name_val,pic_file_name = pic_file_name_val,\
#             file_att = file_att_val,vid_file_name = vid_file_name_val,classified_flag = classified_flag_val,video_flag = video_flag_val,cfy_res = cfy_res_val)         
#         return True 
# 
#     def dft_dbi_file_delete(self, inputData):
#         bufferdata = inputData['tupLable']
#         print(bufferdata)
#         models.t_cebs_batch_file.objects.filter(batch_no = bufferdata['batch_no'],hole_no = bufferdata['hole_no']).delete()
#         return True

    def __dft_getRandomSid(self,strlen):
        str_array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
        sid=''.join(random.sample(str_array,strlen))
        return sid
    def _dft_getRandomUid(self,strlen):
        str_array=['0','1','2','3','4','5','6','7','8','9']
        uid=''.join(random.sample(str_array,strlen))
        return uid
    
  #LC:add protection
    def dft_dbi_user_sheet_add(self, inputData):
        uid_val = "UID"+self._dft_getRandomUid(7)
        login_name_val = inputData['login_name']
        pass_word_val = inputData['pass_word']
        grade_level_val = inputData['grade_level']
        email_val = inputData['email']
        memo_val = inputData['memo']
        result = models.t_cebs_user_sheet.objects.filter(uid = uid_val)
        #print(result[0].login_name)
        if result.exists():
            self.dft_dbi_user_sheet_add(inputData)
        else:
            models.t_cebs_user_sheet.objects.create(
            uid = uid_val,login_name = login_name_val,pass_word = pass_word_val,
            grade_level = grade_level_val,email = email_val,memo = memo_val         
            )
            print("add user successful.")
            status={"status":"true","msg":"用户新建成功"}
            return status
    
    
    def dft_dbi_user_sheet_delete(self, inputData):
        uid = inputData['uid']
        models.t_cebs_user_sheet.objects.filter(uid = uid).delete()
        status={"status":"true","msg":"用户已删除"}
        return status
    
    #LC:add protection
    def dft_dbi_user_sheet_modify(self, inputData):
        uid = inputData['uid']
        result = models.t_cebs_user_sheet.objects.filter(uid = uid)
        if result.exists():
            if 'login_name' in inputData.keys():
                login_name_val = inputData['login_name']
            else:
                login_name_val = result[0].login_name
            if 'pass_word' in inputData.keys():
                pass_word_val = inputData['pass_word']
            else:
                pass_word_val = result[0].pass_word
            if 'grade_level' in inputData.keys():
                grade_level_val = inputData['grade_level']
            else:
                grade_level_val = result[0].grade_level
            if 'reg_date' in inputData.keys():
                reg_date_val = inputData['reg_date']
            else:
                reg_date_val = result[0].reg_date.strftime('%Y-%m-%d %H:%M:%S')
            if 'email' in inputData.keys():
                email_val = inputData['email']
            else:
                email_val = result[0].email
            if 'memo' in inputData.keys():
                memo_val = inputData['memo']
            else:
                memo_val = result[0].memo
            models.t_cebs_user_sheet.objects.filter(uid = uid).update(
                login_name = login_name_val,pass_word = pass_word_val,
                grade_level = grade_level_val,reg_date = reg_date_val,email = email_val,memo = memo_val  
                )
            resp={"status":"true","msg":"用户信息修改成功"}        
        else:
            resp={"status":"false","msg":"用户不存在，请检查信息"}
        return resp
    #LC:add protection
    def dft_dbi_user_sheet_read(self, inputData):
        uid = inputData['uid']
        bufferout = {}
        result = models.t_cebs_user_sheet.objects.filter(uid = uid)
        if result.exists():
            bufferout['login_name'] = result[0].login_name
            bufferout['pass_word'] = result[0].pass_word
            bufferout['grade_level'] = result[0].grade_level
            bufferout['reg_date'] = result[0].reg_date.strftime('%Y-%m-%d %H:%M:%S')
            bufferout['email'] = result[0].email
            bufferout['memo'] = result[0].memo
            resp={'status':'true','msg':'用户信息获取成功','data':bufferout}
#             return bufferout
        else:
            resp={'status':'false','msg':'用户不存在，请检查信息'}
        return resp
        
        
            
    def dft_dbi_product_profile_add(self, inputData):
        dev_code_val = inputData['dev_code']
        hw_ver_val= inputData['hw_ver']
        sw_ver_val = inputData['sw_ver']
        authtoken_val = inputData['authtoken']
        models.t_cebs_product_profile.objects.create(
            dev_code = dev_code_val, hw_ver = hw_ver_val,
            sw_ver = sw_ver_val,authtoken = authtoken_val
            )
        return True
    
    def dft_dbi_product_profile_delete(self, inputData):
        sid = inputData['id']
        models.t_cebs_product_profile.objects.filter(id = sid).delete()
        return True

    def dft_dbi_product_profile_modify(self, inputData):
        sid = inputData['id']
        result = models.t_cebs_product_profile.objects.filter(id = sid)
        if result.exists():
            if 'dev_code' in inputData.keys():
                dev_code_val = inputData['dev_code']
            else:
                dev_code_val = result[0].dev_code
            if 'hw_ver' in inputData.keys():
                hw_ver_val = inputData['hw_ver']
            else:
                hw_ver_val = result[0].hw_ver
            if 'sw_ver' in inputData.keys():
                sw_ver_val = inputData['sw_ver']
            else:
                sw_ver_val = result[0].sw_ver
            if 'authtoken' in inputData.keys():
                authtoken_val = inputData['authtoken']
            else:
                authtoken_val = result[0].authtoken
            if 'mfd' in inputData.keys():
                mfd_val = inputData['mfd']
            else:
                mfd_val = result[0].mfd.strftime('%Y-%m-%d %H:%M:%S')
            models.t_cebs_product_profile.objects.filter(id = sid).update(
                dev_code = dev_code_val, hw_ver = hw_ver_val,
                sw_ver = sw_ver_val,authtoken = authtoken_val,mfd = mfd_val,
                )
        return False
       
    def dft_dbi_product_profile_read(self, inputData):
        sid = inputData['id']
        bufferout = {}
        result = models.t_cebs_product_profile.objects.filter(id = sid)
        if result.exists():
            bufferout['dev_code'] = result[0].dev_code
            bufferout['hw_ver'] = result[0].hw_ver
            bufferout['sw_ver'] = result[0].sw_ver
            bufferout['authtoken'] = result[0].authtoken
            bufferout['mfd'] = result[0].mfd.strftime('%Y-%m-%d %H:%M:%S')
            print(bufferout)
            return bufferout
        
          
    def dft_dbi_cali_profile_add(self, inputData):
        platetype_val = inputData['platetype']
        left_bot_x_val = inputData['left_bot_x']
        left_bot_y_val = inputData['left_bot_y']
        right_up_x_val = inputData['right_up_x']
        right_up_y_val = inputData['right_up_y']
        # accspeed_val = inputData['accspeed']
        # print("11111")
        # print(inputData['accspeed'])
        # print(accspeed_val)
        # decspeed_val = inputData['decspeed']
        # movespeed_val = inputData['movespeed']
        # zero_spd_val = inputData['zero_spd']
        # zero_dec_val = inputData['zero_dec']
        # back_step_val = inputData['back_step']
#         foreignkeyname = inputData['uid']
#         print(inputData)
#         print(foreignkeyname)
        result = models.t_cebs_cali_profile.objects.all()
        #print(result[0].login_name)
        if result.exists():
            pass
            #print(uid_val)
        #注意：子表中得加id    
        else:
            # models.t_cebs_cali_profile.objects.create(
            #     platetype = platetype_val, uid_id = foreignkeyname, left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
            #     right_up_x = right_up_x_val, right_up_y = right_up_y_val, accspeed = accspeed_val,
            #     decspeed = decspeed_val, movespeed = movespeed_val, zero_spd = zero_spd_val,
            #     zero_dec = zero_dec_val, back_step = back_step_val
            #     )
            models.t_cebs_cali_profile.objects.create(
                platetype = platetype_val, left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
                right_up_x = right_up_x_val, right_up_y = right_up_y_val
                )
        return True
    
    def dft_dbi_cali_profile_delete(self, inputData):    
        sid = inputData['id']
        models.t_cebs_cali_profile.objects.filter(id = sid).delete()
        return True
    
    
    def dft_dbi_cali_profile_modify(self, inputData): 
        sid = inputData['id']
        result = models.t_cebs_cali_profile.objects.filter(id = sid)
        if result.exists():
            if 'platetype' in inputData.keys():
                platetype_val = inputData['platetype']
            else:
                platetype_val = result[0].platetype
            if 'calitime' in inputData.keys():
                calitime_val = inputData['calitime']
            else:
                calitime_val = result[0].calitime.strftime('%Y-%m-%d %H:%M:%S')
            if 'left_bot_x' in inputData.keys():
                left_bot_x_val = inputData['left_bot_x']
            else:
                left_bot_x_val = result[0].left_bot_x
            if 'left_bot_y' in inputData.keys():
                left_bot_y_val = inputData['left_bot_y']
            else:
                left_bot_y_val = result[0].left_bot_y
            if 'right_up_x' in inputData.keys():
                right_up_x_val = inputData['right_up_x']
            else:
                right_up_x_val = result[0].right_up_x
            if 'right_up_y' in inputData.keys():
                right_up_y_val = inputData['right_up_y']
            else:
                right_up_y_val = result[0].right_up_y
            # if 'accspeed' in inputData.keys():
            #     accspeed_val = inputData['accspeed']
            # else:
            #     accspeed_val = result[0].accspeed
            # if 'decspeed' in inputData.keys():
            #     decspeed_val = inputData['decspeed']
            # else:
            #     decspeed_val = result[0].decspeed
            # if 'movespeed' in inputData.keys():
            #     movespeed_val = inputData['movespeed']
            # else:
            #     movespeed_val = result[0].movespeed
            # if 'zero_spd' in inputData.keys():
            #     zero_spd_val = inputData['zero_spd']
            # else:
            #     zero_spd_val = result[0].zero_spd
            # if 'zero_dec' in inputData.keys():
            #     zero_dec_val = inputData['zero_dec']
            # else:
            #     zero_dec_val = result[0].zero_dec
            # if 'back_step' in inputData.keys():
            #     back_step_val = inputData['back_step']
            # else:
            #     back_step_val = result[0].back_step   
                        
            # models.t_cebs_cali_profile.objects.filter(id = sid).update(
            #     platetype = platetype_val,calitime = calitime_val, left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
            #     right_up_x = right_up_x_val, right_up_y = right_up_y_val, accspeed = accspeed_val,
            #     decspeed = decspeed_val, movespeed = movespeed_val, zero_spd = zero_spd_val,
            #     zero_dec = zero_dec_val, back_step = back_step_val
            #     )

            models.t_cebs_cali_profile.objects.filter(id = sid).update(
                platetype = platetype_val,calitime = calitime_val, left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
                right_up_x = right_up_x_val, right_up_y = right_up_y_val
                )
        return False
        
    def dft_dbi_cali_profile_read(self, inputData):  
        sid = inputData['id']
        bufferout = {}
        result = models.t_cebs_cali_profile.objects.filter(id = sid)
        if result.exists():
            bufferout['platetype'] = result[0].platetype
            bufferout['calitime'] = result[0].calitime.strftime('%Y-%m-%d %H:%M:%S')
            bufferout['uid'] = result[0].uid_id
            bufferout['left_bot_x'] = result[0].left_bot_x
            bufferout['left_bot_y'] = result[0].left_bot_y
            bufferout['right_up_x'] = result[0].right_up_x
            bufferout['right_up_y'] = result[0].right_up_y
            # bufferout['accspeed'] = result[0].accspeed
            # bufferout['decspeed'] = result[0].decspeed
            # bufferout['movespeed'] = result[0].movespeed
            # bufferout['zero_spd'] = result[0].zero_spd
            # bufferout['zero_dec'] = result[0].zero_dec
            # bufferout['back_step'] = result[0].back_step
            print(bufferout)
            return bufferout
                     
    def dft_dbi_object_profil_add(self, inputData):
        defaultflag_val = inputData['defaultflag']
        objname_val = inputData['objname']
        objtype_val = inputData['objtype']
        dir_origin_val = inputData['dir_origin']
        dir_middle_val = inputData['dir_middle']
        memo_val = inputData['memo']
        foreignkeyname = inputData['uid']
        result = models.t_cebs_user_sheet.objects.filter(uid = foreignkeyname)
        if result.exists():
            uid_val = result[0].uid
        models.t_cebs_object_profile.objects.create(
            objname = objname_val, objtype = objtype_val, uid_id = uid_val, dir_origin = dir_origin_val,
            dir_middle = dir_middle_val,memo = memo_val,defaultflag = defaultflag_val
            )
        return True
    
    def dft_dbi_object_profile_delete(self, inputData):
        objid = inputData['objid']
        models.t_cebs_object_profile.objects.filter(objid = objid).delete()
        return True   
    
    def dft_dbi_object_profile_modify(self, inputData):
        objid = inputData['objid']
        result = models.t_cebs_object_profile.objects.filter(objid = objid)
        if result.exists():
            if 'defaultflag' in inputData.keys():
                defaultflag_val = inputData['defaultflag']
            else:
                defaultflag_val = result[0].defaultflag
            if 'objname' in inputData.keys():
                objname_val = inputData['objname']
            else:
                objname_val = result[0].objname
            if 'objtype' in inputData.keys():
                objtype_val = inputData['objtype']
            else:
                objtype_val = result[0].objtype
            if 'dir_origin' in inputData.keys():
                dir_origin_val = inputData['dir_origin']
            else:
                dir_origin_val = result[0].dir_origin
            if 'dir_middle' in inputData.keys():
                dir_middle_val = inputData['dir_middle']
            else:
                dir_middle_val = result[0].dir_middle
            if 'memo' in inputData.keys():
                memo_val = inputData['memo']
            else:
                memo_val = result[0].memo
            models.t_cebs_object_profile.objects.filter(objid = objid).update(
                objname = objname_val, objtype = objtype_val, dir_origin = dir_origin_val,
                dir_middle = dir_middle_val,memo = memo_val,defaultflag = defaultflag_val
                )
        return False
    
    def dft_dbi_object_profile_read(self, inputData):
        objid = inputData['objid']
        bufferout = {}
        result = models.t_cebs_object_profile.objects.filter(objid = objid)
        if result.exists():
            bufferout['defaultflag'] = result[0].defaultflag
            bufferout['objname'] = result[0].objname
            bufferout['objtype'] = result[0].objtype
            bufferout['uid'] = result[0].uid_id
            bufferout['dir_origin'] = result[0].dir_origin
            bufferout['dir_middle'] = result[0].dir_middle
            bufferout['memo'] = result[0].memo
            print(bufferout)
            return bufferout
                   
                 
    def dft_dbi_config_eleg_add(self, inputData):
        fixpoint_val = inputData['fixpoint']
        autoexpo_val = inputData["autoexpo"]
        autoexpo_val = inputData["autoexpo"]
        autovideo_val = inputData['autovideo']
        autodist_val = inputData['autodist']
        addset_val = inputData['addset']
        autocap_val = inputData['autocap']
        autoperiod_val = inputData['autoperiod']
        videotime_val = inputData['videotime']
        slimit_val = inputData['slimit']
        smlimit_val = inputData['smlimit']
        mblimit_val = inputData['mblimit']
        blimit_val = inputData['blimit']
        accspeed_val = inputData['accspeed']
        decspeed_val = inputData['decspeed']
        movespeed_val = inputData['movespeed']
        zero_spd_val = inputData['zero_spd']
        zero_dec_val = inputData['zero_dec']
        back_step_val = inputData['back_step']
        foreignkeyname = inputData['objid']
        print(foreignkeyname)
        #关联到别的表单就要加  _id   只能锁定上表的主键
        result = models.t_cebs_object_profile.objects.filter(objid = foreignkeyname)
        if result.exists():
            objid_val = result[0].objid
        models.t_cebs_config_eleg.objects.create(
            objid_id = objid_val, fixpoint = fixpoint_val,autoexpo = autoexpo_val, autovideo = autovideo_val, autodist = autodist_val,
            addset = addset_val, autocap = autocap_val, autoperiod = autoperiod_val, videotime = videotime_val,
            slimit = slimit_val, smlimit =smlimit_val, mblimit = mblimit_val, blimit = blimit_val,
            accspeed = accspeed_val, decspeed = decspeed_val, movespeed = movespeed_val,
            zero_spd = zero_spd_val, zero_dec = zero_dec_val, back_step  = back_step_val
            )
        return True

    def dft_dbi_config_eleg_read(self, inputData):
        confid = inputData['confid']
        bufferout = {}
        result = models.t_cebs_config_eleg.objects.filter(confid = confid) 
        if result.exists():
            bufferout['objid'] = result[0].objid_id
            bufferout['fixpoint'] = result[0].fixpoint
            bufferout["autoexpo"] = result[0].autoexpo
            bufferout['autovideo'] = result[0].autovideo
            bufferout['autodist'] = result[0].autodist
            bufferout['addset'] = result[0].addset
            bufferout['autocap'] = result[0].autocap
            bufferout['autoperiod'] = result[0].autoperiod
            bufferout['videotime'] = result[0].videotime
            bufferout['slimit'] = result[0].slimit
            bufferout['smlimit'] = result[0].smlimit
            bufferout['mblimit'] = result[0].mblimit
            bufferout['blimit'] = result[0].blimit
            bufferout['accspeed'] = result[0].accspeed
            bufferout['decspeed'] = result[0].decspeed
            bufferout['movespeed'] = result[0].movespeed
            bufferout['zero_spd'] = result[0].zero_spd
            bufferout['zero_dec'] = result[0].zero_dec
            bufferout['back_step'] = result[0].back_step
            print(bufferout)
            return bufferout
        
    def dft_dbi_config_eleg_delete(self, inputData):
        confid = inputData['confid']
        models.t_cebs_config_eleg.objects.filter(confid = confid).delete()
        return True   
 
    def dft_dbi_config_eleg_modify(self, inputData):     
        confid = inputData['confid']    
        result = models.t_cebs_config_eleg.objects.filter(confid = confid)
        if result.exists():
            if 'fixpoint' in inputData.keys():
                fixpoint_val = inputData['fixpoint']
            else:
                fixpoint_val = result[0].fixpoint  
            if "autoexpo" in inputData.keys():
                autoexpo_val = inputData["autoexpo"]
            else:
                autoexpo_val = inputData["autoexpo"]
            if 'autovideo' in inputData.keys():
                autovideo_val = inputData['autovideo']
            else:
                autovideo_val = result[0].autovideo 
            if 'autodist' in inputData.keys():
                autodist_val = inputData['autodist']
            else:
                autodist_val = result[0].autodist
            if 'addset' in inputData.keys():
                addset_val = inputData['addset']
            else:
                addset_val = result[0].addset
            if 'autocap' in inputData.keys():
                autocap_val = inputData['autocap']
            else:
                autocap_val = result[0].autocap
            if 'autoperiod' in inputData.keys():
                autoperiod_val = inputData['autoperiod']
            else:
                autoperiod_val = result[0].autoperiod
            if 'videotime' in inputData.keys():
                videotime_val = inputData['videotime']
            else:
                videotime_val = result[0].videotime
            if 'slimit' in inputData.keys():
                slimit_val = inputData['slimit']
            else:
                slimit_val = result[0].slimit
            if 'smlimit' in inputData.keys():
                smlimit_val = inputData['smlimit']
            else:
                smlimit_val = result[0].smlimit
            if 'mblimit' in inputData.keys():
                mblimit_val = inputData['mblimit']
            else:
                mblimit_val = result[0].mblimit
            if 'blimit' in inputData.keys():
                blimit_val = inputData['blimit']
            else:
                blimit_val = result[0].blimit
            if 'accspeed' in inputData.keys():
                accspeed_val = inputData['accspeed']
            else:
                accspeed_val = result[0].accspeed
            if 'decspeed' in inputData.keys():
                decspeed_val = inputData['decspeed']
            else:
                decspeed_val = result[0].decspeed
            if 'movespeed' in inputData.keys():
                movespeed_val = inputData['movespeed']
            else:
                movespeed_val = result[0].movespeed
            if 'zero_spd' in inputData.keys():
                zero_spd_val = inputData['zero_spd']
            else:
                zero_spd_val = result[0].zero_spd
            if 'zero_dec' in inputData.keys():
                zero_dec_val = inputData['zero_dec']
            else:
                zero_dec_val = result[0].zero_dec
            if 'back_step' in inputData.keys():
                back_step_val = inputData['back_step']
            else:
                back_step_val = result[0].back_step 

            models.t_cebs_config_eleg.objects.filter(confid = confid).update(
                fixpoint = fixpoint_val,autoexpo = autoexpo_val, autovideo = autovideo_val, autodist = autodist_val,
                addset = addset_val, autocap = autocap_val, autoperiod = autoperiod_val, videotime = videotime_val,
                slimit = slimit_val, smlimit =smlimit_val, mblimit = mblimit_val, blimit = blimit_val,
                accspeed = accspeed_val,decspeed = decspeed_val, movespeed = movespeed_val,
                zero_spd = zero_spd_val,zero_dec = zero_dec_val, back_step = back_step_val
                )
        return False    
    
    def dft_dbi_config_stackcell_add(self, inputData):
        addset_val = inputData['addset']  
        line_area_val = inputData['line_area']
        line_width_val = inputData['line_width']
        line_long_val = inputData['line_long']
        line_dilate_val = inputData['line_dilate']
        area_up_val = inputData['area_up']
        area_low_val = inputData['area_low']
        area_dilate_val = inputData['area_dilate']
        area_erode_val = inputData['area_erode']
        square_min_val = inputData['square_min']
        square_max_val = inputData['square_max']
        radius_min_val = inputData['radius_min']
        radius_max_val = inputData['radius_max']
        cell_dilate_val = inputData['cell_dilate']
        cell_erode_val = inputData['cell_erode']
        cell_round_val = inputData['cell_round']
        cell_distance_val = inputData['cell_distance']
        train_delay_val = inputData['train_delay']
        foreignkeyname = inputData['objid']
        print(foreignkeyname)
        result = models.t_cebs_object_profile.objects.filter(objid = foreignkeyname)
        if result.exists():
            objid_val = result[0].objid
        models.t_cebs_config_stackcell.objects.create(
            objid_id = objid_val, addset = addset_val, line_area = line_area_val, line_width = line_width_val, line_long = line_long_val,
            line_dilate = line_dilate_val, area_up = area_up_val,  area_low = area_low_val, area_dilate = area_dilate_val,
            area_erode = area_erode_val, square_min = square_min_val, square_max = square_max_val, radius_min= radius_min_val,
            radius_max = radius_max_val, cell_dilate = cell_dilate_val, cell_erode = cell_erode_val, cell_round = cell_round_val,
            cell_distance = cell_distance_val,train_delay = train_delay_val
            )  
        return True

    def dft_dbi_config_stackcell_delete(self, inputData):    
        confid = inputData['confid']
        models.t_cebs_config_stackcell.objects.filter(confid = confid).delete()
        return True

    def dft_dbi_config_stackcell_modify(self, inputData):
        print(inputData)
        confid = inputData['confid']
        result = models.t_cebs_config_stackcell.objects.filter(confid = confid)
        if result.exists():
            if 'addset' in inputData.keys():
                addset_val = inputData['addset']
            else:
                addset_val = result[0].addset
            if 'line_area' in inputData.keys():
                line_area_val = inputData['line_area']
            else:
                line_area_val = result[0].line_area
            if 'line_width' in inputData.keys():
                line_width_val = inputData['line_width']
            else:
                line_width_val = result[0].line_width           
            if 'line_long' in inputData.keys():
                line_long_val = inputData['line_long']
            else:
                line_long_val = result[0].line_long
            if 'line_dilate' in inputData.keys():
                line_dilate_val = inputData['line_dilate']
            else:
                line_dilate_val = result[0].line_dilate    
            if 'area_up' in inputData.keys():
                area_up_val = inputData['area_up']
            else:
                area_up_val = result[0].area_up   
            if 'area_low' in inputData.keys():
                area_low_val = inputData['area_low']
            else:
                area_low_val = result[0].area_low
            if 'area_dilate' in inputData.keys():
                area_dilate_val = inputData['area_dilate']
            else:
                area_dilate_val = result[0].area_dilate
            if 'area_erode' in inputData.keys():
                area_erode_val = inputData['area_erode']
            else:
                area_erode_val = result[0].area_erode 
            if 'square_min' in inputData.keys():
                square_min_val = inputData['square_min']
            else:
                square_min_val = result[0].square_min 
            if 'square_max' in inputData.keys():
                square_max_val = inputData['square_max']
            else:
                square_max_val = result[0].square_max 
            if 'radius_min' in inputData.keys():
                radius_min_val = inputData['radius_min']
            else:
                radius_min_val = result[0].radius_min 
            if 'radius_max' in inputData.keys():
                radius_max_val = inputData['radius_max']
            else:
                radius_max_val = result[0].radius_max 
            if 'cell_dilate' in inputData.keys():
                cell_dilate_val = inputData['cell_dilate']
            else:
                cell_dilate_val = result[0].cell_dilate 
            if 'cell_erode' in inputData.keys():
                cell_erode_val = inputData['cell_erode']
            else:
                cell_erode_val = result[0].cell_erode    
            if 'cell_round' in inputData.keys():
                cell_round_val = inputData['cell_round']
            else:
                cell_round_val = result[0].cell_round
            if 'cell_distance' in inputData.keys():
                cell_distance_val = inputData['cell_distance']
            else:
                cell_distance_val = result[0].cell_distance
            if 'train_delay_val' in inputData.keys():
                train_delay_val = inputData['train_delay']
            else:
                train_delay_val = result[0].train_delay
            models.t_cebs_config_stackcell.objects.filter(confid = confid).update(
                addset = addset_val,  line_area = line_area_val, line_width = line_width_val, line_long = line_long_val,
                line_dilate = line_dilate_val, area_up = area_up_val,  area_low = area_low_val, area_dilate = area_dilate_val,
                area_erode = area_erode_val, square_min = square_min_val, square_max = square_max_val, radius_min= radius_min_val,
                radius_max = radius_max_val, cell_dilate = cell_dilate_val, cell_erode = cell_erode_val, cell_round = cell_round_val,
                cell_distance = cell_distance_val,train_delay = train_delay_val            
                )    
        else:
            return False   
    def dft_dbi_config_stackcell_read(self, inputData):
        confid = inputData['confid']
        bufferout = {}
        result = models.t_cebs_config_stackcell.objects.filter(confid = confid) 
        if result.exists():
            bufferout['objid'] = result[0].objid_id
            bufferout['addset'] = result[0].addset
            bufferout['line_area'] = result[0].line_area
            bufferout['line_width'] = result[0].line_width
            bufferout['line_long'] = result[0].line_long
            bufferout['line_dilate'] = result[0].line_dilate
            bufferout['area_up'] = result[0].area_up
            bufferout['area_low'] = result[0].area_low
            bufferout['area_dilate'] = result[0].area_dilate
            bufferout['area_erode'] = result[0].area_erode
            bufferout['square_min'] = result[0].square_min
            bufferout['square_max'] = result[0].square_max
            bufferout['radius_min'] = result[0].radius_min
            bufferout['radius_max'] = result[0].radius_max
            bufferout['cell_dilate'] = result[0].cell_dilate
            bufferout['cell_erode'] = result[0].cell_erode
            bufferout['cell_round'] = result[0].cell_round
            bufferout['cell_distance'] = result[0].cell_distance
            bufferout['train_delay'] = result[0].train_delay
            print(bufferout)
            return bufferout    
        
        
    def dft_dbi_result_eleg_add(self, inputData):
        snbatch_val = inputData['snbatch']
        snhole_val = inputData['snhole'] 
        file_attr_val = inputData['file_attr'] 
        name_before_val = inputData['name_before'] 
        name_after_val = inputData['name_after'] 
        bigalive_val = inputData['bigalive'] 
        bigdead_val = inputData['bigdead'] 
        midalive_val = inputData['midalive'] 
        middead_val = inputData['middead'] 
        smaalive_val = inputData['smaalive'] 
        smdead_val = inputData['smdead'] 
        totalalive_val = inputData['totalalive'] 
        totaldead_val = inputData['totaldead'] 
        totalsum_val = inputData['totalsum'] 
        doneflag_val = inputData['doneflag'] 
        memo_val = inputData['memo'] 
        foreignkeyname = inputData['confid'] 
        print(foreignkeyname)
        result = models.t_cebs_object_profile.objects.filter(objid = foreignkeyname)
        if result.exists():
            confid_val = result[0].objid
        models.t_cebs_result_eleg.objects.create(
            confid_id = confid_val, snbatch = snbatch_val, snhole = snhole_val, file_attr = file_attr_val, name_before = name_before_val,
            name_after = name_after_val, bigalive = bigalive_val, bigdead = bigdead_val, midalive = midalive_val, middead = middead_val,
            smaalive = smaalive_val, smdead = smdead_val,totalalive = totalalive_val, totaldead = totaldead_val, totalsum = totalsum_val, 
            doneflag = doneflag_val, memo = memo_val
            )           
        return True
    
    def dft_dbi_result_eleg_delete(self, inputData):
        sid = inputData['sid']
        models.t_cebs_result_eleg.objects.filter(sid = sid).delete()
        return True

    def dft_dbi_result_eleg_modify(self, inputData):
        print(inputData)
        sid = inputData['sid']
        result = models.t_cebs_result_eleg.objects.filter(sid = sid)
        if result.exists():
#             if 'confid_id' in inputData.keys():
#                 confid_val = inputData['confid_id']
#             else:
#                 confid_val = result[0].confid_id        
            if 'snbatch' in inputData.keys():
                snbatch_val = inputData['snbatch']
            else:
                snbatch_val = result[0].snbatch
            if 'snhole' in inputData.keys():
                snhole_val = inputData['snhole']
            else:
                snhole_val = result[0].snhole
            if 'file_attr' in inputData.keys():
                file_attr_val = inputData['file_attr']
            else:
                file_attr_val = result[0].file_attr           
            if 'name_before' in inputData.keys():
                name_before_val = inputData['name_before']
            else:
                name_before_val = result[0].name_before
            if 'cap_time' in inputData.keys():
                cap_time_val = inputData['cap_time']
            else:
                cap_time_val = result[0].cap_time    
            if 'name_after' in inputData.keys():
                name_after_val = inputData['name_after']
            else:
                name_after_val = result[0].name_after   
            if 'rec_time' in inputData.keys():
                rec_time_val = inputData['rec_time']
            else:
                rec_time_val = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S')
            if 'bigalive' in inputData.keys():
                bigalive_val = inputData['bigalive']
            else:
                bigalive_val = result[0].bigalive
            if 'bigdead' in inputData.keys():
                bigdead_val = inputData['bigdead']
            else:
                bigdead_val = result[0].bigdead 
            if 'midalive' in inputData.keys():
                midalive_val = inputData['midalive']
            else:
                midalive_val = result[0].midalive 
            if 'middead' in inputData.keys():
                middead_val = inputData['middead']
            else:
                middead_val = result[0].middead 
            if 'smaalive' in inputData.keys():
                smaalive_val = inputData['smaalive']
            else:
                smaalive_val = result[0].smaalive 
            if 'smdead' in inputData.keys():
                smdead_val = inputData['smdead']
            else:
                smdead_val = result[0].smdead 
            if 'totalalive' in inputData.keys():
                totalalive_val = inputData['totalalive']
            else:
                totalalive_val = result[0].totalalive 
            if 'totaldead' in inputData.keys():
                totaldead_val = inputData['totaldead']
            else:
                totaldead_val = result[0].totaldead    
            if 'totalsum' in inputData.keys():
                totalsum_val = inputData['totalsum']
            else:
                totalsum_val = result[0].totalsum
            if 'doneflag' in inputData.keys():
                doneflag_val = inputData['doneflag']
            else:
                doneflag_val = result[0].doneflag
            if 'memo' in inputData.keys():
                memo_val = inputData['memo']
            else:
                memo_val = result[0].memo
            models.t_cebs_result_eleg.objects.filter(sid =sid).update(
                snbatch = snbatch_val, snhole = snhole_val, file_attr = file_attr_val, name_before = name_before_val,cap_time = cap_time_val,
                name_after = name_after_val, rec_time = rec_time_val,bigalive = bigalive_val, bigdead = bigdead_val, midalive = midalive_val, middead = middead_val,
                smaalive = smaalive_val, smdead = smdead_val,totalalive = totalalive_val, totaldead = totaldead_val, totalsum = totalsum_val, 
                doneflag = doneflag_val, memo = memo_val
                )  
        else:           
            return False
        
        
    def dft_dbi_result_eleg_read(self, inputData):
        sid = inputData['sid']
        bufferout= {}
        result = models.t_cebs_result_eleg.objects.filter(sid = sid)
        if result.exists():
            bufferout['confid'] = result[0].confid_id
            bufferout['snbatch'] = result[0].snbatch
            bufferout['snhole'] = result[0].snhole
            bufferout['name_before'] = result[0].name_before
            bufferout['cap_time'] = result[0].cap_time.strftime('%Y-%m-%d %H:%M:%S') 
            bufferout['name_after'] = result[0].name_after
            bufferout['rec_time'] = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S') 
            bufferout['bigalive'] = result[0].bigalive
            bufferout['bigdead'] = result[0].bigdead  
            bufferout['midalive'] = result[0].midalive 
            bufferout['middead'] = result[0].middead 
            bufferout['smaalive'] = result[0].smaalive 
            bufferout['smdead'] = result[0].smdead 
            bufferout['totalalive'] = result[0].totalalive 
            bufferout['totaldead'] = result[0].totaldead 
            bufferout['totalsum'] = result[0].totalsum 
            bufferout['doneflag'] = result[0].doneflag 
            bufferout['memo'] = result[0].memo 
            print(bufferout)
            return bufferout 
                   
                  
    def dft_dbi_result_stackcell_add(self, inputData):
        file_attr_val = inputData['file_attr'] 
        name_before_val = inputData['name_before'] 
        name_after_val = inputData['name_after'] 
        totalnbr_val = inputData['totalnbr']   
        validnbr_val = inputData['validnbr'] 
        doneflag_val = inputData['doneflag'] 
        memo_val = inputData['memo'] 
        foreignkeyname = inputData['confid'] 
        print(foreignkeyname)
        result = models.t_cebs_object_profile.objects.filter(objid = foreignkeyname)
        if result.exists():
            confid_val = result[0].objid
        models.t_cebs_result_stackcell.objects.create(
            confid_id = confid_val,file_attr = file_attr_val, name_before = name_before_val, name_after = name_after_val,
            totalnbr = totalnbr_val, validnbr = validnbr_val, doneflag = doneflag_val, memo = memo_val              
            )
        return True
    
    def dft_dbi_result_stackcell_delete(self, inputData):   
        sid = inputData['sid']
        models.t_cebs_result_stackcell.objects.filter(sid = sid).delete()         
        return True

    def dft_dbi_result_stackcell_modify(self, inputData):
        print(inputData)
        sid = inputData['sid']
        result = models.t_cebs_result_stackcell.objects.filter(sid = sid)
        if result.exists():
#             if 'confid_id' in inputData.keys():
#                 confid_val = inputData['confid_id']
#             else:
#                 confid_val = result[0].confid_id        
            if 'file_attr' in inputData.keys():
                file_attr_val = inputData['file_attr']
            else:
                file_attr_val = result[0].file_attr
            if 'name_before' in inputData.keys():
                name_before_val = inputData['name_before']
            else:
                name_before_val = result[0].name_before
            if 'name_after' in inputData.keys():
                name_after_val = inputData['name_after']
            else:
                name_after_val = result[0].name_after           
            if 'rec_time' in inputData.keys():
                rec_time_val = inputData['rec_time']
            else:
                rec_time_val = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S')
            if 'totalnbr' in inputData.keys():
                totalnbr_val = inputData['totalnbr']
            else:
                totalnbr_val = result[0].totalnbr    
            if 'validnbr' in inputData.keys():
                validnbr_val = inputData['validnbr']
            else:
                validnbr_val = result[0].validnbr   
            if 'doneflag' in inputData.keys():
                doneflag_val = inputData['doneflag']
            else:
                doneflag_val = result[0].doneflag 
            if 'memo' in inputData.keys():
                memo_val = inputData['memo']
            else:
                memo_val = result[0].memo   
            models.t_cebs_result_stackcell.objects.filter(sid =sid).update(
                file_attr = file_attr_val, name_before = name_before_val, name_after = name_after_val,rec_time = rec_time_val,
                totalnbr = totalnbr_val, validnbr = validnbr_val, doneflag = doneflag_val, memo = memo_val
                )  
        else:           
            return False        
            
    #this read operation api will return all the data in this row         
    def dft_dbi_result_stackcell_read(self, inputData):            
        sid = inputData['sid']
        bufferout= {}
        result = models.t_cebs_result_stackcell.objects.filter(sid = sid)
        if result.exists():
            bufferout['confid'] = result[0].confid_id
            bufferout['file_attr'] = result[0].file_attr 
            bufferout['name_before'] = result[0].name_before
            bufferout['name_after'] = result[0].name_after
            bufferout['rec_time'] = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S') 
            bufferout['totalnbr'] = result[0].totalnbr
            bufferout['validnbr'] = result[0].validnbr
            bufferout['doneflag'] = result[0].doneflag
            bufferout['memo'] = result[0].memo
            print(bufferout)
            return bufferout
    
    #here leave a demo for return the value you only need, not all the data return
    def dft_dbi_result_stackcell_read_input(self, inputData):
        sid = inputData['sid']
        bufferout= {}
        result = models.t_cebs_result_stackcell.objects.filter(sid = sid)
        if result.exists():        
            if 'confid' in inputData.keys():
                bufferout['confid'] = result[0].confid_id
            else:
                pass
            if 'file_attr' in inputData.keys():
                bufferout['file_attr'] = result[0].file_attr;
            else:
                pass
            if 'name_before' in inputData.keys():
                bufferout['name_before'] = result[0].name_before;
            else:
                pass
            if 'name_after' in inputData.keys():
                bufferout['name_after'] = result[0].name_after;
            else:
                pass
            if 'rec_time' in inputData.keys():
                bufferout['rec_time'] = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S') ;
            else:
                pass
            if 'totalnbr' in inputData.keys():
                bufferout['totalnbr'] = result[0].totalnbr;
            else:
                pass
            if 'validnbr' in inputData.keys():
                bufferout['validnbr'] = result[0].validnbr;
            else:
                pass
            if 'doneflag' in inputData.keys():
                bufferout['doneflag'] = result[0].doneflag;
            else:
                pass
            if 'memo' in inputData.keys():
                bufferout['memo'] = result[0].memo;
            else:
                pass
        print(bufferout)
        return bufferout      

    #this is demo to catch the one batch file  result
    def dft_dbi_cebs_result_eleg(self, inputData):
        snbatch = inputData['snbatch']
        result = models.t_cebs_result_eleg.objects.filter(snbatch = snbatch)
        res = []
        if result.exists(): 
            for i in range(0,len(result)):
                bufferout = {}
                bufferout['snhole']= result[i].snhole
                bufferout['bigalive']= result[i].bigalive
                bufferout['bigdead']= result[i].bigdead
                bufferout['midalive']= result[i].midalive
                bufferout['middead']= result[i].middead
                bufferout['smaalive']= result[i].smaalive
                bufferout['totalalive']= result[i].totalalive
                bufferout['totaldead']= result[i].totaldead
                bufferout['totalsum']= result[i].totalsum
                res.append(bufferout)
                print(bufferout)
        print('res',res)       
        return res       
           
    def dft_dbi_cebs_init_config_read(self, inputData):
        bufferout = {}
        result = models.t_cebs_object_profile.objects.filter(defaultflag = True)
        if result.exists():
            foundObjid=result[0].objid
            bufferout['objid'] = result[0].objid
            bufferout['objname'] = result[0].objname
            bufferout['objtype'] = result[0].objtype
            #bufferout['uid'] = result[0].uid
            bufferout['uid'] = result[0].uid_id
            bufferout['dir_origin'] = result[0].dir_origin
            bufferout['dir_middle'] = result[0].dir_middle
        
        #result = models.t_cebs_config_eleg.objects.filter(objid = foundObjid)
        result = models.t_cebs_config_eleg.objects.filter(objid_id = foundObjid)
        if result.exists():
            bufferout['confid'] = result[0].confid
            bufferout['fixpoint'] = result[0].fixpoint
            bufferout["autoexpo"] = result[0].autoexpo
            bufferout['autovideo'] = result[0].autovideo
            bufferout['autodist'] = result[0].autodist
            bufferout['addset'] = result[0].addset
            bufferout['autocap'] = result[0].autocap
            bufferout['autoperiod'] = result[0].autoperiod
            bufferout['videotime'] = result[0].videotime
            bufferout['slimit'] = result[0].slimit
            bufferout['smlimit'] = result[0].smlimit
            bufferout['mblimit'] = result[0].mblimit
            bufferout['blimit'] = result[0].blimit
            bufferout['accspeed'] = result[0].accspeed
            bufferout['decspeed'] = result[0].decspeed
            bufferout['movespeed'] = result[0].movespeed
            bufferout['zero_spd'] = result[0].zero_spd
            bufferout['zero_dec'] = result[0].zero_dec
            bufferout['back_step'] = result[0].back_step
        
        result = models.t_cebs_cali_profile.objects.all()   
        if result.exists():
            bufferout['platetype'] = result[0].platetype
            bufferout['calitime'] = str(result[0].calitime)
            bufferout['caliuid'] = result[0].uid_id
            bufferout['left_bot_x'] = result[0].left_bot_x
            bufferout['left_bot_y'] = result[0].left_bot_y
            bufferout['right_up_x'] = result[0].right_up_x
            bufferout['right_up_y'] = result[0].right_up_y
              

        print(bufferout)
        return bufferout 

    def dft_dbi_cebs_hstGetConfig(self, inputData):
        bufferout = {}
        objectProfile={}
        elegObj={}
        caliProfile={}
        bufferout['cmd'] ='hstGetConfig',
        result = models.t_cebs_object_profile.objects.filter(defaultflag = True)
        if result.exists():
            foundObjid=result[0].objid
            objectProfile['objid'] = result[0].objid
            objectProfile['objname'] = result[0].objname
            objectProfile['objtype'] = result[0].objtype
            #bufferout['uid'] = result[0].uid
            objectProfile['uid'] = result[0].uid_id
            objectProfile['dir_origin'] = result[0].dir_origin
            objectProfile['dir_middle'] = result[0].dir_middle
            objectProfile['memo'] = result[0].memo
            objectProfile['defaultflag']=result[0].defaultflag
        else:
            bufferout['error_no']='not found default setting'
            return bufferout
        
        # bufferout['cebs_object_profile']=objectProfile
        #result = models.t_cebs_config_eleg.objects.filter(objid = foundObjid)
        result = models.t_cebs_config_eleg.objects.filter(objid_id = foundObjid)
        if result.exists():
            elegObj['confid'] = result[0].confid
            elegObj['fixpoint'] = result[0].fixpoint
            elegObj["autoexpo"] = result[0].autoexpo
            elegObj['autovideo'] = result[0].autovideo
            # elegObj['autodist'] = result[0].autodist
            elegObj['autowork'] = result[0].autowork
            elegObj['blurylimit'] = result[0].blurylimit
            elegObj['addset'] = result[0].addset
            elegObj['autocap'] = result[0].autocap
            elegObj['autoperiod'] = result[0].autoperiod
            elegObj['videotime'] = result[0].videotime
            elegObj['slimit'] = result[0].slimit
            elegObj['smlimit'] = result[0].smlimit
            elegObj['mblimit'] = result[0].mblimit
            elegObj['blimit'] = result[0].blimit
            elegObj['accspeed'] = result[0].accspeed
            elegObj['decspeed'] = result[0].decspeed
            elegObj['movespeed'] = result[0].movespeed
            elegObj['zero_spd'] = result[0].zero_spd
            # elegObj['zero_dec'] = result[0].zero_dec
            elegObj['zero_acc'] = result[0].zero_acc
            elegObj['back_step'] = result[0].back_step
            elegObj['autoclfy'] = result[0].autoclfy
            elegObj['objid'] = result[0].objid_id
        else:
            bufferout['error_no']='not found eleg setting'
            return bufferout
        
        # bufferout['cebs_config_eleg']=elegObj
		
        result = models.t_cebs_cali_profile.objects.all()   
        if result.exists():
            caliProfile['platetype'] = result[0].platetype
            caliProfile['calitime'] = str(result[0].calitime)
            caliProfile['uid'] = result[0].uid_id
            caliProfile['left_bot_x'] = result[0].left_bot_x
            caliProfile['left_bot_y'] = result[0].left_bot_y
            caliProfile['right_up_x'] = result[0].right_up_x
            caliProfile['right_up_y'] = result[0].right_up_y
            caliProfile['plateoption']=['96_STANDARD','48_STANDARD','24_STANDARD','12_STANDARD','6_STANDARD']
        else:
            bufferout['error_no']='not found cali setting'
            return bufferout
        bufferout['cebs_object_profile']=objectProfile
        bufferout['cebs_config_eleg']=elegObj
        bufferout['cebs_cali_profile']=caliProfile

        print(bufferout)
        return bufferout         
        
    def dft_dbi_cebs_hstSetConfig(self, inputData):
        print(inputData)
        defaultflag_val = inputData['cebs_object_profile']['defaultflag'] 
        objname_val = inputData['cebs_object_profile']['objname'] 
        objtype_val = inputData['cebs_object_profile']['objtype'] 
          
        dir_origin_val = inputData['cebs_object_profile']['dir_origin'] 
        dir_middle_val = inputData['cebs_object_profile']['dir_middle'] 
        memo_val = inputData['cebs_object_profile']['memo'] 
        
        if "uid" in inputData['cebs_object_profile'].keys():
            foreignkeyname=inputData['cebs_object_profile']['uid']
        else:
            foreignkeyname=None

        result = models.t_cebs_user_sheet.objects.filter(uid = foreignkeyname)

        if result.exists():
            obj_uid_val = result[0].uid
        else:
            obj_uid_val = None
#         result = models.t_cebs_user_sheet.objects.filter(uid = foreignkeyname)
#         if result.exists():
#             uid_val = result[0].uid

        result=models.t_cebs_object_profile.objects.filter(defaultflag = True)
        
        if result.exists():
            models.t_cebs_object_profile.objects.filter(defaultflag =True).update(
            defaultflag = defaultflag_val,objname = objname_val, objtype = objtype_val, 
            dir_origin = dir_origin_val, dir_middle = dir_middle_val, memo = memo_val,uid_id=obj_uid_val             
            )
        else:
            models.t_cebs_object_profile.objects.create(
            defaultflag = defaultflag_val,objname = objname_val, objtype = objtype_val, 
            dir_origin = dir_origin_val, dir_middle = dir_middle_val, memo = memo_val,uid_id=obj_uid_val             
            )  

        fixpoint_val = inputData['cebs_config_eleg']['fixpoint']
        autoexpo_val = inputData["cebs_config_eleg"]["autoexpo"]
        autovideo_val = inputData['cebs_config_eleg']['autovideo']
        # autodist_val = inputData['cebs_config_eleg']['autodist']
        addset_val = inputData['cebs_config_eleg']['addset']
        autocap_val = inputData['cebs_config_eleg']['autocap']
        autoperiod_val = inputData['cebs_config_eleg']['autoperiod']
        videotime_val = inputData['cebs_config_eleg']['videotime']
        slimit_val = inputData['cebs_config_eleg']['slimit']
        smlimit_val = inputData['cebs_config_eleg']['smlimit']
        mblimit_val = inputData['cebs_config_eleg']['mblimit']
        blimit_val = inputData['cebs_config_eleg']['blimit']
        accspeed_val = inputData['cebs_config_eleg']['accspeed']
        decspeed_val = inputData['cebs_config_eleg']['decspeed']
        movespeed_val = inputData['cebs_config_eleg']['movespeed']
        zero_spd_val = inputData['cebs_config_eleg']['zero_spd']
        # zero_dec_val = inputData['cebs_config_eleg']['zero_dec']
        zero_acc_val = inputData['cebs_config_eleg']['zero_acc']
        back_step_val = inputData['cebs_config_eleg']['back_step']
        autoclfy_val = inputData['cebs_config_eleg']['autoclfy']
        autowork_val = inputData['cebs_config_eleg']['autowork']
        blurylimit_val = inputData['cebs_config_eleg']['blurylimit']

        
        # foreignkeyname = models.t_cebs_object_profile.objects.all().last().objid
        # print(foreignkeyname)
        #关联到别的表单就要加  _id   只能锁定上表的主键
        # result = models.t_cebs_object_profile.objects.filter(objid = foreignkeyname)
        result=models.t_cebs_object_profile.objects.filter(defaultflag = True)
        if result.exists():
            objid_val = result[0].objid

        
        result=models.t_cebs_config_eleg.objects.filter(objid_id=objid_val)

        if result.exists():
            models.t_cebs_config_eleg.objects.filter(objid_id=objid_val).update(
            objid_id = objid_val, fixpoint = fixpoint_val, autoexpo = autoexpo_val, autovideo = autovideo_val, addset = addset_val,
            autocap = autocap_val, autoperiod = autoperiod_val, videotime = videotime_val,
            slimit = slimit_val, smlimit =smlimit_val, mblimit = mblimit_val, blimit = blimit_val,
            accspeed = accspeed_val, decspeed = decspeed_val, movespeed = movespeed_val,
            zero_spd = zero_spd_val, back_step  = back_step_val, autoclfy = autoclfy_val,
            autowork = autowork_val, blurylimit = blurylimit_val, zero_acc = zero_acc_val 
            )
        else:
            models.t_cebs_config_eleg.objects.create(
            objid_id = objid_val, fixpoint = fixpoint_val, autoexpo = autoexpo_val, autovideo = autovideo_val, addset = addset_val,
            autocap = autocap_val, autoperiod = autoperiod_val, videotime = videotime_val,
            slimit = slimit_val, smlimit =smlimit_val, mblimit = mblimit_val, blimit = blimit_val,
            accspeed = accspeed_val, decspeed = decspeed_val, movespeed = movespeed_val,
            zero_spd = zero_spd_val, back_step  = back_step_val, autoclfy = autoclfy_val,
            autowork = autowork_val, blurylimit = blurylimit_val, zero_acc = zero_acc_val)
            
        platetype_val = inputData['cebs_cali_profile']['platetype']
        left_bot_x_val = inputData['cebs_cali_profile']['left_bot_x']
        left_bot_y_val = inputData['cebs_cali_profile']['left_bot_y']
        right_up_x_val = inputData['cebs_cali_profile']['right_up_x']
        right_up_y_val = inputData['cebs_cali_profile']['right_up_y']
        if "uid" in inputData['cebs_cali_profile'].keys():
            foreignkeyname=inputData['cebs_cali_profile']['uid']
        else:
            foreignkeyname=None
#         foreignkeyname = inputData['cebs_cali_profile']['uid']
        calitime_val = inputData['cebs_cali_profile']['calitime']
        result = models.t_cebs_user_sheet.objects.filter(uid = foreignkeyname)

        if result.exists():
            uid_val = result[0].uid
        else:
            uid_val=None
        
        # result= models.t_cebs_cali_profile.objects.filter(uid_id=uid_val)
        result= models.t_cebs_cali_profile.objects.all()
        if result.exists(): 
            models.t_cebs_cali_profile.objects.filter(id=result[0].id).update(
            platetype = platetype_val,  left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
            right_up_x = right_up_x_val, right_up_y = right_up_y_val, uid_id = uid_val, calitime = calitime_val
            ) 
        else:
            models.t_cebs_cali_profile.objects.create(
            platetype = platetype_val,  left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
            right_up_x = right_up_x_val, right_up_y = right_up_y_val, uid_id = uid_val, calitime = calitime_val
            )           
        return inputData

    def dft_dbi_cebs_hstUpdateCaliPar(self, inputData): 
        # if "uid" in inputData['cebs_cali_profile']:
        #     uid_val=inputData['cebs_cali_profile']['uid']
        # else:
        #     uid_val=None
       
        # result = models.t_cebs_cali_profile.objects.filter(uid_id = uid_val)
        result= models.t_cebs_cali_profile.objects.all()
        if result.exists():
            platetype_val = inputData['cebs_cali_profile']['platetype']
            calitime_val = inputData['cebs_cali_profile']['calitime']
            left_bot_x_val = inputData['cebs_cali_profile']['left_bot_x']
            left_bot_y_val = inputData['cebs_cali_profile']['left_bot_y']
            right_up_x_val = inputData['cebs_cali_profile']['right_up_x']
            right_up_y_val = inputData['cebs_cali_profile']['right_up_y']
        else:
            cali_info={}
            cali_info['cmd']='hstUpdateCaliPar'
            cali_info['error_no']='Update Cali profile fail. Not found cali record.'
            return cali_info

        models.t_cebs_cali_profile.objects.filter(id = result[0].id).update(
            platetype = platetype_val,calitime = calitime_val, left_bot_x = left_bot_x_val, left_bot_y = left_bot_y_val,
            right_up_x = right_up_x_val, right_up_y = right_up_y_val
                )

        if result[0].uid_id is not None:
            inputData['cebs_cali_profile']['uid']=result[0].uid_id
        
        return inputData

    def dft_dbi_cebs_hstAddBatchNbr(self, inputData): 
        res = models.t_cebs_user_sheet.objects.filter(uid = inputData['cebs_batch_info']['user'])
        if res:
            uid_val = inputData['cebs_batch_info']['user']
        else:
            uid_val = None
        createtime_val = inputData['cebs_batch_info']['createtime'] 
        comp_nbr_val = inputData['cebs_batch_info']['comp_nbr'] 
        usr_def1_val = inputData['cebs_batch_info']['usr_def1']   
        usr_def2_val = inputData['cebs_batch_info']['usr_def2'] 
        models.t_cebs_batch_info.objects.create(
             uid_id = uid_val,createtime = createtime_val, comp_nbr = comp_nbr_val, usr_def1 = usr_def1_val,
             usr_def2 = usr_def2_val              
              )
        #result = models.t_cebs_batch_info.objects.filter(createtime = createtime_val)
        result = models.t_cebs_batch_info.objects.last()
        bufferout = {}
        dbainfo={}
        # print(result.snbatch)
        # if result.exists():
        #     print("found subid")
        dbainfo['snbatch']=result.snbatch
        dbainfo['uid_id']=result.uid_id
        dbainfo['createtime']=str(result.createtime)
        dbainfo['comp_nbr']=result.comp_nbr
        dbainfo['usr_def1']=result.usr_def1
        dbainfo['usr_def2']=result.usr_def2
        bufferout['cmd']="hstAddBatchNbr"
        bufferout['cebs_batch_info']=dbainfo

        return bufferout

    def dft_dbi_cebs_hstAddPicCap(self, inputData): 
        # sid_val = inputData['cebs_pvci_eleg']['sid'] 
        # confid_val = inputData['cebs_pvci_eleg']['confid'] 
        result = models.t_cebs_object_profile.objects.filter(defaultflag = True, objtype=1)

        if result.exists():
            foundObjid=result[0].objid 
            print(foundObjid)    
            config_result=models.t_cebs_config_eleg.objects.filter(objid_id = foundObjid)
            if config_result.exists():
                confid_val=config_result[0].confid
                print(confid_val)
        else:
            confd={}
            confd['cmd']='hstAddPicCap'
            confd['error_no']='Not found defaultflag true & objtype is ELEG'
            return confd

        snbatch_val = inputData['cebs_pvci_eleg']['snbatch'] 
        snhole_val = inputData['cebs_pvci_eleg']['snhole']   
        file_attr_val = inputData['cebs_pvci_eleg']['file_attr'] 
        name_before_val = inputData['cebs_pvci_eleg']['name_before'] 
        video_before_val = inputData['cebs_pvci_eleg']['video_before'] 
        cap_time_val = inputData['cebs_pvci_eleg']['cap_time'] 
        name_after_val = inputData['cebs_pvci_eleg']['name_after'] 
        memo_val = inputData['cebs_pvci_eleg']['memo'] 
        rec_time_val = inputData['cebs_pvci_eleg']['rec_time'] 

        models.t_cebs_pvci_eleg.objects.create(
            confid_id = confid_val, snbatch = snbatch_val, snhole = snhole_val, file_attr = file_attr_val, name_before = name_before_val,
            name_after = name_after_val, bigalive = 0, bigdead = 0, midalive = 0, middead = 0,
            smaalive = 0, smdead = 0,totalalive = 0, totaldead = 0, totalsum = 0, 
            doneflag = 0, memo = memo_val, rec_time=rec_time_val,cap_time=cap_time_val,video_before=video_before_val
            ) 

        inputData['cebs_pvci_eleg']['sid']=models.t_cebs_pvci_eleg.objects.last().sid
        inputData['cebs_pvci_eleg']['confid']=models.t_cebs_pvci_eleg.objects.last().confid_id
        return inputData

    def dft_dbi_cebs_hstUpdatePicCfy(self, inputData): 
        sid_val = inputData['cebs_pvci_eleg']['sid'] 
        confid_val= inputData['cebs_pvci_eleg']['confid_id'] 
        snbatch_val = inputData['cebs_pvci_eleg']['snbatch'] 
        snhole_val = inputData['cebs_pvci_eleg']['snhole']   
        file_attr_val = inputData['cebs_pvci_eleg']['file_attr'] 
        name_before_val = inputData['cebs_pvci_eleg']['name_before'] 
        video_before_val = inputData['cebs_pvci_eleg']['video_before'] 
        cap_time_val = inputData['cebs_pvci_eleg']['cap_time'] 
        name_after_val = inputData['cebs_pvci_eleg']['name_after'] 
        memo_val = inputData['cebs_pvci_eleg']['memo'] 
        rec_time_val = inputData['cebs_pvci_eleg']['rec_time'] 

        bigalive_val=inputData['cebs_pvci_eleg']['bigalive']
        bigdead_val=inputData['cebs_pvci_eleg']['bigdead']
        midalive_val=inputData['cebs_pvci_eleg']['midalive']
        middead_val=inputData['cebs_pvci_eleg']['middead']
        smaalive_val=inputData['cebs_pvci_eleg']['smalive']
        smdead_val=inputData['cebs_pvci_eleg']['smdead']
        totalalive_val=inputData['cebs_pvci_eleg']['totalalive']
        totaldead_val=inputData['cebs_pvci_eleg']['totaldead']
        totalsum_val=inputData['cebs_pvci_eleg']['totalsum']
        doneflag_val=inputData['cebs_pvci_eleg']['doneflag']


        models.t_cebs_pvci_eleg.objects.filter(sid =sid_val).update(
            snbatch = snbatch_val, snhole = snhole_val, file_attr = file_attr_val, name_before = name_before_val,cap_time = cap_time_val,
            name_after = name_after_val, rec_time = rec_time_val,bigalive = bigalive_val, bigdead = bigdead_val, midalive = midalive_val, 
            middead = middead_val,smaalive = smaalive_val, smdead = smdead_val,totalalive = totalalive_val, totaldead = totaldead_val, 
            totalsum = totalsum_val, doneflag = doneflag_val, memo = memo_val ,confid_id = confid_val, video_before=video_before_val
            )  
        return inputData

    def dft_dbi_cebs_hstReadPic(self, inputData):
        snbatch_val = inputData['batch_number'] 
        snhole_val = inputData['hole_number']
        bufferout= {}
        bufferout['cmd']='hstReadPic'
        bufferout['error_no']='no_error'
        dbinfo={}
        result = models.t_cebs_pvci_eleg.objects.filter(snbatch = snbatch_val,snhole=snhole_val)
        if result.exists():
            dbinfo['sid'] = result[0].sid
            dbinfo['confid'] = result[0].confid_id
            dbinfo['snbatch'] = result[0].snbatch
            dbinfo['snhole'] = result[0].snhole
            dbinfo['file_attr'] = result[0].file_attr
            dbinfo['name_before'] = result[0].name_before
            dbinfo['cap_time'] = result[0].cap_time.strftime('%Y-%m-%d %H:%M:%S') 
            dbinfo['video_before'] = result[0].video_before
            dbinfo['name_after'] = result[0].name_after
            dbinfo['rec_time'] = result[0].rec_time.strftime('%Y-%m-%d %H:%M:%S') 
            dbinfo['bigalive'] = result[0].bigalive
            dbinfo['bigdead'] = result[0].bigdead  
            dbinfo['midalive'] = result[0].midalive 
            dbinfo['middead'] = result[0].middead 
            dbinfo['smaalive'] = result[0].smaalive 
            dbinfo['smdead'] = result[0].smdead 
            dbinfo['totalalive'] = result[0].totalalive 
            dbinfo['totaldead'] = result[0].totaldead 
            dbinfo['totalsum'] = result[0].totalsum 
            dbinfo['doneflag'] = result[0].doneflag 
            dbinfo['memo'] = result[0].memo 
            print(dbinfo)
        else:
            bufferout['error_no']='not found pic data'
        bufferout['cebs_pvci_eleg']=dbinfo
        return bufferout 

    def dft_dbi_cebs_hstReadUnclfyPar(self, inputData):
        file_attr_val = inputData['file_attr'] 
        bufferout= {}
        result = models.t_cebs_pvci_eleg.objects.filter(file_attr = file_attr_val,doneflag= False).order_by('cap_time')
        if result.exists():
            bufferout['batchNbr']=result[0].snbatch
            bufferout['holeNbr']=result[0].snhole
            bufferout['fileAbsOrigin']=result[0].name_before
            bufferout['fileAbsMiddle']=result[0].name_after
            bufferout['fileAbsVideo']=result[0].video_before
 
        
        else:

            bufferout['error_no']='not found Unclfy pic data'
        bufferout['cmd']='hstReadUnclfyPar'
        bufferout['file-attr']=file_attr_val
        return bufferout 