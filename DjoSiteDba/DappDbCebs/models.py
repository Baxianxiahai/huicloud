# coding:utf8
from django.db import models

# Create your models here.

class t_customer_mission(models.Model):
    sid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32)
    timeStampSubmit = models.DateTimeField(auto_now=True, null=True)
    pageNbr = models.IntegerField(default=0)
    filePath = models.CharField(max_length=254)
    fileName = models.CharField(max_length=254)    

class t_cebs_classify_exec_log(models.Model):
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

#TUP的工作指示控制字
class t_cebs_counter(models.Model):
    tup_lable = models.CharField(max_length=50, primary_key=True)
    picbatchcnt = models.IntegerField(default=0)
    picbatchclas = models.IntegerField(default=0)
    picremaincnt = models.IntegerField(default=0)
    picbatfluclas = models.IntegerField(default=0)
    picremflucnt = models.IntegerField(default=0)

#TUP工作环境控制数据库表单
class t_cebs_env(models.Model):
    tup_lable = models.CharField(max_length=50, primary_key=True)
    workdir = models.CharField(max_length=254, null=True, blank=True)
    pic_origin = models.CharField(max_length=254, null=True, blank=True)
    pic_middle = models.CharField(max_length=254, null=True, blank=True)
    holeboard_type = models.CharField(max_length=254, null=True, blank=True)
    holeboard_left_bot_x = models.IntegerField(default=0)
    holeboard_left_bot_y = models.IntegerField(default=0)
    holeboard_right_up_x = models.IntegerField(default=0)
    holeboard_right_up_y = models.IntegerField(default=0)
    pic_take_fix_point_set = models.BooleanField(default=False)
    pic_classification_set = models.BooleanField(default=False)
    pic_auto_work_after_start_set = models.BooleanField(default=False)
    pic_auto_work_tti = models.IntegerField(default=0)
    vis_small_low_limit = models.IntegerField(default=0)
    vis_small_mid_limit = models.IntegerField(default=0)
    vis_mid_big_limit = models.IntegerField(default=0)
    vis_big_upper_limit = models.IntegerField(default=0)
    vis_res_addup_set = models.BooleanField(default=False)
    vis_cap_enable_set = models.BooleanField(default=False)
    vis_cap_dur_in_sec = models.IntegerField(default=3)
    vis_clfy_gen_par1 = models.IntegerField(default=0)
    vis_clfy_gen_par2 = models.IntegerField(default=0)
    vis_clfy_gen_par3 = models.IntegerField(default=0)
    vis_clfy_gen_par4 = models.IntegerField(default=0)

#TUP中荧光堆叠照片识别处理过程
class t_cebs_fspc(models.Model):
    tup_lable = models.CharField(max_length=50, primary_key=True)
    mark_line = models.IntegerField(default=0)
    mark_width = models.IntegerField(default=0)
    mark_area = models.IntegerField(default=0)
    mark_dilate = models.IntegerField(default=0)
    area_square_min = models.IntegerField(default=0)
    area_squre_max = models.IntegerField(default=0)
    area_dilate = models.IntegerField(default=0)
    area_erode = models.IntegerField(default=0)
    cell_square_min = models.IntegerField(default=0)
    cell_square_max = models.IntegerField(default=0)
    cell_raduis_min = models.IntegerField(default=0)
    cell_raduis_max = models.IntegerField(default=0)
    cell_square_min = models.IntegerField(default=0)
    cell_dilate = models.IntegerField(default=0)
    cell_erode = models.IntegerField(default=0)
    cell_ce = models.IntegerField(default=0)
    cell_distance = models.IntegerField(default=0)
    pic_train_delay = models.IntegerField(default=0)
    addup_set = models.BooleanField(default=False)

#拍照与识别文件控制
class t_cebs_batch_file(models.Model):
    sid = models.AutoField(primary_key=True)
    last_update_time = models.DateTimeField(auto_now=True, null=True)
    batch_no = models.IntegerField(default=0)
    hole_no = models.IntegerField(default=0)
    hole_name = models.CharField(max_length=10, null=True, blank=True)
    pic_file_name = models.CharField(max_length=254, null=True, blank=True)
    file_att = models.CharField(max_length=25, default='normal', null=True, blank=True)
    vid_file_name = models.CharField(max_length=254, null=True, blank=True)
    classified_flag = models.BooleanField(default=False)
    video_flag = models.BooleanField(default=False)
    cfy_res = models.CharField(max_length=25, null=True, blank=True)
    
    
    
    
    
    
    






    


