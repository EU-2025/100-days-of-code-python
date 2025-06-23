from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

EMAIL_EXAMPLE = "example@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for n in range(randint(8, 10))]
    symbols_list = [choice(symbols) for n in range(randint(2, 4))]
    numbers_list = [choice(numbers) for n in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    
    entry_password.delete(0, END)
    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    user_id = entry_user.get()
    password = entry_password.get()
    
    if website == "" or user_id == "" or password == "":
        messagebox.showinfo(title= "Oops",message="Please do not leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {user_id}"
                                f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        with open("data.txt", "a") as pass_file:
            pass_file.write(f"{website} | {user_id} | {password}\n")
            entry_website.delete(0,END)
            entry_password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website: ")
label_website.grid(column=0, row= 1,sticky="e")
label_user = Label(text="Email/Username: ")
label_user.grid(column=0, row= 2,sticky="e")
label_password = Label(text="Password: ")
label_password.grid(column=0, row= 3,sticky="e")

# Entry
entry_website = Entry(width=35, highlightthickness=0)
entry_website.grid(column=1, row=1, columnspan=2, sticky="we")
entry_website.focus()
entry_user = Entry(width=35, highlightthickness=0)
entry_user.grid(column=1, row=2, columnspan=2, sticky="we")
entry_user.insert(0,EMAIL_EXAMPLE)
entry_password = Entry(width=21, highlightthickness=0)
entry_password.grid(column=1, row=3, sticky="we")

# Buttons
button_gen_pass = Button(text="Generate Password", highlightthickness=0, command=generate_pass)
button_gen_pass.grid(column=2, row=3, sticky="w")
button_add = Button(text="Add", width=36, highlightthickness=0, command=save_data)
button_add.grid(column=1, row=4, columnspan=2, sticky="we")


window.mainloop()

