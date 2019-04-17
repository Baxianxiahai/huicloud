from django.db import models


# Create your models here.
# 磷石膏物流平台运输的货品的规格
class dct_t_l3f13phos_goods_info(models.Model):
    sid = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=25)
    goods_length = models.FloatField(default=0)
    goods_height = models.FloatField(default=0)
    goods_width = models.FloatField(default=0)


# 磷石膏物流平台装货和卸货户头的信息
class dct_t_l3f13phos_account_info(models.Model):
    sid = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=50)


# 磷石膏物流平台的公司的信息
class dct_t_l3f13phos_company_info(models.Model):
    com_code = models.CharField(max_length=15, primary_key=True)
    business_img = models.CharField(max_length=100)
    business_code = models.CharField(max_length=50)
    com_name = models.CharField(max_length=100)
    com_repre = models.CharField(max_length=10)
    com_time = models.DateField(null=True, default=None)
    com_address = models.CharField(max_length=255)


# 磷石膏物流平台用户的信息
class dct_t_l3f13phos_app_user_info(models.Model):
    uid = models.CharField(max_length=15, primary_key=True)
    uname = models.CharField(max_length=10,null=True)
    utelephone = models.CharField(max_length=11)
    vercode = models.IntegerField(null=True, default=None)
    vertime = models.DateTimeField(max_length=0, null=True, default=None)
    idnumber = models.CharField(max_length=20,null=True)
    openid = models.CharField(max_length=50)
    user_type = models.IntegerField(default=1)  #1：该用户为司机，2：该用户为管理人员
    driver_code = models.CharField(max_length=20, null=True, default=None) #驾驶证号码
    driver_status = models.IntegerField(default=3) #1：用户拥有待接受的任务；2：用户拥有正在进行中的任务；3：用户处于空闲中，表示用户已拒绝掉任务或者已完成任务。
    id_positive = models.CharField(max_length=100, null=True, default=None)
    id_side = models.CharField(max_length=100, null=True, default=None)
    drive_img = models.CharField(max_length=100, null=True, default=None)
    trans_img = models.CharField(max_length=100, null=True, default=None)
    trans_code = models.CharField(max_length=100, null=True, default=None)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    regitime = models.DateTimeField(max_length=0)
    info_status=models.BooleanField(default=False)
    driver_type = models.IntegerField(null=True, default=None)  # 值为1表示该用户有所属公司，值为0表示该用户为散户，管理人员不需要本信息


# 用户下的汽车信息
class dct_t_l3f13phos_user_car(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f13phos_app_user_info, on_delete=models.CASCADE)
    car_type = models.IntegerField(default=0) #1：车头；2：挂车
    car_img = models.CharField(max_length=100)
    car_plate = models.CharField(max_length=20,unique=True)


# 用户与公司的映射表
class dct_t_l3f13phos_user_company(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f13phos_app_user_info, on_delete=models.CASCADE)
    com_code = models.ForeignKey(dct_t_l3f13phos_company_info, on_delete=models.CASCADE)
    ustatus = models.IntegerField(default=0) #内部司机的审核状态.0表示审核未通过，1表示审核通过，暂时不用


# 公司的合同模板（暂时认为一家公司一个模板）
class dct_t_l3f13phos_contract(models.Model):
    sid = models.AutoField(primary_key=True)
    contname = models.CharField(max_length=100)
    com_code = models.ForeignKey(dct_t_l3f13phos_company_info, on_delete=models.CASCADE)
    txt_1 = models.TextField(null=True, default=None)
    txt_2 = models.TextField(null=True, default=None)
    txt_3 = models.TextField(null=True, default=None)
    contstatus = models.BooleanField(default=True)


# 任务的详细情况
class dct_t_l3f13phos_task(models.Model):
    task_code = models.CharField(max_length=20,primary_key=True)
    driver = models.ForeignKey(dct_t_l3f13phos_app_user_info,related_name='driver_user', null=True, on_delete=models.SET_NULL, default=None)
    manage = models.ForeignKey(dct_t_l3f13phos_app_user_info,related_name='manage_user', null=True, on_delete=models.SET_NULL, default=None)
    com_code = models.ForeignKey(dct_t_l3f13phos_company_info, null=True, on_delete=models.SET_NULL, default=None)
    start_date = models.DateTimeField(max_length=0, null=True, default=None)
    arrive_time = models.DateTimeField(max_length=0, null=True, default=None)
    sprovince = models.CharField(max_length=10)
    scity = models.CharField(max_length=30)
    scounty = models.CharField(max_length=30)
    saddress = models.CharField(max_length=100)
    eprovince = models.CharField(max_length=10)
    ecity = models.CharField(max_length=30)
    ecounty = models.CharField(max_length=30)
    eaddress = models.CharField(max_length=100)
    load_account = models.ForeignKey(dct_t_l3f13phos_account_info,related_name='load_account',null=True, on_delete=models.SET_NULL, default=None)
    unload_account = models.ForeignKey(dct_t_l3f13phos_account_info,related_name='unload_account', null=True, on_delete=models.SET_NULL, default=None)
    task_status = models.IntegerField(default=0) #1、未接受；2、已接受；3、已完成；4、已拒绝
    contcode = models.ForeignKey(dct_t_l3f13phos_contract, on_delete=models.SET_NULL, null=True, default=None)
    weight = models.FloatField(default=0)
    price = models.FloatField(default=0)
    lpound = models.FloatField(default=0)
    upound = models.FloatField(default=0)
    load_img = models.CharField(max_length=100, null=True, default=None)
    unload_img = models.CharField(max_length=100, null=True, default=None)
    load_date=models.DateTimeField(null=True,default=None)
    unload_date=models.DateTimeField(null=True,default=None)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    ulongitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    ulatitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    goods_type=models.ForeignKey(dct_t_l3f13phos_goods_info,null=True,on_delete=models.SET_NULL)


# 任务的视频记录
class dct_t_l3f13phos_video(models.Model):
    sid = models.AutoField(primary_key=True)
    task_code = models.ForeignKey(dct_t_l3f13phos_task, on_delete=models.CASCADE)
    vtime = models.DateTimeField(max_length=0)
    vtype = models.IntegerField(default=0)
    vname = models.CharField(max_length=30)
    vpath = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)


# 任务的路径记录
class dct_t_l3f13phos_route(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f13phos_app_user_info, on_delete=models.CASCADE)
    taskcode = models.ForeignKey(dct_t_l3f13phos_task, on_delete=models.CASCADE)
    reporttime = models.DateTimeField(max_length=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, default=None)


# 公司数据天汇总表
class dct_t_l3f13phos_company_data_day(models.Model):
    sid = models.AutoField(primary_key=True)
    com_code = models.ForeignKey(dct_t_l3f13phos_company_info, on_delete=models.CASCADE)
    data_day = models.DateField(null=True, default=None)
    pound = models.FloatField(default=0)


# 司机数据天汇总表
class dct_t_l3f13phos_user_data_day(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f13phos_app_user_info, on_delete=models.CASCADE)
    data_day = models.DateField(null=True, default=None)
    pound = models.FloatField(default=0)
    price = models.FloatField(default=0)


# 公司数据月汇总表
class dct_t_l3f13phos_company_data_mounth(models.Model):
    sid = models.AutoField(primary_key=True)
    com_code = models.ForeignKey(dct_t_l3f13phos_company_info, on_delete=models.CASCADE)
    mounth_start = models.DateField(null=True, default=None)
    mounth_end = models.DateField(null=True, default=None)
    pound = models.FloatField(default=0)


# 司机数据月汇总表
class dct_t_l3f13phos_user_data_mounth(models.Model):
    sid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(dct_t_l3f13phos_app_user_info, on_delete=models.CASCADE)
    mounth_start = models.DateField(null=True, default=None)
    mounth_end = models.DateField(null=True, default=None)
    pound = models.FloatField(default=0)
    price = models.FloatField(default=0)
