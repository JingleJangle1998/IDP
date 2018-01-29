import sqlite3
import pymysql
import pymysql.cursors
conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()

c.execute("""
CREATE TABLE klantgegevens( 
klantID INTEGER auto_increment PRIMARY KEY,
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
apparaatID INTEGER auto_increment PRIMARY KEY,
naam VARCHAR(255),
kcalperminuut REAL);""")

c.execute("""
CREATE TABLE  activiteit ( 
activeitenID INTEGER auto_increment PRIMARY KEY,
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