
from tkinter import *

box = Tk()
box.geometry("300x300")

def b1_fun():
    print("B1 Pressed")
    
def b2_fun():
    print("B2 Pressed")


l = Label(box,
          text = "PYTHON GUI",
          font = 30)
m = Message(box,
            text = "Hello",
            font = 30)
b1 = Button(box,
           text = "B1",
           font = 20,
           command = b1_fun,
            bg = "red",
            height = 10,
            width = 10)
b2 = Button(box,
           text = "B2",
           font = 20,
           command = b2_fun,
            bg = "blue",
            height = 10,
            width = 10)

l.pack()
m.pack()
b1.pack(side = LEFT)
b2.pack(side = RIGHT)
box.mainloop()
