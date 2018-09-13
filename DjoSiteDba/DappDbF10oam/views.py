from django.shortcuts import render
import math
import time
import os
import stat
import datetime
import json

# Create your views here.
from DappDbF10oam.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
class dct_DappF10Class():
    __MFUN_CLOUD_QRCODE_ABS_DIR="/var/www/html/avorion/hcu_qrcode/"
    __MFUN_CLOUD_QRCODE_WWW_DIR="/avorion/hcu_qrcode/"
    __MFUN_CLOUD_TEMP_DIR='./temp/'

    __MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN=5
    __MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX=100
    __MFUN_CLOUD_ADMINTOOLS_FHYS_QRCODE_BASE="http://www.foome.com.cn/mfunhcu/l4hcuinstall/index.html?code="
    __MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE="http://ngrok2.hkrob.com/mfunhcu/l4aqycactive/index.html?code="

    __HUITP_IEID_UNI_EQU_ENTRY_NONE=0
    __HUITP_IEID_UNI_EQU_ENTRY_HCU_SW=1
    __HUITP_IEID_UNI_EQU_ENTRY_HCU_DB=2
    __HUITP_IEID_UNI_EQU_ENTRY_IHU=3
    __HUITP_IEID_SUI_EQU_ENTRY_INVALID=0XFF
    __HUITP_IEID_UNI_FW_UPGRADE_NONE=0
    __HUITP_IEID_UNI_FW_UPGRADE_NO=1
    __HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE=2
    __HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL=3
    __HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH=4
    __HUITP_IEID_UNI_FW_UPGRADE_YES_INVALID=0XFF
    __MFUN_HCU_SW_LOAD_FLAG_INVALID=0
    __MFUN_HCU_SW_LOAD_FLAG_VALID=1

    __MFUN_CLOUD_SWLOAD_DIR="/var/www/html/avorion/hcu_sw_active/"

    def dft_dbi_scan_newcode_check(self,inputData):
        devCode=inputData['devCode']
        result=dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode)
        if result.exists():
            result=dct_t_l3f10oam_qrcodeinfo.objects.get(dev_code=devCode)
            result.validflag='Y'
            result.save()
            resp=True
        else:
            resp= False
        return resp
    def dft_dbi_aqyc_qrcode_scan_siteinfo_update_gps(self,inputData):
        devCode = inputData['devCode']
        latitude=inputData['latitude']
        longitude=inputData['longitude']
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            site_code=result[0].site_code
            site_code.latitude=latitude
            site_code.longitude=longitude
            site_code.save()
        return True
    ###########################################################################
    '''                                  ADMINTOOLS                         '''
    ###########################################################################
    def dft_dbi_tools_qrcode_filelist(self,inputData):
        user=inputData['user']
        filelist=[]
        if user=='admin':
            result=dct_t_l3f10oam_regqrcode.objects.all()
            if result.exists():
                for line in result:
                    filename=line.zipfile
                    fileurl=self.__MFUN_CLOUD_QRCODE_WWW_DIR+filename
                    fileinfo={'name':filename,'URL':fileurl}
                    filelist.append(fileinfo)
        else:
            result=dct_t_l3f10oam_regqrcode.objects.filter(applyuser=user)
            if result.exists():
                for line in result:
                    filename = line.zipfile
                    fileurl = self.__MFUN_CLOUD_QRCODE_WWW_DIR + filename
                    fileinfo = {'name': filename, 'URL': fileurl}
                    filelist.append(fileinfo)
        return filelist

    def dft_dbi_tools_qrcode_newapply(self,inputData):
        body=inputData['body']
        user=inputData['user']
        facCode=body['FACCode']
        pdCode=body['PDCode']
        pjCode=body['PJCode']
        userCode=body['UserCode']
        productType=body['ProductType']
        formalFlag=body['FormalFlag']
        applyNum=int(body['ApplyNbr'])
        if applyNum>self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX:
            msg="申请的数量不能超过"+str(self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX)
            resp={'auth':'false','msg':msg}
            return resp
        if(len(pdCode)>=5):
            pdCode=pdCode[0:5]
        if len(pdCode)>4:
            pdCode_base=pdCode
        else:
            pdCode_middle="G"+pdCode
            pdCode_base=pdCode_middle.ljust(5).replace(" ","_")
        if (pjCode=='AQYC') | (pjCode=='ANXX'):
            qrcode_base=self.__MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE
        elif pjCode=='FHYS' :
            qrcode_base=self.__MFUN_CLOUD_ADMINTOOLS_FHYS_QRCODE_BASE
        else:
            resp = {'auth': 'false', 'msg': "申请的项目代码不存在"}
            return resp
        if len(userCode)>=self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN:
            msg = "申请的用户代码必须小于最大允许长度" + str(self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN)
            resp = {'auth': 'false', 'msg': msg}
            return resp
        digLen=self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN-len(userCode)
        result=dct_t_l3f10oam_regqrcode.objects.filter(pdtype=productType,pdcode=pdCode,pjcode=pjCode,usercode=userCode)
        digStopArray=[]
        if result.exists():
            for line in result:
                digStopArray.append(line.digstop)
            digstop=max(digStopArray)
            digStart=digstop+1
            maxAllow=math.pow(10,digLen)-1
            if(digStart+applyNum)<=maxAllow:
                digStop=digStart+applyNum-1
                approveNum=applyNum
            elif ((digStart<maxAllow) and(maxAllow<digStart+applyNum)):
                digStop=maxAllow
                approveNum=maxAllow-digStart+1
            else:
                digStop=0
                approveNum=0
        else:
            digStart=1
            digStop=applyNum
            approveNum=applyNum
        if approveNum==0:
            resp = {'auth': 'false', 'msg': "该请求条件已无代码可分配"}
            return resp
        else:
            resp = {'auth': 'true',
                    'digstart':digStart,
                    'digstop':digStop,
                    'diglen':digLen,
                    'qrcode_base':qrcode_base,
                    'approvenum':approveNum,
                    'pdcodebase':pdCode_base,
                    }
            return resp
    def dft_dbi_qrcode_data_insert(self,inputData):
        digStart=inputData['digstart']
        digStop=inputData['digstop']
        devCodeArray=inputData['DevCodeArray']
        user=inputData['user']
        zipfile=inputData['zipfile']
        approvenum=inputData['approvenum']
        facCode = inputData['FACCode']
        pdCode = inputData['PDCode']
        pjCode = inputData['PJCode']
        userCode = inputData['UserCode']
        productType = inputData['ProductType']
        formalFlag = inputData['FormalFlag']
        applyNum = int(inputData['ApplyNbr'])
        qrcode_insert_list=list()
        pj_insert_list=list()
        base_port_max=dct_t_l3f2cm_device_inventory.objects.all().order_by("-base_port")[0].base_port
        for devCode in devCodeArray:
            if dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).exists():
                pass
            else:
                base_port_max=base_port_max+1
                qrcode_insert_list.append(dct_t_l3f2cm_device_inventory(dev_code=devCode, create_date=datetime.date.today(),hw_type=int(pdCode),base_port=base_port_max))
        dct_t_l3f2cm_device_inventory.objects.bulk_create(qrcode_insert_list)
        time.sleep(1)
        if pjCode=='AQYC':
            for devCode in devCodeArray:
                result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
                basePort=result[0].base_port
                weburl="http://"+str(devCode)+"ngrok2.hkrob.com:8080/yii2basic/web/index.php"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "2" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "3" + "ISAPI/Streaming/Channels/101"
                pj_insert_list.append(dct_t_l3f2cm_device_aqyc(dev_code_id=devCode,web_url=weburl,pic1_url=pic1url,ctrl1_url=ctrl1url,video1_url=video1url))
            dct_t_l3f2cm_device_aqyc.objects.bulk_create(pj_insert_list)

        time.sleep(1)
        if pjCode == 'FSTT':
            for devCode in devCodeArray:
                result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
                basePort = result[0].base_port
                weburl = "http://" + str(devCode) + "ngrok2.hkrob.com:8080/yii2basic/web/index.php"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "2" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "3" + "ISAPI/Streaming/Channels/101"
                pic2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "6" + "/ISAPI/Streaming/channels/1/picture"
                ctrl2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "6" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video2url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "7" + "ISAPI/Streaming/Channels/101"
                pic3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "8" + "/ISAPI/Streaming/channels/1/picture"
                ctrl3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "8" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video3url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(basePort) + "9" + "ISAPI/Streaming/Channels/101"
                pj_insert_list.append(
                    dct_t_l3f2cm_device_fstt(dev_code_id=devCode,web_url=weburl,pic1_url=pic1url,ctrl1_url=ctrl1url,video1_url=video1url,pic2_url=pic2url,ctrl2_url=ctrl2url,video2_url=video2url,
                                             pic3_url=pic3url,ctrl3_url=ctrl3url,video3_url=video3url))
            dct_t_l3f2cm_device_fstt.objects.bulk_create(pj_insert_list)
        else:
            pass
        dct_t_l3f10oam_regqrcode.objects.create(applyuser=user,faccode=facCode,pdtype=productType,pdcode=pdCode,pjcode=pjCode,usercode=userCode,isformal=formalFlag,applynum=applyNum,approvenum=approvenum,digstart=digStart,digstop=digStop,zipfile=zipfile)
        return 'true'

    def dft_dbi_tools_swload_table_get(self):
        ColumnName=[]
        TableData=[]
        ColumnName.append('SID')
        ColumnName.append('EQU_ENTRY')
        ColumnName.append('VALID_FLAG')
        ColumnName.append('UPGRADE_FLAG')
        ColumnName.append('HW_TYPE')
        ColumnName.append('HW_ID')
        ColumnName.append('SW_REL')
        ColumnName.append('SW_VER')
        ColumnName.append('DB_VER')
        ColumnName.append('FILE_LINK')
        ColumnName.append('FILE_SIZE')
        ColumnName.append('FILE_CHECKSUM')
        result=dct_t_l3f10oam_swloadinfo.objects.all()
        if result.exists():
            for line in result:
                sid=line.sid
                equentry=line.equentry
                validflag=line.validflag
                upgradeflag=line.upgradeflag
                hwtype=line.hwtype
                hwid=line.hwid
                swrel=line.swrel
                swver=line.swver
                dbver=line.dbver
                filelink=line.filelink
                filesize=line.filesize
                checknum=line.checksum
                if equentry==self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW:
                    equentry="HCU_SW"
                elif equentry==self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB:
                    equentry='HCU_DB'
                elif equentry==self.__HUITP_IEID_UNI_EQU_ENTRY_IHU:
                    equentry='IHU_SW'
                else:
                    equentry='INVALID'

                if upgradeflag==self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE:
                    upgradeflag='STABLE'
                elif upgradeflag==self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL:
                    upgradeflag="TRAIL"
                elif upgradeflag==self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH:
                    upgradeflag='PATCH'
                else:
                    upgradeflag="INVALID"
                if validflag==0:
                    Flag="N"
                elif validflag==1:
                    Flag="Y"
                else:
                    Flag="Unknow"
                temp=[]
                temp.append(sid)
                temp.append(equentry)
                temp.append(Flag)
                temp.append(upgradeflag)
                temp.append(hwtype)
                temp.append(hwid)
                temp.append(swrel)
                temp.append(swver)
                temp.append(dbver)
                temp.append(filelink)
                temp.append(filesize)
                temp.append(checknum)
                TableData.append(temp)
        sw_table={'ColumnName':ColumnName,'TableData':TableData}
        return sw_table

    def dft_dbi_tools_swload_info_add(self,inputData):
        equentry=inputData['equentry']
        validflag=inputData['validflag']
        upgradeflag=inputData['upgradeflag']
        hwtype=inputData['hwtype']
        hwid=inputData['hwid']
        swrel=inputData['swrel']
        swver=inputData['swver']
        dbver=inputData['dbver']
        filelink_new=inputData['filelink']
        filesize=inputData['filesize']
        checksum=inputData['checksum']
        dct_t_l3f10oam_swloadinfo.objects.create(equentry=equentry,validflag=validflag,upgradeflag=upgradeflag,
                                                 hwtype=hwtype,hwid=hwid,swrel=swrel,swver=swver,dbver=dbver,filelink=filelink_new,filesize=filesize,checksum=checksum)
        resp = {'auth': 'true', 'msg': "添加新的SW Load信息成功"}
        return resp

    def dft_dbi_tools_swload_info_delete(self,inputData):
        sid=inputData['sid']
        result=dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid)
        if result.exists():
            for line in result:
                file_link=line.filelink
                os.chmod(file_link,stat.S_IRWXO)
                os.unlink(file_link)
        dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid).delete()
        return True
    
    def dft_dbi_tools_swload_validflag_change(self,inputData):
        sid=inputData['sid']
        result=dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid)
        if result.exists():
            for line in result:
                validFlag=int(line.validflag)
                if validFlag==0:
                    new_validFlag=1
                    result.update(validflag=new_validFlag)
                elif validFlag==1:
                    new_validFlag=0
                    result.update(validflag=new_validFlag)
        return True
    
    
    '''处理从下位机发上来的消息'''
    def dft_dbi_hcu_inventory_confirm_view(self, socketId, inputData):
        Frusr=inputData['Frusr']
        ToUsr=inputData['ToUsr']
        MsgData=inputData['IeCnt']
        hwType=MsgData['ht']
        hwPemId=MsgData['hi']
        stSwRel=MsgData['ssr']
        stSwVer=MsgData['ssv']
        stDbVer=MsgData['sdv']
        stSwCheckSum=MsgData['ssc']
        stSwTotalLen=MsgData['ssl']
        stDbCheckSum=MsgData['sdc']
        stDbTotalLen=MsgData['sdl']
        trSwRel=MsgData['tsr']
        trSwVer=MsgData['tsv']
        trDbVer=MsgData['tdv']
        trSwCheckSum=MsgData['tsc']
        trSwTotalLen=MsgData['tsl']
        trDbCheckSum=MsgData['tdc']
        trDbTotalLen=MsgData['tdl']
        ptSwRel=MsgData['psr']
        ptSwVer=MsgData['psv']
        ptDbVer=MsgData['pdv']
        ptSwCheckSum=MsgData['psc']
        ptSwTotalLen=MsgData['psl']
        ptDbCheckSum=MsgData['pdc']
        ptDbTotalLen=MsgData['pdl']
        upgradeFlag=MsgData['up']
        stNodeSwRel=MsgData['snsr']
        stNodeSwVer=MsgData['snsv']
        stNodeSwCheckSum=MsgData['snsc']
        stNodeSwTotalLen=MsgData['snsl']
        trNodeSwRel=MsgData['tnsr']
        trNodeSwVer=MsgData['tnsv']
        trNodeSwCheckSum=MsgData['tnsc']
        trNodeSwTotalLen=MsgData['tnsl']
        ptNodeSwRel=MsgData['pnsr']
        ptNodeSwVer=MsgData['pnsv']
        ptNodeSwCheckSum=MsgData['pnsc']
        ptNodeSwTotalLen=MsgData['pnsl']
        result=dct_t_l3f10oam_swloadinfo.objects.filter(validflag=1,upgradeflag=upgradeFlag,hwtype=hwType,hwid=hwPemId)
        ht=0;hi=0;ssr=0;ssv=0;sdv=0;ssc=0;ssl=0;sdc=0;sdl=0;tsr=0;tsv=0;tdv=0;tsc=0;tsl=0;tdc=0;tdl=0;psr=0;psv=0;pdv=0;psc=0;psl=0;
        pdc=0;pdl=0;up=0;snsr=0;snsv=0;snsc=0;snsl=0;tnsr=0;tnsv=0;tnsc=0;tnsl=0;pnsv=0;pnsc=0;pnsl=0;pnsr=0
        if result.exists():
            ht = hwType
            hi = hwPemId
            up = upgradeFlag
            for line in result:
                if line.upgradeflag==1:
                    return
                elif line.upgradeflag==2:
                    ssr=line.swrel
                    ssv=line.swver
                    sdv=line.dbver
                    ssc=line.checksum
                    ssl=line.filesize
                elif line.upgradeflag == 3:
                    tsr = line.swrel
                    tsv = line.swver
                    tdv = line.dbver
                    tsc = line.checksum
                    tsl = line.filesize
                elif line.upgradeflag == 4:
                    psr = line.swrel
                    psv = line.swver
                    pdv = line.dbver
                    psc = line.checksum
                    psl = line.filesize
                else:
                    return
        else:
            return

        msg = {'socketid': socketId,
               'data': {'ToUsr': Frusr, 'FrUsr': ToUsr, "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                        'MsgId': 0XA021, 'MsgLn': 115, "IeCnt":
                            {"ht": ht, "hi": hi, "ssr": ssr, "ssv": ssv, "sdv": sdv, "ssc": ssc, "ssl": ssl, "sdc": sdc,
                             "sdl": sdl, "tsr": tsr, "tsv": tsv, "tdv": tdv, "tsc": tsc, "tsl": tsl, "tdc": tdc,
                             "tdl": tdl, "psr": psr, "psv": psv, "pdv": pdv, "psc": psc, "psl": psl, "pdc": pdc,
                             "pdl": pdl, "up": up, "snsr": snsr, "snsv": snsv, "snsc": snsc, "snsl": snsl, "tnsr": tnsr,
                             "tnsv": tnsv, "tnsc": tnsc, "tnsl": tnsl, "pnsr": pnsr, "pnsv": pnsv, "pnsc": pnsc,
                             "pnsl": pnsl, "ts": int(time.time())},
                        "FnFlg": 0}}
        msg_len = len(json.dumps(msg))
        msg_final = {'socketid': socketId,'data': {'ToUsr': Frusr, 'FrUsr': ToUsr, "CrTim": int(time.time()),'MsgTp': 'huitp_json', 'MsgId': 0XA021, 'MsgLn': msg_len,"IeCnt":
            {"ht": ht, "hi": hi, "ssr": ssr, "ssv": ssv, "sdv": sdv, "ssc": ssc, "ssl": ssl, "sdc": sdc, "sdl": sdl,
             "tsr": tsr, "tsv": tsv, "tdv": tdv, "tsc": tsc, "tsl": tsl, "tdc": tdc,
             "tdl": tdl, "psr": psr, "psv": psv, "pdv": pdv, "psc": psc, "psl": psl, "pdc": pdc, "pdl": pdl, "up": up,
             "snsr": snsr, "snsv": snsv, "snsc": snsc, "snsl": snsl, "tnsr": tnsr,
             "tnsv": tnsv, "tnsc": tnsc, "tnsl": tnsl, "pnsr": pnsr, "pnsv": pnsv, "pnsc": pnsc, "pnsl": pnsl,
             "ts": int(time.time())},
                                                   "FnFlg": 0}}
        return msg_final