from django.shortcuts import render
from DappDbF1vmlog.models import *
# from django.db.models import Max


# Create your views here.
class dct_classDbiL3apF1vmlog:
    __MFUN_L1VM_DBI_MAX_LOG_NUM = 10000

    def __init__(self):
        pass

    def dft_dbi_l1comvm_syslog_save_view(self, inputData):
        sysVer = inputData["sysver"]
        sysprog = inputData["sysprog"]
        project = inputData["project"]
        fromuser = inputData["fromuser"]
        srcname = inputData["srcname"]
        destname = inputData["destname"]
        msgid = inputData["msgid"]
        logtime = inputData["logtime"]
        logdata = inputData["logdata"]
        dct_t_l3f1vm_loginfo.objects.create(sysver=sysVer, sysprj=project, fromuser=fromuser, syspgm=sysprog,
                                            srcname=srcname, destname=destname, msgid=msgid, logtime=logtime,
                                            logdata=logdata
                                            )
        resp = {'status': 'true'}
        return resp
    
    def dft_dbi_cron_l1vm_loginfo_cleanup_view(self, inputData):
        result = dct_t_l3f1vm_loginfo.objects.last()
        dct_t_l3f1vm_loginfo.objects.filter(sid__lte=result.sid - self.__MFUN_L1VM_DBI_MAX_LOG_NUM).delete()
        resp = {'status': 'true'}
        return resp
