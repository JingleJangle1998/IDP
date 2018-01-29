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
CREATE TABLE  aanwezigheid ( 
aanwezigheidID INTEGER auto_increment PRIMARY KEY,
klantID INTEGER,
datum VARCHAR(255),
inlogtijd VARCHAR(255),
uitlogtijd VARCHAR(255),
FOREIGN KEY(klantID) REFERENCES klantgegevens(klantID));""")



conn.commit()
conn.close()