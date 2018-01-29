import pymysql
import pymysql.cursors
conn = pymysql.connect(host='188.166.116.67',
                               user='groep5',
                               password='HWu4RTsD8&@UUN',
                               db='groep5_benno',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()


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
conn.commit()
conn.close()