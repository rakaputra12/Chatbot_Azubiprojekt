import tkinter as tk

window = tk.Tk()
y = 0

def sayHi():
    global y
    y += 1
    print(y)

window.geometry("200x100")
b = tk.Button(
    window,
    text='click here',
    command=sayHi
)

b.pack()
window.mainloop()