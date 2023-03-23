from tkinter import *

window = Tk()
window.minsize(width=500, height=250)
window.title("Mile to Km Converter")

input = Entry()
input.grid(column=1, row=0)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

is_equal = Label(text="is Equal to ")
is_equal.grid(column=0, row=1)

ans_label = Label(text=0)
ans_label.grid(column=1, row=1)


def answer():
    mile = int(input.get())
    km = mile * 1.609344
    ans_label.config(text=km)


button = Button(text="click me", command=answer)
button.grid()

window.mainloop()
