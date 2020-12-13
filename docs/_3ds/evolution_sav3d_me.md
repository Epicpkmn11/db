---
author: Manurocker95
autogen_scripts: true
categories:
- game
color: '#6d7a68'
created: '2017-01-31T16:20:47Z'
description: A monkey who wants to survive!
download_page: https://github.com/Manurocker95/Evolution_Sav3D_Me/releases/tag/1.1
downloads:
  Evolution_Sav3D_Me.cia:
    size: 15668160
    url: https://github.com/Manurocker95/Evolution_Sav3D_Me/releases/download/1.1/Evolution_Sav3D_Me.cia
  Evolution_Sav3D_Me.rar:
    size: 15800689
    url: https://github.com/Manurocker95/Evolution_Sav3D_Me/releases/download/1.1/Evolution_Sav3D_Me.rar
github: Manurocker95/Evolution_Sav3D_Me
icon: https://raw.githubusercontent.com/Manurocker95/Evolution_Sav3D_Me/Evolution_Sav3D_Me/icon.png
image: https://db.universal-team.net/assets/images/images/evolution_sav3d_me.png
layout: app
qr:
  Evolution_Sav3D_Me.cia: https://db.universal-team.net/assets/images/qr/evolution_sav3d_me.cia.png
scripts:
  Evolution_Sav3D_Me.3dsx:
  - message: UU is unable to extract this at the moment...
    type: promptMessage
  - type: exit
  - file: Evolution_Sav3D_Me.rar
    message: Downloading Evolution_Sav3D_Me.rar...
    output: /Evolution_Sav3D_Me.rar
    repo: Manurocker95/Evolution_Sav3D_Me
    type: downloadRelease
  - file: /Evolution_Sav3D_Me.rar
    input: Evolution_Sav3D_Me.3dsx
    message: Extracting Evolution_Sav3D_Me.3dsx...
    output: '%3DSX%/Evolution_Sav3D_Me.3dsx'
    type: extractFile
  - file: /Evolution_Sav3D_Me.rar
    message: Deleting Evolution_Sav3D_Me.rar...
    type: deleteFile
source: https://github.com/Manurocker95/Evolution_Sav3D_Me
systems:
- 3DS
title: Evolution_Sav3D_Me
update_notes: <p>Changed the splash screen</p>
updated: '2017-08-23T11:38:07Z'
version: '1.1'
version_title: 'A New Release '
wiki: https://github.com/Manurocker95/Evolution_Sav3D_Me/wiki
---
