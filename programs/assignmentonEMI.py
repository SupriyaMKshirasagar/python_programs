from tkinter import*
import tkinter as Tk

main_window=Tk.Tk(className="EMI CALCULATOR")


def calculate():
    input_principal=int(principal.get())
    input_rate=float(rate.get())/1200
    input_month=float(month.get())
    input_downpayment=int(DownPayment.get())
    new_principal=input_principal-input_downpayment
    emi_val=new_principal*input_rate*(pow((1+input_rate),input_month)/(pow((1+input_rate),input_month)-1))
    emi.set('{:.2f}'.format(emi_val))
    
    total_payment_val=emi_val*input_month
    total_interest_val=total_payment_val-new_principal
    total_interest.set('{:.2f}'.format(total_interest_val))
    total_payment.set('{:.2f}'.format(total_payment_val))
    
    pass
 



main_window=Tk.Tk()
main_window.title=("EMI calculator using python")
main_window.geometry("")
main_window.configure(bg="#f0c33c")

Tk.Label(main_window,text='EMI CALCULATOR',font=('impact',20),bg="#f0c33c",padx=10,pady=10).grid(row=0)
#Creating label
Tk.Label(main_window,text='Amount',bg="#f0c33c",padx=10,pady=10).grid(row=1)
Tk.Label(main_window,text='Interest',bg="#f0c33c",padx=10,pady=10).grid(row=2)
Tk.Label(main_window,text='Duration',bg="#f0c33c",padx=10,pady=10).grid(row=3)
Tk.Label(main_window,text='DownPayment',bg="#f0c33c",padx=10,pady=10).grid(row=4)
#Creating Buttons
Tk.Button(main_window,text="Calculate",command=calculate,bg="#f0c33c",padx=10,pady=10).grid(row=5,columnspan=1)




principal=Tk.IntVar(main_window)
rate=Tk.IntVar(main_window)
month=Tk.IntVar(main_window)
emi=Tk.IntVar(main_window)
total_interest=Tk.IntVar(main_window)
total_payment=Tk.IntVar(main_window)
DownPayment=Tk.IntVar(main_window)


principal.set(0)
rate.set(0)
month.set(0)
DownPayment.set(0)
emi.set(0)
total_interest.set(0)
total_payment.set(0)

Tk.Entry(main_window,textvariable=principal).grid(row=1,column=1)
Tk.Entry(main_window,textvariable=rate).grid(row=2,column=1)
Tk.Entry(main_window,textvariable=month).grid(row=3,column=1)
Tk.Entry(main_window,textvariable=DownPayment).grid(row=4,column=1)




Tk.Label(main_window,text='EMI',bg="#f0c33c",padx=10,pady=10).grid(row=5,columnspan=2)
Tk.Label(main_window,textvariable=emi,font=('Arial',16),bg="#f0c33c",padx=10,pady=10).grid(row=6,columnspan=2)
Tk.Label(main_window,text='Total Interest',bg="#f0c33c",padx=10,pady=10).grid(row=7,columnspan=2)
Tk.Label(main_window,textvariable=total_interest,font=('Arial',16),bg="#f0c33c",padx=10,pady=10).grid(row=8,columnspan=2)
Tk.Label(main_window,text='Total Amount',bg="#f0c33c",padx=10,pady=10).grid(row=9,columnspan=2)
Tk.Label(main_window,textvariable=total_payment,font=('Arial',16),bg="#f0c33c",padx=10,pady=10).grid(row=10,columnspan=2)

    





main_window.mainloop()