# coding:utf8
from django.db import models
from serial.properties import NoneType

# Create your models here.

# class t_customer_mission(models.Model):
#     sid = models.AutoField(primary_key=True)
#     user = models.CharField(max_length=32)
#     timeStampSubmit = models.DateTimeField(auto_now=True, null=True)
#     pageNbr = models.IntegerField(default=0)
#     filePath = models.CharField(max_length=254)
#     fileName = models.CharField(max_length=254)    
# 
# class t_cebs_classify_exec_log(models.Model):
#     sid = models.AutoField(primary_key=True)
#     user = models.CharField(max_length=32)
#     timeStampExec = models.DateTimeField(auto_now=True, null=True)
#     pageLen = models.IntegerField(default=0)
#     pageWidth = models.IntegerField(default=0)
#     resTotal = models.IntegerField(default=0)
#     resTotalAlive = models.IntegerField(default=0)
#     resTotalDead = models.IntegerField(default=0)
#     resSmallAlive = models.IntegerField(default=0)
#     resSmallDead = models.IntegerField(default=0)
#     resMidAlive = models.IntegerField(default=0)
#     resMidDead = models.IntegerField(default=0)
#     resBigAlive = models.IntegerField(default=0)
#     resBigDead = models.IntegerField(default=0)
#     resUnclassifyAlive = models.IntegerField(default=0)
#     resUnclassifyDead = models.IntegerField(default=0)
# 
# #TUP的工作指示控制字
# class t_cebs_counter(models.Model):
#     tup_lable = models.CharField(max_length=50, primary_key=True)
#     picbatchcnt = models.IntegerField(default=0)
#     picbatchclas = models.IntegerField(default=0)
#     picremaincnt = models.IntegerField(default=0)
#     picbatfluclas = models.IntegerField(default=0)
#     picremflucnt = models.IntegerField(default=0)
# 
# #TUP工作环境控制数据库表单
# class t_cebs_env(models.Model):
#     tup_lable = models.CharField(max_length=50, primary_key=True)
#     workdir = models.CharField(max_length=254, null=True, blank=True)
#     pic_origin = models.CharField(max_length=254, null=True, blank=True)
#     pic_middle = models.CharField(max_length=254, null=True, blank=True)
#     holeboard_type = models.CharField(max_length=254, null=True, blank=True)
#     holeboard_left_bot_x = models.IntegerField(default=0)
#     holeboard_left_bot_y = models.IntegerField(default=0)
#     holeboard_right_up_x = models.IntegerField(default=0)
#     holeboard_right_up_y = models.IntegerField(default=0)
#     pic_take_fix_point_set = models.BooleanField(default=False)
#     pic_classification_set = models.BooleanField(default=False)
#     pic_auto_work_after_start_set = models.BooleanField(default=False)
#     pic_auto_work_tti = models.IntegerField(default=0)
#     vis_small_low_limit = models.IntegerField(default=0)
#     vis_small_mid_limit = models.IntegerField(default=0)
#     vis_mid_big_limit = models.IntegerField(default=0)
#     vis_big_upper_limit = models.IntegerField(default=0)
#     vis_res_addup_set = models.BooleanField(default=False)
#     vis_cap_enable_set = models.BooleanField(default=False)
#     vis_cap_dur_in_sec = models.IntegerField(default=3)
#     vis_clfy_gen_par1 = models.IntegerField(default=0)
#     vis_clfy_gen_par2 = models.IntegerField(default=0)
#     vis_clfy_gen_par3 = models.IntegerField(default=0)
#     vis_clfy_gen_par4 = models.IntegerField(default=0)
# 
# #TUP中荧光堆叠照片识别处理过程
# class t_cebs_fspc(models.Model):
#     tup_lable = models.CharField(max_length=50, primary_key=True)
#     mark_line = models.IntegerField(default=0)
#     mark_width = models.IntegerField(default=0)
#     mark_area = models.IntegerField(default=0)
#     mark_dilate = models.IntegerField(default=0)
#     area_square_min = models.IntegerField(default=0)
#     area_squre_max = models.IntegerField(default=0)
#     area_dilate = models.IntegerField(default=0)
#     area_erode = models.IntegerField(default=0)
#     cell_square_min = models.IntegerField(default=0)
#     cell_square_max = models.IntegerField(default=0)
#     cell_raduis_min = models.IntegerField(default=0)
#     cell_raduis_max = models.IntegerField(default=0)
#     cell_dilate = models.IntegerField(default=0)
#     cell_erode = models.IntegerField(default=0)
#     cell_ce = models.IntegerField(default=0)
#     cell_distance = models.IntegerField(default=0)
#     pic_train_delay = models.IntegerField(default=0)
#     addup_set = models.BooleanField(default=False)
# 
# #拍照与识别文件控制
# class t_cebs_batch_file(models.Model):
#     sid = models.AutoField(primary_key=True)
#     last_update_time = models.DateTimeField(auto_now=True, null=True)
#     batch_no = models.IntegerField(default=0)
#     hole_no = models.IntegerField(default=0)
#     hole_name = models.CharField(max_length=10, null=True, blank=True)
#     pic_file_name = models.CharField(max_length=254, null=True, blank=True)
#     file_att = models.CharField(max_length=25, default='normal', null=True, blank=True)
#     vid_file_name = models.CharField(max_length=254, null=True, blank=True)
#     classified_flag = models.BooleanField(default=False)
#     video_flag = models.BooleanField(default=False)
#     cfy_res = models.CharField(max_length=25, null=True, blank=True)
    
    
class t_cebs_user_sheet(models.Model):
    uid = models.CharField(max_length=15,primary_key=True)
    login_name=models.CharField(max_length=20)
    pass_word=models.CharField(max_length=100)
    grade_level=models.IntegerField(default=4,null=True)
    reg_date=models.DateTimeField(auto_now_add=True)  #创建时间不再更新
    email=models.EmailField(null=True,blank=True)
    memo=models.CharField(max_length=500,null=True)
    
class t_cebs_language_config(models.Model):
    lang_abbr = models.CharField(max_length=2,primary_key=True)
    lang_name = models.CharField(max_length=20)
    lang_icon = models.CharField(max_length=20)
    defaultflag = models.BooleanField(default=False)

class t_cebs_language_dict(models.Model):
    sid=models.AutoField(primary_key=True)
    english = models.CharField(max_length=200)
    chinese = models.CharField(max_length=200)

class t_lcebs_user_right_menu(models.Model):
    sid = models.AutoField(primary_key=True) 
    uid = models.ForeignKey(t_cebs_user_sheet,on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)
    
class t_lcebs_user_right_action(models.Model):
    sid = models.AutoField(primary_key=True) 
    uid = models.ForeignKey(t_cebs_user_sheet,on_delete=models.CASCADE)
    action_name = models.CharField(max_length=50)
    
class t_cebs_product_profile(models.Model):
    dev_code = models.CharField(max_length=20)
    hw_ver = models.IntegerField(null=True,blank=True)
    sw_ver = models.IntegerField(null=True,blank=True)
    authtoken = models.CharField(max_length=128)
    mfd = models.DateTimeField(auto_now_add=True)
    
class t_cebs_cali_profile(models.Model):
    platetype = models.IntegerField(default=5,null=True)
    calitime = models.DateTimeField(auto_now=True)
    uid = models.ForeignKey(t_cebs_user_sheet,on_delete=models.CASCADE)
    left_bot_x = models.IntegerField(default=0)
    left_bot_y = models.IntegerField(default=0)
    right_up_x = models.IntegerField(default=0)
    right_up_y = models.IntegerField(default=0)

    
class t_cebs_object_profile(models.Model):
    objid = models.AutoField(primary_key=True) 
    defaultflag = models.BooleanField(default=False)
    objname = models.CharField(max_length=20,db_index=True)
    objtype = models.IntegerField(default=1)
    uid = models.ForeignKey(t_cebs_user_sheet,on_delete=models.CASCADE)
    dir_origin = models.CharField(max_length=100)
    dir_middle = models.CharField(max_length=100)
    memo=models.CharField(max_length=500)
 
class t_cebs_config_eleg(models.Model):
    confid = models.AutoField(primary_key=True) 
    objid = models.ForeignKey(t_cebs_object_profile,on_delete=models.CASCADE)
    fixpoint = models.BooleanField(default=False)
    autovideo = models.BooleanField(default=False)
    autodist = models.BooleanField(default=False)
    addset = models.BooleanField(default=True)
    autocap = models.BooleanField(default=False)
    autoperiod = models.IntegerField(default=60)
    videotime = models.IntegerField(default=3)
    slimit = models.IntegerField(default=200)
    smlimit = models.IntegerField(default=500)
    mblimit = models.IntegerField(default=2000)
    blimit = models.IntegerField(default=5000)
    accspeed = models.IntegerField(default=4)
    decspeed = models.IntegerField(default=4)
    movespeed = models.IntegerField(default=4)
    zero_spd = models.IntegerField(default=4)
    zero_dec = models.IntegerField(default=4)
    back_step = models.IntegerField(default=4)

class t_cebs_config_stackcell(models.Model):
    confid = models.AutoField(primary_key=True)
    objid = models.ForeignKey(t_cebs_object_profile,on_delete=models.CASCADE)
    addset = models.BooleanField(default=True)
    line_area = models.IntegerField(default=10000)
    line_width = models.IntegerField(default=44)
    line_long = models.IntegerField(default=222)
    line_dilate = models.IntegerField(default=22)
    area_up = models.IntegerField(default=1000000)
    area_low = models.IntegerField(default=100000)
    area_dilate = models.IntegerField(default=1500)
    area_erode = models.IntegerField(default=5)
    square_min = models.IntegerField(default=920)
    square_max = models.IntegerField(default=1500)
    radius_min = models.IntegerField(default=19)
    radius_max = models.IntegerField(default=23)
    cell_dilate = models.IntegerField(default=61)
    cell_erode = models.IntegerField(default=5)
    cell_round = models.IntegerField(default=50)
    cell_distance = models.IntegerField(default=30)
    train_delay = models.IntegerField(default=2)
    
class  t_cebs_result_eleg(models.Model):   
    sid = models.AutoField(primary_key=True)
    confid = models.ForeignKey(t_cebs_object_profile,on_delete=models.CASCADE)
    snbatch = models.IntegerField(default=0)
    snhole = models.IntegerField(default=0)
    file_attr = models.IntegerField(default=1,db_index=True)
    name_before = models.CharField(max_length=20)
    cap_time = models.DateTimeField(auto_now_add=True)
    name_after = models.CharField(max_length=20)
    rec_time = models.DateTimeField(auto_now=True)
    bigalive = models.IntegerField(default=0)
    bigdead = models.IntegerField(default=0)
    midalive = models.IntegerField(default=0)
    middead = models.IntegerField(default=0)
    smaalive = models.IntegerField(default=0)
    smdead = models.IntegerField(default=0)
    totalalive = models.IntegerField(default=0)
    totaldead = models.IntegerField(default=0)
    totalsum = models.IntegerField(default=0)
    doneflag = models.BooleanField(default=False)
    memo=models.CharField(max_length=500)
    
class t_cebs_result_stackcell(models.Model):
    sid = models.AutoField(primary_key=True)
    confid = models.ForeignKey(t_cebs_object_profile,on_delete=models.CASCADE)
    file_attr = models.IntegerField(default=1)
    name_before = models.CharField(max_length=20)
    name_after = models.CharField(max_length=20)
    rec_time = models.DateTimeField(auto_now=True)
    totalnbr = models.IntegerField(default=0)
    validnbr = models.IntegerField(default=0)
    doneflag = models.BooleanField(default=False)
    memo=models.CharField(max_length=500)
    
class t_cebs_batch_info(models.Model):
    snbatch = models.AutoField(primary_key=True)
    uid = models.ForeignKey(t_cebs_user_sheet,on_delete=models.CASCADE)
    createtime = models.DateTimeField(auto_now=True)
    comp_nbr = models.IntegerField(default=4)
    usr_def1 = models.CharField(max_length=256)
    usr_def2 = models.CharField(max_length=256)
   
    
    
    
    
    
    
    
    