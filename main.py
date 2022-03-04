import pyttsx3

from calculatefuture import AlgoCal


def userchoice():
    userag = True
    print("WELCOME!!! LETS SEE YOUR FUTURE.\n")
    pyttsx3.speak("WELCOME!!! LETS SEE YOUR FUTURE.")
    while userag:  # if user want to perform the activity again
        userdate = str(input('Enter date(yyyy-mm-dd): '))
        try:
            classobj = AlgoCal(userdate)  # calling the class
            perchar = classobj.validate()
            print("\nYour characters according to given date are as follow: ")
            print("\nYour characters according solar cycle are:\n" + perchar[0])  # printing the char
            print("\nYour characters according lunar cycle are:\n" + perchar[1])  # printing the char
        except ValueError:
            print("Enter date in proper format.")
        loopchoice = str(input('\nIf you want to revisit then press "Y". If you want to exit press "N". ').upper())
        if loopchoice == "Y":
            userag = True
        else:
            userag = False


userchoice()
