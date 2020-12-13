---
author: mrdanielps
categories:
- emulator
color: '#d3d2d2'
created: '2014-11-17T22:30:56Z'
description: A Virtual Boy emulator for the 3DS
download_page: https://github.com/mrdanielps/r3Ddragon/releases/tag/v0.87
downloads:
  r3Ddragon-v0.87.zip:
    size: 463677
    url: https://github.com/mrdanielps/r3Ddragon/releases/download/v0.87/r3Ddragon-v0.87.zip
github: mrdanielps/r3Ddragon
icon: https://raw.githubusercontent.com/mrdanielps/r3Ddragon/master/icon.png
image: https://raw.githubusercontent.com/mrdanielps/r3Ddragon/master/resources/banner.png
layout: app
scripts:
  r3Ddragon.cia:
  - file: r3Ddragon.*\.zip
    message: Downloading r3Ddragon zip...
    output: /r3Ddragon.zip
    repo: mrdanielps/r3Ddragon
    type: downloadRelease
  - file: /r3Ddragon.zip
    input: r3Ddragon.cia
    message: Extracting r3Ddragon.cia...
    output: /r3Ddragon.cia
    type: extractFile
  - file: /r3Ddragon.cia
    message: Installing r3Ddragon.cia...
    type: installCia
  - file: /r3Ddragon.cia
    message: Deleting r3Ddragon.cia...
    type: deleteFile
  - file: /r3Ddragon.zip
    message: Deleting r3Ddragon.zip...
    type: deleteFile
source: https://github.com/mrdanielps/r3Ddragon
systems:
- 3DS
title: r3Ddragon
update_notes: '<h4>Changelog:</h4>

  <ul>

  <li>Removed libhax. Homebrew launcher users will have to run a kernel exploit (like
  <a href="https://github.com/nedwill/fasthax/releases">fasthax</a>) first.</li>

  <li>Added settings for frameskip, maxcycles, sound and debug output.</li>

  <li>Implemented floating point instructions.</li>

  </ul>

  <h4>Known Issues:</h4>

  <ul>

  <li>Low compatibility.</li>

  <li>Glitchy graphics on some commercial games.</li>

  <li>Frame limiting is broken when frameskip is enabled.</li>

  <li>Some menu options aren''t implemented.</li>

  <li>To change ROMs you have to exit first (touchscreen-&gt;File-&gt;Exit).</li>

  </ul>'
updated: '2017-02-02T23:45:48Z'
version: v0.87
version_title: v0.87
wiki: https://github.com/mrdanielps/r3Ddragon/wiki
---
