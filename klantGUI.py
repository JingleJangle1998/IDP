from tkinter import *
from tkinter import messagebox
import sqlite3
import smtplib

#------------------------------------SPORTACTIVITEITEN---------------------------#
def sportactiviteiten():
    sportactiviteitenwindow = Toplevel(root)
    sportactiviteitenwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 500, 200
    sportactiviteitenwindow.geometry('%ix%i' % (screenX, screenY))
    KlantID = Label(sportactiviteitenwindow, text="KlantID", background=backgroundColor)
    KlantID.grid(row=0, column=2)
    KlantIDentry = Entry(sportactiviteitenwindow, bd=3)
    KlantIDentry.grid(row=0, column=3)
    klantinformatie = Label(sportactiviteitenwindow, text='', background=backgroundColor)
    klantinformatie.grid(row=2, column=1)
    opvragenloopband = Button(sportactiviteitenwindow, text="Hardlopen", background=backgroundColor,
                         command=lambda: klantinformatie.configure(text=(hardlopen())))
    opvragenloopband.grid(row=1, column=0)
    opvragenfietsen = Button(sportactiviteitenwindow, text="Fietsen", background=backgroundColor,
                              command=lambda: klantinformatie.configure(text=(fietsen())))
    opvragenfietsen.grid(row=1, column=1)
    opvragenroeien = Button(sportactiviteitenwindow, text="Roeien", background=backgroundColor,
                              command=lambda: klantinformatie.configure(text=(roeien())))
    opvragenroeien.grid(row=1, column=2)
    opvragenbenchpress = Button(sportactiviteitenwindow, text="Benchpress", background=backgroundColor,
                              command=lambda: klantinformatie.configure(text=(benchpress())))
    opvragenbenchpress.grid(row=1, column=3)
    opvragenpulldown = Button(sportactiviteitenwindow, text="Pulldown", background=backgroundColor,
                              command=lambda: klantinformatie.configure(text=(pulldown())))
    opvragenpulldown.grid(row=1, column=4)
    list = ""

    def hardlopen():
        conn = sqlite3.connect("company.db")
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(
            data[13]) + '-' + str(data[14]) + '\n'
        conn.close()
        return list

    def fietsen():
        conn = sqlite3.connect("company.db")
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(
            data[13]) + '-' + str(data[14]) + '\n'
        conn.close()
        return list

    def roeien():
        conn = sqlite3.connect("company.db")
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(
            data[13]) + '-' + str(data[14]) + '\n'
        conn.close()
        return list

    def benchpress():
        conn = sqlite3.connect("company.db")
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(
            data[13]) + '-' + str(data[14]) + '\n'
        conn.close()
        return list

    def pulldown():
        conn = sqlite3.connect("company.db")
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(
            data[13]) + '-' + str(data[14]) + '\n'
        conn.close()
        return list



#------------------------------------OPVRAGENKLANT-------------------------------#

def opvragenklant():
    Opvragenklantwindow = Toplevel(root)
    Opvragenklantwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 500, 200
    Opvragenklantwindow.geometry('%ix%i' % (screenX, screenY))
    KlantID = Label(Opvragenklantwindow, text="KlantID", background=backgroundColor)
    KlantID.grid(row=0, column=2)
    KlantIDentry = Entry(Opvragenklantwindow, bd=3)
    KlantIDentry.grid(row=0, column=3)
    klantinformatie = Label(Opvragenklantwindow, text='', background=backgroundColor)
    klantinformatie.grid(row=2, column=1)
    bekijkklant = Button(Opvragenklantwindow, text="Inloggen", background=backgroundColor,
                         command=lambda: klantinformatie.configure(text=(klantgegevens())))
    bekijkklant.grid(row=0, column=4)
    donebutton = Button(Opvragenklantwindow, text='Done', background=backgroundColor, command=lambda: sluitopvragenklant())
    donebutton.grid(row=0, column=0)
    list = ""

    def klantgegevens():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(data[13]) + '-' +str(data[14]) + '\n'
        conn.close()
        return list  # het returne van de print statement

    def sluitopvragenklant():
        Opvragenklantwindow.destroy()

#--------------------------------------OPVRAGENKLANT---------------------------------#
#--------------------------------------ADVIESVRAGEN----------------------------------#
def advies():
    adviesvragenwindow = Toplevel(root)
    adviesvragenwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 500, 200
    adviesvragenwindow.geometry('%ix%i' % (screenX, screenY))
    email = Label(adviesvragenwindow, text="Email", background=backgroundColor)
    email.grid(row=0, column=0)
    emailentry = Entry(adviesvragenwindow, bd=3)
    emailentry.grid(row=0, column=1)
    wachtwoord = Label(adviesvragenwindow, text="Wachtwoord", background=backgroundColor)
    wachtwoord.grid(row=1, column=0)
    wachtwoordentry = Entry(adviesvragenwindow,show="*", bd=3)
    wachtwoordentry.grid(row=1, column=1)
    tekst = Label(adviesvragenwindow, text="Bericht", background=backgroundColor)
    tekst.grid(row=2, column=0)
    tekstentry = Entry(adviesvragenwindow, bd=3)
    tekstentry.grid(row=2, column=1)
    def emailsturen():
        TEKST = tekstentry.get()
        fromaddr = emailentry.get()
        toaddrs = 'djimschaap@gmail.com'
        msg = "\r\n".join([
            "From: %s" % fromaddr,
            "To: djimschaap@gmail.com",
            "Subject: Advies aanvraag",
            "",
            TEKST
        ])
        username = fromaddr
        password = wachtwoordentry.get()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        adviesvragenwindow.destroy()

    donebutton = Button(adviesvragenwindow, text='Done', background=backgroundColor, command=lambda: emailsturen())
    donebutton.grid(row=3, column=2)









backgroundColor = 'LightBlue2'

root = Tk()
welkomLabel = Label(background=backgroundColor, foreground= 'navy', text='Welkom bij Benno Sport', font=('', 40, ''))
welkomLabel.pack(side=TOP)
OpvragenklantwindowButton = Button(root, text="Gegevens inzien", command=opvragenklant, width =80, height =10, background='cyan2', font=('', 10, ''))
OpvragenklantwindowButton.pack(pady =10)
OpvragenactiviteitwindowButton = Button(root, text="Sportactiviteiten", command=sportactiviteiten, width =80, height =10, background='cyan2', font=('', 10, ''))
OpvragenactiviteitwindowButton.pack(pady =10)
OpvragenactiviteitwindowButton = Button(root, text="Advies aanvragen", command=advies, width =80, height =10, background='cyan2', font=('', 10, ''))
OpvragenactiviteitwindowButton.pack(pady =10)
root.configure(background=backgroundColor)
root.mainloop()