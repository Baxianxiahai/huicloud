from django.shortcuts import render
from django.db import transaction
from django.db.models import Q
from DappDbF1sym.models import dct_t_l3f1sym_user_right_menu,dct_t_l3f1sym_user_right_project,dct_t_l3f1sym_user_login_session,dct_t_l3f1sym_account_primary,dct_t_l3f1sym_user_right_action,dct_t_l3f1sym_account_secondary
import random
import datetime
import time
import pycurl
import io
# Create your views here.
#在Python中，_、__和__XX__的区别，请参考https://www.cnblogs.com/lijunjiang2015/p/7802410.html
class dct_classDbiL3apF1sym:
    __MFUN_HCU_FHYS_CMCC_URL='http://api.sms.heclouds.com/tempsmsSend'
    __MFUN_HCU_FHYS_CMCC_SICODE='a2bb3546a41649a29e2fcb635e091dd5'
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_PW='10832'        
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM='10833'
    __MENUACTIONINDEX={
        'webauth':{
            #FUM1SYM
            'menu_user_profile':0X0101,
            'UserManage':0X0102,
            'ParaManage':0X0103,
            'ExportTableManage':0X0104,
            'SoftwareLoadManage':0X0105,
        
            #FUM2CM
            'PGManage':0X0201,
            'ProjManage':0X0202,
            'MPManage':0X0203,
            'DevManage':0X0204,
            'KeyManage':0X0205,
            'KeyAuth':0X0206,
            'KeyHistory':0X0207,
    
            #FUM3DM
            'MPMonitor':0X0301,
            'MPStaticMonitorTable':0X0302,
            'MPMonitorCard':0X0303,
    
            #FUM4ICM
            'InstConf':0X0401,
            'InstRead':0X0402,
            'InstDesign':0X0403,
            'InstControl':0X0404,
            'InstSnapshot':0X0405,
            'InstVideo':0X0406,
    
            #FUM5FM
            'WarningCheck':0X0501,
            'WarningHandle':0X0502,
            'WarningLimit':0X0503,
    
            #FUM6PM
            'AuditTarget':0X0601,
            'AuditStability':0X0602,
            'AuditAvailability':0X0603,
            'AuditError':0X0604,
            'AuditQuality':0X0605,
    
            #FUM6ADS
            'ADConf':0X0701,
            'ADManage':0X0702,
            "WEBConf":0X0703,
    
            #FUM8PSM
    
            #FUM9GISM
            'GeoInfoQuery':0X0901,
            'GeoTrendAnalysis':0X0902,
            'GeoDisaterForecast':0X0903,
            'GeoEmergencyDirect':0X0904,
            'GeoDiffusionAnalysis':0X0905,
    
            #FUM11FAAM
            'StaffManage':0X0A01,
            'AttendanceManage':0X0A02,
            'FactoryManage':0X0A03,
            'SpecificationManage':0X0A04,
            'AssembleManage':0X0A05,
            'AssembleAudit':0X0A06,
            'AttendanceAudit':0X0A07,
            'KPIAudit':0X0A08,
            'ConsumablesManage':0X0A09,
            'ConsumablesHistory':0X0A0A,
            'ProductStorageManage':0X0A0B,
            'ProductDeliveryManage':0X0A0C,
            'MaterialStorageManage':0X0A0D,
            'MaterialDeliveryManage':0X0A0E,
            'SeafoodInfo':0X0A0F,
            'SeafoodAudit':0X0A10,
            },
        'actionauth':{
            #FUM1SYM
            'login':0X0101,
            'Get_user_auth_code':0X0102,
            'Reset_password':0X0103,
            'UserInfo':0X0120,
            'UserNew':0X0121,
            'UserMod':0X0122,
            'UserDel':0X0123,
            'UserTable':0X0124,
            #FUM2CM
            'PGNew':0X0201,
            'PGMod':0X0202,
            'PGDel':0X0203,
            'PGTable':0X0204,
            'PGProj':0X0205,
            'ProjectPGList':0X0206,
            'ProjectList':0X0220,
            'UserProj':0X0221,
            'ProjTable':0X0222,
            'ProjPoint':0X0223,
            'ProjNew':0X0224,
            'ProjMod':0X0225,
            'ProjDel':0X0226,
            'PointProj':0X0240,
            'PointTable':0X0241,
            'PointNew':0X0242,
            'PointMod':0X0243,
            'PointDel':0X0244,
            'PointDev':0X0245,
            'DevTable':0X0260,
            'DevNew':0X0261,
            'DevMod':0X0262,
            'DevDel':0X0263,
            'GetStationActiveInfo':0X0264,
            'StationActive':0X0265,
            'TableQuery':0X0266,
            'ProductModel':0X0267,
            'PointConf':0X0268,
            'PointLogin':0X0269,
            'UserKey':0X02A0,
            'ProjKeyList':0X02A1,
            'ProjKey':0X02A2,
            'ProjUserList':0X02A3,
            'KeyTable':0X02A4,
            'KeyNew':0X02A5,
            'KeyMod':0X02A6,
            'KeyDel':0X02A7,
            'DomainAuthlist':0X02A8,
            'KeyAuthlist':0X02A9,
            'KeyGrant':0X02AA,
            'KeyAuthNew':0X02AB,
            'KeyAuthDel':0X02AC,
            #FUM3DMA
            'DevSensor':0X0301,
            'SensorList':0X0302,
            'MonitorList':0X0303,
            'FakeMonitorList':0X0304,
            'Favourite_list':0X0305,
            'Favourite_count':0X0306,
            'GetStaticMonitorTable':0X0307,
            'PointPicture':0X0308,
            'KeyHistory':0X0320,
            'GetOpenImg':0X0321,
            #FUM4ICM
            'SensorUpdate':0X0401,
            'GetVideoCameraWeb':0X0402,
            'GetVideoList':0X0403,
            'GetVideo':0X0404,
            'GetCameraStatus':0X0405,
            'GetCameraUnit':0X0406,
            'CameraVAdj':0X0407,
            'CameraHAdj':0X0408,
            'CameraZAdj':0X0409,
            'CameraReset':0X040A,
            'GetCameraStatus':0X040B,
            'OpenLock':0X040C,
            #FUM5FM
            'MonitorAlarmList':0x0501,
            'DevAlarm':0x0502,
            'AlarmType':0x0503,
            'AlarmQuery':0x0504,
            'AlarmQueryRealtime':0x0505,
            'GetWarningHandleListTable':0x0506,
            'GetWarningImg':0x0507,
            'AlarmHandle':0x0508,
            'AlarmClose':0x0509,
            'GetHistoryRTSP':0x050A,
            #FUM6PM
            'GetAuditStabilityTable':0x0601,
            #FUM7ADS
            'SetUserMsg':0X0701,
            'GetUserMsg':0X0702,
            'ShowUserMsg':0X0703,
            'GetUserImg':0X0704,
            'ClearUserImg':0X0705,
            #FUM11FAAM
            'AttendanceAudit':0x0A01,
            'AttendanceMod':0x0A02,
            'KPIAudit':0x0A03,
            'StaffDel':0x0A04,
            'ConsumablesPurchaseNew':0x0A05,
            'ConsumablesTable':0x0A06,
            'ConsumablesHistory':0x0A07,
            'GetConsumablesPurchase':0x0A08,
            'ConsumablesPurchaseMod':0x0A09,
            'ConsumablesPurchaseDel':0x0A0A,
            'ProductStockNew':0x0A0B,
            'GetProductWeightAndSize':0x0A0C,
            'GetProductStockList':0x0A0D,
            'GetProductEmptyStock':0x0A0E,
            'ProductStockTable':0x0A0F,
            'ProductStockDel':0x0A10,
            'GetProductStockDetail':0x0A11,
            'ProductStockTransfer':0x0A12,
            'ProductStockHistory':0x0A13,
            'MaterialStockNew':0x0A14,
            'GetMaterialStockList':0x0A15,
            'GetMaterialEmptyStock':0x0A16,
            'MaterialStockDel':0x0A17,
            'MaterialStockTable':0x0A18,
            'GetMaterialStockDetail':0x0A19,
            'MaterialStockIncomeNew':0x0A1A,
            'MaterialStockRemovalNew':0x0A1B,
            'MaterialStockHistory':0x0A1C,
            'GetMaterialStockHistoryDetail':0x0A1D,
            'MaterialStockIncomeMod':0x0A1E,
            'MaterialStockRemovalMod':0x0A1F,
            'MaterialStockRemovalDel':0x0A20,
            'GetProductStockHistoryDetail':0x0A21,
            'ProductStockRemovalMod':0x0A22,
            'ProductStockRemovalDel':0x0A23,
            'ProductStockRemovalNew':0x0A24,
            'SeafoodInfo':0x0A30,
            'SeafoodAudit':0x0A31,
            },
        }
    __MFUN_CURRENT_WORKING_PROGRAM_NAME_UNIQUE=0
    def __init__(self):
        pass
        
    def __dft_https_request(self,url):
        c=pycurl.Curl()
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
        c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
        c.setopt(pycurl.MAXREDIRS, 5)
        head = ['Accept:*/*',
            'Content-Type:application/xml',
            'render:json',
            'clientType:json',
            'Accept-Charset:GBK,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding:gzip,deflate,sdch',
            'Accept-Language:zh-CN,zh;q=0.8',
            'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11']
        buf = io.BytesIO()
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.POSTFIELDS, '1')
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, head)
        c.perform()
        the_page = buf.getvalue()
        # print the_page
        buf.close()
        if the_page:
            return 'true'
        else:
            return 'false'
        
    def __dft_getRandomSid(self,strlen):
        str_array=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
        sid=''.join(random.sample(str_array,strlen))
        return sid
    def __dft_getRandomUid(self,strlen):
        str_array=['0','1','2','3','4','5','6','7','8','9']
        uid=''.join(random.sample(str_array,strlen))
        return uid
    def __dft_updateSession(self,uid,sessionid):
        now_time=int(time.time())
        result=dct_t_l3f1sym_user_login_session.objects.filter(uid_id=uid)
        if result.exists():
            result=dct_t_l3f1sym_user_login_session.objects.filter(uid_id=uid).update(session_id=sessionid,timestamp=now_time)
        else:
            primary=dct_t_l3f1sym_account_primary.objects.get(uid=uid)
            result=dct_t_l3f1sym_user_login_session(uid=primary,session_id=sessionid,timestamp=now_time)
            result.save()
        return result
    def dft_dbi_session_check(self,session):
        now_time=int(time.time())
        result=dct_t_l3f1sym_user_login_session.objects.filter(session_id=session)
        if result.exists():
            lastupdate=result[0].timestamp
            if(now_time<lastupdate+900):
                uid=result[0].uid_id
                self.__dft_updateSession(uid, session)
            else:
                uid=""
        else:
            uid=""
        return uid
    def dft_dbi_user_authcheck(self,action,sessionid):
        auth="true"
        status="true"
        msg=""
        account=""
        uid=self.dft_dbi_session_check(sessionid)
        if uid=="":
            auth = "false"
            status = "false"
            msg = "网页长时间没有操作，会话超时"
        else:
            result=dct_t_l3f1sym_account_primary.objects.filter(uid=uid)
            grade=result[0].grade_lever
            account=result[0].login_name
            if(action not in self.__MENUACTIONINDEX['actionauth'].keys()):
                auth='false'
                msg=action+'不在默认目录中，请联系管理员添加'
            else:
                if grade==0:
                    result = dct_t_l3f1sym_user_right_action.objects.filter(action_code=self.__MENUACTIONINDEX['actionauth'][action], l1_auth=1)
                elif grade==1:
                    result = dct_t_l3f1sym_user_right_action.objects.filter(action_code=self.__MENUACTIONINDEX['actionauth'][action], l2_auth=1)
                elif grade==2:
                    result = dct_t_l3f1sym_user_right_action.objects.filter(action_code=self.__MENUACTIONINDEX['actionauth'][action], l3_auth=1)
                elif grade==3:
                    result = dct_t_l3f1sym_user_right_action.objects.filter(action_code=self.__MENUACTIONINDEX['actionauth'][action], l4_auth=1)
                elif grade==4:
                    result = dct_t_l3f1sym_user_right_action.objects.filter(action_code=self.__MENUACTIONINDEX['actionauth'][action], l5_auth=1)
                else:
                    auth='false'
                    msg='您的账户等级错误，请联系管理人员'
                if result.exists():
                    auth="true"
                else:
                    auth="false" 
        authcheck={'status':status,'auth':auth,'uid':uid,'account':account,'msg':msg}
        return authcheck
    def dft_dbi_login_req(self,name,password):
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=name)
        if result.exists():
            pwd=result[0].pass_word
            uid=result[0].uid
            grade=result[0].grade_lever
            if grade==0:
                admin='true'
            else:
                admin='false'
            if pwd==password:
                strlen=10
                sessionid=self.__dft_getRandomSid(strlen)
                body={'key':sessionid,'admin':admin}
                msg='登录成功'
                self.__dft_updateSession(uid,sessionid)
#                 raise ValueError("-1")
            else:
                body={'key':"",'admin':'false'}
                msg='登录失败，密码错误'
        else:
            body = {'key': "", 'admin': 'false'}
            msg = '登录失败，用户名错误'
        login_info={'body':body,'msg':msg}
#         print(login_info)
        return login_info
    #在Django中，多表间的查询可以通过外键的方式进行查询，详见work1
    def dft_dbi_userauthcode_process(self,username):
        authcode=self.__dft_getRandomUid(6)
        result=dct_t_l3f1sym_account_primary.objects.get(login_name=username)
        if result:
            dct_t_l3f1sym_account_primary.objects.filter(login_name=username).update(auth_code=authcode)
            tel=dct_t_l3f1sym_account_secondary.objects.filter(uid=result.uid)
            telephone=tel[0].telephone
            url=self.__MFUN_HCU_FHYS_CMCC_URL+'?sicode='+self.__MFUN_HCU_FHYS_CMCC_SICODE+'&mobiles='+str(telephone)+'&tempid='+self.__MFUN_HCU_FHYS_CMCC_TEMPCODE_PW+'&smscode='+authcode
            resp=self.__dft_https_request(url)
            return resp
        else:
            return ""
        
    def dft_dbi_reset_password_process(self,username,code,password):
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=username)
        if result.exists():
            authcode=result[0].auth_code
            print(authcode)
            uid=result[0].uid
            grade=result[0].grade_lever
            if grade==0:
                admin="true"
            else:
                admin="false"
            if(str(authcode)==code):
                print(code)
                sessionid=self.__dft_getRandomSid(10)
                print(sessionid)
                body={'key':sessionid,'admin':admin}
                msg='验证码正确，登录成功'
                self.__dft_updateSession(uid, sessionid)
                dct_t_l3f1sym_account_primary.objects.filter(login_name=username).update(pass_word=password)
            else:
                body={'key':"",'admin':""}
                msg='验证码错误，登录失败'
        else:
            body={'key':"",'admin':""}
            msg='登陆失败，用户名错误'
        login_info={'body':body,'msg':msg}
        return login_info
    
    def dft_dbi_userinfo_req(self,sessionid):
        userauth={}
        session=dct_t_l3f1sym_user_login_session.objects.filter(session_id=sessionid)
        now=int(time.time())
        if(session.exists()):
            uid=session[0].uid
            lastupdate = session[0].timestamp
            city=dct_t_l3f1sym_account_secondary.objects.filter(uid_id=uid).first().city
            if(lastupdate<now+900):
                grade_idx=session[0].uid.grade_lever
                menugroup=session[0].uid.menu_group
                name=session[0].uid.login_name
                
                if_online=True
                map_latitude=0
                map_longitude=0
                userpoint={'Latitude':map_latitude,'Longitude':map_longitude}
                grade_info=dct_t_l3f1sym_user_right_menu.objects.filter(menu_group=menugroup)
                for line in grade_info:
                    if line.menu_name in self.__MENUACTIONINDEX['webauth'].keys() :
                        self.__MENUACTIONINDEX['webauth'][line.menu_name]=1
                for key in self.__MENUACTIONINDEX['webauth']:
                    if self.__MENUACTIONINDEX['webauth'][key]==1:
                        self.__MENUACTIONINDEX['webauth'][key]='true'
                    else:
                        self.__MENUACTIONINDEX['webauth'][key]='false'
                print(self.__MENUACTIONINDEX['webauth'])
                userauth['webauth']=self.__MENUACTIONINDEX['webauth']
                userauth['query']='true'
                userauth['mod']='true'
                userinfo={'id':sessionid,'name':name,'level':grade_idx,'city':city,'online':if_online,'point':userpoint,'userauth':userauth}
        else:
            userinfo={}
        return userinfo
    def dft_dbi_usernum_inquery(self):
        result=dct_t_l3f1sym_account_primary.objects.all()
        return len(result)
    
    def dft_dbi_usertable_req(self,uid,keyword):
        usertable=[]
        if keyword=="":
            result=dct_t_l3f1sym_account_secondary.objects.filter(uid__grade_lever__gte=dct_t_l3f1sym_account_secondary.objects.get(uid__uid=uid).uid.grade_lever)
            for line in result:
                temp = {'id': line.uid,
                        'name': line.uid.login_name,
                        'nickname': line.nick_name,
                        'mobile': line.telephone,
                        'mail': line.uid.email,
                        'type': line.uid.grade_lever,
                        'date': line.uid.red_date,
                        'memo': " "}
                usertable.append(temp)
        else:
            result=dct_t_l3f1sym_account_secondary.objects.filter(Q(uid__login_name__icontains=keyword)|Q(nick_name__icontains=keyword)|Q(telephone__icontains=keyword))
            for line in result:
                temp={'id':line.uid,
                      'name':line.uid.login_name,
                      'nickname':line.nick_name,
                      'mobile':line.telephone,
                      'mail':line.uid.email,
                      'type':line.uid.grade_lever,
                      'date':line.uid.red_date,
                      'memo':" "}
                usertable.append(temp)
        return usertable
        
    def dft_dbi_userinfo_new(self,userinfo):
        uid='UID'+self.__dft_getRandomUid(7)
        if userinfo['name']!="":user=userinfo['name'].replace(' ','')
        else:user=""
        if userinfo['nickname']!="":nick=userinfo['nickname'].replace(' ','')
        else:nick=""
        if userinfo['password']!="":password=userinfo['password'].replace(' ','')
        else:password=""
        if userinfo['type']!="":grade=userinfo['type'].replace(' ','')
        else:grade=""
        if userinfo['mobile']!="":mobile=userinfo['mobile'].replace(' ','')
        else:mobile=""
        if userinfo['mail']!="":mail=userinfo['mail'].replace(' ','')
        else:mail=""
        if userinfo['memo']!="":backup=userinfo['memo'].replace(' ','')
        else:backup=""
        if userinfo['auth']!="":auth=userinfo['auth'].replace(' ','')
        else:auth=""
        city="上海"
        print(user,nick,password,type,mobile,mail,backup,auth)
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=user)
        if result.exists():
            result=dct_t_l3f1sym_account_primary.objects.get(login_name=user)
            result.pass_word=password
            result.email=mail
            result.menu_group=0
            result.auth_code=0
            result.grade_lever=grade
            result.save()
            dct_t_l3f1sym_account_secondary.objects.update(uid=dct_t_l3f1sym_account_primary.objects.get(login_name=user),gender=1,telephone=mobile,nick_name=nick,city=city)
        else:
            result=dct_t_l3f1sym_account_primary(uid=uid,login_name=user,pass_word=password,email=mail,menu_group=0,auth_code=0,grade_lever=grade)
            result.save()
            dct_t_l3f1sym_account_secondary.objects.create(uid=dct_t_l3f1sym_account_primary.objects.get(login_name=user),gender=1,telephone=mobile,nick_name=nick,city=city)
        return uid
    
    def dft_dbi_userinfo_update(self,userinfo):
        if userinfo['userid']!="":uid=userinfo['userid'].replace(' ','')
        else:uid=""
        if userinfo['name']!="":user=userinfo['name'].replace(' ','')
        else:user=""
        if userinfo['nickname']!="":nick=userinfo['nickname'].replace(' ','')
        else:nick=""
        if userinfo['password']!="":password=userinfo['password'].replace(' ','')
        else:password=""
        if userinfo['type']!="":grade=userinfo['type'].replace(' ','')
        else:grade=""
        if userinfo['mobile']!="":mobile=userinfo['mobile'].replace(' ','')
        else:mobile=""
        if userinfo['mail']!="":email=userinfo['mail'].replace(' ','')
        else:email=""
        if userinfo['memo']!="":memo=userinfo['memo'].replace(' ','')
        else:memo=""
        if userinfo['auth']!="":auth=userinfo['auth'].replace(' ','')
        else:auth=""
        user_update=dct_t_l3f1sym_account_secondary.objects.get(uid__uid=uid)
        if (password != ""):
            user_update = dct_t_l3f1sym_account_secondary.objects.get(uid__uid=uid)
            user_update.uid.login_name = user
            user_update.nick_name = nick
            user_update.uid.pass_word = password
            user_update.uid.gradelever = grade
            user_update.telephone = mobile
            user_update.uid.email = email
            user_update.save()
    
        else:
            user_update = dct_t_l3f1sym_account_secondary.objects.get(uid__uid=uid)
            user_update.uid.login_name = user
            user_update.nick_name = nick
            user_update.uid.grade_lever = grade
            user_update.telephone = mobile
            user_update.uid.email = email
            user_update.save()
    
        dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid).delete()
        if auth!="":
            for i in range(len(auth)):
                if auth[i]['id']=="":authcode='PG_0000'
                else:authcode=auth[i]['id']
                auth_array=authcode.split('_')
                auth_type=auth_array[0]
                auth_code=auth_array[1]
                auth_type=auth_type.upper()
                if(auth_type=="PG"):
                    auth_type=1
                else:
                    auth_type=2
                dct_t_l3f1sym_user_right_project.objects.create(uid=dct_t_l3f1sym_account_primary.objects.get(uid=uid),auth_type=auth_type,auth_code=auth_code)
        return
    def dft_dbi_userinfo_delete(self,uid):
        dct_t_l3f1sym_account_primary.objects.filter(uid=uid).delete()
        return
    
if __name__=="__main__":
    a = dct_classDbiL3apF1sym()
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# print(int(time.time()))