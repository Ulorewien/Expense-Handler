from datetime import date

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

def getMonthNumber(month):
    month_list = getMonthList()
    short_month_list = getShortMonthList()
    try:
        return str(short_month_list.index(month) + 1)
    except:
        return str(month_list.index(month) + 1)

def validateDate(day, month, year):
    day = day.replace(" ","")
    month = month.replace(" ","")
    year = year.replace(" ","")
    if(day == "" or month == "" or year == ""):
        return False

    try:
        day = int(day)
        year = int(year)
    except:
        return False
    
    month_list = getMonthList()
    short_month_list = getShortMonthList()
    current_year = date.today().year
    current_month = date.today().month
    current_day = date.today().day
    if(day < 1 or day > 31 or year > current_year or year < current_year - 10):
        return False
    if((month not in month_list) and (month not in short_month_list)):
        return False
    
    try:
        month_index = month_list.index(month) + 1
    except:
        month_index = short_month_list.index(month) + 1
    if(year == current_year):
        if(month_index > current_month):
            return "Future Date"
        elif(month_index == current_month):
            if(day > current_day):
                return "Future Date"

    months_30 = ["April", "June", "September", "November"]
    months_31 = ["January", "March", "May", "July", "August", "October", "December"]
    short_months_30 = ["Apr", "Jun", "Sept", "Nov"]
    short_months_31 = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]

    if((month in months_30) or (month in short_months_30)):
        if(day <= 30):
            return True
        else:
            return False

    elif(month == "Feb" or month == "February"):
        if(year%4 == 0):
            if(day <= 29):
                return True
            else:
                return False
        else:
            if(day <= 28):
                return True
            else:
                return False
    
    return True