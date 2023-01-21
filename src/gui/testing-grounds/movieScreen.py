from tkinter import *
import customtkinter

ws = customtkinter.CTk()
width = 400 # Width 
height = 250 # Height
 
screen_width = ws.winfo_screenwidth()  # Width of the screen
screen_height = ws.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
ws.geometry("{}x{}+{}+{}".format(width, height, int(x), int(y)))

# f = ("Times bold", 14)

# def prevPage():
#     ws.destroy()
#     import homeScreen
    
# Label(
#     ws,
#     text="This is First page",
#     padx=20,
#     pady=20,
#     bg='#5d8a82',
#     font=f
# ).pack(expand=True, fill=BOTH)

# Button(
#     ws, 
#     text="Previous Page", 
#     font=f,
#     command=prevPage
#     ).pack(fill=X, expand=TRUE, side=LEFT)

# button = ws.CTkButton(master=ws, text="prev", command=prevPage)



ws.mainloop()