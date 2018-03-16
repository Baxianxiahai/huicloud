# -*- mode: python -*-

#Comments Add by ZJL
#pyinstaller -F -w -p/usr/local/lib/python3.6/site-packages/django/:/usr/local/lib/python3.6/site-packages/django/template/:/usr/local/lib/python3.6/site-packages/django/templatetags/i18n.p:/usr/local/lib/python3.6/site-packages/django/templatetags/:/usr/local/lib/python3.6/site-packages/django/core/:/usr/local/lib:/usr/lib/:/usr/local/lib/python3.5/ hstMain.py

block_cipher = None


a = Analysis(['hstMain.py'],
             pathex=['/usr/local/lib/python3.6/site-packages/django/', '/usr/local/lib/python3.6/site-packages/django/template/', '/usr/local/lib/python3.6/site-packages/django/templatetags/i18n.p', '/usr/local/lib/python3.6/site-packages/django/templatetags/', '/usr/local/lib/python3.6/site-packages/django/core/', '/usr/local/lib', '/usr/lib/', '/usr/local/lib/python3.5/', '/home/hitpony/EclipseWs/sdde/hst'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='hstMain',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
