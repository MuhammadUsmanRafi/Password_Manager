import random
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_hold = password_entry.get()
    if len(password_hold) == 0:
        password_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def adding_data():
    name_of_website = website_entry.get()
    name_of_user = Email_Username_entry.get()
    password_hidden = password_entry.get()
    if len(name_of_website) == 0:
        messagebox.showerror(title="Empty Field", message="Enter a name of the website\nPlease!")
    elif len(password_hidden) == 0:
        messagebox.showerror(title="Empty Field", message="Enter a password!")
    else:
        is_ok = messagebox.askokcancel(title="Detail Check", message=f"These are the detailed entered: \n Email:  "
                                                                     f"{name_of_user}\n  Password:  {password_hidden}\n"
                                                                     f" Are you sure to save these info?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{name_of_website}   |   {name_of_user}   |   {password_hidden}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", background="white", font=("Arial", "12"))
website_label.grid(row=1, column=0, sticky="nsew")

Email_Username_label = Label(text="Email/Username:", background="white", font=("Arial", "12"))
Email_Username_label.grid(row=2, column=0, sticky="nsew")

password_label = Label(text="Password:", background="white", font=("Arial", "12"))
password_label.grid(row=3, column=0, sticky="nsew")

website_entry = Entry(background="white", width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="nsew")
website_entry.focus()

Email_Username_entry = Entry(background="white", width=35)
Email_Username_entry.insert(0, "musmanrajputt490@gmail.com")
Email_Username_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")

password_entry = Entry(background="white", width=21)
password_entry.grid(row=3, column=1, sticky="nsew")

generate_password_button = Button(text="Generate Password", background="white", foreground="black",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="nsew")

add_button = Button(text="Add", background="white", foreground="black", width=35, command=adding_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")

window.mainloop()