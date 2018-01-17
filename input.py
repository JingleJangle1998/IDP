import sqlite3
connection = sqlite3.connect("company.db")


geslacht = input('Geslacht:')
voornaam = input('Voornaam:')
tussenvoegsel = input('Tussenvoegsel:')
achternaam = input('Achternaam:')
geboortedatum = input('Geboortedatum:')
postcode = input('Postcode:')
huisnummer = input('Huisnummer:')
toevoeging = input('Toevoeging:')
straatnaam = input('Straatnaam:')
woonplaats = input('Woonplaats:')
email = input('Email:')
telefoonnummer = input('Telefoonnummer: ')
IBAN = input('IBAN:')



cursor = connection.cursor()

staff_data = [(geslacht, voornaam, achternaam, geboortedatum, postcode, huisnummer, straatnaam, woonplaats, email, telefoonnummer, IBAN)]

for p in staff_data:
    format_str = """INSERT INTO klantgegevens (klantID, geslacht, voornaam, achternaam, geboortedatum, postcode, huisnummer, straatnaam, woonplaats, email, telefoonnummer, iban)
    VALUES (NULL, "{geslacht}", "{voor}", "{achter}", "{geboorte}", "{postcode}", "{huisnummer}", "{straatnaam}", "{woonplaats}", "{email}", "{telefoonnummer}", "{iban}");"""

    sql_command = format_str.format(geslacht=p[0], voor=p[1], achter=p[2], geboorte=p[3], postcode=p[4], huisnummer=p[5], straatnaam=p[6], woonplaats=p[7], email=p[8], telefoonnummer=p[9], iban=p[10])
    cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()