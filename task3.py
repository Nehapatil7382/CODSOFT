import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Please enter positive integer!")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text="Generated Password: " + password, fg="#FF0000")  
    except ValueError as e:
        password_label.config(text=str(e), fg="#FF0000")

window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")
window.configure(bg="#E6E6FA") 

length_label = tk.Label(window, text="Password Length:", font=('Arial', 12), bg="#E6E6FA")  
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(window, width=10, font=('Arial', 12))
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=('Arial', 12), bg="#FFD700")  
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

password_label = tk.Label(window, text="", font=('Arial', 12), bg="#E6E6FA")  
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
