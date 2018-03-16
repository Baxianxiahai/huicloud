from django.shortcuts import render, redirect, HttpResponse
#from django.contrib import admin
from DappDbTest import models
#from DjoSiteDba import DappDbTest.models

# Create your views here.

def index(request):
    #request.POST
    #request.GET
    #return render.content("Hello World!")
    return HttpResponse("Hello World!")  # 返回字符串

def user_info_add(request):
    #print("request = ", request);
    #models.UserInfo.objects.all()
    #models.UserInfo.objects.all().values('user')    #只取user列
    #models.UserInfo.objects.all().values_list('id','user')    #取出id和user列，并生成一个列表
    #models.UserInfo.objects.get(id=1)
    #models.UserInfo.objects.get(user='yangmv')
    #print("Request-Pwd= ", request['pwd']);
    
    if ((request['user'] != '') and (request['pwd'] != '')):
      models.UserInfo.objects.create(user=request['user'], pwd=request['pwd']);
      return HttpResponse("Execute user_info_add with parameter success!")
    else:
        models.UserInfo.objects.create(user='test1',pwd='123456')
        obj = models.UserInfo(user='test2',pwd='123456')
        obj.save()
        dic = {'user':'test3','pwd':'123456'}
        models.UserInfo.objects.create(**dic)
        return HttpResponse("Execute user_info_add default success!")  # 返回字符串


def user_info_delete(request):
    models.UserInfo.objects.filter(user='test1').delete()
    models.UserInfo.objects.filter(user='test2').delete()
    models.UserInfo.objects.filter(user='test3').delete()
    return HttpResponse("Execute user_info_delete success!")  # 返回字符串

def user_info_modify(request):
    models.UserInfo.objects.filter(user='test1').update(pwd='520')
#     obj = models.UserInfo.objects.get(user='test2')
#     obj.pwd = '520'
#     obj.save()
    return HttpResponse("Execute user_info_modify success!")  # 返回字符串

def user_info_show(request):
    user_list = models.UserInfo.objects.all()
    print("Show Request GET = ", request.GET);
    print("Show Request POST = ", request.POST);
    print("Show Request FILES = ", request.FILES);
    #return render(request, 'show.html', {''})  # 返回模板内容
    return render(request, "user_info_show.html", {'user_list':user_list})

def user_info_home(request):
    models.UserInfo.objects.create(user='test1')
    after = models.UserInfo.objects.all()
    print(after[0].pwd)
    return render(request, 'user_info_home.html')

def login(request):
    if request.method == "GET":
        return render(request, 'reg.html')
    elif request.method == "POST":
        # redio 单选框获取
        redio = request.POST.get("gender")
        print("单选框的值：", redio)
        # checkbox 复选框获取
        checkbox = request.POST.getlist("favor")
        print("复选框的值", checkbox)
        # 获取文件数据
        obj = request.FILES.get("fafafa")
        print(obj, type(obj), obj.name)  # 打印文件信息
        import os
        file_path = os.path.join('upload', obj.name)
        with open (file_path, mode="wb") as f:
            for i in obj.chunks():
                f.write(i)
        return render(request, "reg.html")
    else:
        # PUT, DELETE, HEAD, OPTION……
        return redirect("/reg/")
    

def orm(request):
# 创建数据
    # 第一种方式
    # models.UserInfo.objects.create(username="root",password="123")
    # 第二种方式
    # obj = models.UserInfo(username='fzh', password="iajtag")
    # obj.save()
    # 第三种方式
    # dic = {'username':'fgf', 'password':'666'}
    # models.UserInfo.objects.create(**dic)

# 查询数据
    # result = models.UserInfo.objects.all()  # 查询所有，为QuerySet类型，可理解成列表
    # result = models.UserInfo.objects.filter(username="fgf",password="666")  # 列表
    # result = models.UserInfo.objects.filter(username="fgf").first()  # 对象
    # 条件查询。filter 相当于where查询条件，里面的"，"会组成and条件
    # for row in result:  # 打印查询到数据。
    #     print(row.id,row.username,row.password)

    # 查看QuerySet类型具体做了什么事情，可以： print(result.query)

# 删除数据
    # models.UserInfo.objects.all().delete()  # 删除所有
    # models.UserInfo.objects.filter(id=4).delete()  # 删除所有

# 更新数据
    # models.UserInfo.objects.all().update(password=8888)
    # models.UserInfo.objects.filter(id=3).update(password=888888)

    #return HttpResponse('orm')
    return render.content('orm')


