from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    letters_list = [choice(letters) for letter in range(randint(8, 10))]
    symbols_list = [choice(symbols) for symbol in range(randint(2, 4))]
    numbers_list =[choice(numbers) for number in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
    # window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

    # canvas

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

    # three labels

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

user_label = Label(text="User/Email Name: ")
user_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

    # Entries

website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1)

user_entry = Entry(width=46)
user_entry.insert(0, "Screachail")
user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

    # Buttons

    # calls action() when pressed
generate_password_button = Button(text="Generate password", command=generate_password, width=20)
generate_password_button.grid(row=3, column=2, columnspan=2)

def find_password():
    try:
        with open("data.json", "r") as f:
            # Reading old data
            stored_password = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Sorry, we have no such file in the database")
    else:
        input_password = website_entry.get()
        if input_password in stored_password:
        #getting password from the JSON file
            password = stored_password[input_password].get("password")
            messagebox.showinfo(title="Your password", message=f"Website: {input_password} \nPassword: {password}")
        else:
            messagebox.showwarning(title="WARNING", message="Sorry, we have no such password in the database")

    # Buttons
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2, columnspan=1)

def add():
    get_website = website_entry.get()
    get_user = user_entry.get()
    get_password = password_entry.get()
    new_data = {
        get_website: {
            "email": get_user,
            "password": get_password,
        }
    }
    if get_website == "" or get_password == "" or get_user == "":
        messagebox.showwarning(title="WARNING", message="Please don't leave any of the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry, message=f"These are the details entered: \nUser/Email: "
                                                                    f"{get_user} "
                                                                    f"\nPassword: {get_password} \nIs it okay to save?")

    if is_ok:
        try:
            with open("data.json", "r") as f:
                #Reading old data
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(new_data, f, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                #Saving updated data
                json.dump(data, f, indent=4)


        finally:
            messagebox.showinfo(title="Done!", message=f"Added {get_website} to the database")

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# calls action() when pressed
add_password_button = Button(text="Add", command=add, width=39)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
