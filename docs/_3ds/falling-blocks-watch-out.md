---
author: Spaqin
categories:
- game
color: '#a09585'
created: '2016-01-30T08:52:55Z'
description: Falling Blocks Watch Out, a 3DS homebrew Tetris clone.
download_page: https://github.com/Spaqin/fbwo-3ds/releases/tag/v0.4.1
downloads:
  fbwo.v0.4.1.zip:
    size: 7350096
    url: https://github.com/Spaqin/fbwo-3ds/releases/download/v0.4.1/fbwo.v0.4.1.zip
github: Spaqin/fbwo-3ds
icon: https://db.universal-team.net/assets/images/icons/fbwo-3ds.png
image: https://db.universal-team.net/assets/images/images/fbwo-3ds.png
layout: app
scripts:
  fbwo.3dsx:
  - file: fbwo.*\.zip
    message: Downloading fbwo.zip...
    output: /fbwo.zip
    repo: Spaqin/fbwo-3ds
    type: downloadRelease
  - file: /fbwo.zip
    input: fbwodata
    message: Extracting fbwodata...
    output: /fbwodata
    type: extractFile
  - file: /fbwo.zip
    input: 3ds/fbwo/fbwo.3dsx
    message: Extracting fbwo.3dsx...
    output: /3ds/fbwo.3dsx
    type: extractFile
  - file: /fbwo.zip
    message: Deleting fbwo.zip...
    type: deleteFile
  fbwo.cia:
  - file: fbwo.*\.zip
    message: Downloading fbwo.zip...
    output: /fbwo.zip
    repo: Spaqin/fbwo-3ds
    type: downloadRelease
  - file: /fbwo.zip
    input: fbwodata
    message: Extracting fbwodata...
    output: /fbwodata
    type: extractFile
  - file: /fbwo.zip
    input: fbwo.cia
    message: Extracting fbwo.cia...
    output: /fbwo.cia
    type: extractFile
  - file: /fbwo.cia
    message: Installing fbwo.cia...
    type: installCia
  - file: /fbwo.zip
    message: Deleting fbwo.zip...
    type: deleteFile
  - file: /fbwo.cia
    message: Deleting fbwo.zip...
    type: deleteFile
source: https://github.com/Spaqin/fbwo-3ds
systems:
- 3DS
title: Falling Blocks Watch Out
update_notes: '<p>A quick update adding per-level glue delay.<br>

  Be careful, the config file is different from the previous one.</p>'
updated: '2016-03-06T09:43:45Z'
version: v0.4.1
version_title: FBWO v0.4.1
wiki: https://github.com/Spaqin/fbwo-3ds/wiki
---
