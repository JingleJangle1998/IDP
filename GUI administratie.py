from tkinter import *
from tkinter import messagebox
import sqlite3


# -------------------------------NIEUWEKLANT-------------------------------------#
def NieuweKlant():
    Nieuweklantwindow = Toplevel(root)
    Nieuweklantwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY= 700, 470
    Nieuweklantwindow.geometry('%ix%i' % (screenX, screenY))
    # ---------------GESLACHT---------------------------#
    Geslacht = StringVar(value="1")
    Dhr = Radiobutton(Nieuweklantwindow, text="Dhr.", variable=Geslacht, value="Dhr.", background=backgroundColor)
    Dhr.grid(row=0, column=0)
    Mevr = Radiobutton(Nieuweklantwindow, text="Mevr", variable=Geslacht, value="Mevr", background=backgroundColor)
    Mevr.grid(row=0, column=1)
    # ---------------VOORNAAM---------------------------#
    Voornaam = Label(Nieuweklantwindow, text="Voornaam", background=backgroundColor)
    Voornaam.grid(row=1, column=0, sticky=W)
    Voornaamentry = Entry(Nieuweklantwindow, bd=3)
    Voornaamentry.grid(row=1, column=1)
    # ----------------ACHTERNAAM-------------------------#
    Achternaam = Label(Nieuweklantwindow, text="Achternaam", background=backgroundColor)
    Achternaam.grid(row=2, column=0, sticky=W)
    Achternaamentry = Entry(Nieuweklantwindow, bd=3)
    Achternaamentry.grid(row=2, column=1)
    Tussenvoegsel = Label(Nieuweklantwindow, text="Tussenvoegsel", background=backgroundColor)
    Tussenvoegsel.grid(row=2, column=2)
    Tussenvoegselentry = Entry(Nieuweklantwindow, bd=3)
    Tussenvoegselentry.grid(row=2, column=3)
    # ---------------GEBOORTEDATUM----------------------#
    GeboorteDag = Label(Nieuweklantwindow, text="dd", background=backgroundColor)
    GeboorteDag.grid(row=3, column=0)
    GeboorteDagentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteDagentry.grid(row=3, column=1)
    Geboortemaand = Label(Nieuweklantwindow, text="mm", background=backgroundColor)
    Geboortemaand.grid(row=4, column=0)
    GeboorteMaandentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteMaandentry.grid(row=4, column=1)
    Geboortejaar = Label(Nieuweklantwindow, text="jjjj", background=backgroundColor)
    Geboortejaar.grid(row=5, column=0)
    GeboorteJaarentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteJaarentry.grid(row=5, column=1)
    # ---------------Adresss----------------------------#
    Woonplaats = Label(Nieuweklantwindow, text="Woonplaats", background=backgroundColor)
    Woonplaats.grid(row=6, column=0)
    Woonplaatsentry = Entry(Nieuweklantwindow, bd=3)
    Woonplaatsentry.grid(row=6, column=1)
    Postcode = Label(Nieuweklantwindow, text="Postcode", background=backgroundColor)
    Postcode.grid(row=6, column=2)
    Postcodeentry = Entry(Nieuweklantwindow, bd=3)
    Postcodeentry.grid(row=6, column=3)
    Straatnaam = Label(Nieuweklantwindow, text="Straatnaam", background=backgroundColor)
    Straatnaam.grid(row=7, column=0)
    Straatnaamentry = Entry(Nieuweklantwindow, bd=3)
    Straatnaamentry.grid(row=7, column=1)
    Huisnummer = Label(Nieuweklantwindow, text="Huisnummer", background=backgroundColor)
    Huisnummer.grid(row=8, column=0)
    Huisnummerentry = Entry(Nieuweklantwindow, bd=3)
    Huisnummerentry.grid(row=8, column=1)
    Huisnummertoevoeging = Label(Nieuweklantwindow, text="Toevoeging", background=backgroundColor)
    Huisnummertoevoeging.grid(row=8, column=2)
    Huisnummertoevoegingentry = Entry(Nieuweklantwindow, bd=3)
    Huisnummertoevoegingentry.grid(row=8, column=3)
    # --------------Bankgegevens-----------------------#
    IBAN = Label(Nieuweklantwindow, text="IBAN", background=backgroundColor)
    IBAN.grid(row=9, column=0)
    IBANentry = Entry(Nieuweklantwindow, bd=3)
    IBANentry.grid(row=9, column=1)
    # ---------------CONTACTGEGEVENS--------------------#
    Email = Label(Nieuweklantwindow, text="E-mail", background=backgroundColor)
    Email.grid(row=10, column=0)
    Emailentry = Entry(Nieuweklantwindow, bd=3)
    Emailentry.grid(row=10, column=1)
    Telefoonnummer = Label(Nieuweklantwindow, text='Telefoonnummer', background=backgroundColor)
    Telefoonnummer.grid(row=11, column=0)
    Telefoonnummerentry = Entry(Nieuweklantwindow, bd=3)
    Telefoonnummerentry.grid(row=11, column=1)
    # -----------------Abbonnement----------------------#
    Abonnement = StringVar(value="1")
    easy = Radiobutton(Nieuweklantwindow, text="Easy", variable=Abonnement, value="Easy", background=backgroundColor)
    easy.grid(row=12, column=0)
    smart = Radiobutton(Nieuweklantwindow, text="Smart", variable=Abonnement, value="Smart", background=backgroundColor)
    smart.grid(row=12, column=1)
    flex = Radiobutton(Nieuweklantwindow, text="Flex", variable=Abonnement, value="Flex", background=backgroundColor)
    flex.grid(row=12, column=2)
    # -----------------PasjUID---------------#
    PasjeUID = Label(Nieuweklantwindow, text="PasjeUID", background=backgroundColor)
    PasjeUID.grid(row=13, column=0)
    PasjeUIDentry = Entry(Nieuweklantwindow, bd=3)
    PasjeUIDentry.grid(row=13, column=1)
    # -----------------Saven van gegevens---------------#
    def toevoegenklant():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        Geboortedatum = str(GeboorteJaarentry.get()) + "-" + str(GeboorteMaandentry.get()) + "-" + str(
            GeboorteDagentry.get())
        geslacht = Geslacht.get()
        voornaam = Voornaamentry.get()
        tussenvoegsel = Tussenvoegselentry.get()
        achternaam = Achternaamentry.get()
        postcode = Postcodeentry.get()
        huisnummer = Huisnummerentry.get()
        toevoeging = Huisnummertoevoegingentry.get()
        straatnaam = Straatnaamentry.get()
        woonplaats = Woonplaatsentry.get()
        email = Emailentry.get()
        telefoonnummer = Telefoonnummerentry.get()
        Iban = IBANentry.get()
        abonnement = Abonnement.get()
        pasje = PasjeUIDentry.get()
        c.execute("INSERT INTO klantgegevens VALUES (NULL , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (pasje, geslacht, voornaam, tussenvoegsel, achternaam, Geboortedatum, postcode, huisnummer, toevoeging,
                   straatnaam, woonplaats, email, telefoonnummer, Iban, abonnement))
        Nieuweklantwindow.destroy()
        messagebox.showinfo("confirmation", "gegevens succesvol opgeslagen")
        conn.commit()
        conn.close()

    # --------------------Buttons-----------------------#
    Save = Button(Nieuweklantwindow, text="Save gegevens", command=lambda: toevoegenklant(), background=backgroundColor)
    Save.grid(row=14)


# ------------------------------NIEUWEKLANT-------------------------------#


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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        voornaam = Voornaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET voornaam=?  WHERE klantID=?", (voornaam, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        achternaam = Achternaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET achternaam=?  WHERE klantID=?", (achternaam, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        tussenvoegsel = Tussenvoegselentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET tussenvoegsel=?  WHERE klantID=?", (tussenvoegsel, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        woonplaats = Woonplaatsentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET woonplaats=?  WHERE klantID=?", (woonplaats, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        postcode = Postcodeentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET postcode=?  WHERE klantID=?", (postcode, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        straatnaam = Straatnaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET straatnaam=?  WHERE klantID=?", (straatnaam, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        huisnummer = Huisnummerentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET huisnummer=?  WHERE klantID=?", (huisnummer, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        toevoeging = Huisnummertoevoegingentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET toevoeging=?  WHERE klantID=?", (toevoeging, klantID))
        conn.commit()
        conn.close()

    Updatetoevoeging = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenhuisnummertoevoeging(), background=backgroundColor)
    Updatetoevoeging.grid(row=8, column=5)
    # --------------Bankgegevens-----------------------#
    IBAN = Label(Wijzigenklantwindow, text="IBAN", background=backgroundColor)
    IBAN.grid(row=9, column=0)
    IBANentry = Entry(Wijzigenklantwindow, bd=3)
    IBANentry.grid(row=9, column=1)

    def wijzigeniban():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        iban = IBANentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET IBAN=?  WHERE klantID=?", (iban, klantID))
        conn.commit()
        conn.close()

    Updateiban = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigeniban(), background=backgroundColor)
    Updateiban.grid(row=9, column=2)
    # ---------------EMAIL--------------------#
    Email = Label(Wijzigenklantwindow, text="E-mail", background=backgroundColor)
    Email.grid(row=10, column=0)
    Emailentry = Entry(Wijzigenklantwindow, bd=3)
    Emailentry.grid(row=10, column=1)

    def wijzigenemail():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        email = Emailentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET email=?  WHERE klantID=?", (email, klantID))
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
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        telefoonnummer = Telefoonnummerentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET telefoonnummer=?  WHERE klantID=?", (telefoonnummer, klantID))
        conn.commit()
        conn.close()

    Updatetelefoonnummer = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigentelefoonnummer(), background=backgroundColor)
    Updatetelefoonnummer.grid(row=11, column=2)
    # ------------------PasjeUID----------------------#
    PasjeUID = Label(Wijzigenklantwindow, text="PasjeUID", background=backgroundColor)
    PasjeUID.grid(row=12, column=0)
    PasjeUIDentry = Entry(Wijzigenklantwindow, bd=3)
    PasjeUIDentry.grid(row=12, column=1)

    def wijzigenpasjeUID():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        pasje = PasjeUIDentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET UID=?  WHERE klantID=?", (pasje, klantID))
        conn.commit()
        conn.close()

    Updatepasjeuid = Button(Wijzigenklantwindow, text="Update", command=lambda: wijzigenpasjeUID(), background=backgroundColor)
    Updatepasjeuid.grid(row=12, column=2)

    # ------------------Abonnement----------------------#
    Abonnement = StringVar(value="1")
    easy = Radiobutton(Wijzigenklantwindow, text="Easy", variable=Abonnement, value="Easy", background=backgroundColor)
    easy.grid(row=13, column=0)
    smart = Radiobutton(Wijzigenklantwindow, text="Smart", variable=Abonnement, value="Smart", background=backgroundColor)
    smart.grid(row=13, column=1)
    flex = Radiobutton(Wijzigenklantwindow, text="Flex", variable=Abonnement, value="Flex", background=backgroundColor)
    flex.grid(row=13, column=2)
    Verlopen = Radiobutton(Wijzigenklantwindow, text="Verlopen", variable=Abonnement, value="verlopen", background=backgroundColor)
    Verlopen.grid(row=13, column=3)

    def wijzigenabonnement():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        abonnement = Abonnement.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET abonnement=?  WHERE klantID=?", (abonnement, klantID))
        conn.commit()
        conn.close()

    Updateabonnement = Button(Wijzigenklantwindow, text="Update", background=backgroundColor, command=lambda: wijzigenabonnement())
    Updateabonnement.grid(row=13, column=4)


# ------------------------------WIJZIGENKLANT------------------------------#


# -------------------------------OPVRAGENKLANT-----------------------------#
def opvragenklant():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    Opvragenklantwindow = Toplevel(root)
    Opvragenklantwindow.configure(background=backgroundColor, pady=50)
    screenX, screenY = 700, 400
    Opvragenklantwindow.geometry('%ix%i' % (screenX, screenY))
    KlantID = Label(Opvragenklantwindow, text="KlantID", background=backgroundColor)
    KlantID.grid(row=0, column=2)
    KlantIDentry = Entry(Opvragenklantwindow, bd=3)
    KlantIDentry.grid(row=0, column=3)
    klantinformatie = Label(Opvragenklantwindow, text='')
    klantinformatie.grid(row=2, column=1)
    bekijkklant = Button(Opvragenklantwindow, text="Filter",
                         command=lambda: klantinformatie.configure(text=(klantgegevens())), background=backgroundColor)
    bekijkklant.grid(row=0, column=4)
    donebutton = Button(Opvragenklantwindow, text='Done', command=lambda: sluitopvragenklant(), background=backgroundColor)
    donebutton.grid(row=0, column=0)
    list = ""
    for row in c.execute(
            "SELECT * FROM klantgegevens"):
        list += str(row[0]) + '-' + str(row[1]) + '-' + str(row[2]) + '-' + str(row[3]) + '-' + str(row[4]) + '-' + str(
            row[5]) + '-' + str(row[6]) + '-' + str(row[7]) + '-' + str(row[8]) + '-' + str(row[9]) + '-' + str(
            row[10]) + '-' + str(row[11]) + '-' + str(row[12]) + '-' + str(row[13]) + '-' + str(row[14]) + '-' + str(row[15]) + '\n'
    klantinformatie.configure(text=list)
    conn.close()

    def klantgegevens():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(data[13]) + '-' +str(data[14]) + '-' + str(data[15]) + '\n'
        conn.close()
        return list  # het returne van de print statement

    def sluitopvragenklant():
        Opvragenklantwindow.destroy()


# -------------------------OPVRAGENKLANT-------------------------#


# -------------------------VERWIJDERENKLANT----------------------#
def verwijderenklant():
    verwijderenklantwindow = Toplevel(root)
    verwijderenklantwindow.configure(background=backgroundColor)
    screenX, screenY = 700, 200
    verwijderenklantwindow.geometry('%ix%i' % (screenX, screenY))
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    KlantID = Label(verwijderenklantwindow, text="KlantID", background=backgroundColor)
    KlantID.grid(row=0, column=2)
    KlantIDentry = Entry(verwijderenklantwindow, bd=3)
    KlantIDentry.grid(row=0, column=3)
    klantinformatie = Label(verwijderenklantwindow, text='')
    klantinformatie.grid(row=1, column=1)
    bekijkklant = Button(verwijderenklantwindow, text="Filter", background=backgroundColor,
                         command=lambda: klantinformatie.configure(text=(klantgegevens())))
    bekijkklant.grid(row=0, column=4)
    donebutton = Button(verwijderenklantwindow, text='Done', command=lambda: sluitverwijderenklant(), background=backgroundColor)
    donebutton.grid(row=0, column=0)
    verwijderenbutton = Button(verwijderenklantwindow, text='verwijderen', command=lambda: verwijderen(), background=backgroundColor)
    verwijderenbutton.grid(row=1, column=2)

    def klantgegevens():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantID)  # gevens ophalen uit de DB
        data = c.fetchone()  # opgehaalde gevens in een lijst zetten
        list = str(data[0]) + '-' + str(data[1]) + '-' + str(data[2]) + '-' + str(data[3]) + '-' + str(
            data[4]) + '-' + str(data[5]) + '-' + str(data[6]) + '-' + str(data[7]) + '-' + str(data[8]) + '-' + str(
            data[9]) + '-' + str(data[10]) + '-' + str(data[11]) + '-' + str(data[12]) + '-' + str(data[13]) + '-' + str(data[14]) + '-' + str(data[15]) + '\n'
        conn.close()
        return list  # het returne van de print statement

    def verwijderen():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        klantID = KlantIDentry.get()
        c.execute("DELETE FROM klantgegevens WHERE klantID=?", klantID)
        conn.commit()
        conn.close()

    def sluitverwijderenklant():
        verwijderenklantwindow.destroy()

#-----------------------------------------VERWIJDERENKLANT--------------------------------------#

backgroundColor = 'LightBlue2'

root = Tk()
welkomLabel = Label(background=backgroundColor, foreground= 'navy', text='Benno sport administratie', font=('', 40, ''))
welkomLabel.pack(side=TOP)
NieuweKlantwindowButton = Button(root, text="Nieuwe Klant", command=NieuweKlant, width =80, height =10, background='cyan2', font=('', 10, ''))
NieuweKlantwindowButton.pack(pady =10)
WijzigenklantwindowButton = Button(root, text="Wijzigen Klant", command=Wijzigenklant, width =80, height =10, background='cyan2', font=('', 10, ''))
WijzigenklantwindowButton.pack(pady =10)
OpvragenklantwindowButton = Button(root, text="opvragen klant", command=opvragenklant, width =80, height =10, background='cyan2', font=('', 10, ''))
OpvragenklantwindowButton.pack(pady =10)
VerwijderenklantwindowButton = Button(root, text='klant verwijderen', command=verwijderenklant, width =80, height =10, background='cyan2', font=('', 10, ''))
VerwijderenklantwindowButton.pack(pady =10)
root.configure(background=backgroundColor)

root.mainloop()

