#!/usr/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('TextEditor!')
root.iconbitmap('text editor logo.png')
root.geometry("1200x660")

#create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#create scrollbar for textbox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


#Let's create the text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True,                                                    yscrollcommand=text_scroll.set)
my_text.pack()

#configure the scroll bar
text_scroll.config(command=my_text.yview)

#Lets create the menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")

#Add Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Redo")

#status bar at the bottom of app
status_bar = Label(root, text='Ready ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
