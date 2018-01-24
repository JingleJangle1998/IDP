import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE klantgegevens ( 
klantID INTEGER PRIMARY KEY,
geslacht VARCHAR(255),
voornaam VARCHAR(255),
tussenvoegsel VARCHAR(255)  ,
achternaam VARCHAR(255),
geboortedatum DATE,
postcode VARCHAR(255),
huisnummer INTEGER,
toevoeging VARCHAR(255) ,
straatnaam VARCHAR(255),
woonplaats VARCHAR(255),
email VARCHAR(255),
telefoonnummer VARCHAR(255),
IBAN VARCHAR(255));"""

cursor.execute(sql_command)


# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()