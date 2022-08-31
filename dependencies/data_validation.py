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
        "Day" : day_of_expense,
        "Month" : month_of_expense,
        "Year" : year_of_expense,
        "Type" : type_of_expense,
        "Amount" : amount_of_expense,
        "Mode" : mode_of_payment,
    }
    addExpenseData(data)

def addFunds(app):
    day_of_funds = app.select_day_dropdown.get()
    month_of_funds = app.select_month_dropdown.get()
    year_of_funds = app.select_year_dropdown.get()
    amount_of_funds = app.funds_amount_entry.get()
    mode_of_payment = app.mode_of_payment_dropdown.get()

    date_is_correct = validateDate(day_of_funds, month_of_funds, year_of_funds)
    if(date_is_correct == "Future Date"):
        app.date_validation_variable.set(date_is_correct)
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    elif(not date_is_correct):
        app.date_validation_variable.set("Enter a valid date")
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.date_validation_variable.set("")

    try:
        amount_of_funds = int(amount_of_funds)
    except:
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    if(not isinstance(amount_of_funds, int)):
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.amount_validation_variable.set("")

    mode_of_payment_list = getFundsModeList()
    if(mode_of_payment not in mode_of_payment_list):
        app.mode_validation_variable.set("This payment method does not exist")
        app.mode_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.mode_validation_variable.set("")

    data = {
        "Day" : day_of_funds,
        "Month" : month_of_funds,
        "Year" : year_of_funds,
        "Amount" : amount_of_funds,
        "Mode" : mode_of_payment,
    }
    addFundsData(data)

def addIncome(app):
    day_of_income = app.select_day_dropdown.get()
    month_of_income = app.select_month_dropdown.get()
    year_of_income = app.select_year_dropdown.get()
    type_of_income = app.income_type_dropdown.get()
    amount_of_income = app.income_amount_entry.get()

    date_is_correct = validateDate(day_of_income, month_of_income, year_of_income)
    if(date_is_correct == "Future Date"):
        app.date_validation_variable.set(date_is_correct)
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    elif(not date_is_correct):
        app.date_validation_variable.set("Enter a valid date")
        app.date_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.date_validation_variable.set("")

    type_of_income_list = getIncomeTypeList()
    if(type_of_income not in type_of_income_list):
        app.type_validation_variable.set("This type does not exist")
        app.type_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.type_validation_variable.set("")

    try:
        amount_of_income = int(amount_of_income)
    except:
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    if(not isinstance(amount_of_income, int)):
        app.amount_validation_variable.set("Enter a valid amount")
        app.amount_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.amount_validation_variable.set("")

    data = {
        "Day" : day_of_income,
        "Month" : month_of_income,
        "Year" : year_of_income,
        "Type" : type_of_income,
        "Amount" : amount_of_income,
    }
    addIncomeData(data)

def addExpenseTypeOrMode(app):
    expense_type = app.expense_type_entry.get()
    expense_mode = app.expense_mode_entry.get()

    if(not (expense_type.replace(" ","") or expense_mode.replace(" ",""))):
        app.entry_validation_variable.set("Enter at least one input")
        app.entry_validation_message.config(foreground = app.specs["Color"]["error"])
        return
    app.entry_validation_variable.set("")

    expense_type = expense_type.lstrip()
    expense_type = expense_type.rstrip()
    expense_mode = expense_mode.lstrip()
    expense_mode = expense_mode.rstrip()

    data = {
        "Type" : expense_type,
        "Mode" : expense_mode,
    }

    addExpenseTypeOrModeData(data)