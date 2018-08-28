from django.shortcuts import render
import math
import time
import os
import stat

# Create your views here.
from DappDbF10oam.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
class dct_DappF10Class():
    __MFUN_CLOUD_QRCODE_ABS_DIR="/var/www/html/avorion/hcu_qrcode/"
    __MFUN_CLOUD_QRCODE_WWW_DIR="/avorion/hcu_qrcode/"
    __MFUN_CLOUD_TEMP_DIR='./temp/'

    __MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN=6
    __MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX=100
    __MFUN_CLOUD_ADMINTOOLS_FHYS_QRCODE_BASE="http://www.foome.com.cn/mfunhcu/l4hcuinstall/index.html?code="
    __MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE="http://www.hkrob.com/mfunhcu/l4aqycactive/index.html?code="

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
        result=dct_t_l3f2cm_device_common.objects.filter(dev_code=devCode)
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

        if pjCode=='AQYC':
            qrcode_base=self.__MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE
        elif pjCode=='FHYS':
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
                    'approvenum':approveNum}
            return resp
    def dft_dbi_qrcode_data_insert(self,inputData):
        digStart=inputData['digstart']
        digStop=inputData['digstop']
        devCode=inputData['devcode']
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
        for digStart in range(digStop+1):
            dct_t_l3f10oam_qrcodeinfo.objects.create(pdtype=productType,pdcode=pdCode,pjcode=pjCode,dev_code=devCode)
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
                temp=[]
                temp.append(sid)
                temp.append(equentry)
                temp.append(validflag)
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
        filename=inputData['filename']
        nameseg_entry='XXX'
        nameseg_upgrade='XXX'
        nameseg_type='XXX'
        if equentry=='HCU_SW':
            equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW
            nameseg_entry='HCU'
            nameseg_type='.HEX'
        elif equentry=='HCU_DB':
            equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB
            nameseg_entry='HCU'
            nameseg_type=".SQL"
            nameseg_upgrade='MYSQL'
        elif equentry=='IHU_SW':
            equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_IHU
            nameseg_entry='IHU'
            nameseg_type=".BIN"
        else:
            equentry=self.__HUITP_IEID_SUI_EQU_ENTRY_INVALID
            nameseg_entry='XXX'
            nameseg_type=".XXX"
        if validflag=="INVALID":
            validflag=self.__MFUN_HCU_SW_LOAD_FLAG_INVALID
        elif validflag=="VALID":
            validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID

        if upgradeflag=="UPGRADE_NO":
            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_NO
        elif upgradeflag=="STABLE_YES":
            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE
            nameseg_upgrade='STABLE'
        elif upgradeflag=="TRAIL_YES":
            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL
            nameseg_upgrade="TRAIL"
        elif upgradeflag=="PATCH_YES":
            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH
            nameseg_upgrade='PATCH'
        else:
            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_INVALID
        file_link=self.__MFUN_CLOUD_SWLOAD_DIR+filename
        if os.path.exists(file_link):
            resp={'auth':'false','msg':"文件上传失败"}
            return resp
        if equentry=='HCU_DB':
            filename_new = nameseg_entry + "_HPT" + hwtype + "_PEM" + hwid + "_REL" + swrel + "_VER" + dbver + "_" + nameseg_upgrade+nameseg_type
        else:
            filename_new = nameseg_entry + "_HPT" + hwtype + "_PEM" + hwid + "_REL" + swrel + "_VER" + swver + "_" + nameseg_upgrade+nameseg_type
        filelink_new=self.__MFUN_CLOUD_SWLOAD_DIR+filename_new
        os.chmod(filename_new,stat.S_IRWXO)
        os.rename(file_link,filelink_new)

        filesize=os.path.getsize(filelink_new)
        f_handle=os.open(filelink_new,os.O_RDWR)
        content=os.read(f_handle,filesize)
        os.close(f_handle)
        if filesize==False or content==False:
            resp = {'auth': 'false', 'msg': "计算CHECKSUM，文件读取失败"}
            return resp
        checksum=0
        for i in range(filesize):
            data=ord(content[i])
            checksum=checksum+data
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