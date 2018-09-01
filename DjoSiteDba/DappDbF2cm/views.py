from django.shortcuts import render
import random
import time
import datetime
from DappDbF2cm.models import *
from DappDbF1sym.models import *
from DappDbF3dm.models import *
from django.db.models import Q
from DappDbF10oam.models import *
import json

# Create your views here.
class dct_classDbiL3apF2cm:
    __MFUN_L3APL_F2CM_AUTH_TYPE_TIME="T"
    __MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER="N"
    __MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER="F"
    __MFUN_L3APL_F2CM_KEY_TYPE_RFID='R'
    __MFUN_L3APL_F2CM_KEY_TYPE_BLE='B'
    __MFUN_L3APL_F2CM_KEY_TYPE_USER='U'
    __MFUN_L3APL_F2CM_KEY_TYPE_WECHAT='W'
    __MFUN_L3APL_F2CM_KEY_TYPE_IDCARD='I'
    __MFUN_L3APL_F2CM_KEY_TYPE_PHONE='P'
    __MFUN_L3APL_F2CM_KEY_TYPE_UNDEFINED='N'

    __MFUN_HCU_FHYS_KEY_VALID="Y"
    __MFUN_HCU_FHYS_KEY_INVALID="N"


    def __dft_getRandomDigID(self, strlen):
        str_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        uid = ''.join(random.sample(str_array, strlen))
        return uid

    def __dft_dbi_get_user_auth_project(self,inputData):
        uid=inputData
        projlist=[]
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        for line in result:
            auth_code=line.auth_code
            fromat=int(line.auth_type)
            if fromat==2:
                pcode=auth_code
                result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                for line in result:
                    temp={'id':line.prj_code,'name':line.prj_name}
                    projlist.append(temp)
            elif fromat==1:
                pcode=auth_code
                temp=self.dft_dbi_pg_projlist_req(pcode)
                for i in range(len(temp)):
                    projlist.append(temp[i])
        if len(projlist)==0:
            return projlist
        projlist_1=[]
        for i in range(len(projlist)):
            if projlist[i] not in projlist_1:
                projlist_1.append(projlist[i])
        return projlist_1


    def __dft_dbi_get_user_auth_projgroup(self,inputData):
        projectlist=self.__dft_dbi_get_user_auth_project(inputData)
        print(projectlist)
        pg_list=[]
        for i in range(len(projectlist)):
            pcode=projectlist[i]['id']
            result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
            if result.exists():
                for line in result:
                    if line.pg_code!=None:
                        temp={'id':line.pg_code.pg_code,'name':line.pg_code.pg_name}
                        if temp not in pg_list:
                            pg_list.append(temp)
        return pg_list
    def __dft_dbi_get_user_auth_site(self,inputData):
        projectlist=self.__dft_dbi_get_user_auth_project(inputData)
        site_list=[]
        for i in range(len(projectlist)):
            pcode=projectlist[i]['id']
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=pcode)
            for line in result:
                temp={'id':line.site_code,'name':line.site_name,'projcode':line.prj_code_id}
                site_list.append(temp)
        return site_list

    def __dft_dbi_get_user_name(self,inputData):
        uid=inputData
        result=dct_t_l3f1sym_account_secondary.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                name=line.true_name
        else:
            name=uid
        if name=="":
            name=uid
        return name

    def __dft_dbi_get_tower_info(self,inputData):
        result=dct_t_l3f2cm_site_fstt.objects.filter(site_code=inputData)
        tower_info=""
        if result.exists():
            for line in result:
                tower_info=line
        return tower_info

    def __dft_dbi_print_export_usertable(self,inputData):
        column=[]
        data=[]
        column.append('用户ID')
        column.append('用户名')
        column.append('昵称')
        column.append('电话')
        column.append('邮箱')
        column.append('属性')
        column.append('更新日期')
        column.append('备注')

        self_grade=0
        result=dct_t_l3f1sym_account_secondary.objects.filter(uid_id=inputData)
        if result.exists():
            for line in result:
                self_grade=int(line.uid.grade_lever)
                if self_grade==0:grade_name='管理员'
                elif self_grade==1:grade_name='高级用户'
                elif self_grade==2:grade_name='一级用户'
                elif self_grade==3:grade_name='二级用户'
                elif self_grade==4:grade_name='三级用户'
                else:grade_name='用户等级未知'
                temp=[]
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.red_date))
                temp.append(line.uid.backup)
                data.append(temp)
        result=dct_t_l3f1sym_account_secondary.objects.filter(uid__grade_lever__gt=self_grade)
        if result.exists():
            for line in result:
                user=line.uid.login_name
                grade=int(line.uid.grade_lever)
                if grade==0:grade_name='管理员'
                elif grade==1:grade_name='高级用户'
                elif grade==2:grade_name='一级用户'
                elif grade==3:grade_name='二级用户'
                elif grade==4:grade_name='三级用户'
                else:grade_name='用户等级未知'
                temp=[]
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.red_date))
                temp.append(line.uid.backup)
                data.append(temp)
        if user=='admin':
            data=[]
            result=dct_t_l3f1sym_account_secondary.objects.all()
            for line in result:
                grade=int(line.uid.grade_lever)
                if grade==0:grade_name='管理员'
                elif grade==1:grade_name='高级用户'
                elif grade==2:grade_name='一级用户'
                elif grade==3:grade_name='二级用户'
                elif grade==4:grade_name='三级用户'
                else:grade_name='用户等级未知'
                temp = []
                temp.append(line.uid.uid)
                temp.append(line.uid.login_name)
                temp.append(line.nick_name)
                temp.append(line.telephone)
                temp.append(line.uid.email)
                temp.append(grade_name)
                temp.append(str(line.uid.red_date))
                temp.append(line.uid.backup)
                data.append(temp)
        user_table={"data":data,'column':column}
        return user_table
    def __dft_dbi_print_export_pgtable(self,inputData):
        column=[]
        data=[]
        column.append('项目组编号')
        column.append('项目组名称')
        column.append('责任人')
        column.append('电话')
        column.append('所属单位')
        column.append('地址')
        column.append('备注')
        pglist=self.__dft_dbi_get_user_auth_projgroup(inputData)
        for i in range(len(pglist)):
            pgcode=pglist[i]['id']
            result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
            for line in result:
                temp=[]
                temp.append("PG_"+str(line.pg_code))
                temp.append(line.pg_name)
                temp.append(line.superintendent)
                temp.append(line.telephone)
                temp.append(line.department)
                temp.append(line.address)
                temp.append(line.comments)
                data.append(temp)
        pg_table={"column":column,"data":data}
        return pg_table
    def __dft_dbi_print_export_project_table(self,inputData):
        column=[]
        data=[]
        column.append('项目编号')
        column.append('项目名称')
        column.append('负责人')
        column.append('电话')
        column.append('所属单位')
        column.append('地址')
        column.append('备注')
        projectlist=self.__dft_dbi_get_user_auth_project(inputData)
        for i in range(len(projectlist)):
            pcode=projectlist[i]['id']
            result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
            if result.exists():
                for line in result:
                    temp=[]
                    temp.append("P_"+str(line.prj_code))
                    temp.append(line.prj_name)
                    temp.append(line.superintendent)
                    temp.append(line.telephone)
                    temp.append(line.department)
                    temp.append(line.address)
                    temp.append(line.comments)
                    data.append(temp)
        project_table={"column":column,"data":data}
        return project_table
    def __dft_dbi_print_export_site_table(self,inputData):
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
            pcode=projectlist[i]['id']
            result=dct_t_l3f2cm_site_common.objects.filter(prj_code_id=pcode)
            if result.exists():
                for line in result:
                    temp=[]
                    temp.append(line.site_code)
                    temp.append(line.site_name)
                    temp.append(line.superintendent)
                    temp.append(line.telephone)
                    temp.append(line.address)
                    temp.append(line.longitude)
                    temp.append(line.latitude)
                    temp.append(str(line.create_date))
                    temp.append(line.comments)
                    data.append(temp)
        site_table={'column':column,'data':data}
        return site_table
    def __dft_dbi_print_export_devtable(self,inputData):
        column=[]
        data=[]
        column.append('设备编号')
        column.append('站点名称')
        column.append('所属项目')
        column.append('安装时间')
        site_list=self.__dft_dbi_get_user_auth_site(inputData)
        for i in range(len(site_list)):
            statcode=site_list[i]['id']
            result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statcode)
            if result.exists():
                for line in result:
                    devcode=line.dev_code
                    statcode=line.site_code_id
                    starttime=line.create_date
                    result=dct_t_l3f2cm_site_common.objects.filter(site_code=statcode)
                    if result.exists():
                        for line in result:
                            pcode=line.prj_code_id
                            temp=[]
                            temp.append(devcode)
                            temp.append(statcode)
                            temp.append(pcode)
                            temp.append(str(starttime))
                            data.append(temp)
        dev_table={'column':column,'data':data}
        return dev_table
    def dft_dbi_print_excel_table_query_process(self,inputData):
        tablename=inputData['tablename']
        uid=inputData['uid']
        data=[]
        column=[]
        if tablename=='usertable':
            resp = self.__dft_dbi_print_export_usertable(uid)
        elif tablename=='PGtable':
            resp = self.__dft_dbi_print_export_pgtable(uid)
        elif tablename=='Projtable':
            resp = self.__dft_dbi_print_export_project_table(uid)
        elif tablename=='Pointtable':
            resp = self.__dft_dbi_print_export_site_table(uid)
        elif tablename=='Devtable':
            resp = self.__dft_dbi_print_export_devtable(uid)
        else:
            resp={'data':data,'column':column}
        
        return resp

    def dft_dbi_project_number_inquery(self):
        result=dct_t_l3f2cm_project_common.objects.all()
        return len(result)

    def dft_dbi_all_pgnum_inquery(self):
        result = dct_t_l3f2cm_pg_common.objects.all()
        return len(result)

    def dft_dbi_user_pg_table_req(self,inputData):
        uid=inputData['uid']
        startseq=int(inputData['startseq'])
        query_length=int(inputData['query_length'])
        keyword=inputData['keyword']
        pglist=self.__dft_dbi_get_user_auth_projgroup(uid)
        pgtable=[]
        pgtotal=len(pglist)
        print(pglist)
        if (startseq<=pgtotal) and (startseq+query_length>pgtotal):
            query_length=pgtotal-startseq
        elif startseq>pgtotal:
            query_length=0
        for startseq in range(startseq+query_length):
            pgcode=pglist[startseq]['id']
            if keyword=="":
                result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                if result.exists():
                    for line in result:
                        temp={
                            'PGCode':line.pg_code,
                            'PGName':line.pg_name,
                            'ChargeMan':line.superintendent,
                            'Telephone':line.telephone,
                            'Department':line.department,
                            'Address':line.address,
                            'Stage':line.comments
                        }
                        pgtable.append(temp)
            else:
                result = dct_t_l3f2cm_pg_common.objects.filter(Q(pg_code=pgcode),Q(pg_name__icontains=keyword)|Q(superintendent__icontains=keyword)|Q(department__icontains=keyword))
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
    def dft_dbi_all_project_table_req(self,inputData):
        uid=inputData['uid']
        startseq=inputData['startseq']
        query_length=inputData['query_length']
        keyword=inputData['keyword']
        projectList=self.__dft_dbi_get_user_auth_project(uid)
        projectTotal=len(projectList)
        if (startseq<=projectTotal) and (startseq+query_length>projectTotal):
            query_length=projectTotal-startseq
        elif startseq>projectTotal:
            query_length=0
        projectTable=[]
        for startseq in range(startseq+query_length):
            pcode=projectList[startseq]['id']
            if keyword=="":
                result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                if result.exists():
                    for line in result:
                        temp={
                            'ProjCode':line.prj_code,
                            'ProjName':line.prj_name,
                            'ChargeMan':line.superintendent,
                            'Telephone':line.telephone,
                            'Department':line.department,
                            'Address':line.address,
                            'ProStartTime':str(line.create_date),
                            'Stage':line.comments,
                              }
                        projectTable.append(temp)
            else:
                result = dct_t_l3f2cm_project_common.objects.filter(Q(prj_code=pcode), Q(prj_name__icontains=keyword) | Q(superintendent__icontains=keyword) | Q(department__icontains=keyword))
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
        list=[]
        result=dct_t_l3f2cm_pg_common.objects.all()
        if result.exists():
            for line in result:
                temp={'id':line.pg_code,'name':line.pg_name}
                list.append(temp)
        result=dct_t_l3f2cm_project_common.objects.all()
        if result.exists():
            for line in result:
                temp={'id':line.prj_code,'name':line.prj_name}
                list.append(temp)
        return list

    def dft_dbi_user_all_projlist_req(self,inputData):
        uid=inputData['uid']
        list=self.__dft_dbi_get_user_auth_project(uid)
        return list

    def dft_dbi_user_pglist_req(self,inputData):
        uid = inputData['uid']
        pglist=[]
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        if result.exists():
            for line in result:
                authtype=line.auth_type
                authcode=line.auth_code
                if authtype==1:
                    pgcode=authcode
                else:
                    continue
                result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                if result.exists():
                    for line in result:
                        temp={'id':line.pg_code,'name':line.pg_name}
                        pglist.append(temp)
        return pglist

    def dft_dbi_user_projpglist_req(self,inputData):
        uid=inputData['uid']
        table=[]
        result=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=uid)
        if result.exists():
            pgcode=""
            pcode=""
            for line in result:
                if line.auth_type==1:
                    pgcode=line.auth_code
                elif line.auth_type==2:
                    pcode=line.auth_code
                else:
                    continue
                if pgcode!="":
                    result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
                    if result.exists():
                        for line in result:
                            temp={'id':line.pg_code,'name':line.pg_name}
                            table.append(temp)
                if pcode!="":
                    result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
                    if result.exists():
                        for line in result:
                            temp={'id':line.prj_code,'name':line.prj_name}
                            table.append(temp)
        return table

    def dft_dbi_pg_projlist_req(self,inputData):
        pg_code=inputData
        result=dct_t_l3f2cm_project_common.objects.filter(pg_code_id=pg_code)
        projlist=[]
        if result.exists():
            for line in result:
                temp={'id':line.prj_code,'name':line.prj_name}
                projlist.append(temp)
        return projlist

    def dft_dbi_pginfo_new(self,inputData):
        uid=inputData['uid']
        pgname=inputData['PGName']
        owner=inputData['ChargeMan']
        telphone=inputData['Telephone']
        department=inputData['Department']
        addr=inputData['Address']
        strage=inputData['Stage']
        projlist=inputData['Projlist']
        pgcode=self.__dft_getRandomDigID(7)   #为自增长的字段是否还要随机生成?
        result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
        if result.exists():
            self.dft_dbi_pginfo_new(inputData)
        else:
            dct_t_l3f2cm_pg_common.objects.create(pg_code=pgcode,pg_name=pgname,
                                                  pg_creator=uid,superintendent=owner,
                                                  telephone=telphone,department=department,
                                                  address=addr,comments=strage)
        if projlist!=None:
            for i in range(len(projlist)):
                p_code=""
                p_code=projlist[i]['id']
                if p_code!="":
                    dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code).update(pg_code=dct_t_l3f2cm_pg_common.objects.get(pg_code=pgcode))

        dct_t_l3f1sym_user_right_project.objects.create(uid_id=uid,auth_type=1,auth_code=pgcode)
        return True
    def dft_dbi_pginfo_modify(self,inputData):
        pgcode=inputData['PGCode']
        pgname=inputData['PGName']
        owner=inputData['ChargeMan']
        phone=inputData['Telephone']
        department=inputData['Department']
        addr=inputData['Address']
        stage=inputData['Stage']
        projlist=inputData['Projlist']
        result=dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode)
        if result.exists():
            dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode).update(pg_name=pgname,superintendent=owner,telephone=phone,department=department,address=addr,comments=stage)
        if len(projlist)!=0:
            for i in range(len(projlist)):
                p_code=""
                p_code=projlist[i]['id']
                if p_code!="":
                    dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code).update(
                        pg_code=dct_t_l3f2cm_pg_common.objects.get(pg_code=pgcode))
        return True

    def dft_dbi_projinfo_new(self,inputData):
        uid=inputData['uid']
        p_code=self.__dft_getRandomDigID(8)
        pname=inputData['pname']
        chargeman=inputData['chargeman']
        telephone=inputData['telephone']
        department=inputData['department']
        addr=inputData['addr']
        starttime=inputData['starttime']
        stage=inputData['stage']
        result=dct_t_l3f2cm_project_common.objects.filter(prj_code=p_code)
        if result.exists():
            self.dft_dbi_projinfo_new(inputData)
        else:
            dct_t_l3f2cm_project_common.objects.create(prj_code=p_code,prj_name=pname,prj_creator=uid,superintendent=chargeman,telephone=telephone,address=addr,comments=stage,department=department)
        dct_t_l3f1sym_user_right_project.objects.create(auth_type=2,auth_code=p_code,uid=(dct_t_l3f1sym_account_primary.objects.get(uid=uid)))
        return True

    def dft_dbi_projinfo_modify(self,inputData):
        pcode=inputData['ProjCode']
        pname=inputData['ProjName']
        chargeman=inputData['ChargeMan']
        telephone=inputData['Telephone']
        department=inputData['Department']
        addr=inputData['Address']
        starttime=inputData['ProStartTime']
        stage=inputData['Stage']
        result=dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode)
        if result.exists():
            resp=dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)
            resp.prj_name=pname
            resp.superintendent=chargeman
            resp.telephone=telephone
            resp.department=department
            resp.address=addr
            resp.comments=stage
            resp.save()
            # dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode).update(prj_name=pname,superintendent=chargeman,telephone=telephone,department=department,address=addr,comments=stage)
        return True
    def dft_dbi_projinfo_delete(self,inputData):
        pcode=inputData['pcode']
        dct_t_l3f2cm_project_common.objects.filter(prj_code=pcode).delete()
        dct_t_l3f1sym_user_right_project.objects.filter(auth_code=pcode).delete()
        return True
    def dft_dbi_pginfo_delete(self,inputData):
        pgcode=inputData['pgcode']
        dct_t_l3f2cm_pg_common.objects.filter(pg_code=pgcode).delete()
        dct_t_l3f1sym_user_right_project.objects.filter(auth_type=1,auth_code=pgcode).delete()
        return True

    def dft_dbi_all_sitenum_inquery(self):
        result=dct_t_l3f2cm_site_common.objects.all()
        return len(result)

    def dft_dbi_user_all_project_sitelist_req(self,inputData):
        uid=inputData['uid']
        projectlist=self.__dft_dbi_get_user_auth_project(uid)
        sitelist=[]
        for line in projectlist:
            pcode=line['id']
            if pcode!="":
                result=dct_t_l3f2cm_site_common.objects.filter(prj_code=pcode)
                if result.exists():
                    for site in result:
                        temp={'id':site.site_code,'name':site.site_name,'ProjCode':site.prj_code_id}
                        sitelist.append(temp)
        return sitelist

    def dft_dbi_one_proj_sitelist_req(self,inputData):
        pcode=inputData['p_code']
        sitelist=[]
        result=dct_t_l3f2cm_site_common.objects.filter(prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)))
        if result.exists():
            for line in result:
                temp = {'id': line.site_code, 'name': line.site_name, 'ProjCode': line.prj_code_id}
                sitelist.append(temp)
        return sitelist

    def dft_dbi_all_sitetable_req(self,inputData):
        uid=inputData['uid']
        startseq=inputData['startseq']
        query_length=inputData['query_length']
        keyword=inputData['keyword']
        projectlist=self.__dft_dbi_get_user_auth_project(uid)
        projtotal=len(projectlist)
        if (startseq<=projtotal) and (startseq+query_length>projtotal):
            query_length=projtotal-startseq
        elif startseq>projtotal:
            query_length=0
        sitetable=[]
        for i in range(startseq,startseq+query_length):
            pcode=projectlist[i]['id']
            if keyword=="":
                result=dct_t_l3f2cm_site_common.objects.filter(prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode)))
                if result.exists():
                    for line in result:
                        statCode=line.site_code
                        towerInfo=self.__dft_dbi_get_tower_info(statCode)
                        if len(towerInfo)==0:
                            temp={
                                'StatCode':statCode,
                                'StatName':line.site_name,
                                'ProjCode':line.prj_code_id,
                                'ChargeMan':line.superintendent,
                                'Telephone':line.telephone,
                                'Longitude':str(line.longitude),
                                'Latitude':str(line.latitude),
                                'Department':line.department,
                                'Address':line.address,
                                'Country': line.district,
                                'Street': line.street,
                                'Square': line.site_area,
                                'ProStartTime':str(line.create_date),
                                'Stage':line.comments,
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
                                'ProStartTime': line.create_date,
                                'Stage': line.comments,
                                'SN':towerInfo.tower_sn,
                                'PN':towerInfo.tower_code,
                                'Order':towerInfo.order_no,
                                'Model':towerInfo.tower_conf
                            }
                        sitetable.append(temp)
                else:
                    result = dct_t_l3f2cm_site_common.objects.filter(
                        Q(prj_code=(dct_t_l3f2cm_project_common.objects.get(prj_code=pcode))),Q(site_name__icontains=keyword)|Q(address__icontains=keyword))
                    if result.exists():
                        for line in result:
                            statCode = line.site_code
                            towerInfo = self.__dft_dbi_get_tower_info(statCode)
                            if len(towerInfo) == 0:
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
                                    'Model': towerInfo.tower_conf
                                }
                            sitetable.append(temp)
        return sitetable

    def dft_dbi_point_get_activeinfo(self,inputData):
        statCode=inputData['statCode']
        result=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        status=""
        if result.exists():
            for line in result:
                status=line.status
                if status=="C":
                    status='true'
                else:
                    status='false'
        return status

    def dft_dbi_point_set_activeInfo(self,inputData):
        statCode=inputData['statcode']
        status="C"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(status=status)
        return True

    def dft_dbi_siteInfo_new(self,inputData):
        statCode=self.__dft_getRandomDigID(9)
        statname=inputData['StatName']
        pcode=inputData['ProjCode']
        ChargeMan=inputData['ChargeMan']
        Telephone=inputData['Telephone']
        Longitude=inputData['Longitude']
        Latitude=inputData['Latitude']
        Department=inputData['Department']
        Address=inputData['Address']
        Country=inputData['Country']
        Street=inputData['Street']
        Square=inputData['Square']
        ProStartTime=inputData['ProStartTime']
        Stage=inputData['Stage']
        status='I'
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
        if result.exists():
            dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(site_name=statname, status=status,
                                                    prj_code_id=pcode, superintendent=ChargeMan, telephone=Telephone,
                                                    address=Address, longitude=Longitude, latitude=Latitude,
                                                    comments=Stage,department=Department,district=Country,street=Street,site_area=Square,create_date=ProStartTime)
        else:
            dct_t_l3f2cm_site_common.objects.create(site_code=statCode, site_name=statname, status=status,
                                                    prj_code_id=pcode, superintendent=ChargeMan, telephone=Telephone,
                                                    address=Address,comments=Stage,department=Department,district=Country,street=Street,site_area=Square,create_date=ProStartTime)
        return True

    def dft_dbi_siteinfo_modify(self,inputData):
        StatCode=int(inputData['StatCode'])
        StatName=inputData['StatName']
        ProjCode=inputData['ProjCode']
        ChargeMan=inputData['ChargeMan']
        Telephone=inputData['Telephone']
        Longitude=inputData['Longitude']
        Latitude=inputData['Latitude']
        Department=inputData['Department']
        Address=inputData['Address']
        Country=inputData['Country']
        Street=inputData['Street']
        Square=inputData['Square']
        ProStartTime=inputData['ProStartTime']
        Stage=inputData['Stage']
        print(StatCode)
        result = dct_t_l3f2cm_site_common.objects.filter(site_code=StatCode)
        if result.exists():
            dct_t_l3f2cm_site_common.objects.filter(site_code=StatCode).update(site_name=StatName,
                                                                               prj_code_id=ProjCode,
                                                                               superintendent=ChargeMan,
                                                                               telephone=Telephone,
                                                                               address=Address, longitude=Longitude,
                                                                               latitude=Latitude,
                                                                               comments=Stage,department=Department,district=Country,street=Street,site_area=Square,create_date=ProStartTime
                                                                               )
        else:
            self.dft_dbi_siteInfo_new(inputData)
        return True

    def dft_dbi_all_hcutable_req(self,inputData):
        uid=inputData['uid']
        startSeq=inputData['startseq']
        query_length=inputData['query_length']
        keyWord=inputData['keyWord']
        siteList=self.__dft_dbi_get_user_auth_site(uid)
        siteTotal=len(siteList)
        if((startSeq<=siteTotal)and(startSeq+query_length)>siteTotal):
            query_length=siteTotal-startSeq
        elif(startSeq>siteTotal):
            query_length=0
        hcuTable=[]
        for i in range(startSeq+query_length):
            statCode=siteList[i]['id']
            result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
            if result.exists():
                for line in result:
                    devcode=line.dev_code
                    starttime=line.create_date
                    resp=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devcode)
                    if resp.exists():
                        for line in resp:
                            macaddr=line.mac_addr
                            ipaddr=line.ip_addr
                            devstatus='true'
                            url=line.cam_url
                            if keyWord=="":
                                projInfo=dct_t_l3f2cm_site_common.objects.filter(site_code=statCode)
                                projCode=projInfo[0].prj_code_id
                            else:
                                projInfo = dct_t_l3f2cm_site_common.objects.filter(site_code=statCode and ( Q(site_name__icontains=keyWord) or Q(address__icontains=keyWord)))
                                projCode = projInfo[0].prj_code_id
                            temp={
                                'DevCode':devcode,
                                'StatCode':statCode,
                                'ProjCode':projCode,
                                'StartTime':str(starttime),
                                'PreEndTime':"",
                                'EndTime':"",
                                'DevStatus':devstatus,
                                'VideoURL':url,
                                'MAC':macaddr,
                                'IP':ipaddr,
                            }
                            hcuTable.append(temp)            
        return hcuTable

    def dft_dbi_site_devlist_req(self,inputData):
        statCode=inputData['statcode']
        result=dct_t_l3f2cm_device_inventory.objects.filter(site_code_id=statCode)
        devList=[]
        if result.exists():
            for line in result:
                temp={'id':line.site_code_id,'name':line.dev_code}
                devList.append(temp)
        return devList

    def dft_dbi_siteinfo_delete(self,inputData):
        statCode=inputData['statcode']
        result=dct_t_l3f2cm_site_common.objects.filter(site_code =statCode).delete()
        return result

    def dft_dbi_aqyc_deviceinfo_delete(self,inputData):
        devCode=inputData['devcode']
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).delete()
        return True

    def dft_dbi_all_hcunum_inquery(self):
        result=dct_t_l3f2cm_device_inventory.objects.all()
        return len(result)
    def dft_dbi_aqyc_devinfo_update(self,inputData):
        devCode=inputData['DevCode']
        statcode=inputData['StatCode']
        starttime=inputData['StartTime']
        preendtime=inputData['PreEndTime']
        endtime=inputData['EndTime']
        devstatus=inputData['DevStatus']
        videourl=inputData['VideoURL']
        if devstatus=='true':
            devstatus='Y'
        else:
            devstatus='N'
        devCode1=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if devCode1.exists():
            result=dct_t_l3f2cm_device_aqyc.objects.filter(dev_code_id=devCode)
            if result.exists():
                result=dct_t_l3f2cm_device_aqyc.objects.get(dev_code_id=devCode)
                result.dev_code.create_date=starttime
                result.dev_code.site_code_id=statcode
                result.status=devCode
                result.cam_url=videourl
                result.save()
        else:
            dct_t_l3f2cm_device_inventory.objects.create(dev_code=devCode,site_code_id=statcode,create_date=starttime)
            dct_t_l3f2cm_device_aqyc.objects.create(dev_code_id=devCode,status=devstatus,cam_url=videourl)
        status="C"
        print(statcode)
        print(status)
        dct_t_l3f2cm_site_common.objects.filter(site_code=statcode).update(status=status)
        return True

    def dft_dbi_qrcode_scan_newcode_check(self,inputData):
        devCode=inputData['devcode']
        validFlag="Y"
        timestamp=int(time.time())
        timeStamp=time.localtime(timestamp)
        valiDate=time.strftime("%Y-%m-%d",timeStamp)
        result=dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode)
        if result.exists():
            dct_t_l3f10oam_qrcodeinfo.objects.filter(dev_code=devCode).update(validflag=validFlag,validdate=valiDate)
            return True
        else:
            return False

    def dft_dbi_qrcode_scan_newcode_add(self,inputData):
        devCode=inputData['devcode']
        statCode=inputData['statcode']
        latitude=inputData['latitude']
        longitude=inputData['longitude']
        timestamp = int(time.time())
        timeStamp = time.localtime(timestamp)
        openDate = time.strftime("%Y-%m-%d", timeStamp)
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode).update(site_code_id=statCode,create_date=openDate)
        else:
            dct_t_l3f2cm_device_inventory.objects.create(dev_code=devCode,site_code_id=statCode,create_date=openDate)
        status="A"
        dct_t_l3f2cm_site_common.objects.filter(site_code=statCode).update(status=status,latitude=latitude,longitude=longitude)
        return True

    def dft_dbi_qrcode_scan_free_projsite_inquery(self):
        status="C"
        sitetable=[]
        projtable=[]
        result=dct_t_l3f2cm_site_common.objects.filter(~Q(status=status))
        if result.exists():
            for line in result:
                temp={
                    'StatCode':line.site_code,
                    'StatName':line.site_name,
                    'ProjCode':line.prj_code_id,
                    'ChargeMan':line.superintendent,
                    'Telephone':line.telephone,
                    'Longitude':line.longitude,
                    'Latitude':line.latitude,
                    'Department':line.department,
                    'Address':line.address,
                    'Country':line.district,
                    'Street':line.street,
                    'Square':line.site_area,
                    'ProStartTime':line.create_date,
                    'Stage':line.comments,
                }
                sitetable.append(temp)
                id=line.prj_code.prj_code
                name=line.prj_code.prj_name
                temp={"id":id,'name':name}
                projtable.append(temp)
        resp={'site_list':sitetable,'proj_list':projtable}
        return resp

    def dft_dbi_aqyc_qrcode_scan_siteinfo_update_gps(self,inputData):
        devCode=inputData['devcode']
        latitude=inputData['latitude']
        longitude=inputData['longitude']
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devCode)
        if result.exists():
            for line in result:
                statCode=line.site_code
                statCode.latitude=latitude
                statCode.longitude=longitude
                statCode.save(update_fields=['latitude','longitude'])
        return True

    def dft_dbi_fstt_point_config_query(self,inputData):
        statCode=inputData['statCode']
        confList=[]
        if statCode=='S_48071851':
            temp={'id':'1','name':'摄像头'}
            confList.append(temp)
            temp = {'id': '2', 'name': '温度传感器'}
            confList.append(temp)
            temp = {'id': '3', 'name': '湿度传感器'}
            confList.append(temp)
        elif statCode=='S_49950094':
            temp = {'id': '1', 'name': '摄像头'}
            confList.append(temp)
            temp = {'id': '2', 'name': '粉尘传感器'}
            confList.append(temp)
            temp = {'id': '3', 'name': '风向传感器'}
            confList.append(temp)
            temp={'id':'4','name':'风速传感器'}
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
    def dft_dbi_fstt_point_login_history(self,inputData):
        statCode=inputData['statCode']
        loginHistory=[]
        result=dct_t_l3f2cm_favour_site.objects.filter(site_code_id=statCode)
        if result.exists():
            uid=result[0].uid_id
            name=self.__dft_dbi_get_user_name(uid)
            loginTime=result[0].create_time
            temp={'name':name,'time':loginTime}
            loginHistory.append(temp)
        return loginHistory

    def dft_dbi_project_userkey_process(self,inputData):
        uid=inputData['uid']
        result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(ownerid=uid)
        user_keylist=[]
        if result.exists():
            for line in result:
                keyid=line.keyid
                keyname=line.keyname
                p_code=line.prj_code_id
                temp={'id':keyid,'name':keyname,'domain':p_code}
                user_keylist.append(temp)
        return user_keylist

    def dft_dbi_all_projkey_process(self,inputData):
        uid=inputData['uid']
        all_keylist=[]
        projectlist=self.__dft_dbi_get_user_auth_project(uid)
        for projectInfo in projectlist:
            pcode=projectInfo['id']
            result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode)
            if result.exists():
                for line in result:
                    keyid=line.keyid
                    keyname=line.keyname
                    p_code=line.prj_code_id
                    keyusername=line.ownername
                    temp={
                        'id':keyid,'name':keyname,'ProjCode':p_code,'username':keyusername
                    }
                    all_keylist.append(temp)
        return all_keylist

    def dft_dbi_project_keylist_process(self,inputData):
        pcode=inputData['pcode']
        result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode)
        proj_keylist=[]
        if result.exists():
            for line in result:
                keyid=line.keyid
                keyname=line.keyname
                if line.ownername!='NULL':
                    keyusername=line.ownername
                else:
                    keyusername='未授予'
                temp={"id":keyid,'name':keyname,'username':keyusername}
                proj_keylist.append(temp)
        return proj_keylist

    def dft_dbi_fhys_projkey_delete(self,inputData):
        pcode=inputData['pcode']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(prj_code_id=pcode).delete()
        return True

    def dft_dbi_site_keyauth_delete(self,inputData):
        statCode=inputData['statcode']
        dct_t_l3f2cm_key_auth_fhys.objects.filter(authobj=statCode).delete()
        return True

    def dft_dbi_fhys_deviceinfo_delete(self,inputData):
        devcode=inputData['devcode']
        result=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devcode)
        if result.exists():
            for line in result:
                statCode=line.site_code
                status="I"
                statCode.status=status
                statCode.save()
        dct_t_l3f2cm_device_inventory.objects.filter(dev_code=devcode).delete()
        return True

    def dft_dbi_all_projkeyuser_process(self,inputData):
        uid=inputData['uid']
        projectlist=self.__dft_dbi_get_user_auth_project(uid)
        all_projuser=[]
        for projinfo in projectlist:
            pcode=projinfo['id']
            result=dct_t_l3f1sym_user_right_project.objects.filter(auth_code=pcode)
            if result.exists():
                for line in result:
                    keyuserid=line.uid_id
                    resp=dct_t_l3f1sym_account_secondary.objects.filter(uid_id=keyuserid)
                    if resp.exists():
                        for line in resp:
                            keyusername=line.nick_name
                    temp={'id':keyuserid,'name':keyusername,"ProjCode":pcode}
                    all_projuser.append(temp)

        return all_projuser

    def dft_dbi_all_keynum_inquiry(self):
        result=dct_t_l3f2cm_virtual_key_fhys.objects.all()
        return (len(result))

    def dft_dbi_all_keytable_req(self,inputData):
        uid=inputData['uid']
        startseq=inputData['startseq']
        query_length=inputData['query_length']
        keyword=inputData['keyword']
        projectlist=self.__dft_dbi_get_user_auth_project(uid)
        projtotal=len(projectlist)
        if ((startseq<=projtotal)and(startseq+query_length>projtotal)):
            query_length=projtotal-startseq
        elif(startseq>projtotal):
            query_length=0
        else:
            query_length=projtotal
        keytable=[]
        for startseq in range(startseq+query_length):
            pcode=projectlist[startseq]['id']
            projname=projectlist[startseq]['name']
            if keyword!="":
                result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(Q(prj_code_id=pcode),(Q(keyname__icontains=keyword) | Q(ownername__icontains=keyword)))
                if result.exists():
                    for line in result:
                        temp={'KeyCode':line.keyid,
                              'KeyName':line.keyname,
                              'KeyType':line.keytype,
                              'HardwareCode':line.hwcode,
                              'KeyProj':pcode,
                              'KeyProjName':projname,
                              'KeyUser':line.ownerid,
                              'KeyUserName':line.ownername,
                              'Memo':line.memo
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

    def dft_dbi_key_new_process(self,inputData):
        keyname=inputData['KeyName']
        pcode=inputData['KeyProj']
        keytype=inputData['KeyType']
        hwcode=inputData['HardwareCode']
        memo=inputData['Memo']
        keyid='KEY'+self.__dft_getRandomDigID(6)
        keystatus='N'
        result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid)
        if result.exists():
            self.dft_dbi_key_new_process(inputData)
        else:
            dct_t_l3f2cm_virtual_key_fhys.objects.create(keyid=keyid,keyname=keyname,prj_code_id=pcode
                                                         ,keystatus=keystatus,keytype=keytype,hwcode=hwcode,
                                                         memo=memo)
        return True
    def dft_dbi_key_mod_process(self,inputData):
        keyname=inputData['KeyName']
        pcode=inputData['KeyProj']
        keytype=inputData['KeyType']
        hwcode=inputData['HardwareCode']
        memo=inputData['Memo']
        keyid=inputData['KeyCode']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(keyname=keyname,prj_code_id=pcode
                                                         ,keytype=keytype,hwcode=hwcode,memo=memo)
        return True

    def dft_dbi_key_del_process(self,inputData):
        keyid=inputData['keyid']
        dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).delete()
        return True

    def dft_dbi_obj_authlist_process(self,inputData):
        authobjcode=inputData['authobjcode']
        code_prefix=authobjcode[0:2]
        authlist=[]
        result=dct_t_l3f2cm_key_auth_fhys.objects.filter(authobj=int(authobjcode))
        if result.exists():
            for line in result:
                if line.authlevel=="P":
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
    def dft_dbi_key_authlist_process(self,inputData):
        keyid=inputData['keyid']
        authlist=[]
        result=dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid=keyid)
        if result.exists():
            for line in result:
                department=""
                keyname=""
                keyuserid=""
                keyusername=""
                keylevel=line.authlevel
                authid=line.sid
                authtype=line.authtype
                authobjcode=line.authobj
                if authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_TIME:
                    authtype = "时间授权"
                elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_NUMBER:
                    authtype = "次数授权"
                elif authtype == self.__MFUN_L3APL_F2CM_AUTH_TYPE_FOREVER:
                    authtype = "永久授权"
                keyname=line.keyid.keyname
                keyuserid=line.keyid.ownerid
                keyusername=line.keyid.ownername
                if keylevel=="P":
                    resp=dct_t_l3f2cm_project_common.objects.filter(prj_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department=line.prj_name
                else:
                    resp = dct_t_l3f2cm_site_common.objects.filter(site_code=authobjcode)
                    if resp.exists():
                        for line in resp:
                            department = line.site_name
                temp={"AuthId":str(authid),"DomainId":authobjcode,"DomainName":department,"KeyId":keyid,"KeyName":keyname,"UserId":keyuserid,"UserName":keyusername,"AuthWay":authtype,}
                authlist.append(temp)
        return authlist


    def dft_dbi_key_grant_process(self,inputData):
        keyid=inputData['keyid']
        keyuserid=inputData['keyuserid']
        result=dct_t_l3f1sym_account_primary.objects.filter(uid=keyuserid)
        if result.exists():
            keyusername=result[0].login_name
            dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(ownerid=keyuserid,ownername=keyusername)
        return True

    def dft_dbi_key_authnew_process(self,inputData):
        authobjcode=int(inputData['DomainId'])
        keyid=inputData['KeyId']
        authtype=inputData['Authway']
        if authobjcode<100000000:
            authlevel='P'
        else:
            authlevel='D'
        validstart=time.strftime("%Y-%m-%d", time.localtime())
        if authtype=='always':
            authtype='F'
            result=dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid,authobj=authobjcode,authtype=authtype)
            if result.exists():
                pass
            else:
                dct_t_l3f2cm_key_auth_fhys.objects.create(keyid_id=keyid,authlevel=authlevel,authobj=authobjcode,authtype=authtype)
        else:
            validend=authtype
            authtype='T'
            result = dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid, authobj=authobjcode, authtype=authtype)
            if result.exists():
                dct_t_l3f2cm_key_auth_fhys.objects.filter(keyid_id=keyid, authobj=authobjcode, authtype=authtype).update(authlevel=authlevel,validstart=validstart,validend=validend)

            else:
                dct_t_l3f2cm_key_auth_fhys.objects.create(keyid_id=keyid, authlevel=authlevel, authobj=authobjcode,
                                                          authtype=authtype,validstart=validstart,validend=validend)
        return True
    def dft_dbi_key_authdel_process(self,inputData):
        authid=inputData['authid']
        dct_t_l3f2cm_key_auth_fhys.objects.filter(sid=authid).delete()
        return True
    '''没表，暂时先不做'''
    def dft_dbi_fhys_get_rtutable_req(self):
        return False

    '''没表，暂时先不做'''

    def dft_dbi_fhys_get_otdrtable_req(self):
        return False

    def dft_dbi_fhyswechat_get_userinfo(self,inputData):
        openid=inputData['openid']
        keytype=self.__MFUN_L3APL_F2CM_KEY_TYPE_WECHAT
        userinfo=[]
        result=dct_t_l3f2cm_virtual_key_fhys.objects.filter(hwcode=openid,keytype=keytype)
        if result.exists():
            for line in result:
                keyid=line.keyid
                username=line.ownername
                userid=line.ownerid
                if username!="" and userid!="":
                    userinfo={'username':username,'userid':userid,'wechatid':openid}
                else:
                    memo="临时微信虚拟钥匙，暂未绑定"
                    keystatus=self.__MFUN_HCU_FHYS_KEY_INVALID
                    dct_t_l3f2cm_virtual_key_fhys.objects.filter(keyid=keyid).update(keystatus=keystatus,memo=memo)
        return userinfo

    def dft_dbi_fhyswechat_userbind(self,inputData):
        openid=inputData['openid']
        username=inputData['username']
        password=inputData['password']
        mobile=inputData['mobile']
        result=dct_t_l3f1sym_account_primary.objects.filter(login_name=username)
        if result.exists():
            for line in result:
                pwd=line.pass_word
                if pwd==password:
                    userid=line.uid
                    usercheck=True
                    resp=dct_t_l3f1sym_user_right_project.objects.filter(uid_id=userid)
                    projlist=[]
                    if resp.exists():
                        for line in resp:
                            authcode=line.auth_code
                            authtype=line.auth_type
                            if authtype==2:
                                pcode=authcode
                                projlist.append(pcode)
                    msg='用户验证通过'
                else:
                    msg='密码错误，请重新输入'
                    usercheck=False
        else:
            msg='用户不存在，请重新输入'
            usercheck=False
        if usercheck==True and len(projlist)>0:
            i=0
            keytype=self.__MFUN_L3APL_F2CM_KEY_TYPE_WECHAT
            keystatus=self.__MFUN_HCU_FHYS_KEY_VALID
            memo='新建微信虚拟钥匙，请授权'
            while i<len(projlist):
                keyid="KEY"+self.__dft_getRandomDigID(6)
                keyname='微信钥匙['+mobile+']'
                pcode=projlist[i]
                dct_t_l3f2cm_virtual_key_fhys.objects.create(keyid=keyid,keyname=keyname,prj_code_id=pcode,ownerid=userid,
                                                             ownername=username,keystatus=keystatus,keytype=keytype,hwcode=openid,
                                                             memo=memo)
                i=i+1
            msg='用户微信钥匙绑定成功'
        bindinfo={'usercheck':usercheck,'msg':msg,'username':username,'userid':userid}
        return bindinfo


class HCUReportAndConfirm():
    def __init__(self):
        pass
    def dft_dbi_response_HCU_data(self,socketId,inputData):
        InsertTime=datetime.datetime.now()
        ServerName=inputData["ToUsr"]
        cpuId=inputData['IeCnt']['cpuId']
        dev_Code = inputData['FrUsr']
        if cpuId=="" or cpuId==None:
            return
        result=dct_t_l3f2cm_device_holops.objects.filter(cpu_id=cpuId)
        if result.exists():
            result.update(last_update=datetime.datetime.now(),socket_id=socketId)
            for line in result:
                if line.valid_flag:
                    resp=dct_t_l3f2cm_device_inventory.objects.filter(dev_code=line.dev_code)
                    if resp.exists():
                        for line_dev in resp:
                            hwtype=line_dev.hw_type
                            ngrokPort=line_dev.base_port
                            hcuLable=line_dev.dev_code
                            zhbLable=line_dev.zhb_label
                            upgradeFlag=line_dev.upgradeflag
                            restartRightNow=line_dev.rebootflag
                            calWinddir=line_dev.winddir_delta
                            calWinddirCoefMax=line_dev.winddir_coefmax
                            calWinddirCoefMin=line_dev.winddir_coefmin
                            calWinddirCoefK=line_dev.winddir_coefK
                            calWinddirCoefB=line_dev.winddir_coefB
                            calPm25CoefMax=line_dev.dust_coefmax
                            calPm25CoefMin=line_dev.dust_coefmin
                            calPm25CoefK=line_dev.dust_coefK
                            calPm25CoefB=line_dev.dust_coefB
                            dust_threshold=line_dev.dust_threshold
                            calTempCoefMax=line_dev.temp_coefmax
                            calTempCoefMin=line_dev.temp_coefmin
                            calTempCoefK=line_dev.temp_coefK
                            calTempCoefB=line_dev.temp_coefB
                            calHumidCoefMax=line_dev.humid_coefmax
                            calHumidCoefMin=line_dev.humid_coefmin
                            calHumidCoefK=line_dev.humid_coefK
                            calHumidCoefB=line_dev.humid_coefB
                            calWindspdCoefMax=line_dev.windspd_coefmax
                            calWindspdCoefMin=line_dev.windspd_coefmin
                            calWindspdCoefK=line_dev.winddir_coefK
                            calWindspdCoefB=line_dev.windspd_coefB
                            calNoiseCoefMax=line_dev.noise_coefmax
                            calNoiseCoefMin=line_dev.noise_coefmin
                            calNoiseCoefK=line_dev.noise_coefK
                            calNoiseCoefB=line_dev.noise_coefB
                            msgIeCnt = {
                                "hwType": hwtype,
                                'ngrokPort': ngrokPort,
                                'hcuLable': hcuLable,
                                'zhbLable': zhbLable,
                                'upgradeFlag': upgradeFlag,
                                'restartRightNow': restartRightNow,
                                'calWinddir': calWinddir,
                                'calPm25CoefMax': calPm25CoefMax,
                                'calPm25CoefMin': calPm25CoefMin,
                                'calPm25CoefK': calPm25CoefK,
                                'calPm25CoefB': calPm25CoefB,
                                'calPm25ThdCannon':dust_threshold,
                                'calTempCoefMax': calTempCoefMax,
                                'calTempCoefMin': calTempCoefMin,
                                'calTempCoefK': calTempCoefK,
                                'calTempCoefB': calTempCoefB,
                                'calHumidCoefMax': calHumidCoefMax,
                                'calHumidCoefMin': calHumidCoefMin,
                                'calHumidCoefK': calHumidCoefK,
                                'calHumidCoefB': calHumidCoefB,
                                'calWinddirCoefMax': calWinddirCoefMax,
                                'calWinddirCoefMin': calWinddirCoefMin,
                                'calWinddirCoefK': calWinddirCoefK,
                                'calWinddirCoefB': calWinddirCoefB,
                                'calWindspdCoefMax': calWindspdCoefMax,
                                'calWindspdCoefMin': calWindspdCoefMin,
                                'calWindspdCoefK': calWindspdCoefK,
                                'calWindspdCoefB': calWindspdCoefB,
                                'calNoiseCoefMax': calNoiseCoefMax,
                                'calNoiseCoefMin': calNoiseCoefMin,
                                'calNoiseCoefK': calNoiseCoefK,
                                'calNoiseCoefB': calNoiseCoefB,
                            }
                            msg={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':115,"IeCnt":msgIeCnt,"FnFlg":0}}
                            msg_len=len(json.dumps(msg))
                            msg_final={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':msg_len,"IeCnt":msgIeCnt,"FnFlg":0}}
                            return msg_final
                    else:
                        msg={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':115,"IeCnt":{},"FnFlg":0}}
                        msg_len=len(json.dumps(msg))
                        msg_final={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':msg_len,"IeCnt":{},"FnFlg":0}}
                        return msg_final
                    
                else:
                    msg={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':115,"IeCnt":{},"FnFlg":0}}
                    msg_len=len(json.dumps(msg))
                    msg_final={'socketid':socketId,'data':{'ToUsr':dev_Code,'FrUsr':ServerName,"CrTim":int(time.time()),'MsgTp':'huitp_json','MsgId':0XF040,'MsgLn':msg_len,"IeCnt":{},"FnFlg":0}}
                    return msg_final   
        else:
            dct_t_l3f2cm_device_holops.objects.create(cpu_id=cpuId,socket_id=socketId,last_update=InsertTime)
            return False
        
    def dft_dbi_device_heart_report(self,socketId,inputData):
        dev_Code = inputData['FrUsr']
        ServerName = inputData["ToUsr"]
        dct_t_l3f2cm_device_holops.objects.filter(dev_code=dev_Code).update(last_update=datetime.datetime.now(),socket_id=socketId)
        msg = {'socketid': socketId,
               'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                        'MsgTp': 'huitp_json', 'MsgId': 0X5C7F, 'MsgLn': 115, "IeCnt": {"rand":random.randint(10000,9999999)}, "FnFlg": 0}}
        msg_len = len(json.dumps(msg))
        msg_final = {'socketid': socketId,
                     'data': {'ToUsr': dev_Code, 'FrUsr': ServerName, "CrTim": int(time.time()),
                              'MsgTp': 'huitp_json', 'MsgId': 0X5C7F, 'MsgLn': msg_len, "IeCnt": {"rand":random.randint(10000,9999999)},
                              "FnFlg": 0}}
        return msg_final
        














