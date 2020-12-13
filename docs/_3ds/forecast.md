---
author: NatTupper
categories:
- utility
color: '#a2a3a4'
created: '2017-07-18T12:56:44Z'
description: A weather app for the 3DS
download_page: https://github.com/NatTupper/Forecast/releases/tag/v1.0.1
downloads:
  Forecast-1.0.1.zip:
    size: 828371
    url: https://github.com/NatTupper/Forecast/releases/download/v1.0.1/Forecast-1.0.1.zip
github: NatTupper/Forecast
icon: https://raw.githubusercontent.com/NatTupper/Forecast/master/icon.png
image: https://raw.githubusercontent.com/NatTupper/Forecast/master/res/banner%20icon.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  Forecast.3dsx:
  - file: Forecast.*\.zip
    message: Downloading Forecast zip...
    output: /Forecast.zip
    repo: NatTupper/Forecast
    type: downloadRelease
  - file: /Forecast.zip
    input: Forecast.3dsx
    message: Extracting Forecast.3dsx...
    output: '%3DSX%/Forecast.3dsx'
    type: extractFile
  - file: /Forecast.zip
    message: Deleting Forecast.zip...
    type: deleteFile
  Forecast.cia:
  - file: Forecast.*\.zip
    message: Downloading Forecast zip...
    output: /Forecast.zip
    repo: NatTupper/Forecast
    type: downloadRelease
  - file: /Forecast.zip
    input: Forecast.cia
    message: Extracting Forecast.cia...
    output: /Forecast.cia
    type: extractFile
  - file: /Forecast.cia
    message: Installing Forecast.cia...
    type: installCia
  - file: /Forecast.cia
    message: Deleting Forecast.cia...
    type: deleteFile
  - file: /Forecast.zip
    message: Deleting Forecast.zip...
    type: deleteFile
source: https://github.com/NatTupper/Forecast
systems:
- 3DS
title: Forecast
update_notes: '<h2>Fixed</h2>

  <ul>

  <li>Fixed <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="245271043" data-permission-text="Title is private" data-url="https://github.com/NatTupper/Forecast/issues/1"
  data-hovercard-type="issue" data-hovercard-url="/NatTupper/Forecast/issues/1/hovercard"
  href="https://github.com/NatTupper/Forecast/issues/1">#1</a></li>

  </ul>'
updated: '2017-07-25T12:39:20Z'
version: v1.0.1
version_title: v1.0.1
wiki: https://github.com/NatTupper/Forecast/wiki
---
