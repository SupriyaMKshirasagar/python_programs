{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Varblbl' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_13180\\815138690.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     22\u001b[0m \u001b[0mlabl_3\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mLabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"Gender\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mwidth\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mfont\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"bold\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[0mlabl_3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m70\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m230\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 24\u001b[1;33m \u001b[0mvarblbl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mVarblbl\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     25\u001b[0m \u001b[0mRadiobutton\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"Male\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mpadx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvarblbliable\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mvarblbl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m235\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m230\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m \u001b[0mRadiobutton\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"Female\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mpadx\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvarblbliable\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mvarblbl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m290\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m230\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Varblbl' is not defined"
     ]
    }
   ],
   "source": [
    "from tkinter import*  \n",
    "base = Tk()  \n",
    "base.geometry('500x500')  \n",
    "base.title(\"Registration Form\")  \n",
    "  \n",
    "labl_0 = Label(base, text=\"Registration form\",width=20,font=(\"bold\", 20))  \n",
    "labl_0.place(x=90,y=53)  \n",
    "  \n",
    "  \n",
    "labl_1 = Label(base, text=\"FullName\",width=20,font=(\"bold\", 10))  \n",
    "labl_1.place(x=80,y=130)  \n",
    "  \n",
    "entry_1 = Entry(base)  \n",
    "entry_1.place(x=240,y=130)  \n",
    "  \n",
    "labl_2 = Label(base, text=\"Email\",width=20,font=(\"bold\", 10))  \n",
    "labl_2.place(x=68,y=180)  \n",
    "  \n",
    "entry_02 = Entry(base)  \n",
    "entry_02.place(x=240,y=180)  \n",
    "  \n",
    "labl_3 = Label(base, text=\"Gender\",width=20,font=(\"bold\", 10))  \n",
    "labl_3.place(x=70,y=230)  \n",
    "varblbl = Varblbl()  \n",
    "Radiobutton(base, text=\"Male\",padx = 5, varblbliable=varblbl, value=1).place(x=235,y=230)  \n",
    "Radiobutton(base, text=\"Female\",padx = 20, varblbliable=varblbl, value=2).place(x=290,y=230)  \n",
    "  \n",
    "labl_4 = Label(base, text=\"Age:\",width=20,font=(\"bold\", 10))  \n",
    "labl_4.place(x=70,y=280)  \n",
    "  \n",
    "  \n",
    "entry_02 = Entry(base)  \n",
    "entry_02.place(x=240,y=280)  \n",
    "  \n",
    "Button(base, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  \n",
    "# it will be used for displaying the registration form onto the window  \n",
    "base.mainloop()  \n",
    "print(\"Registration form is created seccussfully...\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_13180\\3540611395.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     46\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     47\u001b[0m \u001b[0mButton\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"Register\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwidth\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m200\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m400\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 48\u001b[1;33m \u001b[0mbase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmainloop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\Program Files\\anaconda\\lib\\tkinter\\__init__.py\u001b[0m in \u001b[0;36mmainloop\u001b[1;34m(self, n)\u001b[0m\n\u001b[0;32m   1427\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mmainloop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1428\u001b[0m         \u001b[1;34m\"\"\"Call the mainloop of Tk.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1429\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtk\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmainloop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1430\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1431\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mquit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "from tkinter import *  \n",
    "base = Tk()  \n",
    "base.geometry(\"500x500\")  \n",
    "base.title(\"registration form\")  \n",
    "  \n",
    "lb1= Label(base, text=\"Enter Name\", width=10, font=(\"arial\",12))  \n",
    "lb1.place(x=20, y=120)  \n",
    "en1= Entry(base)  \n",
    "en1.place(x=200, y=120)  \n",
    "  \n",
    "lb3= Label(base, text=\"Enter Email\", width=10, font=(\"arial\",12))  \n",
    "lb3.place(x=19, y=160)  \n",
    "en3= Entry(base)  \n",
    "en3.place(x=200, y=160)  \n",
    "  \n",
    "lb4= Label(base, text=\"Contact Number\", width=13,font=(\"arial\",12))  \n",
    "lb4.place(x=19, y=200)  \n",
    "en4= Entry(base)  \n",
    "en4.place(x=200, y=200)  \n",
    "  \n",
    "lb5= Label(base, text=\"Select Gender\", width=15, font=(\"arial\",12))  \n",
    "lb5.place(x=5, y=240)  \n",
    "vars = IntVar()  \n",
    "Radiobutton(base, text=\"Male\", padx=5,variable=vars, value=1).place(x=180, y=240)  \n",
    "Radiobutton(base, text=\"Female\", padx =10,variable=vars, value=2).place(x=240,y=240)  \n",
    "Radiobutton(base, text=\"others\", padx=15, variable=vars, value=3).place(x=310,y=240)  \n",
    "  \n",
    "list_of_cntry = (\"Country\", \"India\", \"Nepal\", \"Germany\")  \n",
    "cv = StringVar()  \n",
    "drplist= OptionMenu(base, cv, *list_of_cntry)  \n",
    "drplist.config(width=15)  \n",
    "cv.set(\"Country\")  \n",
    "lb2= Label(base, text=\"Select Country\", width=13,font=(\"arial\",12))  \n",
    "lb2.place(x=14,y=280)  \n",
    "drplist.place(x=200, y=275)  \n",
    "  \n",
    "lb6= Label(base, text=\"Enter Password\", width=13,font=(\"arial\",12))  \n",
    "lb6.place(x=19, y=320)  \n",
    "en6= Entry(base, show='*')  \n",
    "en6.place(x=200, y=320)  \n",
    "  \n",
    "lb7= Label(base, text=\"Re-Enter Password\", width=15,font=(\"arial\",12))  \n",
    "lb7.place(x=21, y=360)  \n",
    "en7 =Entry(base, show='*')  \n",
    "en7.place(x=200, y=360)  \n",
    "  \n",
    "Button(base, text=\"Register\", width=10).place(x=200,y=400)  \n",
    "base.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
