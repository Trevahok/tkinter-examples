from tkinter import *
from tkinter import messagebox


def test():
    if username.get().rstrip()=="sv" and password.get().rstrip()=='sv':
        messagebox.showinfo("Access Granted!","Welcome master!")
    else:
        messagebox.showinfo("Access Denied!","Go away,stranger!")

main=Tk()
main.title("Login Screen")

quit_button=Button(main,text="Exit",command=main.destroy)
quit_button.pack(side=BOTTOM,fill=X)

check_button=Button(main,text="Check",command=test)
check_button.pack(side=BOTTOM,fill=X)

password=Entry(main,show="*")
password.pack(side=BOTTOM,fill=X)

text2=Label(main,text="Password:")
text2.pack(side=BOTTOM,fill=X)


username=Entry(main)
username.pack(side=BOTTOM,fill=X)
text=Label(main,text="Username:")
text.pack(side=BOTTOM,fill=X)

main.mainloop()
