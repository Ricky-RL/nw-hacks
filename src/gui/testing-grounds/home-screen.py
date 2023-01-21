from tkinter import *

window = Tk()

def click(event):
    gameInput.config(state=NORMAL)
    gameInput.delete(0,END)


# Search function
labelSearch = Label(window,text = "I like playing...")
gameInput = Entry(window)
gameInput.insert(0,"name of game")
gameInput.config(state=DISABLED)
gameInput.bind("<Button-1>", click)

labelSearch.pack()
gameInput.pack()


mainloop()