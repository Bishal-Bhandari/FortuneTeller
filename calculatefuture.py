from datetime import datetime


class algocal:
    def __init__(self,userdate):
       self.userdate = userdate

    def validate(self):
        try:
            dateuser = datetime.strptime(self.userdate, '%Y-%m-%d')
            print("hello form validation "+ str(dateuser))
            self.datecal(dateuser)
        except ValueError:
            raise ValueError("\nIncorrect data format, should be YYYY-MM-DD or YYYY.MM.DD")

    def datecal(self,dateuser):
        return print(dateuser)
