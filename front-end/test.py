from tkinter import *

window = Tk()

bg = PhotoImage(file = "bg image.png")

label1 = Label(window, image = bg)
label1.pack()

button = Button(window, text = "Click me")
button.pack()

window.mainloop()

