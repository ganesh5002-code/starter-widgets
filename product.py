from tkinter import *

window = Tk()
window.title("Getting started with widgets")
window.geometry('400x300')

welcome_label = Label(text = "Hello there", fg= "blue", bg="#00FF00", height=1, width=400)

first_number_label = Label(text = "Enter your first number", fg= "white", bg = "#FFA500", height= 1, width= 400)
first_number_entry = Entry()

second_number_label = Label(text = "Enter your second number", fg= "white", bg = "#FF0059", height= 1, width= 400)

second_number_entry = Entry()

def display():
    first_num = float(first_number_entry.get())
    sec_num = float(second_number_entry.get())
    product = first_num * sec_num
    answer = f"The product of, {first_num} and, {sec_num} is: {product}\n"
    text_box.insert(END, answer)


button = Button(text= "Calculate", command= display, fg= "brown", bg= "#898935")
text_box = Text(height= 2)

welcome_label.pack()
first_number_label.pack()
first_number_entry.pack()
second_number_label.pack()
second_number_entry.pack()
button.pack()
text_box.pack()

window.mainloop()

