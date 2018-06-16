# -*- coding: utf-8 -*-
import os
import hashlib
os.environ['DJANGO_SETTINGS_MODULE']='xhzn_db_new.settings'
import django
django.setup()
import json
from xhzn.models import t_l3f1sym_menu_code_mapping as menu
def Hello_world():
    print("HELLO WORLD")
def aaa(aa):
    action = aa.POST.get('action')
    user = aa.POST.get('body[username]')
    pwd = aa.POST.get('body[password]')
    print(action,user,pwd)
def code():
    Menu=menu.objects.all()
    a=[]
    b=[]
    for line in Menu:
        a.append(line.menu_code)
        b.append(line.menu_name)
    c={"code":a,"name":b}
    return c
if __name__ == '__main__':
    print("Work Start")
    print(code())
    print("Work Ending")