from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    for _ in range(randint(8, 12)):
        password_list += choice(letters)
    for _ in range(randint(2, 4)):
        password_list += choice(numbers)
    for _ in range(randint(1, 2)):
        password_list += choice(symbols)
    shuffle(password_list)
    password = f'{"".join(password_list)}'
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(message="Password saved to clipboard")
    

def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    if len(website) < 1:
        messagebox.showerror(title='Input Error', message="Please complete the Website field")
        website_entry.focus()
    elif len(password) < 8:
        messagebox.showerror(title='Input Error', message="Please complete the Password fields")
        password_entry.focus()
    elif len(email) < 10:
        messagebox.showerror(title='Input Error', message="Please complete the Email fields")
        username_entry.focus()
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\n'
                                                              f'Password: {password}\n Is it ok to save?')

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300)
logo_image = PhotoImage(file='img.png')
canvas.create_image(150, 150, image=logo_image)
canvas.grid(column=0, row=1, columnspan=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

website_entry = Entry(width=30)
website_entry.grid(sticky="W", column=1, row=2, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=3)

username_entry = Entry(width=30)
username_entry.grid(sticky="W", column=1, row=3, columnspan=2)
username_entry.insert(0, "youremail@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

password_entry = Entry(width=30)
password_entry.grid(sticky="W", column=1, row=4, columnspan=2)

password_button = Button(text="Generate Password", width=25, command=generate_password)
password_button.grid(sticky="W", column=1, row=5)

add_button = Button(text="Save to file", width=25, command=save)
add_button.grid(sticky="W", column=1, row=6)

window.mainloop()
