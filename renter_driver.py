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
        renter.renters.append(renter.Renter(texte.anrede,texte.name))
        renters_index = len(renter.renters) - 1
        actual = renter.renters[renters_index]
        fill_renter_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global renters_index
        actual = renter.renters[renters_index]
        actual.anrede = anred_var.get()
        actual.name = name_var.get()
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global renters_index
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
        """Lädt Abjekte aus Datei"""
        global renters_index
        renters_index = 0
        renter.load_renters()
        if len(renter.renters) == 0:
            button_new_action()
        else:
            actual = renter.renters[renters_index]
            fill_renter_data(actual)
    
    def button_save_file_action():
        """Schreibt alle Mieter-Objekte in Datei"""
        renter.save_renters()
    
    def fill_renter_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        anred_var.set(actual.anrede)   
        name_var.set(actual.name)
    
        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        renter_frame = tkinter.Tk()
        renter_frame.title("Mieterdaten")
    else:
        renter_frame = tkinter.Frame(parent)
        renter_frame.grid(row=1, column=2)
    
    data_frame = tkinter.Frame(renter_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
    data_frame.grid(row=1, column=1)
    
    #Datendisplay/edit
    anred_label = tkinter.Label(data_frame, text=texte.anrede)
    anred_var = tkinter.StringVar(data_frame)
    anred_data = tkinter.Entry(data_frame,textvariable=anred_var)
    
    anred_label.grid(row=1, column=1, sticky=tkinter.W)
    anred_data.grid(row=1, column=2, sticky=tkinter.W)
    
    name_label = tkinter.Label(data_frame, text=texte.name)
    name_var = tkinter.StringVar(data_frame)
    name_data = tkinter.Entry(data_frame,textvariable=name_var)
    
    name_label.grid(row=2, column=1, sticky=tkinter.W)
    name_data.grid(row=2, column=2, sticky=tkinter.W)
    
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
    
    
    renter_frame.mainloop()

##############################################################################
############################## Skript starts here ############################
##############################################################################
if __name__ == "__main__":
    gui_renter_frame()