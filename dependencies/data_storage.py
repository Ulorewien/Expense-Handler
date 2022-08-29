from openpyxl import *

def addExpenseData(data):
    # print(data)
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

def createWorkbook(month):
    workbook = Workbook()
    workbook.create_sheet(month)
    workbook["A1"] = "Date"
    workbook["B1"] = "Expense"
    workbook["C1"] = "Amount"
    workbook["D1"] = "Method"
    workbook["E1"] = "Total Expenditure"
    workbook["F1"] = "Total Funds"
    workbook["G1"] = "Income"
    workbook["H1"] = "Amount"