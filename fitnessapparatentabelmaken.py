import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE  apparaten ( 
apparaatID INTEGER PRIMARY KEY,
naam VARCHAR(255),
beschrijving VARCHAR(255),
kcalperminuut REAL);"""

cursor.execute(sql_command)


# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()