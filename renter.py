"""Modul stellt Funktionalitäten zur Verwaltung von Mietern bereit."""

import db
import sqlite3
import config.settings as settings

class Renter:

    def __init__(self, id = None, 
                anrede1 = "n/a",  vorname1 = None, nachname1 = "Leerstand", 
                anrede2 = None, vorname2 = None, nachname2 = None,
                weitere_personen = None, adresse_vorher = None, adresse_nachher = None, anzahl_personen = 1):
        self.id = id
        self.anrede1 = anrede1
        self.vorname1 = vorname1
        self.nachname1 = nachname1
        self.anrede2 = anrede2
        self.vorname2 = vorname2
        self.nachname2 = nachname2
        self.weitere_personen = weitere_personen
        self.adresse_vorher = adresse_vorher
        self.adresse_nachher = adresse_nachher
        self.anzahl_personen = anzahl_personen

    def db_insert(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "insert into renters values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        zeiger.execute(sql_string, (
            None,
            self.anrede1,
            self.vorname1,
            self.nachname1,
            self.anrede2,
            self.vorname2,
            self.nachname2,
            self.weitere_personen,
            self.adresse_vorher,
            self.adresse_nachher,
            self.anzahl_personen
        ))
        verbindung.commit()
        self.id = zeiger.lastrowid
        verbindung.close()

    def db_update(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = """update renters set
            anrede1=?, vorname1=?, nachname1=?, 
            anrede2=?, vorname2=?, nachname2=?,
            weitere_personen=?,
            adresse_vorher=?, adresse_nachher=?,
            anzahl_personen=? where id=?"""
        zeiger.execute(sql_string, (
            self.anrede1,
            self.vorname1,
            self.nachname1,
            self.anrede2,
            self.vorname2,
            self.nachname2,
            self.weitere_personen,
            self.adresse_vorher,
            self.adresse_nachher,
            self.anzahl_personen,
            self.id
        ))
        verbindung.commit()
        verbindung.close()

    def db_delete(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "delete from renters where id = ?"
        zeiger.execute(sql_string, (self.id,))
        verbindung.commit()
        verbindung.close()


# Persistenz
def load_renters():
    global renters
    renters.clear()
    for r in db.read_renters():
        renters.append(Renter(*r))

        
# Initialisierung des Moduls
renters = list()
load_renters()

