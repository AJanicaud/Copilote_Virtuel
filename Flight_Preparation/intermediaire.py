from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox
import Classe
import math


def launch(Data):
    #Opening of the second interface
    Mission_Parameters_2 = Tk()
    Mission_Parameters_2.title('Plan de vol')
    Mission_Parameters_2.geometry("750x400")
    
    #Font allows to choose the police, the size and the type of our     text. We set two types that we will use
    font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
    font_aircraft = tkFont.Font(family='Helvetica', size=14)
    
    #We set the title of this interface
    Title1 = Label(Mission_Parameters_2, text='Plan de vol', pady=3, height=2, font=font1, fg='red')
    Title1.pack()
    
    #This one concerns time of arrival
    frame_arrival = LabelFrame(Mission_Parameters_2, height=75, text="Informations concernant le vol")
    frame_arrival.grid_propagate(0)
    frame_arrival.pack(fill="both", expand="no", padx=125)
    
    #This one concerns the position of the map frame
    frame_map = LabelFrame(Mission_Parameters_2, height=200, text="Carte")
    frame_map.grid_propagate(0)
    frame_map.pack(fill="both", expand="no", padx=75)
    
    Arrival_Time = Label(frame_arrival, text="Heure prévue d'arrivée", font=font_aircraft).place(x=30, y=5)
    
    string_1 = str(math.floor(Classe.Donnees.get_arrival_hour(Data)))+ ' ' + 'H' +' '+ str(math.floor(Classe.Donnees.get_arrival_minute(Data))) + ' ' + Classe.Donnees.get_arrival_ampm(Data)
    Hour_Arrival_Time = Label(frame_arrival, text=string_1, font=font_aircraft, fg='blue').place(x=55, y=30)

    Fuel_Needed = Label(frame_arrival, text="Fuel nécessaire", font=font_aircraft).place(x=350, y=5)
    string_2 = str(math.floor(Classe.Donnees.get_fuel_needed(Data))) + ' ' + 'L'
    Prediction_Fuel_Needed = Label(frame_arrival, text=string_2, font=font_aircraft, fg='blue').place(x=385, y=30)
    
    Mission_Parameters_2.mainloop()
