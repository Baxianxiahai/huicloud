from django.shortcuts import render
# from DappDbF11faam.models import dct_t_l3f11faam_product_stock_sheet
# # Create your views here.
# 
# def insert():
#     dct_t_l3f11faam_product_stock_sheet.objects.create(stockname="上海一仓",stockaddress="上海市浦东新区",stockheader="李四")
from DappDbF11faam.models import dct_t_l3f11faam_typesheet

def insert(body):
    typeCode=body["specificationcode"]
    appleGrade=body["specificationlevel"]
    appleNum=body['specificationnumber']
    appleWeight=body["specificationweight"]
    memo=body['specificationmemo']
    print(typeCode,appleGrade,appleNum,appleWeight,memo)
    typesheet=dct_t_l3f11faam_typesheet(pjcode="HYGS",typecode=typeCode,applenum=appleNum,appleweight=appleWeight,applegrade=appleGrade,memo=memo)
    typesheet.save()
    print(typesheet)
    if typesheet.sid:  
        return True
    else:
        return False
    