from dependencies.date import *

def addExpense(app):
    day_of_expense = app.select_day_dropdown.get()
    month_of_expense = app.select_month_dropdown.get()
    year_of_expense = app.select_year_dropdown.get()
    date_is_correct = validateDate(day_of_expense, month_of_expense, year_of_expense)
    print(date_is_correct)

def addFunds():
    print("Funds added")

def addIncome():
    print("Income added")