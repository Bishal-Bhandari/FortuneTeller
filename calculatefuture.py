from datetime import datetime
import pandas as pd


class AlgoCal:
    def __init__(self, userdate):
        self.userdate = userdate

    def validate(self):
        try:
            dateuser = datetime.strptime(self.userdate, '%Y-%m-%d')
            print("Your date of birth is: " + str(dateuser))
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
        yearcharver = excelyear['yearchar'].values  # reading year char column from file
        monthver = excelmonth['months'].values  # reading month column from file
        monthcharver = excelmonth['charmonth'].values  # reading month column from file
        return self.fortunecal(datemonth, dateyear, yearver, monthver, yearcharver, monthcharver)

    def fortunecal(self, datemonth, dateyear, yearver, monthver, yearcharver, monthcharver):
        for i in range(len(monthver)):  # for looping on basis of month
            if monthver[i] == datemonth:  # for checking the user month
                for j in range(len(yearver)):  # for looping on basis of year
                    try:
                        if yearver[j] == dateyear:  # for checking the user year
                            return yearcharver[j], monthcharver[i]
                    except ValueError:
                        print("No valid date found.")
