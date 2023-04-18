import tkinter as ss    #importing tkinter

main = ss.Tk(className="emi calculator")  #changing dailog box name



main.geometry("400x400") #setting height and width of the window


def call():
    input_val=txt1.get()
    print(input_val)
    input_val2=txt2.get()
    print(input_val2)


label1=ss.Label(main,text="Name")         #creating label
txt1=ss.Entry(main)                       #creating text box
label2=ss.Label(main,text="Password")     #creating button
txt2=ss.Entry(main)
btn1=ss.Button(main,text="Submit",command=call)

label1.grid(row=0,column=0)
txt1.grid(row=0,column=1)
label2.grid(row=1,column=0)
txt2.grid(row=1,column=1)
btn1.grid(row=2,column=1)



    






main.mainloop()