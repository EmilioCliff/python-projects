from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
# import pandas

password = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# def search():
#     data_read = pandas.read_csv("password.txt")
#     website_data = [[row.website, row.email, row.password] for (index, row) in data_read.iterrows()
#                     if row.website == website_entry.get().lower()]
#     if len(website_data) > 0:
#         messagebox.showinfo(title=website_data[0][0], message=f"Here is your:\n Email: {website_data[0][1]}\n "
#                                                               f"Password: {website_data[0][2]}")
#     else:
#         messagebox.showinfo(title="No data found", message=f"There is no saved data of the {website_data[0][0]} "
#                                                            f"website provided")

def search():
    website = website_entry.get()
    try:
        with open("password2.json", "r") as file_data:
            data_read = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No DataFile Found")
    else:
        if website in data_read:
            messagebox.showinfo(title=website, message=f"Email: {data_read[website]['email']}\n "
                                                       f"Password: {data_read[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} website")


def password_generator():
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    global password
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_generated = password_entry.get()
    details_dict = {
        website_name: {
            "email": email_name,
            "password": password_generated
        }
    }
    if len(website_name) == 0 or len(password_generated) == 0:
        messagebox.showerror(title="error", message="Please don't leave any blanks")
        return
    # is_ok = messagebox.askokcancel(title=f"{website_name}", message=f"These are the details entered \n"
    #                                                                 f"Email: {email_name} \n"
    #                                                                 f"Password: {password_generated} \n"
    #                                                                 f"Is it ok?")
    # if is_ok:
    try:
        with open("password2.json", "r") as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        with open("password2.json", 'w') as passwords:
            json.dump(details_dict, passwords, indent=4)
    else:
        data.update(details_dict)
        with open("password2.json", "w") as passwords:
            json.dump(data, passwords, indent=4)


    # passwords.write(f"\n{website_name},{email_name},{password_generated}")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.attributes("-alpha", 1)

canvas = Canvas(width=200, height=200)
my_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
email_entry = Entry(width=40)
email_entry.insert(END, "emiliocliff@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

website_label = Label(text="Password")
website_label.grid(column=0, row=3)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15 ,command=search)
search_button.grid(row=1, column=2)

window.mainloop()
