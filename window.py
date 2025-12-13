from tkinter import *
from datetime import date

window = Tk()
window.title('Starting window')
window.geometry('600x700')

welcome_label = Label(text = "Hello there", fg="green", bg = "#00FFFF", height = 1, width = 600)
name_label =  Label(text = "Enter your full name", fg = "white", bg = "#0000FF", height = 1, width = 600)

name_entry = Entry()

def display():
    name = name_entry.get()
    greet = "Hello" + name + "\n"
    message = "Welcome to the application, today's date is:"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

button = Button(text = "begin", command=display, fg = "orange", bg="#FF0000", height=1, width = 50)
text_box = Text(height = 2)

welcome_label.pack()
name_label.pack()
name_entry.pack()
button.pack()
text_box.pack()

window.mainloop()




