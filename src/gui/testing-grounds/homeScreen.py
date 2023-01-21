from tkinter import *
import customtkinter


window = customtkinter.CTk()
#window = Tk()
window.geometry('1920x1080')

def click(event):
    gameInput.config(state=NORMAL)
    gameInput.delete(0,END)

def press(event):
    window.destroy()
    import movieScreen


# Search function
labelSearch = Label(window,text = "I like playing...")
gameInput = Entry(window)
gameInput.insert(0,"name of game")
gameInput.config(state=DISABLED)
gameInput.bind("<Button-1>", click)

gameInput.bind("<Return>", press)

labelSearch.pack()
gameInput.pack()


window.mainloop()