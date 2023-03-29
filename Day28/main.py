import time
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(text_canvas, text="00:00")
    title.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title.config(text="Long Break", fg=GREEN, font=(
            FONT_NAME, 60, "italic"), bg=YELLOW)
        countDown(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Short Break", fg=GREEN, font=(
            FONT_NAME, 60, "italic"), bg=YELLOW)
        countDown(short_break_sec)
    else:
        title.config(text="Work Time", fg=GREEN, font=(
            FONT_NAME, 60, "italic"), bg=YELLOW)
        countDown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countDown(n):
    count_min = math.floor(n / 60)
    count_sec = n % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_canvas, text=f"{count_min}:{count_sec}")
    if n > 0:
        global timer
        timer = window.after(1000, countDown, n - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark.config(text="✓")


# countDown(10)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=112, bg=YELLOW)
window.title("Pomodoro")
# window.after(1000, countDown, 20)
title = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 60, "italic"), bg=YELLOW)
title.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_canvas = canvas.create_text(104, 130, text="00:00", fill="white",
                                 font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="reset", command=reset_time)
reset_button.grid(column=2, row=2)
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
checkmark.grid(column=1, row=3)
window.mainloop()
