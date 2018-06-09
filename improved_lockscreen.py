from tkinter import *

from tkinter import messagebox


def test():
    if username.get().rstrip()=="sv" and password.get().rstrip()=='sv':
        messagebox.showinfo("Access Granted!","Welcome master!")
    else:
        messagebox.showinfo("Access Denied!","Go away,stranger!")
                                    
main=Tk()



main.mainloop()

