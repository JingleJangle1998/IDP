from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors
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
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM activiteit WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        conn.close()
        return data

    def fietsen():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM activiteit WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        conn.close()
        return data

    def roeien():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM activiteit WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        conn.close()
        return data

    def benchpress():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM activiteit WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        conn.close()
        return data

    def pulldown():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM activiteit WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        conn.close()
        return data



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
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=%s", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        return data  # het returne van de print statement

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



# ------------------------------WIJZIGENKLANT-----------------------------#
def Wijzigenklant():
    Wijzigenklantwindow = Toplevel(root)
    Wijzigenklantwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 700, 400
    Wijzigenklantwindow.geometry('%ix%i' % (screenX, screenY))
    # ----------------KlantID----------------------------#
    KlantID = Label(Wijzigenklantwindow, text="KlantID", background=backgroundColor)
    KlantID.grid(row=0, column=0)
    KlantIDentry = Entry(Wijzigenklantwindow, bd=3)
    KlantIDentry.grid(row=0, column=1)
    # ---------------VOORNAAM---------------------------#
    Voornaam = Label(Wijzigenklantwindow, text="Voornaam", background=backgroundColor)
    Voornaam.grid(row=1, column=0, sticky=W)
    Voornaamentry = Entry(Wijzigenklantwindow, bd=3)
    Voornaamentry.grid(row=1, column=1)

    def wijzigenvoornaam():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        c = conn.cursor()
        voornaam = Voornaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET voornaam=%s  WHERE klantID=%s", (voornaam, klantID))
        conn.commit()
        conn.close()

    Updatevoornaam = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenvoornaam(), background=backgroundColor)
    Updatevoornaam.grid(row=1, column=2)
    # ----------------ACHTERNAAM-------------------------#
    Achternaam = Label(Wijzigenklantwindow, text="Achternaam", background=backgroundColor)
    Achternaam.grid(row=2, column=0, sticky=W)
    Achternaamentry = Entry(Wijzigenklantwindow, bd=3)
    Achternaamentry.grid(row=2, column=1)

    def wijzigenachternaam():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        achternaam = Achternaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET achternaam=%s  WHERE klantID=%s", (achternaam, klantID))
        conn.commit()
        conn.close()

    Updateachternaam = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenachternaam(), background=backgroundColor)
    Updateachternaam.grid(row=2, column=2)
    # ------------------Tussenvoegsel--------------------#
    Tussenvoegsel = Label(Wijzigenklantwindow, text="Tussenvoegsel", background=backgroundColor)
    Tussenvoegsel.grid(row=2, column=3)
    Tussenvoegselentry = Entry(Wijzigenklantwindow, bd=3)
    Tussenvoegselentry.grid(row=2, column=4)

    def wijzigentussenvoegsel():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        tussenvoegsel = Tussenvoegselentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET tussenvoegsel=%s  WHERE klantID=%s", (tussenvoegsel, klantID))
        conn.commit()
        conn.close()

    Updatetussenvoegsel = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigentussenvoegsel(), background=backgroundColor)
    Updatetussenvoegsel.grid(row=2, column=5)
    # ---------------Adresss----------------------------#
    Woonplaats = Label(Wijzigenklantwindow, text="Woonplaats", background=backgroundColor)
    Woonplaats.grid(row=6, column=0)
    Woonplaatsentry = Entry(Wijzigenklantwindow, bd=3)
    Woonplaatsentry.grid(row=6, column=1)

    def wijzigenwoonplaats():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        woonplaats = Woonplaatsentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET woonplaats=%s  WHERE klantID=%s", (woonplaats, klantID))
        conn.commit()
        conn.close()

    Updatewoonplaats = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenwoonplaats(), background=backgroundColor)
    Updatewoonplaats.grid(row=6, column=2)
    # ----------------------POSTCODE---------------------#
    Postcode = Label(Wijzigenklantwindow, text="Postcode", background=backgroundColor)
    Postcode.grid(row=6, column=3)
    Postcodeentry = Entry(Wijzigenklantwindow, bd=3)
    Postcodeentry.grid(row=6, column=4)

    def wijzigenpostcode():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        postcode = Postcodeentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET postcode=%s  WHERE klantID=%s", (postcode, klantID))
        conn.commit()
        conn.close()

    Updatepostode = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenpostcode(), background=backgroundColor)
    Updatepostode.grid(row=6, column=5)
    # -----------------------STRAATNAAM------------------#
    Straatnaam = Label(Wijzigenklantwindow, text="Straatnaam", background=backgroundColor)
    Straatnaam.grid(row=7, column=0)
    Straatnaamentry = Entry(Wijzigenklantwindow, bd=3)
    Straatnaamentry.grid(row=7, column=1)

    def wijzigenstraatnaam():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        straatnaam = Straatnaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET straatnaam=%s  WHERE klantID=%s", (straatnaam, klantID))
        conn.commit()
        conn.close()

    Updatestraatnaam = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenstraatnaam(), background=backgroundColor)
    Updatestraatnaam.grid(row=7, column=2)
    # ------------------------HUISNUMMER-----------------#
    Huisnummer = Label(Wijzigenklantwindow, text="Huisnummer", background=backgroundColor)
    Huisnummer.grid(row=8, column=0)
    Huisnummerentry = Entry(Wijzigenklantwindow, bd=3)
    Huisnummerentry.grid(row=8, column=1)

    def wijzigenhuisnummer():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        huisnummer = Huisnummerentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET huisnummer=%s  WHERE klantID=%s", (huisnummer, klantID))
        conn.commit()
        conn.close()

    Updatehuisnummer = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenhuisnummer(), background=backgroundColor)
    Updatehuisnummer.grid(row=8, column=2)
    # ------------HUISNUMMERTOEVOEGING------------------#
    Huisnummertoevoeging = Label(Wijzigenklantwindow, text="Toevoeging", background=backgroundColor)
    Huisnummertoevoeging.grid(row=8, column=3)
    Huisnummertoevoegingentry = Entry(Wijzigenklantwindow, bd=3)
    Huisnummertoevoegingentry.grid(row=8, column=4)

    def wijzigenhuisnummertoevoeging():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        toevoeging = Huisnummertoevoegingentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET toevoeging=%s  WHERE klantID=%s", (toevoeging, klantID))
        conn.commit()
        conn.close()

    Updatetoevoeging = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenhuisnummertoevoeging(), background=backgroundColor)
    Updatetoevoeging.grid(row=8, column=5)

    # ---------------EMAIL--------------------#
    Email = Label(Wijzigenklantwindow, text="E-mail", background=backgroundColor)
    Email.grid(row=10, column=0)
    Emailentry = Entry(Wijzigenklantwindow, bd=3)
    Emailentry.grid(row=10, column=1)

    def wijzigenemail():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        email = Emailentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET email=%s  WHERE klantID=%s", (email, klantID))
        conn.commit()
        conn.close()

    Updateemail = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenemail(), background=backgroundColor)
    Updateemail.grid(row=10, column=2)
    # ------------------TELEFOONNUMMER---------#
    Telefoonnummer = Label(Wijzigenklantwindow, text='Telefoonnummer', background=backgroundColor)
    Telefoonnummer.grid(row=11, column=0)
    Telefoonnummerentry = Entry(Wijzigenklantwindow, bd=3)
    Telefoonnummerentry.grid(row=11, column=1)

    def wijzigentelefoonnummer():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        telefoonnummer = Telefoonnummerentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET telefoonnummer=%s  WHERE klantID=%s", (telefoonnummer, klantID))
        conn.commit()
        conn.close()

    Updatetelefoonnummer = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigentelefoonnummer(), background=backgroundColor)
    Updatetelefoonnummer.grid(row=11, column=2)



# ------------------------------WIJZIGENKLANT------------------------------#


#-----------------------------------------AANWEZIGHEIDKLANTEN--------------------------------------
def aanwezigheidklanten():
    Aanwzigheidklantenwindow = Toplevel(root)
    Aanwzigheidklantenwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 700, 400
    Aanwzigheidklantenwindow.geometry('%ix%i' % (screenX, screenY))
    klantinformatie = Label(Aanwzigheidklantenwindow, text='', background=backgroundColor)
    klantinformatie.grid(row=2, column=1)
    bekijkklant = Button(Aanwzigheidklantenwindow, text="Aantal mensen aanwezig",
                         command=lambda: klantinformatie.configure(text=(aanwezigheid())), background=backgroundColor)
    bekijkklant.grid(row=0, column=0)
    def aanwezigheid():
        conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        c = conn.cursor()
        c.execute("SELECT uitlogtijd FROM aanwezigheid")  # gevens ophalen uit de DB
        data = c.fetchall()  # opgehaalde gevens in een lijst zetten
        aanwezigheidslijst = []
        for iets in data:
            if iets == None:
                aanwezigheidslijst.append(iets)
        aanwezigeidmensen = len(aanwezigheidslijst)

        conn.close()
        return aanwezigeidmensen  # het returne van de print statement


#-----------------------------------------AANWEZIGHEIDKLANTEN--------------------------------------#




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
WijzigenklantwindowButton = Button(root, text="Wijzigen NAW gegevens", command=Wijzigenklant, width =80, height =10, background='cyan2', font=('', 10, ''))
WijzigenklantwindowButton.pack(pady =10)
Aanwezigheidklantenwindowbutton = Button(root, text='Hoeveel klanten zijn er aanwezig', command=aanwezigheidklanten, width =80, height =5, background='cyan2', font=('', 10, ''))
Aanwezigheidklantenwindowbutton.pack(pady =10)
root.configure(background=backgroundColor)
root.mainloop()