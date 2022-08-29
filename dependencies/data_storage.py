from openpyxl import *
from dependencies.excel_functions import *

def addExpenseData(data):
    month = data["Month"] + data["Year"]
    try:
        workbook = load_workbook("./output/Expenditure.xlsx")
    except:
        workbook = createWorkbook(data["Month"])
    
    if(data["Month"] in workbook.sheetnames):
        worksheet = workbook[data["Month"]]
    else:
        workbook.create_sheet(data["Month"])
        worksheet = workbook[data["Month"]]

    

    workbook.save("./output/Expenditure.xlsx")