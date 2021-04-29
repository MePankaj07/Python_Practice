import calendar
def prinCalendar():
    year = int(input("Input the year : "))
    month = int(input("Input the month : "))
    print(calendar.month(year, month))
prinCalendar()