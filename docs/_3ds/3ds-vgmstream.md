---
author: TricksterGuy
categories:
- utility
color: '#182448'
created: '2016-02-01T06:16:42Z'
description: Port of vgmstream for the nintendo 3ds along with a player
download_page: https://github.com/TricksterGuy/3ds-vgmstream/releases/tag/v0.2.0
downloads:
  3ds-vgmstream.3ds:
    size: 982016
    url: https://github.com/TricksterGuy/3ds-vgmstream/releases/download/v0.2.0/3ds-vgmstream.3ds
  3ds-vgmstream.cia:
    size: 995264
    url: https://github.com/TricksterGuy/3ds-vgmstream/releases/download/v0.2.0/3ds-vgmstream.cia
  3ds-vgmstream.zip:
    size: 459519
    url: https://github.com/TricksterGuy/3ds-vgmstream/releases/download/v0.2.0/3ds-vgmstream.zip
github: TricksterGuy/3ds-vgmstream
icon: https://raw.githubusercontent.com/TricksterGuy/3ds-vgmstream/master/resources/icon.png
image: https://raw.githubusercontent.com/TricksterGuy/3ds-vgmstream/master/resources/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  3ds-vgmstream.cia: https://db.universal-team.net/assets/images/qr/3ds-vgmstream.cia.png
scripts:
  3ds-vgmstream.3dsx:
  - file: 3ds-vgmstream.zip
    message: Downloading 3ds-vgmstream.zip...
    output: /3ds-vgmstream.zip
    repo: TricksterGuy/3ds-vgmstream
    type: downloadRelease
  - file: /3ds-vgmstream.zip
    input: 3ds/3ds-vgmstream/3ds-vgmstream.3dsx
    message: Extracting 3ds-vgmstream.3dsx...
    output: '%3DSX%/3ds-vgmstream.3dsx'
    type: extractFile
  - file: /3ds-vgmstream.zip
    message: Deleting 3ds-vgmstream.zip...
    type: deleteFile
source: https://github.com/TricksterGuy/3ds-vgmstream
systems:
- 3DS
title: 3ds-vgmstream
update_notes: '<p>New:<br>

  Now uses dsp over csnd, this grants all of the benefits of dsp, better streaming.  This
  does however require users to dump their dsp firmware (see <a href="https://github.com/Cruel/DspDump">dsp
  dumper</a>)</p>

  <p>Fixed:<br>

  Various other fixes, such as the sound being garbled if you play multiple songs
  in a single session.</p>'
updated: '2016-07-11T07:32:44Z'
version: v0.2.0
version_title: Version 0.2.0
wiki: https://github.com/TricksterGuy/3ds-vgmstream/wiki
---
