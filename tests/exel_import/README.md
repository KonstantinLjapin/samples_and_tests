"""wb = load_workbook("шаблон отчета.xlsx")
sheet = wb["Данные"]

#Заполнение данных

report_table = BytesIO()
wb.save(report_table)

report_table.seek(0)
wb.close()
при загрузке workbook, срезы удаляются, так как openpyxl не поддерживает их,
 я так понимаю, что нужно сменить библиотеку или предложите свой вариант
Есть код на openpyxl, который вносит данные в лист Excel, но при этом разрушает
 Slicer List (фильтры) в таблице при открытии таблицы:
  "UserWarning: Slicer List extension is not supported and will be removed",
   оставляйте ваш тг для связи
"""
