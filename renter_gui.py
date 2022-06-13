""" Testrahmen für Modul renter
   
Bei Verwendung als Modul muss ein tkinter.Tk oder tkinter.Frame 
mit Namen "renter_frame" als Parent zur Verfügung gestellt werden."""
    
import tkinter
import renter
import config.nebenkosten_text_de as texte

    
##############################################################################
############################ Function definitions ############################
##############################################################################
def gui_renter_frame(parent = None):
    """Aufbau des Mieter-Fensters"""
    ##########################################################################
    ############################ nested Functions## ##########################
    ##########################################################################

    def button_next_action():
        """Zeigt nächsten Datensatz an"""
        global renters_index
        if renters_index < len(renter.renters) - 1:
            renters_index += 1
        actual = renter.renters[renters_index]
        fill_renter_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global renters_index
        if renters_index > 0:
            renters_index -= 1
        actual = renter.renters[renters_index]
        fill_renter_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global renters_index
        renter.renters.append(renter.Renter())
        renters_index = len(renter.renters) - 1
        actual = renter.renters[renters_index]
        actual.db_insert()
        fill_renter_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global renters_index
        actual = renter.renters[renters_index]
        actual.anrede1 = anred1_var.get()
        actual.vorname1 = vorname1_var.get()
        actual.nachname1 = nachname1_var.get()
        actual.anrede2 = anred2_var.get()
        actual.vorname2 = vorname2_var.get()
        actual.nachname2 = nachname2_var.get()
        actual.anzahl_personen = anzahl_personen_var.get()
        actual.weitere_personen = weitere_personen_var.get()
        actual.db_update()
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global renters_index
        renter.renters[renters_index].db_delete()
        renter.renters.pop(renters_index)
        if len(renter.renters) == 0:
            button_new_action()
        elif renters_index == 0:
            pass
        else:
            renters_index -= 1
        actual = renter.renters[renters_index]
        fill_renter_data(actual)
    
    
    def button_load_file_action():
        """Lädt Objekte aus DB"""
        global renters_index
        renters_index = 0
        renter.load_renters()
        if len(renter.renters) == 0:
            button_new_action()
        else:
            actual = renter.renters[renters_index]
            fill_renter_data(actual)
    

    def fill_renter_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        id_var.set(actual.id)
        anred1_var.set(actual.anrede1)   
        vorname1_var.set(actual.vorname1)
        nachname1_var.set(actual.nachname1)
        anred2_var.set(actual.anrede2)   
        vorname2_var.set(actual.vorname2)
        nachname2_var.set(actual.nachname2)
        anzahl_personen_var.set(actual.anzahl_personen)
        weitere_personen_var.set(actual.weitere_personen)
        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        renter_frame = tkinter.Tk()
        renter_frame.title("Mieterdaten")
    else:
        renter_frame = tkinter.Frame(parent)
        renter_frame.grid(row=1, column=1)
    
    data_frame = tkinter.Frame(renter_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
    data_frame.grid(row=1, column=1, sticky=tkinter.NW)
    
    #Datendisplay/edit
    id_label = tkinter.Label(data_frame, text=texte.id)
    id_var = tkinter.StringVar(data_frame)
    id_data = tkinter.Entry(data_frame, textvariable=id_var,state=tkinter.DISABLED)
    id_label.grid(row=0, column=1, sticky=tkinter.W)
    id_data.grid(row=0, column=2, sticky=tkinter.W)
    
    anred1_label = tkinter.Label(data_frame, text=texte.anrede)
    anred1_var = tkinter.StringVar(data_frame)
    anred1_data = tkinter.Entry(data_frame,textvariable=anred1_var)
    anred1_label.grid(row=1, column=1, sticky=tkinter.W)
    anred1_data.grid(row=1, column=2, sticky=tkinter.W)
    
    vorname1_label = tkinter.Label(data_frame, text=texte.vorname)
    vorname1_var = tkinter.StringVar(data_frame)
    vorname1_data = tkinter.Entry(data_frame,textvariable=vorname1_var)
    vorname1_label.grid(row=2, column=1, sticky=tkinter.W)
    vorname1_data.grid(row=2, column=2, sticky=tkinter.W)

    nachname1_label = tkinter.Label(data_frame, text=texte.nachname)
    nachname1_var = tkinter.StringVar(data_frame)
    nachname1_data = tkinter.Entry(data_frame,textvariable=nachname1_var)
    nachname1_label.grid(row=2, column=3, sticky=tkinter.W)
    nachname1_data.grid(row=2, column=4, sticky=tkinter.W)

    anred2_label = tkinter.Label(data_frame, text=texte.anrede+" 2")
    anred2_var = tkinter.StringVar(data_frame)
    anred2_data = tkinter.Entry(data_frame,textvariable=anred2_var)
    anred2_label.grid(row=3, column=1, sticky=tkinter.W)
    anred2_data.grid(row=3, column=2, sticky=tkinter.W)
    
    vorname2_label = tkinter.Label(data_frame, text=texte.vorname+" 2")
    vorname2_var = tkinter.StringVar(data_frame)
    vorname2_data = tkinter.Entry(data_frame,textvariable=vorname2_var)
    vorname2_label.grid(row=4, column=1, sticky=tkinter.W)
    vorname2_data.grid(row=4, column=2, sticky=tkinter.W)

    nachname2_label = tkinter.Label(data_frame, text=texte.nachname+" 2")
    nachname2_var = tkinter.StringVar(data_frame)
    nachname2_data = tkinter.Entry(data_frame,textvariable=nachname2_var)
    nachname2_label.grid(row=4, column=3, sticky=tkinter.W)
    nachname2_data.grid(row=4, column=4, sticky=tkinter.W)

    anzahl_personen_label = tkinter.Label(data_frame, text=texte.anzahl_personen)
    anzahl_personen_var = tkinter.StringVar(data_frame)
    anzahl_personen_data = tkinter.Entry(data_frame,textvariable=anzahl_personen_var)
    anzahl_personen_label.grid(row=5, column=1, sticky=tkinter.W)
    anzahl_personen_data.grid(row=5, column=2, sticky=tkinter.W)

    weitere_personen_label = tkinter.Label(data_frame, text=texte.weitere_personen)
    weitere_personen_var = tkinter.StringVar(data_frame)
    weitere_personen_data = tkinter.Entry(data_frame,textvariable=weitere_personen_var)
    weitere_personen_label.grid(row=6, column=1, sticky=tkinter.W)
    weitere_personen_data.grid(row=6, column=2, columnspan=3, sticky=tkinter.W+tkinter.E)


    #Fenster mit Daten füttern
    if len(renter.renters) == 0:
        button_load_file_action()
    renters_index = 0
    actual = renter.renters[renters_index]
    fill_renter_data(actual)
    
    #Interaktion
    controls_frame = tkinter.Frame(renter_frame)
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

    
    renter_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
if __name__ == "__main__":
    gui_renter_frame()