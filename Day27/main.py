from tkinter import *

window = Tk()
window.title("First GUI program")
window.minsize(500, 300)

my_label = Label(text="example", font=("Arial", 24))
# print(my_label)
my_label.grid(column=0, row=0)

# button


def click():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="click me", command=click)
button.grid(column=1, row=1)

button1 = Button(text="Button 2")
button1.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)
# print(input)
window.mainloop()
