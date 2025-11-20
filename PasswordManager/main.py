from random import shuffle
from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','r','s','t',]
    numbers = ['1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','*','+']
    password_list = []

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password =  ''.join(password_list)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f" These are the details entered:"
                                                      f" \n Website: {website} "
                                                      f"\nEmail:{email} "
                                                      f"\nPasssword{password}"
                                                      f"\nIs it ok to save?")
        if is_ok:
            with open('data_password.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "alvaro2600@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

#Buttons
generate_passsword_button = Button(text="Generate Password", command=generate_password)
generate_passsword_button.grid(column=2, row=3)
addbutton = Button(text="Add", width=36, command=save)
addbutton.grid(column=1, row=4)

window.mainloop()
