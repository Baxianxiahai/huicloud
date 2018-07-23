from django.shortcuts import render
import random
import time
import datetime
import os
import stat
from django.db.models import Q
# from DappDbF11faam.models import dct_t_l3f11faam_product_stock_sheet
# # Create your views here.
# 
# def insert():
#     dct_t_l3f11faam_product_stock_sheet.objects.create(stockname="上海一仓",stockaddress="上海市浦东新区",stockheader="李四")
from DappDbF11faam.models import *
from DappDbF1sym.models import *
class dct_classDbiL3apF11Faam:
    __MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR='/xhzn/avorion/userphoto/'
    def __init__(self):
        pass
    def __dft_getUserLever(self,inputData):
        sessionid=inputData
        result=dct_t_l3f1sym_user_login_session.objects.get(session_id=sessionid)
        if result:
            userLever=result.uid.grade_lever
        else:
            userLever=''
        return userLever
    def __dft_getRandomUid(self, strlen):
        str_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        uid = ''.join(random.sample(str_array, strlen))
        return uid

    def __dft_get_user_auth_factory(self, inputData):
        uid = inputData
        result = dct_t_l3f1sym_account_primary.objects.filter(uid=uid)
        if result.exists():
            pjCode = result[0].backup
        else:
            pjCode = ""
        return pjCode

    def __dft_get_factory_config(self,pjCode):
        result=dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=pjCode)
        if result.exists():
            config={'workstart':result[0].workstart,
                    'workend':result[0].workend,
                    'reststart':result[0].reststart,
                    'restend':result[0].restend,
                    'fullwork':result[0].fullwork}
        else:
            config=""
        return config

    def __dft_get_employee_config(self,pjCode,employee):
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode,employee=employee,onjob=True)
        if result.exists():
            unitprice={'unitprice':result[0].unitprice,'standardnum':result[0].standardnum}
        else:
            unitprice=""
        return unitprice
    
    def __dft_get_product_type(self,pjCode):
        typeList=[]
        result=dct_t_l3f11faam_type_sheet.objects.filter(pjcode=pjCode)
        for line in result:
            typeList.append(line)
        return typeList
    
    def dft_dbi_faam_factory_codelist_query(self,inputData):
        pjCode=self.__dft_get_user_auth_factory(inputData)
        codeList=[]
        if pjCode!="":
            result=dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=pjCode)
            for line in result:
                temp={'id':line.pjcode}
                codeList.append(temp)
        return codeList
    
    
    def dft_dbi_faam_factory_table_query(self, inputData):
        uid = inputData['uid']
        keyword = inputData['keyword']
        pjCode = self.__dft_get_user_auth_factory(uid)
        factoryTable = []
        if keyword == "":
            result = dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=pjCode)
            if result.exists():
                for line in result:
                    temp = {'factoryid': str(line.sid),
                            'factorycode': line.pjcode,
                            'factorydutyday':str(line.fullwork),
                            'factorylongitude':str(line.longitude),
                            'factorylatitude':str(line.latitude),
                            'factoryworkstarttime':str(line.workstart),
                            'factoryworkendtime':str(line.workend),
                            'factorylaunchstarttime':str(line.reststart),
                            'factorylaunchendtime':str(line.restend),
                            'factoryaddress':str(line.address),
                            'factorymemo':str(line.memo),
                            'factorytrafficmoney':str(line.trafficmoney),
                            'factorybonus':str(line.factorybonus),
                            }
                    factoryTable.append(temp)
            else:
                temp={}
                factoryTable.append(temp)
        else:
            result = dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=pjCode,pjcode__icontains=keyword)
            if result.exists():
                for line in result:
                    temp = {'factoryid': str(line.sid),
                            'factorycode': line.pjcode,
                            'factorydutyday':str(line.fullwork),
                            'factorylongitude':str(line.longitude),
                            'factorylatitude':str(line.latitude),
                            'factoryworkstarttime':str(line.workstart),
                            'factoryworkendtime':str(line.workend),
                            'factorylaunchstarttime':str(line.reststart),
                            'factorylaunchendtime':str(line.restend),
                            'factoryaddress':str(line.address),
                            'factorymemo':str(line.memo),
                            'factorytrafficmoney':str(line.trafficmoney),
                            'factorybonus':str(line.factorybonus),
                            }
                    factoryTable.append(temp)
            else:
                temp={}
                factoryTable.append(temp)
        return factoryTable
    
    def dft_dbi_factory_table_modify(self, inputData):
        if 'factoryid' not in inputData.keys():
            sid = ""
        else:
            sid = inputData['factoryid'].replace(' ', '')
        if 'factorycode' not in inputData.keys():
            pjCode = ""
        else:
            pjCode = inputData['factorycode'].replace(' ', '')
        if 'factorydutyday' not in inputData.keys():
            fullWork = ""
        else:
            fullWork = int(inputData['factorydutyday'].replace(' ', ''))
        if 'factorylongitude' not in inputData.keys():
            longitude = ""
        else:
            longitude = int(inputData['factorylongitude'].replace(' ', ''))
        if 'factorylatitude' not in inputData.keys():
            latitude = ""
        else:
            latitude = int(inputData['factorylatitude'].replace(' ', ''))
        if 'factoryworkstarttime' not in inputData.keys():
            workStart = ""
        else:
            workStart = inputData['factoryworkstarttime'].replace(' ', '')
        if 'factoryworkendtime' not in inputData.keys():
            workEnd = ""
        else:
            workEnd = inputData['factoryworkendtime'].replace(' ', '')
        if 'factorylaunchstarttime' not in inputData.keys():
            restStart = ""
        else:
            restStart = inputData['factorylaunchstarttime'].replace(' ', '')
        if 'factorylaunchendtime' not in inputData.keys():
            restEnd = ""
        else:
            restEnd = inputData['factorylaunchendtime'].replace(' ', '')
        if 'factoryaddress' not in inputData.keys():
            address = ""
        else:
            address = inputData['factoryaddress'].replace(' ', '')
        if 'factorymemo' not in inputData.keys():
            memo = ""
        else:
            memo = inputData['factorymemo'].replace(' ', '')
        if 'factorytrafficmoney' not in inputData.keys():
            trafficmoney = ""
        else:
            trafficmoney = int(inputData['factorytrafficmoney'].replace(' ', ''))
        if 'factorybonus' not in inputData.keys():
            factorybonus = ""
        else:
            factorybonus = int(inputData['factorybonus'].replace(' ', ''))
        dct_t_l3f11faam_factory_sheet.objects.filter(sid=sid).update(pjcode=pjCode,workstart=workStart,workend=workEnd,reststart=restStart,restend=restEnd,fullwork=fullWork,address=address,latitude=latitude,longitude=longitude,trafficmoney=trafficmoney,factorybonus=factorybonus,memo=memo)
    
    def dft_dbi_factory_table_new(self, inputData):
        if 'factorycode' not in inputData.keys():
            pjCode = ""
        else:
            pjCode = inputData['factorycode'].replace(' ', '')
        if 'factorydutyday' not in inputData.keys():
            fullWork = ""
        else:
            fullWork = inputData['factorydutyday'].replace(' ', '')
        if 'factorylongitude' not in inputData.keys():
            longitude = ""
        else:
            longitude = inputData['factorylongitude'].replace(' ', '')
        if 'factorylatitude' not in inputData.keys():
            latitude = ""
        else:
            latitude = inputData['factorylatitude'].replace(' ', '')
        if 'factoryworkstarttime' not in inputData.keys():
            workStart = ""
        else:
            workStart = inputData['factoryworkstarttime'].replace(' ', '')
        if 'factoryworkendtime' not in inputData.keys():
            workEnd = ""
        else:
            workEnd = inputData['factoryworkendtime'].replace(' ', '')
        if 'factorylaunchstarttime' not in inputData.keys():
            restStart = ""
        else:
            restStart = inputData['factorylaunchstarttime'].replace(' ', '')
        if 'factorylaunchendtime' not in inputData.keys():
            restEnd = ""
        else:
            restEnd = inputData['factorylaunchendtime'].replace(' ', '')
        if 'factoryaddress' not in inputData.keys():
            address = ""
        else:
            address = inputData['factoryaddress'].replace(' ', '')
        if 'factorymemo' not in inputData.keys():
            memo = ""
        else:
            memo = inputData['factorymemo'].replace(' ', '')
        if 'factorytrafficmoney' not in inputData.keys():
            trafficmoney = ""
        else:
            trafficmoney = inputData['factorytrafficmoney'].replace(' ', '')
        if 'factorybonus' not in inputData.keys():
            factorybonus = ""
        else:
            factorybonus = inputData['factorybonus'].replace(' ', '')
        if workStart=="":workStart='07:30:00'
        if workEnd=="":workEnd='16:00:00'
        if restStart=="":restStart='12:30:00'
        if restEnd=="":restEnd='13:00:00'
        if longitude=="":longitude=0
        if latitude=="":latitude=0
        dct_t_l3f11faam_factory_sheet.objects.create(pjcode=pjCode,workstart=workStart,workend=workEnd,reststart=restStart,restend=restEnd,fullwork=fullWork,address=address,latitude=latitude,longitude=longitude,trafficmoney=trafficmoney,factorybonus=factorybonus,memo=memo)
    
    def dft_dbi_factory_table_delete(self,inputData):
        sid=inputData['factoryid']
        dct_t_l3f11faam_factory_sheet.objects.filter(sid=sid).delete()
        
    def dft_dbi_product_type_num_inquery(self,uid):
        pjCode=self.__dft_get_user_auth_factory(uid['uid'])
        result=dct_t_l3f11faam_type_sheet.objects.filter(pjcode=pjCode)
        i=0
        for line in result:
            i=i+1
        return i
    
    def dft_dbi_product_type_table_query(self,inputData):
        uid=inputData['uid']
        keyword=inputData['keyword']
        pjCode=self.__dft_get_user_auth_factory(uid)
        productType=[]
        if keyword=="":
            result=dct_t_l3f11faam_type_sheet.objects.filter(pjcode=pjCode)
            for line in result:
                temp={
                    'specificationid':str(line.sid),
                    'specificationcode':line.typecode,
                    'specificationlevel':line.applegrade,
                    'specificationnumber':str(line.applenum),
                    'specificationweight':str(line.appleweight),
                    'specificationmemo':line.memo,
                    }
                productType.append(temp)
        else:
            result=dct_t_l3f11faam_type_sheet.objects.filter(pjcode=pjCode,typecode__icontains=keyword)
            for line in result:
                temp={
                    'specificationid':str(line.sid),
                    'specificationcode':line.typecode,
                    'specificationlevel':line.applegrade,
                    'specificationnumber':str(line.applenum),
                    'specificationweight':str(line.appleweight),
                    'specificationmemo':line.memo,
                    }
                productType.append(temp)
        return productType
    def dft_dbi_product_type_modify(self,inputData):
        if 'specificationid' not in inputData.keys():
            sid=''
        else:
            sid=inputData['specificationid']
        if 'specificationcode' not in inputData.keys():
            typeCode=''
        else:
            typeCode=inputData['specificationcode']
        if 'specificationlevel' not in inputData.keys():
            appleGrade = ''
        else:
            appleGrade = inputData['specificationlevel']
        if 'specificationnumber' not in inputData.keys():
            appleNum = ''
        else:
            appleNum = inputData['specificationnumber']
        if 'specificationweight' not in inputData.keys():
            appleWeight = ''
        else:
            appleWeight = inputData['specificationweight']
        if 'specificationmemo' not in inputData.keys():
            memo = ''
        else:
            memo = inputData['specificationmemo']
        if appleNum=="":appleNum=0
        if appleWeight=="":appleWeight=0
        dct_t_l3f11faam_type_sheet.objects.filter(sid=sid).update(typecode=typeCode,applenum=appleNum,appleweight=appleWeight,applegrade=appleGrade,memo=memo)
        
    def dft_dbi_product_type_new(self,inputData):
        if 'specificationcode' not in inputData.keys():
            typeCode=''
        else:
            typeCode=inputData['specificationcode']
        if 'specificationlevel' not in inputData.keys():
            appleGrade = ''
        else:
            appleGrade = inputData['specificationlevel']
        if 'specificationnumber' not in inputData.keys():
            appleNum = ''
        else:
            appleNum = inputData['specificationnumber']
        if 'specificationweight' not in inputData.keys():
            appleWeight = ''
        else:
            appleWeight = inputData['specificationweight']
        if 'specificationmemo' not in inputData.keys():
            memo = ''
        else:
            memo = inputData['specificationmemo']
        if appleNum=="":appleNum=0
        if appleWeight=="":appleWeight=0
        dct_t_l3f11faam_type_sheet.objects.create(typecode=typeCode,applenum=appleNum,appleweight=appleWeight,applegrade=appleGrade,memo=memo)
        
    def dft_dbi_product_type_delete(self,inputData):
        sid=inputData['sid']
        dct_t_l3f11faam_type_sheet.objects.filter(sid=sid).delete()
    
    def dft_dbi_staff_table_new(self,inputData):
        if 'name' not in inputData.keys():
            employee = ''
        else:
            employee = inputData['name']
        if 'PJcode' not in inputData.keys():
            pjCode = ''
        else:
            pjCode = inputData['PJcode']
        if 'position' not in inputData.keys():
            position = ''
        else:
            position = inputData['position']
        if 'gender' not in inputData.keys():
            gender = ''
        else:
            gender = inputData['gender']
        if 'mobile' not in inputData.keys():
            phone = ''
        else:
            phone = inputData['mobile']
        if 'geoinfo' not in inputData.keys():
            zone = ''
        else:
            zone = inputData['geoinfo']
        if 'identify' not in inputData.keys():
            idCard = ''
        else:
            idCard = inputData['identify']
        if 'address' not in inputData.keys():
            address = ''
        else:
            address = inputData['address']
        if 'bank' not in inputData.keys():
            bank = ''
        else:
            bank = inputData['bank']
        if 'account' not in inputData.keys():
            account = ''
        else:
            account = inputData['account']
        if 'photo' not in inputData.keys():
            photo = ''
        else:
            photo = inputData['photo']
        if 'salary' not in inputData.keys():
            unitPrice = ''
        else:
            unitPrice = inputData['salary']
        if 'KPI' not in inputData.keys():
            standardNum = ''
        else:
            standardNum = inputData['KPI']
        if 'memo' not in inputData.keys():
            memo = ''
        else:
            memo = inputData['memo']
        
        now=time.strftime("%Y-%m-%d",time.localtime(int(time.time())))
        mid='MID'+self.__dft_getRandomUid(7)
        file_link=self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+photo
        if(os.path.exists(file_link)):
            file_new_name=mid+'.jpg'
            file_link_new='D:/sss'+file_new_name
            os.chmod(file_link,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
            if os.path.exists(file_link_new):
                os.unlink(file_link_new)
            os.rename(file_link,file_link_new)
            dct_t_l3f11faam_member_sheet.objects.create(mid=mid,pjcode=pjCode,employee=employee,gender=gender,phone=phone,regdate=now,position=position,zone=zone,idcard=idCard,address=address,bank=bank,bankcard=account,photo=file_new_name,unitprice=unitPrice,standardnum=standardNum,memo=memo)
        else:
            dct_t_l3f11faam_member_sheet.objects.create(mid=mid,pjcode=pjCode,employee=employee,gender=gender,phone=phone,regdate=now,position=position,zone=zone,idcard=idCard,address=address,bank=bank,bankcard=account,unitprice=unitPrice,standardnum=standardNum,memo=memo)
        return True
    
    def dft_dbi_staff_table_delete(self,inputData):
        uid=inputData['uid']
        onJob=False
        dct_t_l3f11faam_member_sheet.objects.filter(mid=uid).update(onjob=onJob)
    
    def dft_dbi_staff_table_modify(self,inputData):
        if 'staffid' not in inputData.keys():
            staffId=""
        else:staffId=inputData['staffid']
        if 'name' not in inputData.keys():
            employee = ''
        else:
            employee = inputData['name']
        if 'PJcode' not in inputData.keys():
            pjCode = ''
        else:
            pjCode = inputData['PJcode']
        if 'position' not in inputData.keys():
            position = ''
        else:
            position = inputData['position']
        if 'gender' not in inputData.keys():
            gender = ''
        else:
            gender = inputData['gender']
        if 'mobile' not in inputData.keys():
            phone = ''
        else:
            phone = inputData['mobile']
        if 'geoinfo' not in inputData.keys():
            zone = ''
        else:
            zone = inputData['geoinfo']
        if 'identify' not in inputData.keys():
            idCard = ''
        else:
            idCard = inputData['identify']
        if 'address' not in inputData.keys():
            address = ''
        else:
            address = inputData['address']
        if 'bank' not in inputData.keys():
            bank = ''
        else:
            bank = inputData['bank']
        if 'account' not in inputData.keys():
            account = ''
        else:
            account = inputData['account']
        if 'photo' not in inputData.keys():
            photo = '1'
        else:
            photo = inputData['photo']
        if 'salary' not in inputData.keys():
            unitPrice = ''
        else:
            unitPrice = inputData['salary']
        if 'status' not in inputData.keys():
            onjob = ''
        else:
            onjob = inputData['status']
        if 'KPI' not in inputData.keys():
            standardNum = ''
        else:
            standardNum = inputData['KPI']
        if 'memo' not in inputData.keys():
            memo = ''
        else:
            memo = inputData['memo']
        if 'nickname' not in inputData.keys():
            nickname=""
        else:
            nickname= inputData['nickname']
        now = time.strftime("%Y-%m-%d", time.localtime(int(time.time())))
        print(nickname)
        file_link = self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+ photo
        if (os.path.exists(file_link)):
            file_new_name = staffId + '.jpg'
            file_link_new = self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR + file_new_name
            os.chmod(file_link, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            if os.path.exists(file_link_new):
                os.unlink(file_link_new)
            os.rename(file_link, file_link_new)
            dct_t_l3f11faam_member_sheet.objects.filter(mid=staffId).update(pjcode=pjCode, employee=employee, openid=nickname,gender=gender,
                                                        phone=phone, regdate=now, position=position, zone=zone,
                                                        idcard=idCard, address=address, bank=bank, bankcard=account,
                                                        photo=file_new_name, unitprice=unitPrice,
                                                        standardnum=standardNum,onjob=onjob, memo=memo)
        else:
            dct_t_l3f11faam_member_sheet.objects.filter(mid=staffId).update(pjcode=pjCode, employee=employee,openid=nickname, gender=gender,
                                                        phone=phone, regdate=now, position=position, zone=zone,
                                                        idcard=idCard, address=address, bank=bank, bankcard=account,
                                                        unitprice=unitPrice, standardnum=standardNum,onjob=onjob,  memo=memo)
    
    def dft_dbi_staff_namelist_query(self,inputData):
        uid=inputData['uid']
        nameList=[]
        pjCode=self.__dft_get_user_auth_factory(uid)
        print(pjCode)
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        for line in result:
            temp={'id':line.mid,'name':line.employee}
            nameList.append(temp)
        return nameList
    
    def dft_dbi_employee_number_inquery(self,inputData):
        uid=inputData['uid']
        pjCode=self.__dft_get_user_auth_factory(uid)
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        i=0
        for line in result:
            i=i+1
        return i
    
    def dft_dbi_staff_table_query(self,inputData):
        uid=inputData['uid']
        keyword=inputData['keyword']
        containLeave=inputData['containLeave']
        pjCode = self.__dft_get_user_auth_factory(uid)
        staffTable=[]
        if(containLeave=='true'):
            if keyword=="":
                result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
                for line in result:
                    if line.onjob==True:
                        onJob=1
                    else:
                        onJob=0
                    temp={'id':line.mid,'name':line.employee,'PJcode':line.pjcode,'nickname':line.openid,
                          'mobile':line.phone,'gender':line.gender,'identify':line.idcard,'geoinfo':line.zone,
                          'address':line.address,'bank':line.bank,'account':line.bankcard,'photo':self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+line.photo,
                          'salary':line.unitprice,'position':line.position,'status':str(onJob),'KPI':line.standardnum,
                          'memo':line.memo}
                    staffTable.append(temp)
            else:
                result = dct_t_l3f11faam_member_sheet.objects.filter(Q(pjcode=pjCode),Q(employee__icontains=keyword)|Q(phone__icontains=keyword))
                for line in result:
                    if line.onjob==True:
                        onJob=1
                    else:
                        onJob=0
                    temp={'id':line.mid,'name':line.employee,'PJcode':line.pjcode,'nickname':line.openid,
                          'mobile':line.phone,'gender':line.gender,'identify':line.idcard,'geoinfo':line.zone,
                          'address':line.address,'bank':line.bank,'account':line.bankcard,'photo':self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+line.photo,
                          'salary':line.unitprice,'position':line.position,'status':str(onJob),'KPI':line.standardnum,
                          'memo':line.memo}
                    staffTable.append(temp)
        else:
            onJob=True
            if keyword=="":
                result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode,onjob=onJob)
                for line in result:
                    if line.onjob==True:
                        onJob=1
                    else:
                        onJob=0
                    temp={'id':line.mid,'name':line.employee,'PJcode':line.pjcode,'nickname':line.openid,
                          'mobile':line.phone,'gender':line.gender,'identify':line.idcard,'geoinfo':line.zone,
                          'address':line.address,'bank':line.bank,'account':line.bankcard,'photo':self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+line.photo,
                          'salary':line.unitprice,'position':line.position,'status':str(onJob),'KPI':line.standardnum,
                          'memo':line.memo}
                    staffTable.append(temp)
            else:
                result = dct_t_l3f11faam_member_sheet.objects.filter(Q(pjcode=pjCode),Q(onjob=onJob),Q(employee__icontains=keyword)|Q(phone__icontains=keyword))
                for line in result:
                    if line.onjob==True:
                        onJob=1
                    else:
                        onJob=0
                    temp={'id':line.mid,'name':line.employee,'PJcode':line.pjcode,'nickname':line.openid,
                          'mobile':line.phone,'gender':line.gender,'identify':line.idcard,'geoinfo':line.zone,
                          'address':line.address,'bank':line.bank,'account':line.bankcard,'photo':self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+line.photo,
                          'salary':line.unitprice,'position':line.position,'status':str(onJob),'KPI':line.standardnum,
                          'memo':line.memo}
                    staffTable.append(temp)
        return staffTable
    
    
    def dft_dbi_attendance_record_batch_add(self, inputData):
        uid = inputData['uid']
        pjCode = self.__dft_get_user_auth_factory(uid)
        factory_config = self.__dft_get_factory_config(pjCode)
        if factory_config == "":
            return False
        else:
            restStart = factory_config['reststart']
            restEnd = factory_config['restend']
            workStart = factory_config['workstart']
            workEnd = factory_config['workend']
            dayHour = (restStart.hour - workStart.hour) + (workEnd.hour - restEnd.hour)
            dayMin = (restStart.minute - workStart.minute) + (workEnd.minute - restEnd.minute)
            workTime = round(dayHour + dayMin / 60, 1)
            workDay=datetime.datetime.today()
            offWorkTime=0
            laterWorkFlag=0
            earlyLeaveFlag=0
            onJob=True
            result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode,onjob=onJob)
            for line in result:
                employee=line.employee
                unitPrice=line.unitprice
                print(employee)
                print(unitPrice)
                Daily=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode,employee=employee,workday=workDay)
                if Daily.exists():
                    pass
                else:
                    dct_t_l3f11faam_daily_sheet.objects.create(pjcode=pjCode,employee=employee,workday=workDay,arraytime=workStart,leavetime=workEnd,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag)
                    
    def dft_dbi_attendance_history_query(self,inputData):
        ColumnName=[]
        TableData=[]
        uid=inputData['uid']
        user=inputData['user']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        keyWord=inputData['keyWord']
        Time=str(datetime.date.today())
        timeStart=datetime.datetime.strptime(timeStart,'%Y-%m-%d')
        timeEnd = datetime.datetime.strptime(timeEnd,'%Y-%m-%d')
        Time = datetime.datetime.strptime(Time,'%Y-%m-%d')
        lever=int(self.__dft_getUserLever(user))
        if(lever>1):
            if(Time!=timeStart):
                history = {'Result': False, 'ColumnName': ColumnName, 'TableData': TableData}
                return history
            else:
                ColumnName.append('序号')
                ColumnName.append('姓名')
                ColumnName.append('岗位')
                ColumnName.append('区域')
                ColumnName.append('日期')
                ColumnName.append('上班时间')
                ColumnName.append('下班时间')
                ColumnName.append('请假时长')
                ColumnName.append('工时(小时)')
                pjCode=self.__dft_get_user_auth_factory(uid)
                result=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode,employee__icontains=keyWord)
                for line in result:
                    workDay=datetime.datetime.strptime(str(line.workday),'%Y-%m-%d')
                    if workDay>=timeStart and workDay<=timeEnd:
                        sid=line.sid
                        employee=line.employee
                        tableWorkDay=line.workday
                        arriveTime=line.arraytime
                        
                        leaveTime=line.leavetime
                        offWork=line.offwork
                        workTime=line.worktime
                        employee_sheet=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode,employee=employee)
                        for line in employee_sheet:
                            position=line.position
                            zone=line.zone
                        temp=[]
                        temp.append(sid)
                        temp.append(employee)
                        temp.append(position)
                        temp.append(str(zone))
                        temp.append(str(tableWorkDay))
                        temp.append(str(arriveTime))
                        temp.append(str(leaveTime))
                        temp.append(str(offWork))
                        temp.append(workTime)
                        TableData.append(temp)
                history = {'Result': True, 'ColumnName': ColumnName, 'TableData': TableData}
                return history
        else:
            ColumnName.append('序号')
            ColumnName.append('姓名')
            ColumnName.append('岗位')
            ColumnName.append('区域')
            ColumnName.append('日期')
            ColumnName.append('上班时间')
            ColumnName.append('下班时间')
            ColumnName.append('请假时长')
            ColumnName.append('工时(小时)')
            pjCode = self.__dft_get_user_auth_factory(uid)
            result = dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode, employee__icontains=keyWord)
            for line in result:
                workDay = datetime.datetime.strptime(str(line.workday),'%Y-%m-%d')
                if workDay >= timeStart and workDay <= timeEnd:
                    sid = line.sid
                    employee = line.employee
                    tableWorkDay = line.workday
                    arriveTime = line.arraytime
                    leaveTime = line.leavetime
                    offWork = line.offwork
                    workTime = line.worktime
                    employee_sheet = dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode, employee=employee)
                    for line in employee_sheet:
                        position = line.position
                        zone = line.zone
                    temp = []
                    temp.append(sid)
                    temp.append(employee)
                    temp.append(position)
                    temp.append(str(zone))
                    temp.append(str(tableWorkDay))
                    temp.append(str(arriveTime))
                    temp.append(str(leaveTime))
                    temp.append(str(offWork))
                    temp.append(workTime)
                    TableData.append(temp)
            history = {'Result': True, 'ColumnName': ColumnName, 'TableData': TableData}
            return history   
        
    def dft_dbi_attendance_history_audit(self,inputData):
        uid=inputData['uid']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        timeStart=datetime.datetime.strptime(timeStart,'%Y-%m-%d')
        timeEnd = datetime.datetime.strptime(timeEnd, '%Y-%m-%d')
        keyWord=inputData['keyWord']
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('姓名')
        ColumnName.append('岗位')
        ColumnName.append('区域')
        ColumnName.append('开始日期')
        ColumnName.append('结束日期')
        ColumnName.append('迟到次数')
        ColumnName.append('早退次数')
        ColumnName.append('请假次数')
        ColumnName.append('请假时长')
        ColumnName.append('工作天数')
        ColumnName.append('工作时长')
        pjCode=self.__dft_get_user_auth_factory(uid)
        print(pjCode)
        buffer=[]
        if(keyWord==""):
            result=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode)
            for line in result:
                workDay=datetime.datetime.strptime(str(line.workday),'%Y-%m-%d')
                if workDay>=timeStart and workDay<=timeEnd:
                    buffer.append(line)
        else:
            result = dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode,employee__icontains=keyWord)
            for line in result:
                workDay = datetime.datetime.strptime(str(line.workday), '%Y-%m-%d')
                if workDay >= timeStart and workDay <= timeEnd:
                    buffer.append(line)
        if(len(buffer)==0):
            history={'ColumnName':ColumnName,'TableData':TableData}
            return history
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        nameList=[]
        for line in result:
            temp={'employee':line.employee,'position':line.position,'zone':line.zone}
            nameList.append(temp)
        workingDay={}
        lateWorkDay={}
        earlyLeaveDay={}
        totalWorkTime={}
        offWorkDay={}
        totalOffWorkTime={}
        for i in range(len(buffer)):
            employee=buffer[i].employee
            lateWorkFlag=buffer[i].laterflag
            earlyLeaveFlag=buffer[i].earlyflag
            offWorkTime=buffer[i].offwork
            workTime=buffer[i].worktime
            if (employee in workingDay.keys()) and (employee in lateWorkDay.keys()) and (employee in earlyLeaveDay.keys()) and (employee in totalWorkTime.keys()) and (employee in offWorkDay.keys()) and (employee in totalOffWorkTime.keys()):
                if lateWorkFlag:
                    lateWorkDay[employee]=lateWorkDay[employee]+1
                if earlyLeaveFlag:
                    earlyLeaveDay[employee]=earlyLeaveDay[employee]+1
                if workTime!=0:
                    workingDay[employee]=workingDay[employee]+1
                    totalWorkTime[employee]=totalWorkTime[employee]+workTime
                if offWorkTime!=0:
                    offWorkDay[employee]=offWorkDay[employee]+1
                    totalOffWorkTime[employee]=totalOffWorkTime[employee]+offWorkTime
            else:
                if lateWorkFlag:
                    lateWorkDay[employee]=1
                else:
                    lateWorkDay[employee]=0
                if earlyLeaveFlag:
                    earlyLeaveDay[employee]=1
                else:
                    earlyLeaveDay[employee]=1
                if workTime!=0:
                    workingDay[employee]=1
                    totalWorkTime[employee]=workTime
                else:
                    workingDay[employee]=0
                    totalWorkTime[employee]=0
                if offWorkTime!=0:
                    offWorkDay[employee]=1
                    totalOffWorkTime[employee]=offWorkTime
                else:
                    offWorkDay[employee] = 0
                    totalOffWorkTime[employee] = 0
        sid=0
        for i in range(len(nameList)):
            employee=nameList[i]['employee']
            position=nameList[i]['position']
            zone=nameList[i]['zone']
            if (employee in workingDay.keys()) and (employee in lateWorkDay.keys()) and (
                    employee in earlyLeaveDay.keys()) and (employee in totalWorkTime.keys()) and (
                    employee in offWorkDay.keys()) and (employee in totalOffWorkTime.keys()):
                temp=[]
                sid=sid+1
                temp.append(sid)
                temp.append(employee)
                temp.append(position)
                temp.append(zone)
                temp.append(str(timeStart))
                temp.append(str(timeEnd))
                temp.append(lateWorkDay[employee])
                temp.append(earlyLeaveDay[employee])
                temp.append(offWorkDay[employee])
                temp.append(totalOffWorkTime[employee])
                temp.append(workingDay[employee])
                temp.append(totalWorkTime[employee])
                TableData.append(temp)
        history = {'ColumnName': ColumnName, 'TableData': TableData}
        return history
    def dft_dbi_attendance_record_new(self,inputData):
        dateNow=datetime.date.today()
        uid=inputData['uid']
        employee=inputData['name']
        offWorkTime=inputData['leavehour']
        workDay=inputData['date']
        arriveTime=inputData['arrivetime']
        leaveTime=inputData['leavetime']
        dateNow=datetime.datetime.strptime(str(dateNow),'%Y-%m-%d')
        workDay=datetime.datetime.strptime(workDay,'%Y-%m-%d')
        if(dateNow!=workDay):
            return False
        else:
            pjCode=self.__dft_get_user_auth_factory(uid)
            employee_config=self.__dft_get_employee_config(pjCode,employee)
            if employee_config!="":
                unitPrice=employee_config['unitprice']
                standnumber=employee_config['standardnum']
            else:
                unitPrice=0
            factory_config=self.__dft_get_factory_config(pjCode)
            if factory_config=="":
                return False
            else:
                restStart=factory_config['reststart']
                restEnd=factory_config['restend']
                stdWorkStart=factory_config['workstart']
                stdWorkEnd=factory_config['workend']
                arriveTimeInt=datetime.datetime.strptime(arriveTime,'%H:%M:%S')
                leaveTimeInt=datetime.datetime.strptime(leaveTime,'%H:%M:%S')
                restStart=datetime.datetime.strptime(str(restStart),'%H:%M:%S')
                restEnd = datetime.datetime.strptime(str(restEnd), '%H:%M:%S')
                stdWorkStart = datetime.datetime.strptime(str(stdWorkStart), '%H:%M:%S')
                stdWorkEnd = datetime.datetime.strptime(str(stdWorkEnd), '%H:%M:%S')
                if (arriveTimeInt<=restStart) and (leaveTimeInt>=restEnd):
                    timeInterval=(restStart-arriveTimeInt).seconds+(leaveTimeInt-restEnd).seconds
                elif(arriveTimeInt>=restStart) and(arriveTimeInt<=restEnd):
                    timeInterval=(leaveTimeInt-restEnd).seconds
                elif(arriveTimeInt>=restEnd):
                    timeInterval=(leaveTimeInt-arriveTimeInt).seconds
                elif(leaveTimeInt<=restStart):
                    timeInterval=leaveTimeInt-arriveTimeInt
                else:
                    timeInterval=0
                workTime=round(timeInterval/3600,1)-int(offWorkTime)
                if workTime<0:
                    workTime=0
                if arriveTimeInt<=stdWorkStart:laterWorkFlag=False
                else:laterWorkFlag=True
                if leaveTimeInt>=stdWorkEnd:earlyLeaveFlag=False
                else:earlyLeaveFlag=True
                onJob=True
                result=dct_t_l3f11faam_member_sheet.objects.filter(employee=employee,onjob=onJob,pjcode=pjCode)
                if result.exists():
                    workDay=datetime.datetime.strftime(workDay,'%Y-%m-%d')
                    result=dct_t_l3f11faam_daily_sheet.objects.filter(employee=employee,pjcode=pjCode,workday=workDay)
                    if result.exists():
                        dct_t_l3f11faam_daily_sheet.objects.filter(employee=employee,pjcode=pjCode,workday=workDay).update(arrivetime=arriveTime,leavetime=leaveTime,offwork=offWorkTime,
                                                                                                                           unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag)
                    else:
                        print(pjCode,employee,workDay,arriveTime,leaveTime,offWorkTime,workTime,unitPrice,laterWorkFlag,earlyLeaveFlag)
                        dct_t_l3f11faam_daily_sheet.objects.create(pjcode=pjCode,employee=employee,workday=workDay,arraytime=arriveTime,leavetime=leaveTime,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag,daystandardnum=standnumber)
                else:
                    return False
        
    def dft_dbi_attendance_recode_delete(self,inputData):
        recordId=inputData['attendanceid']
        dct_t_l3f11faam_daily_sheet.objects.filter(sid=recordId).delete()

    def dft_dbi_attendance_recode_get(self,inputData):
        recordId=inputData['attendanceid']
        result=dct_t_l3f11faam_daily_sheet.objects.filter(sid=recordId)
        if result.exists():
            for line in result:
                record={'attendanceID':line.sid,
                        'PJcode':line.pjcode,
                        'name':line.employee,
                        'arrivetime':str(line.arraytime),
                        'leavetime':str(line.leavetime),
                        'leavehour':str(line.offwork),
                        'date':str(line.workday)}
        else:
            record={}
        return record
    def dft_dbi_attendance_record_modify(self,inputData):
        dateNow=datetime.date.today()
        uid=inputData['uid']
        sid=inputData['attendanceID']
        employee=inputData['name']
        offWorkTime=inputData['leavehour']
        workDay=inputData['date']
        arriveTime=inputData['arrivetime']
        leaveTime=inputData['leavetime']
        dateNow=datetime.datetime.strptime(str(dateNow),'%Y-%m-%d')
        workDay=datetime.datetime.strptime(workDay,'%Y-%m-%d')
        if(dateNow!=workDay):
            return False
        else:
            pjCode=self.__dft_get_user_auth_factory(uid)
            employee_config=self.__dft_get_employee_config(pjCode,employee)
            if employee_config!="":
                unitPrice=employee_config['unitprice']
            else:
                unitPrice=0
            factory_config=self.__dft_get_factory_config(pjCode)
            if factory_config=="":
                return False
            else:
                restStart=factory_config['reststart']
                restEnd=factory_config['restend']
                stdWorkStart=factory_config['workstart']
                stdWorkEnd=factory_config['workend']
                arriveTimeInt=datetime.datetime.strptime(arriveTime,'%H:%M:%S')
                leaveTimeInt=datetime.datetime.strptime(leaveTime,'%H:%M:%S')
                restStart=datetime.datetime.strptime(str(restStart),'%H:%M:%S')
                restEnd = datetime.datetime.strptime(str(restEnd), '%H:%M:%S')
                stdWorkStart = datetime.datetime.strptime(str(stdWorkStart), '%H:%M:%S')
                stdWorkEnd = datetime.datetime.strptime(str(stdWorkEnd), '%H:%M:%S')
                if (arriveTimeInt<=restStart) and (leaveTimeInt>=restEnd):
                    timeInterval=(restStart-arriveTimeInt).seconds+(leaveTimeInt-restEnd).seconds
                elif(arriveTimeInt>=restStart) and(arriveTimeInt<=restEnd):
                    timeInterval=(leaveTimeInt-restEnd).seconds
                elif(arriveTimeInt>=restEnd):
                    timeInterval=(leaveTimeInt-arriveTimeInt).seconds
                elif(leaveTimeInt<=restStart):
                    timeInterval=leaveTimeInt-arriveTimeInt
                else:
                    timeInterval=0
                workTime=round(timeInterval/3600,1)-int(offWorkTime)
                if workTime<0:
                    workTime=0
                if arriveTimeInt<=stdWorkStart:laterWorkFlag=False
                else:laterWorkFlag=True
                if leaveTimeInt>=stdWorkEnd:earlyLeaveFlag=False
                else:earlyLeaveFlag=True
                onJob=True
                result=dct_t_l3f11faam_member_sheet.objects.filter(employee=employee,onjob=onJob,pjcode=pjCode)
                if result.exists():
                    workDay=datetime.datetime.strftime(workDay,'%Y-%m-%d')
                    result=dct_t_l3f11faam_daily_sheet.objects.filter(employee=employee,pjcode=pjCode,workday=workDay)
                    if result.exists():
                        dct_t_l3f11faam_daily_sheet.objects.filter(sid=sid).update(workday=workDay,arraytime=arriveTime,leavetime=leaveTime,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag)
                        return True
                    else:
                        return False
                else:
                    return False
    def dft_dbi_production_history_query(self,inputData):
        ColumnName=[]
        TableData=[]
        ColumnName.append("序号")
        ColumnName.append("二维码")
        ColumnName.append("工人姓名")
        ColumnName.append("产品规格")
        ColumnName.append("申请时间")
        ColumnName.append("成品时间")
        uid=inputData['uid']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        keyWord=inputData['keyWord']
        dayTimeStart=timeStart+' 00:00:00'
        dayTimeEnd=timeEnd+' 23:59:59'
        dayTimeStart=datetime.datetime.strptime(dayTimeStart,'%Y-%m-%d %H:%M:%S')
        dayTimeEnd = datetime.datetime.strptime(dayTimeEnd, '%Y-%m-%d %H:%M:%S')
        pjCode=self.__dft_get_user_auth_factory(uid)
        result=dct_t_l3f11faam_production.objects.filter(Q(pjcode=pjCode),Q(owner__icontains=keyWord)|Q(typecode__icontains=keyWord))
        for line in result:
            applyTime=line.applytime
            applyTime = datetime.datetime.strptime(str(applyTime), '%Y-%m-%d %H:%M:%S.%f')
            if (applyTime>=dayTimeStart) and (applyTime<=dayTimeEnd):
                temp=[]
                temp.append(line.sid)
                temp.append(line.qrcode)
                temp.append(line.owner)
                temp.append(line.typecode)
                temp.append(str(line.applytime))
                temp.append(str(line.activetime))
                TableData.append(temp)
        history={'ColumnName':ColumnName,'TableData':TableData}
        return history
    
    def dft_dbi_production_history_audit(self,inputData):
        ColumnName=[]
        TableData=[]
        Result=True
        uid=inputData['uid']
        user=inputData['user']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        keyWord=inputData['keyWord']
        lever=self.__dft_getUserLever(user)
        ColumnName.append("序号")
        ColumnName.append("员工姓名")
        ColumnName.append("岗位")
        ColumnName.append("区域")
        ColumnName.append("开始日期")
        ColumnName.append("结束日期")
        ColumnName.append("产品规格")
        ColumnName.append("总箱数")
        ColumnName.append("总粒数")
        ColumnName.append("总重量")
        pjCode=self.__dft_get_user_auth_factory(uid)
        dayTimeStart = timeStart + ' 00:00:00'
        dayTimeEnd = timeEnd + ' 23:59:59'
        dayTimeStart = datetime.datetime.strptime(dayTimeStart, '%Y-%m-%d %H:%M:%S')
        dayTimeEnd = datetime.datetime.strptime(dayTimeEnd, '%Y-%m-%d %H:%M:%S')
        buffer=[]
        if keyWord=="":
            result=dct_t_l3f11faam_production.objects.filter(pjcode=pjCode)
            for line in result:
                activeTime=line.activetime
#                 activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
                if activeTime>=dayTimeStart and activeTime<=dayTimeEnd:
                    buffer.append(line)
        else:
            result = dct_t_l3f11faam_production.objects.filter(Q(pjcode=pjCode),Q(owner__icontains=keyWord)|Q(typecode__icontains=keyWord))
            for line in result:
                activeTime=line.activetime
#                 activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
                if activeTime>=dayTimeStart and activeTime<=dayTimeEnd:
                    buffer.append(line)
        if len(buffer)==0:
            history={'ColumnName':ColumnName,'TableData':TableData,'Result':Result}
            return history
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        nameList=[]
        for line in result:
            temp={'employee':line.employee,'position':line.position,'zone':line.zone}
            nameList.append(temp)
        typeList=self.__dft_get_product_type(pjCode)
        package={}
        for i in range(len(buffer)):
            employee=buffer[i].owner
            typeCode=buffer[i].typecode
            package[employee]={}
            if typeCode in package[employee].keys():
                package[employee][typeCode]=package[employee][typeCode]+1
            else:
                package[employee][typeCode]=1
        if lever>1:
            week=datetime.date.today()
            week = week + datetime.timedelta(days=-1)
            week = datetime.datetime.strptime(str(week),"%Y-%m-%d %H:%M:%S")
            if week>dayTimeStart:
                Result=False
                history={'Result':Result,'ColumnName':ColumnName,'TableData':TableData}
                return history
            else:
                Result=True
                sid=0
                packageSum=0
                numSum=0
                weightSum=0
                for i in range(len(nameList)):
                    employee=nameList[i]['employee']
                    position=nameList[i]['position']
                    zone = nameList[i]['zone']
                    for j in range(len(typeList)):
                        typeCode=typeList[j].typecode
                        appleNum=typeList[j].applenum
                        appleWeight=typeList[j].appleweight
                        if employee in package.keys():
                            if typeCode in package[employee].keys():
                                sid = sid + 1
                                totalPackage = int(package[employee][typeCode])
                                totalNum = totalPackage * int(appleNum)
                                totalWeight = totalPackage * appleWeight
                                temp = []
                                temp.append(sid)
                                temp.append(employee)
                                temp.append(position)
                                temp.append(zone)
                                temp.append(timeStart)
                                temp.append(timeEnd)
                                temp.append(typeCode)
                                temp.append(totalPackage)
                                temp.append(totalNum)
                                temp.append(str(totalWeight))
                                TableData.append(temp)
        
                                packageSum = packageSum + totalPackage;
                                numSum = numSum + totalNum
                                weightSum = weightSum + totalWeight
                if packageSum!=0:
                    temp=[]
                    temp.append(0)
                    temp.append("汇总")
                    temp.append("-------")
                    temp.append("-------")
                    temp.append(timeStart)
                    temp.append(timeEnd)
                    temp.append("-------")
                    temp.append(packageSum)
                    temp.append(numSum)
                    temp.append(str(weightSum))
                    TableData.append(temp)
                history={'Result':Result,'TableData':TableData,'ColumnName':ColumnName}
                return history
        else:
            Result = True
            sid = 0
            packageSum = 0
            numSum = 0
            weightSum = 0
            for i in range(len(nameList)):
                employee = nameList[i]['employee']
                position = nameList[i]['position']
                zone = nameList[i]['zone']
                for j in range(len(typeList)):
                    typeCode = typeList[j].typecode
                    appleNum = typeList[j].applenum
                    appleWeight = typeList[j].appleweight
                    if employee in package.keys():
                        if typeCode in package[employee].keys():
                            sid = sid + 1
                            totalPackage = int(package[employee][typeCode])
                            totalNum = totalPackage * int(appleNum)
                            totalWeight = totalPackage * appleWeight
                            temp = []
                            temp.append(sid)
                            temp.append(employee)
                            temp.append(position)
                            temp.append(zone)
                            temp.append(timeStart)
                            temp.append(timeEnd)
                            temp.append(typeCode)
                            temp.append(totalPackage)
                            temp.append(totalNum)
                            temp.append(str(totalWeight))
                            TableData.append(temp)
    
                            packageSum = packageSum + totalPackage;
                            numSum = numSum + totalNum
                            weightSum = weightSum + totalWeight
            if packageSum != 0:
                temp = []
                temp.append(0)
                temp.append("汇总")
                temp.append("-------")
                temp.append("-------")
                temp.append(timeStart)
                temp.append(timeEnd)
                temp.append("-------")
                temp.append(packageSum)
                temp.append(numSum)
                temp.append(str(weightSum))
                TableData.append(temp)
            history = {'Result': Result, 'TableData': TableData, 'ColumnName': ColumnName}
            return history
        
    def dft_dbi_employee_kpi_audit(self,inputData):
        ColumnName=[]
        TableData=[]
        uid=inputData['uid']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        keyWord=inputData['keyWord']
        ColumnName.append("序号")
        ColumnName.append("员工姓名")
        ColumnName.append("岗位")
        ColumnName.append("区域")
        ColumnName.append("开始日期")
        ColumnName.append("结束日期")
        ColumnName.append("工作天数")
        ColumnName.append("工作时间")
        ColumnName.append("现时薪")
        ColumnName.append("总时薪")
        ColumnName.append("总箱数")
        ColumnName.append("总重量")
        ColumnName.append("总粒数")
        ColumnName.append("标准绩效")
        ColumnName.append("完成比例")
        pjCode=self.__dft_get_user_auth_factory(uid)
        dayTimeStart = timeStart + ' 00:00:00'
        dayTimeEnd = timeEnd + ' 23:59:59'
        dayTimeStart = datetime.datetime.strptime(dayTimeStart, '%Y-%m-%d %H:%M:%S')
        dayTimeEnd = datetime.datetime.strptime(dayTimeEnd, '%Y-%m-%d %H:%M:%S')
        workBuf=[]
        if keyWord!="":
            result=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode,employee=keyWord)
            for line in result:
                workDay=str(line.workday)
                workDay=datetime.datetime.strptime(str(workDay),'%Y-%m-%d')
                if workDay>=dayTimeStart and workDay<=dayTimeEnd:
                    workBuf.append(line)
        else:
            result=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode)
            for line in result:
                workDay=str(line.workday)
                workDay=datetime.datetime.strptime(str(workDay),'%Y-%m-%d')
                if workDay>=dayTimeStart and workDay<=dayTimeEnd:
                    workBuf.append(line)
        productBuf = []
        if keyWord != "":
            result = dct_t_l3f11faam_production.objects.filter(pjcode=pjCode, owner=keyWord)
            for line in result:
                activeTime = line.activetime
                print(activeTime)
                if activeTime >= dayTimeStart and activeTime <= dayTimeEnd:
                    productBuf.append(line)
        else:
            result = dct_t_l3f11faam_production.objects.filter(pjcode=pjCode)
            for line in result:
                activeTime = line.activetime
                if activeTime >= dayTimeStart and activeTime <= dayTimeEnd:
                    productBuf.append(line)
        print(productBuf)
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        nameList=[]
        for line in result:
            temp={'employee':line.employee,'unitprice':line.unitprice,'position':line.position,'zone':line.zone}
            nameList.append(temp)
        typeList=self.__dft_get_product_type(pjCode)
        workingDay={}
        totalWorkTime={}
        totalTimeSalary={}
        standardNumList={}
        packageSum={}
        numSum={}
        weightSum={}
        for i in range(len(workBuf)):
            employee=workBuf[i].employee
            workTime=workBuf[i].worktime
            dayStandardNum=workBuf[i].daystandardnum
            if (employee in workingDay.keys()) and (employee in totalWorkTime.keys()) and (employee in totalTimeSalary.keys()):
                if workTime!=0:
                    workingDay[employee]=workingDay[employee]+1
                    totalWorkTime[employee] = totalWorkTime[employee] + workTime
                    totalTimeSalary[employee]=totalTimeSalary[employee]+workBuf[i].unitprice*workBuf[i].worktime
            else:
                if workTime!=0:
                    workingDay[employee]=1
                    totalWorkTime[employee] = workTime
                    totalTimeSalary[employee]=workBuf[i].unitprice *workBuf[i].worktime
                else:
                    workingDay[employee] = 0
                    totalWorkTime[employee] = 0
                    totalTimeSalary[employee] = 0
            if employee in standardNumList.keys():
                standardNumList[employee]=standardNumList[employee]+dayStandardNum
            else:
                standardNumList[employee]=dayStandardNum
        package={}
        for i in range(len(productBuf)):
            employee=productBuf[i].owner
            typeCode=productBuf[i].typecode
            package[employee]={}
            if typeCode in package[employee].keys():
                package[employee][typeCode]=package[employee][typeCode]+1
            else:
                package[employee][typeCode]=1
        for i in range(len(nameList)):
            employee=nameList[i]['employee']
            totalPackage=0
            totalNum=0
            totalWeight=0
            for j in range(len(typeList)):
                typeCode=typeList[j].typecode
                appleNum=typeList[j].applenum
                appleWeight=typeList[j].appleweight
                if employee in package.keys():
                    if typeCode in package[employee].keys():
                        perPackage=int(package[employee][typeCode])
                        totalPackage+=perPackage
                        totalNum+=perPackage*int(appleNum)
                        totalWeight+=perPackage*int(appleWeight)
            if (totalPackage==0) or (totalNum==0) or (totalWeight==0):
                continue
            
            packageSum[employee]=totalPackage
            numSum[employee]=totalNum
            weightSum[employee]=totalWeight
        sid=0
        for i in range(len(nameList)):
            position=nameList[i]['position']
            zone=nameList[i]['zone']
            employee=nameList[i]['employee']
            unitPrice=nameList[i]['unitprice']
            if (employee in workingDay.keys()) and (employee in totalWorkTime.keys()):
                if employee in packageSum.keys():tempPackageSum=packageSum[employee]
                else:tempPackageSum=0
                if employee in weightSum.keys():tempWeightSum=weightSum[employee]
                else:tempWeightSum=0
                if employee in numSum.keys():tempNumSum=numSum[employee]
                else:tempNumSum=0
                if employee in standardNumList.keys():totalStandardNum=standardNumList[employee]
                else:totalStandardNum=0

                if totalStandardNum!=0:
                    kpiSalary=str(round((tempNumSum/totalStandardNum)*100,2))+'%'
                else:
                    kpiSalary='%'
                sid=sid+1
                temp=[]
                temp.append(sid)
                temp.append(employee)
                temp.append(position)
                temp.append(zone)
                temp.append(timeStart)
                temp.append(timeEnd)
                temp.append(workingDay[employee])
                temp.append(totalWorkTime[employee])
                temp.append(unitPrice)
                temp.append(totalTimeSalary[employee])
                temp.append(tempPackageSum)
                temp.append(tempWeightSum)
                temp.append(tempNumSum)
                temp.append(totalStandardNum)
                temp.append(kpiSalary)
                TableData.append(temp)
        total=[]
        Day=0
        Time=0
        Salary=0
        Num=0
        Weight=0
        Apple=0
        for i in range(len(TableData)):
            Day=Day+TableData[i][6]
            Time=Time+TableData[i][7]
            Salary=Salary+TableData[i][9]
            Num=Num+TableData[i][10]
            Weight=Weight+TableData[i][11]
            Apple=Apple+TableData[i][12]
        total.append(0)
        total.append("汇总")
        total.append("-----")
        total.append("-----")
        total.append(timeStart)
        total.append(timeEnd)
        total.append(Day)
        total.append(Time)
        total.append("-----")
        total.append(Salary)
        total.append(Num)
        total.append(Weight)
        total.append(Apple)
        total.append("-----")
        total.append("-----")
        TableData.append(total)
        history={'ColumnName':ColumnName,'TableData':TableData}
        return history
    
    def dft_dbi_consumables_buy(self,inputData):
        supplier=inputData['vendor']
        datatype=inputData['item']
        number=inputData['number']
        unit_price=inputData['unit']
        total_price=inputData['total']
        datype=inputData['type']
        print(datatype)
        if datatype=='1':contype='纸箱'
        elif datatype=='2':contype='保鲜袋'
        elif datatype=='3':contype='胶带'
        elif datatype=='4':contype='标签'
        elif datatype=='5':contype='托盘'
        elif datatype=='6':contype='垫片'
        elif datatype=='7':contype='网套'
        elif datatype=='8':contype='打包带'
        storage_time=datetime.datetime.now()
        print(storage_time)
        dct_t_l3f11faam_buy_consumables.objects.create(supplier=supplier,contype=contype,amount=number,unitprice=unit_price,totalprice=total_price,createtime=storage_time,datatype=datype)
        result=dct_t_l3f11faam_buy_consumables.objects.filter(createtime=storage_time)
        if result.exists():
            for line in result:
                consumable={'consumablespurchaseID':line.sid}
        else:
            consumable={}
        return consumable
    def dft_dbi_get_print(self,inputData):
        sid=inputData['itemid']
        PrintColumn=[]
        PrintDetail=[]
        PrintColumn.append('项目')
        PrintColumn.append('内容')
        result=dct_t_l3f11faam_buy_consumables.objects.filter(sid=sid)
        key=["序号","耗材类型","供应商","耗材规格","数量","单价","总价","入库时间"]
        if result.exists():
            for line in result:
                value=[line.sid,line.contype,line.supplier,line.datatype,line.amount,str(line.unitprice),str(line.totalprice),str(line.createtime)]
                for i in range(len(key)):
                    PrintItem=[]
                    ss=value[i]
                    PrintItem.append(key[i])
                    PrintItem.append(ss)
                    PrintDetail.append(PrintItem)
        PrintTable={'column':PrintColumn,'detail':PrintDetail}
        return PrintTable
        
    def dft_dbi_consumables_table(self):
        ColumnName=[]
        TableData=[]
        dataType=["纸箱","网套","托盘","胶带","标签","保鲜袋","打包带","垫片"]
        sid=1
        total_number=[0,0,0,0,0,0,0,0]
        total_money=[0,0,0,0,0,0,0,0]
        final_time=['0','0','0','0','0','0','0','0']
        ColumnName.append("序号")
        ColumnName.append("名称")
        ColumnName.append("历史总量")
        ColumnName.append("历史总价")
        ColumnName.append("历史平均价格")
        ColumnName.append("最后一次入库时间")
        result=dct_t_l3f11faam_buy_consumables.objects.all()
        if result.exists():
            for line in result:
                if line.contype=='纸箱':
                    total_money[0]=total_money[0]+line.totalprice
                    total_number[0]=total_number[0]+line.amount
                    final_time[0]=str(line.createtime)
                elif line.contype=='网套':
                    total_money[1] = total_money[1] + line.totalprice
                    total_number[1] = total_number[1] + line.amount
                    final_time[1] = str(line.createtime)
                elif line.contype=='托盘':
                    total_money[2] = total_money[2] + line.totalprice
                    total_number[2] = total_number[2] + line.amount
                    final_time[2] = str(line.createtime)
                elif line.contype=='胶带':
                    total_money[3] = total_money[3] + line.totalprice
                    total_number[3] = total_number[3] + line.amount
                    final_time[3] = str(line.createtime)
                elif line.contype=='标签':
                    total_money[4] = total_money[4] + line.totalprice
                    total_number[4] = total_number[4] + line.amount
                    final_time[4] = str(line.createtime)
                elif line.contype=='保鲜袋':
                    total_money[5] = total_money[5] + line.totalprice
                    total_number[5] = total_number[5] + line.amount
                    final_time[5] = str(line.createtime)
                elif line.contype=='打包带':
                    total_money[6] = total_money[6] + line.totalprice
                    total_number[6] = total_number[6] + line.amount
                    final_time[6] = str(line.createtime)
                elif line.contype=='垫片':
                    total_money[7] = total_money[7] + line.totalprice
                    total_number[7] = total_number[7] + line.amount
                    final_time[7] = str(line.createtime)
            for m in range(len(dataType)):
                temp=[]
                if total_number[m]==0:
                    temp.append(sid)
                    temp.append(dataType[m])
                    temp.append('暂无数据')
                    temp.append('暂无数据')
                    temp.append('暂无数据')
                    temp.append('暂无数据')
                else:
                    if total_money[m]==0:
                        price=0
                    else:
                        price=total_money[m]/total_number[m]
                    temp.append(sid)
                    temp.append(dataType[m])
                    temp.append(str(total_number[m]))
                    temp.append(str(total_money[m]))
                    temp.append(str(round(price,3)))
                    temp.append(final_time[m])
                TableData.append(temp)
                sid=sid+1
        table={'ColumnName':ColumnName,'TableData':TableData}
        return table
        
    def dft_dbi_consumables_history_table(self,inputData):
        key=inputData['key']
        timeStart=inputData['timeStart']
        timeEnd=inputData['timeEnd']
        timeStart=datetime.datetime.strptime(timeStart, '%Y-%m-%d %H:%M:%S.%f')
        timeEnd=datetime.datetime.strptime(timeEnd,'%Y-%m-%d %H:%M:%S.%f')
        keyWord=inputData['keyWord']
        ColumnName=[]
        TableData=[]
        sid=1
        ColumnName.append('序号')
        ColumnName.append('名称')
        ColumnName.append('单价')
        ColumnName.append('数量')
        ColumnName.append('总价')
        ColumnName.append('规格')
        ColumnName.append('供应商')
        ColumnName.append('入库时间')
        if keyWord=="":
            if key=="":
                result=dct_t_l3f11faam_buy_consumables.objects.filter(createtime__gte=timeStart,createtime__lte=timeEnd)
            else:
                result=dct_t_l3f11faam_buy_consumables.objects.filter(contype=key,createtime__gte=timeStart,createtime__lte=timeEnd)
        else:
            if key=="":
                result=dct_t_l3f11faam_buy_consumables.objects.filter(createtime__gte=timeStart,createtime__lte=timeEnd,supplier__icontains=keyWord)
            else:
                result=dct_t_l3f11faam_buy_consumables.objects.filter(contype=key,createtime__gte=timeStart,createtime__lte=timeEnd,supplier__icontains=keyWord)
        if result.exists():
            for line in result:
                temp=[]
                temp.append("")
                temp.append(sid)
                temp.append(line.contype)
                temp.append(str(line.unitprice))
                temp.append(str(line.amount))
                temp.append(str(line.totalprice))
                temp.append(line.datatype)
                temp.append(line.supplier)
                temp.append(str(line.createtime))
                TableData.append(temp)
                sid=sid+1
        history={"ColumnName":ColumnName,"TableData":TableData}
        return history
    
    def dft_dbi_get_consumbales_purchase(self,inputData):
        consumables_key=['consumablespurchaseID','item','number','unit','total','vendor','type']
        consumables_value=[]
        sid=inputData['sid']
        result=dct_t_l3f11faam_buy_consumables.objects.filter(sid=sid)
        for line in result:
            consumables_value.append(line.sid)
            if line.contype=="纸箱":consumables_value.append('1')
            elif line.contype=="保鲜袋":consumables_value.append('2')
            elif line.contype=="胶带":consumables_value.append('3')
            elif line.contype=="标签":consumables_value.append('4')
            elif line.contype=="托盘":consumables_value.append('5')
            elif line.contype=="垫片":consumables_value.append('6')
            elif line.contype=="网套":consumables_value.append('7')
            elif line.contype=="打包带":consumables_value.append('8')
            else:break
            consumables_value.append(line.amount)
            consumables_value.append(int(line.unitprice))
            consumables_value.append(int(line.totalprice))
            consumables_value.append(line.supplier)
            consumables_value.append(line.datatype)
            ConsumablesTable=dict(zip(consumables_key,consumables_value))
            print()
        return ConsumablesTable
        
        
        
        
        
        
        
        
        
        
        
        
        
        
