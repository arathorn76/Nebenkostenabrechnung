"""Modul stellt Funktionalitäten zur Verwaltung von Mietern bereit."""

import pickle

rentersfile = "data\\renters.pickle"
class Renter:

    def __init__(self, anrede = "n/a", name = "Leerstand"):
        self.anrede = anrede
        self.name = name
        self.number_people = 1

    def set_appartment(self, appartment):
        pass

    def set_number_people(self, number_people):
        self.number_people = number_people


# Persistenz
def load_renters():
    with open(rentersfile, "rb") as f:
        global renters
        renters = pickle.load(f)

def save_renters():
    with open(rentersfile, "wb") as f:
        pickle.dump(renters, f)



# Initialisierung des Moduls
renters = list()

