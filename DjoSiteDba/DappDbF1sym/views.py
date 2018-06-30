from django.shortcuts import render
from django.db import transaction
from DappDbF1sym.models import dct_t_l3f1sym_user_login_session,dct_t_l3f1sym_account_primary,dct_t_l3f1sym_user_right_action
import random
import datetime
import time
# Create your views here.
class dct_classDbiL3apF1sym:
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
        print(uid)
        print(sessionid)
        result=dct_t_l3f1sym_user_login_session.objects.filter(uid=uid)
        if result.exists():
            result=dct_t_l3f1sym_user_login_session.objects.filter(uid=uid).update(session_id=sessionid,timestamp=now_time)
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
        return authcheck
    def dft_dbi_login_req(self,name,password):
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=name)
        if result.exists():
            pwd=result[0].pass_word
            uid=result[0].uid
            grade=result[0].grade_lever
            if grade==1:
                admin='true'
            else:
                admin='false'
            if pwd==password:
                strlen=10
                sessionid=self.__dft_getRandomSid(strlen)
                body={'key':sessionid,'admin':admin}
                msg='登录成功'
                self.__dft_updateSession(uid,sessionid)
            else:
                body={'key':"",'admin':''}
                msg='登录失败，密码错误'
        else:
            body = {'key': "", 'admin': ''}
            msg = '登录失败，用户名错误'
        login_info={'body':body,'msg':msg}
        return login_info
if __name__=="__main__":
    a = dct_classDbiL3apF1sym()
    a.test2()
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(int(time.time()))