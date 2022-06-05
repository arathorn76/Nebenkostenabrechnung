"""Module providing stuff for houses."""

import pickle

housefile = "data\\houses.pickle"


##############################################################################
############################## Class definitions #############################
##############################################################################
class House:
    """Class for modelling houses.
    
    Context: calculating side costs for renters"""
    
    def __init__(self, name, streat_and_number = "21 Jump Street", zipcode="12345", city="Stadt"):
        self.name = name
        self.streat_and_number = streat_and_number
        self.zipcode = zipcode
        self.city = city

    def get_adress(self):
        return self.name + "\n" + self.streat_and_number + "\n" + self.zipcode + " " + self.city

# Persistenz
def load_houses():
    global houses
    try:
        with open(housefile, "rb") as f:
            houses = pickle.load(f)
    except FileNotFoundError:
        save_houses()

def save_houses():
    global houses
    with open(housefile, "wb") as f:
        pickle.dump(houses, f)



#Initialisierung des Moduls
houses = list()