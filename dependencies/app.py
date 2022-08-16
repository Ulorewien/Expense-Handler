import threading
from tkinter import *
from configparser import ConfigParser

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
        self.font_labels = self.specs["Application"]["font"] + self.specs["Font_size"]["labels"]
        self.font_buttons = self.specs["Application"]["font"] + self.specs["Font_size"]["buttons"]
        self.Window = Tk()
        self.Window.title("Expense Handler")
        self.Window.configure(bg = self.bg_color)
        self.Window.geometry(self.specs["Application"]["width"] + "x" + self.specs["Application"]["height"])
        self.select_entry_label = Label(self.Window, text = "Select the type of entry", font = self.font_labels, background = self.bg_color)
        self.select_entry_label.place(relx = 0.5, rely = 0.15, anchor = "center")
        self.expense_button = Button(self.Window, text = "Expense", relief = RAISED, font = self.font_buttons, command = lambda:self.addExpensePage())
        self.expense_button.place(relx = 0.2, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.funds_button = Button(self.Window, text = "Funds", relief = RAISED, font = self.font_buttons, command = lambda:self.addFundsPage())
        self.funds_button.place(relx = 0.5, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.income_button = Button(self.Window, text = "Income", relief = RAISED, font = self.font_buttons, command = lambda:self.addIncomePage())
        self.income_button.place(relx = 0.8, rely = 0.4, relwidth = 0.2, anchor = "center")
        self.Window.mainloop()

    def addExpensePage(self):
        print("This is the Expense Page.")

    def addFundsPage(self):
        print("This is the Funds Page.")

    def addIncomePage(self):
        print("This is the Income Page.")

def getSpecifications():
    file = "dependencies/specifications.ini"
    specs = ConfigParser()
    specs.read(file)
    return specs