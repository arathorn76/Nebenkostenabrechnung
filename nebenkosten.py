"""Main program for side costs
"""

#import houses
import renter
import renter_driver
import tkinter
import config.nebenkosten_text_de as texte

# h1 = houses.House("Daxstein", "Oberer Daxstein 21", "12345", "Zenting")

# print(h1.get_adress())

# r1 = renter.Renter("Herr", "Christian Manderla")

# r1.set_appartment(3)

# renter.renters.append(r1)

# renter.save_renters()


top_window = tkinter.Tk()
top_window.title(texte.title)

renter_driver.gui_renter_frame(top_window)

top_window.mainloop()