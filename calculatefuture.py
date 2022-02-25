from datetime import datetime
import pandas as pd


class algocal:
    def __init__(self, userdate):
        self.userdate = userdate

    def validate(self):
        try:
            dateuser = datetime.strptime(self.userdate, '%Y-%m-%d')
            print("hello form validation " + str(dateuser))
            perchar = self.fileread(dateuser)
            return perchar
        except ValueError:
            raise ValueError("\nIncorrect data format, should be YYYY-MM-DD or YYYY.MM.DD")

    def fileread(self, dateuser):
        dateyear = dateuser.year  # user given date
        datemonth = dateuser.month  # user given date
        excelyear = pd.read_excel(r'dateyear.xlsx')  # read file for year
        excelmonth = pd.read_excel(r'datemonth.xlsx')  # read file for month
        yearver = excelyear['year'].values  # reading year column from file
        monthver = excelmonth['months'].values  # reading month column from file
        self.fortunecal(datemonth, dateyear, yearver, monthver)

    def fortunecal(self, datemonth, dateyear, yearver, monthver):
        for x in range(0,12):
            if monthver[x] == datemonth:
                print("yes")


