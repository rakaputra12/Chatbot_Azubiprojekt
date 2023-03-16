import random

jokes = ["Yo my Menn das ist Me!"]
number = random.randrange(0,3)


import tkinter 

window = tkinter.Tk()
y = 0

print(number)
window.geometry("700x200")
tkinter.Label(window, text=jokes[number], font="Helvetica 16 bold").pack()

window.mainloop()


'''import tkinter as tk

window = tk.Tk()
y = 0

def sayHi():
    global y
    y += 1
    print(y)xs

window.geometry("200x100")
b = tk.Button(
    window,
    text='click here',
    command=sayHi
)

b.pack()
window.mainloop()'''