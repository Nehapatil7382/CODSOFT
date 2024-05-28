import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
window = tk.Tk()
window.title("Calculator")
window.geometry('300x250') 
window.configure(bg='#000000')  

entry1 = tk.Entry(window, width=10, font=('Arial', 14), bg='#FFFFFF', fg='#000000')  
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(window, width=10, font=('Arial', 14), bg='#FFFFFF', fg='#000000')  
entry2.grid(row=0, column=1, padx=10, pady=10)

add_button = tk.Button(window, text="+", command=lambda: calculate('+'), width=5, height=2, font=('Arial', 14), bg='#FF0000', fg='#FFFFFF') 
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(window, text="-", command=lambda: calculate('-'), width=5, height=2, font=('Arial', 14), bg='#FF0000', fg='#FFFFFF')  
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(window, text="*", command=lambda: calculate('*'), width=5, height=2, font=('Arial', 14), bg='#FF0000', fg='#FFFFFF')  
multiply_button.grid(row=2, column=0, padx=5, pady=5)

divide_button = tk.Button(window, text="/", command=lambda: calculate('/'), width=5, height=2, font=('Arial', 14), bg='#FF0000', fg='#FFFFFF') 
divide_button.grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(window, text="Result:", font=('Arial', 14), bg='#000000', fg='#FFFFFF') 
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
window.mainloop()
