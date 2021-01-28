'https://www.herber.de/forum/archiv/1148to1152/1151902_Pivottabellen_aktualisieren_VBA.html
'https://excelnova.org/pivot-tabellen-automatisch-aktualisieren/
'https://www.ms-office-forum.net/forum/showthread.php?t=338874
'https://answers.microsoft.com/de-de/msoffice/forum/msoffice_excel-mso_windows8-mso_2013_release/alle-pivot-tabellendiagramme-gleichzeitig/b47d696a-ab85-49a6-afd8-c7aa47d5cd22

''BLATTSCHUTZ
Private Sub Worksheet_Activate()
    ActiveSheet.PivotTables("PivotTable1").PivotCache.Refresh
End Sub

Private Sub Worksheet_Change(ByVal Target As Range)
    Application.EnableEvents = False
    ThisWorkbook.RefreshAll
    Application.EnableEvents = True
End Sub

Sub Aktualisieren()
    ThisWorkbook.RefreshAll
End Sub

Private Sub Workbook_SheetActivate(ByVal Sh As Object)
    Dim pt As PivotTable
    For Each pt In Sh.PivotTables
        pt.PivotCache.Refresh
    Next
End Sub

'http://www.office-loesung.de/ftopic327619_0_0_asc.php
Private Sub Worksheet_Activate()
    Dim pt As PivotTable
    Me.Unprotect
    For Each pt In ActiveSheet.PivotTables
        pt.RefreshTable
    Next pt
    Me.Protect
End Sub