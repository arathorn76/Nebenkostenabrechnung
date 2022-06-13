"""Modul zur Verwaltung von Adressen"""

from re import A
import sqlite3
import config.settings as settings
import db
from renter_gui import gui_renter_frame
import tkinter
import config.nebenkosten_text_de as texte


class Adresse:

    def __init__(self, id = None, strasse = '', hausnummer = '', strasse2 = '', hausnummer2 = '', plz = '', ort = '', land = 'Deutschland'):
            self.id = id
            self.strasse = strasse
            self.hausnummer = hausnummer
            self.strasse2 = strasse2
            self.hausnummer2 = hausnummer2
            self.plz = plz
            self.ort = ort
            self.land = land

    def get_adress_lines(self):
        line1 = ' '.join([self.strasse, self.hausnummer])
        if self.strasse2 == '' and self.hausnummer2 == '':
            line2 = ''
        elif self.strasse2 == '':
            line2 = self.hausnummer2
        elif self.hausnummer2 == '':
            line2 = self.strasse2
        else:
            line2 = ' '.join([self.strasse2, self.hausnummer2])
        line3 = ' '.join([self.plz, self.ort])
        line4 = self.land
        return (line1, line2, line3, line4)

    def db_insert(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "insert into adressen values(?, ?, ?, ?, ?, ?, ?, ?)"
        zeiger.execute(sql_string, (
            None,
            self.strasse,
            self.hausnummer,
            self.strasse2,
            self.hausnummer2,
            self.plz,
            self.ort,
            self.land
        ))
        verbindung.commit()
        self.id = zeiger.lastrowid
        verbindung.close()

    def db_update(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = """update adressen set
            strasse=?, hausnummer=?, 
            strasse2=?, hausnummer2=?, 
            plz=?, ort=?, 
            land=? where id=?"""
        zeiger.execute(sql_string, (
            self.strasse,
            self.hausnummer,
            self.strasse2,
            self.hausnummer2,
            self.plz,
            self.ort,
            self.land,
            self.id
        ))
        verbindung.commit()
        verbindung.close()

    def db_delete(self):
        verbindung = sqlite3.connect(settings.dbfile)
        zeiger = verbindung.cursor()
        sql_string = "delete from adressen where id = ?"
        zeiger.execute(sql_string, (self.id,))
        verbindung.commit()
        verbindung.close()

class MessageBox(object):

    def __init__(self, msg, b1, b2, frame, entry):

        root = self.root = tkinter.Tk()
        root.title('Message')
        self.msg = str(msg)
        adr = list()
        for a in adressen:
            adr.append(a.get_adress_lines())

        cnames=tkinter.StringVar(value=adr)

        # remove the outer frame if frame=False
        if not frame: root.overrideredirect(True)
        # default values for the buttons to return
        self.b1_return = True
        self.b2_return = False
        # if b1 or b2 is a tuple unpack into the button text & return value
        if isinstance(b1, tuple): b1, self.b1_return = b1
        if isinstance(b2, tuple): b2, self.b2_return = b2
        # main frame
        frm_1 = tkinter.Frame(root)
        frm_1.pack(ipadx=2, ipady=2)
        # the message
        message = tkinter.Label(frm_1, text=self.msg)
        message.pack(padx=8, pady=8)
        # create listbox
        lbox = tkinter.Listbox(frm_1, listvariable=cnames, height=8)
        lbox.pack(padx=8, pady=8)
        # button frame
        frm_2 = tkinter.Frame(frm_1)
        frm_2.pack(padx=4, pady=4)
        # buttons
        btn_1 = tkinter.Button(frm_2, width=8, text=b1)
        btn_1['command'] = self.b1_action
        btn_1.pack(side='left')
        if not entry: btn_1.focus_set()
        btn_2 = tkinter.Button(frm_2, width=8, text=b2)
        btn_2['command'] = self.b2_action
        btn_2.pack(side='left')
        # the enter button will trigger the focused button's action
        btn_1.bind('<KeyPress-Return>', func=self.b1_action)
        btn_2.bind('<KeyPress-Return>', func=self.b2_action)
        # roughly center the box on screen
        # for accuracy see: https://stackoverflow.com/a/10018670/1217270
        root.update_idletasks()
        xp = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        yp = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        geom = (root.winfo_width(), root.winfo_height(), xp, yp)
        root.geometry('{0}x{1}+{2}+{3}'.format(*geom))
        # call self.close_mod when the close button is pressed
        root.protocol("WM_DELETE_WINDOW", self.close_mod)
        # a trick to activate the window (on windows 7)
        root.deiconify()
        # if t is specified: call time_out after t seconds

    def b1_action(self, event=None):
        try: x = self.entry.get()
        except AttributeError:
            self.returning = self.b1_return
            self.root.quit()
        else:
            if x:
                self.returning = x
                self.root.quit()

    def b2_action(self, event=None):
        self.returning = self.b2_return
        self.root.quit()

    # remove this function and the call to protocol
    # then the close button will act normally
    def close_mod(self):
        pass


def gui_adress_selector(msg, b1='OK', b2='Cancel', frame=True, entry=False):
    """Create an instance of MessageBox, and get data back from the user.
    msg = string to be displayed
    b1 = text for left button, or a tuple (<text for button>, <to return on press>)
    b2 = text for right button, or a tuple (<text for button>, <to return on press>)
    frame = include a standard outerframe: True or False
    entry = include an entry widget that will have its contents returned: True or False
    """
    msgbox = MessageBox(msg, b1, b2, frame, entry)
    msgbox.root.mainloop()
    # the function pauses here until the mainloop is quit
    msgbox.root.destroy()
    return msgbox.returning

# Persistenz
def load_adressen():
    global adressen
    adressen.clear()
    for a in db.read_adressen():
        adressen.append(Adresse(*a))

def get_adress_list():
    adress_list = list()
    for a in adressen:
        adress_list.append((a.id, a.get_adress_lines()))
    return adress_list

def get_adress_by_id(query_id):
    for a in get_adress_list():
        if a[0] == query_id:
            return a

# GUI
def gui_adress_frame(parent = None):
    """Aufbau des Adressen-Fensters"""
    ##########################################################################
    ############################ nested Functions## ##########################
    ##########################################################################

    def button_next_action():
        """Zeigt nächsten Datensatz an"""
        global adress_index
        if adress_index < len(adressen) - 1:
            adress_index += 1
        actual = adressen[adress_index]
        fill_adress_data(actual)
    
    def button_prev_action():
        """Zeigt vorherigen Datensatz an"""
        global adress_index
        if adress_index > 0:
            adress_index -= 1
        actual = adressen[adress_index]
        fill_adress_data(actual)
     
    
    def button_new_action():
        """Erzeugt neuen Datensatz mit Pseudowerten."""
        global adress_index
        adressen.append(Adresse())
        adress_index = len(adressen) - 1
        actual = adressen[adress_index]
        actual.db_insert()
        fill_adress_data(actual)
    
    def button_change_action():
        """Übernimmt geänderte Werte in Objekt"""
        global adress_index
        actual = adressen[adress_index]
        actual.strasse = strasse_var.get()
        actual.hausnummer = hausnummer_var.get()
        actual.strasse2 = strasse2_var.get()
        actual.hausnummer2 = hausnummer2_var.get()
        actual.plz = plz_var.get()
        actual.ort = ort_var.get()
        actual.land = land_var.get()
        actual.db_update()
    
    def button_delete_action():
        """Löscht aktuelles Objekt"""
        global adress_index
        adressen[adress_index].db_delete()
        adressen.pop(adress_index)
        if len(adressen) == 0:
            button_new_action()
        elif adress_index == 0:
            pass
        else:
            adress_index -= 1
        actual = adressen[adress_index]
        fill_adress_data(actual)
    
    
    def button_load_file_action():
        """Lädt Objekte aus DB"""
        global adress_index
        adress_index = 0
        load_adressen()
        if len(adressen) == 0:
            button_new_action()
        else:
            actual = adressen[adress_index]
            fill_adress_data(actual)
    

    def fill_adress_data(actual):
        """Übernimmt Werte des aktuellen Mieter-Objekts in Anzeige"""
        id_var.set(actual.id)
        strasse_var.set(actual.strasse)   
        hausnummer_var.set(actual.hausnummer)
        strasse2_var.set(actual.strasse2)
        hausnummer2_var.set(actual.hausnummer2)   
        plz_var.set(actual.plz)
        ort_var.set(actual.ort)
        land_var.set(actual.land)

        
    ##########################################################################
    ############################ Coding starts here ##########################
    ##########################################################################
    #Fenster aufbauen
    if parent == None:
        adress_frame = tkinter.Tk()
        adress_frame.title("Adressdaten")
    else:
        adress_frame = tkinter.Frame(parent)
        adress_frame.grid(row=1, column=1)
    
    data_frame = tkinter.Frame(adress_frame, relief=tkinter.GROOVE, borderwidth=5, padx=5, pady=5)
    data_frame.grid(row=1, column=1, sticky=tkinter.NW)
    
    #Datendisplay/edit
    id_label = tkinter.Label(data_frame, text=texte.id)
    id_var = tkinter.StringVar(data_frame)
    id_data = tkinter.Entry(data_frame, textvariable=id_var,state=tkinter.DISABLED)
    id_label.grid(row=0, column=1, sticky=tkinter.W)
    id_data.grid(row=0, column=2, sticky=tkinter.W)

    strasse_label = tkinter.Label(data_frame, text=texte.strasse)
    strasse_var = tkinter.StringVar(data_frame)
    strasse_data = tkinter.Entry(data_frame,textvariable=strasse_var)
    strasse_label.grid(row=1, column=1, sticky=tkinter.W)
    strasse_data.grid(row=1, column=2, sticky=tkinter.W)
    
    hausnummer_label = tkinter.Label(data_frame, text=texte.hausnummer)
    hausnummer_var = tkinter.StringVar(data_frame)
    hausnummer_data = tkinter.Entry(data_frame,textvariable=hausnummer_var)
    hausnummer_label.grid(row=1, column=3, sticky=tkinter.W)
    hausnummer_data.grid(row=1, column=4, sticky=tkinter.W)

    strasse2_label = tkinter.Label(data_frame, text=texte.strasse+" 2")
    strasse2_var = tkinter.StringVar(data_frame)
    strasse2_data = tkinter.Entry(data_frame,textvariable=strasse2_var)
    strasse2_label.grid(row=2, column=1, sticky=tkinter.W)
    strasse2_data.grid(row=2, column=2, sticky=tkinter.W)

    hausnummer2_label = tkinter.Label(data_frame, text=texte.hausnummer+" 2")
    hausnummer2_var = tkinter.StringVar(data_frame)
    hausnummer2_data = tkinter.Entry(data_frame,textvariable=hausnummer2_var)
    hausnummer2_label.grid(row=2, column=3, sticky=tkinter.W)
    hausnummer2_data.grid(row=2, column=4, sticky=tkinter.W)
    
    plz_label = tkinter.Label(data_frame, text=texte.plz)
    plz_var = tkinter.StringVar(data_frame)
    plz_data = tkinter.Entry(data_frame,textvariable=plz_var)
    plz_label.grid(row=3, column=1, sticky=tkinter.W)
    plz_data.grid(row=3, column=2, sticky=tkinter.W)

    ort_label = tkinter.Label(data_frame, text=texte.ort)
    ort_var = tkinter.StringVar(data_frame)
    ort_data = tkinter.Entry(data_frame,textvariable=ort_var)
    ort_label.grid(row=3, column=3, sticky=tkinter.W)
    ort_data.grid(row=3, column=4, sticky=tkinter.W)

    land_label = tkinter.Label(data_frame, text=texte.land)
    land_var = tkinter.StringVar(data_frame)
    land_data = tkinter.Entry(data_frame,textvariable=land_var)
    land_label.grid(row=4, column=1, sticky=tkinter.W)
    land_data.grid(row=4, column=2, sticky=tkinter.W)

    #Fenster mit Daten füttern
    if len(adressen) == 0:
        button_load_file_action()
    adress_index = 0
    actual = adressen[adress_index]
    fill_adress_data(actual)
    
    #Interaktion
    controls_frame = tkinter.Frame(adress_frame)
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

    
    adress_frame.mainloop()
        

# Initialisierung des Moduls
adressen = list()
load_adressen()
adress_index = 0

if __name__ == "__main__":
    gui_adress_frame()