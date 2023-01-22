from tkinter import *
from PIL import *
import customtkinter


state = False
def click(event):
    gameInput.config(state=NORMAL)
    gameInput.delete(0,END)

def press(event):
    frame1.lower()
    frame2.lift()
    state = True
    frame2.lift()
    frame2.place(x=5, y=5)

def prev():
    frame2.lower()
    frame1.lift()
    state = False

window = Tk()
window.title = "Video Game to Movie Recommender"
width = 923
height = 641
window.geometry("923x641")

# # Search function

frame1 = Frame(window, bg='#a2b0a5')
labelSearch = Label(frame1,text="I like playing...", bg='#a2b0a5',font=("Arial", 25))
gameInput = Entry(frame1, font=("Arial", 25))
gameInput.insert(0,"name of game")
gameInput.config(state=DISABLED)
gameInput.bind("<Button-1>", click)
gameInput.bind("<Return>", press)
frame1.place(x=width/2-40,y=height/2-80)

frame2 = Frame(window, bg='black', width=width, height=height)
#back_btn = PhotoImage(file="back.png")
b = Button(frame2, text="return", command=prev, bg='#d5f7e3',width=8, height=2, font=("Arial", 12))
b.pack()

labelSearch.pack()
gameInput.pack()

bg = PhotoImage(file = "home Background.png")
background = Label(window, image = bg)
background.lower()
background.place(x = 0, y = 0)

background.pack()

mainloop()

# if __name__ == "__main__": GUI()
#
# #window = customtkinter.CTk()
# window = Tk()
# width = 1920 # Width
# height = 1080 # Height
# window.geometry(f'{width}x{height}+{-10}+{0}')
#
# # Set Background image
# bg = PhotoImage(file = "home Background.png")
# background = Label(window, image = bg)
# # background.place(x = 0, y = 0)
# background.pack()
#
# def click(event):
#     gameInput.config(state=NORMAL)
#     gameInput.delete(0,END)
#
# def press(event):
#     window.destroy()
#     import movieScreen
#
#
# # Search function
# labelSearch = Label(window,text = "I like playing...")
# gameInput = Entry(window)
# gameInput.insert(0,"name of game")
# gameInput.config(state=DISABLED)
# gameInput.bind("<Button-1>", click)
#
# gameInput.bind("<Return>", press)
#
# labelSearch.pack()
# gameInput.pack()
#
#
# window.mainloop()