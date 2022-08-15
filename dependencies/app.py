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
        self.Window = Tk()
        self.Window.title("Expense Handler")
        self.Window.geometry(self.specs["Application"]["width"]+"x"+self.specs["Application"]["height"])
        self.select_entry_label = Label(self.Window, text="Select the type of entry")
        self.Window.mainloop()

def getSpecifications():
    file = "dependencies/specifications.ini"
    specs = ConfigParser()
    specs.read(file)
    return specs