from tkinter import *
import tkinter as tk
#import openpyxl,xlrd
#from openpyxl import workbook
import pathlib


main=Tk()
main.title("Data Entry Form")
main.geometry("500X500")
main.config(highlightbackground="black")



file=pathlib.path("Shop_Data.xlsx")
if file.exists():
    pass
else:
    file=workbook()
    sheet=file.active
    sheet["A1"]="Date"
    sheet["B1"]="ID"
    sheet["C1"]="Customer Name"
    sheet["D1"]="Product Name"
    sheet["E1"]="Product price"
    sheet["F1"]="Phone number"
    
    
    file.save("Shop_Data.xlsx")
    
    
    
    
    #Submit function for Button
    
    
    
    
    
    
    
    
    
    #Design part
    Tk.Label(main,text='Date',bg="#f0c33c",padx=10,pady=10).grid(row=1)
    Tk.Label(main,text='ID',bg="#f0c33c",padx=10,pady=10).grid(row=1)
    Tk.Label(main,text='Customer Name',bg="#f0c33c",padx=10,pady=10).grid(row=1)
    Tk.Label(main,text='Product Name',bg="#f0c33c",padx=10,pady=10).grid(row=1)
    Tk.Label(main,text='Product Price',bg="#f0c33c",padx=10,pady=10).grid(row=1)
    Tk.Label(main,text='Phone Number',bg="#f0c33c",padx=10,pady=10).grid(row=1)

