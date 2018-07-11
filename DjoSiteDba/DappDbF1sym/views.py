from django.shortcuts import render
from django.db import transaction
from django.db.models import Q
from DappDbF1sym.models import dct_t_l3f1sym_user_right_project,dct_t_l3f1sym_user_login_session,dct_t_l3f1sym_account_primary,dct_t_l3f1sym_user_right_action,dct_t_l3f1sym_account_secondary
import random
import datetime
import time
import pycurl
import io
from werkzeug import responder
# Create your views here.
#在Python中，_、__和__XX__的区别，请参考https://www.cnblogs.com/lijunjiang2015/p/7802410.html
class dct_classDbiL3apF1sym:
    __MFUN_HCU_FHYS_CMCC_URL='http://api.sms.heclouds.com/tempsmsSend'
    __MFUN_HCU_FHYS_CMCC_SICODE='a2bb3546a41649a29e2fcb635e091dd5'
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_PW='10832'        
    __MFUN_HCU_FHYS_CMCC_TEMPCODE_ALARM='10833'
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
        c.setopt(pycurl.POSTFIELDS, 1)
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, head)
        c.perform()
        the_page = buf.getvalue()
        # print the_page
        buf.close()
        return the_page
        
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
                uid=result[0].uid
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
            auth = "fasle"
            status = "false"
            msg = "网页长时间没有操作，会话超时"
        else:
            result=dct_t_l3f1sym_account_primary.objects.filter(uid=uid)
            grade=result[0].grade_lever
            if grade==0:
                result = dct_t_l3f1sym_user_right_action.objects.filter(action_name=action, l1_auth=1)
            elif grade==1:
                result = dct_t_l3f1sym_user_right_action.objects.filter(action_name=action, l2_auth=1)
            elif grade==2:
                result = dct_t_l3f1sym_user_right_action.objects.filter(action_name=action, l3_auth=1)
            elif grade==3:
                result = dct_t_l3f1sym_user_right_action.objects.filter(action_name=action, l4_auth=1)
            else:
                result = dct_t_l3f1sym_user_right_action.objects.filter(action_name=action, l5_auth=1)
            if result.exists():
                auth="true"
            else:
                auth="false"
        authcheck={'status':status,'auth':auth,'uid':uid,'account':account,'msg':msg}
        return auth
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
            result.auth_code=authcode
            result.save()
            tel=dct_t_l3f1sym_account_secondary.objects.filter(id=result)
            telephone=tel[0].telephone
            url=self.__MFUN_HCU_FHYS_CMCC_URL+'?sicode='+self.__MFUN_HCU_FHYS_CMCC_SICODE+'&mobiles='+telephone+'&tempid='+self.__MFUN_HCU_FHYS_CMCC_TEMPCODE_PW+'&smscode='+authcode
            resp=self.__dft_https_request(url)
            return resp
        else:
            return ""
        
        
    def dft_dbi_reset_password_process(self,username,code,password):
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=username)
        if result.exists():
            authcode=result[0].auth_code
            uid=result[0].uid
            grade=result[0].grade_lever
            if grade==0:
                admin="true"
            else:
                admin="false"
            
            if(authcode==code):
                sessionid=self.__dft_getRandomSid(10)
                body={'key':sessionid,'admin':admin}
                msg='验证码正确，登录成功'
                self.__dft_updateSession(uid, sessionid)
                dct_t_l3f1sym_account_primary.objects.get(login_name=username).update(pass_word=password)
            else:
                body={'key':"",'admin':""}
                msg='验证码错误，登录失败'
        else:
            body={'key':"",'admin':""}
            msg='登陆失败，用户名错误'
        login_info={'body':body,'msg':msg}
        return login_info
    
    def dft_dbi_userinfo_req(self,sessionid):
        result=dct_t_l3f1sym_account_primary.objects.filter(session_id=sessionid)
        if result.exists():
            'sdasdas'
     
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