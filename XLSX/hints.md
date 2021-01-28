---
to: pdf
title: "Excel-Tipps and Tricks"
author: "Dr. Bastian Ebeling"
date: \today
lang: de-DE
smart: true
documentclass: scrartcl
colorlinks: true
hyperrefoptions:
    - linktoc=all
    - pdfwindowui
---

## Sheet Protections

Quelle: <https://praxistipps.chip.de/excel-passwort-des-blattschutzes-vergessen_16735> bzw. <https://archive.vn/J5N4N>

* Open `xlsx` file with archiver
* Search relevant sheet in structure (top folder `xl` and therein `worksheets`)
* Process `sheet#.xml`
  * remove tag starting with `<sheetProtection"` ending with `"scenarios="1">`
* save and be happy
