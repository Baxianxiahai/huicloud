from django.shortcuts import render
from DappDbF12iwdp.models import *
import time
import datetime
import random
import json


# Create your views here.

class dct_classDbiL3apF12Iwdp:

    def create_task_id(self):
        """具体标志为T+年+月+日+时+分+1000以内的随机数"""
        now = datetime.datetime.now()
        code = "T" + str(now.year).zfill(4) + str(now.month).zfill(2) + str(now.day).zfill(2) + str(now.hour).zfill(
            2) + str(now.minute).zfill(2) + str(random.randint(0, 999)).zfill(3)
        resp = dct_t_l3f12iwdp_task.objects.filter(taskid=code)
        if resp.exists():
            self.create_task_id()
        else:
            return code
        # return code

    def dft_dbi_insert_employee_view(self, inputData):
        uid = inputData['uid']
        uname = inputData['uname']
        uavatar = inputData['avatar']
        uemail = inputData['email']
        telephone = inputData['tel']
        companyid = inputData['companyid']
        companyname = inputData['companyname']
        departmentid = inputData['departmentid']
        departmentname = inputData['departmentname']
        resp_employee = dct_t_l3f12iwdp_user.objects.filter(uid=uid)
        if resp_employee.exists():
            resp_employee.update(uname=uname, uavatar=uavatar, uemail=uemail, utelephone=telephone,
                                 ucompanyid=companyid,
                                 ucompanyname=companyname, udepartmentid=departmentid,
                                 udepartmentname=departmentname)
        else:
            dct_t_l3f12iwdp_user.objects.create(uid=uid, uname=uname, uavatar=uavatar, uemail=uemail,
                                                utelephone=telephone,
                                                ucompanyid=companyid,
                                                ucompanyname=companyname, udepartmentid=departmentid,
                                                udepartmentname=departmentname)

    def dft_dbi_employee_integral_setting_view(self, inputData):
        uid = inputData['uid']
        outtime = inputData['outtime']
        unfinish = inputData['unfinish']
        finish = inputData['finish']
        refuse = inputData['refuse']
        accept = inputData['accept']
        resp = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=uid)
        if (resp.exists()):
            dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=uid).update(outtime=outtime, unfinish=unfinish,
                                                                               finish=finish, refuse=refuse,
                                                                               accept=accept)
        else:
            dct_t_l3f12iwdp_integral_setting.objects.create(uid_id=uid, outtime=outtime, unfinish=unfinish,
                                                            finish=finish, refuse=refuse, accept=accept)

    def dft_dbi_employee_intergral_get_view(self, inputData):
        uid = inputData['uid']
        #         result={}
        resp = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=uid)
        if (resp.exists()):
            outtime = resp[0].outtime
            unfinish = resp[0].unfinish
            finish = resp[0].finish
            refuse = resp[0].refuse
            accept = resp[0].accept
            result = {"outtime": outtime, "unfinish": unfinish, "finish": finish, "refuse": refuse, "accept": accept,
                      "errcode": '0'}
        else:
            result = {"errcode": "2", "errmsg": "暂无数据"}
        return result

    def dft_dbi_get_employee_user_info_view(self, inputData):
        uid = inputData["uid"]
        resp = dct_t_l3f12iwdp_user.objects.filter(uid=uid)
        if resp.exists():
            name = resp[0].uname
            uemail = resp[0].uemail
            uavatar = resp[0].uavatar
            utelephone = resp[0].utelephone
            ucompanyid = resp[0].ucompanyid
            ucompanyname = resp[0].ucompanyname
            udepartmentid = resp[0].udepartmentid
            udepartmentname = resp[0].udepartmentname
            ulevel = resp[0].ulevel
            result = {"errcode": '0', 'errmsg': '查询成功', 'uid': uid, 'name': name,
                      'email': uemail, 'avatar': uavatar, 'telephone': utelephone,
                      'companyid': ucompanyid, 'companyname': ucompanyname, 'departmentid':
                          udepartmentid, 'departmentname': udepartmentname, 'level': ulevel}
        else:
            result = {'errcode': '2', 'errmsg': '查询失败'}
        return result

    def dft_dbi_get_company_jsapi_ticket_view(self, inputData):
        corpid = inputData['corpid']
        resp = dct_t_l3f12iwdp_company_jsapi_ticket.objects.filter(cordid=corpid)
        if resp.exists():
            last_time = time.mktime(resp[0].last_time.timetuple())
            if (time.time() - last_time >= 60 * 60 * 1.8):
                result = {'errcode': "3", 'errmsg': "信息过期"}
            else:
                jsticket = resp[0].jsticket
                errcode = "0"
                errmsg = '信息正确'
                result = {'errcode': errcode, 'errmsg': errmsg, 'time': last_time, 'ticket': jsticket}
        else:
            errcode = "2"
            errmsg = '找不到数据'
            result = {'errcode': errcode, 'errmsg': errmsg}
        return result

    def dft_dbi_set_company_jsapi_ticket_view(self, inputData):
        corpid = inputData['corpid']
        ticket = inputData['ticket']
        resp = dct_t_l3f12iwdp_company_jsapi_ticket.objects.filter(cordid=corpid)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        errcode = "0"
        errmsg = '信息正确'
        if (resp.exists()):
            resp.update(jsticket=ticket, last_time=now_time)
        else:
            dct_t_l3f12iwdp_company_jsapi_ticket.objects.create(cordid=corpid, jsticket=ticket, last_time=now_time)
        result = {'errcode': errcode, 'errmsg': errmsg, 'time': time.time(), 'ticket': ticket}
        return result

    def dft_dbi_employee_release_or_save_task_view(self, inputData, save):
        taskId = inputData['taskid']
        title = inputData['title']
        describe = inputData['describe']
        level = inputData['level']
        start = inputData['start'] + ":00"
        end = inputData['end'] + ":00"
        remind = inputData['remind']
        charge = inputData['charge']
        CC = inputData['CC']
        submission = inputData['submission']
        superior = inputData['superior']
        finance = inputData['finance']
        releaser = inputData['releaser']
        enclosure=json.dumps(inputData["enclosure"],ensure_ascii=False)
        task_list = list()
        if (remind == "1"):
            remindTime = None
        elif (remind == "2"):
            remindTime = end
        elif (remind == "3"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(minutes=5))
        elif (remind == "4"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(minutes=15))
        elif (remind == "5"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(minutes=30))
        elif (remind == "6"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(minutes=60))
        elif (remind == "7"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days=1))
        elif (remind == "8"):
            remindTime = str(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days=3))
        else:
            remindTime = None
        if taskId != "":
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskId).delete()
        task_id = self.create_task_id()
        if (save):
            dct_t_l3f12iwdp_task.objects.create(taskid=task_id, taskname=title, taskdescribe=describe, tasklevel=level,
                                                taskstart=start, taskend=end, taskremind=remindTime, taskstate=1,taskenclosure=enclosure)
        else:
            dct_t_l3f12iwdp_task.objects.create(taskid=task_id, taskname=title, taskdescribe=describe, tasklevel=level,
                                                taskstart=start, taskend=end, taskremind=remindTime, taskstate=2,taskenclosure=enclosure)
        for i in range(len(releaser)):
            task_list.append(
                dct_t_l3f12iwdp_user_task(uid_id=releaser[i], taskid_id=task_id, user_type=1, show=True, read=True))
        if save:
            for i in range(len(charge)):
                task_list.append(dct_t_l3f12iwdp_user_task(uid_id=charge[i], taskid_id=task_id, user_type=2))
            for i in range(len(CC)):
                task_list.append(dct_t_l3f12iwdp_user_task(uid_id=CC[i], taskid_id=task_id, user_type=3))
        else:
            for i in range(len(charge)):
                task_list.append(dct_t_l3f12iwdp_user_task(uid_id=charge[i], taskid_id=task_id, user_type=2, show=True))
            for i in range(len(CC)):
                task_list.append(dct_t_l3f12iwdp_user_task(uid_id=CC[i], taskid_id=task_id, user_type=3, show=True))
        for i in range(len(submission)):
            task_list.append(dct_t_l3f12iwdp_user_task(uid_id=submission[i], taskid_id=task_id, user_type=4))
        for i in range(len(superior)):
            task_list.append(dct_t_l3f12iwdp_user_task(uid_id=superior[i], taskid_id=task_id, user_type=5))
        for i in range(len(finance)):
            task_list.append(dct_t_l3f12iwdp_user_task(uid_id=finance[i], taskid_id=task_id, user_type=6))
        dct_t_l3f12iwdp_user_task.objects.bulk_create(task_list)
        result = {"errcode": "0", 'errmsg': '插入成功'}
        return result

    def dft_dbi_get_task_detail_view(self, inputData):
        taskid = inputData['taskid']
        userid = inputData['userid']
        resp = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid)
        accept = 0
        if (resp.exists()):
            title = resp[0].taskid.taskname
            describe = resp[0].taskid.taskdescribe
            level = resp[0].taskid.tasklevel
            start = resp[0].taskid.taskstart
            end = resp[0].taskid.taskend
            remindtime = resp[0].taskid.taskremind
            state = resp[0].taskid.taskstate
            review = resp[0].taskid.taskreview
            enclosure=json.loads(resp[0].taskid.taskenclosure,encoding='utf8')
            if state == 2:
                resp_accept = resp.filter(uid_id=userid, user_type=2)
                if resp_accept.exists():
                    accept = resp_accept[0].taskaccept
            chargeID = []
            chargeName = []
            CCID = []
            CCName = []
            submissionID = []
            submissionName = []
            superiorID = []
            superiorName = []
            financeID = []
            financeName = []
            releaserID = []
            releaserName = []
            if remindtime == None:
                remind = 1
            elif ((end - remindtime).seconds == 0):
                remind = 2
            elif ((end - remindtime).seconds == 5 * 60):
                remind = 3
            elif ((end - remindtime).seconds == 15 * 60):
                remind = 4
            elif ((end - remindtime).seconds == 30 * 60):
                remind = 5
            elif ((end - remindtime).seconds == 60 * 60):
                remind = 6
            elif ((end - remindtime).seconds == 1 * 24 * 60 * 60):
                remind = 7
            elif ((end - remindtime).seconds == 3 * 24 * 60 * 60):
                remind = 8
            else:
                remind = 1
            for line in resp:
                if line.user_type == 1:
                    releaserID.append(line.uid_id)
                    releaserName.append(line.uid.uname)
                if line.user_type == 2:
                    chargeID.append(line.uid_id)
                    chargeName.append(line.uid.uname)
                if line.user_type == 3:
                    CCID.append(line.uid_id)
                    CCName.append(line.uid.uname)
                if line.user_type == 4:
                    submissionID.append(line.uid_id)
                    submissionName.append(line.uid.uname)
                if line.user_type == 5:
                    superiorID.append(line.uid_id)
                    superiorName.append(line.uid.uname)
                if line.user_type == 6:
                    financeID.append(line.uid_id)
                    financeName.append(line.uid.uname)
            task_detail = {'title': title, 'describe': describe, 'level': level, 'start': str(start), 'end': str(end),
                           'remind': remind,
                           "releaseID": releaserID, "releaseName": releaserName, 'chargeID': chargeID,
                           'chargeName': chargeName,
                           'CCID': CCID, 'CCName': CCName, 'submissionID': submissionID,
                           'submissionName': submissionName,
                           'superiorID': superiorID, 'superiorName': superiorName, 'financeID': financeID,
                           'financeName': financeName,
                           'state': state, 'review': review, 'accept': accept,'enclosure':enclosure}
            result = {'errcode': "0", 'errmsg': '查找成功', 'detail': task_detail}
        else:
            result = {'errcode': "2", 'errmsg': '暂无数据'}
        return result

    def dft_dbi_employee_delete_task_view(self, inputData):
        taskid = inputData['taskid']
        resp = dct_t_l3f12iwdp_task.objects.filter(taskid=taskid)
        if resp.exists():
            resp.delete()
            result = {'errcode': '0', 'errmsg': '删除成功'}
        else:
            result = {'errcode': '3', 'errmsg': '任务未找到'}
        return result

    def dft_dbi_employee_task_click_view(self, inputData):
        taskid = inputData['taskid']
        userid = inputData['userid']
        kind = inputData['kind']
        resp = dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid)
        if resp.exists():
            state = resp[0].taskid.taskstate
            review = resp[0].taskid.taskreview
            if kind == 1:
                pass
            elif kind == 2:
                if state == 2 or state == 3 :
                    dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=2).update(
                        read=True)
                elif state==4:
                    dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=4).update(
                        read=True)
                # elif state == 5 or state == 6 or state == 7:
                #     dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=4).update(
                #         read=True)
            elif kind == 3:
                dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=4).update(
                    read=True)
                if review == 1:
                    dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=5).update(
                        read=True)
                elif review == 2:
                    dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=6).update(
                        read=True)
                # if state==6:
                #     dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=5).update(
                #         read=True)
            else:
                dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=3).update(read=True)
            result = {'errcode': "0", 'errmsg': '已读'}
        else:
            result = {'errcode': "3", 'errmsg': '数据查找失败'}
        return result

    def dft_dbi_employee_accept_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=2)
        if resp_result.exists():
            resp_integral = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)
            if resp_integral.exists():
                release_id = resp_integral[0].uid_id
                integral = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=release_id)[0].accept
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            resp_employee = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2, uid_id=uid)
            if resp_employee.exists():
                employee_integral = resp_employee[0].integral
                total_integral = employee_integral + integral
                resp_employee.update(integral=total_integral, taskaccept=True)
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            resp = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2)
            if resp.exists():
                accept = False
                for line in resp:
                    if line.taskaccept == 1:
                        accept = True
                    else:
                        accept = False
                        break
                    # else:
                    #     continue
                if (accept):
                    dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=4)
                    dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=4).update(show=True)
                    resp_sub = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=4)
                    if resp_sub.exists():
                        resp_update = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2,
                                                                               uid_id=resp_sub[0].uid_id)
                        if resp_update.exists():
                            resp_update.update(show=False)
                result = {'errcode': '0', 'errmsg': '操作成功'}
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_employee_refuse_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=2)
        if resp_result.exists():
            resp_integral = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)
            if resp_integral.exists():
                release_id = resp_integral[0].uid_id
                integral = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=release_id)[0].accept
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            resp_employee = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2, uid_id=uid)
            if resp_employee.exists():
                employee_integral = resp_employee[0].integral
                total_integral = employee_integral - integral
                resp_employee.update(integral=total_integral, taskaccept=False)
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=3)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_employee_success_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=4)
        if resp_result.exists():
            if dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=5).exists():
                resp_result.update(show=False)
            resp_task = dct_t_l3f12iwdp_task.objects.filter(taskid=taskid)[0].taskend
            if (resp_task > datetime.datetime.now()):
                outTime = False
                dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=5, taskreview=1,
                                                                          taskendtime=datetime.datetime.now())
            else:
                outTime = True
                dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=7, taskreview=1,
                                                                          taskendtime=datetime.datetime.now())
            resp_integral = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)
            if resp_integral.exists():
                release_id = resp_integral[0].uid_id
                if (outTime):
                    integral = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=release_id)[0].outtime
                else:
                    integral = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=release_id)[0].finish
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            resp_employee = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2)
            if resp_employee.exists():
                for line in resp_employee:
                    employee_integral = line.integral
                    userid = line.uid_id
                    total_integral = employee_integral + integral
                    dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, user_type=2, taskid_id=taskid).update(
                        integral=total_integral)
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=5).update(show=True)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_employee_fail_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=4)
        if resp_result.exists():
            if dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=5).exists():
                resp_result.update(show=False)
            resp_integral = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)
            if resp_integral.exists():
                release_id = resp_integral[0].uid_id
                integral = dct_t_l3f12iwdp_integral_setting.objects.filter(uid_id=release_id)[0].unfinish
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            resp_employee = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2)
            if resp_employee.exists():
                for line in resp_employee:
                    employee_integral = line.integral
                    total_integral = employee_integral - integral
                    uid = line.uid_id
                    dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2, uid_id=uid).update(integral=total_integral)
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=6,taskreview=1)
            dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=5).update(show=True)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_superior_adopt_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=5)
        if resp_result.exists():
            if dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=6).exists():
                resp_result.update(show=False)
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskreview=2)
            dct_t_l3f12iwdp_user_task.objects.filter(taskid=taskid, uid_id=uid, user_type=6).update(show=True)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_superior_refuse_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=5)
        if resp_result.exists():
            resp_result.update(show=False,read=False)
            resp_task = dct_t_l3f12iwdp_task.objects.filter(taskid=taskid)
            if resp_task.exists():
                state = resp_task[0].taskstate
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            if state == 5:
                resp_integral = dct_t_l3f12iwdp_integral_setting.objects.filter(
                    uid_id=dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)[0].uid_id)[0].finish
            elif state == 6:
                resp_integral = -1 * (dct_t_l3f12iwdp_integral_setting.objects.filter(
                    uid_id=dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)[0].uid_id)[
                                          0].unfinish)
            elif state == 7:
                resp_integral = dct_t_l3f12iwdp_integral_setting.objects.filter(
                    uid_id=dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=1)[0].uid_id)[0].outtime
            else:
                result = {'errcode': '4', 'errmsg': '状态未知'}
                return result
            resp_charge = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2)
            if resp_charge.exists():
                for line in resp_charge:
                    total_integral = line.integral - resp_integral
                    userid = line.uid_id
                    dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, user_type=2, uid_id=userid).update(
                        integral=total_integral)
            else:
                result = {'errcode': '3', 'errmsg': '信息查找失败'}
                return result
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskstate=4, taskreview=0)
            dct_t_l3f12iwdp_user_task.objects.filter(taskid=taskid, uid_id=uid, user_type=5).update(show=False)
            dct_t_l3f12iwdp_user_task.objects.filter(taskid=taskid, user_type=4).update(read=False,show=True)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_finance_adopt_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=6)
        if resp_result.exists():
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskreview=3)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_finance_refuse_task_view(self, inputData):
        taskid = inputData['taskid']
        uid = inputData['userid']
        resp_result = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=uid, user_type=6)
        if resp_result.exists():
            resp_result.update(show=False,read=False)
            dct_t_l3f12iwdp_user_task.objects.filter(taskid=taskid, user_type=5).update(read=False, show=True)
            dct_t_l3f12iwdp_task.objects.filter(taskid=taskid).update(taskreview=1)
            result = {'errcode': '0', 'errmsg': '操作成功'}
        else:
            result = {'errcode': '3', 'errmsg': '信息查找失败'}
        return result

    def dft_dbi_get_employee_all_task_list_view(self, inputData):
        uid = inputData['uid']
        resp = dct_t_l3f12iwdp_user_task.objects.filter(uid_id=uid, show=True)
        task_list = []
        # task_array = []
        if resp.exists():
            for line in resp:
                if line.user_type == 1:
                    kind = 1
                elif line.user_type == 3:
                    kind = 4
                else:
                    if (line.taskid.taskstate == 2 or line.taskid.taskstate == 3 or line.taskid.taskstate == 4):
                        kind = 2
                    elif (line.taskid.taskstate == 5 or line.taskid.taskstate == 6 or line.taskid.taskstate == 7):
                        kind = 3
                    else:
                        kind = 1
                title = line.taskid.taskname
                state = line.taskid.taskstate
                review = line.taskid.taskreview
                taskid = line.taskid_id
                read = line.read
                user_type = line.user_type
                task = {'title': title, 'state': state, 'review': review, 'taskid': taskid, 'kind': kind,
                        'read': read, 'user_type': user_type}
                task_list.append(task)
            result = {'errcode': '0', 'errmsg': '查找成功', 'task': task_list}
        else:
            result = {'errcode': '0', 'errmsg': '暂无数据', 'task': task_list}
        return result

    def dft_dbi_employee_search_task_view(self, inputData):
        task = inputData['key']
        userid = inputData['userid']
        resp = dct_t_l3f12iwdp_task.objects.filter(taskname__icontains=task)
        task_list = []
        if resp.exists():
            for line in resp:
                taskid = line.taskid
                resp_user = dct_t_l3f12iwdp_user_task.objects.filter(taskid_id=taskid, uid_id=userid, show=True)
                if resp_user.exists():
                    for line in resp_user:
                        if line.user_type == 1:
                            kind = 1
                        elif line.user_type == 3:
                            kind = 4
                        else:
                            if (line.taskid.taskstate == 2 or line.taskid.taskstate == 3 or line.taskid.taskstate == 4):
                                kind = 2
                            elif (
                                    line.taskid.taskstate == 5 or line.taskid.taskstate == 6 or line.taskid.taskstate == 7):
                                kind = 3
                            else:
                                kind = 1
                        title = line.taskid.taskname
                        state = line.taskid.taskstate
                        review = line.taskid.taskreview
                        taskid = line.taskid_id
                        read = line.read
                        user_type = line.user_type
                        task = {'title': title, 'state': state, 'review': review, 'taskid': taskid, 'kind': kind,
                                'read': read, 'user_type': user_type}
                        task_list.append(task)
            result = {'errcode': '0', 'errmsg': '查找成功', 'task': task_list}
        else:
            result = {'errcode': '2', 'errmsg': '暂无数据', 'task': task_list}
        return result

    def dft_dbi_get_employee_integral_all_view(self, inputData):
        userid = inputData['uid']
        now_day = datetime.datetime.now()
        now_year = now_day.year
        now_mounth = now_day.month
        now_day = 1
        if now_mounth == 12:
            last_year = now_year + 1
            last_mounth = 1
        else:
            last_year = now_year
            last_mounth = now_mounth + 1
        total_integral = 0
        first_time = str(now_year) + "-" + str(now_mounth) + "-" + str(now_day)
        last_time = str(last_year) + "-" + str(last_mounth) + "-" + str(now_day)
        resp = dct_t_l3f12iwdp_task.objects.filter(dct_t_l3f12iwdp_user_task__uid_id=userid,
                                                   dct_t_l3f12iwdp_user_task__user_type=2,
                                                   taskendtime__gte=first_time, taskendtime__lt=last_time)
        for line in resp:
            taskid = line.taskid
            resp_task = dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=2)
            for line in resp_task:
                total_integral = total_integral + line.integral
        result = {'errcode': '0', 'errmsg': '查询成功', 'integral': total_integral}
        return result

    def dft_dbi_get_employee_integral_day_view(self, inputData):
        userid = inputData['uid']
        now_date = datetime.datetime.now()
        now_year = now_date.year
        now_mounth = now_date.month
        now_day = 1
        day_array = []
        name = ""
        integral_array = []
        resp_name=dct_t_l3f12iwdp_user.objects.filter(uid=userid)
        if(resp_name.exists()):
            name=resp_name[0].uname
        if now_mounth == 12:
            last_year = now_year + 1
            last_mounth = 1
        else:
            last_year = now_year
            last_mounth = now_mounth + 1
        first_time = str(now_year) + "-" + str(now_mounth) + "-" + str(now_day)
        last_time = str(last_year) + "-" + str(last_mounth) + "-" + str(now_day)
        d1 = datetime.datetime.strptime(last_time, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(first_time, '%Y-%m-%d')
        delta = d1 - d2
        for i in range(delta.days + 1):
            date_time = d2 + datetime.timedelta(days=i)
            if (date_time <= now_date + datetime.timedelta(days=1)):
                day_array.append(date_time)
                integral_array.append(0)
        resp = dct_t_l3f12iwdp_task.objects.filter(dct_t_l3f12iwdp_user_task__uid_id=userid,
                                                   dct_t_l3f12iwdp_user_task__user_type=2,
                                                   taskendtime__gte=first_time, taskendtime__lt=last_time)
        if resp.exists():
            for line in resp:
                taskid = line.taskid
                task_time = line.taskendtime
                resp_task = dct_t_l3f12iwdp_user_task.objects.filter(uid_id=userid, taskid_id=taskid, user_type=2)
                integral = resp_task[0].integral
                # name = resp_task[0].uid.uname
                for j in range(len(day_array) - 1):
                    if (task_time >= day_array[j] and task_time < day_array[j + 1]):
                        integral_array[j] = integral_array[j] + integral
            result = {'errcode': '0', 'errmsg': '查询成功', 'day': [str(i) for i in day_array], 'integral': integral_array,
                      'name': name, 'mounth': now_mounth}
        else:
            result = {'errcode': '0', 'errmsg': '数据无法查询', 'day': [str(i) for i in day_array],
                      'integral': integral_array,'name': name, 'mounth': now_mounth}
        return result

    def dft_dbi_employee_publish_comment_view(self, inputData):
        taskid = inputData['taskid']
        text = inputData['text']
        userid = inputData['userid']
        resp_task = dct_t_l3f12iwdp_task.objects.filter(taskid=taskid)
        resp_user=dct_t_l3f12iwdp_user.objects.filter(uid=userid)
        # time_now=datetime.datetime.now()
        if resp_task.exists():
            if resp_user.exists():
                name=resp_user[0].uname
                comment=json.loads(resp_task[0].comment,encoding='utf8')
                comment_new={'name':name,'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'text': text}
                comment.append(comment_new)
                resp_task.update(comment=json.dumps(comment, ensure_ascii=False))
                result = {'errcode': '0', 'errmsg': '查找成功'}
            else:
                result = {'errcode': '2', 'errmsg': '查找失败'}
        else:
            result = {'errcode': '2', 'errmsg': '查找失败'}
        return result

    def dft_dbi_employee_get_comments_view(self,inputData):
        taskid = inputData['taskid']
        resp_task=dct_t_l3f12iwdp_task.objects.filter(taskid=taskid)
        comment=[]
        if resp_task.exists():
            comment=resp_task[0].comment
            result={'errcode':'0','errmsg':'查找成功','comment':json.loads(comment,encoding='utf8')}
        else:
            result = {'errcode': '2', 'errmsg': '查找失败', 'comment': comment}
        return result

