import sqlite3
import pymysql
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='schaap14',
                             db='company',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
c = connection.cursor()


c.execute("""INSERT INTO apparaten (apparaatID, naam, kcalperminuut)

    VALUES (NULL, 'hardlopen', 45

);""")

c.execute("""INSERT INTO apparaten (apparaatID, naam, kcalperminuut)

    VALUES (NULL, 'fietsen', 60

);""")

c.execute("""INSERT INTO apparaten (apparaatID, naam,kcalperminuut)

    VALUES (NULL, 'benchpress' ,2

);""")

c.execute("""INSERT INTO apparaten (apparaatID, naam, kcalperminuut)

    VALUES (NULL, 'roeien', 84

);""")

c.execute("""INSERT INTO apparaten (apparaatID, naam, kcalperminuut)

    VALUES (NULL, 'pulldown', 1 

);""")
# never forget this, if you want the changes to be saved:
connection.commit()
connection.close()