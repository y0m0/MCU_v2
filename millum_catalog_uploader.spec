# -*- mode: python -*-
a = Analysis(['millum_catalog_uploader.py'],
             pathex=['C:\\Users\\admin\\Dropbox\\python catalog\\Mcu v02'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='millum_catalog_uploader.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='version.txt', icon='upload.ico')
