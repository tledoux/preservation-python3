# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
            )

a.datas += [('images/preservation-python.ico','./images/preservation-python.ico', "DATA")]
a.datas += [('translations/es/LC_MESSAGES/preservation.mo','./translations/es/LC_MESSAGES/preservation.mo', "DATA")]
a.datas += [('translations/fr/LC_MESSAGES/preservation.mo','./translations/fr/LC_MESSAGES/preservation.mo', "DATA")]
a.datas += [('images/snake_head.png','./images/snake_head.png', "DATA")]
a.datas += [('images/snake_tail.png','./images/snake_tail.png', "DATA")]
a.datas += [('images/snake_body.png','./images/snake_body.png', "DATA")]
a.datas += [('images/snake_turn.png','./images/snake_turn.png', "DATA")]
a.datas += [('images/accessrights.png','./images/accessrights.png', "DATA")]
a.datas += [('images/backup.png','./images/backup.png', "DATA")]
a.datas += [('images/brokenhardware.png','./images/brokenhardware.png', "DATA")]
a.datas += [('images/checksum.png','./images/checksum.png', "DATA")]
a.datas += [('images/context.png','./images/context.png', "DATA")]
a.datas += [('images/custody.png','./images/custody.png', "DATA")]
a.datas += [('images/dataobject.png','./images/dataobject.png', "DATA")]
a.datas += [('images/delete.png','./images/delete.png', "DATA")]
a.datas += [('images/emulation.png','./images/emulation.png', "DATA")]
a.datas += [('images/legal.png','./images/legal.png', "DATA")]
a.datas += [('images/metadata.png','./images/metadata.png', "DATA")]
a.datas += [('images/migration.png','./images/migration.png', "DATA")]
a.datas += [('images/obsolete.png','./images/obsolete.png', "DATA")]
a.datas += [('images/orgcommitment.png','./images/orgcommitment.png', "DATA")]
a.datas += [('images/packaging.png','./images/packaging.png', "DATA")]
a.datas += [('images/provenance.png','./images/provenance.png', "DATA")]
a.datas += [('images/reference.png','./images/reference.png', "DATA")]
a.datas += [('images/refresh.png','./images/refresh.png', "DATA")]
a.datas += [('images/representation.png','./images/representation.png', "DATA")]
a.datas += [('images/softwarebug.png','./images/softwarebug.png', "DATA")]
a.datas += [('images/techwatch.png','./images/techwatch.png', "DATA")]
a.datas += [('images/virus.png','./images/virus.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='preservation-python3',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon=['./images/preservation-python.ico'],
          version='file_version_info.txt',
         )