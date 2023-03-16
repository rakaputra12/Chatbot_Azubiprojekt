#Foto
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("1000x400")

photo = tk.PhotoImage(file= "/Users/Rakaadita/Downloads/logiofix.png")

photo2 =Image.open("/Users/Rakaadita/Downloads/logiofix.png")
resized_image = photo2.resize((1000,300), Image.ANTIALIAS)
converted_image =ImageTk.PhotoImage(resized_image)

foto_label = tk.Label(window, image=photo, width=1000, height=300,bg="black",fg="yellow")
foto_label.pack()


window.mainloop()