from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def password_gen():
    password_textbox.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_char = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_char + password_symbol + password_number
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = ''.join(password_list)
    password_textbox.insert(0, password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = website_textbox.get()
    user_info = user_textbox.get()
    pass_info = password_textbox.get()
    output = f"{website} | {user_info} | {pass_info}\n"
    # messagebox.showinfo(title="Title", message="this is test message")
    if len(website) == 0 or len(pass_info) == 0:
        messagebox.showerror(
            title="Opps", message="Enter Your Information Corretly")
    else:
        yes_or_no = messagebox.askyesno(
            title="Confirm", message="Do You Want To Save The Information ? ")
        print(yes_or_no)
        if yes_or_no:
            with open("info.txt", "a") as file:
                file.write(output)
                website_textbox.delete(0, END)
                # user_textbox.delete(0, END)
                password_textbox.delete(0, END)
        else:
            website_textbox.delete(0, END)
            # user_textbox.delete(0, END)
            password_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)
website = Label(text="website", font=("Courier", 10))
website.grid(row=1, column=0)
website_textbox = Entry(width=35)
website_textbox.grid(row=1, column=1, columnspan=2)
user_input = Label(text="Email/Username", font=("Courier", 10))
user_textbox = Entry(width=35)
user_textbox.insert(0, "test@gmail.com")
user_textbox.grid(row=2, column=1, columnspan=2)
user_input.grid(row=2, column=0)
password = Label(text="password", font=("Courier", 10))
password_textbox = Entry(width=16)
password.grid(row=3, column=0)
password_textbox.grid(row=3, column=1)
password_gen_button = Button(text="generate password", command=password_gen)
password_gen_button.grid(row=3, column=2)
add_btn = Button(text="Add", width=33, command=save_info)
add_btn.grid(row=4, column=1, columnspan=2)
window.mainloop()
