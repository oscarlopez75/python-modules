import datetime


class dateFormatClass:
    now = None
    day = None
    month = None
    year = None
    dayName = None
    dayStr = None
    monthStr = None
    allOk = True



    def __init__(self):
        try:
            self.now = datetime.datetime.now()  # Gets the current date
        except:
            self.allOk = False
        else:
            self.addZero()
            self.formatDayMonth()


    #Adds a leading zero if the date or the month is less than 10
    def addZero(self):
        if self.now.day < 10:
            self.day = "0" + str(self.now.day)
        else:
            self.day = str(self.now.day)

        if self.now.month < 10:
            self.month = "0" + str(self.now.month)
        else:
            self.month = str(self.now.month)

        self.year = str(self.now.year)

    #Gets the day name and the month
    def formatDayMonth(self):
        self.dayName = self.getDayOfWeek(self.now.weekday())
        self.dayStr = self.day + self.getDaySub(self.now.day)
        self.monthStr = self.getMonth(self.now.month)

    #You can use this for testing
    def displayDate(self):
        if self.allOk:
            print(self.now)
        else:
            print("Error")

    #Returns the date in EU format
    def displayDateEu(self):

        if self.allOk:
            return self.day + "/" + self.month + "/" + self.year
        else:
            return "Error"

    # Returns the date in US format
    def displayDateUs(self):

        if self.allOk:
            return self.month + "/" + self.day + "/" + self.year
        else:
            return "Error"

    def getDayOfWeek(self, dayNumber):

        daysWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        return daysWeek[dayNumber]

    def getDaySub(self, day):

        daySub = ['none', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th'
            , 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st', 'nd', 'rd' 'th', 'th'
            , 'th', 'th', 'th', 'th', 'th', 'st']

        return daySub[day]

    def getMonth(self, month):
        monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July'
            , 'August', 'September', 'October', 'November', 'December']

        return monthName[month - 1]

    def displayDateEuSt(self):

        if self.allOk:
            return self.dayName + " " + self.dayStr + " of " + self.monthStr + ", " + self.year
        else:
            return "Error"

    def displayDateUsSt(self):

        if self.allOk:
            return self.dayName + " " + self.monthStr + " " + self.dayStr + ", " + self.year
        else:
            return "Error"

    def dateJson(self):

        if self.allOk:
            dateJson = {"day_number": str(self.day), "month_number": str(self.month), "year": str(self.year)
            , "day_name": self.dayName, "day_sub": self.dayStr, "month_name": self.monthStr}

            return dateJson
        else:
            dateJson = {"day_number": "Error", "month_number": "Error", "year": "Error"
                , "day_name": "Error", "day_sub": "Error", "month_name": "Error"}
            return dateJson