from tkinter import *
from tkinter import messagebox
import csv


root = Tk()
root.title("Data Management Application")

date_label = Label(root, text="Date:")
date_label.grid(row=0, column=0)
date_entry = Entry(root)
date_entry.grid(row=0, column=1)

id_label = Label(root, text="ID:")
id_label.grid(row=1, column=0)
id_entry = Entry(root)
id_entry.grid(row=1, column=1)

customer_label = Label(root, text="Customer Name:")
customer_label.grid(row=2, column=0)
customer_entry = Entry(root)
customer_entry.grid(row=2, column=1)

product_label = Label(root, text="Product Name:")
product_label.grid(row=3, column=0)
product_entry = Entry(root)
product_entry.grid(row=3, column=1)

price_label = Label(root, text="Product Price/Service Fees:")
price_label.grid(row=4, column=0)
price_entry = Entry(root)
price_entry.grid(row=4, column=1)

phone_label = Label(root, text="Phone Number:")
phone_label.grid(row=5, column=0)
phone_entry = Entry(root)
phone_entry.grid(row=5, column=1)




def reset_fields():
    # Clear the entry fields
    date_entry.delete(0, END)
    id_entry.delete(0, END)
    customer_entry.delete(0, END)
    product_entry.delete(0, END)
    price_entry.delete(0, END)
    phone_entry.delete(0, END)



def save_data():
    date = date_entry.get()
    ID = id_entry.get()
    customer_name = customer_entry.get()
    product_name = product_entry.get()
    price = price_entry.get()
    phone_number = phone_entry.get()

    # Save data to a CSV file or a database of your choice
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, ID, customer_name, product_name, price, phone_number])

    messagebox.showinfo("Success", "Data saved successfully!")
    
    
    
save_button=Button(root,text="Save",command=save_data).grid(row=6,columnspan=1)
reset_button=Button(root,text="Reset",command=reset_fields).grid(row=6,columnspan=2)   







root.mainloop()

