import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# -------------------------- PASSWORD GENERATOR --------------------------------------


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password_list = [random.choice(letters) for letter in range(random.randint(8, 12))]
    password_list += [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #    password += char
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


def clear_password():
    password_entry.delete(0, len(password_entry.get()))


# ----------------------------- PASSWORD DATA ----------------------------------------


def save_data():
    website_name = website_entry.get().lower()
    email_info = email_entry.get()
    password = password_entry.get()

    new_data = {
        website_name: {
            "email": email_info,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Don't leave fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, len(website_name))  # last=END is not being recognized
            password_entry.delete(0, len(password))


def find_password():
    website_name1 = website_entry.get().lower()
    with open("data.json") as password_dict:
        pass_dict = json.load(password_dict)
        try:
            website_name_dict = pass_dict[website_name1]
        except KeyError:
            messagebox.showwarning(title="No password for such website is saved", message="The password for the website you entered is not saved in database.")
        else:
            website_password = website_name_dict["password"]
            messagebox.showinfo(title="Your Password", message=f"Website: {website_name1}\nEmail: {website_name_dict['email']}\nPassword: {website_password}")


# --------------------------------- UI SETUP -----------------------------------------


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_img)
canvas.grid(row=0, column=1)

# LABELS

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# ENTRIES

website_entry = tkinter.Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=55)
email_entry.insert(0, "bagewaditarun@gmail.com")  # 0 is the index of the starting cursor
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=55)
password_entry.grid(row=3, column=1, columnspan=2)

# BUTTONS

add_button = tkinter.Button(text="Add", width=48, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

generate_button = tkinter.Button(text="Generate Password", command=generate_password, width=20)
generate_button.grid(row=4, column=1)

clear_password_button = tkinter.Button(text="Clear Password", command=clear_password, width=18)
clear_password_button.grid(row=4, column=2)

search_button = tkinter.Button(text="Search", width=18, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
