import tkinter
from tkinter import messagebox
import random
import string


# Function to generate password
def gen_password(length, use_digits, use_upper, use_lower, use_special, add_rick):
    char_set = ""
    if use_digits == True:  # checks if the booleans given from the GUI box is T/F
        char_set += string.digits  # 0-9 library
    if use_upper:
        char_set += string.ascii_uppercase  # A-Z library
    if use_lower:
        char_set += string.ascii_lowercase  # a-z library
    if use_special:
        char_set += string.punctuation  # special char library
    if add_rick:  # the word rick
        char_set += "rick"

    if char_set == "":  # if no boxes ticked show this
        messagebox.showwarning("Input Error", "Please tick at least one box")
        return ""

    password = ''.join(random.choice(char_set) for i in range(length))
    return password


# Function to update the password field
def update_password():
    try:  # gets the booleans outcome from the GUI
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_special = special_var.get()
        add_rick = add_rick_var.get()
        # calls function gen password
        password = gen_password(length, use_digits, use_upper, use_lower, use_special, add_rick)
        password_entry.delete(0, tkinter.END)  # removes previous + adds new
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for length")


# Setting up the GUI
root = tkinter.Tk()
root.title("Password Generator")

tkinter.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tkinter.Entry(root)
length_entry.grid(row=0, column=1)

digits_var = tkinter.BooleanVar()  # these are the buttons + position + text
tkinter.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=1, column=0, sticky="w")

upper_var = tkinter.BooleanVar()
tkinter.Checkbutton(root, text="Include Uppercase", variable=upper_var).grid(row=2, column=0, sticky="w")

lower_var = tkinter.BooleanVar()
tkinter.Checkbutton(root, text="Include Lowercase", variable=lower_var).grid(row=3, column=0, sticky="w")

special_var = tkinter.BooleanVar()
tkinter.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, column=0, sticky="w")

add_rick_var = tkinter.BooleanVar()
tkinter.Checkbutton(root, text="Include RICK?", variable=add_rick_var).grid(row=5, column=0, sticky="w")

#  calls the fuction "update_password"
tkinter.Button(root, text="Generate Password", command=update_password).grid(row=6, column=0, columnspan=2)

tkinter.Label(root, text="Generated Password:").grid(row=7, column=0)
password_entry = tkinter.Entry(root)
password_entry.grid(row=7, column=1)

root.mainloop()
