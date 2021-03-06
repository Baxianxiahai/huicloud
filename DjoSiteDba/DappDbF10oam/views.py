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
    __MFUN_CLOUD_QRCODE_ABS_DIR = "/var/www/html/avorion/hcu_qrcode/"
    __MFUN_CLOUD_QRCODE_WWW_DIR = "/avorion/hcu_qrcode/"
    __MFUN_CLOUD_TEMP_DIR = './temp/'

    __MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN = 5
    __MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX = 100
    __MFUN_CLOUD_ADMINTOOLS_FHYS_QRCODE_BASE = "http://www.foome.com.cn/mfunhcu/l4hcuinstall/index.html?code="
    __MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE = "http://ngrok2.hkrob.com/mfunhcu/l4aqycactive/index.html?code="

    __HUITP_IEID_UNI_EQU_ENTRY_NONE = 0
    __HUITP_IEID_UNI_EQU_ENTRY_HCU_SW = 1
    __HUITP_IEID_UNI_EQU_ENTRY_HCU_DB = 2
    __HUITP_IEID_UNI_EQU_ENTRY_IHU = 3
    __HUITP_IEID_SUI_EQU_ENTRY_INVALID = 0XFF
    __HUITP_IEID_UNI_FW_UPGRADE_NONE = 0
    __HUITP_IEID_UNI_FW_UPGRADE_NO = 1
    __HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE = 2
    __HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL = 3
    __HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH = 4
    __HUITP_IEID_UNI_FW_UPGRADE_YES_INVALID = 0XFF
    __MFUN_HCU_SW_LOAD_FLAG_INVALID = 0
    __MFUN_HCU_SW_LOAD_FLAG_VALID = 1

    __MFUN_CLOUD_SWLOAD_DIR = "/var/www/html/avorion/hcu_sw_active/"

    def dft_dbi_scan_newcode_check(self, inputData):
        devCode = inputData['devCode']
        result = dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode)
        if result.exists():
            result = dct_t_l3f10oam_qrcodeinfo.objects.get(dev_code=devCode)
            result.validflag = 'Y'
            result.save()
            resp = True
        else:
            resp = False
        return resp

    def dft_dbi_aqyc_qrcode_scan_siteinfo_update_gps(self, inputData):
        devCode = inputData['devCode']
        latitude = inputData['latitude']
        longitude = inputData['longitude']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            site_code = result[0].site_code
            site_code.latitude = latitude
            site_code.longitude = longitude
            site_code.save()
        return True

    ###########################################################################
    '''                                  ADMINTOOLS                         '''

    ###########################################################################
    def dft_dbi_tools_qrcode_filelist(self, inputData):
        user = inputData['user']
        filelist = []
        if user == 'admin':
            result = dct_t_l3f10oam_regqrcode.objects.all()
            if result.exists():
                for line in result:
                    filename = line.zipfile
                    fileurl = self.__MFUN_CLOUD_QRCODE_WWW_DIR + filename
                    fileinfo = {'name': filename, 'URL': fileurl}
                    filelist.append(fileinfo)
        else:
            result = dct_t_l3f10oam_regqrcode.objects.filter(applyuser=user)
            if result.exists():
                for line in result:
                    filename = line.zipfile
                    fileurl = self.__MFUN_CLOUD_QRCODE_WWW_DIR + filename
                    fileinfo = {'name': filename, 'URL': fileurl}
                    filelist.append(fileinfo)
        return filelist

    def dft_dbi_tools_qrcode_newapply(self, inputData):
        body = inputData['body']
        user = inputData['user']
        facCode = body['FACCode']
        pdCode = body['PDCode']
        pjCode = body['PJCode']
        userCode = body['UserCode']
        productType = body['ProductType']
        formalFlag = body['FormalFlag']
        applyNum = int(body['ApplyNbr'])
        if applyNum > self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX:
            msg = "申请的数量不能超过" + str(self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_APPLY_MAX)
            resp = {'auth': 'false', 'msg': msg}
            return resp
        if (len(pdCode) >= 5):
            pdCode = pdCode[0:5]
        if len(pdCode) > 4:
            pdCode_base = pdCode
        else:
            pdCode_middle = "G" + pdCode
            pdCode_base = pdCode_middle.ljust(5).replace(" ", "_")
        if (pjCode == 'AQYC') | (pjCode == 'ANXX'):
            qrcode_base = self.__MFUN_CLOUD_ADMINTOOLS_AQYC_QRCODE_BASE
        elif pjCode == 'FHYS':
            qrcode_base = self.__MFUN_CLOUD_ADMINTOOLS_FHYS_QRCODE_BASE
        else:
            resp = {'auth': 'false', 'msg': "申请的项目代码不存在"}
            return resp
        if len(userCode) >= self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN:
            msg = "申请的用户代码必须小于最大允许长度" + str(self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN)
            resp = {'auth': 'false', 'msg': msg}
            return resp
        digLen = self.__MFUN_CLOUD_ADMINTOOLS_QRCODE_DIGCODE_LEN - len(userCode)
        result = dct_t_l3f10oam_regqrcode.objects.filter(pdtype=productType, pdcode=pdCode, pjcode=pjCode,
                                                         usercode=userCode)
        digStopArray = []
        if result.exists():
            for line in result:
                digStopArray.append(line.digstop)
            digstop = max(digStopArray)
            digStart = digstop + 1
            maxAllow = math.pow(10, digLen) - 1
            if (digStart + applyNum) <= maxAllow:
                digStop = digStart + applyNum - 1
                approveNum = applyNum
            elif ((digStart < maxAllow) and (maxAllow < digStart + applyNum)):
                digStop = maxAllow
                approveNum = maxAllow - digStart + 1
            else:
                digStop = 0
                approveNum = 0
        else:
            digStart = 1
            digStop = applyNum
            approveNum = applyNum
        if approveNum == 0:
            resp = {'auth': 'false', 'msg': "该请求条件已无代码可分配"}
            return resp
        else:
            resp = {'auth': 'true',
                    'digstart': digStart,
                    'digstop': digStop,
                    'diglen': digLen,
                    'qrcode_base': qrcode_base,
                    'approvenum': approveNum,
                    'pdcodebase': pdCode_base,
                    }
            return resp

    def dft_dbi_qrcode_data_insert(self, inputData):
        digStart = inputData['digstart']
        digStop = inputData['digstop']
        devCodeArray = inputData['DevCodeArray']
        user = inputData['user']
        zipfile = inputData['zipfile']
        approvenum = inputData['approvenum']
        facCode = inputData['FACCode']
        pdCode = inputData['PDCode']
        pjCode = inputData['PJCode']
        userCode = inputData['UserCode']
        productType = inputData['ProductType']
        formalFlag = inputData['FormalFlag']
        applyNum = int(inputData['ApplyNbr'])
        qrcode_insert_list = list()
        pj_insert_list = list()
        cail_list = list()
        base_port_max = dct_t_l3f2cm_device_inventory.objects.all().order_by("-base_port")[0].base_port
        for devCode in devCodeArray:
            if dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).exists():
                pass
            else:
                base_port_max = base_port_max + 1
                qrcode_insert_list.append(
                    dct_t_l3f2cm_device_inventory(dev_code=devCode, create_date=datetime.date.today(),
                                                  hw_type=int(pdCode), base_port=base_port_max))
                cail_list.append(dct_t_l3f2cm_device_cail(dev_code_id=devCode))
        dct_t_l3f2cm_device_inventory.objects.bulk_create(qrcode_insert_list)
        dct_t_l3f2cm_device_cail.objects.bulk_create(cail_list)
        time.sleep(1)
        if pjCode == 'AQYC':
            for devCode in devCodeArray:
                result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
                basePort = result[0].base_port
                weburl = "http://" + str(devCode) + "ngrok2.hkrob.com:8080/yii2basic/web/index.php"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "2" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "3" + "ISAPI/Streaming/Channels/1"
                pj_insert_list.append(
                    dct_t_l3f2cm_device_aqyc(dev_code_id=devCode, web_url=weburl, pic1_url=pic1url, ctrl1_url=ctrl1url,
                                             video1_url=video1url))
            dct_t_l3f2cm_device_aqyc.objects.bulk_create(pj_insert_list)

        time.sleep(1)
        if pjCode == 'FSTT':
            for devCode in devCodeArray:
                result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
                basePort = result[0].base_port
                weburl = "http://" + str(devCode) + "ngrok2.hkrob.com:8080/yii2basic/web/index.php"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "2" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "3" + "ISAPI/Streaming/Channels/101"
                pic2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "6" + "/ISAPI/Streaming/channels/1/picture"
                ctrl2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "6" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video2url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "7" + "ISAPI/Streaming/Channels/101"
                pic3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "8" + "/ISAPI/Streaming/channels/1/picture"
                ctrl3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "8" + "/ISAPI /PTZCtrl/channels/1/continuous"
                video3url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    basePort) + "9" + "ISAPI/Streaming/Channels/101"
                pj_insert_list.append(
                    dct_t_l3f2cm_device_fstt(dev_code_id=devCode, web_url=weburl, pic1_url=pic1url, ctrl1_url=ctrl1url,
                                             video1_url=video1url, pic2_url=pic2url, ctrl2_url=ctrl2url,
                                             video2_url=video2url,
                                             pic3_url=pic3url, ctrl3_url=ctrl3url, video3_url=video3url))
            dct_t_l3f2cm_device_fstt.objects.bulk_create(pj_insert_list)
        else:
            pass
        dct_t_l3f10oam_regqrcode.objects.create(applyuser=user, faccode=facCode, pdtype=productType, pdcode=pdCode,
                                                pjcode=pjCode, usercode=userCode, isformal=formalFlag,
                                                applynum=applyNum, approvenum=approvenum, digstart=digStart,
                                                digstop=digStop, zipfile=zipfile)
        return 'true'

    def dft_dbi_tools_swload_table_get(self, inputData):
        ColumnName = []
        TableData = []
        ColumnName.append('SID')
        ColumnName.append('EQU_ENTRY')
        ColumnName.append('VALID_FLAG')
        ColumnName.append('UPGRADE_FLAG')
        ColumnName.append('UPLOAD_TIME')
        ColumnName.append('HW_TYPE')
        ColumnName.append('HW_ID')
        ColumnName.append('SW_REL')
        ColumnName.append('SW_VER')
        ColumnName.append('DB_VER')
        ColumnName.append('FILE_LINK')
        ColumnName.append('FILE_SIZE')
        ColumnName.append('FILE_CHECKSUM')
        ColumnName.append('NOTE')
        equEntry = inputData['filter'][0]['value']
        validFlag = inputData['filter'][1]['value']
        upgradeFlag = inputData['filter'][2]['value']
        hwType = inputData['filter'][3]['value']
        hwPem = inputData['filter'][4]['value']
        swRel = inputData['filter'][5]['value']
        swVer = inputData['filter'][6]['value']
        dbVer = inputData['filter'][7]['value']
        if equEntry == "HCU_SW":
            equentry_d = self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW
        elif equEntry == "HCU_DB":
            equentry_d = self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB
        elif equEntry == "IHU_SW":
            equentry_d = self.__HUITP_IEID_UNI_EQU_ENTRY_IHU
        else:
            equentry_d = ""

        if validFlag == "INVALID":
            validflag_d = self.__MFUN_HCU_SW_LOAD_FLAG_INVALID
        elif validFlag == "VALID":
            validflag_d = self.__MFUN_HCU_SW_LOAD_FLAG_VALID
        else:
            validflag_d = ""

        if upgradeFlag == "UPGRADE_NO":
            upgradeflag_d = self.__HUITP_IEID_UNI_FW_UPGRADE_NO
        elif upgradeFlag == "STABLE_YES":
            upgradeflag_d = self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE
        elif upgradeFlag == "TRAIL_YES":
            upgradeflag_d = self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL
        elif upgradeFlag == "PATCH_YES":
            upgradeflag_d = self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH
        else:
            upgradeflag_d = ""

        sql = "SELECT * FROM DappDbF10oam_dct_t_l3f10oam_swloadinfo WHERE((CONCAT(equentry) LIKE '%%" + str(
            equentry_d) + "%%' ) " \
                          "AND (CONCAT(validflag) LIKE '%%" + str(validflag_d) + "%%')" \
                                                                                 "AND (CONCAT(upgradeflag) LIKE '%%" + str(
            upgradeflag_d) + "%%')" \
                             "AND (CONCAT(hwtype) LIKE '%%" + str(hwType) + "%%')" \
                                                                            "AND (CONCAT(hwid) LIKE '%%" + str(
            hwPem) + "%%')" \
                     "AND (CONCAT(swrel) LIKE '%%" + str(swRel) + "%%')" \
                                                                  "AND (CONCAT(swver) LIKE '%%" + str(swVer) + "%%')" \
                                                                                                               "AND (CONCAT(dbver) LIKE '%%" + str(
            dbVer) + "%%')" \
                     ")"
        result = dct_t_l3f10oam_swloadinfo.objects.raw(sql)
        for line in result:
            sid = line.sid
            equentry = line.equentry
            validflag = line.validflag
            upgradeflag = line.upgradeflag
            hwtype = line.hwtype
            hwid = line.hwid
            swrel = line.swrel
            swver = line.swver
            dbver = line.dbver
            filelink = line.filelink
            filesize = line.filesize
            checknum = line.checksum
            uploadtime = str(line.createtime)
            note = line.note
            if equentry == self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW:
                equentry = "HCU_SW"
            elif equentry == self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB:
                equentry = 'HCU_DB'
            elif equentry == self.__HUITP_IEID_UNI_EQU_ENTRY_IHU:
                equentry = 'IHU_SW'
            else:
                equentry = 'INVALID'

            if upgradeflag == self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE:
                upgradeflag = 'STABLE'
            elif upgradeflag == self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL:
                upgradeflag = "TRAIL"
            elif upgradeflag == self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH:
                upgradeflag = 'PATCH'
            else:
                upgradeflag = "INVALID"
            if validFlag == self.__MFUN_HCU_SW_LOAD_FLAG_INVALID:
                validFlag = "N"
            elif validFlag == self.__MFUN_HCU_SW_LOAD_FLAG_VALID:
                validFlag = "Y"
            temp = []
            temp.append(sid)
            temp.append(equentry)
            temp.append(validflag)
            temp.append(upgradeflag)
            temp.append(uploadtime)
            temp.append(hwtype)
            temp.append(hwid)
            temp.append(swrel)
            temp.append(swver)
            temp.append(dbver)
            temp.append(filelink)
            temp.append(filesize)
            temp.append(checknum)
            temp.append(note)
            TableData.append(temp)
        sw_table = {'ColumnName': ColumnName, 'TableData': TableData}
        return sw_table

    def dft_dbi_tools_swload_info_add(self, inputData):
        equentry = inputData['equentry']
        validflag = inputData['validflag']
        upgradeflag = inputData['upgradeflag']
        hwtype = inputData['hwtype']
        hwid = inputData['hwid']
        swrel = inputData['swrel']
        swver = inputData['swver']
        dbver = inputData['dbver']
        filelink_new = inputData['filelink']
        filesize = inputData['filesize']
        checksum = inputData['checksum']
        result = dct_t_l3f10oam_swloadinfo.objects.filter(filelink=filelink_new)
        if result.exists():
            resp = {'auth': 'false', 'msg': "SW Load信息已存在"}
            return resp
        else:
            dct_t_l3f10oam_swloadinfo.objects.create(equentry=equentry, validflag=validflag, upgradeflag=upgradeflag,
                                                     hwtype=hwtype, hwid=hwid, swrel=swrel, swver=swver, dbver=dbver,
                                                     filelink=filelink_new, filesize=filesize, checksum=checksum)
            resp = {'auth': 'true', 'msg': "添加新的SW Load信息成功"}
            return resp

    def dft_dbi_tools_swload_info_delete(self, inputData):
        sid = inputData['sid']
        result = dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid)
        if result.exists():
            for line in result:
                file_link = line.filelink
                os.chmod(file_link, stat.S_IRWXO)
                os.unlink(file_link)
        dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid).delete()
        return True

    def dft_dbi_tools_swload_validflag_change(self, inputData):
        sid = inputData['sid']
        result = dct_t_l3f10oam_swloadinfo.objects.filter(sid=sid)
        if result.exists():
            for line in result:
                validFlag = int(line.validflag)
                if validFlag == 0:
                    new_validFlag = 1
                    result.update(validflag=new_validFlag)
                elif validFlag == 1:
                    new_validFlag = 0
                    result.update(validflag=new_validFlag)
        return True

    '''处理从下位机发上来的消息'''

    def dft_dbi_hcu_inventory_confirm_view(self, socketId, inputData):
        Frusr = inputData['FrUsr']
        ToUsr = inputData['ToUsr']
        MsgData = inputData['IeCnt']
        hwType = MsgData['ht']
        hwPemId = MsgData['hi']
        stSwRel = MsgData['ssr']
        stSwVer = MsgData['ssv']
        stDbVer = MsgData['sdv']
        stSwCheckSum = MsgData['ssc']
        stSwTotalLen = MsgData['ssl']
        stDbCheckSum = MsgData['sdc']
        stDbTotalLen = MsgData['sdl']
        trSwRel = MsgData['tsr']
        trSwVer = MsgData['tsv']
        trDbVer = MsgData['tdv']
        trSwCheckSum = MsgData['tsc']
        trSwTotalLen = MsgData['tsl']
        trDbCheckSum = MsgData['tdc']
        trDbTotalLen = MsgData['tdl']
        ptSwRel = MsgData['psr']
        ptSwVer = MsgData['psv']
        ptDbVer = MsgData['pdv']
        ptSwCheckSum = MsgData['psc']
        ptSwTotalLen = MsgData['psl']
        ptDbCheckSum = MsgData['pdc']
        ptDbTotalLen = MsgData['pdl']
        upgradeFlag = MsgData['up']
        stNodeSwRel = MsgData['snsr']
        stNodeSwVer = MsgData['snsv']
        stNodeSwCheckSum = MsgData['snsc']
        stNodeSwTotalLen = MsgData['snsl']
        trNodeSwRel = MsgData['tnsr']
        trNodeSwVer = MsgData['tnsv']
        trNodeSwCheckSum = MsgData['tnsc']
        trNodeSwTotalLen = MsgData['tnsl']
        ptNodeSwRel = MsgData['pnsr']
        ptNodeSwVer = MsgData['pnsv']
        ptNodeSwCheckSum = MsgData['pnsc']
        ptNodeSwTotalLen = MsgData['pnsl']
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=Frusr).update(sw_ver=int(stSwVer))
        ht = hwType;
        hi = hwPemId;
        ssr = stSwRel;
        ssv = stSwVer;
        sdv = stDbVer;
        ssc = stSwCheckSum;
        ssl = stSwTotalLen;
        sdc = stDbCheckSum;
        sdl = stDbTotalLen;
        tsr = trSwRel;
        tsv = trSwVer;
        tdv = trDbVer;
        tsc = trSwCheckSum;
        tsl = trSwTotalLen;
        tdc = trDbCheckSum;
        tdl = trDbTotalLen;
        psr = ptSwRel;
        psv = ptSwVer;
        pdv = ptDbVer;
        psc = ptSwCheckSum;
        psl = ptSwTotalLen;
        pdc = ptDbCheckSum;
        pdl = ptDbTotalLen;
        up = upgradeFlag;
        snsr = stNodeSwRel;
        snsv = stNodeSwVer;
        snsc = stNodeSwCheckSum;
        snsl = stNodeSwTotalLen;
        tnsr = trNodeSwRel;
        tnsv = trNodeSwVer;
        tnsc = trNodeSwCheckSum;
        tnsl = trNodeSwTotalLen;
        pnsv = ptNodeSwRel;
        pnsc = ptNodeSwVer;
        pnsl = ptNodeSwCheckSum;
        pnsr = ptNodeSwTotalLen
        result_s = dct_t_l3f10oam_swloadinfo.objects.filter(equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW,
                                                            validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE,
                                                            hwtype=hwType).order_by("-swrel", "-swver")
        if result_s.exists():
            ssr = result_s[0].swrel
            ssv = result_s[0].swver
            sdv = result_s[0].dbver
            ssc = result_s[0].checksum
            ssl = result_s[0].filesize
            resp_s_db = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                                 equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB,
                                                                 hwtype=hwType, dbver=sdv)
            if resp_s_db.exists():
                sdc = resp_s_db[0].checksum
                sdl = resp_s_db[0].filesize
        result_t = dct_t_l3f10oam_swloadinfo.objects.filter(equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW,
                                                            validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL
                                                            , hwtype=hwType).order_by("-swrel", "-swver")
        if result_t.exists():
            tsr = result_t[0].swrel
            tsv = result_t[0].swver
            tdv = result_t[0].dbver
            tsc = result_t[0].checksum
            tsl = result_t[0].filesize
            resp_t_db = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                                 equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB,
                                                                 #                                                                  upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL,
                                                                 hwtype=hwType, dbver=tdv)
            if resp_t_db.exists():
                tdc = resp_t_db[0].checksum
                tdl = resp_t_db[0].filesize
        result_p = dct_t_l3f10oam_swloadinfo.objects.filter(equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_SW,
                                                            validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                            upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH
                                                            , hwtype=hwType).order_by("-swrel", "-swver")
        if result_p.exists():
            psr = result_p[0].swrel
            psv = result_p[0].swver
            pdv = result_p[0].dbver
            psc = result_p[0].checksum
            psl = result_p[0].filesize
            resp_p_db = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                                 equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_HCU_DB,
                                                                 #                                                                  upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH,
                                                                 hwtype=hwType, dbver=pdv)
            if resp_p_db.exists():
                pdc = resp_p_db[0].checksum
                pdl = resp_p_db[0].filesize
        resp_s_ihu = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                              equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_IHU,
                                                              upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_STABLE,
                                                              hwtype=hwType).order_by("-swrel", "-swver")
        if resp_s_ihu.exists():
            snsr = resp_s_ihu[0].swrel
            snsv = resp_s_ihu[0].swver
            snsc = resp_s_ihu[0].checksum
            snsl = resp_s_ihu[0].filesize
        resp_t_ihu = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                              equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_IHU,
                                                              upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_TRAIL,
                                                              hwtype=hwType).order_by("-swrel", "-swver")
        if resp_t_ihu.exists():
            tnsr = resp_t_ihu[0].swrel
            tnsv = resp_t_ihu[0].swver
            tnsc = resp_t_ihu[0].checksum
            tnsl = resp_t_ihu[0].filesize
        resp_p_ihu = dct_t_l3f10oam_swloadinfo.objects.filter(validflag=self.__MFUN_HCU_SW_LOAD_FLAG_VALID,
                                                              equentry=self.__HUITP_IEID_UNI_EQU_ENTRY_IHU,
                                                              upgradeflag=self.__HUITP_IEID_UNI_FW_UPGRADE_YES_PATCH,
                                                              hwtype=hwType).order_by("-swrel", "-swver")
        if resp_p_ihu.exists():
            pnsr = resp_p_ihu[0].swrel
            pnsv = resp_p_ihu[0].swver
            pnsc = resp_p_ihu[0].checksum
            pnsl = resp_p_ihu[0].filesize
        msg = {'socketid': socketId,
               'data': {'ToUsr': Frusr, 'FrUsr': ToUsr, "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                        'MsgId': 0XA021, 'MsgLn': 115, "IeCnt":
                            {"ht": ht, "hi": hi, "ssr": ssr, "ssv": ssv, "sdv": sdv, "ssc": ssc, "ssl": ssl, "sdc": sdc,
                             "sdl": sdl, "tsr": tsr, "tsv": tsv, "tdv": tdv, "tsc": tsc, "tsl": tsl, "tdc": tdc,
                             "tdl": tdl, "psr": psr, "psv": psv, "pdv": pdv, "psc": psc, "psl": psl, "pdc": pdc,
                             "pdl": pdl, "up": up, "snsr": snsr, "snsv": snsv, "snsc": snsc, "snsl": snsl, "tnsr": tnsr,
                             "tnsv": tnsv, "tnsc": tnsc, "tnsl": tnsl, "pnsr": pnsr, "pnsv": pnsv, "pnsc": pnsc,
                             "pnsl": pnsl, "ts": int(time.time())}, "FnFlg": 0}}
        msg_len = len(json.dumps(msg))
        msg_final = {'socketid': socketId,
                     'data': {'ToUsr': Frusr, 'FrUsr': ToUsr, "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                              'MsgId': 0XA021, 'MsgLn': msg_len, "IeCnt":
                                  {"ht": ht, "hi": hi, "ssr": ssr, "ssv": ssv, "sdv": sdv, "ssc": ssc, "ssl": ssl,
                                   "sdc": sdc, "sdl": sdl,
                                   "tsr": tsr, "tsv": tsv, "tdv": tdv, "tsc": tsc, "tsl": tsl, "tdc": tdc,
                                   "tdl": tdl, "psr": psr, "psv": psv, "pdv": pdv, "psc": psc, "psl": psl, "pdc": pdc,
                                   "pdl": pdl, "up": up,
                                   "snsr": snsr, "snsv": snsv, "snsc": snsc, "snsl": snsl, "tnsr": tnsr,
                                   "tnsv": tnsv, "tnsc": tnsc, "tnsl": tnsl, "pnsr": pnsr, "pnsv": pnsv, "pnsc": pnsc,
                                   "pnsl": pnsl,
                                   "ts": int(time.time())}, "FnFlg": 0}}
        return msg_final
