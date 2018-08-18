from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import MySQLdb

connection = MySQLdb.connect("localhost", "root", "", "institute")
cursor = connection.cursor()

view = Tk()
view.title("DISPLAY")
view.geometry("1550x1000")
count = 0

lb1 = Label(view, text=" ID ", width=5, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb1.grid(column=0,row=0)

lb2 = Label(view, text=" NAME ", width=13, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb2.grid(column=1,row=0)

lb3 = Label(view, text=" ADDRESS ", width=17, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb3.grid(column=2,row=0)

lb4 = Label(view, text=" CONTACT ", width=10, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb4.grid(column=3,row=0)

lb5 = Label(view, text=" EMAIL ", width=14, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb5.grid(column=4,row=0)

lb6 = Label(view, text=" DOB ", width=9, justify='center',borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb6.grid(column=5,row=0)

lb7 = Label(view, text=" QUALIFICATION ", width=15, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb7.grid(column=6,row=0)

lb8 = Label(view, text=" COLLEGE ", width=12, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb8.grid(column=7,row=0)

lb9 = Label(view, text=" BRANCH ", width=10, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb9.grid(column=8,row=0)

lb10 = Label(view, text=" PROFESSION ", width=15, borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb10.grid(column=9,row=0)

lb11 = Label(view, text=" INFO ", width=5, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb11.grid(column=10,row=0)

lb12 = Label(view, text=" SIGNATURE ", width=15, justify='center', borderwidth=2, relief="raised", font=("Helvetica", 15, "bold"))
lb12.grid(column=11,row=0)

search="SELECT * FROM student"
cursor.execute(search)
rows=cursor.fetchall()

for row in rows:
    count += 1
    lb21 = Label(view, text=row[0], width=5, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb21.grid(column=0,row=count)

    lb22 = Label(view, text=row[1], width=13, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb22.grid(column=1,row=count)

    lb23 = Label(view, text=row[2], width=17, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb23.grid(column=2,row=count)

    lb24 = Label(view, text=row[3], width=10, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb24.grid(column=3,row=count)

    lb25 = Label(view, text=row[4], width=14, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb25.grid(column=4,row=count)

    lb26 = Label(view, text=row[5], width=9, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb26.grid(column=5,row=count)

    lb27 = Label(view, text=row[6], width=15, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb27.grid(column=6,row=count)

    lb28 = Label(view, text=row[7], width=12, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb28.grid(column=7,row=count)

    lb29 = Label(view, text=row[8], width=10, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb29.grid(column=8,row=count)

    lb30 = Label(view, text=row[9], width=15, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb30.grid(column=9,row=count)

    lb31 = Label(view, text=row[10], width=5, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb31.grid(column=10,row=count)

    lb32 = Label(view, text=row[11], width=15, justify='center', borderwidth=2, relief="solid", font=("bold", 15), background="light gray")
    lb32.grid(column=11,row=count)



view.mainloop()
