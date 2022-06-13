import tkinter
import house
import config.nebenkosten_text_de as texte
import adresses
from nebenkosten import button_adresses_action


##############################################################################
############################ Function definitions ############################
##############################################################################        
def gui_houses_frame(parent):
    """Aufbau des Häuser-Fensters"""
    ##########################################################################
    ############################ nested Functions## ##########################
    ##########################################################################

    def button_next_action():
        """Zeigt nächsten Datensatz an"""
        global houses_index
        if houses_index < len(house.houses) - 1:
            houses_index += 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global houses_index
        if houses_index > 0:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global houses_index
        house.houses.append(house.House())
        houses_index = len(house.houses) - 1
        actual = house.houses[houses_index]
        actual.db_insert()
        fill_house_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global houses_index
        actual = house.houses[houses_index]
        actual.name = name_var.get()
        actual.size = size_var.get()
        actual.db_update()
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global houses_index
        house.houses[houses_index].db_delete()
        house.houses.pop(houses_index)
        if len(house.houses) == 0:
            button_new_action()
        elif houses_index == 0:
            pass
        else:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_house_data(actual)
    
    def button_adress_action():
        choosen_adress = [None]
        adresses.gui_adress_selector(choosen_adress)
        print(choosen_adress[0])
    
    def button_load_file_action():
        """Lädt Abjekte aus Datei"""
        global houses_index
        houses_index = 0
        house.load_houses()
        if len(house.houses) == 0:
            button_new_action()
        else:
            actual = house.houses[houses_index]
            fill_house_data(actual)
    

    
    def fill_house_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        id_var.set(actual.id)
        name_var.set(actual.name)
        size_var.set(actual.size)
        adress = adresses.get_adress_by_id(actual.adress_id)
        if adress != None:
            adress_var.set(','.join(adress[1]))
        else:
            adress_var.set('')
    
        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        houses_frame = tkinter.Tk()
        houses_frame.title("Hausdaten")
    else:
        houses_frame = tkinter.Frame(parent)
        houses_frame.grid(row=1, column=1)
    
    data_frame = tkinter.Frame(houses_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
    data_frame.grid(row=1, column=1, sticky=tkinter.NW)
    
    #Datendisplay/edit
    id_label = tkinter.Label(data_frame, text=texte.id)
    id_var = tkinter.StringVar(data_frame)
    id_data = tkinter.Entry(data_frame, textvariable=id_var,state=tkinter.DISABLED)
    id_label.grid(row=0, column=1, sticky=tkinter.W)
    id_data.grid(row=0, column=2, sticky=tkinter.W)

    name_label = tkinter.Label(data_frame, text=texte.name)
    name_var = tkinter.StringVar(data_frame)
    name_data = tkinter.Entry(data_frame,textvariable=name_var)
    name_label.grid(row=1, column=1, sticky=tkinter.W)
    name_data.grid(row=1, column=2, sticky=tkinter.W)
    
    size_label = tkinter.Label(data_frame, text=texte.size)
    size_var = tkinter.StringVar(data_frame)
    size_data = tkinter.Entry(data_frame,textvariable=size_var)
    size_label.grid(row=2, column=1, sticky=tkinter.W)
    size_data.grid(row=2, column=2, sticky=tkinter.W)

    adress_label = tkinter.Label(data_frame, text=texte.adress)
    adress_var = tkinter.StringVar(data_frame)
    adress_data = tkinter.Entry(data_frame, textvariable=adress_var,state=tkinter.DISABLED)
    adress_label.grid(row=3, column=1, sticky=tkinter.W)
    adress_data.grid(row=3, column=2, columnspan=3, sticky=tkinter.W+tkinter.E)

    adress_button = tkinter.Button(data_frame, text=texte.adress_button, command=button_adress_action)
    adress_button.grid(row=4, column=3, sticky=tkinter.W)

    
    #Fenster mit Daten füttern
    if len(house.houses) == 0:
        button_load_file_action()
    houses_index = 0
    actual = house.houses[houses_index]
    fill_house_data(actual)
    
    #Interaktion
    controls_frame = tkinter.Frame(houses_frame)
    button_prev = tkinter.Button(controls_frame, text=texte.button_prev, command=button_prev_action)
    button_next = tkinter.Button(controls_frame, text=texte.button_next, command=button_next_action)
    button_new = tkinter.Button(controls_frame, text= texte.button_new, command=button_new_action)
    button_change = tkinter.Button(controls_frame, text=texte.button_change, command=button_change_action)
    button_delete = tkinter.Button(controls_frame, text=texte.button_delete, command=button_delete_action)

    
    controls_frame.grid(row=2, column=1)
    button_prev.grid(row=1, column=1)
    button_next.grid(row=1, column=2)
    button_new.grid(row=1, column=3)
    button_change.grid(row=1, column=4)
    button_delete.grid(row=1, column=5)
    
    
    houses_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
houses_index = 0

if __name__ == "__main__":
    gui_houses_frame()