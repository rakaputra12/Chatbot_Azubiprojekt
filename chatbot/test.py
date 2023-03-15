import random

jokes = ["Yo my Menn das ist Me!"]
number = random.randrange(0,3)


import tkinter 

window = tkinter.Tk()
y = 0

window.geometry("700x200")
tkinter.Label(window, text=jokes[number], font="Helvetica 16 bold").pack()
window.mainloop()