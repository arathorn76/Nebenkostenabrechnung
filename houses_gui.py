import tkinter
import house
import config.nebenkosten_text_de as texte


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
        fill_renter_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global houses_index
        if houses_index > 0:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_renter_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global houses_index
        house.houses.append(house.House(texte.name))
        houses_index = len(house.houses) - 1
        actual = house.houses[houses_index]
        fill_renter_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global houses_index
        actual = house.houses[houses_index]
        actual.name = name_var.get()
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global houses_index
        house.houses.pop(houses_index)
        if len(house.houses) == 0:
            button_new_action()
        elif houses_index == 0:
            pass
        else:
            houses_index -= 1
        actual = house.houses[houses_index]
        fill_renter_data(actual)
    
    
    
    def button_load_file_action():
        """Lädt Abjekte aus Datei"""
        global houses_index
        houses_index = 0
        house.load_houses()
        if len(house.houses) == 0:
            button_new_action()
        else:
            actual = house.houses[houses_index]
            fill_renter_data(actual)
    
    def button_save_file_action():
        """Schreibt alle Mieter-Objekte in Datei"""
        #renter.save_renters()
        house.save_houses()
        pass
    
    def fill_renter_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        name_var.set(actual.name)
    
        
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
    
    name_label = tkinter.Label(data_frame, text=texte.name)
    name_var = tkinter.StringVar(data_frame)
    name_data = tkinter.Entry(data_frame,textvariable=name_var)
    
    name_label.grid(row=2, column=1, sticky=tkinter.W)
    name_data.grid(row=2, column=2, sticky=tkinter.W)
    
    #Fenster mit Daten füttern
    if len(house.houses) == 0:
        button_load_file_action()
    houses_index = 0
    actual = house.houses[houses_index]
    fill_renter_data(actual)
    
    #Interaktion
    controls_frame = tkinter.Frame(houses_frame)
    button_prev = tkinter.Button(controls_frame, text=texte.button_prev, command=button_prev_action)
    button_next = tkinter.Button(controls_frame, text=texte.button_next, command=button_next_action)
    button_new = tkinter.Button(controls_frame, text= texte.button_new, command=button_new_action)
    button_change = tkinter.Button(controls_frame, text=texte.button_change, command=button_change_action)
    button_delete = tkinter.Button(controls_frame, text=texte.button_delete, command=button_delete_action)
    button_load_file = tkinter.Button(controls_frame, text=texte.button_load_file, command=button_load_file_action)
    button_save_file = tkinter.Button(controls_frame, text=texte.button_save_file, command=button_save_file_action)
    
    controls_frame.grid(row=2, column=1)
    button_prev.grid(row=1, column=1)
    button_next.grid(row=1, column=2)
    button_new.grid(row=1, column=3)
    button_change.grid(row=1, column=4)
    button_delete.grid(row=1, column=5)
    button_load_file.grid(row=2, column=1)
    button_save_file.grid(row=2, column=3)
    
    
    houses_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
houses_index = 0

if __name__ == "__main__":
    gui_houses_frame()