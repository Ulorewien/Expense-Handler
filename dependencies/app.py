import threading
from tkinter import *
from tkinter import ttk
from dependencies.specifications import *
from dependencies.date import *
from dependencies.data import *

page_number = ""

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.Window.quit()

    def run(self):
        # print("App is running...")
        self.specs = getSpecifications()
        self.bg_color = self.specs["Application"]["background_color"]
        self.font_headers = self.specs["Application"]["font"] + " " + self.specs["Font_size"]["headers"]
        self.font_labels = self.specs["Application"]["font"] + " " + self.specs["Font_size"]["labels"]
        self.font_buttons = self.specs["Application"]["font"] + " " + self.specs["Font_size"]["buttons"]
        self.font_inputs = self.specs["Application"]["font"] + " " + self.specs["Font_size"]["inputs"]
        self.Window = Tk()
        self.Window.title("Expense Handler")
        self.Window.configure(bg = self.bg_color)
        self.Window.resizable(False, False)
        self.Window.geometry(self.specs["Application"]["width"] + "x" + self.specs["Application"]["height"])
        self.drawMenuBar()
        self.homePage()
        self.Window.mainloop()

    def drawMenuBar(self):
        self.menubar = Menu(self.Window)
        self.options = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Options", menu = self.options)
        self.options.add_command(label = "Home", command = lambda:self.destroyPage(self.specs["Pages"]["home_page"]))
        self.options.add_command(label = "Expense", command = lambda:self.destroyPage(self.specs["Pages"]["expense_page"]))
        self.options.add_command(label = "Funds", command = lambda:self.destroyPage(self.specs["Pages"]["funds_page"]))
        self.options.add_command(label = "Income", command = lambda:self.destroyPage(self.specs["Pages"]["income_page"]))
        self.options.add_separator()
        self.options.add_command(label = "Exit", command = self.Window.destroy)
        self.Window.config(menu = self.menubar)

    def homePage(self):
        self.select_entry_label = Label(self.Window, text = "Select the type of entry", font = self.font_headers, background = self.bg_color)
        self.select_entry_label.place(relx = 0.5, rely = 0.15, anchor = "center")
        self.expense_button = Button(self.Window, text = "Expense", relief = RAISED, font = self.font_buttons, command = lambda:self.destroyPage(self.specs["Pages"]["expense_page"]))
        self.expense_button.place(relx = 0.2, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.funds_button = Button(self.Window, text = "Funds", relief = RAISED, font = self.font_buttons, command = lambda:self.destroyPage(self.specs["Pages"]["funds_page"]))
        self.funds_button.place(relx = 0.5, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.income_button = Button(self.Window, text = "Income", relief = RAISED, font = self.font_buttons, command = lambda:self.destroyPage(self.specs["Pages"]["income_page"]))
        self.income_button.place(relx = 0.8, rely = 0.4, relwidth = 0.2, anchor = "center")

    def addExpensePage(self):
        self.expense_header_label = Label(self.Window, text = "Expense", font = self.font_headers, background = self.bg_color)
        self.expense_header_label.place(relx = 0.5, rely = 0.1, anchor = "center")
        self.select_date_label = Label(self.Window,  text = "Select the date : ", font = self.font_labels, background = self.bg_color)
        self.select_date_label.place(relx = 0.2, rely = 0.25, anchor = "center")
        self.select_day_variable = StringVar()
        self.select_day_dropdown = ttk.Combobox(self.Window, textvariable = self.select_day_variable, background = self.bg_color)
        self.select_day_dropdown["values"] = getDayList()
        self.select_day_dropdown.place(relx = 0.45, rely = 0.25, relwidth= 0.15, anchor = "center")
        self.select_month_variable = StringVar()
        self.select_month_dropdown = ttk.Combobox(self.Window, textvariable = self.select_month_variable, background = self.bg_color)
        self.select_month_dropdown["values"] = getShortMonthList()
        self.select_month_dropdown.place(relx = 0.65, rely = 0.25, relwidth= 0.15, anchor = "center")
        self.select_year_variable = StringVar()
        self.select_year_dropdown = ttk.Combobox(self.Window, textvariable = self.select_year_variable, background = self.bg_color)
        self.select_year_dropdown["values"] = getYearList()
        self.select_year_dropdown.place(relx = 0.85, rely = 0.25, relwidth= 0.15, anchor = "center")
        self.expense_type_label = Label(self.Window,  text = "Type of expense : ", font = self.font_labels, background = self.bg_color)
        self.expense_type_label.place(relx = 0.2, rely = 0.4, anchor = "center")
        self.expense_type_variable = StringVar()
        self.expense_type_dropdown = ttk.Combobox(self.Window, textvariable = self.expense_type_variable, background = self.bg_color)
        self.expense_type_dropdown["values"] = ["Food", "Cab"]
        self.expense_type_dropdown.place(relx = 0.45, rely = 0.4, relwidth= 0.2, anchor = "center")
        self.expense_amount_label = Label(self.Window, text = "Amount : ", font = self.font_labels, background = self.bg_color)
        self.expense_amount_label.place(relx = 0.2, rely = 0.55, anchor = "center")
        self.expense_amount_entry = Entry(self.Window, font = self.font_inputs, background = self.bg_color)
        self.expense_amount_entry.place(relx = 0.45, rely = 0.55, relwidth = 0.2, anchor = "center")
        self.mode_of_payment_label = Label(self.Window, text = "Payment method : ", font = self.font_labels, background = self.bg_color)
        self.mode_of_payment_label.place(relx = 0.2, rely = 0.7, anchor = "center")
        self.mode_of_payment_variable = StringVar()
        self.mode_of_payment_dropdown = ttk.Combobox(self.Window, textvariable = self.mode_of_payment_variable, background = self.bg_color)
        self.mode_of_payment_dropdown["values"] = ["Gpay", "Cash"]
        self.mode_of_payment_dropdown.place(relx = 0.45, rely = 0.7, relwidth = 0.2, anchor = "center")
        self.add_expense_button = Button(self.Window, text = "Add Expense", relief = RAISED, font = self.font_buttons, command = lambda:addExpense(self))
        self.add_expense_button.place(relx = 0.5, rely = 0.85, relwidth = 0.3, anchor = "center")

    def addFundsPage(self):
        self.funds_header_label = Label(self.Window, text = "Funds", font = self.font_headers, background = self.bg_color)
        self.funds_header_label.place(relx = 0.5, rely = 0.1, anchor = "center")
        self.select_date_label = Label(self.Window,  text = "Select the date : ", font = self.font_labels, background = self.bg_color)
        self.select_date_label.place(relx = 0.2, rely = 0.25, anchor = "center")
        self.select_day_variable = StringVar()
        self.select_day_dropdown = ttk.Combobox(self.Window, textvariable = self.select_day_variable, background = self.bg_color)
        self.select_day_dropdown["values"] = getDayList()
        self.select_day_dropdown.place(relx = 0.45, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.select_month_variable = StringVar()
        self.select_month_dropdown = ttk.Combobox(self.Window, textvariable = self.select_month_variable, background = self.bg_color)
        self.select_month_dropdown["values"] = getShortMonthList()
        self.select_month_dropdown.place(relx = 0.65, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.select_year_variable = StringVar()
        self.select_year_dropdown = ttk.Combobox(self.Window, textvariable = self.select_year_variable, background = self.bg_color)
        self.select_year_dropdown["values"] = getYearList()
        self.select_year_dropdown.place(relx = 0.85, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.funds_amount_label = Label(self.Window, text = "Amount : ", font = self.font_labels, background = self.bg_color)
        self.funds_amount_label.place(relx = 0.2, rely = 0.4, anchor = "center")
        self.funds_amount_entry = Entry(self.Window, font = self.font_inputs, background = self.bg_color)
        self.funds_amount_entry.place(relx = 0.45, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.mode_of_payment_label = Label(self.Window, text = "Payment method : ", font = self.font_labels, background = self.bg_color)
        self.mode_of_payment_label.place(relx = 0.2, rely = 0.55, anchor = "center")
        self.mode_of_payment_variable = StringVar()
        self.mode_of_payment_dropdown = ttk.Combobox(self.Window, textvariable = self.mode_of_payment_variable, background = self.bg_color)
        self.mode_of_payment_dropdown["values"] = ["Gpay", "Cash"]
        self.mode_of_payment_dropdown.place(relx = 0.45, rely = 0.55, relwidth = 0.2, anchor = "center")
        self.add_funds_button = Button(self.Window, text = "Add Funds", relief = RAISED, font = self.font_buttons, command = lambda:addFunds(self))
        self.add_funds_button.place(relx = 0.5, rely = 0.7, relwidth = 0.3, anchor = "center")

    def addIncomePage(self):
        self.income_header_label = Label(self.Window, text = "Income", font = self.font_headers, background = self.bg_color)
        self.income_header_label.place(relx = 0.5, rely = 0.1, anchor = "center")
        self.select_date_label = Label(self.Window,  text = "Select the date : ", font = self.font_labels, background = self.bg_color)
        self.select_date_label.place(relx = 0.2, rely = 0.25, anchor = "center")
        self.select_day_variable = StringVar()
        self.select_day_dropdown = ttk.Combobox(self.Window, textvariable = self.select_day_variable, background = self.bg_color)
        self.select_day_dropdown["values"] = getDayList()
        self.select_day_dropdown.place(relx = 0.45, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.select_month_variable = StringVar()
        self.select_month_dropdown = ttk.Combobox(self.Window, textvariable = self.select_month_variable, background = self.bg_color)
        self.select_month_dropdown["values"] = getShortMonthList()
        self.select_month_dropdown.place(relx = 0.65, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.select_year_variable = StringVar()
        self.select_year_dropdown = ttk.Combobox(self.Window, textvariable = self.select_year_variable, background = self.bg_color)
        self.select_year_dropdown["values"] = getYearList()
        self.select_year_dropdown.place(relx = 0.85, rely = 0.25, relwidth = 0.15, anchor = "center")
        self.income_type_label = Label(self.Window,  text = "Type of income : ", font = self.font_labels, background = self.bg_color)
        self.income_type_label.place(relx = 0.2, rely = 0.4, anchor = "center")
        self.income_type_variable = StringVar()
        self.income_type_dropdown = ttk.Combobox(self.Window, textvariable = self.income_type_variable, background = self.bg_color)
        self.income_type_dropdown["values"] = ["Food", "Cab"]
        self.income_type_dropdown.place(relx = 0.45, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.income_amount_label = Label(self.Window, text = "Amount : ", font = self.font_labels, background = self.bg_color)
        self.income_amount_label.place(relx = 0.2, rely = 0.55, anchor = "center")
        self.income_amount_entry = Entry(self.Window, font = self.font_inputs, background = self.bg_color)
        self.income_amount_entry.place(relx = 0.45, rely = 0.55, relwidth = 0.2, anchor = "center")
        self.add_income_button = Button(self.Window, text = "Add Income", relief = RAISED, font = self.font_buttons, command = lambda:addIncome(self))
        self.add_income_button.place(relx = 0.5, rely = 0.7, relwidth = 0.3, anchor = "center")

    def destroyPage(self, next_page_number):
        global page_number
        for widget in self.Window.winfo_children():
            widget.destroy()
        self.drawMenuBar()
        if(next_page_number == self.specs["Pages"]["home_page"]):
            self.homePage()
        elif(next_page_number == self.specs["Pages"]["expense_page"]):
            self.addExpensePage()
        elif(next_page_number == self.specs["Pages"]["funds_page"]):
            self.addFundsPage()
        elif(next_page_number == self.specs["Pages"]["income_page"]):
            self.addIncomePage()