"""Modul zur Verwaltung der Daten


"""

import sqlite3
import config.settings as settings

##############################################################################
################################ DB definition ###############################
##############################################################################
def create_adress_table(zeiger):
    zeiger.execute("""
        CREATE TABLE IF NOT EXISTS adressen (
            id INTEGER PRIMARY KEY,
            strasse VARCHAR(40),
            hausnummer VARCHAR(10),
            strasse2 VARCHAR(40),
            hausnummer2 VARCHAR(10),
            plz VARCHAR(8),
            ort VARCHAR(40),
            land VARCHAR(40)
        )
    """)

def create_house_table(zeiger):
    zeiger.execute("""
        CREATE TABLE IF NOT EXISTS houses (
            id INTEGER PRIMARY KEY,
            name VARCHAR(40),
            adress_id REFERENCES adressen(id),
            size INTEGER
        )
    """)

def create_appt_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS appartments (
            id INTEGER PRIMARY KEY,
            name VARCHAR(40),
            house_id REFERENCES houses(id),
            lage VARCHAR(40),
            size INTEGER,
            roomcount INTEGER
        )
    """)

def create_meters_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS meters (
            id INTEGER PRIMARY KEY,
            name VARCHAR(40),
            type VARCHAR(20),
            lage VARCHAR(80),
            number VARCHAR(40)
        )
    """)

def create_metervalues_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS metervalues (
            meter_id REFERENCES meters(id),
            datum DATE,
            value FLOAT,
            PRIMARY KEY(meter_id, datum)
        )
    """)

def create_house_appt_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS house_appartments (
            house_id REFERENCES houses(id),
            appartment_id REFERENCES appartments(id),
            PRIMARY KEY (house_id, appartment_id)
        )
    """)

def create_meter_registration_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS meter_registration (
            meter_id REFERENCES meters(id),
            house_id REFERENCES houses(id),
            appartment_id REFERENCES appartments(id),
            begda DATE,
            endda DATE,
            PRIMARY KEY (meter_id, house_id, appartment_id)
        )
    """)

def create_renter_location_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS renter_location (
            renter_id REFERENCES renters(id),
            appartment_id REFERENCES appartments(id),
            begda_vertrag DATE,
            endda_vertrag DATE,
            datum_uebergabe DATE,
            datum_rueckgabe DATE,
            deposit_payed FLOAT,
            deposit_last_payment DATE,
            deposit_keep FLOAT,
            deposit_keep_reason VARCHAR(200),
            deposit_returned_date DATE,
            PRIMARY KEY (renter_id, appartment_id)
        )
    """)

def create_renters_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS renters (
            id INTEGER PRIMARY KEY,
            anrede1 VARCHAR(40),
            vorname1 VARCHAR(40),
            nachname1 VARCHAR(40),
            anrede2 VARCHAR(40),
            vorname2 VARCHAR(40),
            nachname2 VARCHAR(40),
            weitere_personen VARCHAR(200),
            adresse_vorher REFERENCES adressen(id),
            adresse_nachher REFERENCES adressen(id),
            anzahl_personen INTEGER
        )
    """)
    # anzahl_personen evtl. in separate Tabelle mit Zeitraum-Bezug?

def create_db():
    verbindung = sqlite3.connect(settings.dbfile)
    zeiger = verbindung.cursor()
    create_adress_table(zeiger)
    create_renters_table(zeiger)
    create_house_table(zeiger)
    create_appt_table(zeiger)
    create_meters_table(zeiger)
    create_metervalues_table(zeiger)
    create_house_appt_table(zeiger)
    create_meter_registration_table(zeiger)
    create_renter_location_table(zeiger)
    verbindung.commit()
    verbindung.close()

##############################################################################
############################ read/write access ###############################
##############################################################################



def read_renters():
    verbindung = sqlite3.connect(settings.dbfile)
    zeiger = verbindung.cursor()
    sql_string = """
    select * from renters
    """
    zeiger.execute(sql_string)
    renters = zeiger.fetchall()
    verbindung.close()
    return renters

def read_adressen():
    verbindung = sqlite3.connect(settings.dbfile)
    zeiger = verbindung.cursor()
    sql_string = """
    select * from adressen
    """
    zeiger.execute(sql_string)
    adressen = zeiger.fetchall()
    verbindung.close()
    return adressen

def read_houses():
    verbindung = sqlite3.connect(settings.dbfile)
    zeiger = verbindung.cursor()
    sql_string = """
    select * from houses
    """
    zeiger.execute(sql_string)
    houses = zeiger.fetchall()
    verbindung.close()
    return houses

if __name__ == "__main__":
    create_db()

