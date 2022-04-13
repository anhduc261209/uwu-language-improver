from tkinter import *
from tkinter.scrolledtext import ScrolledText
import os

def clear():
    inputfield.delete(1.0, END)

def improve():
    outputfield.delete(1.0, END)
    string = inputfield.get(1.0, END)
    string = string.replace("l", "w")
    string = string.replace("r", "w")
    print(string)
    outputfield.insert(1.0, string)

# Initialize
root = Tk()
root.title("UWU Language Improver")
root.geometry("400x300")
root.iconbitmap(os.path.join(os.getcwd(), 'uwu.ico'))

# Text frame
text_frame = Frame(root)
text_frame.pack(pady = 20)

# Components in text frame
inputfield = ScrolledText(text_frame, width = 15, height = 10, font = ("Mv Boli", 13))
inputfield.grid(row = 0, column = 0)
# Set the cursor to inputfield
inputfield.focus()
outputfield = ScrolledText(text_frame, width = 15, height = 10, font = ("Mv Boli", 13))
outputfield.grid(row = 0, column = 1)

# Button frame
button_frame = Frame(root)
button_frame.pack(pady = 0)

# Components in button frame

clear_btn = Button(button_frame, font = ("MV Boli", 10), text = "Clear", command = clear)
clear_btn.grid(row = 0, column = 0, padx = 20)

improve_btn = Button(button_frame, font = ("MV Boli", 10), text = "UWU!", command = improve)
improve_btn.grid(row = 0, column = 1, padx = 20)

root.mainloop()