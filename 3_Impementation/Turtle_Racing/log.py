"""login"""
from tkinter import *


def login_details():
    """Login Details"""
    print("Enter User name For set user name:")
    user=input()
    print("Enter password For set password:")
    pas=input()
    print("--------****************____________")
    print(" Varify yours Login Credentail !")
    print("Enter User Name:")
    name=input()
    print("Enter Password:")
    password=input()

    if(name==user and password==pas):
        print("You Sucessfully Log_in")
        import main
        return 0
    else:
        print("Incorrect login credential")
    return 0

# Create Object
root = Tk()

# Initialize tkinter window with dimensions 400x150
root.geometry('400x150')
root.title('Login For Start Racing !')

# Set the position of button on the top of window
btn1=Button(root, text="Login", command=login_details)
btn1.pack(side='top')

root.mainloop()
