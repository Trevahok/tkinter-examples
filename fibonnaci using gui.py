from tkinter import *
from tkinter import messagebox
def  fib():
    n=number.get()
    first=1
    second=1
    fi=[1,1]
    for i in range(int(n)):
        third=first+second
        fi.append(third)
        first=second
        second=third
    messagebox.showinfo('fibonacci','\n'.join(map(str,fi)))


main=Tk()
main.title('Surprise Program')
number=Entry(main,bd=5)
number.pack(side=RIGHT)
text=Label(main,text="Enter the number :")
text.pack(side=LEFT)
gen_button=Button(main,text="generate",command=fib)
gen_button.pack(anchor ='s',expand=1,side=BOTTOM,fill=BOTH)
main.mainloop()


