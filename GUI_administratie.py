from tkinter import *
from tkinter import messagebox
import sqlite3



# -------------------------------NIEUWEKLANT-------------------------------------#
def NieuweKlant():
    Nieuweklantwindow = Toplevel(root)
    # ---------------GESLACHT---------------------------#
    Geslacht = StringVar(value="1")
    Dhr = Radiobutton(Nieuweklantwindow, text="Dhr.", variable=Geslacht, value="Dhr.")
    Dhr.grid(row=0, column=0)
    Mevr = Radiobutton(Nieuweklantwindow, text="Mevr", variable=Geslacht, value="Mevr")
    Mevr.grid(row=0, column=1)
    # ---------------VOORNAAM---------------------------#
    Voornaam = Label(Nieuweklantwindow, text="Voornaam")
    Voornaam.grid(row=1, column=0, sticky=W)
    Voornaamentry = Entry(Nieuweklantwindow, bd=3)
    Voornaamentry.grid(row=1, column=1)
    # ----------------ACHTERNAAM-------------------------#
    Achternaam = Label(Nieuweklantwindow, text="Achternaam")
    Achternaam.grid(row=2, column=0, sticky=W)
    Achternaamentry = Entry(Nieuweklantwindow, bd=3)
    Achternaamentry.grid(row=2, column=1)
    Tussenvoegsel = Label(Nieuweklantwindow, text="Tussenvoegsel")
    Tussenvoegsel.grid(row=2, column=2)
    Tussenvoegselentry = Entry(Nieuweklantwindow, bd=3)
    Tussenvoegselentry.grid(row=2, column=3)
    # ---------------GEBOORTEDATUM----------------------#
    GeboorteDag = Label(Nieuweklantwindow, text="dd")
    GeboorteDag.grid(row=3, column=0)
    GeboorteDagentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteDagentry.grid(row=3, column=1)
    Geboortemaand = Label(Nieuweklantwindow, text="mm")
    Geboortemaand.grid(row=4, column=0)
    GeboorteMaandentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteMaandentry.grid(row=4, column=1)
    Geboortejaar = Label(Nieuweklantwindow, text="jjjj")
    Geboortejaar.grid(row=5, column=0)
    GeboorteJaarentry = Entry(Nieuweklantwindow, bd=3)
    GeboorteJaarentry.grid(row=5, column=1)
    # ---------------Adresss----------------------------#
    Woonplaats = Label(Nieuweklantwindow, text="Woonplaats")
    Woonplaats.grid(row=6, column=0)
    Woonplaatsentry = Entry(Nieuweklantwindow, bd=3)
    Woonplaatsentry.grid(row=6, column=1)
    Postcode = Label(Nieuweklantwindow, text="Postcode")
    Postcode.grid(row=6, column=2)
    Postcodeentry = Entry(Nieuweklantwindow, bd=3)
    Postcodeentry.grid(row=6, column=3)
    Straatnaam = Label(Nieuweklantwindow, text="Straatnaam")
    Straatnaam.grid(row=7, column=0)
    Straatnaamentry = Entry(Nieuweklantwindow, bd=3)
    Straatnaamentry.grid(row=7, column=1)
    Huisnummer = Label(Nieuweklantwindow, text="Huisnummer")
    Huisnummer.grid(row=8, column=0)
    Huisnummerentry = Entry(Nieuweklantwindow, bd=3)
    Huisnummerentry.grid(row=8, column=1)
    Huisnummertoevoeging = Label(Nieuweklantwindow, text="Toevoeging")
    Huisnummertoevoeging.grid(row=8, column=2)
    Huisnummertoevoegingentry = Entry(Nieuweklantwindow, bd=3)
    Huisnummertoevoegingentry.grid(row=8, column=3)
    # --------------Bankgegevens-----------------------#
    IBAN = Label(Nieuweklantwindow, text="IBAN")
    IBAN.grid(row=9, column=0)
    IBANentry = Entry(Nieuweklantwindow, bd=3)
    IBANentry.grid(row=9, column=1)
    # ---------------CONTACTGEGEVENS--------------------#
    Email = Label(Nieuweklantwindow, text="E-mail")
    Email.grid(row=10, column=0)
    Emailentry = Entry(Nieuweklantwindow, bd=3)
    Emailentry.grid(row=10, column=1)
    Telefoonnummer = Label(Nieuweklantwindow, text='Telefoonnummer')
    Telefoonnummer.grid(row=11, column=0)
    Telefoonnummerentry = Entry(Nieuweklantwindow, bd=3)
    Telefoonnummerentry.grid(row=11, column=1)
    # -----------------Abbonnement----------------------#
    abonnement = StringVar(value="1")
    easy = Radiobutton(Nieuweklantwindow, text="Easy", variable=abonnement, value="Easy")
    easy.grid(row=12, column=0)
    smart = Radiobutton(Nieuweklantwindow, text="Smart", variable=abonnement, value="Smart")
    smart.grid(row=12, column=1)
    flex = Radiobutton(Nieuweklantwindow, text="Flex", variable=abonnement, value="Flex")
    flex.grid(row=12, column=2)
    # -----------------Saven van gegevens---------------#
    def toevoegenklant():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        Geboortedatum = str(GeboorteJaarentry.get())+"-"+str(GeboorteMaandentry.get())+"-"+str(GeboorteDagentry.get())
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
        c.execute("INSERT INTO klantgegevens VALUES (NULL , ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (geslacht, voornaam, tussenvoegsel, achternaam, Geboortedatum, postcode, huisnummer, toevoeging,
                   straatnaam, woonplaats, email, telefoonnummer, Iban))
        Nieuweklantwindow.destroy()
        messagebox.showinfo("confirmation", "gegevens succesvol opgeslagen")
        conn.commit()
        conn.close()

    # --------------------Buttons-----------------------#
    Save = Button(Nieuweklantwindow, text="Save gegevens", command=lambda : toevoegenklant())
    Save.grid(row=13)
# ------------------------------NIEUWEKLANT-------------------------------#


# ------------------------------WIJZIGENKLANT-----------------------------#
def Wijzigenklant():
    Wijzigenklantwindow = Toplevel(root)
    #----------------KlantID----------------------------#
    KlantID = Label(Wijzigenklantwindow, text="KlantID")
    KlantID.grid(row=0, column=0)
    KlantIDentry = Entry(Wijzigenklantwindow, bd=3)
    KlantIDentry.grid(row=0, column=1)
    # ---------------VOORNAAM---------------------------#
    Voornaam = Label(Wijzigenklantwindow, text="Voornaam")
    Voornaam.grid(row=1, column=0, sticky=W)
    Voornaamentry = Entry(Wijzigenklantwindow, bd=3)
    Voornaamentry.grid(row=1, column=1)
    def wijzigenvoornaam():
        conn = sqlite3.connect('company.db')
        c = conn.cursor()
        voornaam = Voornaamentry.get()
        klantID = KlantIDentry.get()
        c.execute("UPDATE klantgegevens SET voornaam =  WHERE klantID = 1")
        conn.commit()
        conn.close()

    Updatevoornaam = Button(Wijzigenklantwindow, text="Update", command=lambda : wijzigenvoornaam() )
    Updatevoornaam.grid(row=1, column=3)
    # ----------------ACHTERNAAM-------------------------#
    Achternaam = Label(Wijzigenklantwindow, text="Achternaam")
    Achternaam.grid(row=2, column=0, sticky=W)
    Achternaamentry = Entry(Wijzigenklantwindow, bd=3)
    Achternaamentry.grid(row=2, column=1)
    Tussenvoegsel = Label(Wijzigenklantwindow, text="Tussenvoegsel")
    Tussenvoegsel.grid(row=2, column=2)
    Tussenvoegselentry = Entry(Wijzigenklantwindow, bd=3)
    Tussenvoegselentry.grid(row=2, column=3)
    # ---------------Adresss----------------------------#
    Woonplaats = Label(Wijzigenklantwindow, text="Woonplaats")
    Woonplaats.grid(row=6, column=0)
    Woonplaatsentry = Entry(Wijzigenklantwindow, bd=3)
    Woonplaatsentry.grid(row=6, column=1)
    Postcode = Label(Wijzigenklantwindow, text="Postcode")
    Postcode.grid(row=6, column=2)
    Postcodeentry = Entry(Wijzigenklantwindow, bd=3)
    Postcodeentry.grid(row=6, column=3)
    Straatnaam = Label(Wijzigenklantwindow, text="Straatnaam")
    Straatnaam.grid(row=7, column=0)
    Straatnaamentry = Entry(Wijzigenklantwindow, bd=3)
    Straatnaamentry.grid(row=7, column=1)
    Huisnummer = Label(Wijzigenklantwindow, text="Huisnummer")
    Huisnummer.grid(row=8, column=0)
    Huisnummerentry = Entry(Wijzigenklantwindow, bd=3)
    Huisnummerentry.grid(row=8, column=1)
    Huisnummertoevoeging = Label(Wijzigenklantwindow, text="Toevoeging")
    Huisnummertoevoeging.grid(row=8, column=2)
    Huisnummertoevoegingentry = Entry(Wijzigenklantwindow, bd=3)
    Huisnummertoevoegingentry.grid(row=8, column=3)
    # --------------Bankgegevens-----------------------#
    IBAN = Label(Wijzigenklantwindow, text="IBAN")
    IBAN.grid(row=9, column=0)
    IBANentry = Entry(Wijzigenklantwindow, bd=3)
    IBANentry.grid(row=9, column=1)
    # ---------------CONTACTGEGEVENS--------------------#
    Email = Label(Wijzigenklantwindow, text="E-mail")
    Email.grid(row=10, column=0)
    Emailentry = Entry(Wijzigenklantwindow, bd=3)
    Emailentry.grid(row=10, column=1)
    Telefoonnummer = Label(Wijzigenklantwindow, text='Telefoonnummer')
    Telefoonnummer.grid(row=11, column=0)
    Telefoonnummerentry = Entry(Wijzigenklantwindow, bd=3)
    Telefoonnummerentry.grid(row=11, column=1)
    #------------------Abbonnement----------------------#
    abonnement = StringVar(value="1")
    easy = Radiobutton(Wijzigenklantwindow, text="Easy", variable=abonnement, value="Easy")
    easy.grid(row=12, column=0)
    smart = Radiobutton(Wijzigenklantwindow, text="Smart", variable=abonnement, value="Smart")
    smart.grid(row=12, column=1)
    flex = Radiobutton(Wijzigenklantwindow, text="Flex", variable=abonnement, value="Flex")
    flex.grid(row=12, column=2)
    Verlopen = Radiobutton(Wijzigenklantwindow, text="Verlopen", variable=abonnement, value="verlopen")
    Verlopen.grid(row=12, column=3)
# ------------------------------WIJZIGENKLANT-----------------------------#


#-------------------------------opvragenklant-----------------------------#
def opvragenklant():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
    Opvragenklantwindow = Toplevel(root)
    c.execute("SELECT * FROM users")  # gevens ophalen uit de DB
    list = c.fetchone()  # opgehaalde gevens in een lijst zetten
    conn.commit()
    conn.close()
    return list[0]  # het returne van de print statement





root = Tk()
NieuweKlantwindowButton = Button(root, text="Nieuwe Klant", command=NieuweKlant)
NieuweKlantwindowButton.pack()
WijzigenklantwindowButton = Button(root, text="Wijzigen Klant", command=Wijzigenklant)
WijzigenklantwindowButton.pack()
OpvragenklantwindowButton = Button(root, text="opvragen klant", command=opvragenklant)
OpvragenklantwindowButton.pack()
root.mainloop()
