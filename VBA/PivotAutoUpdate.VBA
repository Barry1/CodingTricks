'https://excelnova.org/pivot-tabellen-automatisch-aktualisieren/
'https://www.ms-office-forum.net/forum/showthread.php?t=338874
Private Sub Worksheet_Activate()
    ActiveSheet.PivotTables("PivotTable1").PivotCache.Refresh
End Sub

Private Sub Worksheet_Change(ByVal Target As Range)
Application.EnableEvents = False
    ThisWorkbook.RefreshAll
Application.EnableEvents = True
End Sub