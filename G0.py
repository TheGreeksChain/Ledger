#Smart Contracts

import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

#Parties
label0 = Label(master, text = 'G A', relief = 'groove', width = 40)
label1 = Label(master, text = 'G B', relief = 'groove', width = 40)
Party_A = Entry(master, relief = 'groove', width = 40)
Party_B = Entry(master, relief = 'groove', width = 40)

#Consideration
label2 = Label(master, text = 'G A Consideration', relief = 'groove', width = 40)
label3 = Label(master, text = 'G B Consideration', relief = 'groove', width = 40)
Party_A_C = Entry(master, relief = 'groove', width = 40)
Party_B_C = Entry(master, relief = 'groove', width = 40)

#Signed
label4 = Label(master, text = 'Sign', relief = 'groove', width = 40)
label5 = Label(master, text = 'Transaction Number', relief = 'groove', width = 40)
Party_A_Sign = Entry(master, relief = 'groove', width = 40)
Party_B_Sign = Entry(master, relief = 'groove', width = 40)

#Date
label6 = Label(master, text = 'Date', relief = 'groove', width = 40)
Date = Entry(master, relief = 'groove', width = 40)


#write to file function
def write():
    
    #Define Variavles
    Party_Red = str(Party_A.get())
    Party_Blue = str(Party_B.get())
    Party_Red_C = str(Party_A_C.get())
    Party_Blue_C = str(Party_B_C.get())
    Party_Red_Sign = str(Party_A_Sign.get())
    Party_Blue_Sign = str(Party_B_Sign.get())
    Date_0 = str(Date.get())

    #Openfile
    with open('G_Ledger.csv', 'a') as csvfile:
    #define fieldnames
        fieldnames = ['Party A', 'Party A Consideration', 'Party A Signiture', 'Party B', 'Party B Consideration', 'Party B Signiture', 'Date']
    #define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Write
        writer.writerow({'Party A': Party_Red, 'Party A Consideration':Party_Red_C, 'Party A Signiture':Party_Red_Sign,
                         'Party B': Party_Blue, 'Party B Consideration':Party_Blue_C, 'Party B Signiture':Party_Blue_Sign,
                         'Date': Date_0})

#Button to run write
b1 = Button(master, text = 'Execute Smart Contract', relief = 'groove', width = 25, command=write)

#function two to clear the entry widgets
def clear():
    Party_A.delete(0, END)
    Party_B.delete(0, END)
    Party_A_C.delete(0, END)
    Party_B_C.delete(0, END)
    Party_A_Sign.delete(0, END)
    Party_B_Sign.delete(0, END)
    Date.delete(0,END)
                        
#button to run function clear
b2 = Button(master, text = 'New Contract', relief = 'groove', width = 25, command=clear)

#Geometry
label0.grid( row = 1, column = 1, padx = 10 )
Party_A.grid( row = 2, column = 1, padx = 10 )
label1.grid( row = 1, column = 2, padx = 10 )
Party_B.grid( row = 2, column = 2, padx = 10 )

label2.grid( row = 3, column = 1, padx = 10 )
Party_A_C.grid( row = 4, column = 1, padx = 10 )
label3.grid( row = 3, column = 2, padx = 10 )
Party_B_C.grid( row = 4, column = 2, padx = 10 )
label4.grid( row = 5, column = 1, padx = 10 )
label5.grid( row = 5, column = 2, padx = 10 )

Party_A_Sign.grid( row = 6, column = 1, padx = 10 )
Party_B_Sign.grid( row = 6, column = 2, padx = 10 )

label6.grid( row = 7, column = 1, padx = 10 )
Date.grid( row = 7, column = 2, padx = 10 )

b1.grid( row = 8, column = 1, columnspan = 2)
b2.grid( row = 9, column = 1, columnspan = 2)

#Static Properties
master.title('The Greeks')
