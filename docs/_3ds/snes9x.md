---
author: bubble2k16
categories:
- emulator
color: '#2f6fb0'
created: '2016-10-15T13:52:35Z'
description: SNES9x Port for 3DS / 2DS
download_page: https://github.com/bubble2k16/snes9x_3ds/releases/tag/v1.30
downloads:
  snes9x_3ds-v1.30.zip:
    size: 1832323
    url: https://github.com/bubble2k16/snes9x_3ds/releases/download/v1.30/snes9x_3ds-v1.30.zip
github: bubble2k16/snes9x_3ds
icon: https://raw.githubusercontent.com/bubble2k16/snes9x_3ds/master/assets/icon.png
image: https://db.universal-team.net/assets/images/images/snes9x_3ds.png
layout: app
scripts:
  snes9x_3ds.3dsx:
  - file: snes9x_3ds.*\.zip
    message: Downloading snes9x_3ds.zip...
    output: /snes9x_3ds.zip
    repo: bubble2k16/snes9x_3ds
    type: downloadRelease
  - file: /snes9x_3ds.zip
    input: snes9x_3ds.3dsx
    message: Extracting snes9x_3ds.3dsx...
    output: '%3DSX%/snes9x_3ds.3dsx'
    type: extractFile
  - file: /snes9x_3ds.zip
    message: Deleting snes9x_3ds.zip...
    type: deleteFile
  snes9x_3ds.cia:
  - file: snes9x_3ds.*\.zip
    message: Downloading snes9x_3ds.zip...
    output: /snes9x_3ds.zip
    repo: bubble2k16/snes9x_3ds
    type: downloadRelease
  - file: /snes9x_3ds.zip
    input: snes9x_3ds.cia
    message: Extracting snes9x_3ds.cia...
    output: /snes9x_3ds.cia
    type: extractFile
  - file: /snes9x_3ds.cia
    message: Installing snes9x_3ds.cia...
    type: installCia
  - file: /snes9x_3ds.cia
    message: Deleting snes9x_3ds.cia...
    type: deleteFile
  - file: /snes9x_3ds.zip
    message: Deleting snes9x_3ds.zip...
    type: deleteFile
source: https://github.com/bubble2k16/snes9x_3ds
systems:
- 3DS
title: Snes9x
update_notes: '<ul>

  <li>Improved sound synchronization.</li>

  <li>Added BlargSNES DSP Core (experimental) for performance. The original Snes9X
  DSP core (default) suffers from sound skipping in some games like Aladdin and Gradius
  3. You can choose which DSP core to use from the Options menu. The BlargSNES DSP
  Core sounds similar to the Snes9x Core for most games. Sounds like Final Fantasy
  3''s the howling wind sound different.</li>

  <li>Added support for Tengai Makyou Zero English Patch (for hopefully all future
  versions)</li>

  </ul>'
updated: '2018-03-24T01:43:21Z'
version: v1.30
version_title: v1.30
wiki: https://github.com/bubble2k16/snes9x_3ds/wiki
---
