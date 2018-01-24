import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()



sql_command1 = """INSERT INTO apparaten (apparaatID, naam, beschrijving, kcalperminuut)
    VALUES (NULL, 'hardlopen', 'Een loopband is een trainings- of onderzoeksapparaat om op te bewegen.
Loopbanden worden veel ingezet als fitnessmateriaal. De apparaten worden voor privégebruik in huis aangeschaft en staan opgesteld in fitnesscentra. In deze toepassing (er zijn ook loopbanden voor transport/vervoer bijvoorbeeld op luchthavens) zijn het grote lopende banden voor mensen om op te bewegen met als doel, verbetering van: de conditie, de gezondheid en/of de lichaamsbouw. Hieraan kan gewerkt worden terwijl men op dezelfde plaats blijft.', 45
);"""
cursor.execute(sql_command1)

sql_command2 = """INSERT INTO apparaten (apparaatID, naam, beschrijving, kcalperminuut)
    VALUES (NULL, 'fietsen', 'Een fitnessapparaat waarop fietsbewegingen gemaakt kunnen worden om daarmee de lichamelijke conditie te verbeteren', 60
);"""
cursor.execute(sql_command2)

sql_command3 = """INSERT INTO apparaten (apparaatID, naam, beschrijving, kcalperminuut)
    VALUES (NULL, 'benchpress', 'Bankdrukken, of bench press, is een oefening waarbij een bepaalde weerstand, een gewicht, moet worden overwonnen, liggende op een speciale bank. Een drukbank is meestal voorzien van haltersteunen zodat een lange halter (een barbell) vanuit liggende positie gepakt kan worden. De halter wordt vervolgens omlaag gebracht naar de borst en raakt deze liefst kort aan en daarna wordt de halter met kracht weer omhoog geduwd. Deze oefening wordt vaak gebruikt bij fitnesstraining, bodybuilding, powerlifting en krachttraining. Het is tevens één van de bekendste oefeningen bij weerstandtraining (gewichttraining).',2
);"""
cursor.execute(sql_command3)

sql_command4 = """INSERT INTO apparaten (apparaatID, naam, beschrijving, kcalperminuut)
    VALUES (NULL, 'roeien', 'Een indoorroeier of roei-ergometer is een machine die wordt gebruikt voor de simulatie van de actie van waterkracht - roeien, als oefening of als opleiding voor het roeien. Wedstrijden in indoorroeien worden ook ingericht als een sport op zich. De term indoorroeier verwijst ook naar een deelnemer aan deze sport. Een bekend merk, dat ook in bijna elke sportscholen/fitnesscentra is terug te vinden, is Concept2.', 84
);"""
cursor.execute(sql_command4)

sql_command5 = """INSERT INTO apparaten (apparaatID, naam, beschrijving, kcalperminuut)
    VALUES (NULL, 'pulldown', 'De pulldown-oefening is een krachttraining die bedoeld is om de latissimus dorsi-spier te ontwikkelen . Het vervult de functies van neerwaartse rotatie en depressie van de scapulae in combinatie met adductie en extensie van het schoudergewricht.', 1 
);"""
cursor.execute(sql_command5)

# never forget this, if you want the changes to be saved:
connection.commit()

connection.close()