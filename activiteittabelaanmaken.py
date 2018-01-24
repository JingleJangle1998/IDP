import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE  activiteit ( 
activeitenID INTEGER PRIMARY KEY,
klantID INTEGER,
apparaatID INTEGER,
tijd INTEGER,
aantalkeer INTEGER ,
afstand INTEGER ,
verbranddeKcal REAL,
FOREIGN KEY(klantID) REFERENCES klantgegevens(klantID),
FOREIGN KEY(apparaatID) REFERENCES apparaten(apparaatID));"""

cursor.execute(sql_command)



# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()