from django.shortcuts import render
import random
import time
import datetime
import os
import stat
from django.db.models import Q
from datetime import timedelta
from DappDbF11faam.models import *
from DappDbF1sym.models import *
from _datetime import date
class dct_classDbiL3apF11Faam:
    __MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR = '/xhzn/avorion/userphoto/'
    __HUITP_IEID_UNI_COM_CONFIRM_YES = 0X01
    __HUITP_IEID_UNI_COM_CONFIRM_NO = 0X02
    __HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_TRUE = 2
    __HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_FALSE = 1
    def __init__(self):
        pass
    def __dft_getUserLever(self,inputData):
        sessionid=inputData
        result=dct_t_l3f1sym_user_login_session.objects.get(session_id=sessionid)
        if result:
            userLever=result.uid.grade_level
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
            file_link_new=self.__MFUN_HCU_FAAM_EMPLOYEE_PHOTO_WWW_DIR+file_new_name
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
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        for line in result:
            temp={'id':line.mid,'name':line.employee}
            nameList.append(temp)
        return nameList
    
    def dft_dbi_employee_number_inquery(self,inputData):
        uid=inputData['uid']
        pjCode=self.__dft_get_user_auth_factory(uid)
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        return len(result)
    
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
                daystandnumbet=line.standardnum
                Daily=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=pjCode,employee=employee,workday=workDay)
                if Daily.exists():
                    pass
                else:
                    dct_t_l3f11faam_daily_sheet.objects.create(pjcode=pjCode,daystandardnum=daystandnumbet,employee=employee,workday=workDay,arrivetime=workStart,leavetime=workEnd,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag)
                    
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
                        arriveTime=line.arrivetime
                        
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
                    arriveTime = line.arrivetime
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
                temp.append(str(lateWorkDay[employee]))
                temp.append(str(earlyLeaveDay[employee]))
                temp.append(str(offWorkDay[employee]))
                temp.append(str(totalOffWorkTime[employee]))
                temp.append(str(workingDay[employee]))
                temp.append(str(totalWorkTime[employee]))
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
#                         print(pjCode,employee,workDay,arriveTime,leaveTime,offWorkTime,workTime,unitPrice,laterWorkFlag,earlyLeaveFlag)
                        dct_t_l3f11faam_daily_sheet.objects.create(pjcode=pjCode,employee=employee,workday=workDay,arrivetime=arriveTime,leavetime=leaveTime,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag,daystandardnum=standnumber)
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
                        'arrivetime':str(line.arrivetime),
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
                workTime=round(timeInterval/3600,1)-float(offWorkTime)
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
                        dct_t_l3f11faam_daily_sheet.objects.filter(sid=sid).update(workday=workDay,arrivetime=arriveTime,leavetime=leaveTime,offwork=offWorkTime,worktime=workTime,unitprice=unitPrice,laterflag=laterWorkFlag,earlyflag=earlyLeaveFlag)
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
            applyTime = datetime.datetime.strptime(str(applyTime), '%Y-%m-%d %H:%M:%S')
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
                if activeTime==None:
                    activeTime="1900-01-01 00:00:00"
                    activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
                if activeTime>=dayTimeStart and activeTime<=dayTimeEnd:
                    buffer.append(line)
        else:
            result = dct_t_l3f11faam_production.objects.filter(Q(pjcode=pjCode),Q(owner__icontains=keyWord)|Q(typecode__icontains=keyWord))
            for line in result:
                activeTime=line.activetime
                if activeTime==None:
                    activeTime="1900-01-01 00:00:00"
                    activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
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
            if employee in package.keys():
                pass
            else:
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
                if activeTime==None:
                    activeTime="1900-01-01 00:00:00"
                    activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
                if activeTime >= dayTimeStart and activeTime <= dayTimeEnd:
                    productBuf.append(line)
        else:
            result = dct_t_l3f11faam_production.objects.filter(pjcode=pjCode)
            for line in result:
                activeTime = line.activetime
                if activeTime==None:
                    activeTime="1900-01-01 00:00:00"
                    activeTime=datetime.datetime.strptime(activeTime, '%Y-%m-%d %H:%M:%S')
                if activeTime >= dayTimeStart and activeTime <= dayTimeEnd:
                    productBuf.append(line)
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
            if employee in package.keys():
                pass
            else:
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
                    kpiSalary=str(round((tempPackageSum/totalStandardNum)*100,2))+'%'
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
        if datatype=='1':contype='纸箱'
        elif datatype=='2':contype='保鲜袋'
        elif datatype=='3':contype='胶带'
        elif datatype=='4':contype='标签'
        elif datatype=='5':contype='托盘'
        elif datatype=='6':contype='垫片'
        elif datatype=='7':contype='网套'
        elif datatype=='8':contype='打包带'
        storage_time=datetime.datetime.now()
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
        return ConsumablesTable
    def dft_dbi_consumables_purchase_mod(self,inputData):
        storage_time = datetime.datetime.now()
        sid=inputData['consumablespurchaseID']
        item=inputData['item']
        number=inputData['number']
        unit=inputData['unit']
        total=inputData['total']
        vendor=inputData['vendor']
        if item=='1':type='纸箱'
        elif item=='2':type='保鲜袋'
        elif item=='3':type='胶带'
        elif item=='4':type='标签'
        elif item=='5':type='托盘'
        elif item=='6':type='垫片'
        elif item=='7':type='网套'
        elif item=='8':type='打包带'
        else:type=""
        if type=="":
            return False
        else:
            dct_t_l3f11faam_buy_consumables.objects.filter(sid=sid).update(supplier=vendor,contype=type,amount=number,
                                                           unitprice=unit,totalprice=total,createtime=storage_time)
            return True
        
    def dft_dbi_consumables_purchase_del(self,inputData):
        sid=inputData['consumablespurchaseID']
        dct_t_l3f11faam_buy_consumables.objects.filter(sid=sid).delete()
        return True
    
    def dft_dbi_product_stock_new(self,inputData):
        name=inputData['name']
        address=inputData['address']
        result=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name)
        data_now=datetime.datetime.now()
        if result.exists():
            dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name,stockaddress=address,createtime=data_now)
        else:
            productweight=0
            productnum=0
            number=0
            dct_t_l3f11faam_product_stock_sheet.objects.create(stockname=name,stockaddress=address,productweight=productweight,productnum=productnum,number=number,createtime=data_now,updatetime=data_now)
    
    def dft_dbi_get_product_weight_and_size(self):
        weight=[]
        size=[]
        result=dct_t_l3f11faam_type_sheet.objects.all()
        for line in result:
            if str(line.appleweight)+'KG' not in weight:
                weight.append(str(line.appleweight)+'KG')
            if line.applegrade=='A':grade='特级'
            elif line.applegrade=='1':grade='一级'
            elif line.applegrade=='2':grade='二级'
            elif line.applegrade=='3':grade='三级'
            elif line.applegrade=='S':grade='混合'
            if grade not in size:
                size.append(grade)
        product={'weight':weight,'size':size}
        return product

    def dft_dbi_get_product_stock_list(self):
        table=[]
        name=[]
        result=dct_t_l3f11faam_product_stock_sheet.objects.all()
        for line in result:
            if line.stockname not in name:
                name.append(line.stockname)
                cargo={'id':str(line.sid),'name':line.stockname,'address':line.stockaddress}
                table.append(cargo)
            else:
                continue
        return table

    def dft_dbi_get_product_empty_stock(self):
        empty = []
        name=[]
        result=dct_t_l3f11faam_product_stock_sheet.objects.all()
        for line in result:
            if line.stockname not in name:
                name.append(line.stockname)
        for nameList in name:
            total_number=0
            result=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=nameList)
            for line in result:
                total_number=total_number+int(line.number)
                id=line.sid
                address=line.stockaddress
            if total_number==0:
                temp = {'id': id, 'name': nameList, 'address': address}
                empty.append(temp)
            else:
                continue
        return empty

    def dft_dbi_product_stock_del(self,inputData):
        id=int(inputData['stockID'])
        name=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=id).stockname
        result=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name)
        totalNum=0
        for line in result:
            totalNum=totalNum+line.number
        if totalNum<=0:
            dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name).delete()
            return True
        else:
            return False

    def dft_dbi_product_stock_table(self,inputData):
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('库名')
        ColumnName.append('重量/箱')
        ColumnName.append('规格')
        ColumnName.append('粒数/箱')
        ColumnName.append('箱数')
        ColumnName.append('仓库地址')
        ColumnName.append('最后操作时间')
        ColumnName.append('备注')
        id=inputData['StockID']
        Period=inputData['Period']
        size=inputData['KeyWord']
        if id=="":
            if Period=="" and size=="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.all()
            elif Period!="" and size=="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(productweight=Period)
            elif Period=="" and size!="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(puoductsize=size)
            elif Period!="" and size!="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(productweight=Period, puoductsize=size)
        else:
            name=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=id).stockname
            if Period=="" and size=="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name)
            elif Period!="" and size=="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(productweight=Period,stockname=name)
            elif Period=="" and size!="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(puoductsize=size,stockname=name)
            elif Period!="" and size!="":
                result = dct_t_l3f11faam_product_stock_sheet.objects.filter(productweight=Period, puoductsize=size,stockname=name)
        i=1
        for line in result:
            if line.puoductsize=="A":type="特级"
            elif line.puoductsize=='1':type='一级'
            elif line.puoductsize=='2':type='二级'
            elif line.puoductsize=='3':type='三级'
            elif line.puoductsize=='S':type='混合'
            else:type='暂无数据'
            temp=[]
            temp.append(str(line.sid))
            temp.append(str(i))
            temp.append(line.stockname)
            temp.append(str(line.productweight)+'KG')
            temp.append(type)
            temp.append(line.productnum)
            temp.append(line.number)
            temp.append(line.stockaddress)
            temp.append(str(line.updatetime))
            temp.append(line.message)
            TableData.append(temp)
            i=i+1
        product={'ColumnName':ColumnName,'TableData':TableData}
        return product

    def dft_dbi_get_product_stock_detail(self,inputData):
        sid=int(inputData['stockID'])
        result=dct_t_l3f11faam_product_stock_sheet.objects.filter(sid=sid)
        for line in result:
            name=line.stockname
            weight=str(line.productweight*1.0)+'KG'
            if line.puoductsize == "A":
                type = "特级"
            elif line.puoductsize == '1':
                type = '一级'
            elif line.puoductsize == '2':
                type = '二级'
            elif line.puoductsize == '3':
                type = '三级'
            elif line.puoductsize == 'S':
                type = '混合'
            else:type='暂无数据'
            list=self.dft_dbi_get_product_stock_list()
            for i in range(len(list)):
                if name==list[i]['name']:
                    id=str(list[i]['id'])
            #table={"ID":sid,'storageID':str(id),'size':type,'weight':weight,'maxStorage':'100'}
            table={'storageID':str(id),'size':type,'weight':weight,'maxStorage':'100'}
        return table
    #因为部分数据暂时无法进行实际的实现
    def dft_dbi_product_stock_transfer(self,inputData):
        storageID=int(inputData['storageID'])
        weight=float(inputData['weight'].strip().strip('KG'))
        size=inputData['size']
        number=int(inputData['number']) #转移的数量
        target=inputData['target'] #目标库
        note=inputData['note']
        date_now=datetime.datetime.now()
        if size=='特级':size='A'
        elif size=='一级':size='1'
        elif size=='二级':size='2'
        elif size=='三级':size='3'
        elif size=='混合':size='S'
        else:return False
        result=dct_t_l3f11faam_product_stock_sheet.objects.filter(sid=storageID)
        for line in result:
            name=line.stockname
        result=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name,productweight=weight,puoductsize=size,productnum=28)
        for line in result:
            productNum=line.productnum #每箱苹果的数量
            productNumber=line.number #仓库的现存数量
        if number>productNumber:
            return False
        else:
            out_stock=dct_t_l3f11faam_product_stock_sheet.objects.get(stockname=name,productweight=weight,puoductsize=size,productnum=28)
            out_stock.number=(productNumber-number)
            out_stock.updatetime=date_now
            out_stock.message=note
            out_stock.save(update_fields=['number','updatetime','message'])
            intoStockInfo=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=target)
            into_stock=dct_t_l3f11faam_product_stock_sheet.objects.filter(sid=target,productweight=weight,puoductsize=size,productnum=productNum)
            if into_stock.exists():
                update_stock=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=target,productweight=weight,puoductsize=size,productnum=productNum)
                update_stock.number=(into_stock[0].number+number)
                update_stock.message=note
                update_stock.updatetime=date_now
#                 into_stock[0].save(update_fields=['productweight','puoductsize','productnum','number','message','updatetime'])
                update_stock.save(update_fields=['number','message','updatetime'])
                dct_t_l3f11faam_product_history.objects.create(stockname=name,productweight=weight,puoductsize=size,productnum=productNum,
                                                               number=number,containerID='---',platenumber='---',
                                                               drivername='---',driverphone='---',receivingunit=intoStockInfo.stockname,logisticsunit='---',
                                                               message=note)
            else:
                if intoStockInfo:
                    intoStockInfo.productweight=weight
                    intoStockInfo.puoductsize=size
                    intoStockInfo.productnum=productNum
                    intoStockInfo.number=number
                    intoStockInfo.updatetime=date_now
                    intoStockInfo.message=note
                    intoStockInfo.save(update_fields=['productweight','puoductsize','productnum','number','updatetime','message'])
                    dct_t_l3f11faam_product_history.objects.create(stockname=name, productweight=weight,
                                                                   puoductsize=size, productnum=productNum,
                                                                   number=number, containerID='---', platenumber='---',
                                                                   drivername='---', driverphone='---',
                                                                   receivingunit=intoStockInfo.stockname, logisticsunit='---',
                                                                   message=note)
                else:
                    dct_t_l3f11faam_product_stock_sheet.objects.create(message=note,stockname=intoStockInfo.stockname,createtime=intoStockInfo.createtime,stockaddress=intoStockInfo.stockaddress,productweight=weight,puoductsize=size,productnum=productNum,updatetime=date_now,number=number)
                    dct_t_l3f11faam_product_history.objects.create(stockname=name, productweight=weight,
                                                                   puoductsize=size, productnum=productNum,
                                                                   number=number, containerID='---', platenumber='---',
                                                                   drivername='---', driverphone='1---',
                                                                   receivingunit=intoStockInfo.stockname, logisticsunit='---',
                                                                   message=note)
            return True
    #因为部分数据无法获取到，所以暂时将该处理函数进行搁置
    def dft_dbi_product_stock_removal_new(self,inputData):
        dateNow=datetime.datetime.now()
        storageID=inputData['storageID']
        weight=int(inputData['weight'])
        size=inputData['size']
        number=int(inputData['number'])
        container=inputData['container']
        trunk=inputData['trunk']
        mobile=inputData['mobile']
        driver=inputData['driver']
        target=inputData['target']
        logistics=inputData['logistics']
        if size=='特级':size='A'
        elif size=='一级':size='1'
        elif size=='二级':size='2'
        elif size=='三级':size='3'
        elif size=='混合':size='S'
        else:size=""
        reuslt=dct_t_l3f11faam_product_stock_sheet.objects.filter(sid=storageID)
        for line in reuslt:
            name=line.stockname
            productNum=line.productnum
            productNumber=line.number
            if number>productNumber:
                return False
            else:
                out_stock=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=storageID)
                out_stock.number=productNum-number
                out_stock.save(update_fields=['number'])
                dct_t_l3f11faam_product_history.objects.create(stockname=name,productweight=weight,
                                                               puoductsize=size,productnum=productNum,
                                                               number=number,containerID=container,platenumber=trunk,
                                                               drivername=driver,driverphone=mobile,
                                                               receivingunit=target,logisticsunit=logistics
                                                               ,message=str(dateNow)+'，正常出库')
                return True
    def dft_dbi_product_stock_history(self,inputData):
        timeEnd=datetime.date.today()
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('出库方')
        ColumnName.append('重量/箱')
        ColumnName.append('规格')
        ColumnName.append('粒数/箱')
        ColumnName.append('箱数')
        ColumnName.append('集装箱号')
        ColumnName.append('车牌号')
        ColumnName.append('司机姓名')
        ColumnName.append('司机手机')
        ColumnName.append('收货单位')
        ColumnName.append('物流单位')
        ColumnName.append('出库时间')
        ColumnName.append('备注')
        stockID=inputData['StockID']
        keyWord=inputData['KeyWord']
        period=inputData['Period']
        if stockID=='all':stockID=''
        else:stockID=int(stockID)
        if period=='1':
            timeStart=timeEnd
        elif period=='7':
            timeStart=timeEnd-timedelta(days=6)
        elif period=='30':
            timeStart = timeEnd - timedelta(days=29)
        elif period=='all':
            timeStart='0001-01-01'
        timeStart=datetime.datetime.strptime((str(timeStart)+' 00:00:00.000000'), '%Y-%m-%d %H:%M:%S.%f')
        timeEnd=datetime.datetime.strptime((str(timeEnd)+' 23:59:59.999999'), '%Y-%m-%d %H:%M:%S.%f')
        if stockID=="":
            stockName=""
        else:
            result=dct_t_l3f11faam_product_stock_sheet.objects.get(sid=stockID)
            stockName=result.stockname
        if stockName=="":
            if keyWord=="":
                result=dct_t_l3f11faam_product_history.objects.filter(outtime__gte=timeStart,outtime__lte=timeEnd)
            else:
                result = dct_t_l3f11faam_product_history.objects.filter(outtime__gte=timeStart,outtime__lte=timeEnd,drivername__icontains=keyWord)
        else:
            if keyWord=="":
                result=dct_t_l3f11faam_product_history.objects.filter(stockname=stockName,outtime__gte=timeStart,outtime__lte=timeEnd)
            else:
                result = dct_t_l3f11faam_product_history.objects.filter(stockname=stockName,drivername__icontains=keyWord,outtime__gte=timeStart,outtime__lte=timeEnd)
        i=1
        for line in result:
            if line.puoductsize=="A":size='特级'
            elif line.puoductsize=="1":size='一级'
            elif line.puoductsize=="2":size='二级'
            elif line.puoductsize=="3":size='三级'
            elif line.puoductsize=="S":size='混合'
            else:size=""
            middle=[]
            if line.containerID=='---':
                middle.append("")
            else:
                middle.append(str(line.sid))
            middle.append(i)
            middle.append(line.stockname)
            middle.append(line.productweight)
            middle.append(size)
            middle.append(line.productnum)
            middle.append(line.number)
            middle.append(line.containerID)
            middle.append(line.platenumber)
            middle.append(line.drivername)
            middle.append(line.driverphone)
            middle.append(line.receivingunit)
            middle.append(line.logisticsunit)
            middle.append(str(line.outtime))
            middle.append(line.message)
            TableData.append(middle)
            i=i+1
        history={'ColumnName':ColumnName,'TableData':TableData}
        return history
    def dft_dbi_get_product_stock_history_detail(self,inputData):
        ID=inputData['removalID']
        result=dct_t_l3f11faam_product_history.objects.filter(sid=ID)
        for line in result:
            stockID=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=line.stockname)[0].sid
            if line.puoductsize=="A":size='特级'
            elif line.puoductsize=="1":size='一级'
            elif line.puoductsize=="2":size='二级'
            elif line.puoductsize=="3":size='三级'
            elif line.puoductsize=="S":size='混合'
            else:size=""
            weight=str(line.productweight)+'KG'
            number=str(line.number)
            container=line.containerID
            trunk=line.platenumber
            driver=line.drivername
            mobile=line.driverphone
            target=line.receivingunit
            logistics=line.logisticsunit
            result={'storageID':stockID,'weight':weight,'size':size,'number':number,'container':container,'trunk':trunk,'driver':driver,'mobile':mobile,'target':target,'logistics':logistics}
        return result
    def dft_dbi_material_stock_new(self,inputData):
        #0 自有 1 第三方
        name=inputData['name']
        address=inputData['address']
        isself=int(inputData['mode'])
        if isself==0:
            Tableisself=True
        else:
            Tableisself=False
        result=dct_t_l3f11faam_material_stock_table.objects.filter(stockname=name)
        if result.exists():
            dct_t_l3f11faam_material_stock_table.objects.filter(stockname=name).update(stockaddress=address,isself=Tableisself)
        else:
            dct_t_l3f11faam_material_stock_table.objects.create(stockname=name,stockaddress=address,stockleader="-",isself=Tableisself,bucketnum=0,totalprice=0)

    def dft_dbi_get_material_stock_list(self):
        result=dct_t_l3f11faam_material_stock_table.objects.all()
        stock_list=[]
        for line in result:
            id=line.sid
            name=line.stockname
            address=line.stockaddress
            cargo={'id':str(id),'name':name,'address':address}
            stock_list.append(cargo)
        return stock_list
    def dft_dbi_get_material_empty_stock(self):
        result=dct_t_l3f11faam_material_stock_table.objects.filter(bucketnum=0)
        empty_list=[]
        for line in result:
            id=line.sid
            name=line.stockname
            address=line.stockaddress
            cargo={'id':str(id),'name':name,'address':address}
            empty_list.append(cargo)
        return empty_list
    def dft_dbi_empty_material_stock_del(self,inputData):
        id=inputData['stockID']
        result=dct_t_l3f11faam_material_stock_table.objects.filter(sid=id)
        for line in result:
            if line.bucketnum<=0:
                result.delete()
            else:
                return False
    def dft_dbi_material_stock_table(self,inputData):
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('库名')
        ColumnName.append('自有')
        ColumnName.append('桶数')
        ColumnName.append('总费用')
        ColumnName.append('最后一次操作时间')
        ColumnName.append('仓库地址')
        if inputData['StockID']=='all':
            result=dct_t_l3f11faam_material_stock_table.objects.all()
        else:
            ID=int(inputData['StockID'])
            result=dct_t_l3f11faam_material_stock_table.objects.filter(sid=ID)
        i=1
        for line in result:
            table=[]
            id=line.sid
            name=line.stockname
            address=line.stockaddress
            isself=line.isself
            if isself==True:
                mode='是'
            else:
                mode='否'
            bucket=line.bucketnum
            price=line.totalprice
            date=line.updatetime
            table.append(str(id))
            table.append(str(i))
            table.append(name)
            table.append(mode)
            table.append(bucket)
            table.append(price)
            table.append(str(date))
            table.append(address)
            TableData.append(table)
            i=i+1
        history={'ColumnName':ColumnName,'TableData':TableData}
        return history
    def dft_dbi_get_material_stock_detail(self,inputData):
        ID=inputData['stockID']
        result=dct_t_l3f11faam_material_stock_table.objects.filter(sid=ID)
        if result.exists():
            for line in result:
                if line.isself:
                    mode='0'
                else:
                    mode='1'
                table={'storageID':str(line.sid),'mode':mode,'localStorage':'50','maxStorage':'100'}
        else:
            table={}
        return table

    def dft_dbi_material_stock_income_new(self,inputData):
        ID=inputData['storageID']
        bucket=int(inputData['bucket'])
        price=int(inputData['price'])
        materialMode=inputData['materialMode']
        if materialMode=='0':
            mode=True #入库
        else:
            mode=False #代存
        vendor=inputData['vendor']
        buyer=inputData['buyer']
        mobile=inputData['mobile']
        result=dct_t_l3f11faam_material_stock_table.objects.get(sid=ID)
        if result:
            into=True
            stockName=result.stockname
            result.bucketnum=result.bucketnum+bucket
            result.totalprice=result.totalprice+price
            result.save(update_fields=['bucketnum','totalprice'])
            dct_t_l3f11faam_material_history.objects.create(stockid=ID,stockname=stockName,
                                                            into=into,bucketnum=bucket,
                                                            price=price,mode=mode,vendor=vendor,
                                                            charge=buyer,mobile=mobile,
                                                            trunk="---",target='---',logisitics='---')
            return True
        else:
            return False
    def dft_dbi_material_stock_remova_new(self,inputData):
        ID=inputData['storageID']
        bucket=int(inputData['bucket'])
        price=int(inputData['price'])
        materialMode=inputData['materialMode']
        if materialMode=='0':
            materialMode=True
        else:
            materialMode=False
        trunk=inputData['trunk']
        driver=inputData['driver']
        mobile=inputData['mobile']
        target=inputData['target']
        logistics=inputData['logistics']
        result=dct_t_l3f11faam_material_stock_table.objects.filter(sid=ID)
        if result.exists():
            for line in result:
                if bucket>line.bucketnum:
                    return False
                else:
                    totalNumber=int(line.bucketnum)-bucket
                    totalPrice=int(line.totalprice)+price
                    stockUpdate=dct_t_l3f11faam_material_stock_table.objects.get(sid=ID)
                    stockUpdate.bucketnum=totalNumber
                    stockUpdate.totalprice=totalPrice
                    stockUpdate.save(update_fields=['bucketnum','totalprice'])
                    dct_t_l3f11faam_material_history.objects.create(stockid=ID,stockname=line.stockname,
                                                                    into=False,bucketnum=bucket,price=price,
                                                                    mode=materialMode,vendor="---",charge=driver,
                                                                    mobile=mobile,trunk=trunk,target=target,logisitics=logistics)
        else:
            return False

    def dft_dbi_material_stock_history(self,inputData):
        timeEnd=datetime.date.today()
        ColumnName=[]
        TableData=[]
        ColumnName.append('序号')
        ColumnName.append('仓库名')
        ColumnName.append('入库/出库')
        ColumnName.append('桶数')
        ColumnName.append('费用')
        ColumnName.append('供应商')
        ColumnName.append('购买者/司机')
        ColumnName.append('手机号')
        ColumnName.append('车牌号')
        ColumnName.append('收货单位')
        ColumnName.append('物流')
        ColumnName.append('时间')
        ID=inputData['StockID']
        day=inputData['Period']
        keyWord=inputData['KeyWord']
        if day=='1':timeStart=timeEnd
        elif day=='7':timeStart=timeEnd-timedelta(days=6)
        elif day=='30':timeStart=timeEnd-timedelta(days=29)
        elif day=='all':timeStart='0001-01-01'
        timeStart = datetime.datetime.strptime((str(timeStart) + ' 00:00:00.000000'), '%Y-%m-%d %H:%M:%S.%f')
        timeEnd = datetime.datetime.strptime((str(timeEnd) + ' 23:59:59.999999'), '%Y-%m-%d %H:%M:%S.%f')
        if(ID=='all'):
            if keyWord=="":
                result=dct_t_l3f11faam_material_history.objects.filter(time__gte=timeStart,time__lte=timeEnd)
            else:
                result=dct_t_l3f11faam_material_history.objects.filter(time__gte=timeStart,time__lte=timeEnd,charge__icontains=keyWord)
        else:
            if keyWord=="":
                result=dct_t_l3f11faam_material_history.objects.filter(time__gte=timeStart,time__lte=timeEnd,stockid=ID)
            else:
                result=dct_t_l3f11faam_material_history.objects.filter(stockid=ID,time__gte=timeStart,time__lte=timeEnd,charge__icontains=keyWord)
        i=1
        for line in result:
            empty=[]
            name=line.stockname
            check=dct_t_l3f11faam_material_stock_table.objects.filter(stockname=name)
            if check.exists():
                empty.append(line.sid)
            else:
                empty.append("")
            if line.into:
                mode='入库'
            else:
                mode='出库'
            empty.append(i)
            empty.append(line.stockname)
            empty.append(mode)
            empty.append(line.bucketnum)
            empty.append(line.price)
            empty.append(line.vendor)
            empty.append(line.charge)
            empty.append(line.mobile)
            empty.append(line.trunk)
            empty.append(line.target)
            empty.append(line.logisitics)
            empty.append(str(line.time))
            TableData.append(empty)
            i=i+1
        history={'ColumnName':ColumnName,'TableData':TableData}
        return history
    def dft_dbi_get_material_stock_history_deatil(self,inputData):
        sid=inputData['removalID']
        table={}
        result=dct_t_l3f11faam_material_history.objects.filter(sid=sid)
        for line in result:
            if line.mode:
                materialMode='0'
            else:
                materialMode='1'
            if line.into:
                table={'type':'0','storageID':line.stockid,'materialMode':materialMode,'bucket':line.bucketnum,'price':line.price,'buyer':line.charge,'vendor':line.vendor,'mobile':line.mobile}
            else:
                table = {'type': '1', 'storageID': line.stockid, 'materialMode': materialMode, 'bucket': line.bucketnum,
                         'price': line.price, 'trunk':line.trunk,'driver':line.charge,'mobile':line.mobile,
                         'target':line.target,'logistics':line.logisitics}
        return table

    def dft_dbi_material_stock_income_mod(self,inputData):
        incomeID=inputData['incomeID']
        storageID=inputData['storageID']
        bucket=int(inputData['bucket'])
        price=int(inputData['price'])
        vendor=inputData['vendor']
        buyer=inputData['buyer']
        mobile=inputData['mobile']
        result=dct_t_l3f11faam_material_stock_table.objects.get(sid=storageID)
        result1=dct_t_l3f11faam_material_history.objects.get(sid=incomeID)
        if result and result1:
            totalBucket=result.bucketnum-result1.bucketnum+bucket
            totalPrice=result.totalprice-result1.price+price
            if totalBucket<0:
                return False
            else:
                result.bucketnum=totalBucket
                result.totalprice=totalPrice
                result.save(update_fields=['bucketnum','totalprice'])
                result1.bucketnum=bucket
                result1.price=price
                result1.charge=buyer
                result1.vendor=vendor
                result1.mobile=mobile
                result1.save(update_fields=['bucketnum','price','charge','vendor','mobile'])
                return True
        else:
            return False
    def dft_dbi_material_stock_removal_mod(self,inputData):
        removalID = inputData['removalID']
        storageID = inputData['storageID']
        bucket = int(inputData['bucket'])
        price = int(inputData['price'])
        trunk = inputData['trunk']
        driver = inputData['driver']
        mobile = inputData['mobile']
        target = inputData['target']
        logistics = inputData['logistics']
        result = dct_t_l3f11faam_material_stock_table.objects.get(sid=storageID)
        result1 = dct_t_l3f11faam_material_history.objects.get(sid=removalID)
        if result and result1:
            totalBucket = result.bucketnum + result1.bucketnum - bucket
            totalPrice = result.bucketnum - result1.bucketnum + price
            if totalBucket<0:
                return False
            else:
                result.bucketnum = totalBucket
                result.totalprice = totalPrice
                result.save(update_fields=['bucketnum', 'totalprice'])
                result1.bucketnum = bucket
                result1.price = price
                result1.charge = driver
                result1.mobile = mobile
                result1.trunk = trunk
                result1.target = target
                result1.logistics = logistics
                result1.save(update_fields=['bucketnum','price','charge','mobile','trunk','target','logistics'])
                return True
        else:
            return False
    def dft_dbi_material_stock_removal_del(self,inputData):
        ID=inputData['removalID']
        result=dct_t_l3f11faam_material_history.objects.filter(sid=ID)
        if result.exists():
            for line in result:
                stockID=line.stockid
                into=line.into
                bucket=int(line.bucketnum)
                price=int(line.price)
                if into==True:
                    dct_t_l3f11faam_material_history.objects.filter(sid=ID).delete()
                    stock=dct_t_l3f11faam_material_stock_table.objects.get(sid=stockID)
                    if stock.bucketnum-bucket<0:
                        return False
                    else:
                        stock.bucketnum=stock.bucketnum-bucket
                        stock.totalprice=stock.totalprice-price
                        stock.save(update_fields=['bucketnum','totalprice'])
                else:
                    dct_t_l3f11faam_material_history.objects.filter(sid=ID).delete()
                    stock = dct_t_l3f11faam_material_stock_table.objects.get(sid=stockID)
                    stock.bucketnum = stock.bucketnum + bucket
                    stock.totalprice = stock.totalprice - price
                    stock.save(update_fields=['bucketnum', 'totalprice'])
        else:
            return False

    def dft_dbi_product_stock_removal_mod(self,inputData):
        removalID=inputData['removalID']
        # size=inputData['size']
        number=int(inputData['number'])
        container=inputData['container']
        trunk=inputData['trunk']
        mobile=inputData['mobile']
        driver=inputData['driver']
        target=inputData['target']
        logistics=inputData['logistics']
        # if size=='特级':size='A'
        # elif size=='一级':size='1'
        # elif size=='二级':size='2'
        # elif size=='三级':size='3'
        # elif size=='混合':size='S'
        # else:size=""
        result=dct_t_l3f11faam_product_history.objects.filter(sid=removalID)
        for line in result:
            name=line.stockname
            prosize=line.puoductsize
            proweight=line.productweight
            pronum=line.productnum
            old_number=line.number
            result_1=dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name,productweight=proweight,puoductsize=prosize,productnum=pronum)
            if result.exists():
                new_number=result_1[0].number
                if new_number+old_number-number>=0:
                    result_1[0].number=(new_number+old_number-number)
                    result_1[0].save(update_fields=['number'])
                    line.number=number
                    line.containerID=container
                    line.platenumber=trunk
                    line.drivername=driver
                    line.driverphone=mobile
                    line.receivingunit=target
                    line.logisticsunit=logistics
                    line.save(update_fields=['number','containerID','platenumber','drivername','driverphone','receivingunit','logisticsunit'])
                else:
                    return False
            else:
                return False

    def dft_dbi_product_stock_removal_del(self,inputData):
        removalID=inputData['removalID']
        result = dct_t_l3f11faam_product_history.objects.filter(sid=removalID)
        if result.exists():
            for line in result:
                name = line.stockname
                prosize = line.puoductsize
                proweight = line.productweight
                pronum = line.productnum
                old_number = line.number
                result_1 = dct_t_l3f11faam_product_stock_sheet.objects.filter(stockname=name, productweight=proweight,
                                                                              puoductsize=prosize, productnum=pronum)
                if result.exists():
                    new_number = result_1[0].number
                    result_1[0].number = new_number + old_number
                    result_1[0].save(update_fields=['number'])
                    line.delete()
                else:
                    return False
        else:
            return False
    def dft_dbi_faam_table_query(self,inputData):
        ColumnName=[]
        TableData=[]
        uid=inputData['uid']
        ColumnName.append('序号')
        ColumnName.append('员工名')
        ColumnName.append('性别')
        ColumnName.append('微信昵称')
        ColumnName.append('联系方式')
        ColumnName.append('在职')
        ColumnName.append('地址')
        ColumnName.append('岗位')
        ColumnName.append('时薪')
        pjCode=self.__dft_get_user_auth_factory(uid)
        result=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjCode)
        i=1
        for line in result:
            history=[]
            if line.gender==1:sex='男'
            else:sex='女'
            if line.onjob==True:onjob='是'
            else:onjob='否'
            history.append(i)
            history.append(line.employee)
            history.append(sex)
            history.append(line.openid)
            history.append(line.phone)
            history.append(onjob)
            history.append(line.address)
            history.append(line.position)
            history.append(line.unitprice)
            TableData.append(history)
            i=i+1
        Table={'ColumnName':ColumnName,'TableData':TableData}
        return Table
    
    
    '''*****************************微信小程序开始*****************************************'''
    def dft_dbi_faam_qrcode_kq_process(self,inputData):
        scanCode=inputData['scanCode']
        latitude=int(inputData['latitude'])
        longitude=int(inputData['longitude'])
        nickname=inputData['nickname']
        pagephone=inputData['pagephone']
        timeStamp=int(time.time())
        localTime=time.localtime(timeStamp)
        workDay=time.strftime("%Y-%m-%d",localTime)
        currentTime=time.strftime("%H:%M:%S",localTime)
        result=dct_t_l3f11faam_factory_sheet.objects.filter(pjcode=scanCode)
        if result.exists():
            for line in result:
                restStart=str(line.reststart)
                restEnd=str(line.restend)
                stdWorkStart=str(line.workstart)
                stdWorkEnd=str(line.workend)
                targetLatitude=int(line.latitude)
                targetLongitude=int(line.longitude)
                delta_latitude=abs(latitude-targetLatitude)
                delta_longitude=abs(longitude-targetLongitude)
                if delta_latitude>50000 or delta_longitude>50000:
                    resp={'employee':nickname,'message':'考勤位置错误'}
                    return resp
        else:
            resp = {'employee': nickname, 'message': '二维码无效'}
            return resp
        membersheet=dct_t_l3f11faam_member_sheet.objects.filter(openid=nickname,pjcode=scanCode)
        if membersheet.exists():
            for line in membersheet:
                employee=line.employee
                standardnum=line.standardnum
                if employee!="":
                    unitPrice=line.unitprice
                    dailysheet=dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=scanCode,employee=employee,workday=workDay)
                    if dailysheet.exists():
                        for line_daily in dailysheet:
                            arriveTimeInt=str(line_daily.arrivetime)
                            leaverTimeInt=str(currentTime)
                            offWorkTime=round(line_daily.offwork,1)
                            arriveTimeStr=workDay+" "+arriveTimeInt
                            leaverTimeStr=workDay+" " +leaverTimeInt
                            restStartStr=workDay+" "+restStart
                            restEndStr=workDay+" "+restEnd
                            stdWorkStartStr=workDay+" "+stdWorkStart
                            stdWorkEndStr=workDay+" "+stdWorkEnd
                            arriveTimeInt = time.strptime(arriveTimeStr, "%Y-%m-%d %H:%M:%S.%f")
                            arriveTimeInt = time.mktime(arriveTimeInt)
                            leaverTimeInt = time.strptime(leaverTimeStr, "%Y-%m-%d %H:%M:%S.%f")
                            leaverTimeInt = time.mktime(leaverTimeInt)
                            restStartInt = time.strptime(restStartStr, "%Y-%m-%d %H:%M:%S.%f")
                            restStartInt = time.mktime(restStartInt)
                            restEndInt = time.strptime(restEndStr, "%Y-%m-%d %H:%M:%S.%f")
                            restEndInt = time.mktime(restEndInt)
                            stdWorkStartInt = time.strptime(stdWorkStartStr, "%Y-%m-%d %H:%M:%S.%f")
                            stdWorkStartInt = time.mktime(stdWorkStartInt)
                            stdWorkEndInt = time.strptime(stdWorkEndStr, "%Y-%m-%d %H:%M:%S.%f")
                            stdWorkEndInt = time.mktime(stdWorkEndInt)
                            if arriveTimeInt<restStartInt and leaverTimeInt>restEndInt:
                                timeInterval=restStartInt-arriveTimeInt+leaverTimeInt-restEndInt
                            elif arriveTimeInt>=restStartInt and arriveTimeInt<restEndInt:
                                timeInterval=leaverTimeInt-restEndInt
                            elif leaverTimeInt>restStartInt and leaverTimeInt<restEndInt:
                                timeInterval=restStartInt-arriveTimeInt
                            elif arriveTimeInt>restEndInt:
                                timeInterval=leaverTimeInt-arriveTimeInt
                            elif leaverTimeInt<restStartInt:
                                timeInterval=leaverTimeInt-arriveTimeInt
                            else:
                                timeInterval=0

                            hour=int((timeInterval%(3600*24))/3600)
                            min=int((timeInterval%3600)/60)
                            WorkTime=hour+round(min/60,1)-offWorkTime
                            if WorkTime<0:WorkTime=0
                            if arriveTimeInt<=stdWorkStartInt:
                                lateWorkFlag=0
                            else:
                                lateWorkFlag=1
                            if leaverTimeInt<=stdWorkEndInt:
                                earlyLeaveFlag=0
                            else:
                                earlyLeaveFlag=1
                            dayStandardNum=standardnum*WorkTime
                            dct_t_l3f11faam_daily_sheet.objects.filter(pjcode=scanCode,employee=employee,workday=workDay,daystandardnum=dayStandardNum).update(leavetime=currentTime,worktime=WorkTime,unitprice=unitPrice,laterflag=lateWorkFlag,earlyflag=earlyLeaveFlag)
                            resp = {'employee': employee, 'message': '考勤成功'}
                    else:
                        dct_t_l3f11faam_daily_sheet.objects.create(pjcode=scanCode,employee=employee,workday=workDay,arrivetime=currentTime)
                        resp={'employee':employee,'message':'考勤成功'}

                else:
                    resp = {'employee': nickname, 'message': '用户注册未审核'}
        else:
            if pagephone=="":
                resp = {'employee': nickname, 'message': '请输入手机号'}
                return resp
            else:
                member_by_phone_sheet=dct_t_l3f11faam_member_sheet.objects.filter(phone=pagephone)
                if member_by_phone_sheet.exists():
                    dct_t_l3f11faam_member_sheet.objects.filter(phone=pagephone).update(openid=nickname)
                    resp={'employee': nickname, 'message': '注册成功'}
                else:
                    resp = {'employee': nickname, 'message': '用户未注册'}
        return resp
    def dft_dbi_faam_qrcode_sc_process(self,inputData):
        scanCode=inputData['scanCode']
        nickName=inputData['nickname']
        tiamstamp=int(time.time())
        localTime=time.localtime(tiamstamp)
        currentTime=time.strftime("%Y-%m-%d %H:%M:%S",localTime)
        codeResult=dct_t_l3f11faam_production.objects.filter(qrcode=scanCode)
        if codeResult.exists():
            for line in codeResult:
                activeTime=line.activetime
                pjCode=line.pjcode
                qrcode_owner=line.owner
                appleGrade=line.typecode
                memberResult=dct_t_l3f11faam_member_sheet.objects.filter(openid=nickName,pjcode=pjCode)
                appleType=dct_t_l3f11faam_type_sheet.objects.filter(typecode=appleGrade)
                if appleType.exists():
                    appleNum=appleType[0].applenum
                else:
                    appleNum="未知类型"
                if memberResult.exists():
                    for line in memberResult:
                        scan_operator=line.employee
                        if activeTime==None:
                            dct_t_l3f11faam_production.objects.filter(qrcode=scanCode).update(activeman=scan_operator,activetime=currentTime)
                            resp={'flag':True,'employee':scan_operator,'message':'统计成功'}
                        else:
                            dct_t_l3f11faam_production.objects.filter(qrcode=scanCode).update(lastactivetime=currentTime)
                            resp = {'flag': False, 'employee': scan_operator, 'message': '姓名：'+qrcode_owner+'；粒数：'+str(appleNum)}
                else:
                    resp = {'flag': False, 'employee': nickName, 'message': '扫描用户未注册'}
        else:
            resp = {'flag': False, 'employee': nickName, 'message': '二维码无效'}
        return resp
    def dft_dbi_faam_qrcode_sh_process(self):
        return True
    '''*****************************微信小程序结束*****************************************'''
    def dft_dbi_huitp_xmlmsg_equlable_apply_report(self,inputData):
        week=inputData['week']
        pjCode=inputData['pjcode']
        applyNum=inputData['applynum']
        labelBaseInfo=inputData['labelBaseInfo']
        userTabTL=inputData['userTabTL']
        currentTime=inputData['currentTime']
        userTabTR=inputData['userTabTR']
        start = 0
        end = 0
        result=dct_t_l3f11faam_production.objects.filter(applyweek=week,pjcode=pjCode).order_by('-sid')
        if result.exists():
            line=result[0]
            lastCode=line.qrcode
            lastNum=int(lastCode[-5:])
            if lastNum+applyNum<99999:
                start=lastNum+1
                end=start+applyNum
                for i in range(start,end):
                    digNum=str(i).rjust(5,'0')
                    qrcode=labelBaseInfo+digNum
                    product_result=dct_t_l3f11faam_production.objects.filter(qrcode=qrcode)
                    if product_result.exists():
                        pass
                    else:
                        dct_t_l3f11faam_production.objects.create(pjcode=pjCode,qrcode=qrcode,owner=userTabTL,typecode=userTabTR,applyweek=week,applytime=currentTime)
                allocateResp = self.__HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_TRUE
                comConfirm = self.__HUITP_IEID_UNI_COM_CONFIRM_YES
            else:
                allocateResp = self.__HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_FALSE
                comConfirm = self.__HUITP_IEID_UNI_COM_CONFIRM_NO
        else:
            if applyNum<99999:
                start=1
                end = start + applyNum
                for i in range(start, end):
                    digNum = str(i).rjust(5, '0')
                    qrcode = labelBaseInfo + digNum
                    product_result = dct_t_l3f11faam_production.objects.filter(qrcode=qrcode)
                    if product_result.exists():
                        pass
                    else:
                        dct_t_l3f11faam_production.objects.create(pjcode=pjCode, qrcode=qrcode, owner=userTabTL,
                                                                  typecode=userTabTR, applyweek=week,
                                                                  applytime=currentTime)
                allocateResp = self.__HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_TRUE
                comConfirm = self.__HUITP_IEID_UNI_COM_CONFIRM_YES
            else:
                allocateResp = self.__HUITP_IEID_UNI_EQULABLE_ALLOCATION_FLAG_FALSE
                comConfirm = self.__HUITP_IEID_UNI_COM_CONFIRM_NO
        resp={'start':start,'end':end,'allocateResp':allocateResp,'comConfirm':comConfirm}
        return resp
    def dft_dbi_huitp_xmlmsg_equlable_userlist_report(self,inputData):
        userList=inputData['userlist']
        pjcode=inputData['pjcode']
        syncStart=inputData['syncstart']
        currrntNum=0
        counter=0
        memberResult=dct_t_l3f11faam_member_sheet.objects.filter(pjcode=pjcode,onjob=1)
        if memberResult.exists():
            total_num=len(memberResult)
            if  total_num<syncStart+100:
                for line in memberResult:
                    counter=counter+1
                    if syncStart>counter:
                        continue
                    workid=line.mid
                    employee=line.employee
                    userList=userList+employee+" "+workid+";"
                    currrntNum=currrntNum+1
            else:
                if currrntNum<100:
                    counter=counter+1
                    for line in memberResult:
                        if syncStart>counter:
                            continue
                        workid = line.mid
                        employee = line.employee
                        userList = userList + employee + " " + workid + ";"
                        currrntNum = currrntNum + 1
            comConfirm=self.__HUITP_IEID_UNI_COM_CONFIRM_YES
        else:
            total_num=0
            comConfirm=self.__HUITP_IEID_UNI_COM_CONFIRM_NO
        resp={'comConfirm':comConfirm,'userList':userList,'currrntNum':currrntNum,'totalNum':total_num}
        return resp
       
        
        
        
        
        
        
        
        
        
        
        
        
