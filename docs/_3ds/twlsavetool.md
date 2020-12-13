---
author: TuxSH
autogen_scripts: true
categories:
- utility
- save-tool
color: '#386637'
created: '2015-12-24T15:36:14Z'
description: A 3DS homebrew that allows you to read, write, and erase save files from
  NDS cartridges
download_page: https://github.com/TuxSH/TWLSaveTool/releases/tag/v1.2
downloads:
  TWLSaveTool.cia:
    size: 614848
    url: https://github.com/TuxSH/TWLSaveTool/releases/download/v1.2/TWLSaveTool.cia
  TWLSaveTool.zip:
    size: 114930
    url: https://github.com/TuxSH/TWLSaveTool/releases/download/v1.2/TWLSaveTool.zip
github: TuxSH/TWLSaveTool
icon: https://raw.githubusercontent.com/TuxSH/TWLSaveTool/master/app/IconLarge.png
image: https://avatars2.githubusercontent.com/u/1922548?v=4
layout: app
license: gpl-2.0
license_name: GNU General Public License v2.0
qr:
  TWLSaveTool.cia: https://db.universal-team.net/assets/images/qr/twlsavetool.cia.png
scripts:
  TWLSaveTool.3dsx:
  - file: TWLSaveTool.zip
    message: Downloading TWLSaveTool.zip...
    output: /TWLSaveTool.zip
    repo: TuxSH/TWLSaveTool
    type: downloadRelease
  - file: /TWLSaveTool.zip
    input: 3ds/TWLSaveTool/TWLSaveTool.3dsx
    message: Extracting TWLSaveTool.3dsx...
    output: '%3DSX%/TWLSaveTool.3dsx'
    type: extractFile
  - file: /TWLSaveTool.zip
    message: Deleting TWLSaveTool.zip...
    type: deleteFile
source: https://github.com/TuxSH/TWLSaveTool
systems:
- 3DS
title: TWLSaveTool
update_notes: "<ul>\n<li>Fix Pok\xE9mon Mystery Dungeon: Explorers of Sky (thanks\
  \ to <a class=\"user-mention\" data-hovercard-type=\"user\" data-hovercard-url=\"\
  /users/Steveice10/hovercard\" data-octo-click=\"hovercard-link-click\" data-octo-dimensions=\"\
  link_type:self\" href=\"https://github.com/Steveice10\">@Steveice10</a>)</li>\n\
  </ul>"
updated: '2016-08-27T19:27:37Z'
version: v1.2
version_title: TWLSaveTool v1.2
wiki: https://github.com/TuxSH/TWLSaveTool/wiki
---
