from calculatefuture import algocal


def userchoice():
    userag = True
    print("WELCOME!!! LETS SEE YOUR FUTURE.\n")
    # pyttsx3.speak("WELCOME!!! LETS SEE YOUR FUTURE.")
    while userag:  # if user want to perform the activity again
        userdate = str(input('Enter date(yyyy-mm-dd): '))
        try:
            classobj = algocal(userdate)  # calling the class
            classobj.validate()
        except ValueError:
            print("Enter date in proper format.")
        # print(stripdate.year)
        loopchoice = str(input('\nIf you want to revisit then press "Y". If you want to exit press "N". ').upper())
        if loopchoice == "Y":
            userag = True
        else:
            userag = False


userchoice()
