from openpyxl import *
from dependencies.excel_functions import *
from dependencies.date import *

def addExpenseData(data):
    month = data["Month"] + data["Year"]
    try:
        workbook = load_workbook("./output/Expenditure.xlsx")
    except:
        workbook = createWorkbook(month)
    
    if(month in workbook.sheetnames):
        worksheet = workbook[month]
    else:
        createSheet(workbook, month)
        worksheet = workbook[month]

    new_row = worksheet.max_row + 1
    worksheet["A" + str(new_row)] = data["Day"] + "-" + getMonthNumber(data["Month"]) + "-" + data["Year"]
    worksheet["B" + str(new_row)] = data["Type"]
    worksheet["C" + str(new_row)] = data["Amount"]
    worksheet["D" + str(new_row)] = data["Mode"]
    setRowColor(worksheet, new_row)

    for column in worksheet.columns:
        for cell in column:
            cell.alignment = cell.alignment.copy(horizontal='center', vertical='center')
    workbook._sheets.sort(key = lambda worksheet: worksheet.title[-4:])
    workbook.save("./output/Expenditure.xlsx")