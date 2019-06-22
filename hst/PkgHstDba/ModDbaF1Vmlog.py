# -*- coding: utf-8 -*-
'''
Created on 2019年4月25日

@author: Administrator
'''
import sys
import os
import django
import json
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from DappDbF1vmlog import views as DappDbF1vmlog
from django.db import transaction

class ClassDbaF1vmlog():
    def __init__(self):
        pass
    def dft_dbi_l1comvm_syslog_save_view(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1vmlog_view=DappDbF1vmlog.dct_classDbiL3apF1vmlog()
                result=DappDbF1vmlog_view.dft_dbi_l1comvm_syslog_save_view(inputData)
        except Exception:
            result={"status":'false'}
        return result
    
    def dft_dbi_cron_l1vm_loginfo_cleanup(self,inputData):
        try:
            with transaction.atomic():
                DappDbF1vmlog_view=DappDbF1vmlog.dct_classDbiL3apF1vmlog()
                result=DappDbF1vmlog_view.dft_dbi_cron_l1vm_loginfo_cleanup_view(inputData)
        except Exception:
            result={"status":'false'}
        return result