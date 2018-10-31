from django.shortcuts import render
import json
from DappDbF6pm.models import *
from DappDbF1sym.models import *
from DappDbF2cm.models import *
from DappDbF3dm.models import *
from DappDbInsertData.DappDbMsgDefine import *
import datetime
# Create your views here.

class dct_classDbiL3apF6pm:
    def __dft_dbi_user_statproj_inquery(self,inputData):
        uid=inputData
        p_list=[]
        pg_list=[]
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                temp=line.auth_code
                temp_type=line.auth_type
                if temp_type==1:
                    pg_list.append(temp)
                elif temp_type==2:
                    p_list.append(temp)
        for pg_info in pg_list:
            result=dct_t_l3f2cm_project_common.objects.filter(pg_code_id=pg_info)
            if result.exists():
                for line in result:
                    temp=line.prj_code
                    p_list.append(temp)
        auth_list=[]
        for prj_info in p_list:
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=prj_info)
            if result.exists():
                for line in result:
                    temp={'stat_code':line.site_code,"p_code":prj_info}
                    auth_list.append(temp)
        if len(auth_list)==0:
            return auth_list
        unique_auth_list=[]
        for auth_info in auth_list:
            if auth_info not in unique_auth_list:
                unique_auth_list.append(auth_info)
        return unique_auth_list

    def dft_dbi_aqyc_performance_table_req(self,inputData):
        uid=inputData['uid']
        column=[]
        data=[]
        auth_list=self.__dft_dbi_user_statproj_inquery(uid)
        column.append("设备编号")
        column.append("监测点编号")
        column.append("监测点名称")
        column.append("地址")
        column.append("报告时间")
#         column.append("VM错误")
#         column.append("Socket断开统计")
        column.append("CPU占用")
        column.append("内存占用")
        column.append("硬盘占用")
        column.append("CPU温度")
        column.append("告警计数")
        column.append("服务器重连")
        column.append("连续工作时长(min)")
        for anth_info in auth_list:
            statcode=anth_info['stat_code']
            result=dct_t_l3f6pm_perfdata.objects.filter(site_code_id=statcode)
            if result.exists():
                for line in result:
                    temp=[]
                    statName=line.site_code.site_name
                    address=line.site_code.address
                    devcode=line.dev_code_id
                    createtime=str(line.createtime)
                    workContmins=line.workcontmins
                    alarmCnt=line.alarmcnt
                    discHomeCnt=line.dischomecnt
#                     networkDiscCnt=line.networkdisccnt
#                     socketDiscCnt=line.socketdisccnt
                    cpuOccupy=str(line.cpuoccupy)+"%"
                    memOccupy=str(line.memoccupy)+"%"
                    diskOccupy=str(line.diskoccupy)+"%"
                    cpuTemp=str(line.cputemp)+"℃"
                    temp.append(devcode)
                    temp.append(statcode)
                    temp.append(statName)
                    temp.append(address)
                    temp.append(createtime)
#                     temp.append(networkDiscCnt)
#                     temp.append(socketDiscCnt)
                    temp.append(cpuOccupy)
                    temp.append(memOccupy)
                    temp.append(diskOccupy)
                    temp.append(cpuTemp)
                    data.append(temp)             
                    temp.append(alarmCnt)
                    temp.append(discHomeCnt)
                    temp.append(workContmins)
        resp={'column':column,'data':data}
        return resp

class Accept_Msg_From_HCU_Report():
    def dft_dbi_HCU_Performance_Report(self,socketId,InputData):
        ServerName = InputData["ToUsr"]
        IeCnt = InputData['IeCnt']
        dev_Code = InputData['FrUsr']
        if 'restartCnt' in IeCnt.keys():restartCnt = IeCnt['restartCnt']
        else:restartCnt=0
        if 'networkConnCnt' in IeCnt.keys():networkConnCnt = IeCnt['networkConnCnt']
        else:networkConnCnt=0
        if 'networkConnFailCnt' in IeCnt.keys():networkConnFailCnt = IeCnt['networkConnFailCnt']
        else:networkConnFailCnt=0
        if 'networkDiscCnt' in IeCnt.keys():networkDiscCnt = IeCnt['networkDiscCnt']
        else:networkDiscCnt=0
        if 'socketDiscCnt' in IeCnt.keys():socketDiscCnt = IeCnt['socketDiscCnt']
        else:socketDiscCnt=0
        if 'cpuTemp' in IeCnt.keys():cpuTemp = IeCnt['cpuTemp']
        else:cpuTemp=0
        if 'cpuOccupy' in IeCnt.keys():cpuOccupy = IeCnt['cpuOccupy']
        else:cpuOccupy=0
        if 'memOccupy' in IeCnt.keys():memOccupy = IeCnt['memOccupy']
        else:memOccupy=0
        if 'diskOccupy' in IeCnt.keys():diskOccupy = IeCnt['diskOccupy']
        else:diskOccupy=0
        if 'alarmCnt' in IeCnt.keys():alarmCnt = IeCnt['alarmCnt']
        else:alarmCnt=0
        if 'discHomeCnt' in IeCnt.keys():discHomeCnt = IeCnt['discHomeCnt']
        else:discHomeCnt=0
        if 'contWorkMins' in IeCnt.keys():contWorkMins = IeCnt['contWorkMins']
        else:contWorkMins=0
        if 'vmErrCnt' in IeCnt.keys():vmErrCnt = IeCnt['vmErrCnt']
        else:vmErrCnt=0
        if 'timeStamp' in IeCnt.keys():timeStamp = IeCnt['timeStamp']
        else:timeStamp=0
        date=datetime.datetime.now()
        #restartCnt=IeCnt['restartCnt']
#         networkConnCnt=IeCnt['networkConnCnt']
#         networkConnFailCnt=IeCnt['networkConnFailCnt']
#         networkDiscCnt=IeCnt['networkDiscCnt']
#         socketDiscCnt=IeCnt['socketDiscCnt']
#         cpuTemp=IeCnt['cpuTemp']
#         cpuOccupy=IeCnt['cpuOccupy']
#         memOccupy=IeCnt['memOccupy']
#         diskOccupy=IeCnt['diskOccupy']
#         alarmCnt=IeCnt['alarmCnt']
#         discHomeCnt=IeCnt['discHomeCnt']
#         contWorkMins=IeCnt['contWorkMins']
#         vmErrCnt=IeCnt['vmErrCnt']
#         timeStamp=IeCnt['timeStamp']
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_Code)
        if result.exists():
            resp = dct_t_l3f6pm_perfdata.objects.filter(dev_code_id=dev_Code)
            if resp.exists():
                resp.update(createtime=date,site_code_id=result[0].site_code_id, restartcnt=restartCnt, networkconncnt=networkConnCnt,
                            networkconnfailcnt=networkConnFailCnt, networkdisccnt=networkDiscCnt,
                            socketdisccnt=socketDiscCnt,
                            cpuoccupy=cpuOccupy, memoccupy=memOccupy, diskoccupy=diskOccupy, cputemp=cpuTemp,
                            workcontmins=contWorkMins,
                            alarmcnt=alarmCnt, dischomecnt=discHomeCnt, vmerrcnt=vmErrCnt)
            else:
                dct_t_l3f6pm_perfdata.objects.create(dev_code_id=dev_Code, site_code_id=result[0].site_code_id,
                                                     restartcnt=restartCnt, networkconncnt=networkConnCnt,
                                                     networkconnfailcnt=networkConnFailCnt,
                                                     networkdisccnt=networkDiscCnt, socketdisccnt=socketDiscCnt,
                                                     cpuoccupy=cpuOccupy, memoccupy=memOccupy, diskoccupy=diskOccupy,
                                                     cputemp=cpuTemp, workcontmins=contWorkMins,
                                                     alarmcnt=alarmCnt, dischomecnt=discHomeCnt, vmerrcnt=vmErrCnt)

            Msg_final = {'socketid': socketId,
                     'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                              'MsgId': GOLBALVAR.HUITPJSON_MSGID_PERFORMANCE_CONFIRM, 'MsgLn': 115, "IeCnt": {'cfmYesOrNo': 1}, "FnFlg": 0}}
        else:
            Msg_final = {'socketid': socketId,
                     'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                              'MsgId': GOLBALVAR.HUITPJSON_MSGID_PERFORMANCE_CONFIRM, 'MsgLn': 115, "IeCnt": {'cfmYesOrNo': 0}, "FnFlg": 0}}
        return Msg_final



