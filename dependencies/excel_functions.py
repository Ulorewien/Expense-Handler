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
        setColor(worksheet.cell(1, column), "headers")
        setColor(worksheet.cell(2, column), "headers")

    return workbook

def createSheet(workbook, month):
    workbook.create_sheet(month)
    worksheet = workbook[month]
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
        setColor(worksheet.cell(1, column), "headers")
        setColor(worksheet.cell(2, column), "headers")

def setColor(cell, type):
    specs = getSpecifications()
    cell.fill = PatternFill("solid", start_color = specs["Excel"][type])

def setRowColor(worksheet, row):
    setColor(worksheet.cell(row, 1), "headers")
    setColor(worksheet.cell(row, 2), "expense")
    setColor(worksheet.cell(row, 3), "expense")
    setColor(worksheet.cell(row, 4), "expense")
    setColor(worksheet.cell(row, 5), "expense")
    setColor(worksheet.cell(row, 6), "funds")
    setColor(worksheet.cell(row, 7), "income")
    setColor(worksheet.cell(row, 8), "income")