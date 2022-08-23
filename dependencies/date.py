from datetime import date
import pandas as pd

def getDayList():
    day_list = list(range(1,32))
    return day_list

def getMonthList():
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_list

def getShortMonthList():
    short_month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return short_month_list

def getYearList():
    current_year = date.today().year
    year_list = list(range(current_year, current_year - 11, -1))
    return year_list