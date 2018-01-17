import sqlite3
connection = sqlite3.connect("sport.db")

cursor = connection.cursor()

klantid = input('Klantid:')


cursor.execute("SELECT * FROM klantgegevens WHERE klantID=?", klantid)
print("\npersoon:")
res = cursor.fetchall()
print(res)