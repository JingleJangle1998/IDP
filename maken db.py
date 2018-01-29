import sqlite3
conn = sqlite3.connect("company.db")
c = conn.cursor()

c.execute("""
CREATE TABLE klantgegevens( 
klantID INTEGER PRIMARY KEY,
UID INTEGER,
geslacht VARCHAR(255),
voornaam VARCHAR(255),
tussenvoegsel VARCHAR(255),
achternaam VARCHAR(255),
geboortedatum DATE,
postcode VARCHAR(255),
huisnummer INTEGER,
toevoeging VARCHAR(255) ,
straatnaam VARCHAR(255),
woonplaats VARCHAR(255),
email VARCHAR(255),
telefoonnummer VARCHAR(255),
IBAN VARCHAR(255),
abonnement VARCHAR (255));""")

c.execute("""
CREATE TABLE  apparaten ( 
apparaatID INTEGER PRIMARY KEY,
naam VARCHAR(255),
beschrijving VARCHAR(255),
kcalperminuut REAL);""")

c.execute("""
CREATE TABLE  activiteit ( 
activeitenID INTEGER PRIMARY KEY,
klantID INTEGER,
apparaatID INTEGER,
tijd INTEGER,
aantalkeer INTEGER ,
afstand INTEGER ,
verbranddeKcal REAL,
FOREIGN KEY(klantID) REFERENCES klantgegevens(klantID),
FOREIGN KEY(apparaatID) REFERENCES apparaten(apparaatID));""")

conn.commit()
conn.close()