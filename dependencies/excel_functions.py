from openpyxl import *
from openpyxl.styles import PatternFill
from dependencies.specifications import *

def createWorkbook(month):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = month
    worksheet["A1"] = "Date"
    worksheet["B1"] = "Expense"
    worksheet["C1"] = "Amount"
    worksheet["D1"] = "Method"
    worksheet["E1"] = "Total Expenditure"
    worksheet["F1"] = "Total Funds"
    worksheet["G1"] = "Income"
    worksheet["H1"] = "Amount"

    for column in range(1, worksheet.max_column + 1):
        worksheet.cell(1, column).fill = PatternFill("solid", start_color = getColor("headers"))
        worksheet.cell(2, column).fill = PatternFill("solid", start_color = getColor("headers"))

    return workbook

def getColor(type):
    specs = getSpecifications()
    return specs["Excel"][type]