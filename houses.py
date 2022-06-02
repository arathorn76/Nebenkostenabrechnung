"""Module providing stuff for houses."""

from types import CoroutineType
from unicodedata import name


class House:
    """Class for modelling houses.
    
    Context: calculating side costs for renters"""
    
    def __init__(self, name, streat_and_number, zipcode, city):
        self.name = name
        self.streat_and_number = streat_and_number
        self.zipcode = zipcode
        self.city = city

    def get_adress(self):
        return self.name + "\n" + self.streat_and_number + "\n" + self.zipcode + " " + self.city
        
