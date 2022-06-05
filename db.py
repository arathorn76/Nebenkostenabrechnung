"""Modul zur Verwaltung der Daten


"""

import sqlite3
import config.settings as settings

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
            number VARCHAR(40),
        )
    """)

def create_metervalues_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS metervalues (
            meter_id REFERENCES meters(id),
            datum DATE,
            value FLOAT,
            PRIMARY KEX(meter_id, datum)
        )
    """)

def create_house_appt_table(zeiger):
        zeiger.execute("""
        CREATE TABLE IF NOT EXISTS house_appartments (
            house_id REFERENCES houses(id),
            appartment_id REFERNCES appartments(id),
            PRIMARY KEY (house_id, appartment_id)
        )
    """)

def create_meter_location_table(zeiger):
    pass
# Zählerzuordnung
# Zähler-ID
# Haus-ID
# Wohnungs-ID (* oder None bei Hauszählern)
# Beginndatum
# Endedatum

def create_renter_location_table(zeiger):
    pass
# Mieterzuorndung
# Mieter-ID
# Wohnungs-ID
# Beginndatum Mietvertrag
# Endedatum Mietvertrag
# Datum Übergabe an Mieter
# Datum Rücknahme von Mieter
# Kaution
# Kaution gezahlt am
# kürzung Kautionsrückzahlung
# Kaution zurückgezahlt am

def create_renters_table(zeiger):
    pass
# Mietertabelle
# Anrede
# Vorname
# Nachname
# Weitere Personen
# Adresse Vorher
# Adresse Nachher
# Anzahl Personen (gültib ab/bis?)

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
    create_meter_location_table(zeiger)
    create_renter_location_table(zeiger)
    
    verbindung.commit()

    verbindung.close()







