from django.shortcuts import render
import time,datetime
import pycurl
import io,os,stat
from DappDbF2cm.models import *
from DappDbSnr.models import *
from DappDbF1sym.models import *
import random
# Create your views here.
class dct_classDbiL3apF4icm:
    __MFUN_HCU_AQYC_CU_SOAP_SERVER_URL="http://112.64.17.60:9080/services/pushResource?wsdl"
    __MFUN_HCU_AQYC_VENDOR_NAME="上海申环信息科技有限公司"
    __MFUN_L2SNR_COMAPI_HOUR_VALIDE_NUM=54
    __MFUN_L2SNR_COMAPI_DAY_VALIDE_NUM=21
    __MFUN_L2SDK_IOTHCU_ZHB_HRB_FRAME="ZHB_HRB"
    __MFUN_L2SDK_IOTHCU_ZHB_NOM_FRAME="ZHB_NOM"
    __MFUN_HCU_AQYC_STATUS_ON="Y"
    __MFUN_HCU_AQYC_STATUS_OFF="N"
    __MFUN_HCU_AQYC_SLEEP_DURATION=3600
    __MFUN_HCU_AQYC_TIME_GRID_SIZE=1
    __MFUN_HCU_AQYC_CAM_USERNAME="admin"
    __MFUN_HCU_AQYC_CAM_PASSWORD="Bxxh!123"
    __MFUN_L3APL_F3DM_AQYC_STYPE_PREFIX="YC"
    __MFUN_L3APL_F3DM_AQYC_STYPE_PM="YC_001"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD="YC_002"
    __MFUN_L3APL_F3DM_AQYC_STYPE_WINDDIR="YC_003"
    __MFUN_L3APL_F3DM_AQYC_STYPE_EMC="YC_005"
    __MFUN_L3APL_F3DM_AQYC_STYPE_TEMP="YC_006"
    __MFUN_L3APL_F3DM_AQYC_STYPE_HUMID="YC_007"
    __MFUN_L3APL_F3DM_AQYC_STYPE_NOISE="YC_00A"
    __MFUN_HCU_CMDID_VERSION_SYNC=0xF0
    __MFUN_HCU_CMDID_TIME_SYNC=0xF2
    __MFUN_HCU_CMDID_EMC_DATA=0x20
    __MFUN_HCU_CMDID_PM25_DATA=0x25
    __MFUN_HCU_CMDID_WINDSPD_DATA=0x26
    __MFUN_HCU_CMDID_WINDDIR_DATA=0x27
    __MFUN_HCU_CMDID_TEMP_DATA=0x28
    __MFUN_HCU_CMDID_HUMID_DATA=0x29
    __MFUN_HCU_CMDID_HSMMP_DATA=0x2C
    __MFUN_HCU_CMDID_NOISE_DATA=0x2B
    __MFUN_HCU_CMDID_INVENTORY_DATA=0xA0
    __MFUN_HCU_CMDID_SW_UPDATE=0xA1
    __MFUN_HCU_CMDID_HEART_BEAT=0xFE
    __MFUN_HCU_CMDID_HCU_POLLING=0xFD
    __MFUN_HCU_CMDID_HCU_ALARM_DATA=0xB0
    __MFUN_HCU_CMDID_HCU_PERFORMANCE=0xB1
    __MFUN_HCU_MODBUS_DATA_REQ=0x01
    __MFUN_HCU_MODBUS_SWITCH_SET=0x02
    __MFUN_HCU_MODBUS_ADDR_SET=0x03
    __MFUN_HCU_MODBUS_PERIOD_SET=0x04
    __MFUN_HCU_MODBUS_SAMPLES_SET=0x05
    __MFUN_HCU_MODBUS_TIMES_SET=0x06
    __MFUN_HCU_MODBUS_SWITCH_READ=0x07
    __MFUN_HCU_MODBUS_ADDR_READ=0x08
    __MFUN_HCU_MODBUS_PERIOD_READ=0x09
    __MFUN_HCU_MODBUS_SAMPLES_READ=0x0A
    __MFUN_HCU_MODBUS_TIMES_READ=0x0B
    __MFUN_HCU_MODBUS_DATA_REPORT=0x81
    __MFUN_HCU_MODBUS_SWITCH_SET_ACK=0x82
    __MFUN_HCU_MODBUS_ADDR_SET_ACK=0x83
    __MFUN_HCU_MODBUS_PERIOD_SET_ACK=0x84
    __MFUN_HCU_MODBUS_SAMPLE_SET_ACK=0x85
    __MFUN_HCU_MODBUS_TIMES_SET_ACK=0x86
    __MFUN_HCU_MODBUS_SWITCH_READ_ACK=0x87
    __MFUN_HCU_MODBUS_ADDR_READ_ACK=0x88
    __MFUN_HCU_MODBUS_PERIOD_READ_ACK=0x89
    __MFUN_HCU_MODBUS_SAMPLE_READ_ACK=0x8A
    __MFUN_HCU_MODBUS_TIMES_READ_ACK=0x8B
    __MFUN_L3APL_F4ICM_ID_EQUIP_PM=0x01
    __MFUN_L3APL_F4ICM_ID_EQUIP_WINDSPD=0x02
    __MFUN_L3APL_F4ICM_ID_EQUIP_WINDDIR=0x03
    __MFUN_L3APL_F4ICM_ID_EQUIP_EMC=0x04
    __MFUN_L3APL_F4ICM_ID_EQUIP_TEMP=0x05
    __MFUN_L3APL_F4ICM_ID_EQUIP_HUMID=0x06
    __MFUN_L3APL_F4ICM_ID_EQUIP_NOISE=0x0A
    __MFUN_CLOUD_WWW='www.hkrob.com'
    __MFUN_HCU_SITE_PIC_WWW_PATH='/avorion/picture/'
    __MFUN_HCU_SITE_PIC_BASE_DIR='../../avorion/picture/'
    __MFUN_HCU_SITE_PIC_FILE_TYPE=".jpg"

    __MFUN_L3APL_F2CM_KEY_TYPE_USER="U"
    __MFUN_L3APL_F2CM_KEY_PREFIX="KEY"
    __MFUN_L3APL_F2CM_KEY_ID_LEN=6
    __MFUN_L3APL_F2CM_KEY_TYPE_RFID="R"
    __MFUN_L3APL_F2CM_KEY_TYPE_BLE="B"
    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT="W"
    __MFUN_L3APL_F2CM_KEY_TYPE_IDCARD="I"
    __MFUN_L3APL_F2CM_KEY_TYPE_PHONE="P"
    __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"

    __MFUN_L3APL_F2CM_AUTH_LEVEL_PROJ="P"
    __MFUN_L3APL_F2CM_AUTH_LEVEL_DEVICE="D"
    __MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER="N"
    __MFUN_L3APL_F2CM_AUTH_TYPE_TIME="T"
    __MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER="F"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"
    # __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED="N"

    def __dft_getRandomUid(self, strlen):
        str_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        uid = ''.join(random.sample(str_array, strlen))
        return uid

    def dft_dbi_sensor_info_update(self,inputData):
        devCode=inputData['DevCode']
        sensorCode=inputData['SensorCode']
        status=inputData['status']
        paraList=inputData['ParaList']
        result=dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode)
        resp=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        socket_id=""
        for line in resp:
            socket_id=line.socket_id
        report_data=[]
        if result.exists():
            for line in result:
                temp={}
                if sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_PM:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_PM25_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_PM)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDSPD:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_WINDSPD_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_WINDSPD)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_WINDDIR:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_WINDDIR_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_WINDDIR)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_EMC:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_EMC_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_EMC)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_TEMP:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_TEMP_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_TEMP)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_HUMID:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_HUMID_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_HUMID)[-2:]

                elif sensorCode==self.__MFUN_L3APL_F3DM_AQYC_STYPE_NOISE:
                    ctrl_key=hex(self.__MFUN_HCU_CMDID_NOISE_DATA)[-2:]
                    equip_id=hex(self.__MFUN_L3APL_F4ICM_ID_EQUIP_NOISE)[-2:]

                else:
                    ctrl_key=""
                    equip_id=""
                if status!="" and status!=line.status:
                    optkey_switch_set=hex(self.__MFUN_HCU_MODBUS_SWITCH_SET)[-2:]
                    dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode).update(status=status)
                i=0
                modebus_addr=""
                meas_period=""
                rx_interval=""
                meas_times=""
                while(i<len(paraList)):
                    value=paraList[i]['value']
                    if paraList[i]['name']=='MODBUS_Addr' and value!=line.modbus_addr:
                        modebus_addr=value
                        optkey_modbus_set=hex(self.__MFUN_HCU_MODBUS_ADDR_SET)
                        dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode).update(modebus_addr=value)
                    elif paraList[i]['name']=='Measurement_Period' and value!=line.meas_period:
                        meas_period=value
                        optkey_modbus_set=hex(self.__MFUN_HCU_MODBUS_ADDR_SET)
                        dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode).update(meas_period=value)
                    elif paraList[i]['name']=='Samples_Interval' and value!=line.rx_interval:
                        rx_interval=value
                        optkey_modbus_set=hex(self.__MFUN_HCU_MODBUS_ADDR_SET)
                        dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode).update(rx_interval=value)
                    elif paraList[i]['name']=='Measurement_Times' and value!=line.meas_times:
                        meas_times=value
                        optkey_modbus_set=hex(self.__MFUN_HCU_MODBUS_ADDR_SET)
                        dct_t_l2snr_sensor_ctrl.objects.filter(dev_code=devCode,snrtype=sensorCode).update(meas_times=value)
                    i=i+1
                temp={'ctrl_key':ctrl_key,'optkey_switch_set':optkey_switch_set,'status':status,'equip_id':equip_id,'devCode':devCode,
                      'modbus_addr':modebus_addr,'meas_period':meas_period,'rx_interval':rx_interval,'meas_times':meas_times,'optkey_modbus_set':optkey_modbus_set,'socketid':socket_id}
                report_data.append(temp)
                status='true'
        else:
            status='false'
        resp={'status':status,'data':report_data}
        return resp
    def dft_dbi_hcu_hsmmpdisplay_request(self,inputData):
        return True

    def dft_dbi_get_hcu_camweb_link(self,inputData):
        camweb=[]
        statcode=inputData['statcode']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return camweb
        result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        if result.exists():
            for line in result:
                cam_ctrl=line.ctrl1_url
                rtsp=line.video1_url
                camweb={'video':rtsp,'camera':cam_ctrl}
        return camweb
    def dft_dbi_hcu_hsmmplist_inquery(self,inputData):
        statcode=inputData['statcode']
        date=inputData['date']
        date=time.strptime(date,'%Y-%m-%d')
        hour=int(inputData['hour'])
        start=hour*60
        end=hour*60+59
        hsmmp_list=[]
        result=dct_t_l2snr_picture.objects.filter(site_code_id=statcode,report_data=date,hourminindex__gte=start,hourminindex__lt=end)
        if result.exists():
            for line in result:
                pic_name=line.file_name
                hourminindex=int(line.hourminindex)
                hourindex=float(hourminindex/60)
                minindex=hourminindex-hourindex*60
                pictureUrl=self.__MFUN_CLOUD_WWW+self.__MFUN_HCU_SITE_PIC_WWW_PATH+str(statcode)+'/'+pic_name
                attr='照片_'+str(date)+'_'+str(hourindex)+':'+str(minindex)
                temp={'id':pictureUrl,'attr':attr}
                hsmmp_list.append(temp)
        return hsmmp_list
    def dft_dbi_get_camera_status(self,inputData):
        statCode=inputData['statcode']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        resp=[]
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return resp
        result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        print(devCode)
        if result.exists():
            for line in result:
                url=line.pic1_url
                filename=""
                username=self.__MFUN_HCU_AQYC_CAM_USERNAME
                password=self.__MFUN_HCU_AQYC_CAM_PASSWORD
                curl = pycurl.Curl()
                curl.setopt(pycurl.URL,url)
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
                if filesize!=0:
                    if os.path.exists(self.__MFUN_HCU_SITE_PIC_BASE_DIR+str(statCode))==False:
                        os.mkdir(self.__MFUN_HCU_SITE_PIC_BASE_DIR+str(statCode),stat.S_IRWXO)
                    timestamp=int(time.time())
                    filename=str(statCode)+"_"+str(timestamp)
                    picname=filename+self.__MFUN_HCU_SITE_PIC_FILE_TYPE
                    filelink=self.__MFUN_HCU_SITE_PIC_BASE_DIR+str(statCode)+"/"+str(picname)
                    newfile=open(filelink,'wb')
                    newfile.write(picdata)
                    newfile.close()
                    stamp=datetime.datetime.today()
                    date=stamp.date()
                    hourminindex=(stamp.hour*60+stamp.minute)/1.0
                    filesize=int(filesize)
                    description="站点"+statCode+'上传的照片'
                    dataflag="Y"
                    dct_t_l2snr_picture.objects.create(site_code_id=statCode,file_name=filename,file_size=filesize,description=description,report_data=date,hourminindex=hourminindex,dataflag=dataflag)
                    picUrl=self.__MFUN_HCU_SITE_PIC_BASE_DIR+statCode+"/"+picname
                    resp={"v":'0','h':'0','z':'0','url':picUrl}
                else:
                    result=dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname=result[0].file_name
                        picUrl=self.__MFUN_HCU_SITE_PIC_BASE_DIR+statCode+"/"+picname
                        resp = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        resp={}
        else:
            resp={}
        return resp
    def dft_dbi_get_three_camera_status(self,inputData):
        statCode=inputData['statcode']
        resp=[]
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return resp
        result=dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=devCode)
        if result.exists():
            for line in result:
                url_1=line.pic1_url
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
                    cam_1 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_1 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_1 = {}

                url_2 = line.pic2_url
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
                    cam_2 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_2 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_2 = {}

                url_3 = line.pic3_url
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
                    cam_3 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                else:
                    result = dct_t_l2snr_picture.objects.filter(site_code_id=statCode).order_by('-sid')
                    if result.exists():
                        picname = result[0].file_name
                        picUrl = self.__MFUN_HCU_SITE_PIC_BASE_DIR + statCode + "/" + picname
                        cam_3 = {"v": '0', 'h': '0', 'z': '0', 'url': picUrl}
                    else:
                        cam_3 = {}
            resp.append(cam_1)
            resp.append(cam_2)
            resp.append(cam_3)
            return resp
        else:
            return resp

    def dft_dbi_adjust_camera_vertical(self,inputData):
        statCode=inputData['statCode']
        adj=inputData['adj']
        camID=inputData['camid']
        devCode=""
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return devCode
        resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        if resp.exists():
            for line in resp:
                pic_url=line.pic1_url
                vcrurl=line.ctrl1_url
        else:
            return False
        username=self.__MFUN_HCU_AQYC_CAM_USERNAME
        password=self.__MFUN_HCU_AQYC_CAM_PASSWORD
        ctrl_url=vcrurl+"/PTZCtrl/channels/1/continuous"
        if adj=="1":
            start_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>0</pan><tilt>60</tilt></PTZData>"
        elif adj=="-1":
            start_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>0</pan><tilt>-60</tilt></PTZData>"
        else:
            return False
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, ctrl_url)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.CUSTOMREQUEST, 'PUT')
        curl.setopt(pycurl.POSTFIELDS, start_xml_string)
        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
        curl.setopt(pycurl.TIMEOUT, 30)
        curl.perform()
        stop_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>0</pan><tilt>0</tilt></PTZData>"
        curl.setopt(pycurl.POSTFIELDS, stop_xml_string)
        curl.perform()
        curl.close()

        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, pic_url)
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
            filename = str(statCode) + "_" + str(timestamp)
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
            resp = {"v": str(adj), 'h': '0', 'z': '0', 'url': picUrl}
        else:
            return False
        return resp
    
    def dft_dbi_adjust_camera_horizon(self,inputData):
        statCode=inputData['statCode']
        adj=inputData['adj']
        camID=inputData['camid']
        devCode=""
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return devCode
        resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        if resp.exists():
            for line in resp:
                pic_url=line.pic1_url
                vcrurl=line.ctrl1_url
        else:
            return False
        username=self.__MFUN_HCU_AQYC_CAM_USERNAME
        password=self.__MFUN_HCU_AQYC_CAM_PASSWORD
        ctrl_url=vcrurl+"/PTZCtrl/channels/1/continuous"
        if adj=="1":
            start_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>60</pan><tilt>0</tilt></PTZData>"
        elif adj=="-1":
            start_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>-60</pan><tilt>0</tilt></PTZData>"
        else:
            return False
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, ctrl_url)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.CUSTOMREQUEST, 'PUT')
        curl.setopt(pycurl.POSTFIELDS, start_xml_string)
        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
        curl.setopt(pycurl.TIMEOUT, 30)
        curl.perform()
        stop_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><pan>0</pan><tilt>0</tilt></PTZData>"
        curl.setopt(pycurl.POSTFIELDS, stop_xml_string)
        curl.perform()
        curl.close()

        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, pic_url)
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
            filename = str(statCode) + "_" + str(timestamp)
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
            resp = {"v": str(adj), 'h': '0', 'z': '0', 'url': picUrl}
        else:
            return False
        return resp

    def dft_dbi_adjust_camera_zoom(self,inputData):
        statCode=inputData['statCode']
        adj=inputData['adj']
        camID=inputData['camid']
        devCode=""
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return False
        resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        if resp.exists():
            for line in resp:
                pic_url=line.pic1_url
                vcrurl=line.ctrl1_url
        else:
            return False
        username=self.__MFUN_HCU_AQYC_CAM_USERNAME
        password=self.__MFUN_HCU_AQYC_CAM_PASSWORD
        ctrl_url=vcrurl+"/PTZCtrl/channels/1/absolute"
        adj=int(adj)
        if adj>=0:
            position=(360-adj)*10
            input_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><AbsoluteHigh><elevation>000</elevation><azimuth>"+str(position)+"</azimuth><absoluteZoom>1</absoluteZoom></AbsoluteHigh></PTZData>"
        else:
            position = abs(adj)*10
            input_xml_string = "<PTZData version=\"2.0\" xmlns=\"http://www.hikvision.com/ver20/XMLSchema\"><AbsoluteHigh><elevation>000</elevation><azimuth>"+str(position)+"</azimuth><absoluteZoom>1</absoluteZoom></AbsoluteHigh></PTZData>"
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, ctrl_url)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.CUSTOMREQUEST, 'PUT')
        curl.setopt(pycurl.POSTFIELDS, input_xml_string)
        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
        curl.setopt(pycurl.TIMEOUT, 30)
        curl.perform()
        curl.close()
        time.sleep(8)

        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, pic_url)
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
            filename = str(statCode) + "_" + str(timestamp)
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
            resp = {"v": "0", 'h': str(adj), 'z': '0', 'url': picUrl}
        else:
            return False
        return resp

    def dft_dbi_adjust_camera_reset(self,inputData):
        statCode=inputData['statCode']
        camID=inputData['camid']
        devCode=""
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
        else:
            return False
        resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
        if resp.exists():
            for line in resp:
                pic_url=line.pic1_url
                vcrurl=line.ctrl1_url
        else:
            return False
        username=self.__MFUN_HCU_AQYC_CAM_USERNAME
        password=self.__MFUN_HCU_AQYC_CAM_PASSWORD
        ctrl_url=vcrurl+"/PTZCtrl/channels/1/homeposition/goto"
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, ctrl_url)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.CUSTOMREQUEST, 'PUT')
        curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_ANY)
        curl.setopt(pycurl.TIMEOUT, 30)
        curl.perform()
        curl.close()
        time.sleep(8)

        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, pic_url)
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
            filename = str(statCode) + "_" + str(timestamp)
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
            resp = {"v": "0", 'h': "0", 'z': '0', 'url': picUrl}
        else:
            return False
        return resp

    def dft_dbi_aqyc_tbswr_gettempstatus(self,inputData):
        uid=inputData("uid")
        statCode=inputData('statcode')
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        if result.exists():
            for line in result:
                devCode=line.dev_code
                socket_id=line.socket_id
                resp={'status':"true",'socketId':socket_id,'devCode':devCode}
        else:
            resp={'status':'false'}
        return resp

    def dft_dbi_hcu_lock_compel_open(self,inputData):
        sessionid=inputData['sessionid']
        statCode=inputData['statcode']
        uid=""
        user=""
        result=dct_t_l3f1sym_user_login_session.objects.filter(session_id=sessionid)
        if result.exists():
            for line in result:
                uid=line.uid_id
                user=line.uid.login_name
        else:
            return False
        key_type=self.__MFUN_L3APL_F2CM_KEY_TYPE_USER
        resp=dct_t_l3f2cm_virtual_key_fhys.objects.filter(hwcode=uid,keytype=key_type)
        if resp.exists():
            for line in resp:
                keyid=line.keyid
        else:
            result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
            if result.exists():
                for line in result:
                    pcode=line.prj_code
            else:
                return False
            keyid="KEY"+self.__dft_getRandomUid(6)
            keystatus="Y"
            keyname="用户名钥匙["+user+"]"
            keytype=self.__MFUN_L3APL_F2CM_KEY_TYPE_USER
            hwcode=uid
            memo="系统自动创建的用户名虚拟钥匙"
            dct_t_l3f2cm_virtual_key_fhys.objects.create(keyid=keyid,keyname=keyname,prj_code=pcode,ownerid=uid,ownername=user,keystatus=keystatus,keytype=keytype,hwcode=hwcode,memo=memo)
        authlevel=self.__MFUN_L3APL_F2CM_AUTH_LEVEL_DEVICE
        authtype=self.__MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER
        validnum=1
        result=dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid,authobj=statCode,authtype=authtype)
        if result.exists():
            validnum=result[0].validnum+1
            dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid,authobj=statCode,authtype=authtype).update(validnum=validnum)
        else:
            dct_t_l3f2cm_key_auth_fhys.objects.create(keyid_id=keyid,authlevel=authlevel,authobj=statCode,authtype=authtype,validnum=validnum)
        return True










