from django.shortcuts import render
import pycurl
import io,os,stat
import time,datetime
from DappDbSnr.models import *
from DappDbF2cm.models import *
from DappDbFxprcm.models import *
from DappDbF3dm.models import *
# Create your views here.
class dct_classDbiL3apFxPrcm:
    __MFUN_HCU_AQYC_CU_SOAP_SERVER_URL = "http://112.64.17.60:9080/services/pushResource?wsdl"
    __MFUN_HCU_AQYC_VENDOR_NAME = "上海申环信息科技有限公司"
    __MFUN_L2SNR_COMAPI_HOUR_VALIDE_NUM = 54
    __MFUN_L2SNR_COMAPI_DAY_VALIDE_NUM = 21
    __MFUN_L2SDK_IOTHCU_ZHB_HRB_FRAME = "ZHB_HRB"
    __MFUN_L2SDK_IOTHCU_ZHB_NOM_FRAME = "ZHB_NOM"
    __MFUN_HCU_AQYC_STATUS_ON = "Y"
    __MFUN_HCU_AQYC_STATUS_OFF = "N"
    __MFUN_HCU_AQYC_SLEEP_DURATION = 3600
    __MFUN_HCU_AQYC_TIME_GRID_SIZE = 1
    __MFUN_HCU_AQYC_CAM_USERNAME = "admin"
    __MFUN_HCU_AQYC_CAM_PASSWORD = "Bxxh!123"
    __MFUN_L3APL_F3DM_AQYC_STYPE_PREFIX = "YC"
    __MFUN_L3APL_F3DM_AQYC_STYPE_PM = "YC_001"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD = "YC_002"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDDIR = "YC_003"
    __MFUN_L3APL_F3DM_AQYC_STYPE_EMC = "YC_005"
    __MFUN_L3APL_F3DM_AQYC_STYPE_TEMP = "YC_006"
    __MFUN_L3APL_F3DM_AQYC_STYPE_HUMID = "YC_007"
    __MFUN_L3APL_F3DM_AQYC_STYPE_NOISE = "YC_00A"
    __MFUN_HCU_CMDID_VERSION_SYNC = 0xF0
    __MFUN_HCU_CMDID_TIME_SYNC = 0xF2
    __MFUN_HCU_CMDID_EMC_DATA = 0x20
    __MFUN_HCU_CMDID_PM25_DATA = 0x25
    __MFUN_HCU_CMDID_WINDSPD_DATA = 0x26
    __MFUN_HCU_CMDID_WINDDIR_DATA = 0x27
    __MFUN_HCU_CMDID_TEMP_DATA = 0x28
    __MFUN_HCU_CMDID_HUMID_DATA = 0x29
    __MFUN_HCU_CMDID_HSMMP_DATA = 0x2C
    __MFUN_HCU_CMDID_NOISE_DATA = 0x2B
    __MFUN_HCU_CMDID_INVENTORY_DATA = 0xA0
    __MFUN_HCU_CMDID_SW_UPDATE = 0xA1
    __MFUN_HCU_CMDID_HEART_BEAT = 0xFE
    __MFUN_HCU_CMDID_HCU_POLLING = 0xFD
    __MFUN_HCU_CMDID_HCU_ALARM_DATA = 0xB0
    __MFUN_HCU_CMDID_HCU_PERFORMANCE = 0xB1
    __MFUN_HCU_MODBUS_DATA_REQ = 0x01
    __MFUN_HCU_MODBUS_SWITCH_SET = 0x02
    __MFUN_HCU_MODBUS_ADDR_SET = 0x03
    __MFUN_HCU_MODBUS_PERIOD_SET = 0x04
    __MFUN_HCU_MODBUS_SAMPLES_SET = 0x05
    __MFUN_HCU_MODBUS_TIMES_SET = 0x06
    __MFUN_HCU_MODBUS_SWITCH_READ = 0x07
    __MFUN_HCU_MODBUS_ADDR_READ = 0x08
    __MFUN_HCU_MODBUS_PERIOD_READ = 0x09
    __MFUN_HCU_MODBUS_SAMPLES_READ = 0x0A
    __MFUN_HCU_MODBUS_TIMES_READ = 0x0B
    __MFUN_HCU_MODBUS_DATA_REPORT = 0x81
    __MFUN_HCU_MODBUS_SWITCH_SET_ACK = 0x82
    __MFUN_HCU_MODBUS_ADDR_SET_ACK = 0x83
    __MFUN_HCU_MODBUS_PERIOD_SET_ACK = 0x84
    __MFUN_HCU_MODBUS_SAMPLE_SET_ACK = 0x85
    __MFUN_HCU_MODBUS_TIMES_SET_ACK = 0x86
    __MFUN_HCU_MODBUS_SWITCH_READ_ACK = 0x87
    __MFUN_HCU_MODBUS_ADDR_READ_ACK = 0x88
    __MFUN_HCU_MODBUS_PERIOD_READ_ACK = 0x89
    __MFUN_HCU_MODBUS_SAMPLE_READ_ACK = 0x8A
    __MFUN_HCU_MODBUS_TIMES_READ_ACK = 0x8B
    __MFUN_L3APL_F4ICM_ID_EQUIP_PM = 0x01
    __MFUN_L3APL_F4ICM_ID_EQUIP_WINDSPD = 0x02
    __MFUN_L3APL_F4ICM_ID_EQUIP_WINDDIR = 0x03
    __MFUN_L3APL_F4ICM_ID_EQUIP_EMC = 0x04
    __MFUN_L3APL_F4ICM_ID_EQUIP_TEMP = 0x05
    __MFUN_L3APL_F4ICM_ID_EQUIP_HUMID = 0x06
    __MFUN_L3APL_F4ICM_ID_EQUIP_NOISE = 0x0A
    __MFUN_CLOUD_WWW = 'www.hkrob.com'
    __MFUN_HCU_SITE_PIC_WWW_PATH = '/avorion/picture/'
    __MFUN_HCU_SITE_PIC_BASE_DIR = '../../avorion/picture/'
    __MFUN_HCU_SITE_PIC_FILE_TYPE = ".jpg"

    __MFUN_L3APL_F2CM_KEY_TYPE_USER = "U"
    __MFUN_L3APL_F2CM_KEY_PREFIX = "KEY"
    __MFUN_L3APL_F2CM_KEY_ID_LEN = 6
    __MFUN_L3APL_F2CM_KEY_TYPE_RFID = "R"
    __MFUN_L3APL_F2CM_KEY_TYPE_BLE = "B"
    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT = "W"
    __MFUN_L3APL_F2CM_KEY_TYPE_IDCARD = "I"
    __MFUN_L3APL_F2CM_KEY_TYPE_PHONE = "P"
    __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED = "N"

    __MFUN_L3APL_F2CM_AUTH_LEVEL_PROJ = "P"
    __MFUN_L3APL_F2CM_AUTH_LEVEL_DEVICE = "D"
    __MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER = "N"
    __MFUN_L3APL_F2CM_AUTH_TYPE_TIME = "T"
    __MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER = "F"

    #数据表单不存在关键字段
    def dft_dbi_fstt_neno_status(self,inputData):
        projCode=inputData['projCode']
        statCode=inputData['statCode']
        if statCode=='all':
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=projCode)
            if result.exists():
                for line in result:
                    statCode=line.site_code
                    resp=dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=statCode)
                    if resp.exists():
                        for line in resp:
                            startTime=line.lamp_start
                            stopTime=line.lamp_stop
                            lampMode=line.lamp_mode
                            snrLight=line.snr_light
                            ret={'start':startTime,'end':stopTime,'mode':[lampMode,lampMode],'target':snrLight}
                            resp_msg={'result':True,'ret':ret,'msg':'获取塔站灯带配置参数成功'}
                    else:
                        resp_msg = {'result': True, 'ret': [], 'msg': '获取塔站灯带配置参数失败'}
            else:
                resp_msg = {'result': False, 'ret': [], 'msg': '指定项目下没有塔站'}
        else:
            resp = dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=statCode)
            if resp.exists():
                for line in resp:
                    startTime = line.lamp_start
                    stopTime = line.lamp_stop
                    lampMode = line.lamp_mode
                    snrLight = line.snr_light
                    ret = {'start': startTime, 'end': stopTime, 'mode': [lampMode, lampMode], 'target': snrLight}
                    resp_msg = {'result': True, 'ret': ret, 'msg': '获取塔站灯带配置参数成功'}
            else:
                resp_msg = {'result': True, 'ret': [], 'msg': '获取塔站灯带配置参数失败'}
        return resp_msg
    ''' 原函数有问题'''
    def dft_dbi_fstt_set_neon_status(self,inputData):
        projCode=inputData['projCode']
        statCode=inputData['statCode']
        start=inputData['start']
        end=inputData['end']
        mode=inputData['mode']
        target=inputData['target']
        return False

    def dft_dbi_get_three_camera_status(self,statCode):
        resp=[]
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return resp
        result=dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=devCode)
        cam_1 = {}
        cam_2 = {}
        cam_3 = {}
        if result.exists():
            for line in result:
                url_1=line.cam_url
                filename = ""
                username = self.__MFUN_HCU_AQYC_CAM_USERNAME
                password = self.__MFUN_HCU_AQYC_CAM_PASSWORD
                curl = pycurl.Curl()
                curl.setopt(pycurl.URL, url_1)
                curl.setopt(pycurl.HEADER, 0)
                curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
                curl.setopt(pycurl.PROXYUSERPWD, username + ":" + password)
                curl.setopt(pycurl.TIMEOUT, 30)
                buf = io.BytesIO()
                curl.setopt(pycurl.WRITEFUNCTION, buf.write)
                curl.perform()
                filesize = curl.getinfo(pycurl.SIZE_DOWNLOAD)
                picdata = buf.getvalue()
                curl.close()
                if filesize != 0:
                    if os.path.exists(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode)) == False:
                        os.mkdir(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode), stat.S_IRWXO)
                    timestamp = int(time.time())
                    filename = str(statCode) + "_C1_" + str(timestamp)
                    picname = filename + self.__MFUN_HCU_SITE_PIC_FILE_TYPE
                    filelink = self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode) + "/" + str(picname)
                    newfile = open(filelink, 'wb')
                    newfile.write(picdata)
                    newfile.close()
                    stamp = datetime.datetime.today()
                    date = stamp.date()
                    hourminindex = (stamp.hour * 60 + stamp.minute) / 1.0
                    filesize = int(filesize)
                    description = "站点" + statCode + '上传的照片'
                    dataflag = "Y"
                    dct_t_l2snr_picture.objects.create(site_code_id=statCode, file_name=filename, file_size=filesize,
                                                       description=description, report_data=date,
                                                       hourminindex=hourminindex, dataflag=dataflag)
                    picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                    cam_1 = {'id':'1',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_1 = {'id':'1',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_1 = {}

                url_2 = line.cam_url
                filename = ""
                username = self.__MFUN_HCU_AQYC_CAM_USERNAME
                password = self.__MFUN_HCU_AQYC_CAM_PASSWORD
                curl = pycurl.Curl()
                curl.setopt(pycurl.URL, url_2)
                curl.setopt(pycurl.HEADER, 0)
                curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
                curl.setopt(pycurl.PROXYUSERPWD, username + ":" + password)
                curl.setopt(pycurl.TIMEOUT, 30)
                buf = io.BytesIO()
                curl.setopt(pycurl.WRITEFUNCTION, buf.write)
                curl.perform()
                filesize = curl.getinfo(pycurl.SIZE_DOWNLOAD)
                picdata = buf.getvalue()
                curl.close()
                if filesize != 0:
                    if os.path.exists(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode)) == False:
                        os.mkdir(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode), stat.S_IRWXO)
                    timestamp = int(time.time())
                    filename = str(statCode) + "_C2_" + str(timestamp)
                    picname = filename + self.__MFUN_HCU_SITE_PIC_FILE_TYPE
                    filelink = self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode) + "/" + str(picname)
                    newfile = open(filelink, 'wb')
                    newfile.write(picdata)
                    newfile.close()
                    stamp = datetime.datetime.today()
                    date = stamp.date()
                    hourminindex = (stamp.hour * 60 + stamp.minute) / 1.0
                    filesize = int(filesize)
                    description = "站点" + statCode + '上传的照片'
                    dataflag = "Y"
                    dct_t_l2snr_picture.objects.create(site_code_id=statCode, file_name=filename, file_size=filesize,
                                                       description=description, report_data=date,
                                                       hourminindex=hourminindex, dataflag=dataflag)
                    picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                    cam_2 = {'id':'2',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_2 = {'id':'2',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_2 = {}

                url_3 = line.cam_url
                filename = ""
                username = self.__MFUN_HCU_AQYC_CAM_USERNAME
                password = self.__MFUN_HCU_AQYC_CAM_PASSWORD
                curl = pycurl.Curl()
                curl.setopt(pycurl.URL, url_3)
                curl.setopt(pycurl.HEADER, 0)
                curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
                curl.setopt(pycurl.PROXYUSERPWD, username + ":" + password)
                curl.setopt(pycurl.TIMEOUT, 30)
                buf = io.BytesIO()
                curl.setopt(pycurl.WRITEFUNCTION, buf.write)
                curl.perform()
                filesize = curl.getinfo(pycurl.SIZE_DOWNLOAD)
                picdata = buf.getvalue()
                curl.close()
                if filesize != 0:
                    if os.path.exists(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode)) == False:
                        os.mkdir(self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode), stat.S_IRWXO)
                    timestamp = int(time.time())
                    filename = str(statCode) + "_C3_" + str(timestamp)
                    picname = filename + self.__MFUN_HCU_SITE_PIC_FILE_TYPE
                    filelink = self.__MFUN_HCU_SITE_PIC_BASE_DIR + str(statCode) + "/" + str(picname)
                    newfile = open(filelink, 'wb')
                    newfile.write(picdata)
                    newfile.close()
                    stamp = datetime.datetime.today()
                    date = stamp.date()
                    hourminindex = (stamp.hour * 60 + stamp.minute) / 1.0
                    filesize = int(filesize)
                    description = "站点" + statCode + '上传的照片'
                    dataflag = "Y"
                    dct_t_l2snr_picture.objects.create(site_code_id=statCode, file_name=filename, file_size=filesize,
                                                       description=description, report_data=date,
                                                       hourminindex=hourminindex, dataflag=dataflag)
                    picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                    cam_3 = {'id':'3',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_3 = {'id':'3',"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_3 = {}
            resp.append(cam_1)
            resp.append(cam_2)
            resp.append(cam_3)
            return resp
        else:
            return resp

    def dft_dbi_fstt_app_dev_alarm(self,inputData):
        statCode=inputData['statcode']
        result=dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=statCode)
        statuslist=[]
        alarmlist=[]
        lightlist=[]
        photolist=[]
        if result.exists():
            for line in result:
                detail={'name':'产品编号','value':line.tower_code}
                statuslist.append(detail)
                detail = {'name': '产品类型', 'value': line.tower_type}
                statuslist.append(detail)
                detail = {'name': '产品所含', 'value': line.tower_conf}
                statuslist.append(detail)
                detail = {'name': '创建时间', 'value': line.tower_date}
                statuslist.append(detail)
        result=dct_t_l3f3dm_minute_report_fstt.objects.filter(site_code_id=statCode).order_by("-sid")
        if result.exists():
            map3={
                "AlarmName":'湿度',
                "AlarmEName":"Wet",
                "AlarmValue":result[0].humidity,
                "AlarmUnit":'%',
                "WarningTarget":'false',
            }
            alarmlist.append(map3)
            map4 = {
                "AlarmName": '温度',
                "AlarmEName": "Temperature",
                "AlarmValue": result[0].temperature,
                "AlarmUnit": 'C',
                "WarningTarget": 'false',
            }
            alarmlist.append(map4)
            map5 = {
                "AlarmName": '颗粒',
                "AlarmEName": "PM2.5",
                "AlarmValue": result[0].pm25,
                "AlarmUnit": 'ug/m3',
                "WarningTarget": 'false',
            }
            alarmlist.append(map5)
            if result[0].lampbelt==1:
                light={
                    'name':'灯带组1/2',
                    'value':'常亮中',
                }
                lightlist.append(light)
            else:
                light = {
                    'name': '灯带组1/2',
                    'value': '已熄灭',
                }
                lightlist.append(light)
            if result[0].lampbelt==1:
                light={
                    'name':'灯带组3/4',
                    'value':'常亮中',
                }
                lightlist.append(light)
            else:
                light = {
                    'name': '灯带组3/4',
                    'value': '已熄灭',
                }
                lightlist.append(light)
            if result[0].backlight==1:
                light={
                    'name': '广告屏',
                    'value': '正在播放：'+result[0].backtext,
                }
                lightlist.append(light)
            else:
                light = {
                    'name': '广告屏',
                    'value': "广告位招商中",
                }
                lightlist.append(light)
            ret=self.dft_dbi_get_three_camera_status(statCode)
            for i in range(3):
                if 'id' not in ret[i].keys():
                    temp={
                        'name':"摄像头"+str(i),
                        'value':"未工作",
                        'url':"./screenshot/"+str(i)+".png"
                    }
                else:
                    temp = {
                        'name': "摄像头" + ret[i]['id'],
                        'value': "工作正常",
                        'url': ret[i]['url']
                    }
                photolist.append(temp)
        body={
            'statustitle':'详细信息',
            'statuslist':statuslist,
            'alarmtitle':'传感器',
            'alarmlist':alarmlist,
            'lighttitle':'灯带',
            'lightlist':lightlist,
            'phototitle':'摄像头',
            'photolist':photolist,
        }
        return body

    def dft_dbi_fstt_app_monitor_list(self):
        sitelist=[]
        result=dct_t_l3f2cm_site_fstt.objects.all()
        if result.exists():
            for line in result:
                temp={
                    "StatCode":line.site_code_id,
                    "StatName":line.site_code.site_name,
                    "ChargeMan":line.site_code.superintendent,
                    "Telephone":line.site_code.telephone,
                    "Department":line.site_code.department,
                    "Address":line.site_code.address,
                    "Country":line.site_code.district,
                    "Street":line.site_code.street,
                    "Square":0,
                    "Flag_la":"N",
                    "Latitude":line.site_code.latitude/1000000,
                    "Flag_lo":"E",
                    "Longitude":line.site_code.longitude/1000000,
                    "ProStartTime":line.site_code.create_date,
                    "Stage":"",
                    "Status":line.site_code.status,
                }
                sitelist.append(temp)
        return sitelist
