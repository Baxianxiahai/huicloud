# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

@author: Administrator
'''
import sys
import os
import django
sys.path.append('../DjoSiteDba/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjoSiteDba.settings")
#from DjoSiteDba.wsgi import *
django.setup()
from django.db import transaction
from DappDbSnr import views as DappDbSnr
class classDappDbSnr:
    def __init__(self):
        pass
    def dft_aqyc_old_data_clear(self,inputData):
        try:
            with transaction.atomic():
                DappDbSnr_view=DappDbSnr.dct_classDappDbSnr()
                result=DappDbSnr_view.dft_dbi_shyc_old_data_clear(inputData)
                result={'status':'true'}
        except Exception:
            result={'status':'false'}
        return result
