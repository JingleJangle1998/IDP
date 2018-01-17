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

sql_command = """INSERT INTO klantgegevens (geslacht, voornaam, achternaam, geboortedatum, postcode, huisnummer, straatnaam, woonplaats, email, telefoonnummer, iban)
    VALUES (NULL, 'man', 'sohaib', 'elb', '1961-10-25', '3515GN', 51, 'lauwerecht', 'utrecht', 's_elb@outlook.com', '0619096355', 'NL79281894');"""
cursor.execute(sql_command)



# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()