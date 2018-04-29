'''
Created on 2018/2/23

#
MODDULE: FMPT2 Cloud Connection Data Management

@author: hitpony
'''

#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket
import struct
import string
import datetime  
#import pycurl
import urllib
import json
import time
import urllib3
import socket
import hashlib

#Local include
from PkgFmptHandler import ModFmptCom

class ClassCloudProc(object):
    zStrFmptCloudConHuitpJsonApplyReport = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "IeCnt": {},\
        "FnFlag": 0\
        }

    zStrFmptCloudConHuitpJsonApplyConfirm = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "MsgLn": 0,\
        "IeCnt": {},\
        "FnFlag": 0\
        }

    zStrFmptCloudConHuitpJsonInservReport = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "MsgLn": 0,\
        "IeCnt": {},\
        "FnFlag": 0\
        }

    zStrFmptCloudConHuitpJsonInservConfirm = {\
        "ToUsr": 0,\
        "FrUsr": 0,\
        "CrTim": 0,\
        "MsgTp": 0,\
        "MsgId": 0,\
        "MsgLn": 0,\
        "IeCnt": {},\
        "FnFlag": 0\
        }
    
    #Init this class
    def __init__(self):
        self.zStrFmptCloudConHuitpJsonApplyReport = {\
            "ToUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "FrUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFmptCom.GL_FMPT_HUITP_MSGID_uni_equlabel_apply_report,\
            "MsgLn": 0,\
            "IeCnt": {\
                "facCode": ModFmptCom.GL_FMPT_CLOUDCON_PAR_FAC_CODE_SET_BY_USER,\
                "pdCode": ModFmptCom.GL_FMPT_CLOUDCON_PAR_PD_CODE_SET_BY_USER,\
                "pjCode": ModFmptCom.GL_FMPT_CLOUDCON_PAR_PJ_CODE_SET_BY_USER,\
                "userCode": ModFmptCom.GL_FMPT_CLOUDCON_PAR_USER_CODE_SET_BY_USER,\
                "uAccount": ModFmptCom.GL_FMPT_CLOUDCON_PAR_USER_ACCOUNT_SET_BY_USER,\
                "uPsd": ModFmptCom.GL_FMPT_CLOUDCON_PAR_PASSWD_SET_BY_USER,\
                "productType": ModFmptCom.GL_FMPT_CLOUDCON_PAR_PD_TYPE_SET_BY_USER,\
                "formalFlag": ModFmptCom.GL_FMPT_CLOUDCON_PAR_FORMAL_FLAG_SET_BY_USER,\
                "applyNbr": ModFmptCom.GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_BY_USER,\
                      },\
            "FnFlag": 0\
            }
    
        self.zStrFmptCloudConHuitpJsonApplyConfirm = {\
            "ToUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "FrUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFmptCom.GL_FMPT_HUITP_MSGID_uni_equlabel_apply_confirm,\
            "MsgLn": 0,\
            "IeCnt": {\
                "allocateRes": 0,\
                "allocateNbr": 0,\
                "labelStart": 'IHU_G5104AQYC_SH001',\
                "labelEnd": 'IHU_G5104AQYC_SH099',\
                      },\
            "FnFlag": 0\
            }
    
        self.zStrFmptCloudConHuitpJsonInservReport = {\
            "ToUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "FrUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFmptCom.GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_report,\
            "MsgLn": 0,\
            "IeCnt": {\
                "label": 'IHU_G801_BFSC_TUK01',\
                "useNum": 1,\
                "startStopFlag": ModFmptCom.GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_SET,\
                      },\
            "FnFlag": 0\
            }
    
        self.zStrFmptCloudConHuitpJsonInservConfirm = {\
            "ToUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_LOCAL_DEVID_DEFAULT,\
            "FrUsr": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_SVR_NAME_DEFAULT,\
            "CrTim": int(time.mktime(datetime.datetime.now().timetuple())),\
            "MsgTp": ModFmptCom.GL_FMPT_CLOUDCON_HUITP_MSG_FORMAT,\
            "MsgId": ModFmptCom.GL_FMPT_HUITP_MSGID_uni_equlabel_inservice_confirm,\
            "MsgLn": 0,\
            "IeCnt": {\
                "label": 'IHU_G801_BFSC_TUK01',\
                "useNum": 1,\
                "startStopFlag": ModFmptCom.GL_FMPT_HUITP_IEID_UNI_EQULABLE_INSERVICE_INFO_SET,\
                      },\
            "FnFlag": 0\
            }

    #Setup connection with back-hawl
    def FuncCurlib3ClientConnection(self, jsonInputData):
        encoded_data = json.dumps(jsonInputData).encode('utf-8')
        http = urllib3.PoolManager(maxsize=10, block=True)
        timeout = 2
        socket.setdefaulttimeout(timeout)
        r = http.request(
            'POST',
            'http://' + ModFmptCom.GL_FMPT_CLOUDCON_PAR_IP_ADDR_SET_BY_USER + ':' + ModFmptCom.GL_FMPT_CLOUDCON_HUITP_JSON_PORT + '/',
            body=encoded_data,
            headers={'Content-Type': 'application/json'})
        return json.loads(r.data)
    
    #Parameter set
    def FuncFixParSet(self, applyNum, cloudIpAddr, facCode, pdCode, pjCode, pdType, userCode, userAccount, passwd, formalFlag):
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_BY_USER = applyNum;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_IP_ADDR_SET_BY_USER = cloudIpAddr;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_FAC_CODE_SET_BY_USER = facCode;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_PD_CODE_SET_BY_USER = pdCode;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_PJ_CODE_SET_BY_USER = pjCode;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_PD_TYPE_SET_BY_USER = pdType;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_USER_CODE_SET_BY_USER = userCode;
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_USER_ACCOUNT_SET_BY_USER = userAccount;
        hash = hashlib.md5()
        hash.update(passwd.encode('utf-8'))
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_PASSWD_SET_BY_USER = str(hash.hexdigest());
        ModFmptCom.GL_FMPT_CLOUDCON_PAR_FORMAL_FLAG_SET_BY_USER = formalFlag;
        return 1;
    
    #Apply label
    def FunclabelApply(self, applyNum):
        self.zStrFmptCloudConHuitpJsonApplyReport['IeCnt']['applyNbr'] = applyNum;
        self.zStrFmptCloudConHuitpJsonApplyReport['MsgLn'] = len(json.dumps(self.zStrFmptCloudConHuitpJsonApplyReport['IeCnt']).encode('utf-8'));
        print(self.zStrFmptCloudConHuitpJsonApplyReport)

        #Send to Back-hawl and wait for feedback
        callRes = self.FuncCurlib3ClientConnection(self.zStrFmptCloudConHuitpJsonApplyReport);
        print(callRes)
        output = callRes['content'];

        #decode feedback
        res = {}
        if (('IeCnt' in output) == True):
            print(output['IeCnt'])
            if ((('allocateRes' in output['IeCnt']) == True) and (('allocateNbr' in output['IeCnt']) == True) and (('labelStart' in output['IeCnt']) == True) and (('labelEnd' in output['IeCnt']) == True)):
                self.zStrFmptCloudConHuitpJsonApplyConfirm['IeCnt']['allocateRes'] = output['IeCnt']['allocateRes'];
                self.zStrFmptCloudConHuitpJsonApplyConfirm['IeCnt']['allocateNbr'] = output['IeCnt']['allocateNbr'];
                self.zStrFmptCloudConHuitpJsonApplyConfirm['IeCnt']['labelStart'] = output['IeCnt']['labelStart'];
                self.zStrFmptCloudConHuitpJsonApplyConfirm['IeCnt']['labelEnd'] = output['IeCnt']['labelEnd'];
                res['res'] = 1;
                res['value'] = self.zStrFmptCloudConHuitpJsonApplyConfirm;
            else:
                res['res'] = -1;
        else:
            res['res'] = -2;
        
        #Return back
        return res;
    
    #Auto confirm used label    
    def FunclabelInservConfirm(self, useNum, labelStart, actionFlag):
        self.zStrFmptCloudConHuitpJsonInservReport['IeCnt']['useNum'] = useNum;
        self.zStrFmptCloudConHuitpJsonInservReport['IeCnt']['label'] = labelStart;
        self.zStrFmptCloudConHuitpJsonInservReport['IeCnt']['startStopFlag'] = actionFlag;
        self.zStrFmptCloudConHuitpJsonInservReport['MsgLn'] = len(json.dumps(self.zStrFmptCloudConHuitpJsonApplyReport['IeCnt']).encode('utf-8'));
        print(self.zStrFmptCloudConHuitpJsonApplyReport)

        #Send to Back-hawl and wait for feedback
        callRes = self.FuncCurlib3ClientConnection(self.zStrFmptCloudConHuitpJsonInservReport);
        print(callRes)
        output = callRes['content'];

        #decode feedback
        res = {}
        if (('IeCnt' in output) == True):
            print(output['IeCnt'])
            if ((('label' in output['IeCnt']) == True) and (('useNum' in output['IeCnt']) == True) and (('startStopFlag' in output['IeCnt']) == True)):
                self.zStrFmptCloudConHuitpJsonInservConfirm['IeCnt']['label'] = output['IeCnt']['label'];
                self.zStrFmptCloudConHuitpJsonInservConfirm['IeCnt']['useNum'] = output['IeCnt']['useNum'];
                self.zStrFmptCloudConHuitpJsonInservConfirm['IeCnt']['startStopFlag'] = output['IeCnt']['startStopFlag'];
                res['res'] = 1;
                res['value'] = self.zStrFmptCloudConHuitpJsonInservConfirm;
            else:
                res['res'] = -1;
        else:
            res['res'] = -2;                

        #Return back
        return res;        
        
class ClassHandler:

    def __init__(self):
        pass
  
    def funcCaculateMsgLen_HuitpJsonApplyReport(self):
        return 1;
  
    def funcCaculateMsgLen_HuitpJsonApplyConfirm(self):
        return 1;

    def funcCaculateMsgLen_HuitpJsonInservReport(self):
        return 1;

    def funcCaculateMsgLen_HuitpJsonInservConfirm(self):
        return 1;
    
    #Set parameters
    def func_par_set(self, applyNum, cloudIpAddr, facCode, pdCode, pjCode, pdType, userCode, userAccount, passwd, formalFlag):
        try:
            procObj =  ClassCloudProc();
            res = procObj.FuncFixParSet(applyNum, cloudIpAddr, facCode, pdCode, pjCode, pdType, userCode, userAccount, passwd, formalFlag);
            res = 1
        except Exception as err:  
            print("Exec Err: func_par_set!" + str(err))
            return ("Exec Err: func_par_set!" + str(err))
        finally:
            return res;
    
    #UI apply label by batch
    def func_label_apply(self, applyNum):
        try:
            ModFmptCom.GL_FMPT_CLOUDCON_PAR_APPLY_NUMBER_SET_BY_USER = applyNum;
            objCloud =  ClassCloudProc();
            res = {}
            res['res'] = 1
            callRes = objCloud.FunclabelApply(applyNum);
            if (callRes['res'] < 0):
                res['string'] = 'Exec err - func_label_apply failure in low layer.'
                res['res'] = callRes['res']
            else:
                res['res'] = 1
                res['value'] = callRes['value']
                res['string'] = 'Exec Res - func_label_apply'            
        except Exception as err:  
            print("Exec Err: func_label_apply!" + str(err))
            return ("Exec Err: func_label_apply!" + str(err))
        finally:
            return res;
    
    #Not yet used
    def func_label_use_confirm(self, useNum, labelStart):
        try:
            res = {}
        except Exception as err:  
            print("Exec Err: func_label_use_confirm!" + str(err))
            return ("Exec Err: func_label_use_confirm!" + str(err))
        finally:
            return res;




    
    
        
        
        