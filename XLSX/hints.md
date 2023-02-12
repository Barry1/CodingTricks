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

### Unprotection by file edit

Quelle: <https://praxistipps.chip.de/excel-passwort-des-blattschutzes-vergessen_16735> bzw. <https://archive.vn/J5N4N>

- Open `xlsx` file with archiver
- Search relevant sheet in structure (top folder `xl` and therein `worksheets`)
- Process `sheet#.xml`
  - remove tag starting with `<sheetProtection"` ending with `"scenarios="1">`
- save and be happy

### Cracking the password (or one working analogous)

- <https://www.online-tech-tips.com/ms-office-tips/how-to-remove-crack-or-break-a-forgotten-excel-xls-password/> or <https://archive.vn/51ywg>

```VBA
Sub BreakPassword()

   Dim i As Integer, j As Integer, k As Integer
   Dim l As Integer, m As Integer, n As Integer
   Dim i1 As Integer, i2 As Integer, i3 As Integer
   Dim i4 As Integer, i5 As Integer, i6 As Integer

   On Error Resume Next

   For i = 65 To 66: For j = 65 To 66: For k = 65 To 66
   For l = 65 To 66: For m = 65 To 66: For i1 = 65 To 66
   For i2 = 65 To 66: For i3 = 65 To 66: For i4 = 65 To 66
   For i5 = 65 To 66: For i6 = 65 To 66: For n = 32 To 126

   ActiveSheet.Unprotect Chr(i) & Chr(j) & Chr(k) & _
   Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & _
   Chr(i4) & Chr(i5) & Chr(i6) & Chr(n)

   If ActiveSheet.ProtectContents = False Then
      Exit Sub
   End If

   Next: Next: Next: Next: Next: Next
   Next: Next: Next: Next: Next: Next

End Sub
```

- other solution <https://exceloffthegrid.com/removing-cracking-excel-passwords-with-vba/#Cracking_worksheet_and_workbook_passwords> bzw. <https://archive.is/ULCjT>
