from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    dict = data.to_dict(orient='records')
else:
    dict = data.to_dict(orient='records')
# print(dict[0])

# --------------------------------FUNCTION--------------------------------#


def next_gen():
    global current, flip_timer
    current = random.choice(dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current["French"], fill="black")
    canvas.itemconfig(canvas_img, image=old_img)
    flip_timer = window.after(3000, next_slide)


def next_slide():
    canvas.itemconfig(canvas_img, image=new_img,)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current["English"], fill="white")


def is_known():
    dict.remove(current)
    print(len(dict))
    data = pd.DataFrame(dict)
    data.to_csv("data/word_to_learn.csv")
    next_gen()


# --------------------------------UI--------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, next_slide)
# canvas
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=old_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(
    400, 263, text="", font=("Ariel", 70, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, command=next_gen)
wrong_btn.grid(column=0, row=1)

check = PhotoImage(file="images/right.png")
check_btn = Button(image=check, command=is_known)
check_btn.grid(column=1, row=1)

next_gen()
window.mainloop()
