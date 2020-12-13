---
author: DS-Homebrew
categories:
- utility
- save-tool
color: '#be8345'
created: '2018-10-02T16:59:38Z'
description: 'GodMode9i Explorer - A full access file browser for the Nintendo DS
  and DSi consoles :godmode:'
download_page: https://github.com/DS-Homebrew/GodMode9i/releases/tag/v2.5.0
downloads:
  GodMode9i.7z:
    size: 167764
    url: https://github.com/DS-Homebrew/GodMode9i/releases/download/v2.5.0/GodMode9i.7z
github: DS-Homebrew/GodMode9i
icon: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/icon.bmp
image: https://raw.githubusercontent.com/DS-Homebrew/GodMode9i/master/resources/logo2.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/TWLBot/Builds/blob/master/extras/GodMode9i.7z
  downloads:
    GodMode9i.7z:
      url: https://github.com/TWLBot/Builds/raw/master/extras/GodMode9i.7z
scripts:
  GodMode9i.cia:
  - file: GodMode9i.7z
    message: Downloading GodMode9i.7z...
    output: /GodMode9i.7z
    repo: DS-Homebrew/GodMode9i
    type: downloadRelease
  - file: /GodMode9i.7z
    input: GodMode9i.cia
    message: Extracting GodMode9i.cia...
    output: /GodMode9i.cia
    type: extractFile
  - file: /GodMode9i.cia
    message: Installing GodMode9i.cia...
    type: installCia
  - file: /GodMode9i.cia
    message: Deleting GodMode9i.cia...
    type: deleteFile
  - file: /GodMode9i.7z
    message: Deleting GodMode9i.7z...
    type: deleteFile
  GodMode9i.nds:
  - file: GodMode9i.7z
    message: Downloading GodMode9i.7z...
    output: /GodMode9i.7z
    repo: DS-Homebrew/GodMode9i
    type: downloadRelease
  - file: /GodMode9i.7z
    input: GodMode9i.nds
    message: Extracting GodMode9i.nds...
    output: '%NDS%/GodMode9i.nds'
    type: extractFile
  - file: /GodMode9i.7z
    message: Deleting GodMode9i.7z...
    type: deleteFile
  '[nightly] GodMode9i.cia':
  - file: https://github.com/TWLBot/Builds/raw/master/extras/GodMode9i.7z
    message: Downloading GodMode9i.7z...
    output: /GodMode9i.7z
    type: downloadFile
  - file: /GodMode9i.7z
    input: GodMode9i/GodMode9i.cia
    message: Extracting GodMode9i.cia...
    output: /GodMode9i.cia
    type: extractFile
  - file: /GodMode9i.cia
    message: Installing GodMode9i.cia...
    type: installCia
  - file: /GodMode9i.cia
    message: Deleting GodMode9i.cia...
    type: deleteFile
  - file: /GodMode9i.7z
    message: Deleting GodMode9i.7z...
    type: deleteFile
  '[nightly] GodMode9i.nds':
  - file: https://github.com/TWLBot/Builds/raw/master/extras/GodMode9i.7z
    message: Downloading GodMode9i.7z...
    output: /GodMode9i.7z
    type: downloadFile
  - file: /GodMode9i.7z
    input: GodMode9i/GodMode9i.nds
    message: Extracting GodMode9i.nds...
    output: '%NDS%/GodMode9i.nds'
    type: extractFile
  - file: /GodMode9i.7z
    message: Deleting GodMode9i.7z...
    type: deleteFile
source: https://github.com/DS-Homebrew/GodMode9i
systems:
- DS
title: GodMode9i
update_notes: '<p><strong>What''s new?</strong></p>

  <ul>

  <li>

  <p>Compatibility with GBA ROM dumping has been increased. You can now dump 64MB
  GBA ROMs!<br>

  What can currently be dumped:</p>

  <ul>

  <li>GBA Video: Shark Tale</li>

  <li>GBA Video: Shrek</li>

  <li>GBA Video: Shrek &amp; Shark Tale</li>

  <li>GBA Video: Shrek 2</li>

  </ul>

  <p>What cannot currently be dumped:</p>

  <ul>

  <li>GBA Video: Shrek &amp; Shrek 2 (Reason: Title ID not known)</li>

  </ul>

  </li>

  <li>

  <p>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>)
  Added multi file copy paste support.</p>

  </li>

  <li>

  <p>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>)
  Added selection deletion support</p>

  </li>

  <li>

  <p>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)
  Added save file restoring.</p>

  </li>

  </ul>

  <p><strong>Bug fixes</strong></p>

  <ul>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>)
  Fixed crash when copying empty folders</li>

  <li>(<a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/unresolvedsymbol/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/unresolvedsymbol">@unresolvedsymbol</a>)
  Misc formatting fixes.</li>

  </ul>'
updated: '2020-09-07T09:14:30Z'
version: v2.5.0
version_title: 'v2.5.0: Labor Day release'
wiki: https://github.com/DS-Homebrew/GodMode9i/wiki
---
Features:
- Dump GameBoy Advance cartridges on the original Nintendo DS and Nintendo DS Lite consoles.
- Dump Nintendo DS/DSi cartridges on Nintendo DSi and Nintendo 3DS consoles (if GodMode9i is ran on the console SD card).
- Copy, move, delete, rename files/folders and create folders.
- Mount the NitroFS of .nds files.
- Browse files on supported flashcards when running GM9i from the NAND or SD Card. (`AceKard 2(i)` & `R4 Ultra (r4ultra.com)`)