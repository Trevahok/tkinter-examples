from tkinter import *
from time import sleep
from math import sin
main=Tk()
main.title("testing stuff")
c=Canvas(main,bg="red",height=2000,width=2000)

cx=[73.6,10.6,62.9,26.9,79,26.9,52.2,46.3,68.2,30.3,52.2,30.3]

c.create_polygon(*map(lambda x: 10*x,cx),fill="yellow")
c.pack()
main.mainloop()


