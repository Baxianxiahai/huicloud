# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: Administrator
'''
from PkgHstDba import ModDbaF1sym
class ClassDbaF1symMainEntry():
    def __init__(self):
        pass
    
    def dft_F1sym_Send_Message(self,inputData):
        if inputData['action']=='login':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_login_req(inputData['body'])
        if inputData['action']=='Get_user_auth_code':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userauthcode_process(inputData['body'])
        if inputData['action']=='Reset_password':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_reset_password_process(inputData['body'])
        if inputData['action']=='UserInfo':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_userinfo_req(inputData['body'])
        if inputData['action']=='sessioncheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_session_check(inputData['body'])
        if inputData['action']=='authcheck':
            F1sym=ModDbaF1sym.ClassDbaF1sym()
            result=F1sym.dft_dbi_user_authcheck(inputData['body'])
        
        else:
            pass
        return result
        