import random
import string
import customtkinter as ctk # type: ignore


# prepare functions
def generate_password():
    password_length = int(password_list.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(password_length))
    output.configure(text=password, font=("Ubuntu", 20))

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(output.cget("text"))

# create window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Password Generator")
root.geometry("300x200")

# create dropdown for password
password_list = ctk.CTkComboBox(root, values=[str(i) for i in range(8, 21)])
password_list.set("8")
password_list.pack(pady=5)

# create "generate" button
generate_button = ctk.CTkButton(root, text="GENERATE", command=generate_password)
generate_button.pack(pady=5)

# create "copy" button
copy_button = ctk.CTkButton(root, text="COPY", command=copy_password)
copy_button.pack(pady=5)

# create output window
output = ctk.CTkLabel(root, text="")
output.pack(pady=20)

# run
root.mainloop()