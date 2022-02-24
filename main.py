from datetime import datetime
import pyttsx3
from calculatefuture import algocal

def userchoice():
    userag = True
    print("WELCOME!!! LETS SEE YOUR FUTURE.\n")
    pyttsx3.speak("WELCOME!!! LETS SEE YOUR FUTURE.")
    while userag:  # if user want to perform the activity again
        userdate = str(input('Enter date(yyyy-mm-dd): '))
        stripdate = datetime.strptime(userdate, "%Y-%m-%d")
        #print(stripdate.year)
        x = algocal(stripdate)
        x.datecal()

userchoice()
