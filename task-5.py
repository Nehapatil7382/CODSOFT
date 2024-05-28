import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")
        self.root.configure(bg="#F0F0F0")
        
        self.contacts = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Name:", bg="#F0F0F0")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(self.root, text="Phone:", bg="#F0F0F0")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(self.root, text="Email:", bg="#F0F0F0")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(self.root, text="Address:", bg="#F0F0F0")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, bg="#008000", fg="#FFFFFF")
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts, bg="#008000", fg="#FFFFFF")
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, bg="#008000", fg="#FFFFFF")
        self.search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, bg="#008000", fg="#FFFFFF")
        self.update_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg="#008000", fg="#FFFFFF")
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone number are required!")
            
    def view_contacts(self):
        if self.contacts:
            contacts_window = tk.Toplevel(self.root)
            contacts_window.title("Contacts")
            contacts_window.geometry("400x300")
            contacts_window.configure(bg="#F0F0F0")
            
            for i, contact in enumerate(self.contacts, 1):
                contact_info = "\n".join([f"{key}: {value}" for key, value in contact.items()])
                contact_label = tk.Label(contacts_window, text=f"Contact {i}:\n{contact_info}", bg="#F0F0F0")
                contact_label.pack(padx=10, pady=5, anchor="w")
        else:
            messagebox.showinfo("Info", "No contacts available!")
            
    def search_contact(self):
        search_name = self.name_entry.get()
        found_contacts = [contact for contact in self.contacts if contact["Name"] == search_name]
        
        if found_contacts:
            contacts_window = tk.Toplevel(self.root)
            contacts_window.title("Contacts")
            contacts_window.geometry("400x300")
            contacts_window.configure(bg="#F0F0F0")
            
            for i, contact in enumerate(found_contacts, 1):
                contact_info = "\n".join([f"{key}: {value}" for key, value in contact.items()])
                contact_label = tk.Label(contacts_window, text=f"Contact {i}:\n{contact_info}", bg="#F0F0F0")
                contact_label.pack(padx=10, pady=5, anchor="w")
        else:
            messagebox.showinfo("Info", f"No contacts found with name '{search_name}'!")
            
    def update_contact(self):
        search_name = self.name_entry.get()
        found_contacts = [contact for contact in self.contacts if contact["Name"] == search_name]
        
        if found_contacts:
            update_window = tk.Toplevel(self.root)
            update_window.title("Update Contact")
            update_window.geometry("300x200")
            update_window.configure(bg="#F0F0F0")
            
            update_name_label = tk.Label(update_window, text="New Name:", bg="#F0F0F0")
            update_name_label.grid(row=0, column=0, padx=10, pady=5)
            update_name_entry = tk.Entry(update_window)
            update_name_entry.grid(row=0, column=1, padx=10, pady=5)
            
            update_phone_label = tk.Label(update_window, text="New Phone:", bg="#F0F0F0")
            update_phone_label.grid(row=1, column=0, padx=10, pady=5)
            update_phone_entry = tk.Entry(update_window)
            update_phone_entry.grid(row=1, column=1, padx=10, pady=5)
            
            update_email_label = tk.Label(update_window, text="New Email:", bg="#F0F0F0")
            update_email_label.grid(row=2, column=0, padx=10, pady=5)
            update_email_entry = tk.Entry(update_window)
            update_email_entry.grid(row=2, column=1, padx=10, pady=5)
            
            update_address_label = tk.Label(update_window, text="New Address:", bg="#F0F0F0")
            update_address_label.grid(row=3, column=0, padx=10, pady=5)
            update_address_entry = tk.Entry(update_window)
            update_address_entry.grid(row=3, column=1, padx=10, pady=5)
            
            def update():
                new_name = update_name_entry.get()
                new_phone = update_phone_entry.get()
                new_email = update_email_entry.get()
                new_address = update_address_entry.get()
                
                if new_name and new_phone:
                    for contact in self.contacts:
                        if contact["Name"] == search_name:
                            contact["Name"] = new_name
                            contact["Phone"] = new_phone
                            if new_email:
                                contact["Email"] = new_email
                            if new_address:
                                contact["Address"] = new_address
                            messagebox.showinfo("Success", "Contact updated successfully!")
                            update_window.destroy()
                            break
                else:
                    messagebox.showerror("Error", "New Name and New Phone number are required!")
            
            update_button = tk.Button(update_window, text="Update", command=update, bg="#008000", fg="#FFFFFF")
            update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="WE")
        else:
            messagebox.showinfo("Info", f"No contacts found with name '{search_name}'!")
            
    def delete_contact(self):
        search_name = self.name_entry.get()
        found_contacts = [contact for contact in self.contacts if contact["Name"] == search_name]
        
        if found_contacts:
            confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete contact '{search_name}'?")
            if confirmation:
                self.contacts = [contact for contact in self.contacts if contact["Name"] != search_name]
                messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Info", f"No contacts found with name '{search_name}'!")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactBook(root)
root.mainloop()
