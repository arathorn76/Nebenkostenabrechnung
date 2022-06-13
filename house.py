"""Module providing stuff for houses."""

import db
import sqlite3
import config.settings as settings


##############################################################################
############################## Class definitions #############################
##############################################################################
class House:
    """Class for modelling houses.
    
    Context: calculating side costs for renters"""
    
    def __init__(self, id = None, name='neues Haus', adress_id = None, size = 0):
        self.id = id
        self.name = name
        self.size = size
        self.adress_id = adress_id

    def db_insert(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "insert into houses values(?, ?, ?, ?)"
        zeiger.execute(sql_string, (
            None,
            self.name,
            self.adress_id,
            self.size
        ))
        verbindung.commit()
        self.id = zeiger.lastrowid
        verbindung.close()

    def db_update(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = """update houses set name=?, adress_id=?,  size=? where id=?"""
        zeiger.execute(sql_string, (
            self.name,
            self.adress_id,
            self.size,
            self.id
        ))
        verbindung.commit()
        verbindung.close()

    def db_delete(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "delete from houses where id = ?"
        zeiger.execute(sql_string, (self.id,))
        verbindung.commit()
        verbindung.close()

# Persistenz
def load_houses():
    global houses
    houses.clear()
    for h in db.read_houses():
        houses.append(House(*h))


#Initialisierung des Moduls
houses = list()
load_houses()