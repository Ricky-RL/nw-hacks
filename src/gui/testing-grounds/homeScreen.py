from tkinter import *
import customtkinter


window = customtkinter.CTk()
#window = Tk()
# width = 1600 # Width 
# height = 900 # Height
# window.geometry(f'{width}x{height}+{-10}+{0}')

# Set Background image
bg = PhotoImage(file = "home Background.png")
background = Label(window, image = bg)
# background.place(x = 0, y = 0)
background.pack()

# def click(event):
#     gameInput.config(state=NORMAL)
#     gameInput.delete(0,END)

# def press(event):
#     window.destroy()
#     import movieScreen


# # Search function
# labelSearch = Label(window,text = "I like playing...")
# gameInput = Entry(window)
# gameInput.insert(0,"name of game")
# gameInput.config(state=DISABLED)
# gameInput.bind("<Button-1>", click)

# gameInput.bind("<Return>", press)

# labelSearch.pack()
# gameInput.pack()


window.mainloop()