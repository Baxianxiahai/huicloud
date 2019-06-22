'''
Created on 2018/2/23

@author: hitpony
'''

#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
#reference: http://www.cnblogs.com/tkinter/p/5632258.html

from distutils.core import setup
import py2exe
import sys

py2exe_options = {
    "includes": ["sip"],
    "dll_excludes": ["MSVCP90.dll",],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    "bundle_files": 1,
    }

setup(
  name = 'Fmpt2',
  version = '1.0',
  windows = ['fmpt2Entry_wx.py'],
  zipfile = None,
  options = {'py2exe': py2exe_options}
  )

#
#python3 setup2exe.py py2exe