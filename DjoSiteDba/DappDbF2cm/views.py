from django.shortcuts import render
import random
import os
import datetime
from DappDbF2cm.models import *
from DappDbF1sym.models import *
from DappDbF3dm.models import *
from django.db.models import Q
from DappDbF10oam.models import *
from DappDbF11faam.models import *
import json
from DappDbInsertData.DappDbMsgDefine import *
import pycurl,io


# Create your views here.
class dct_classDbiL3apF2cm:
    __MFUN_L3APL_F2CM_AUTH_TYPE_TIME = "T"
    __MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER = "N"
    __MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER = "F"
    __MFUN_L3APL_F2CM_KEY_TYPE_RFID = 'R'
    __MFUN_L3APL_F2CM_KEY_TYPE_BLE = 'B'
    __MFUN_L3APL_F2CM_KEY_TYPE_USER = 'U'
    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT = 'W'
    __MFUN_L3APL_F2CM_KEY_TYPE_IDCARD = 'I'
    __MFUN_L3APL_F2CM_KEY_TYPE_PHONE = 'P'
    __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED = 'N'

    __MFUN_HCU_FHYS_KEY_VALID = "Y"
    __MFUN_HCU_FHYS_KEY_INVALID = "N"

    __HCU_DUST = True
    __HCU_TEMP = True
    __HCU_HUMID = True
    __HCU_NOISE = True
    __HCU_WINDSPD = True
    __HCU_WINDDIR = True
    __HCU_NO2 = True

    __MFUN_HCU_AQYC_INSTALL_PICTURE = "/var/www/html/avorion/upload/"
    __MFUN_HCU_AQYC_INSTALL_PICTURE2 = "/avorion/upload/"

    def __dft_getRandomDigID(self, strlen):
        str_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        uid = ''.join(random.sample(str_array, strlen))
        return uid

    def __dft_dbi_get_user_auth_project(self, inputData):
        uid = inputData
        projlist = []
        result = dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        for line in result:
            auth_code = line.auth_code
            fromat = int(line.auth_type)
            if fromat == 2:
                pcode = auth_code
                result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                for line in result:
                    temp = {'id': line.prj_code, 'name': line.prj_name}
                    projlist.append(temp)
            elif fromat == 1:
                pcode = auth_code
                temp = self.dft_dbi_pg_projlist_req(pcode)
                for i in range(len(temp)):
                    projlist.append(temp[i])
        if len(projlist) == 0:
            return projlist
        projlist_1 = []
        for i in range(len(projlist)):
            if projlist[i] not in projlist_1:
                projlist_1.append(projlist[i])
        return projlist_1

    def __dft_dbi_get_user_auth_projgroup(self, inputData):
        projectlist = self.__dft_dbi_get_user_auth_project(inputData)
        print(projectlist)
        pg_list = []
        for i in range(len(projectlist)):
            pcode = projectlist[i]['id']
            result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
            if result.exists():
                for line in result:
                    if line.pg_code_id != None:
                        temp = {'id': line.pg_code.pg_code, 'name': line.pg_code.pg_name}
                        if temp not in pg_list:
                            pg_list.append(temp)
        return pg_list

    def __dft_dbi_get_user_auth_site(self, inputData):
        projectlist = self.__dft_dbi_get_user_auth_project(inputData)
        site_list = []
        for i in range(len(projectlist)):
            pcode = projectlist[i]['id']
            result = dct_t_l3f2cm_site_common.objects.filter(prj_code_id=pcode)
            for line in result:
                temp = {'id': line.site_code, 'name': line.site_name, 'projcode': line.prj_code_id}
                site_list.append(temp)
        return site_list

    def __dft_dbi_get_user_name(self, inputData):
        uid = inputData
        result = dct_t_l3f1sym_account_secondary.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                name = line.true_name
        else:
            name = uid
        if name == "":
            name = uid
        return name

    def __dft_dbi_winddir_convert(self, inputData):
        degree = inputData
        if (degree >= 337.5 and degree < 360) or degree < 22.5:
            winddir = '北风'
        elif (degree >= 22.5 and degree < 67.5):
            winddir = '东北风'
        elif (degree >= 67.5 and degree < 112.5):
            winddir = '东风'
        elif (degree >= 112.5 and degree < 157.5):
            winddir = '东南风'
        elif (degree >= 157.5 and degree < 202.5):
            winddir = '南风'
        elif (degree >= 202.5 and degree < 247.5):
            winddir = '西南风'
        elif (degree >= 247.5 and degree < 292.5):
            winddir = '西风'
        elif (degree >= 292.5 and degree < 337.5):
            winddir = '西北风'
        else:
            winddir = '未知'
        return winddir

    def __dft_dbi_get_tower_info(self, inputData):
        result = dct_t_l3f2cm_site_fstt.objects.filter(site_code=inputData)
        tower_info = ""
        if result.exists():
            for line in result:
                tower_info = line
        return tower_info

    def __dft_dbi_print_export_usertable(self, inputData):
        column = []
        data = []
        column.append('用户ID')
        column.append('用户名')
        column.append('昵称')
        column.append('电话')
        column.append('邮箱')
        column.append('属性')
        column.append('更新日期')
        column.append('备注')

        self_grade = 0
        result = dct_t_l3f1sym_account_secondary.objects.filter(uid_id=inputData)
        if result.exists():
            for line in result:
                self_grade = int(line.uid.grade_level)
                if self_grade == 0:
                    grade_name = '管理员'
                elif self_grade == 1:
                    grade_name = '高级用户'
                elif self_grade == 2:
                    grade_name = '一级用户'
                elif self_grade == 3:
                    grade_name = '二级用户'
                elif self_grade == 4:
                    grade_name = '三级用户'
                else:
                    grade_name = '用户等级未知'
                temp = []
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.reg_date))
                temp.append(line.uid.backup)
                data.append(temp)
        result = dct_t_l3f1sym_account_secondary.objects.filter(uid__grade_level__gt=self_grade)
        if result.exists():
            for line in result:
                user = line.uid.login_name
                grade = int(line.uid.grade_level)
                if grade == 0:
                    grade_name = '管理员'
                elif grade == 1:
                    grade_name = '高级用户'
                elif grade == 2:
                    grade_name = '一级用户'
                elif grade == 3:
                    grade_name = '二级用户'
                elif grade == 4:
                    grade_name = '三级用户'
                else:
                    grade_name = '用户等级未知'
                temp = []
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.reg_date))
                temp.append(line.uid.backup)
                data.append(temp)
        if user == 'admin':
            data = []
            result = dct_t_l3f1sym_account_secondary.objects.all()
            for line in result:
                grade = int(line.uid.grade_level)
                if grade == 0:
                    grade_name = '管理员'
                elif grade == 1:
                    grade_name = '高级用户'
                elif grade == 2:
                    grade_name = '一级用户'
                elif grade == 3:
                    grade_name = '二级用户'
                elif grade == 4:
                    grade_name = '三级用户'
                else:
                    grade_name = '用户等级未知'
                temp = []
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.reg_date))
                temp.append(line.uid.backup)
                data.append(temp)
        user_table = {"data": data, 'column': column}
        return user_table

    def __dft_dbi_print_export_pgtable(self, inputData):
        column = []
        data = []
        column.append('项目组编号')
        column.append('项目组名称')
        column.append('责任人')
        column.append('电话')
        column.append('所属单位')
        column.append('地址')
        column.append('备注')
        pglist = self.__dft_dbi_get_user_auth_projgroup(inputData)
        for i in range(len(pglist)):
            pgcode = pglist[i]['id']
            result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
            for line in result:
                temp = []
                temp.append("PG_" + str(line.pg_code))
                temp.append(line.pg_name)
                temp.append(line.superintendent)
                temp.append(line.telephone)
                temp.append(line.department)
                temp.append(line.address)
                temp.append(line.comments)
                data.append(temp)
        pg_table = {"column": column, "data": data}
        return pg_table

    def __dft_dbi_print_export_project_table(self, inputData):
        column = []
        data = []
        column.append('项目编号')
        column.append('项目名称')
        column.append('负责人')
        column.append('电话')
        column.append('所属单位')
        column.append('地址')
        column.append('备注')
        projectlist = self.__dft_dbi_get_user_auth_project(inputData)
        for i in range(len(projectlist)):
            pcode = projectlist[i]['id']
            result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
            if result.exists():
                for line in result:
                    temp = []
                    temp.append("P_" + str(line.prj_code))
                    temp.append(line.prj_name)
                    temp.append(line.superintendent)
                    temp.append(line.telephone)
                    temp.append(line.department)
                    temp.append(line.address)
                    temp.append(line.comments)
                    data.append(temp)
        project_table = {"column": column, "data": data}
        return project_table

    def __dft_dbi_print_export_site_table(self, inputData):
        column = []
        data = []
        column.append('站点编号')
        column.append('站点名称')
        column.append('负责人')
        column.append('电话')
        column.append('地址')
        column.append('经度')
        column.append('纬度')
        column.append('开通时间')
        column.append('备注')
        projectlist = self.__dft_dbi_get_user_auth_project(inputData)
        for i in range(len(projectlist)):
            pcode = projectlist[i]['id']
            result = dct_t_l3f2cm_site_common.objects.filter(prj_code_id=pcode)
            if result.exists():
                for line in result:
                    temp = []
                    temp.append(line.site_code)
                    temp.append(line.site_name)
                    temp.append(line.superintendent)
                    temp.append(line.telephone)
                    temp.append(line.address)
                    temp.append(str(line.longitude))
                    temp.append(str(line.latitude))
                    temp.append(str(line.create_date))
                    temp.append(str(line.comments))
                    data.append(temp)
        site_table = {'column': column, 'data': data}
        return site_table

    def __dft_dbi_print_export_devtable(self, inputData):
        column = []
        data = []
        column.append('设备编号')
        column.append('站点名称')
        column.append('所属项目')
        column.append('安装时间')
        site_list = self.__dft_dbi_get_user_auth_site(inputData)
        for i in range(len(site_list)):
            statcode = site_list[i]['id']
            result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
            if result.exists():
                for line in result:
                    devcode = line.dev_code
                    statcode = line.site_code_id
                    starttime = line.create_date
                    result = dct_t_l3f2cm_site_common.objects.filter(site_code=statcode)
                    if result.exists():
                        for line in result:
                            pcode = line.prj_code_id
                            temp = []
                            temp.append(devcode)
                            temp.append(statcode)
                            temp.append(pcode)
                            temp.append(str(starttime))
                            data.append(temp)
        dev_table = {'column': column, 'data': data}
        return dev_table

    def dft_dbi_print_excel_table_query_process(self, inputData):
        tablename = inputData['tablename']
        uid = inputData['uid']
        data = []
        column = []
        if tablename == 'usertable':
            resp = self.__dft_dbi_print_export_usertable(uid)
        elif tablename == 'PGtable':
            resp = self.__dft_dbi_print_export_pgtable(uid)
        elif tablename == 'Projtable':
            resp = self.__dft_dbi_print_export_project_table(uid)
        elif tablename == 'Pointtable':
            resp = self.__dft_dbi_print_export_site_table(uid)
        elif tablename == 'Devtable':
            resp = self.__dft_dbi_print_export_devtable(uid)
        else:
            resp = {'data': data, 'column': column}

        return resp

    def dft_dbi_project_number_inquery(self):
        result = dct_t_l3f2cm_project_common.objects.all()
        return len(result)

    def dft_dbi_all_pgnum_inquery(self):
        result = dct_t_l3f2cm_pg_common.objects.all()
        return len(result)

    def dft_dbi_user_pg_table_req(self, inputData):
        uid = inputData['uid']
        startseq = int(inputData['startseq'])
        query_length = int(inputData['query_length'])
        keyword = inputData['keyword']
        pglist = dct_t_l3f1sym_user_right_project.objects.filter(auth_type=1, uid_id=uid)
        # pglist=self.__dft_dbi_get_user_auth_projgroup(uid)
        pgtable = []
        pgtotal = len(pglist)
        # print(pglist)
        if (startseq <= pgtotal) and (startseq + query_length > pgtotal):
            query_length = pgtotal - startseq
        elif startseq > pgtotal:
            query_length = 0
        for startseq in range(startseq + query_length):
            pgcode = pglist[startseq].auth_code
            if keyword == "":
                result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                if result.exists():
                    for line in result:
                        temp = {
                            'PGCode': line.pg_code,
                            'PGName': line.pg_name,
                            'ChargeMan': line.superintendent,
                            'Telephone': line.telephone,
                            'Department': line.department,
                            'Address': line.address,
                            'Stage': line.comments
                        }
                        pgtable.append(temp)
            else:
                result = dct_t_l3f2cm_pg_common.objects.filter(Q(pg_code=pgcode), Q(pg_name__icontains=keyword) | Q(
                    superintendent__icontains=keyword) | Q(department__icontains=keyword))
                if result.exists():
                    for line in result:
                        temp = {
                            'PGCode': line.pg_code,
                            'PGName': line.pg_name,
                            'ChargeMan': line.superintendent,
                            'Telephone': line.telephone,
                            'Department': line.department,
                            'Address': line.address,
                            'Stage': line.comments
                        }
                        pgtable.append(temp)
        return pgtable

    def dft_dbi_all_project_table_req(self, inputData):
        uid = inputData['uid']
        startseq = inputData['startseq']
        query_length = inputData['query_length']
        keyword = inputData['keyword']
        projectList = self.__dft_dbi_get_user_auth_project(uid)
        projectTotal = len(projectList)
        if (startseq <= projectTotal) and (startseq + query_length > projectTotal):
            query_length = projectTotal - startseq
        elif startseq > projectTotal:
            query_length = 0
        projectTable = []
        for startseq in range(startseq + query_length):
            pcode = projectList[startseq]['id']
            if keyword == "":
                result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                if result.exists():
                    for line in result:
                        temp = {
                            'ProjCode': line.prj_code,
                            'ProjName': line.prj_name,
                            'ChargeMan': line.superintendent,
                            'Telephone': line.telephone,
                            'Department': line.department,
                            'Address': line.address,
                            'ProStartTime': str(line.create_date),
                            'Stage': line.comments,
                        }
                        projectTable.append(temp)
            else:
                result = dct_t_l3f2cm_project_common.objects.filter(Q(prj_code=pcode),
                                                                    Q(prj_name__icontains=keyword) | Q(
                                                                        superintendent__icontains=keyword) | Q(
                                                                        department__icontains=keyword))
                if result.exists():
                    for line in result:
                        temp = {
                            'ProjCode': line.prj_code,
                            'ProjName': line.prj_name,
                            'ChargeMan': line.superintendent,
                            'Telephone': line.telephone,
                            'Department': line.department,
                            'Address': line.address,
                            'ProStartTime': str(line.create_date),
                            'Stage': line.comments,
                        }
                        projectTable.append(temp)
        return projectTable

    def dft_dbi_user_all_projpglist_req(self):
        list = []
        result = dct_t_l3f2cm_pg_common.objects.all()
        if result.exists():
            for line in result:
                temp = {'id': line.pg_code, 'name': line.pg_name}
                list.append(temp)
        result = dct_t_l3f2cm_project_common.objects.all()
        if result.exists():
            for line in result:
                temp = {'id': line.prj_code, 'name': line.prj_name}
                list.append(temp)
        return list

    def dft_dbi_user_all_projlist_req(self, inputData):
        uid = inputData['uid']
        list = self.__dft_dbi_get_user_auth_project(uid)
        return list

    def dft_dbi_user_pglist_req(self, inputData):
        uid = inputData['uid']
        pglist = []
        result = dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                authtype = line.auth_type
                authcode = line.auth_code
                if authtype == 1:
                    pgcode = authcode
                else:
                    continue
                result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                if result.exists():
                    for line in result:
                        temp = {'id': line.pg_code, 'name': line.pg_name}
                        pglist.append(temp)
        return pglist

    def dft_dbi_user_projpglist_req(self, inputData):
        uid = inputData['uid']
        table = []
        result = dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        if result.exists():
            pgcode = ""
            pcode = ""
            for line in result:
                if line.auth_type == 1:
                    pgcode = line.auth_code
                elif line.auth_type == 2:
                    pcode = line.auth_code
                else:
                    continue
                if pgcode != "":
                    result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                    if result.exists():
                        for line in result:
                            temp = {'id': line.pg_code, 'name': line.pg_name}
                            if temp not in table:
                                table.append(temp)
                if pcode != "":
                    result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                    if result.exists():
                        for line in result:
                            temp = {'id': line.prj_code, 'name': line.prj_name}
                            if temp not in table:
                                table.append(temp)
        return table

    def dft_dbi_pg_projlist_req(self, inputData):
        pg_code = inputData
        result = dct_t_l3f2cm_project_common.objects.filter(pg_code_id=pg_code)
        projlist = []
        if result.exists():
            for line in result:
                temp = {'id': line.prj_code, 'name': line.prj_name}
                projlist.append(temp)
        return projlist

    def dft_dbi_pginfo_new(self, inputData):
        uid = inputData['uid']
        pgname = inputData['PGName']
        owner = inputData['ChargeMan']
        telphone = inputData['Telephone']
        department = inputData['Department']
        addr = inputData['Address']
        strage = inputData['Stage']
        projlist = inputData['Projlist']
        pgcode = self.__dft_getRandomDigID(7)  # 为自增长的字段是否还要随机生成?
        result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
        if result.exists():
            self.dft_dbi_pginfo_new(inputData)
        else:
            dct_t_l3f2cm_pg_common.objects.create(pg_code=pgcode, pg_name=pgname,
                                                  pg_creator=uid, superintendent=owner,
                                                  telephone=telphone, department=department,
                                                  address=addr, comments=strage)
        if projlist != None:
            for i in range(len(projlist)):
                p_code = ""
                p_code = projlist[i]['id']
                if p_code != "":
                    dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code).update(
                        pg_code=dct_t_l3f2cm_pg_common.objects.get(pg_code=pgcode))

        dct_t_l3f1sym_user_right_project.objects.create(uid_id=uid, auth_type=1, auth_code=pgcode)
        return True

    def dft_dbi_pginfo_modify(self, inputData):
        pgcode = inputData['PGCode']
        pgname = inputData['PGName']
        owner = inputData['ChargeMan']
        phone = inputData['Telephone']
        department = inputData['Department']
        addr = inputData['Address']
        stage = inputData['Stage']
        if "Projlist" not in inputData.keys():
            projlist = []
        else:
            projlist = inputData['Projlist']
        result = dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
        if result.exists():
            dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode).update(pg_name=pgname, superintendent=owner,
                                                                         telephone=phone, department=department,
                                                                         address=addr, comments=stage)
        result_pg = dct_t_l3f2cm_project_common.objects.filter(pg_code_id=pgcode)
        #         if result_pg.exists():
        #             for line in result_pg:
        #                 prj_array={"id":line.prj_code,"name":line.prj_name}
        #                 if prj_array in projlist:
        #                     pass
        #                 else:
        #                     print(line.prj_code)
        #                     dct_t_l3f2cm_project_common.objects.filter(prj_code=line.prj_code).update(pg_code_id=None)
        if len(projlist) != 0:
            if len(result_pg) < len(projlist):
                for i in range(len(projlist)):
                    p_code = ""
                    p_code = projlist[i]['id']
                    if p_code != "":
                        dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code).update(
                            pg_code=dct_t_l3f2cm_pg_common.objects.get(pg_code=pgcode))
            else:
                for line in result_pg:
                    prj_array = {'id': str(line.prj_code), 'name': str(line.prj_name)}
                    if prj_array in projlist:
                        pass
                    else:
                        dct_t_l3f2cm_project_common.objects.filter(prj_code=prj_array["id"]).update(pg_code_id=None)
        else:
            dct_t_l3f2cm_project_common.objects.filter(pg_code=pgcode).update(pg_code_id=None)
        return True

    def dft_dbi_projinfo_new(self, inputData):
        uid = inputData['uid']
        p_code = self.__dft_getRandomDigID(8)
        pname = inputData['pname']
        chargeman = inputData['chargeman']
        telephone = inputData['telephone']
        department = inputData['department']
        addr = inputData['addr']
        starttime = inputData['starttime']
        stage = inputData['stage']
        result = dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code)
        if result.exists():
            self.dft_dbi_projinfo_new(inputData)
        else:
            dct_t_l3f2cm_project_common.objects.create(prj_code=p_code, prj_name=pname, prj_creator=uid,
                                                       superintendent=chargeman, telephone=telephone, address=addr,
                                                       comments=stage, department=department, create_date=starttime)
        dct_t_l3f1sym_user_right_project.objects.create(auth_type=2, auth_code=p_code,
                                                        uid=(dct_t_l3f1sym_account_primary.objects.get(uid=uid)))
        return True

    def dft_dbi_projinfo_modify(self, inputData):
        pcode = inputData['ProjCode']
        pname = inputData['ProjName']
        chargeman = inputData['ChargeMan']
        telephone = inputData['Telephone']
        department = inputData['Department']
        addr = inputData['Address']
        starttime = inputData['ProStartTime']
        stage = inputData['Stage']
        result = dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
        if result.exists():
            resp = dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)
            resp.prj_name = pname
            resp.superintendent = chargeman
            resp.telephone = telephone
            resp.department = department
            resp.address = addr
            resp.comments = stage
            resp.create_date = starttime
            resp.save()
            # dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode).update(prj_name=pname,superintendent=chargeman,telephone=telephone,department=department,address=addr,comments=stage)
        return True

    def dft_dbi_projinfo_delete(self, inputData):
        pcode = inputData['pcode']
        dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode).delete()
        dct_t_l3f1sym_user_right_project.objects.filter(auth_code=pcode).delete()
        return True

    def dft_dbi_pginfo_delete(self, inputData):
        pgcode = inputData['pgcode']
        dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode).delete()
        dct_t_l3f1sym_user_right_project.objects.filter(auth_type=1, auth_code=pgcode).delete()
        return True

    def dft_dbi_all_sitenum_inquery(self):
        result = dct_t_l3f2cm_site_common.objects.all()
        return len(result)

    def dft_dbi_user_all_project_sitelist_req(self, inputData):
        uid = inputData['uid']
        projectlist = self.__dft_dbi_get_user_auth_project(uid)
        sitelist = []
        for line in projectlist:
            pcode = line['id']
            if pcode != "":
                result = dct_t_l3f2cm_site_common.objects.filter(prj_code=pcode)
                if result.exists():
                    for site in result:
                        temp = {'id': site.site_code, 'name': site.site_name, 'ProjCode': site.prj_code_id}
                        sitelist.append(temp)
        return sitelist

    def dft_dbi_one_proj_sitelist_req(self, inputData):
        pcode = inputData['p_code']
        sitelist = []
        result = dct_t_l3f2cm_site_common.objects.filter(
            prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)))
        if result.exists():
            for line in result:
                temp = {'id': line.site_code, 'name': line.site_name, 'ProjCode': line.prj_code_id}
                sitelist.append(temp)
        return sitelist

    def dft_dbi_all_sitetable_req(self, inputData):
        uid = inputData['uid']
        startseq = inputData['startseq']
        query_length = inputData['query_length']
        keyword = inputData['keyword']
        projectlist = self.__dft_dbi_get_user_auth_project(uid)
        projtotal = len(projectlist)
        if (startseq <= projtotal) and (startseq + query_length > projtotal):
            query_length = projtotal - startseq
        elif startseq > projtotal:
            query_length = 0
        sitetable = []
        for i in range(startseq, startseq + query_length):
            pcode = projectlist[i]['id']
            if keyword == "":
                result = dct_t_l3f2cm_site_common.objects.filter(
                    prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)))
                if result.exists():
                    for line in result:
                        statCode = line.site_code
                        towerInfo = self.__dft_dbi_get_tower_info(statCode)
                        if hasattr(towerInfo, 'site_code') == False:
                            temp = {
                                'StatCode': statCode,
                                'StatName': line.site_name,
                                'ProjCode': line.prj_code_id,
                                'ChargeMan': line.superintendent,
                                'Telephone': line.telephone,
                                'Longitude': str(line.longitude),
                                'Latitude': str(line.latitude),
                                'Department': line.department,
                                'Address': line.address,
                                'Country': line.district,
                                'Street': line.street,
                                'Square': line.site_area,
                                'ProStartTime': str(line.create_date),
                                'Stage': line.comments,
                            }
                        else:
                            temp = {
                                'StatCode': statCode,
                                'StatName': line.site_name,
                                'ProjCode': line.prj_code_id,
                                'ChargeMan': line.superintendent,
                                'Telephone': line.telephone,
                                'Longitude': str(line.longitude),
                                'Latitude': str(line.latitude),
                                'Department': line.department,
                                'Address': line.address,
                                'Country': line.district,
                                'Street': line.street,
                                'Square': line.site_area,
                                'ProStartTime': str(line.create_date),
                                'Stage': line.comments,
                                'SN': towerInfo.tower_sn,
                                'PN': towerInfo.tower_code,
                                'Order': towerInfo.order_no,
                                'Model': towerInfo.tower_type
                            }
                        sitetable.append(temp)
            else:
                result = dct_t_l3f2cm_site_common.objects.filter(
                    Q(prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode))),
                    Q(site_name__icontains=keyword) | Q(address__icontains=keyword))
                if result.exists():
                    for line in result:
                        statCode = line.site_code
                        towerInfo = self.__dft_dbi_get_tower_info(statCode)
                        if hasattr(towerInfo, 'site_code') == False:
                            temp = {
                                'StatCode': statCode,
                                'StatName': line.site_name,
                                'ProjCode': line.prj_code_id,
                                'ChargeMan': line.superintendent,
                                'Telephone': line.telephone,
                                'Longitude': str(line.longitude),
                                'Latitude': str(line.latitude),
                                'Department': line.department,
                                'Country': line.district,
                                'Street': line.street,
                                'Square': line.site_area,
                                'Address': line.address,
                                'ProStartTime': str(line.create_date),
                                'Stage': line.comments,
                            }
                        else:
                            temp = {
                                'StatCode': statCode,
                                'StatName': line.site_name,
                                'ProjCode': line.prj_code_id,
                                'ChargeMan': line.superintendent,
                                'Telephone': line.telephone,
                                'Longitude': str(line.longitude),
                                'Latitude': str(line.latitude),
                                'Department': line.department,
                                'Country': line.district,
                                'Street': line.street,
                                'Square': line.site_area,
                                'Address': line.address,
                                'ProStartTime': str(line.create_date),
                                'Stage': line.comments,
                                'SN': towerInfo.tower_sn,
                                'PN': towerInfo.tower_code,
                                'Order': towerInfo.order_no,
                                'Model': towerInfo.tower_type
                            }
                        sitetable.append(temp)
        return sitetable

    def dft_dbi_point_get_activeinfo(self, inputData):
        statCode = inputData['statCode']
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        status = ""
        if result.exists():
            for line in result:
                status = line.status
                if status == "C":
                    status = 'true'
                else:
                    status = 'false'
        return status

    def dft_dbi_point_set_activeInfo(self, inputData):
        statCode = inputData['statcode']
        status = "C"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(status=status)
        return True

    def dft_dbi_siteInfo_new(self, inputData):
        statCode = self.__dft_getRandomDigID(9)
        statname = inputData['StatName']
        pcode = inputData['ProjCode']
        ChargeMan = inputData['ChargeMan']
        Telephone = inputData['Telephone']
        Longitude = inputData['Longitude']
        Latitude = inputData['Latitude']
        Department = inputData['Department']
        Address = inputData['Address']
        Country = inputData['Country']
        Street = inputData['Street']
        Square = inputData['Square']
        ProStartTime = inputData['ProStartTime']
        Stage = inputData['Stage']
        status = 'I'
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        if result.exists():
            dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(site_name=statname, status=status,
                                                                               prj_code_id=pcode,
                                                                               superintendent=ChargeMan,
                                                                               telephone=Telephone,
                                                                               address=Address, longitude=Longitude,
                                                                               latitude=Latitude,
                                                                               comments=Stage, department=Department,
                                                                               district=Country, street=Street,
                                                                               site_area=Square,
                                                                               create_date=ProStartTime)
        else:
            dct_t_l3f2cm_site_common.objects.create(site_code=statCode, site_name=statname, status=status,
                                                    prj_code_id=pcode, superintendent=ChargeMan, telephone=Telephone,
                                                    address=Address, comments=Stage, department=Department,
                                                    district=Country, street=Street, site_area=Square,
                                                    create_date=ProStartTime)
        return True

    def dft_dbi_siteinfo_modify(self, inputData):
        StatCode = int(inputData['StatCode'])
        StatName = inputData['StatName']
        ProjCode = inputData['ProjCode']
        ChargeMan = inputData['ChargeMan']
        Telephone = inputData['Telephone']
        Longitude = inputData['Longitude']
        Latitude = inputData['Latitude']
        Department = inputData['Department']
        Address = inputData['Address']
        Country = inputData['Country']
        Street = inputData['Street']
        Square = inputData['Square']
        ProStartTime = inputData['ProStartTime']
        Stage = inputData['Stage']
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=StatCode)
        if result.exists():
            dct_t_l3f2cm_site_common.objects.filter(site_code=StatCode).update(site_name=StatName,
                                                                               prj_code_id=ProjCode,
                                                                               superintendent=ChargeMan,
                                                                               telephone=Telephone,
                                                                               address=Address, longitude=Longitude,
                                                                               latitude=Latitude,
                                                                               comments=Stage, department=Department,
                                                                               district=Country, street=Street,
                                                                               site_area=Square,
                                                                               create_date=ProStartTime
                                                                               )
        else:
            self.dft_dbi_siteInfo_new(inputData)
        return True

    def dft_dbi_fstt_site_info_new_view(self, inputData):
        statCode = self.__dft_getRandomDigID(9)
        statname = inputData['StatName']
        pcode = inputData['ProjCode']
        ChargeMan = inputData['ChargeMan']
        Telephone = inputData['Telephone']
        Longitude = inputData['Longitude']
        Latitude = inputData['Latitude']
        Department = inputData['Department']
        Address = inputData['Address']
        Country = inputData['Country']
        Street = inputData['Street']
        Square = inputData['Square']
        Stage = inputData['Stage']
        SN = inputData["SN"]
        Order = inputData["Order"]
        PN = inputData["PN"]
        Model = inputData["Model"]
        if hasattr(inputData, 'Config'):
            Config = inputData['Config']
        else:
            Config = []
        uid = inputData['uid']
        status = 'I'
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        if result.exists():
            result.update(site_name=statname, status=status, prj_code_id=pcode, superintendent=ChargeMan,
                          telephone=Telephone,
                          address=Address, longitude=Longitude,
                          latitude=Latitude,
                          comments=Stage, department=Department,
                          district=Country, street=Street)
            resp = dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=statCode)
            if resp.exists():
                resp.update(tower_sn=SN, order_no=Order, tower_code=PN, tower_type=Model)
            else:
                dct_t_l3f2cm_site_fstt.objects.create(site_code_id=statCode, tower_sn=SN, order_no=Order, tower_code=PN,
                                                      tower_type=Model, tower_date=datetime.date.today())
        else:
            dct_t_l3f2cm_site_common.objects.create(site_code=statCode, site_name=statname, status=status,
                                                    site_creator=uid,
                                                    prj_code_id=pcode, superintendent=ChargeMan, telephone=Telephone,
                                                    address=Address, comments=Stage, department=Department,
                                                    district=Country, street=Street, create_date=datetime.date.today())
            dct_t_l3f2cm_site_fstt.objects.create(site_code_id=statCode, tower_sn=SN, order_no=Order, tower_code=PN,
                                                  tower_type=Model, tower_date=datetime.date.today())
        return True

    def dft_dbi_fstt_site_info_modify_view(self, inputData):
        StatCode = int(inputData['StatCode'])
        statname = inputData['StatName']
        pcode = inputData['ProjCode']
        ChargeMan = inputData['ChargeMan']
        Telephone = inputData['Telephone']
        Longitude = inputData['Longitude']
        Latitude = inputData['Latitude']
        Department = inputData['Department']
        Address = inputData['Address']
        Country = inputData['Country']
        Street = inputData['Street']
        Square = inputData['Square']
        Stage = inputData['Stage']
        SN = inputData["SN"]
        Order = inputData["Order"]
        PN = inputData["PN"]
        Model = inputData["Model"]
        Config = inputData['Config']
        status = 'I'
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=StatCode)
        if result.exists():
            result.update(site_name=statname, status=status, prj_code_id=pcode, superintendent=ChargeMan,
                          telephone=Telephone,
                          address=Address, longitude=Longitude,
                          latitude=Latitude,
                          comments=Stage, department=Department,
                          district=Country, street=Street)
            resp = dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=StatCode)
            if resp.exists():
                resp.update(tower_sn=SN, order_no=Order, tower_code=PN, tower_type=Model)
            else:
                dct_t_l3f2cm_site_fstt.objects.create(site_code_id=StatCode, tower_sn=SN, order_no=Order, tower_code=PN,
                                                      tower_type=Model, tower_date=datetime.date.today())
        else:
            self.dft_dbi_fstt_site_info_new_view(inputData)
        return True

    def dft_dbi_all_hcutable_req(self, inputData):
        uid = inputData['uid']
        startSeq = inputData['startseq']
        query_length = inputData['query_length']
        keyWord = inputData['keyWord']
        siteList = self.__dft_dbi_get_user_auth_site(uid)
        siteTotal = len(siteList)
        if ((startSeq <= siteTotal) and (startSeq + query_length) > siteTotal):
            query_length = siteTotal - startSeq
        elif (startSeq > siteTotal):
            query_length = 0
        hcuTable = []
        for i in range(startSeq + query_length):
            statCode = siteList[i]['id']
            result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
            if result.exists():
                for line in result:
                    devcode = line.dev_code
                    starttime = line.create_date
                    resp = dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devcode)
                    if resp.exists():
                        for line in resp:
                            macaddr = line.mac_addr
                            ipaddr = line.ip_addr
                            devstatus = 'true'
                            url = line.pic1_url
                            if keyWord == "":
                                projInfo = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
                                projCode = projInfo[0].prj_code_id
                            else:
                                projInfo = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode and (
                                        Q(site_name__icontains=keyWord) or Q(address__icontains=keyWord)))
                                projCode = projInfo[0].prj_code_id
                            temp = {
                                'DevCode': devcode,
                                'StatCode': statCode,
                                'ProjCode': projCode,
                                'StartTime': str(starttime),
                                'PreEndTime': "",
                                'EndTime': "",
                                'DevStatus': devstatus,
                                'VideoURL': url,
                                'MAC': macaddr,
                                'IP': ipaddr,
                            }
                            hcuTable.append(temp)
        return hcuTable

    def dft_dbi_fstt_all_hcutable_req_view(self, inputData):
        uid = inputData['uid']
        startSeq = inputData['startseq']
        query_length = inputData['query_length']
        keyWord = inputData['keyWord']
        siteList = self.__dft_dbi_get_user_auth_site(uid)
        siteTotal = len(siteList)
        if ((startSeq <= siteTotal) and (startSeq + query_length) > siteTotal):
            query_length = siteTotal - startSeq
        elif (startSeq > siteTotal):
            query_length = 0
        hcuTable = []
        for i in range(startSeq + query_length):
            statCode = siteList[i]['id']
            result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
            if result.exists():
                for line in result:
                    devcode = line.dev_code
                    starttime = line.create_date
                    resp = dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=devcode)
                    if resp.exists():
                        for line in resp:
                            macaddr = line.mac_addr
                            ipaddr = line.ip_addr
                            devstatus = 'true'
                            url = line.pic1_url
                            if keyWord == "":
                                projInfo = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
                                projCode = projInfo[0].prj_code_id
                            else:
                                projInfo = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode and (
                                        Q(site_name__icontains=keyWord) or Q(address__icontains=keyWord)))
                                projCode = projInfo[0].prj_code_id
                            temp = {
                                'DevCode': devcode,
                                'StatCode': statCode,
                                'ProjCode': projCode,
                                'StartTime': str(starttime),
                                'PreEndTime': "",
                                'EndTime': "",
                                'DevStatus': devstatus,
                                'VideoURL': url,
                                'MAC': macaddr,
                                'IP': ipaddr,
                            }
                            hcuTable.append(temp)
        return hcuTable

    def dft_dbi_fstt_dev_info_update_view(self, inputData):
        devCode = inputData['DevCode']
        statcode = inputData['StatCode']
        starttime = inputData['StartTime']
        preendtime = inputData['PreEndTime']
        endtime = inputData['EndTime']
        devstatus = inputData['DevStatus']
        videourl = inputData['VideoURL']
        if devstatus == 'true':
            devstatus = 'Y'
        else:
            devstatus = 'N'
        devCode1 = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if devCode1.exists():
            devCode1.update(create_date=starttime, site_code_id=statcode)
            result = dct_t_l3f2cm_device_fstt.objects.filter(dev_code_id=devCode)
            base_port = devCode1[0].base_port
            if result.exists():
                result = dct_t_l3f2cm_device_fstt.objects.get(dev_code_id=devCode)
                if videourl == "" or videourl == None:
                    result.pic1_url = videourl
                result.save()
            else:
                weburl = "http://" + str(devCode) + ".ngrok2.hkrob.com:8080/phpmyadmin"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(base_port) + "2" + "/ISAPI"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "3" + "/ISAPI/Streaming/Channels/1"
                pic2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "6" + "/ISAPI/Streaming/channels/1/picture"
                ctrl2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(base_port) + "6" + "/ISAPI"
                video2url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "7" + "/ISAPI/Streaming/Channels/1"
                pic3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "8" + "/ISAPI/Streaming/channels/1/picture"
                ctrl3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(base_port) + "8" + "/ISAPI"
                video3url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "9" + "/ISAPI/Streaming/Channels/1"
                dct_t_l3f2cm_device_fstt.objects.create(dev_code_id=devCode, web_url=weburl, pic1_url=pic1url,
                                                        ctrl1_url=ctrl1url, video1_url=video1url, pic2_url=pic2url,
                                                        ctrl2_url=ctrl2url, video2_url=video2url, pic3_url=pic3url,
                                                        ctrl3_url=ctrl3url, video3_url=video3url)
        else:
            result = dct_t_l3f2cm_device_inventory.objects.latest('base_port')
            BasePort = result.base_port + 1
            dct_t_l3f2cm_device_inventory.objects.create(dev_code=devCode, site_code_id=statcode, create_date=starttime,
                                                         base_port=BasePort, upgradeflag=1)
            weburl = "http://" + str(devCode) + "ngrok2.hkrob.com:8080/phpmyadmin"
            pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                BasePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
            ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "2" + "/ISAPI"
            video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "3" + "/ISAPI/Streaming/Channels/1"
            pic2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                BasePort) + "6" + "/ISAPI/Streaming/channels/1/picture"
            ctrl2url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "6" + "/ISAPI"
            video2url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "7" + "/ISAPI/Streaming/Channels/1"
            pic3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                BasePort) + "8" + "/ISAPI/Streaming/channels/1/picture"
            ctrl3url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "8" + "/ISAPI"
            video3url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "9" + "/ISAPI/Streaming/Channels/1"
            dct_t_l3f2cm_device_fstt.objects.create(dev_code_id=devCode, web_url=weburl, pic1_url=pic1url,
                                                    ctrl1_url=ctrl1url, video1_url=video1url, pic2_url=pic2url,
                                                    ctrl2_url=ctrl2url, video2_url=video2url, pic3_url=pic3url,
                                                    ctrl3_url=ctrl3url, video3_url=video3url)
        status = "C"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statcode).update(status=status)
        return True

    '''PC端使用工具修改设备的参数信息'''

    def dft_dbi_pc_get_device_list_view(self, inputDate):
        dev_code = inputDate['code']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code__icontains=dev_code)
        dev_list = []
        if result.exists():
            for line in result:
                dev_list.append(line.dev_code)
        return dev_list

    def dft_dbi_pc_get_device_data_view(self, inputData):
        device_code = inputData['code']
        resp = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=device_code)
        result = dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=device_code)
        hcuLable = ""
        hwtype = ""
        swtype = ""
        upgradeFlag = ""
        restartRightNow = ""
        ngrokPort = ""
        cus_info = ""
        userDef1 = ""
        userDef2 = ""
        userDef3 = ""
        userDef4 = ""
        userName = ""
        userPswd = ""
        eccPort = ""
        prescaleXHT = ""
        prescaleCUS = ""
        prescaleOFC = ""
        calPm25CoefMax = ""
        calPm25CoefMin = ""
        calPm25CoefK = ""
        calPm25CoefB = ""
        calTempCoefMax = ""
        calTempCoefMin = ""
        calTempCoefK = ""
        calTempCoefB = ""
        calHumidCoefMax = ""
        calHumidCoefMin = ""
        calHumidCoefK = ""
        calHumidCoefB = ""
        calNoiseCoefMax = ""
        calNoiseCoefMin = ""
        calNoiseCoefK = ""
        calNoiseCoefB = ""
        calWindspdCoefMax = ""
        calWindspdCoefMin = ""
        calWindspdCoefK = ""
        calWindspdCoefB = ""
        calWinddirCoefMax = ""
        calWinddirCoefMin = ""
        calWinddirCoefK = ""
        calWinddirCoefB = ""
        calWinddir = ""
        calPm25ThdCannon = ""
        if resp.exists():
            for line_dev in resp:
                hcuLable = line_dev.dev_code
                hwtype = line_dev.hw_type
                swtype = line_dev.sw_ver
                upgradeFlag = line_dev.upgradeflag
                restartRightNow = line_dev.rebootflag
                ngrokPort = line_dev.base_port
                cus_info = line_dev.cus_info
                userDef1 = line_dev.userdef1
                userDef2 = line_dev.userdef2
                userDef3 = line_dev.userdef3
                userDef4 = line_dev.userdef4
                userName = line_dev.username
                userPswd = line_dev.userpswd
                eccPort = line_dev.eccport
                prescaleOFC = line_dev.prescale_ofc
                prescaleXHT = line_dev.prescale_xht
                prescaleCUS = line_dev.prescale_cus
        if (result.exists()):
            for line in result:
                calPm25CoefMax = line.dust_coefmax
                calPm25CoefMin = line.dust_coefmin
                calPm25CoefK = line.dust_coefK
                calPm25CoefB = line.dust_coefB
                calTempCoefMax = line.temp_coefmax
                calTempCoefMin = line.temp_coefmin
                calTempCoefK = line.temp_coefK
                calTempCoefB = line.temp_coefB
                calHumidCoefMax = line.humid_coefmax
                calHumidCoefMin = line.humid_coefmin
                calHumidCoefK = line.humid_coefK
                calHumidCoefB = line.humid_coefB
                calNoiseCoefMax = line.noise_coefmax
                calNoiseCoefMin = line.noise_coefmin
                calNoiseCoefK = line.noise_coefK
                calNoiseCoefB = line.noise_coefB
                calWindspdCoefMax = line.windspd_coefmax
                calWindspdCoefMin = line.windspd_coefmin
                calWindspdCoefK = line.windspd_coefK
                calWindspdCoefB = line.windspd_coefB
                calWinddirCoefMax = line.winddir_coefmax
                calWinddirCoefMin = line.winddir_coefmin
                calWinddirCoefK = line.winddir_coefK
                calWinddirCoefB = line.winddir_coefB
                calWinddir = line.winddir_delta
                calPm25ThdCannon = line.dust_cannon
        msgIeCnt = {
            "hcuLable": hcuLable,
            "hwtype": hwtype,
            "swtype": swtype,
            "upgradeFlag": upgradeFlag,
            "restartRightNow": restartRightNow,
            "ngrokPort": ngrokPort,
            "cus_info": cus_info,
            "userDef1": userDef1,
            "userDef2": userDef2,
            "userDef3": userDef3,
            "userDef4": userDef4,
            "userName": userName,
            "userPswd": userPswd,
            "eccPort": eccPort,
            "prescaleXHT": prescaleXHT,
            "prescaleCUS": prescaleCUS,
            "prescaleOFC": prescaleOFC,
            "calPm25CoefMax": calPm25CoefMax,
            "calPm25CoefMin": calPm25CoefMin,
            "calPm25CoefK": calPm25CoefK,
            "calPm25CoefB": calPm25CoefB,
            "calTempCoefMax": calTempCoefMax,
            "calTempCoefMin": calTempCoefMin,
            "calTempCoefK": calTempCoefK,
            "calTempCoefB": calTempCoefB,
            "calHumidCoefMax": calHumidCoefMax,
            "calHumidCoefMin": calHumidCoefMin,
            "calHumidCoefK": calHumidCoefK,
            "calHumidCoefB": calHumidCoefB,
            "calNoiseCoefMax": calNoiseCoefMax,
            "calNoiseCoefMin": calNoiseCoefMin,
            "calNoiseCoefK": calNoiseCoefK,
            "calNoiseCoefB": calNoiseCoefB,
            "calWindspdCoefMax": calWindspdCoefMax,
            "calWindspdCoefMin": calWindspdCoefMin,
            "calWindspdCoefK": calWindspdCoefK,
            "calWindspdCoefB": calWindspdCoefB,
            "calWinddirCoefMax": calWinddirCoefMax,
            "calWinddirCoefMin": calWinddirCoefMin,
            "calWinddirCoefK": calWinddirCoefK,
            "calWinddirCoefB": calWinddirCoefB,
            "calWinddir": calWinddir,
            "calPm25ThdCannon": calPm25ThdCannon,
        }
        return msgIeCnt
    def dft_dbi_pc_set_device_data_view(self, inputData):
        device_code = inputData['code']
        device_data = inputData['new_data']
        hwtype = device_data["hwtype"]
        swtype = device_data["swtype"]
        upgradeFlag = device_data["upgradeFlag"]
        restartRightNow = device_data["restartRightNow"]
        ngrokPort = device_data["ngrokPort"]
        cus_info = device_data["cus_info"]
        userDef1 = device_data["userDef1"]
        userDef2 = device_data["userDef2"]
        userDef3 = device_data["userDef3"]
        userDef4 = device_data["userDef4"]
        userName = device_data["userName"]
        userPswd = device_data["userPswd"]
        eccPort = device_data["eccPort"]
        prescaleXHT = device_data["prescaleXHT"]
        prescaleCUS = device_data["prescaleCUS"]
        prescaleOFC = device_data["prescaleOFC"]
        calPm25CoefMax = device_data["calPm25CoefMax"]
        calPm25CoefMin = device_data["calPm25CoefMin"]
        calPm25CoefK = device_data["calPm25CoefK"]
        calPm25CoefB = device_data["calPm25CoefB"]
        calTempCoefMax = device_data["calTempCoefMax"]
        calTempCoefMin = device_data["calTempCoefMin"]
        calTempCoefK = device_data["calTempCoefK"]
        calTempCoefB = device_data["calTempCoefB"]
        calHumidCoefMax = device_data["calHumidCoefMax"]
        calHumidCoefMin = device_data["calHumidCoefMin"]
        calHumidCoefK = device_data["calHumidCoefK"]
        calHumidCoefB = device_data["calHumidCoefB"]
        calNoiseCoefMax = device_data["calNoiseCoefMax"]
        calNoiseCoefMin = device_data["calNoiseCoefMin"]
        calNoiseCoefK = device_data["calNoiseCoefK"]
        calNoiseCoefB = device_data["calNoiseCoefB"]
        calWindspdCoefMax = device_data["calWindspdCoefMax"]
        calWindspdCoefMin = device_data["calWindspdCoefMin"]
        calWindspdCoefK = device_data["calWindspdCoefK"]
        calWindspdCoefB = device_data["calWindspdCoefB"]
        calWinddirCoefMax = device_data["calWinddirCoefMax"]
        calWinddirCoefMin = device_data["calWinddirCoefMin"]
        calWinddirCoefK = device_data["calWinddirCoefK"]
        calWinddirCoefB = device_data["calWinddirCoefB"]
        calWinddir = device_data["calWinddir"]
        calPm25ThdCannon = device_data["calPm25ThdCannon"]
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=device_code).update(hw_type=hwtype,
                                                            sw_ver=swtype,upgradeflag=upgradeFlag,rebootflag=restartRightNow,base_port=ngrokPort,
                                                            cus_info=cus_info,userdef1=userDef1,userdef2=userDef2,userdef3=userDef3,userdef4=userDef4,
                                                            username=userName,userpswd=userPswd,eccport=eccPort,prescale_xht=prescaleXHT,prescale_ofc=prescaleOFC,
                                                            prescale_cus=prescaleCUS)
        dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=device_code).update(dust_coefmax=calPm25CoefMax,
                                                dust_coefmin=calPm25CoefMin,dust_coefK=calPm25CoefK,dust_coefB=calPm25CoefB,
                                                temp_coefmax=calTempCoefMax,temp_coefmin=calTempCoefMin,temp_coefK=calTempCoefK,
                                                temp_coefB=calTempCoefB,humid_coefmax=calHumidCoefMax,humid_coefmin=calHumidCoefMin,
                                                humid_coefK=calHumidCoefK,humid_coefB=calHumidCoefB,noise_coefmax=calNoiseCoefMax,
                                                noise_coefmin=calNoiseCoefMin,noise_coefK=calNoiseCoefK,noise_coefB=calNoiseCoefB,
                                                windspd_coefmax=calWindspdCoefMax,windspd_coefmin=calWindspdCoefMin,windspd_coefK=calWindspdCoefK,
                                                windspd_coefB=calWindspdCoefB,winddir_coefmax=calWinddirCoefMax,winddir_coefmin=calWinddirCoefMin,
                                                winddir_coefK=calWinddirCoefK,winddir_coefB=calWinddirCoefB,winddir_delta=calWinddir,
                                                dust_cannon=calPm25ThdCannon)
        result={"state":'true','message':'修改成功'}
        return result
        
    def dft_dbi_site_devlist_req(self, inputData):
        statCode = inputData['statcode']
        result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        devList = []
        if result.exists():
            for line in result:
                temp = {'id': line.site_code_id, 'name': line.dev_code}
                devList.append(temp)
        return devList

    def dft_dbi_siteinfo_delete(self, inputData):
        statCode = inputData['statcode']
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).delete()
        return result

    def dft_dbi_aqyc_deviceinfo_delete(self, inputData):
        devCode = inputData['devcode']
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).delete()
        return True

    def dft_dbi_all_hcunum_inquery(self):
        result = dct_t_l3f2cm_device_inventory.objects.all()
        return len(result)

    def dft_dbi_aqyc_devinfo_update(self, inputData):
        devCode = inputData['DevCode']
        statcode = inputData['StatCode']
        starttime = inputData['StartTime']
        preendtime = inputData['PreEndTime']
        endtime = inputData['EndTime']
        devstatus = inputData['DevStatus']
        videourl = inputData['VideoURL']
        if devstatus == 'true':
            devstatus = 'Y'
        else:
            devstatus = 'N'
        devCode1 = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if devCode1.exists():
            devCode1.update(create_date=starttime, site_code_id=statcode)
            result = dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
            base_port = devCode1[0].base_port
            if result.exists():
                result = dct_t_l3f2cm_device_aqyc.objects.get(dev_code_id=devCode)
                if videourl == "" or videourl == None:
                    result.cam_url = videourl
                result.save()
            else:
                weburl = "http://" + str(devCode) + ".ngrok2.hkrob.com:8080/phpmyadmin"
                pic1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "2" + "/ISAPI/Streaming/channels/1/picture"
                ctrl1url = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(base_port) + "2" + "/ISAPI"
                video1url = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                    base_port) + "3" + "/ISAPI/Streaming/Channels/1"
                dct_t_l3f2cm_device_aqyc.objects.create(dev_code_id=devCode, web_url=weburl, pic1_url=pic1url,
                                                        ctrl1_url=ctrl1url, video1_url=video1url)
        else:
            result = dct_t_l3f2cm_device_inventory.objects.latest('base_port')
            BasePort = result.base_port + 1
            dct_t_l3f2cm_device_inventory.objects.create(dev_code=devCode, site_code_id=statcode, create_date=starttime,
                                                         base_port=BasePort, upgradeflag=1)
            #             weburl = "http://" + str(devCode) + ".ngrok2.hkrob.com:8080/yii2basic/web/index.php"
            dct_t_l3f2cm_device_cail.objects.create(dev_code_id=devCode)
            weburl = "http://" + str(devCode) + ".ngrok2.hkrob.com:8080/phpmyadmin"
            picurl = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(
                BasePort) + "2" + "/ISAPI/Streaming/channels/1/picture"
            ctrlurl = "http://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "2" + "/ISAPI"
            videourl_B = "rtsp://admin:Bxxh!123@ngrok2.hkrob.com:" + str(BasePort) + "3" + "ISAPI/Streaming/Channels/1"
            dct_t_l3f2cm_device_aqyc.objects.create(dev_code_id=devCode, web_url=weburl, pic1_url=picurl,
                                                    ctrl1_url=ctrlurl, video1_url=videourl_B)
        status = "C"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statcode).update(status=status)
        return True

    def dft_dbi_qrcode_scan_newcode_check(self, inputData):
        devCode = inputData['devcode']
        validFlag = "Y"
        timestamp = int(time.time())
        timeStamp = time.localtime(timestamp)
        valiDate = time.strftime("%Y-%m-%d", timeStamp)
        result = dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode)
        if result.exists():
            dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode).update(validflag=validFlag, validdate=valiDate)
            return True
        else:
            return False

    def dft_dbi_qrcode_scan_newcode_add(self, inputData):
        devCode = inputData['devcode']
        statCode = inputData['statcode']
        latitude = inputData['latitude']
        longitude = inputData['longitude']
        timestamp = int(time.time())
        timeStamp = time.localtime(timestamp)
        openDate = time.strftime("%Y-%m-%d", timeStamp)
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).update(site_code_id=statCode,
                                                                                  create_date=openDate)
        else:
            dct_t_l3f2cm_device_inventory.objects.create(dev_code=devCode, site_code_id=statCode, create_date=openDate)
        status = "A"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(status=status, latitude=latitude,
                                                                           longitude=longitude)
        return True

    def dft_dbi_qrcode_scan_free_projsite_inquery(self):
        status = "C"
        sitetable = []
        projtable = []
        result = dct_t_l3f2cm_site_common.objects.filter(~Q(status=status))
        if result.exists():
            for line in result:
                temp = {
                    'StatCode': line.site_code,
                    'StatName': line.site_name,
                    'ProjCode': line.prj_code_id,
                    'ChargeMan': line.superintendent,
                    'Telephone': line.telephone,
                    'Longitude': line.longitude,
                    'Latitude': line.latitude,
                    'Department': line.department,
                    'Address': line.address,
                    'Country': line.district,
                    'Street': line.street,
                    'Square': line.site_area,
                    'ProStartTime': line.create_date,
                    'Stage': line.comments,
                }
                sitetable.append(temp)
                id = line.prj_code.prj_code
                name = line.prj_code.prj_name
                temp = {"id": id, 'name': name}
                projtable.append(temp)
        resp = {'site_list': sitetable, 'proj_list': projtable}
        return resp

    def dft_dbi_aqyc_qrcode_scan_siteinfo_update_gps(self, inputData):
        devCode = inputData['devcode']
        latitude = inputData['latitude']
        longitude = inputData['longitude']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            for line in result:
                statCode = line.site_code
                statCode.latitude = latitude
                statCode.longitude = longitude
                statCode.save(update_fields=['latitude', 'longitude'])
        return True

    def dft_dbi_fstt_point_config_query(self, inputData):
        statCode = inputData['statCode']
        confList = []
        if statCode == 'S_48071851':
            temp = {'id': '1', 'name': '摄像头'}
            confList.append(temp)
            temp = {'id': '2', 'name': '温度传感器'}
            confList.append(temp)
            temp = {'id': '3', 'name': '湿度传感器'}
            confList.append(temp)
        elif statCode == 'S_49950094':
            temp = {'id': '1', 'name': '摄像头'}
            confList.append(temp)
            temp = {'id': '2', 'name': '粉尘传感器'}
            confList.append(temp)
            temp = {'id': '3', 'name': '风向传感器'}
            confList.append(temp)
            temp = {'id': '4', 'name': '风速传感器'}
            confList.append(temp)
            temp = {'id': '5', 'name': '温度传感器'}
            confList.append(temp)
            temp = {'id': '6', 'name': '湿度传感器'}
            confList.append(temp)
        else:
            temp = {'id': '1', 'name': '摄像头'}
            confList.append(temp)
            temp = {'id': '2', 'name': '粉尘传感器'}
            confList.append(temp)
            temp = {'id': '3', 'name': '风向传感器'}
            confList.append(temp)
            temp = {'id': '4', 'name': '风速传感器'}
            confList.append(temp)
            temp = {'id': '5', 'name': '温度传感器'}
            confList.append(temp)
            temp = {'id': '6', 'name': '湿度传感器'}
            confList.append(temp)
            temp = {'id': '7', 'name': '噪声传感器'}
            confList.append(temp)
        return confList

    def dft_dbi_fstt_point_login_history(self, inputData):
        statCode = inputData['statCode']
        loginHistory = []
        result = dct_t_l3f2cm_favour_site.objects.filter(site_code_id=statCode)
        if result.exists():
            uid = result[0].uid_id
            name = self.__dft_dbi_get_user_name(uid)
            loginTime = result[0].create_time
            temp = {'name': name, 'time': loginTime}
            loginHistory.append(temp)
        return loginHistory

    def dft_dbi_project_userkey_process(self, inputData):
        uid = inputData['uid']
        result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(ownerid=uid)
        user_keylist = []
        if result.exists():
            for line in result:
                keyid = line.keyid
                keyname = line.keyname
                p_code = line.prj_code_id
                temp = {'id': keyid, 'name': keyname, 'domain': p_code}
                user_keylist.append(temp)
        return user_keylist

    def dft_dbi_all_projkey_process(self, inputData):
        uid = inputData['uid']
        all_keylist = []
        projectlist = self.__dft_dbi_get_user_auth_project(uid)
        for projectInfo in projectlist:
            pcode = projectInfo['id']
            result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode)
            if result.exists():
                for line in result:
                    keyid = line.keyid
                    keyname = line.keyname
                    p_code = line.prj_code_id
                    keyusername = line.ownername
                    temp = {
                        'id': keyid, 'name': keyname, 'ProjCode': p_code, 'username': keyusername
                    }
                    all_keylist.append(temp)
        return all_keylist

    def dft_dbi_project_keylist_process(self, inputData):
        pcode = inputData['pcode']
        result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode)
        proj_keylist = []
        if result.exists():
            for line in result:
                keyid = line.keyid
                keyname = line.keyname
                if line.ownername != 'NULL':
                    keyusername = line.ownername
                else:
                    keyusername = '未授予'
                temp = {"id": keyid, 'name': keyname, 'username': keyusername}
                proj_keylist.append(temp)
        return proj_keylist

    def dft_dbi_fhys_projkey_delete(self, inputData):
        pcode = inputData['pcode']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode).delete()
        return True

    def dft_dbi_site_keyauth_delete(self, inputData):
        statCode = inputData['statcode']
        dct_t_l3f2cm_key_auth_fhys.objects.filter(authobj=statCode).delete()
        return True

    def dft_dbi_fhys_deviceinfo_delete(self, inputData):
        devcode = inputData['devcode']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devcode)
        if result.exists():
            for line in result:
                statCode = line.site_code
                status = "I"
                statCode.status = status
                statCode.save()
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devcode).delete()
        return True

    def dft_dbi_all_projkeyuser_process(self, inputData):
        uid = inputData['uid']
        projectlist = self.__dft_dbi_get_user_auth_project(uid)
        all_projuser = []
        for projinfo in projectlist:
            pcode = projinfo['id']
            result = dct_t_l3f1sym_user_right_project.objects.filter(auth_code=pcode)
            if result.exists():
                for line in result:
                    keyuserid = line.uid_id
                    resp = dct_t_l3f1sym_account_secondary.objects.filter(uid_id=keyuserid)
                    if resp.exists():
                        for line in resp:
                            keyusername = line.nick_name
                    temp = {'id': keyuserid, 'name': keyusername, "ProjCode": pcode}
                    all_projuser.append(temp)

        return all_projuser

    def dft_dbi_all_keynum_inquiry(self):
        result = dct_t_l3f2cm_virtual_key_fhys.objects.all()
        return (len(result))

    def dft_dbi_all_keytable_req(self, inputData):
        uid = inputData['uid']
        startseq = inputData['startseq']
        query_length = inputData['query_length']
        keyword = inputData['keyword']
        projectlist = self.__dft_dbi_get_user_auth_project(uid)
        projtotal = len(projectlist)
        if ((startseq <= projtotal) and (startseq + query_length > projtotal)):
            query_length = projtotal - startseq
        elif (startseq > projtotal):
            query_length = 0
        else:
            query_length = projtotal
        keytable = []
        for startseq in range(startseq + query_length):
            pcode = projectlist[startseq]['id']
            projname = projectlist[startseq]['name']
            if keyword != "":
                result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(Q(prj_code_id=pcode), (
                        Q(keyname__icontains=keyword) | Q(ownername__icontains=keyword)))
                if result.exists():
                    for line in result:
                        temp = {'KeyCode': line.keyid,
                                'KeyName': line.keyname,
                                'KeyType': line.keytype,
                                'HardwareCode': line.hwcode,
                                'KeyProj': pcode,
                                'KeyProjName': projname,
                                'KeyUser': line.ownerid,
                                'KeyUserName': line.ownername,
                                'Memo': line.memo
                                }
                        keytable.append(temp)
            else:
                result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode)
                if result.exists():
                    for line in result:
                        temp = {'KeyCode': line.keyid,
                                'KeyName': line.keyname,
                                'KeyType': line.keytype,
                                'HardwareCode': line.hwcode,
                                'KeyProj': pcode,
                                'KeyProjName': projname,
                                'KeyUser': line.ownerid,
                                'KeyUserName': line.ownername,
                                'Memo': line.memo
                                }
                        keytable.append(temp)
        return keytable

    def dft_dbi_key_new_process(self, inputData):
        keyname = inputData['KeyName']
        pcode = inputData['KeyProj']
        keytype = inputData['KeyType']
        hwcode = inputData['HardwareCode']
        memo = inputData['Memo']
        keyid = 'KEY' + self.__dft_getRandomDigID(6)
        keystatus = 'N'
        result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid)
        if result.exists():
            self.dft_dbi_key_new_process(inputData)
        else:
            dct_t_l3f2cm_virtual_key_fhys.objects.create(keyid=keyid, keyname=keyname, prj_code_id=pcode
                                                         , keystatus=keystatus, keytype=keytype, hwcode=hwcode,
                                                         memo=memo)
        return True

    def dft_dbi_key_mod_process(self, inputData):
        keyname = inputData['KeyName']
        pcode = inputData['KeyProj']
        keytype = inputData['KeyType']
        hwcode = inputData['HardwareCode']
        memo = inputData['Memo']
        keyid = inputData['KeyCode']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(keyname=keyname, prj_code_id=pcode
                                                                         , keytype=keytype, hwcode=hwcode, memo=memo)
        return True

    def dft_dbi_key_del_process(self, inputData):
        keyid = inputData['keyid']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).delete()
        return True

    def dft_dbi_obj_authlist_process(self, inputData):
        authobjcode = inputData['authobjcode']
        code_prefix = authobjcode[0:2]
        authlist = []
        result = dct_t_l3f2cm_key_auth_fhys.objects.filter(authobj=int(authobjcode))
        if result.exists():
            for line in result:
                if line.authlevel == "P":
                    department = ""
                    keyname = ""
                    keyuserid = ""
                    keyusername = ""
                    authid = line.sid
                    keyid = line.keyid_id
                    authtype = line.authtype
                    if authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_TIME:
                        authtype = "时间授权"
                    elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER:
                        authtype = "次数授权"
                    elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER:
                        authtype = "永久授权"
                    keyname = line.keyid.keyname
                    keyuserid = line.keyid.ownerid
                    keyusername = line.keyid.ownername
                    resp = dct_t_l3f2cm_project_common.objects.filter(prj_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department = line.department
                    temp = {
                        "AuthId": str(authid),
                        "DomainId": authobjcode,
                        "DomainName": department,
                        "KeyId": keyid,
                        "KeyName": keyname,
                        "UserId": keyuserid,
                        "UserName": keyusername,
                        "AuthWay": authtype,
                    }
                    authlist.append(temp)
                else:
                    department = ""
                    keyname = ""
                    keyuserid = ""
                    keyusername = ""
                    authid = line.sid
                    keyid = line.keyid_id
                    authtype = line.authtype
                    if authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_TIME:
                        authtype = "时间授权"
                    elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER:
                        authtype = "次数授权"
                    elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER:
                        authtype = "永久授权"
                    keyname = line.keyid.keyname
                    keyuserid = line.keyid.ownerid
                    keyusername = line.keyid.ownername
                    resp = dct_t_l3f2cm_site_common.objects.filter(site_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department = line.site_name
                    temp = {
                        "AuthId": str(authid),
                        "DomainId": authobjcode,
                        "DomainName": department,
                        "KeyId": keyid,
                        "KeyName": keyname,
                        "UserId": keyuserid,
                        "UserName": keyusername,
                        "AuthWay": authtype,
                    }
                    authlist.append(temp)
        return authlist

    def dft_dbi_key_authlist_process(self, inputData):
        keyid = inputData['keyid']
        authlist = []
        result = dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid=keyid)
        if result.exists():
            for line in result:
                department = ""
                keyname = ""
                keyuserid = ""
                keyusername = ""
                keylevel = line.authlevel
                authid = line.sid
                authtype = line.authtype
                authobjcode = line.authobj
                if authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_TIME:
                    authtype = "时间授权"
                elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER:
                    authtype = "次数授权"
                elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER:
                    authtype = "永久授权"
                keyname = line.keyid.keyname
                keyuserid = line.keyid.ownerid
                keyusername = line.keyid.ownername
                if keylevel == "P":
                    resp = dct_t_l3f2cm_project_common.objects.filter(prj_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department = line.prj_name
                else:
                    resp = dct_t_l3f2cm_site_common.objects.filter(site_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department = line.site_name
                temp = {"AuthId": str(authid), "DomainId": authobjcode, "DomainName": department, "KeyId": keyid,
                        "KeyName": keyname, "UserId": keyuserid, "UserName": keyusername, "AuthWay": authtype, }
                authlist.append(temp)
        return authlist

    def dft_dbi_key_grant_process(self, inputData):
        keyid = inputData['keyid']
        keyuserid = inputData['keyuserid']
        result = dct_t_l3f1sym_account_primary.objects.filter(uid=keyuserid)
        if result.exists():
            keyusername = result[0].login_name
            dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(ownerid=keyuserid, ownername=keyusername)
        return True

    def dft_dbi_key_authnew_process(self, inputData):
        authobjcode = int(inputData['DomainId'])
        keyid = inputData['KeyId']
        authtype = inputData['Authway']
        if authobjcode < 100000000:
            authlevel = 'P'
        else:
            authlevel = 'D'
        validstart = time.strftime("%Y-%m-%d", time.localtime())
        if authtype == 'always':
            authtype = 'F'
            result = dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid, authobj=authobjcode, authtype=authtype)
            if result.exists():
                pass
            else:
                dct_t_l3f2cm_key_auth_fhys.objects.create(keyid_id=keyid, authlevel=authlevel, authobj=authobjcode,
                                                          authtype=authtype)
        else:
            validend = authtype
            authtype = 'T'
            result = dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid, authobj=authobjcode, authtype=authtype)
            if result.exists():
                dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid, authobj=authobjcode,
                                                          authtype=authtype).update(authlevel=authlevel,
                                                                                    validstart=validstart,
                                                                                    validend=validend)

            else:
                dct_t_l3f2cm_key_auth_fhys.objects.create(keyid_id=keyid, authlevel=authlevel, authobj=authobjcode,
                                                          authtype=authtype, validstart=validstart, validend=validend)
        return True

    def dft_dbi_key_authdel_process(self, inputData):
        authid = inputData['authid']
        dct_t_l3f2cm_key_auth_fhys.objects.filter(sid=authid).delete()
        return True

    '''没表，暂时先不做'''

    def dft_dbi_fhys_get_rtutable_req(self):
        return False

    '''没表，暂时先不做'''

    def dft_dbi_fhys_get_otdrtable_req(self):
        return False

    def dft_dbi_fhyswechat_get_userinfo(self, inputData):
        openid = inputData['openid']
        keytype = self.__MFUN_L3APL_F2CM_KEY_TYPE_WECHAT
        userinfo = []
        result = dct_t_l3f2cm_virtual_key_fhys.objects.filter(hwcode=openid, keytype=keytype)
        if result.exists():
            for line in result:
                keyid = line.keyid
                username = line.ownername
                userid = line.ownerid
                if username != "" and userid != "":
                    userinfo = {'username': username, 'userid': userid, 'wechatid': openid}
                else:
                    memo = "临时微信虚拟钥匙，暂未绑定"
                    keystatus = self.__MFUN_HCU_FHYS_KEY_INVALID
                    dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(keystatus=keystatus, memo=memo)
        return userinfo

    def dft_dbi_fhyswechat_userbind(self, inputData):
        openid = inputData['openid']
        username = inputData['username']
        password = inputData['password']
        mobile = inputData['mobile']
        result = dct_t_l3f1sym_account_primary.objects.filter(login_name=username)
        if result.exists():
            for line in result:
                pwd = line.pass_word
                if pwd == password:
                    userid = line.uid
                    usercheck = True
                    resp = dct_t_l3f1sym_user_right_project.objects.filter(uid_id=userid)
                    projlist = []
                    if resp.exists():
                        for line in resp:
                            authcode = line.auth_code
                            authtype = line.auth_type
                            if authtype == 2:
                                pcode = authcode
                                projlist.append(pcode)
                    msg = '用户验证通过'
                else:
                    msg = '密码错误，请重新输入'
                    usercheck = False
        else:
            msg = '用户不存在，请重新输入'
            usercheck = False
        if usercheck == True and len(projlist) > 0:
            i = 0
            keytype = self.__MFUN_L3APL_F2CM_KEY_TYPE_WECHAT
            keystatus = self.__MFUN_HCU_FHYS_KEY_VALID
            memo = '新建微信虚拟钥匙，请授权'
            while i < len(projlist):
                keyid = "KEY" + self.__dft_getRandomDigID(6)
                keyname = '微信钥匙[' + mobile + ']'
                pcode = projlist[i]
                dct_t_l3f2cm_virtual_key_fhys.objects.create(keyid=keyid, keyname=keyname, prj_code_id=pcode,
                                                             ownerid=userid,
                                                             ownername=username, keystatus=keystatus, keytype=keytype,
                                                             hwcode=openid,
                                                             memo=memo)
                i = i + 1
            msg = '用户微信钥匙绑定成功'
        bindinfo = {'usercheck': usercheck, 'msg': msg, 'username': username, 'userid': userid}
        return bindinfo

    def dft_dbi_HCU_CPU_Query(self, inputData):
        retlist = []
        result = dct_t_l3f2cm_device_holops.objects.all()
        i = 1
        if result.exists():
            for line in result:
                if line.dev_code == None or line.dev_code == "":
                    map = {"cpucode": line.cpu_id, 'cpuname': "CPU[" + line.cpu_id + "]",
                           'cpudetail': "最后一次上报时间：" + str(
                               line.last_update) + "    所属项目信息：" + line.prjname + "    设备信息：" + inputData["key"]}
                    retlist.append(map)
        retval = {
            'status': 'true',
            'auth': 'true',
            'msg': '',
            'ret': retlist,
        }
        return retval

    def dft_dbi_HCU_CPU_Binding(self, inputData):
        dev_code = inputData['code']
        cpu_id = inputData['cpu']
        resp = dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_code)
        if resp.exists():
            resp.update(dev_code=None, valid_flag=0)
            dct_t_l3f2cm_device_holops.objects.filter(cpu_id=cpu_id).update(dev_code=dev_code, valid_flag=True)
            msg = {'status': 'true', 'auth': 'true', 'msg': '重新绑定成功'}
        else:
            dct_t_l3f2cm_device_holops.objects.filter(cpu_id=cpu_id).update(dev_code=dev_code, valid_flag=True)
            msg = {'status': 'true', 'auth': 'true', 'msg': '绑定成功'}
        return msg

    def dft_dbi_HCU_project_list(self):
        projlist = []
        result = dct_t_l3f2cm_project_common.objects.all()
        if result.exists():
            for line in result:
                temp = {'id': line.prj_code, 'name': line.prj_name}
                projlist.append(temp)
        retval = {'status': 'true', 'ret': projlist, 'auth': 'true', 'msg': ''}
        return retval

    def dft_dbi_HCU_Get_Free_Station(self):
        pointtable = []
        result = dct_t_l3f2cm_site_common.objects.all()
        if result.exists():
            for line in result:
                resp = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=line.site_code)
                if resp.exists():
                    pass
                else:
                    temp = {'StatCode': line.site_code,
                            'StatName': line.site_name,
                            'ProjCode': line.prj_code_id,
                            'ChargeMan': line.superintendent,
                            'Telephone': line.telephone,
                            'Longitude': str(line.longitude),
                            'Latitude': str(line.latitude),
                            'Department': line.department,
                            'Address': line.address,
                            'Country': line.district,
                            'Street': line.street,
                            'Square': line.site_area,
                            'ProStartTime': str(line.create_date),
                            'Stage': line.comments,
                            }
                    pointtable.append(temp)
        retval = {'status': 'true', 'ret': pointtable, 'auth': 'true', 'msg': '获取空站点列表成功'}
        return retval

    def dft_dbi_HCU_sys_config(self, inputData):
        dev_code = inputData['code']
        print(dev_code)
        groups = []
        result = dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code)
        if result.exists():
            for line in result:
                if self.__HCU_DUST == True:
                    list = []
                    dust_max = {'paraname': '数据上限', 'type': 'float', 'max': '700', 'min': '10',
                                'value': str(line.dust_coefmax), 'note': "粉尘数据最大值设置"}
                    list.append(dust_max)
                    dust_min = {'paraname': '数据下限', 'type': 'float', 'max': '700', 'min': '10',
                                'value': str(line.dust_coefmin), 'note': "粉尘数据最小值设置"}
                    list.append(dust_min)
                    dust_K = {'paraname': '数据K值', 'type': 'float', 'max': '700', 'min': '',
                              'value': str(line.dust_coefK), 'note': "粉尘数据K值设置"}
                    list.append(dust_K)
                    dust_B = {'paraname': '数据B值', 'type': 'float', 'max': '700', 'min': '',
                              'value': str(line.dust_coefB), 'note': "粉尘数据B值设置"}
                    list.append(dust_B)
                    dust_C = {'paraname': '雾炮门限', 'type': 'float', 'max': '700', 'min': '0',
                              'value': str(line.dust_cannon), 'note': "雾炮门限设置"}
                    list.append(dust_C)
                    dust_group = {'groupname': "粉尘参数设置", 'list': list}
                    groups.append(dust_group)
                if self.__HCU_TEMP == True:
                    list = []
                    temp_max = {'paraname': '数据上限', 'type': 'float', 'max': '100', 'min': '0',
                                'value': str(line.temp_coefmax), 'note': "温度数据最大值设置", }
                    list.append(temp_max)
                    temp_min = {'paraname': '数据下限', 'type': 'float', 'max': '100', 'min': '-40',
                                'value': str(line.temp_coefmin), 'note': "温度数据最小值设置", }
                    list.append(temp_min)
                    temp_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                              'value': str(line.temp_coefK), 'note': "温度数据K值设置", }
                    list.append(temp_K)
                    temp_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                              'value': str(line.temp_coefB), 'note': "温度数据B值设置", }
                    list.append(temp_B)
                    temp_group = {'groupname': "温度参数设置", 'list': list}
                    groups.append(temp_group)
                if self.__HCU_NOISE == True:
                    list = []
                    noise_max = {'paraname': '数据上限', 'type': 'float', 'max': '130', 'min': '30',
                                 'value': str(line.noise_coefmax), 'note': "噪声数据最大值设置", }
                    list.append(noise_max)
                    noise_min = {'paraname': '数据下限', 'type': 'float', 'max': '130', 'min': '30',
                                 'value': str(line.noise_coefmin), 'note': "噪声数据最小值设置", }
                    list.append(noise_min)
                    noise_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                               'value': str(line.noise_coefK), 'note': "噪声数据K值设置", }
                    list.append(noise_K)
                    noise_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                               'value': str(line.noise_coefB), 'note': "噪声数据B值设置", }
                    list.append(noise_B)
                    noise_group = {'groupname': "噪声参数设置", 'list': list}
                    groups.append(noise_group)
                if self.__HCU_HUMID == True:
                    list = []
                    humid_max = {'paraname': '数据上限', 'type': 'float', 'max': '100', 'min': '0',
                                 'value': str(line.humid_coefmax), 'note': "湿度数据最大值设置", }
                    list.append(humid_max)
                    humid_min = {'paraname': '数据下限', 'type': 'float', 'max': '100', 'min': '0',
                                 'value': str(line.humid_coefmin), 'note': "湿度数据最小值设置", }
                    list.append(humid_min)
                    humid_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                               'value': str(line.humid_coefK), 'note': "湿度数据K值设置", }
                    list.append(humid_K)
                    humid_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                               'value': str(line.humid_coefB), 'note': "湿度数据B值设置", }
                    list.append(humid_B)
                    humid_group = {'groupname': "湿度参数设置", 'list': list}
                    groups.append(humid_group)
                if self.__HCU_WINDSPD == True:
                    list = []
                    windspd_max = {'paraname': '数据上限', 'type': 'float', 'max': '1500', 'min': '0',
                                   'value': str(line.windspd_coefmax), 'note': "风速数据最大值设置", }
                    list.append(windspd_max)
                    windspd_min = {'paraname': '数据下限', 'type': 'float', 'max': '1500', 'min': '0',
                                   'value': str(line.windspd_coefmin), 'note': "风速数据最小值设置", }
                    list.append(windspd_min)
                    windspd_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.windspd_coefK), 'note': "风速数据K值设置", }
                    list.append(windspd_K)
                    windspd_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.windspd_coefB), 'note': "风速数据B值设置", }
                    list.append(windspd_B)
                    windspd_group = {'groupname': "风速参数设置", 'list': list}
                    groups.append(windspd_group)
                if self.__HCU_WINDDIR == True:
                    list = []
                    winddir_max = {'paraname': '数据上限', 'type': 'float', 'max': '360', 'min': '0',
                                   'value': str(line.winddir_coefmax), 'note': "风向数据最大值设置", }
                    list.append(winddir_max)
                    winddir_min = {'paraname': '数据下限', 'type': 'float', 'max': '360', 'min': '0',
                                   'value': str(line.winddir_coefmin), 'note': "风向数据最小值设置", }
                    list.append(winddir_min)
                    winddir_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.winddir_coefK), 'note': "风向数据K值设置", }
                    list.append(winddir_K)
                    winddir_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.winddir_coefB), 'note': "风向数据B值设置", }
                    list.append(winddir_B)
                    winddir_delta = {'paraname': '数据θ值', 'type': 'float', 'max': '360', 'min': '0',
                                     'value': str(line.winddir_delta), 'note': "风向数据θ值设置", }
                    list.append(winddir_delta)
                    winddir_group = {'groupname': "风向参数设置", 'list': list}
                    groups.append(winddir_group)
                if self.__HCU_NO2 == True:
                    list = []
                    no2_max = {'paraname': '数据上限', 'type': 'float', 'max': '20', 'min': '0',
                                   'value': str(line.no2_coefmax), 'note': "二氧化氮最大值设置", }
                    list.append(no2_max)
                    no2_min = {'paraname': '数据下限', 'type': 'float', 'max': '0', 'min': '0',
                                   'value': str(line.no2_coefmin), 'note': "二氧化氮最小值设置", }
                    list.append(no2_min)
                    no2_K = {'paraname': '数据K值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.no2_coefK), 'note': "二氧化氮K值设置", }
                    list.append(no2_K)
                    no2_B = {'paraname': '数据B值', 'type': 'float', 'max': '100', 'min': '',
                                 'value': str(line.no2_coefB), 'note': "二氧化氮B值设置", }
                    list.append(no2_B)
                    winddir_group = {'groupname': "二氧化氮参数设置", 'list': list}
                    groups.append(winddir_group)
        ret = {'name': 'configure', 'owner': 'system', 'parameter': {'groups': groups}}
        msg = {'status': 'true', 'auth': 'true', 'ret': ret, 'msg': '获取配置参数成功'}
        return msg

    def dft_dbi_HCU_sys_config_save(self, inputData):
        dev_code = inputData['code']
        data = inputData['configure']['parameter']['groups']
        status = 'false'
        for i in range(len(data)):
            if data[i]['groupname'] == '粉尘参数设置':
                dust_max = data[i]['list'][0]['value']
                dust_min = data[i]['list'][1]['value']
                dust_K = data[i]['list'][2]['value']
                dust_B = data[i]['list'][3]['value']
                dust_C = data[i]['list'][4]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(dust_coefmax=dust_max,
                                                                                     dust_coefmin=dust_min,
                                                                                     dust_coefK=dust_K,
                                                                                     dust_coefB=dust_B,
                                                                                     dust_cannon=dust_C)
                status = 'true'
            elif data[i]['groupname'] == '温度参数设置':
                temp_max = data[i]['list'][0]['value']
                temp_min = data[i]['list'][1]['value']
                temp_K = data[i]['list'][2]['value']
                temp_B = data[i]['list'][3]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(temp_coefmax=temp_max,
                                                                                     temp_coefmin=temp_min,
                                                                                     temp_coefK=temp_K,
                                                                                     temp_coefB=temp_B)
                status = 'true'
            elif data[i]['groupname'] == '噪声参数设置':
                noise_max = data[i]['list'][0]['value']
                noise_min = data[i]['list'][1]['value']
                noise_K = data[i]['list'][2]['value']
                noise_B = data[i]['list'][3]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(noise_coefmax=noise_max,
                                                                                     noise_coefmin=noise_min,
                                                                                     noise_coefK=noise_K,
                                                                                     noise_coefB=noise_B)
                status = 'true'
            elif data[i]['groupname'] == '湿度参数设置':
                humid_max = data[i]['list'][0]['value']
                humid_min = data[i]['list'][1]['value']
                humid_K = data[i]['list'][2]['value']
                humid_B = data[i]['list'][3]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(humid_coefmax=humid_max,
                                                                                     humid_coefmin=humid_min,
                                                                                     humid_coefK=humid_K,
                                                                                     humid_coefB=humid_B)
                status = 'true'
            elif data[i]['groupname'] == '风速参数设置':
                windspd_max = data[i]['list'][0]['value']
                windspd_min = data[i]['list'][1]['value']
                windspd_K = data[i]['list'][2]['value']
                windspd_B = data[i]['list'][3]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(windspd_coefmax=windspd_max,
                                                                                     windspd_coefmin=windspd_min,
                                                                                     windspd_coefK=windspd_K,
                                                                                     windspd_coefB=windspd_B)
                status = 'true'
            elif data[i]['groupname'] == '风向参数设置':
                winddir_max = data[i]['list'][0]['value']
                winddir_min = data[i]['list'][1]['value']
                winddir_K = data[i]['list'][2]['value']
                winddir_B = data[i]['list'][3]['value']
                winddir_delta = data[i]['list'][4]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(winddir_coefmax=winddir_max,
                                                                                     winddir_coefmin=winddir_min,
                                                                                     winddir_coefK=winddir_K,
                                                                                     winddir_coefB=winddir_B,
                                                                                     winddir_delta=winddir_delta)
                status = 'true'
            elif data[i]['groupname'] == '二氧化氮参数设置':
                no2_max = data[i]['list'][0]['value']
                no2_min = data[i]['list'][1]['value']
                no2_K = data[i]['list'][2]['value']
                no2_B = data[i]['list'][3]['value']
                dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=dev_code).update(no2_coefmax=no2_max,
                                                                                     no2_coefmin=no2_min,
                                                                                     no2_coefK=no2_K,
                                                                                     no2_coefB=no2_B)
                status = 'true'
            else:
                status = 'false'
        if status == 'true':
            msg = {'status': status, 'auth': 'true', 'msg': '保存成功'}
        else:
            msg = {'status': status, 'auth': 'true', 'msg': '保存失败'}
        return msg

    def dft_dbi_HCU_Lock_Activate(self, inputData):
        site_code = inputData['StatCode']
        dev_code = inputData['code']
        latitude = inputData['latitude']
        longitude = inputData['longitude']
        result1 = dct_t_l3f2cm_site_common.objects.filter(site_code=site_code)
        result2 = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_code)
        if result1 and result2:
            result1.update(status='A', latitude=latitude, longitude=longitude)
            result2.update(site_code_id=site_code)
            return True
        else:
            return False

    def dft_dbi_get_device_cali(self, inputData):
        devCode = inputData["DevCode"]
        resp = dct_t_l3f2cm_device_cail.objects.filter(dev_code=devCode)
        msg = {}
        if resp.exists():
            for line in resp:
                msg = {
                    "dust_coefmax": line.dust_coefmax,
                    "dust_coefmin": line.dust_coefmin,
                    "dust_coefK": line.dust_coefK,
                    "dust_coefB": line.dust_coefB,
                    "temp_coefmax": line.temp_coefmax,
                    "temp_coefmin": line.temp_coefmin,
                    "temp_coefK": line.temp_coefK,
                    "temp_coefB": line.temp_coefB,
                    "humid_coefmax": line.humid_coefmax,
                    "humid_coefmin": line.humid_coefmin,
                    "humid_coefK": line.humid_coefK,
                    "humid_coefB": line.humid_coefB,
                    "noise_coefmax": line.noise_coefmax,
                    "noise_coefmin": line.noise_coefmin,
                    "noise_coefK": line.noise_coefK,
                    "noise_coefB": line.noise_coefB,
                    "windspd_coefmax": line.windspd_coefmax,
                    "windspd_coefmin": line.windspd_coefmin,
                    "windspd_coefK": line.windspd_coefK,
                    "windspd_coefB": line.windspd_coefB,
                    "winddir_coefmax": line.winddir_coefmax,
                    "winddir_coefmin": line.windspd_coefmin,
                    "winddir_coefK": line.winddir_coefK,
                    "winddir_coefB": line.winddir_coefB,
                    "winddir_delta": line.winddir_delta,
                }
        else:
            msg = {}
        retval = {'status': 'true', 'auth': 'true', 'ret': msg, 'msg': ''}
        return retval

    def dft_dbi_set_device_cali(self, inputData):
        devCode = inputData["DevCode"]
        data = inputData['Calibration']
        result = dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=devCode)
        if result.exists():
            if 'dust_coefmax' in data.keys():
                dust_coefmax = data['dust_coefmax']
            else:
                dust_coefmax = result[0].dust_coefmax
            if 'dust_coefmin' in data.keys():
                dust_coefmin = data['dust_coefmin']
            else:
                dust_coefmin = result[0].dust_coefmin
            if 'dust_coefK' in data.keys():
                dust_coefK = data['dust_coefK']
            else:
                dust_coefK = result[0].dust_coefK
            if 'dust_coefB' in data.keys():
                dust_coefB = data['dust_coefB']
            else:
                dust_coefB = result[0].dust_coefB
            if 'temp_coefmax' in data.keys():
                temp_coefmax = data['temp_coefmax']
            else:
                temp_coefmax = result[0].temp_coefmax
            if 'temp_coefmin' in data.keys():
                temp_coefmin = data['temp_coefmin']
            else:
                temp_coefmin = result[0].temp_coefmin
            if 'temp_coefK' in data.keys():
                temp_coefK = data['temp_coefK']
            else:
                temp_coefK = result[0].temp_coefK
            if 'temp_coefB' in data.keys():
                temp_coefB = data['temp_coefB']
            else:
                temp_coefB = result[0].temp_coefB
            if 'humid_coefmax' in data.keys():
                humid_coefmax = data['humid_coefmax']
            else:
                humid_coefmax = result[0].humid_coefmax
            if 'humid_coefmin' in data.keys():
                humid_coefmin = data['humid_coefmin']
            else:
                humid_coefmin = result[0].humid_coefmin
            if 'humid_coefK' in data.keys():
                humid_coefK = data['humid_coefK']
            else:
                humid_coefK = result[0].humid_coefK
            if 'humid_coefB' in data.keys():
                humid_coefB = data['humid_coefB']
            else:
                humid_coefB = result[0].humid_coefB
            if 'noise_coefmax' in data.keys():
                noise_coefmax = data['noise_coefmax']
            else:
                noise_coefmax = result[0].noise_coefmax
            if 'noise_coefmin' in data.keys():
                noise_coefmin = data['noise_coefmin']
            else:
                noise_coefmin = result[0].noise_coefmin
            if 'noise_coefK' in data.keys():
                noise_coefK = data['noise_coefK']
            else:
                noise_coefK = result[0].noise_coefK
            if 'noise_coefB' in data.keys():
                noise_coefB = data['noise_coefB']
            else:
                noise_coefB = result[0].noise_coefB
            if 'windspd_coefmax' in data.keys():
                windspd_coefmax = data['windspd_coefmax']
            else:
                windspd_coefmax = result[0].windspd_coefmax
            if 'windspd_coefmin' in data.keys():
                windspd_coefmin = data['windspd_coefmin']
            else:
                windspd_coefmin = result[0].windspd_coefmin
            if 'windspd_coefK' in data.keys():
                windspd_coefK = data['windspd_coefK']
            else:
                windspd_coefK = result[0].windspd_coefK
            if 'windspd_coefB' in data.keys():
                windspd_coefB = data['windspd_coefB']
            else:
                windspd_coefB = result[0].windspd_coefB
            if 'winddir_coefmax' in data.keys():
                winddir_coefmax = data['winddir_coefmax']
            else:
                winddir_coefmax = result[0].winddir_coefmax
            if 'winddir_coefmin' in data.keys():
                winddir_coefmin = data['winddir_coefmin']
            else:
                winddir_coefmin = result[0].winddir_coefmin
            if 'winddir_coefK' in data.keys():
                winddir_coefK = data['winddir_coefK']
            else:
                winddir_coefK = result[0].winddir_coefK
            if 'winddir_coefB' in data.keys():
                winddir_coefB = data['winddir_coefB']
            else:
                winddir_coefB = result[0].winddir_coefB
            if 'winddir_delta' in data.keys():
                winddir_delta = data['winddir_delta']
            else:
                winddir_delta = result[0].winddir_delta
            result.update(dust_coefmax=dust_coefmax, dust_coefmin=dust_coefmin, dust_coefK=dust_coefK,
                          dust_coefB=dust_coefB,
                          temp_coefmax=temp_coefmax, temp_coefmin=temp_coefmin, temp_coefK=temp_coefK,
                          temp_coefB=temp_coefB,
                          humid_coefmax=humid_coefmax, humid_coefmin=humid_coefmin, humid_coefK=humid_coefK,
                          humid_coefB=humid_coefB,
                          noise_coefmax=noise_coefmax, noise_coefmin=noise_coefmin, noise_coefK=noise_coefK,
                          noise_coefB=noise_coefB,
                          windspd_coefmax=windspd_coefmax, windspd_coefmin=windspd_coefmin, windspd_coefK=windspd_coefK,
                          windspd_coefB=windspd_coefB,
                          winddir_coefmax=winddir_coefmax, winddir_coefmin=winddir_coefmin, winddir_coefK=winddir_coefK,
                          winddir_coefB=winddir_coefB, winddir_delta=winddir_delta)
            return True
        else:
            return False

    def dft_dbi_hcu_loop_test_view(self, inputData):
        devCode = inputData['code']
        result = dct_t_l3f2cm_device_holops.objects.filter(dev_code=devCode)
        msg = {}
        if result.exists():
            socketID = result[0].socket_id
            if result[0].cmd_flag == GOLBALVAR.HCU_LOOP_TETS_RESP:
                msg = {'status': 'true'}
            else:
                msg = {'status': "pending", 'loop_resp': {'socketid': socketID, 'data':
                    {'ToUsr': devCode, 'FrUsr': "XHTS", "CrTim": int(time.time()),
                     'MsgTp': 'huitp_json', 'MsgId': 0XF041, 'MsgLn': 115,
                     "IeCnt": {"rand": random.randint(10000, 20000)}, "FnFlg": 0}}}
        return msg

    def dft_dbi_hcu_loop_test_start_view(self, inputData):
        devCode = inputData['code']
        dct_t_l3f2cm_device_holops.objects.filter(dev_code=devCode).update(cmd_flag=GOLBALVAR.HCU_LOOP_TETS_REQ)
        msg = {"status": "true", "auth": "true", 'msg': '测试开始'}
        return msg

    def dft_dbi_hcu_reboot(self, inputData):
        devCode = inputData['code']
        req_time = inputData['time']
        result = dct_t_l3f2cm_device_holops.objects.filter(dev_code=devCode)
        if result.exists():
            socketId = result[0].socket_id
            if req_time == 0:
                result.update(cmd_flag=GOLBALVAR.HCU_RESTART_REQ)
            if result[0].cmd_flag == GOLBALVAR.HCU_RESTART_RESP:
                msg = {'status': 'true'}
            else:
                msg = {'status': "pending",
                       'loop_resp': {'socketid': socketId, 'data': {'ToUsr': devCode, 'FrUsr': "XHTS",
                                                                    "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                                                                    'MsgId': 0XF042, 'MsgLn': 115,
                                                                    "IeCnt": {"rand": random.randint(10000, 20000)},
                                                                    "FnFlg": 0}}}
            return msg
        else:
            return False

    def dft_dbi_get_device_detail(self, inputData):
        user_id = inputData['uid']
        dev_array = []
        date_time_now = datetime.datetime.now()
        int_date_time_now = int(time.mktime(date_time_now.timetuple()))
        result = dct_t_l3f1sym_user_right_project.objects.filter(uid_id=user_id)
        project_array = []
        status = 'true'
        userLever = 5
        response_msg = {'status': 'false', 'auth': 'true', 'DevDetail': dev_array, 'UserLever': userLever}
        if result.exists():
            userLever = result[0].uid.grade_level
            for line in result:
                if line.auth_type == 1:
                    resp = dct_t_l3f2cm_project_common.objects.filter(pg_code_id=line.auth_code)
                    if resp.exists():
                        for line_pg in resp:
                            project_array.append(line_pg.prj_code)
                elif line.auth_type == 2:
                    project_array.append(line.auth_code)
                else:
                    pass
        else:
            return response_msg
        dev_code_array = []
        site_name_array = []
        for prj_code in project_array:
            resp_site = dct_t_l3f2cm_site_common.objects.filter(prj_code_id=prj_code)
            if resp_site.exists():
                for line_site in resp_site:
                    statname = line_site.site_name
                    resp_dev = dct_t_l3f2cm_device_inventory.objects.filter(site_code=line_site.site_code)
                    if resp_dev.exists():
                        for line_dev in resp_dev:
                            site_name_array.append(statname)
                            dev_code_array.append(line_dev.dev_code)
                    else:
                        pass
#             else:
# 
#                 return response_msg

        for i in range(len(dev_code_array)):
            resp_dev_data = dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=dev_code_array[i])
            site_name = site_name_array[i]
            if resp_dev_data.exists():
                for line_dev_data in resp_dev_data:
                    last_report = line_dev_data.report_time
                    int_last_report = int(time.mktime(last_report.timetuple()))
                    time_difference = int_date_time_now - int_last_report
                    day_time = int(time_difference / 86400)
                    hour_time = int((time_difference - day_time * 86400) / 3600)
                    min_time = int((time_difference - day_time * 86400 - hour_time * 3600) / 60)
                    senc_time = int(time_difference - day_time * 86400 - hour_time * 3600 - min_time * 60)
                    color = '#00F7DE'
                    if time_difference >= 180:
                        color = "#FFB800"
                    if time_difference >= 3600:
                        color = '#FF5722'
                    last_report = str(day_time) + '天' + str(hour_time) + '时' + str(min_time) + '分' + str(
                        senc_time) + '秒'
                    tsp = int(line_dev_data.tsp)
                    pm01 = round(line_dev_data.pm01, 2)
                    pm25 = round(line_dev_data.pm25, 2)
                    pm10 = round(line_dev_data.pm10, 2)
                    windspd = round(line_dev_data.windspd, 2)
                    noise = round(line_dev_data.noise, 2)
                    winddir = line_dev_data.winddir
                    temp = round(line_dev_data.temperature, 2)
                    humi = round(line_dev_data.humidity, 2)
                    dev_dev = {'DevCode': line_dev_data.dev_code_id, 'StatName': site_name, 'Color': color,
                               'LastReport': last_report, 'TSP': tsp,
                               'PM01': pm01, 'PM25': pm25, 'PM10': pm10, 'Windspd': windspd, 'Noise': noise,
                               'Winddir': winddir, 'Temp': temp, 'Humi': humi}
                    dev_array.append(dev_dev)
        response_msg = {'status': status, 'auth': 'true', 'DevDetail': dev_array, 'UserLever': userLever}
        return response_msg

    def dft_dbi_hcu_get_binding_station_view(self, inputData):
        devCode = inputData['key']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        temp = {}
        if result.exists():
            status = 'true'
            msg = ''
            StationDetail = result[0].site_code
            statcode = StationDetail.site_code
            statname = StationDetail.site_name
            projcode = StationDetail.prj_code_id
            chargeman = StationDetail.superintendent
            telephone = StationDetail.telephone
            longitude = str(StationDetail.longitude)
            latitude = str(StationDetail.latitude)
            department = StationDetail.department
            address = StationDetail.address
            country = StationDetail.district
            street = StationDetail.street
            square = StationDetail.site_area
            prostarttime = str(StationDetail.prj_code.create_date)
            stage = StationDetail.comments
            temp = {'StatCode': statcode, 'StatName': statname, 'ProjCode': projcode, 'ChargeMan': chargeman,
                    'Telephone': telephone, 'Longitude': longitude, 'Latitude': latitude, 'Department': department,
                    'Address': address, 'Country': country, 'Street': street, 'Square': square,
                    'ProStartTime': prostarttime, 'Stage': stage, }
        else:
            status = 'false'
            msg = '错误的设备号'
        retval = {'status': status, 'auth': 'true', 'ret': temp, 'msg': msg}
        return retval

    def dft_dbi_hcu_station_unbind_view(self, inputData):
        devCode = inputData['code']
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).update(site_code_id=None)
        retval = {'status': 'true', 'auth': 'true', 'msg': '解绑成功'}
        return retval

    def dft_dbi_ngrok_reboot(self, inputData):
        devCode = inputData['code']
        req_time = inputData['time']
        result = dct_t_l3f2cm_device_holops.objects.filter(dev_code=devCode)
        if result.exists():
            socketId = result[0].socket_id
            if req_time == 0:
                result.update(cmd_flag=GOLBALVAR.HCU_NGROK_RESTART_REQ)
            if result[0].cmd_flag == GOLBALVAR.HCU_NGROK_RESTART_RESP:
                msg = {'status': 'true'}
            else:
                msg = {'status': "pending",
                       'ngrok_req': {'socketid': socketId, 'data': {'ToUsr': devCode, 'FrUsr': "XHTS",
                                                                    "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                                                                    'MsgId': GOLBALVAR.HUITPJSON_MSGID_NGROKRES_REQ,
                                                                    'MsgLn': 115,
                                                                    "IeCnt": {"rand": random.randint(10000, 20000)},
                                                                    "FnFlg": 0}}}
            return msg
        else:
            return False

    def dft_dbi_sw_restart(self, inputData):
        devCode = inputData['code']
        req_time = inputData['time']
        result = dct_t_l3f2cm_device_holops.objects.filter(dev_code=devCode)
        if result.exists():
            socketId = result[0].socket_id
            if req_time == 0:
                result.update(cmd_flag=GOLBALVAR.HCU_SW_RESTART_REQ)
            if result[0].cmd_flag == GOLBALVAR.HCU_SW_RESTART_RESP:
                msg = {'status': 'true'}
            else:
                msg = {'status': "pending", 'sw_req': {'socketid': socketId, 'data': {'ToUsr': devCode, 'FrUsr': "XHTS",
                                                                                      "CrTim": int(time.time()),
                                                                                      'MsgTp': 'huitp_json',
                                                                                      'MsgId': GOLBALVAR.HUITPJSON_MSGID_SWRESTART_REQ,
                                                                                      'MsgLn': 115,
                                                                                      "IeCnt": {
                                                                                          "rand": random.randint(10000,
                                                                                                                 20000)},
                                                                                      "FnFlg": 0}}}
            return msg
        else:
            return False

    def dft_dbi_point_install_picture_process(self, inputData):
        pic_list = []
        site_code = inputData['StatCode']
        result = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=site_code)
        if result.exists():
            dev_code = result[0].dev_code
        else:
            temp = {'name': '', 'url': ''}
            pic_list.append(temp)
            msg = {"status": "true", "auth": "true", 'pic': pic_list, 'msg': '该站点下没有照片'}
            return msg
        path = self.__MFUN_HCU_AQYC_INSTALL_PICTURE
        path_new = path + dev_code
        print(path_new)
        if os.path.exists(path_new) == False:
            temp = {'name': '', 'url': ''}
            pic_list.append(temp)
            msg = {"status": "true", "auth": "true", 'pic': pic_list, 'msg': '该站点下没有照片'}
            return msg
        for root, dirs, files in os.walk(path_new):
            for file in files:
                print(file)
                if os.path.splitext(file)[1] == '.jpg':
                    name = file
                    url = path_new + "/" + name
                    temp = {'name': name, 'url': self.__MFUN_HCU_AQYC_INSTALL_PICTURE2 + dev_code + "/" + name}
                    pic_list.append(temp)
        msg = {"status": "true", "auth": "true", 'pic': pic_list, 'msg': '获取照片列表成功'}
        return msg

    def dft_dbi_smart_city_ctrl_req(self, inputData):
        cmdTag = inputData['cmdTag']
        site_code = inputData['statCode']
        result = dct_t_l3f2cm_site_fstt.objects.filter(site_code_id=site_code)
        if result.exists():
            resp = dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=site_code)
            if resp.exists():
                dev_code = resp[0].dev_code
                socketID = dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_code)[0].socket_id
                startHour = str(result[0].lamp_start.hour)
                startMin = str(result[0].lamp_start.minute)
                startSec = str(result[0].lamp_start.second)
                stopHour = str(result[0].lamp_stop.hour)
                stopMin = str(result[0].lamp_stop.minute)
                stopSec = str(result[0].lamp_stop.second)
                lightStr = str(result[0].lamp_th)
                lampWorkMode = str(result[0].lamp_mode)
                data = {'cmdTag': cmdTag, 'startHour': startHour, 'startMin': startMin, 'startSec': startSec,
                        'stopHour': stopHour,
                        'stopMin': stopMin, 'stopSec': stopSec, 'lightstrThreadhold': lightStr,
                        'lampWorkMode': lampWorkMode}
                msg = {'status': "pending",
                       'loop_resp': {'socketid': socketID, 'data': {'ToUsr': dev_code, 'FrUsr': "FSTT",
                                                                    "CrTim": int(time.time()), 'MsgTp': 'huitp_json',
                                                                    'MsgId': GOLBALVAR.HUITPJSON_MSGID_SMART_CITY_CTRL_REQ,
                                                                    'MsgLn': 115,
                                                                    "IeCnt": data,
                                                                    "FnFlg": 0}}}
            else:
                return False
        else:
            return False
        return msg

    def dft_dbi_fstt_point_login_view(self, inputData):
        site_code = inputData['StatCode']
        result = dct_t_l3f2cm_favour_site.objects.filter(site_code_id=site_code)
        login_history = []
        if result.exists():
            for line in result:
                name = line.uid.dct_t_l3f1sym_account_secondary.nick_name
                login_time = str(line.create_time)
                temp = {'name': name, 'time': login_time}
                login_history.append(temp)
        return login_history

    def dft_dbi_shyc_old_data_clear(self, inputData):
        delete_days = int(inputData['days'])
        time_now = datetime.datetime.now()
        time_old = time_now - datetime.timedelta(days=delete_days)

    def dft_dbi_faam_old_data_clear(self, inputData):
        pass

    '''内部人员使用的小工具的函数，不需要进行用户的验证，在链接中带有验证信息'''

    def dft_dbi_get_free_cpu_id_internal(self, inputData):
        dev_code = inputData['dev_code']
        cpuArray = []
        result = dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_code)
        if result.exists():
            cpuCode = result[0].cpu_id
            cpuArray.append(cpuCode)
        resp = dct_t_l3f2cm_device_holops.objects.filter(valid_flag=0)
        if resp.exists():
            for line in resp:
                cpuArray.append(line.cpu_id)
        return cpuArray

    def dft_dbi_get_device_detail_internal(self, inputData):
        dev_code = inputData['dev_code']
        hwtype = 0
        valid_flag = 0
        sw_ver = 0
        upgradeflag = 0
        rebootflag = 0
        zhb_label = 0
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_code)
        if result.exists():
            hwtype = result[0].hw_type
            valid_flag = result[0].valid_flag
            sw_ver = result[0].sw_ver
            upgradeflag = result[0].upgradeflag
            rebootflag = result[0].rebootflag
            zhb_label = result[0].zhb_label
        devDetail = {'hwtype': hwtype, 'valid_flag': valid_flag, 'sw_ver': sw_ver, 'upgradeflag': upgradeflag,
                     'rebootflag': rebootflag, 'zhb_label': zhb_label}
        return devDetail

    def dft_dbi_set_device_detail_internal(self, inputData):
        dev_code = inputData['dev_code']
        cpu_code = inputData['cpu_code']
        hwtype = inputData['hwtype']
        valid_flag = inputData['valid_flag']
        sw_ver = inputData['sw_ver']
        upgradeflag = inputData['upgradeflag']
        rebootflag = inputData['rebootflag']
        zhb_label = inputData['zhb_label']
        result = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_code)
        status = 'false'
        msg = '请检查参数是否正确'
        if result.exists():
            resp = dct_t_l3f2cm_device_holops.objects.filter(cpu_id=cpu_code)
            if resp.exists():
                resp_1 = dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_code)
                if resp_1.exists():
                    resp_1.update(dev_code=None, valid_flag=0)
                resp.update(dev_code=dev_code, valid_flag=1)
            result.update(hw_type=hwtype, valid_flag=valid_flag, sw_ver=sw_ver,
                          upgradeflag=upgradeflag, rebootflag=rebootflag, zhb_label=zhb_label)
            status = 'true'
            msg = '修改成功'
        resp_str = {'status': status, 'msg': msg}
        return resp_str

    '''内部人员使用函数的结束标志'''


class HCUReportAndConfirm():

    def __init__(self):
        self.HCU_DEV_STATUS = ""
        self.HCU_DEV_NAME = ""
        self.HCU_REBOOT_STATUS = ""
        self.HCU_REBOOT_NAME = ""
        pass

    def dft_dbi_response_HCU_data(self, socketId, inputData,ipaddr):
        InsertTime = datetime.datetime.now()
        ServerName = inputData["ToUsr"]
        cpuId = inputData['IeCnt']['cpuId']
        prjId = inputData['IeCnt']['prjId']
        prjName = inputData['IeCnt']['prjName']
        dev_Code = inputData['FrUsr']
        if cpuId == "" or cpuId == None:
            return
        result = dct_t_l3f2cm_device_holops.objects.filter(cpu_id=cpuId)
        if result.exists():
            result.update(last_update=datetime.datetime.now(), socket_id=socketId, prjid=prjId, prjname=prjName,ip_addr=ipaddr)
            for line in result:
                if line.valid_flag:
                    resp = dct_t_l3f2cm_device_cail.objects.filter(dev_code_id=line.dev_code)
                    if resp.exists():
                        for line_dev in resp:
                            hwtype = line_dev.dev_code.hw_type
                            ngrokPort = line_dev.dev_code.base_port
                            hcuLable = line_dev.dev_code_id
                            zhbLable = line_dev.dev_code.zhb_label
                            upgradeFlag = line_dev.dev_code.upgradeflag
                            restartRightNow = line_dev.dev_code.rebootflag
                            userName = line_dev.dev_code.username
                            userPswd = line_dev.dev_code.userpswd
                            userDef1 = line_dev.dev_code.userdef1
                            userDef2 = line_dev.dev_code.userdef2
                            userDef3 = line_dev.dev_code.userdef3
                            userDef4 = line_dev.dev_code.userdef4
                            eccPort = line_dev.dev_code.eccport
                            calWinddir = line_dev.winddir_delta
                            calWinddirCoefMax = line_dev.winddir_coefmax
                            calWinddirCoefMin = line_dev.winddir_coefmin
                            calWinddirCoefK = line_dev.winddir_coefK
                            calWinddirCoefB = line_dev.winddir_coefB
                            calPm25CoefMax = line_dev.dust_coefmax
                            calPm25CoefMin = line_dev.dust_coefmin
                            calPm25CoefK = line_dev.dust_coefK
                            calPm25CoefB = line_dev.dust_coefB
                            calPm25ThdCannon = line_dev.dust_cannon
                            calTempCoefMax = line_dev.temp_coefmax
                            calTempCoefMin = line_dev.temp_coefmin
                            calTempCoefK = line_dev.temp_coefK
                            calTempCoefB = line_dev.temp_coefB
                            calHumidCoefMax = line_dev.humid_coefmax
                            calHumidCoefMin = line_dev.humid_coefmin
                            calHumidCoefK = line_dev.humid_coefK
                            calHumidCoefB = line_dev.humid_coefB
                            calWindspdCoefMax = line_dev.windspd_coefmax
                            calWindspdCoefMin = line_dev.windspd_coefmin
                            calWindspdCoefK = line_dev.winddir_coefK
                            calWindspdCoefB = line_dev.windspd_coefB
                            calNoiseCoefMax = line_dev.noise_coefmax
                            calNoiseCoefMin = line_dev.noise_coefmin
                            calNoiseCoefK = line_dev.noise_coefK
                            calNoiseCoefB = line_dev.noise_coefB
                            calNo2CoefMax = line_dev.no2_coefmax
                            calNo2CoefMin = line_dev.no2_coefmin
                            calNo2CoefK = line_dev.no2_coefK
                            calNo2CoefB = line_dev.no2_coefB
                            prescaleXHT = line_dev.dev_code.prescale_xht
                            prescaleCUS = line_dev.dev_code.prescale_cus
                            prescaleOFC = line_dev.dev_code.prescale_ofc
                            ngrokFlag = line_dev.dev_code.port_flag
                            if userName == None: userName = ""
                            if userPswd == None: userPswd = ""
                            if userDef1 == None: userDef1 = ""
                            if userDef2 == None: userDef2 = ""
                            if userDef3 == None: userDef3 = ""
                            if userDef4 == None: userDef4 = ""
                            msgIeCnt = {
                                "htp": hwtype,
                                'npt': ngrokPort,
                                'npf': ngrokFlag,
                                'hlb': hcuLable,
                                'zlb': zhbLable,
                                'ufg': upgradeFlag,
                                'rrn': restartRightNow,
                                'cwd': calWinddir,
                                'p25x': calPm25CoefMax,
                                'p25i': calPm25CoefMin,
                                'p25k': calPm25CoefK,
                                'p25b': calPm25CoefB,
                                'tpx': calTempCoefMax,
                                'tpi': calTempCoefMin,
                                'tpk': calTempCoefK,
                                'tpb': calTempCoefB,
                                'hmx': calHumidCoefMax,
                                'hmi': calHumidCoefMin,
                                'hmk': calHumidCoefK,
                                'hmb': calHumidCoefB,
                                'wdx': calWinddirCoefMax,
                                'wdi': calWinddirCoefMin,
                                'wdk': calWinddirCoefK,
                                'wdb': calWinddirCoefB,
                                'wsx': calWindspdCoefMax,
                                'wsi': calWindspdCoefMin,
                                'wsk': calWindspdCoefK,
                                'wsb': calWindspdCoefB,
                                'nsm': calNoiseCoefMax,
                                'nsi': calNoiseCoefMin,
                                'nsk': calNoiseCoefK,
                                'nsb': calNoiseCoefB,
                                'no2m': calNo2CoefMax,
                                'no2i': calNo2CoefMin,
                                'no2k': calNo2CoefK,
                                'no2b': calNo2CoefB,
                                'ptc': calPm25ThdCannon,
                                #                                 'eda':"",
                                #                                 'eia':"",
                                'ept': eccPort,
                                'psx': prescaleXHT,
                                'psc': prescaleCUS,
                                'pso': prescaleOFC,
                                'un': userName,
                                'up': userPswd,
                                'ud1': userDef1,
                                'ud2': userDef2,
                                'ud3': userDef3,
                                'ud4': userDef4,

                            }
                        msg = {'socketid': socketId,
                               'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                                        'MsgTp': 'huitp_json', 'MsgId': 0XF040, 'MsgLn': 115, "IeCnt": msgIeCnt,
                                        "FnFlg": 0}}
                        msg_len = len(json.dumps(msg))
                        msg_final = {'socketid': socketId,
                                     'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                                              'MsgTp': 'huitp_json', 'MsgId': 0XF040, 'MsgLn': msg_len,
                                              "IeCnt": msgIeCnt, "FnFlg": 0}}
                        return msg_final
                    else:
                        return
                else:
                    return
        else:
            dct_t_l3f2cm_device_holops.objects.create(cpu_id=cpuId, socket_id=socketId, last_update=InsertTime,
                                                      prjid=prjId, prjname=prjName,ip_addr=ipaddr)
            return

    def dft_dbi_device_heart_report(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        ServerName = inputData["ToUsr"]
        dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(last_update=datetime.datetime.now(),
                                                                            socket_id=socketId)
        msg = {'socketid': socketId,
               'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                        'MsgTp': 'huitp_json', 'MsgId': 0X5C7F, 'MsgLn': 115,
                        "IeCnt": {"rand": random.randint(10000, 9999999)}, "FnFlg": 0}}
        msg_len = len(json.dumps(msg))
        msg_final = {'socketid': socketId,
                     'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                              'MsgTp': 'huitp_json', 'MsgId': 0X5C7F, 'MsgLn': msg_len,
                              "IeCnt": {"rand": random.randint(10000, 9999999)},
                              "FnFlg": 0}}
        return msg_final

    def dft_dbi_hcu_loop_test_view(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        rand = inputData['IeCnt']['rand']
        if rand > 0:
            dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(cmd_flag=GOLBALVAR.HCU_LOOP_TETS_RESP)

    def dft_dbi_device_reboot_view(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        rand = inputData['IeCnt']['rand']
        if rand > 0:
            dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(cmd_flag=GOLBALVAR.HCU_RESTART_RESP)

    def dft_dbi_hcu_ngrok_restart_view(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        rand = inputData['IeCnt']['rand']
        if rand > 0:
            dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(
                cmd_flag=GOLBALVAR.HCU_NGROK_RESTART_RESP)

    def dft_dbi_hcu_sw_restart_view(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        rand = inputData['IeCnt']['rand']
        if rand > 0:
            dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(cmd_flag=GOLBALVAR.HCU_SW_RESTART_RESP)

    def dft_dbi_smart_city_ctrl_resp(self, socketId, inputData):
        dev_Code = inputData['FrUsr']
        IeCnt = inputData['IeCnt']
        cmdTag = IeCnt['cmdTag']
        startHour = IeCnt['startHour']
        startMin = IeCnt['startMin']
        startSec = IeCnt['startSec']
        stopHour = IeCnt['stopHour']
        stopMin = IeCnt['stopMin']
        stopSec = IeCnt['stopSec']
        lightStr = IeCnt['lightstrThd']
        lampWorkMode = IeCnt['lampWorkMode']
        startTime = str(startHour) + ":" + str(startMin) + ":" + str(startSec)
        stopTime = str(stopHour) + ":" + str(stopMin) + ":" + str(stopSec)
        result = dct_t_l3f2cm_site_fstt.objects.filter(
            site_code_id=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=dev_Code)[0].site_code)
        if result.exists():
            print("Success Code")
            result.update(lamp_start=startTime, lamp_stop=stopTime, snr_light=lightStr, lamp_mode=lampWorkMode)
        else:
            print("Error Code")

class dct_t_iot_data_report():
    def dft_dbi_nb_iot_curl_token(self,appId,secret,refresh,topken_type):
        print(topken_type)
        if topken_type=="access":
            login_url='https://180.101.147.89:8743/iocm/app/sec/v1.1.0/login'
            login_data = 'appId=' + appId + '&secret=' + secret
        else:
            login_url = 'https://180.101.147.89:8743/iocm/app/sec/v1.1.0/refreshToken'
            data = {"appId":appId,"secret":secret,"refreshToken":refresh}
            login_data=json.dumps(data)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, login_url)
        curl.setopt(pycurl.SSL_VERIFYPEER, False)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.setopt(pycurl.FOLLOWLOCATION, 1)
        curl.setopt(pycurl.AUTOREFERER, 1)
        curl.setopt(pycurl.POST, 1)
        curl.setopt(pycurl.POSTFIELDS, login_data)
        curl.setopt(pycurl.TIMEOUT, 30)
        buf = io.BytesIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.HEADER, 0)
        curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded'])
        curl.setopt(pycurl.SSLCERT, '/var/www/html/outgoing.CertwithKey.pem')
        curl.setopt(pycurl.SSLCERTPASSWD, "IoM@1234")
        curl.perform()
        curlData = json.loads(buf.getvalue(),encoding='utf8')
        curl.close()
        return curlData
    def dft_dbi_nb_iot_data_report_view(self,serviceId,inputData):
        FrUsr = inputData['FrUsr']
        FnFlg=inputData['FnFlg']
        print(serviceId)
        token_expires=dct_t_l3f2cm_nbiot_ctc_token.objects.filter(serviceid=serviceId)
        print(token_expires)
        if token_expires.exists():
            token=token_expires[0].accesstoken
            accexpires=token_expires[0].accexpires
            if(accexpires<datetime.datetime.now()):
                curl_data=self.dft_dbi_nb_iot_curl_token(token_expires[0].appid,token_expires[0].appsecret,"","access")
                accessToken=curl_data['accessToken']
                refreshToken=curl_data['refreshToken']
                expiresIn=int(curl_data['expiresIn'])-300
                time_expires=datetime.datetime.now()+datetime.timedelta(seconds=expiresIn)
                token_expires.update(accesstoken=accessToken,refreshtoken=refreshToken,accexpires=time_expires,refexpires=time_expires)
                pm2d5Value = inputData['IeCnt']['pm2d5Value']
                resp_dev = dct_t_l3f2cm_device_inventory.objects.filter(dev_code=FrUsr)
                if (resp_dev.exists()):
                    dct_t_l3f3dm_current_report_aqyc.objects.create(dev_code_id=FrUsr, pm25=pm2d5Value,
                                                                    site_code_id=resp_dev[0].site_code_id)
                    hourminindex = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
                    dct_t_l3f3dm_minute_report_aqyc.objects.create(dev_code_id=FrUsr, pm25=pm2d5Value,
                                                                   site_code_id=resp_dev[0].site_code_id,
                                                                   hourminindex=hourminindex)
                    # data = self.dft_dbi_get_aqyc_current_report_view(FrUsr)
                    IeCnt={"cfmYesOrNo":1}
                    strLen=len(json.dumps(IeCnt))
                    data={"ToUsr":FrUsr,"FrUsr":"XHTS","CrTim":int(time.time()),"MsgTp":"huitp_json","MsgId":0X5E90,"MsgLn":strLen,"IeCnt":IeCnt,"FnFlg":FnFlg}
                    result = {'result': 'true', 'token': accessToken, 'data': data}
                else:
                    result = {'result': 'false', 'token': token}
            else:
                pm2d5Value=inputData['IeCnt']['pm2d5Value']
                resp_dev=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=FrUsr)
                if(resp_dev.exists()):
                    dct_t_l3f3dm_current_report_aqyc.objects.create(dev_code_id=FrUsr,pm25=pm2d5Value,site_code_id=resp_dev[0].site_code_id)
                    hourminindex = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
                    dct_t_l3f3dm_minute_report_aqyc.objects.create(dev_code_id=FrUsr,pm25=pm2d5Value,site_code_id=resp_dev[0].site_code_id,hourminindex=hourminindex)
                    IeCnt = {"cfmYesOrNo": 1}
                    strLen = len(json.dumps(IeCnt))
                    data = {"ToUsr": FrUsr, "FrUsr": "XHTS", "CrTim": int(time.time()), "MsgTp": "huitp_json",
                            "MsgId": 0X5E90, "MsgLn": strLen, "IeCnt": IeCnt, "FnFlg": FnFlg}
                    result = {'result': 'true', 'token':token,'data':data}
                else:
                    result = {'result': 'false',  'token':token}
        else:
            result={'result':'false', 'token':"信息未找到"}
        return result

    def dft_dbi_get_aqyc_current_report_view(self,dev_code):
        result=dct_t_l3f3dm_current_report_aqyc.objects.filter(dev_code_id=dev_code)
        tsp = 0
        pm01 = 0
        pm25 = 0
        pm10 = 0
        noise = 0
        temperature = 0
        humidity = 0
        winddir = 0
        windspd = 0
        rain = 0
        airpresure = 0
        lightstr = 0
        so2 = 0
        co1 = 0
        no1 = 0
        h2s = 0
        hcho = 0
        toxicgas = 0
        rssi = 0
        pwrind=0
        no2 = 0
        report_date=str(datetime.datetime.now())
        if result.exists():
            for line in result:
                report_date=str(line.report_time)
                tsp=line.tsp
                pm01=line.pm01
                pm25=line.pm25
                pm10=line.pm10
                noise=line.noise
                temperature=line.temperature
                humidity=line.humidity
                winddir=line.winddir
                windspd=line.windspd
                rain=line.rain
                airpresure=line.airpresure
                lightstr=line.lightstr
                so2=line.so2
                co1=line.co1
                no1=line.no1
                h2s=line.h2s
                hcho=line.hcho
                toxicgas=line.toxicgas
                rssi=line.rssi
                pwrind=line.pwrind
                no2=line.no2
        resp_data={'report_time':report_date,
                   'tsp':tsp,
                   'pm01':pm01,
                   'pm25':pm25,
                   'pm10':pm10,
                   'noise':noise,
                   'temperature':temperature,
                   'humidity':humidity,
                   'winddir':winddir,
                   'windspd':windspd,
                   'rain':rain,
                   'airpresure':airpresure,
                   'lightstr':lightstr,
                   'so2':so2,
                   'co1':co1,
                   'no1':no1,
                   'h2s':h2s,
                   'hcho':hcho,
                   'toxicgas':toxicgas,
                   'rssi':rssi,
                   'pwrind':pwrind,
                   'no2':no2,
                   }
        return resp_data