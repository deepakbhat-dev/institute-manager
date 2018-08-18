from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import *
import MySQLdb

#    Create Table
connection = MySQLdb.connect("localhost", "root", "", "institute")
createT = "CREATE TABLE IF NOT EXISTS student(ID int primary key, NAME char(20) , ADDRESS char(50), CONTACT varchar(10),\
 EMAIL char(30), DOB char(10), QUALIFICATION char(50), COLLEGE char(30), BRANCH char(20), PROFESSION char(20),\
  INFO char(5), SIGNATURE char(20))"
cursor = connection.cursor()
cursor.execute(createT)

#    Main Page
project = Tk()
project.title("ANSPRO TECHNOLOGIES")
content = open("E:/Deepu/Project/Python/Institute/Info.txt", "r")
info = content.read()
project.configure(bg='light gray')
msg = Message(project, text=info)
msg.config(aspect=300, bg='light gray', fg='gray11', padx=20, font=('times', 24, 'italic'))
project.geometry('1550x1000')
msg.pack()


def clickedC():
    project.destroy()


btnC = tk.Button(project, text="CANCEL", font=("Helvetica", 10, "bold"), borderwidth=2, relief='raised', activebackground='azure4', command=clickedC)
btnC.pack(side="right", padx=280)

#    Joining Page


def clickedJ():

    c1 = StringVar()
    c2 = StringVar()
    c3 = StringVar()
    c4 = StringVar()
    c5 = StringVar()
    c6 = StringVar()
    c7 = StringVar()
    c8 = StringVar()
    rad = StringVar()
    rinfo = StringVar()

    def clickedB():
        window.destroy()

    window = Toplevel(project)
    window.title("STUDENT REGISTARTION FORM")
    window.geometry('1550x1000')
    window.configure(background="light gray")

    lbl = tk.Label(window, text="STUDENT REGISTRATION FORM", bg='light gray', width=30, font=("Helvetica", 25, "bold"))
    lbl.place(x=400, y=20)
    lb1 = tk.Label(window, text="ID", bg='light gray', width=10, font=("bold", 15))
    lb1.place(x=50, y=100)
    txt1 = Entry(window, width=30)
    txt1.place(x=240, y=100)
    lb2 = tk.Label(window, text="NAME", bg='light gray',  width=10, font=("bold", 15))
    lb2.place(x=50, y=140)
    txt2 = Entry(window, width=30)
    txt2.place(x=240, y=140)
    lb3 = tk.Label(window, text="ADDRESS", bg='light gray',  width=10, font=("bold", 15))
    lb3.place(x=50, y=180)
    txt3 = Entry(window, width=50)
    txt3.place(x=240, y=180)
    lb4 = tk.Label(window, text="CONTACT", bg='light gray',  width=10, font=("bold", 15))
    lb4.place(x=50, y=220)
    txt4 = Entry(window, width=30)
    txt4.place(x=240, y=220)
    lb5 = tk.Label(window, text="EMAIL", bg='light gray',  width=10, font=("bold", 15))
    lb5.place(x=50, y=260)
    txt5 = Entry(window, width=30)
    txt5.place(x=240, y=260)
    lb6 = tk.Label(window, text="DOB", bg='light gray',  width=10, font=("bold", 15))
    lb6.place(x=50, y=300)
    txt6 = Entry(window, width=30)
    txt6.place(x=240, y=300)

    #     Check Boxes
    lb7 = tk.Label(window, text="EDUCATIONAL\nQUALIFICATION", bg='light gray',  width=14, font=("bold", 15))
    lb7.place(x=50, y=340)
    check1 = tk.Checkbutton(window, text="HSC/PUC", variable=c1, onvalue="HSC/PUC", offvalue='', bg='light gray')
    check1.place(x=250, y=340)
    check2 = tk.Checkbutton(window, text="UNDERGRADUATE", variable=c2, onvalue="Undergraduate", offvalue='', bg='light gray')
    check2.place(x=350, y=340)
    check3 = tk.Checkbutton(window, text="DIPLOMA", variable=c3, onvalue="Diploma", offvalue='', bg='light gray')
    check3.place(x=490, y=340)
    check4 = tk.Checkbutton(window, text="BCA", variable=c4, onvalue="BCA", offvalue='', bg='light gray')
    check4.place(x=590, y=340)
    check5 = tk.Checkbutton(window, text="MCA", variable=c5, onvalue="MCA", offvalue='', bg='light gray')
    check5.place(x=670, y=340)
    check6 = tk.Checkbutton(window, text="B.E/B.TECH", variable=c6, onvalue="B.E / B.Tech", offvalue='', bg='light gray')
    check6.place(x=750, y=340)
    check7 = tk.Checkbutton(window, text="M.E/M.TECH", variable=c7, onvalue="M.E / M.Tech", offvalue='', bg='light gray')
    check7.place(x=870, y=340)
    check8 = tk.Checkbutton(window, text="BSC", variable=c8, onvalue="BSC", offvalue='', bg='light gray')
    check8.place(x=1010, y=340)
    lb7 = tk.Label(window, text="Others Specify", bg='light gray')
    lb7.place(x=1090, y=340)
    txt7 = Entry(window, width=20)
    txt7.place(x=1175, y=340)

    lb8 = tk.Label(window, text="SCHOOL/COLL/\nINSTITUTE", bg='light gray',  width=14, font=("bold", 15))
    lb8.place(x=50, y=400)
    txt8 = Entry(window, width=40)
    txt8.place(x=240, y=400)
    lb9 = tk.Label(window, text="BRANCH", bg='light gray',  width=10, font=("bold", 15))
    lb9.place(x=50, y=460)
    txt9 = Entry(window, width=30)
    txt9.place(x=240, y=460)

    #    Radio Buttons
    lb10 = tk.Label(window, text="PROFESSIONAL\nDETAILS", bg='light gray',  width=14, font=("bold", 15))
    lb10.place(x=50, y=510)
    radio1 = tk.Radiobutton(window, text="STUDENT",  bg='light gray', variable=rad, value="Student")
    radio1.place(x=250, y=510)
    radio2 = tk.Radiobutton(window, text="EMPLOYED", bg='light gray',  variable=rad, value="Employed")
    radio2.place(x=350, y=510)
    radio3 = tk.Radiobutton(window, text="UN-EMPLOYED", bg='light gray',  variable=rad, value="Un-Employed")
    radio3.place(x=450, y=510)
    radio4 = tk.Radiobutton(window, text="SELF-EMPLOYED", bg='light gray',  variable=rad, value="Self-Employed")
    radio4.place(x=580, y=510)
    radio5 = tk.Radiobutton(window, text="Any Other Business", bg='light gray',  variable=rad, value="Any")
    radio5.place(x=730, y=510)
    txt10 = Entry(window, width=20)
    txt10.place(x=860, y=510)

    lb11 = tk.Label(window, text="ARE YOU INTRESTED IN RECEIVING INFORMATION ABOUT IN HOUSE SEMINARS/ WORKSHOPS?",\
            width=82, bg='light gray',  font=("bold", 14))
    lb11.place(x=50, y=570)
    radio5 = tk.Radiobutton(window, text="YES", bg='light gray',  variable=rinfo, value="Yes")
    radio5.place(x=980, y=570)
    radio6 = tk.Radiobutton(window, text="NO", bg='light gray',  variable=rinfo, value="No")
    radio6.place(x=1040, y=570)

    lb12 = tk.Label(window, text="SIGNATURE\nOF THE\nCANDIDATE", bg='light gray',  width=12, font=("bold", 15))
    lb12.place(x=50, y=610)
    txt11 = Entry(window, width=30)
    txt11.place(x=240, y=635)

    #   Insert into Database

    def clicked():
        chec = []

        A = txt1.get()
        if A == '':
            messagebox.showerror("Error", "ID cannot be Empty")
        elif A.isdigit() == False:
            messagebox.showerror("Error", "ID must be a Number")
        A = int(A)

        B = txt2.get()
        B = str(B)

        C = txt3.get()
        C = str(C)

        D = txt4.get()
        D = str(D)

        E = txt5.get()
        E = str(E)

        F = txt6.get()
        F = str(F)

        c9 = txt7.get()
        c9 = str(c9)

        #   Add the Checkboxes for Database
        c = [c1.get(), c2.get(), c3.get(), c4.get(), c5.get(), c6.get(), c7.get(), c8.get(), c9]
        for item in c:
            if item != '':
                chec.append(item)

        G = " ".join(chec)

        H = txt8.get()
        H = str(H)

        I = txt9.get()
        I = str(I)

        #  Add Radio into Database
        if rad.get() == "Any":
            J = str(txt10.get())
        else:
            J = rad.get()

        K = rinfo.get()

        L = txt11.get()
        L = str(L)

        if B == '':
            messagebox.showerror("Error", "Name cannot be empty")
        elif L == '':
            messagebox.showerror("Error", "Signature is a must")
        elif D == '' and E == '':
            messagebox.showerror("Error", "Need atleast 1 contact info")
        else:
            insert = "INSERT INTO student(ID, NAME, ADDRESS, CONTACT, EMAIL, DOB, QUALIFICATION, COLLEGE, BRANCH, PROFESSION,\
             INFO, SIGNATURE) VALUES('%d','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s')"\
                 % (A, B, C, D, E, F, G, H, I, J, K, L)
            cursor.execute(insert)
            connection.commit()
            messagebox.showinfo("Notification", "Saved Successfully")





    btnS = tk.Button(window, text="SAVE", font=("Helvetica", 10, "bold"), borderwidth=2, relief='raised', activebackground='azure4', command=clicked)
    btnS.place(x=530, y=750)

    btnB = tk.Button(window, text="BACK", font=("Helvetica", 10, "bold"), borderwidth=2, relief='raised', activebackground='azure4', command=clickedB)
    btnB.place(x=770, y=750)

btnJ = tk.Button(project, text="JOIN NOW", font=("Helvetica", 10, "bold"), borderwidth=2, relief='raised', activebackground='azure4', command=clickedJ)
btnJ.pack(side="left", padx=250)


project.mainloop()
connection.close()
