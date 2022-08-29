from dependencies.date import *
from dependencies.data_storage import *
from dependencies.data_retrieval import *

def addExpense(app):
    day_of_expense = app.select_day_dropdown.get()
    month_of_expense = app.select_month_dropdown.get()
    year_of_expense = app.select_year_dropdown.get()
    type_of_expense = app.expense_type_dropdown.get()
    amount_of_expense = app.expense_amount_entry.get()
    mode_of_payment = app.mode_of_payment_dropdown.get()

    date_is_correct = validateDate(day_of_expense, month_of_expense, year_of_expense)
    if(date_is_correct == "Future Date"):
        app.date_validation_variable.set(date_is_correct)
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    elif(not date_is_correct):
        app.date_validation_variable.set("Enter a valid date")
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.date_validation_variable.set("")

    type_of_expense_list = getExpenseTypeList()
    if(type_of_expense not in type_of_expense_list):
        app.type_validation_variable.set("This type does not exist")
        app.type_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.type_validation_variable.set("")

    try:
        amount_of_expense = int(amount_of_expense)
    except:
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    if(not isinstance(amount_of_expense, int)):
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.amount_validation_variable.set("")

    mode_of_payment_list = getExpenseModeList()
    if(mode_of_payment not in mode_of_payment_list):
        app.mode_validation_variable.set("This payment method does not exist")
        app.mode_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.mode_validation_variable.set("")

    data = {
        "Date" : day_of_expense + month_of_expense + year_of_expense,
        "Type" : type_of_expense,
        "Amount" : amount_of_expense,
        "Mode" : mode_of_payment,
        "Month" : month_of_expense,
    }
    addExpenseData(data)

def addFunds():
    print("Funds added")

def addIncome():
    print("Income added")