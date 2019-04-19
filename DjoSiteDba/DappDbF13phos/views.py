from django.shortcuts import render

# Create your views here.
from DappDbF13phos.models import *
import random
import datetime
from django.db.models import Q
import time


class dct_classDbiL3apF13Phos:
    def __init__(self):
        pass

    def _dft_dbi_create_ID(self):
        ID = random.randint(0, 9999999)
        IDValue = str(ID).zfill(7)
        return IDValue

    def _dft_dbi_create_task_code(self):
        ID = random.randint(0, 999)
        IDValue = str(ID).zfill(3)
        return IDValue

    # 用户登录时检查用户的openid进行匹配
    def dft_dbi_check_openid_view(self, inputData):
        openid = inputData['openid']
        result = dct_t_l3f13phos_app_user_info.objects.filter(openid=openid)
        status = "false"
        if result.exists():
            status = "true"
            uid = result[0].uid
            utype = result[0].user_type
            ustatus = result[0].driver_status
            infostatus = result[0].info_status
            resp = {'status': status, 'uid': uid, 'utype': utype, 'ustatus': ustatus, 'istatus': infostatus}
        else:
            resp = {'status': status, 'message': "用户尚未注册", 'openid': openid}
        return resp

    # 用户使用手机号进行初始注册
    def dft_dbi_user_telphone_register_view(self, inputData):
        openid = inputData['openid']
        telphone = inputData['telphone']
        utype = inputData['utype']
        longitude = inputData['longitude']
        latitude = inputData['latitude']
        uid = "UID" + self._dft_dbi_create_ID()
        regitime = datetime.datetime.now()
        result_uid = dct_t_l3f13phos_app_user_info.objects.filter(uid=uid)
        if result_uid.exists():
            self.dft_dbi_user_telphone_register_view(inputData)
        else:
            dct_t_l3f13phos_app_user_info.objects.create(uid=uid, openid=openid, utelephone=telphone,
                                                         user_type=utype, longitude=longitude, latitude=latitude,
                                                         regitime=regitime)
        resp = {"status": 'true', 'uid': uid, 'utype': utype}
        return resp

    # 获取本用户下的所属公司以及非所属公司
    def dft_dbi_get_coampany_list_view(self, inputData):
        userid = inputData['userid']
        choise = ['个体司机', '集体司机']
        isself = []
        allCom = []
        result_com = dct_t_l3f13phos_company_info.objects.all()
        if result_com.exists():
            for line_com in result_com:
                allCom.append(line_com.com_name)
        result_uid = dct_t_l3f13phos_user_company.objects.filter(uid_id=userid)
        if result_uid.exists():
            for line_uid in result_uid:
                isself.append(line_uid.com_code.com_name)
        notCom = [val for val in allCom if val not in isself]
        notself = [notCom, choise]
        resp = {"status": 'true', 'uid': userid, 'self': isself, 'notself': notself}
        return resp

    def dft_dbi_upload_user_location_view(self, inputData):
        uid = inputData['userid']
        longitude = inputData['longitude']
        latitude = inputData['latitude']
        ustatus = inputData['userStatus']
        result_task = dct_t_l3f13phos_task.objects.filter(driver_id=uid, task_status=2)
        if result_task.exists():
            uid = result_task[0].driver_id
            ustatus = result_task[0].driver.driver_status
            dct_t_l3f13phos_route.objects.create(uid_id=uid, taskcode_id=result_task[0].task_code,
                                                 reporttime=datetime.datetime.now(), longitude=longitude,
                                                 latitude=latitude)
        else:
            result_info = dct_t_l3f13phos_app_user_info.objects.filter(uid=uid)
            if result_info.exists():
                ustatus = result_info[0].driver_status
                dct_t_l3f13phos_app_user_info.objects.filter(uid=uid, info_status=True).update(
                    regitime=datetime.datetime.now(), longitude=longitude, latitude=latitude)
        resp = {'status': 'true', 'userid': uid, 'userStatus': ustatus}
        return resp

    def dft_dbi_driver_information_submit_view(self, inputData):
        uid = inputData['uid']
        driverTypeValue = inputData['driverTypeValue']
        headstock = inputData['headstock']
        trailer = inputData['trailer']
        license = inputData['license']
        operation = inputData['operation']
        name = inputData['name']
        company = inputData['company']
        iDcard = inputData['iDcard']
        headstockSrc = inputData['headstockSrc']
        trailerSrc = inputData['trailerSrc']
        licenseSrc = inputData['licenseSrc']
        operationSrc = inputData['operationSrc']
        idPositive = inputData['idPositive']
        idOtherSide = inputData['idOtherSide']
        result_info = dct_t_l3f13phos_app_user_info.objects.filter(uid=uid)
        if result_info.exists():
            result_info.update(uname=name, idnumber=iDcard, user_type=1, driver_code=license,
                               driver_status=3, id_positive=idPositive, id_side=idOtherSide,
                               drive_img=licenseSrc, trans_img=operationSrc, trans_code=operation,
                               driver_type=driverTypeValue, info_status=True)
            if driverTypeValue != 0:
                result_com = dct_t_l3f13phos_company_info.objects.filter(com_name=company)
                if result_com.exists():
                    com_code = result_com[0].com_code
                    dct_t_l3f13phos_user_company.objects.create(uid_id=uid, com_code_id=com_code)
            dct_t_l3f13phos_user_car.objects.create(uid_id=uid, car_type=1, car_img=headstockSrc, car_plate=headstock)
            dct_t_l3f13phos_user_car.objects.create(uid_id=uid, car_type=2, car_img=trailerSrc, car_plate=trailer)
            resp = {'status': 'true'}
        else:
            resp = {'status': 'false'}
        return resp

    def dft_dbi_get_task_list_view(self, inputData):
        userid = inputData['userid']
        startTime = inputData['start']
        endTime = inputData['end']
        result_task = dct_t_l3f13phos_task.objects.filter(driver_id=userid, task_status=3, arrive_time__gte=startTime,
                                                          arrive_time__lte=endTime)
        task_list = []
        if result_task.exists():
            for line in result_task:
                task_id = line.task_code
                start = line.scity
                end = line.ecity
                goods_name = line.goods_type.goods_name
                arrive_time = str(line.arrive_time)
                task = {"taskId": task_id, "start": start, "end": end, "type": goods_name, "date": arrive_time}
                task_list.append(task)
        resp = {"status": 'true', 'taskList': task_list}
        return resp

    def dft_dbi_get_user_accept_task_info_view(self, inputData):
        uid = inputData['uid']
        result = dct_t_l3f13phos_task.objects.filter(driver_id=uid, task_status=1)
        if result.exists():
            wayBillId = result[0].task_code
            manageid = result[0].manage_id
            driver = result[0].driver.uname
            result_company = dct_t_l3f13phos_user_company.objects.filter(uid_id=manageid)
            if result_company.exists():
                company_name = result_company[0].com_code.com_name
            else:
                company_name = ""
            dtype = result[0].driver.driver_type
            wayBill = []
            detail = {"key": '运输货品', "value": result[0].goods_type.goods_name}
            wayBill.append(detail)
            detail = {"key": '装货时间', "value": str(result[0].start_date.date())}
            wayBill.append(detail)
            detail = {"key": '装货地点',
                      "value": result[0].sprovince + result[0].scity + result[0].scounty + result[0].saddress}
            wayBill.append(detail)
            detail = {"key": '卸货地点',
                      "value": result[0].eprovince + result[0].ecity + result[0].ecounty + result[0].eaddress}
            wayBill.append(detail)
            detail = {"key": '装货户头', "value": result[0].load_account.account_name}
            wayBill.append(detail)
            detail = {"key": '卸货户头', "value": result[0].unload_account.account_name}
            wayBill.append(detail)
            detail = {"key": '预装吨位', "value": str(result[0].weight - 3) + "-" + str(result[0].weight + 3)}
            wayBill.append(detail)
            detail = {"key": '单价(元/吨)', "value": result[0].price}
            wayBill.append(detail)
            resp = {"status": 'true', 'wayBillId': wayBillId, 'wayBill': wayBill, 'company': company_name,
                    'driver': driver, 'dtype': dtype}
            return resp

    def dft_dbi_get_contract_information_view(self, inputData):
        taskid = inputData['taskid']
        result_company = dct_t_l3f13phos_task.objects.filter(task_code=taskid)
        if result_company.exists():
            com_code_id = result_company[0].com_code_id
            com_name = result_company[0].com_code.com_name
            driver = result_company[0].driver.uname
            price = result_company[0].price
            type = result_company[0].goods_type.goods_name
            result_con = dct_t_l3f13phos_contract.objects.filter(com_code_id=com_code_id)
            if result_con.exists():
                text_1 = result_con[0].txt_1
                text_2 = result_con[0].txt_2
                text_3 = result_con[0].txt_3
                resp = {"status": "true", "text_1": text_1, "text_2": text_2, "text_3": text_3, "price": price,
                        "type": type, "company": com_name, "driver": driver, }
            else:
                resp = {"status": "false", 'msg': '合同信息获取失败'}
        else:
            resp = {"status": "false", 'msg': '合同信息获取失败'}
        return resp

    def dft_dbi_user_refuse_task_view(self, inputData):
        taskid = inputData['taskid']
        result_task = dct_t_l3f13phos_task.objects.filter(task_code=taskid)
        if result_task.exists():
            driver_id = result_task[0].driver_id
            result_task.update(task_status=4)
            result_user = dct_t_l3f13phos_app_user_info.objects.filter(uid=driver_id)
            if result_user.exists():
                result_user.update(driver_status=3)
                ustatus = 3
                resp = {"status": 'true', 'taskid': taskid, 'ustatus': ustatus}
            else:
                ustatus = result_task[0].driver.driver_status
                resp = {"status": 'false', 'taskid': taskid, 'ustatus': ustatus}
        else:
            resp = {"status": 'false', "msg": '信息获取失败'}
        return resp

    def dft_dbi_user_accept_task_view(self, inputData):
        uid = inputData['uid']
        taskid = inputData['taskid']
        dct_t_l3f13phos_task.objects.filter(task_code=taskid).update(task_status=2)
        dct_t_l3f13phos_app_user_info.objects.filter(uid=uid).update(driver_status=2)
        resp = {"status": 'true', "ustatus": 2}
        return resp

    def dft_dbi_get_user_accepted_task_info_view(self, inputData):
        userid = inputData['userid']
        result_task = dct_t_l3f13phos_task.objects.filter(driver_id=userid, task_status=2)
        if result_task.exists():
            wayBillId = result_task[0].task_code
            company = result_task[0].com_code.com_name
            driver = result_task[0].driver.uname
            wayBill = []
            if (result_task[0].price != None):
                detail = {"key": "运输货品", "value": result_task[0].goods_type.goods_name}
                wayBill.append(detail)
            detail = {"key": "装货时间", "value": str(result_task[0].start_date.date())}
            wayBill.append(detail)
            detail = {"key": "装货地点",
                      "value": result_task[0].sprovince + result_task[0].scity + result_task[0].scounty + result_task[
                          0].saddress}
            wayBill.append(detail)
            detail = {"key": "卸货地点",
                      "value": result_task[0].eprovince + result_task[0].ecity + result_task[0].ecounty + result_task[
                          0].eaddress}
            wayBill.append(detail)
            detail = {"key": "装货户头", "value": result_task[0].load_account.account_name}
            wayBill.append(detail)
            detail = {"key": "卸货户头", "value": result_task[0].unload_account.account_name}
            wayBill.append(detail)
            detail = {"key": "预装吨位", "value": str(result_task[0].weight - 3) + "-" + str(result_task[0].weight + 3)}
            wayBill.append(detail)
            if (result_task[0].price != None):
                detail = {"key": "单价(元/吨)", "value": result_task[0].price}
                wayBill.append(detail)
            else:
                detail = {"key": "单价(元/吨)", "value": 0}
                wayBill.append(detail)
            if (result_task[0].contcode != None):
                detail = {"key": "合同信息", "value": result_task[0].contcode.contname}
                wayBill.append(detail)
            if (result_task[0].load_img != None):
                picLoadSrc = result_task[0].load_img
            else:
                picLoadSrc = ""
            if (result_task[0].unload_img != None):
                picUnloadSrc = result_task[0].unload_img
            else:
                picUnloadSrc = ""
            if (result_task[0].lpound != None):
                loadPound = result_task[0].lpound
            else:
                loadPound = 0
            if (result_task[0].upound != None):
                unloadPound = result_task[0].upound
            else:
                unloadPound = 0
            if (result_task[0].load_date != None):
                loadDate = str(result_task[0].load_date.date())
            else:
                loadDate = ""
            if (result_task[0].unload_date != None):
                unloadDate = str(result_task[0].unload_date.date())
            else:
                unloadDate = ""
            result_video = dct_t_l3f13phos_video.objects.filter(task_code_id=wayBillId)
            oldLoadVideoFilePath = []
            oldUnloadVideoFilePath = []
            length = 0
            if result_video.exists():
                length = len(result_video)
                for line in result_video:
                    if line.vtype == 1:
                        key = line.sid
                        loadName = line.vname
                        loadSrc = line.vpath
                        detail = {'key': key, 'name': loadName, 'src': loadSrc}
                        oldLoadVideoFilePath.append(detail)
                    else:
                        key = line.sid
                        unloadName = line.vname
                        unloadSrc = line.vpath
                        detail = {'key': key, 'name': unloadName, 'src': unloadSrc}
                        oldUnloadVideoFilePath.append(detail)
            resp = {
                "status": 'true', 'wayBillId': wayBillId, 'userid': userid, 'wayBillAccept': wayBill
                , 'oldLoadVideoFilePath': oldLoadVideoFilePath, 'oldUnloadVideoFilePath': oldUnloadVideoFilePath
                , 'picLoadSrc': picLoadSrc, 'picUnloadSrc': picUnloadSrc, 'loadPound': loadPound
                , 'loadDate': loadDate, 'unloadPound': unloadPound, 'unloadDate': unloadDate
                , 'company': company, 'driver': driver, 'length': length
            }
        else:
            resp = {'status': 'false', 'msg': '信息获取失败'}
        return resp

    def dft_dbi_upload_picture_infomation_view(self, inputData):
        type = inputData['type']
        taskid = inputData['taskid']
        picSrc = inputData['picSrc']
        picPound = inputData['picPound']
        picDate = inputData['picDate']
        longitude = inputData['longitude']
        latitude = inputData['latitude']
        if type == 'load':
            dct_t_l3f13phos_task.objects.filter(task_code=taskid).update(load_img=picSrc, load_date=picDate,
                                                                         lpound=picPound, longitude=longitude,
                                                                         latitude=latitude)
            resp = {"status": 'true', 'msg': '信息上传成功'}
        else:
            dct_t_l3f13phos_task.objects.filter(task_code=taskid).update(unload_img=picSrc, unload_date=picDate,
                                                                         upound=picPound, ulongitude=longitude,
                                                                         ulatitude=latitude)
            resp = {"status": 'true', 'msg': '信息上传成功'}
        return resp

    def dft_dbi_upload_video_view(self, inputData):
        type = inputData['type']
        taskid = inputData['taskid']
        videoSrc = inputData['videoSrc']
        longitude = inputData['longitude']
        latitude = inputData['latitude']
        if type == 'load':
            video_length = len(dct_t_l3f13phos_video.objects.filter(task_code_id=taskid, vtype=1))
            vname = "装货视频" + str(video_length + 1)
            dct_t_l3f13phos_video.objects.create(task_code_id=taskid, vtime=datetime.datetime.now(), vtype=1,
                                                 vname=vname, vpath=videoSrc, longitude=longitude, latitude=latitude)
            resp = {"status": 'true', 'msg': '视频上传成功'}
        else:
            video_length = len(dct_t_l3f13phos_video.objects.filter(task_code_id=taskid, vtype=2))
            vname = "卸货视频" + str(video_length + 1)
            dct_t_l3f13phos_video.objects.create(task_code_id=taskid, vtime=datetime.datetime.now(), vtype=2,
                                                 vname=vname, vpath=videoSrc, longitude=longitude, latitude=latitude)
            resp = {"status": 'true', 'msg': '视频上传成功'}
        return resp

    def dft_dbi_get_video_list_view(self, inputData):
        taskid = inputData['taskid']
        loadVideo = []
        unloadVideo = []
        result_video = dct_t_l3f13phos_video.objects.filter(task_code_id=taskid)
        length = len(result_video)
        if result_video.exists():
            for line in result_video:
                if line.vtype == 1:
                    key = line.sid
                    Name = line.vname
                    Src = line.vpath
                    detail = {'key': key, 'name': Name, 'src': Src}
                    loadVideo.append(detail)
                else:
                    key = line.sid
                    Name = line.vname
                    Src = line.vpath
                    detail = {'key': key, 'name': Name, 'src': Src}
                    unloadVideo.append(detail)
        resp = {"status": 'true', 'taskid': taskid, 'load': loadVideo, 'unload': unloadVideo, 'length': length}
        return resp

    def dft_dbi_video_delete_view(self, inputData):
        taskid = inputData['taskid']
        type = inputData['type']
        src = inputData['src']
        if type == "load":
            type = 1
        else:
            type = 2
        dct_t_l3f13phos_video.objects.filter(task_code_id=taskid, vtype=type, vpath=src).delete()
        resp = {"status": 'true', 'msg': "视频文件删除成功"}
        return resp

    def dft_dbi_task_done_view(self, inputData):
        taskid = inputData['taskid']
        result_task = dct_t_l3f13phos_task.objects.filter(task_code=taskid)
        if result_task.exists():
            result_task.update(arrive_time=datetime.datetime.now(), task_status=3)
            userid = result_task[0].driver_id
            com_code = result_task[0].com_code_id
            price = result_task[0].price
            upound = result_task[0].upound
            dct_t_l3f13phos_app_user_info.objects.filter(uid=userid).update(driver_status=3)
            ustatus = result_task[0].driver.driver_status
            now_date = datetime.datetime.now().date()
            result_driver_day = dct_t_l3f13phos_user_data_day.objects.filter(uid_id=userid, data_day=now_date)
            result_com_day = dct_t_l3f13phos_company_data_day.objects.filter(com_code_id=com_code, data_day=now_date)
            result_user_mounth = dct_t_l3f13phos_user_data_mounth.objects.filter(uid_id=userid,
                                                                                 mounth_start__lte=now_date,
                                                                                 mounth_end__gte=now_date)
            result_com_mounth = dct_t_l3f13phos_company_data_mounth.objects.filter(com_code_id=com_code,
                                                                                   mounth_start__lte=now_date,
                                                                                   mounth_end__gte=now_date)
            now_income = price * upound
            if result_driver_day.exists():
                history_pound = result_driver_day[0].pound
                history_income = result_driver_day[0].price
                new_pound = history_pound + upound
                new_income = history_income + now_income
                result_driver_day.update(pound=new_pound, price=new_income)
            else:
                dct_t_l3f13phos_user_data_day.objects.create(uid_id=userid, data_day=now_date, pound=upound,
                                                             price=now_income)
            if result_com_day.exists():
                history_pound = result_com_day[0].pound
                new_pound = history_pound + upound
                result_com_day.update(pound=new_pound)
            else:
                dct_t_l3f13phos_company_data_day.objects.create(com_code_id=com_code, data_day=now_date, pound=upound)
            if result_user_mounth.exists():
                history_pound = result_user_mounth[0].pound
                history_income = result_user_mounth[0].price
                new_pound = history_pound + upound
                new_income = history_income + now_income
                result_user_mounth.update(pound=new_pound, price=new_income)
            else:
                first = datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
                last = datetime.date(datetime.date.today().year, datetime.date.today().month + 1,
                                     1) - datetime.timedelta(1)
                dct_t_l3f13phos_user_data_mounth.objects.create(uid_id=userid, pound=upound, price=now_income,
                                                                mounth_start=first, mounth_end=last)

            if result_com_mounth.exists():
                history_pound = result_com_mounth[0].pound
                new_pound = history_pound + upound
                result_com_mounth.update(pound=new_pound)
            else:
                first = datetime.date(datetime.date.today().year, datetime.date.today().month, 1)
                last = datetime.date(datetime.date.today().year, datetime.date.today().month + 1,
                                     1) - datetime.timedelta(1)
                dct_t_l3f13phos_company_data_mounth.objects.create(com_code_id=com_code, pound=upound,
                                                                   mounth_start=first, mounth_end=last)
            resp = {"status": 'true', 'msg': "任务已完成", 'ustatus': ustatus}
        else:
            resp = {"status": 'true', 'msg': "任务查找失败，请重试"}
        return resp

    def dft_dbi_get_task_detail_view(self, inputData):
        taskid = inputData['taskid']
        result_task = dct_t_l3f13phos_task.objects.filter(task_code=taskid)
        if result_task.exists():
            if result_task[0].com_code != None:
                company = result_task[0].com_code.com_name
            else:
                company = ""
            if result_task[0].driver != None:
                driver = result_task[0].driver.uname
            else:
                driver = ""
            wayBill = []
            if result_task[0].goods_type != None:
                detail = {"key": "运输货品", 'value': result_task[0].goods_type.goods_name}
                wayBill.append(detail)
            if result_task[0].load_date != None:
                detail = {"key": "装货时间", 'value': str(result_task[0].load_date.date())}
                wayBill.append(detail)
            detail = {"key": "装货地点",
                      'value': result_task[0].sprovince + result_task[0].scity + result_task[0].scounty + result_task[
                          0].saddress}
            wayBill.append(detail)
            detail = {"key": "卸货地点",
                      'value': result_task[0].eprovince + result_task[0].ecity + result_task[0].ecounty + result_task[
                          0].eaddress}
            wayBill.append(detail)
            if result_task[0].load_account != None:
                detail = {"key": "装货户头", 'value': result_task[0].load_account.account_name}
                wayBill.append(detail)
            if result_task[0].goods_type != None:
                detail = {"key": "卸货户头", 'value': result_task[0].unload_account.account_name}
                wayBill.append(detail)
            if result_task[0].price != None:
                detail = {"key": "单价(元/吨)", 'value': result_task[0].price}
                wayBill.append(detail)
            if result_task[0].contcode != None:
                detail = {"key": "合同信息", 'value': result_task[0].contcode.contname}
                wayBill.append(detail)
            result_task.update(arrive_time=datetime.datetime.now(), task_status=3)
            # userid = result_task[0].driver_id
            # dct_t_l3f13phos_app_user_info.objects.filter(uid=userid).update(driver_status=3)
            # ustatus = result_task[0].driver.driver_status
            oldLoadVideoFilePath = []
            oldUnloadVideoFilePath = []
            if result_task[0].load_img != None:
                picLoadSrc = result_task[0].load_img
            else:
                picLoadSrc = ""
            if result_task[0].unload_img != None:
                picUnloadSrc = result_task[0].unload_img
            else:
                picUnloadSrc = ""
            if result_task[0].lpound != None:
                load_pound = result_task[0].lpound
            else:
                load_pound = 0
            if result_task[0].upound != None:
                unload_pound = result_task[0].upound
            else:
                unload_pound = 0
            if result_task[0].load_date != None:
                load_date = str(result_task[0].load_date)
            else:
                load_date = ""
            if result_task[0].unload_date != None:
                unload_date = str(result_task[0].load_date)
            else:
                unload_date = ""
            result_video = dct_t_l3f13phos_video.objects.filter(task_code_id=taskid)
            if result_video.exists():
                for line in result_video:
                    detail = {'key': line.sid, 'name': line.vname, 'src': line.vpath}
                    if line.vtype == 1:
                        oldLoadVideoFilePath.append(detail)
                    else:
                        oldUnloadVideoFilePath.append(detail)
            resp = {
                "status": 'true', 'wayBillId': taskid
                , 'wayBillAccept': wayBill
                , 'oldLoadVideoFilePath': oldLoadVideoFilePath
                , 'oldUnloadVideoFilePath': oldUnloadVideoFilePath
                , 'picLoadSrc': picLoadSrc
                , 'picUnloadSrc': picUnloadSrc
                , 'loadPound': load_pound
                , 'loadDate': load_date
                , 'unloadPound': unload_pound
                , 'unloadDate': unload_date
                , 'company': company
                , 'driver': driver, 'msg': '任务查找成功'
            }
        else:
            resp = {"status": 'false', 'msg': "任务查找失败，请重试"}
        return resp

    def dft_dbi_get_user_information_view(self, inputData):
        userid = inputData['userid']
        now_data = datetime.date.today()
        year_start = str(datetime.date.today().year) + "-01-01"
        year_end = str(datetime.date.today().year) + "-12-31"
        result_user_info=dct_t_l3f13phos_app_user_info.objects.filter(uid=userid)
        year_pound = 0
        year_income = 0
        mounth_pound = 0
        mounth_income = 0
        if result_user_info.exists():
            result_user = dct_t_l3f13phos_user_data_mounth.objects.filter(uid_id=userid, mounth_start__gte=year_start,
                                                                          mounth_end__lte=year_end)
            
            for line in result_user:
                year_pound = year_pound + line.pound
                year_income = year_income + line.price
            result_mounth = result_user.filter(mounth_start__lte=now_data, mounth_end__gte=now_data)
            if result_mounth.exists():
                mounth_pound = result_mounth[0].pound
                mounth_income = result_mounth[0].price
            uname = result_user_info[0].uname
            utelphone = result_user_info[0].utelephone
            resp = {"status": 'true', 'uname': uname, 'utelphone': utelphone, 'mPound': mounth_pound,
                    'mWages': mounth_income, 'yPound': year_pound, 'yWages': year_income,
                    'msg': '个人信息获取成功'}
        else:
            resp = {"status": 'false', 'msg': "个人信息获取失败，请重试"}
        return resp

    def dft_dbi_get_car_list_view(self,inputData):
        userid = inputData['userid']
        result_user=dct_t_l3f13phos_user_car.objects.filter(uid_id=userid)
        length=0
        head=[]
        trailer=[]
        if result_user.exists():
            length=len(result_user)
            for line in result_user:
                if line.car_type==1:
                    head.append(line.car_plate)
                else:
                    trailer.append(line.car_plate)
            resp={'status':'true','head':head,'trailer':trailer,'length':length,'msg':'车辆信息获取成功'}
        else:
            resp = {'status': 'false', 'head': head, 'trailer': trailer, 'length': length,'msg':'请刷新界面'}
        return resp

    def dft_dbi_binding_license_plate_view(self,inputData):
        uid = inputData['uid']
        plate = inputData['plate']
        car_type = inputData['type']
        filePath = inputData['filePath']
        if car_type=='head':
            car_type=1
            result=dct_t_l3f13phos_user_car.objects.filter(uid_id=uid,car_plate=plate)
            if result.exists():
                resp={"status":'false',"msg":"该车辆已存在与您名下"}
            else:
                dct_t_l3f13phos_user_car.objects.create(uid_id=uid,car_type=car_type,car_img=filePath,car_plate=plate)
                resp = {"status": 'true', "msg": "车辆添加成功"}
        else:
            car_type=2
            result = dct_t_l3f13phos_user_car.objects.filter(uid_id=uid, car_plate=plate)
            if result.exists():
                resp = {"status": 'false', "msg": "该车辆已存在与您名下"}
            else:
                dct_t_l3f13phos_user_car.objects.create(uid_id=uid, car_type=car_type, car_img=filePath, car_plate=plate)
                resp = {"status": 'true', "msg": "车辆添加成功"}
        return resp

    def dft_dbi_manage_information_submit_view(self,inputData):
        uid = inputData['uid']
        name = inputData['name']
        company = inputData['company']
        iDcard = inputData['iDcard']
        idPositive = inputData['idPositive']
        idOtherSide = inputData['idOtherSide']
        result_user=dct_t_l3f13phos_app_user_info.objects.filter(uid=uid)
        result_comp=dct_t_l3f13phos_company_info.objects.filter(com_name=company)
        if result_user.exists():
            if result_comp.exists():
                com_code=result_comp[0].com_code
                result_user.update(uname=name,idnumber=iDcard,user_type=2,id_positive=idPositive,id_side=idOtherSide,info_status=True)
                dct_t_l3f13phos_user_company.objects.create(uid_id=uid,com_code_id=com_code)
                resp={'status':'true','msg':'管理人员注册成功'}
            else:
                resp = {'status': 'false', 'msg': '公司选择错误'}
        else:
            resp = {'status': 'false', 'msg': '非合法用户'}
        return resp

    def dft_dbi_get_free_plate_list_view(self,inputData):
        uid = inputData['uid']
        result_company=dct_t_l3f13phos_user_company.objects.filter(uid_id=uid)
        plateList=[]
        if result_company.exists():
            com_code = result_company[0].com_code_id
            # for line in result_company:
            result_company_driver=dct_t_l3f13phos_user_company.objects.filter(Q(com_code_id=com_code),~Q(uid_id=uid))
            for line_com in result_company_driver:
                if line_com.uid.user_type==1 and line_com.uid.info_status==True and line_com.uid.driver_status==3:
                    driver_id=line_com.uid_id
                    result_palte=dct_t_l3f13phos_user_car.objects.filter(uid_id=driver_id,car_type=1)
                    for line_plate in result_palte:
                        plateList.append(line_plate.car_plate)
            result_driver=dct_t_l3f13phos_app_user_info.objects.filter(user_type=1,driver_type=0,driver_status=3,info_status=True)
            for line in result_driver:
                driver_id = line.uid
                result_palte = dct_t_l3f13phos_user_car.objects.filter(uid_id=driver_id, car_type=1)
                for line in result_palte:
                    plateList.append(line.car_plate)
            resp = {'status':"true",'com_code':com_code,'list':plateList,"msg":"空闲车辆信息获取成功"}
            return resp
        else:
            resp = {'status': "false", "msg":'管理员未绑定公司'}
            return resp

    def dft_dbi_get_goods_list_view(self,inputData):
        uid=inputData['uid']
        result_goods=dct_t_l3f13phos_goods_info.objects.all()
        goodsList=[]
        goodsIndex=[]
        for line in result_goods:
            goodsList.append(line.goods_name)
            goodsIndex.append(line.sid)
        resp = {'status':"true",'uid':uid, 'list':goodsList,'index':goodsIndex}
        return resp

    def dft_dbi_get_account_list_view(self,inputData):
        uid = inputData['uid']
        result_account = dct_t_l3f13phos_account_info.objects.all()
        accountList = []
        accountIndex = []
        for line in result_account:
            accountList.append(line.account_name)
            accountIndex.append(line.sid)
        resp = {'status': "true", 'uid': uid, 'list': accountList,'index':accountIndex}
        return resp

    def dft_dbi_manage_release_task_view(self,inputData):
        uid = inputData['uid']
        plate = inputData['plate']
        comCode = inputData['comCode']
        startDate = inputData['startDate']
        goods = inputData['goods']
        start = inputData['start']
        end = inputData['end']
        startDetail = inputData['startDetail']
        endDetail = inputData['endDetail']
        loadAccount = inputData['loadAccount']
        unloadAccount = inputData['unloadAccount']
        pound = inputData['pound']
        price = inputData['price']
        taskid="TID"+str(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))+self._dft_dbi_create_task_code()
        result_task=dct_t_l3f13phos_task.objects.filter(task_code=taskid)
        if result_task.exists():
            self.dft_dbi_manage_release_task_view(inputData)
        else:
            result_plate=dct_t_l3f13phos_user_car.objects.filter(car_plate=plate)
            if result_plate.exists():
                driver_id=result_plate[0].uid_id
                if result_plate[0].uid.driver_type==0:
                    result_contract=dct_t_l3f13phos_contract.objects.filter(com_code_id=comCode)
                    if result_contract.exists():
                        contract=result_contract[0].sid
                    else:
                        contract=None
                else:
                    contract=None
            else:
                resp={"status":'false','msg':'车辆选择出错'}
                return resp
            dct_t_l3f13phos_task.objects.create(task_code=taskid,driver_id=driver_id,manage_id=uid,
                                                com_code_id=comCode,start_date=startDate,sprovince=start[0],
                                                scity=start[1],scounty=start[2],saddress=startDetail,
                                                eprovince=end[0],ecity=end[1],ecounty=end[2],eaddress=endDetail,
                                                load_account_id=loadAccount,unload_account_id=unloadAccount,
                                                task_status=1,contcode_id=contract,weight=pound,price=price,
                                                goods_type_id=goods)
            dct_t_l3f13phos_app_user_info.objects.filter(uid=driver_id).update(driver_status=1)
            resp = {"status": 'true', 'msg': '任务发布成功'}
            return resp
    def dft_dbi_get_refuse_task_list_view(self,inputData):
        uid=inputData['uid']
        taskList=[]
        result_task=dct_t_l3f13phos_task.objects.filter(manage_id=uid,task_status=4)
        for line in result_task:
            task=[]
            detail={"key":'运输货物',"value":line.goods_type.goods_name}
            task.append(detail)
            detail={"key":'发运时间',"value":str(line.start_date.date())}
            task.append(detail)
            detail={"key":'装货地点',"value":line.sprovince+line.scity+line.scounty+line.saddress}
            task.append(detail)
            detail={"key":'卸货地点',"value":line.eprovince+line.ecity+line.ecounty+line.eaddress}
            task.append(detail)
            detail={"key":'装货户头',"value":line.load_account.account_name}
            task.append(detail)
            detail={"key":'卸货户头',"value":line.unload_account.account_name}
            task.append(detail)
            detail={"key":'预装吨位',"value":line.weight}
            task.append(detail)
            detail={"key":'单价(元/吨)',"value":line.price}
            task.append(detail)
            task_info={'taskid':line.task_code,'detail':task}
            taskList.append(task_info)
        resp = {'status': "true",'uid':uid, 'refuseList' :taskList,'msg':'查找已拒绝任务列表成功'}
        return resp

    def dft_dbi_delete_task_info_view(self,inputData):
        uid = inputData['uid']
        taskid = inputData['taskid']
        dct_t_l3f13phos_task.objects.filter(manage_id=uid,task_code=taskid).delete()
        resp={"status":"true","msg":'任务删除成功'}
        return resp

    def dft_dbi_task_reselection_view(self,inputData):
        uid = inputData['uid']
        taskid = inputData['taskid']
        plate = inputData['plate']
        result_palte=dct_t_l3f13phos_user_car.objects.filter(car_plate=plate)
        if result_palte.exists():
            if result_palte[0].uid.user_type==1 and result_palte[0].uid.driver_status == 3:
                driver_id=result_palte[0].uid_id
                result_task=dct_t_l3f13phos_task.objects.filter(task_code=taskid,manage_id=uid)
                if result_task.exists():
                    com_code=result_task[0].com_code_id
                    result_com=dct_t_l3f13phos_user_company.objects.filter(com_code_id=com_code,uid_id=driver_id)
                    if result_com.exists():
                        result_task.update(driver_id=driver_id,task_status=1)
                        dct_t_l3f13phos_app_user_info.objects.filter(uid=driver_id).update(driver_status=1)
                        resp = {"status": 'true', "msg": "任务发布成功"}
                        return resp
                    else:
                        result_cont=dct_t_l3f13phos_contract.objects.filter(com_code_id=com_code)
                        if result_cont.exists():
                            cont_code=result_cont[0].sid
                            result_task.update(driver_id=driver_id,contcode_id=cont_code,task_status=1)
                            dct_t_l3f13phos_app_user_info.objects.filter(uid=driver_id).update(driver_status=1)
                            resp = {"status": 'true', "msg": "任务发布成功"}
                            return resp
                        else:
                            resp={"status":'false',"msg":"本公司下无合同信息"}
                            return resp
                else:
                    resp = {"status": 'false', "msg": "任务不存在，请重新进入本页面"}
                    return resp
            else:
                resp = {"status": 'false', "msg": "车主已有其他任务"}
                return resp
        else:
            resp = {"status": 'false', "msg": "车辆状态异常"}
            return resp



