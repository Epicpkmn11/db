---
author: DeadSkullzJr
bitbucket:
  files:
  - Cheats/cheat.dat
  - Cheats/cheat.db
  - Cheats/cheat_EN.db
  - Cheats/cheats.dat
  - Cheats/cheats.xml
  - Cheats/ezarcode.dat
  - Cheats/user.evoCheats
  - Cheats/usrcheat.dat
  - Cheats/~SCC Cheats~.7z
  repo: DeadSkullzJr/nds-cheat-databases
categories:
- extra
color: '#84836f'
created: '2020-06-11T03:21:33.747363+00:00'
description: 'These cheat database sets are for Nintendo DS flashcarts, cheating devices,
  emulators, and homebrew applications

  for various compatible devices. Each database contains Action Replay codes for your
  favorite NDS games.'
download_page: https://bitbucket.org/DeadSkullzJr/nds-cheat-databases/src/master/Cheats/cheat.dat
downloads:
  Cheats/cheat.dat:
    size: 44493500
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/cheat.dat
  Cheats/cheat.db:
    size: 75934073
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/cheat.db
  Cheats/cheat_EN.db:
    size: 75934073
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/cheat_EN.db
  Cheats/cheats.dat:
    size: 11596364
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/cheats.dat
  Cheats/cheats.xml:
    size: 108105819
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/cheats.xml
  Cheats/ezarcode.dat:
    size: 44493500
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/ezarcode.dat
  Cheats/user.evoCheats:
    size: 11596396
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/user.evoCheats
  Cheats/usrcheat.dat:
    size: 44493500
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/usrcheat.dat
  Cheats/~SCC Cheats~.7z:
    size: 1363341
    url: https://api.bitbucket.org/2.0/repositories/DeadSkullzJr/nds-cheat-databases/src/933c375545d3ff90854d1e210dcf4b3b31d9d585/Cheats/~SCC%20Cheats~.7z
image: https://db.universal-team.net/assets/images/images/nds-cheat-databases.png
layout: app
scripts:
  '[twlmenu] usrcheat.dat':
  - file: https://github.com/TWLBot/Builds/raw/master/usrcheat.dat.7z
    message: Downloading usrcheat.dat...
    output: /usrcheat.dat.7z
    type: downloadFile
  - file: /usrcheat.dat.7z
    input: usrcheat.dat
    message: Extracting usrcheat.dat...
    output: /_nds/TWiLightMenu/extras/usrcheat.dat
    type: extractFile
  - file: /usrcheat.dat.7z
    type: deleteFile
source: https://bitbucket.org/DeadSkullzJr/nds-cheat-databases
systems:
- DS
title: NDS Cheat Databases
updated: '2020-06-11T03:24:40+00:00'
version: 933c375
website: https://gbatemp.net/threads/deadskullzjrs-nds-cheat-databases.488711/
---
