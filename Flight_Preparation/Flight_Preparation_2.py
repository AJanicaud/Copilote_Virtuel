# ________________________________________________________________________________
#                     COPILOTE VIRTUEL
#                       Static model
# ________________________________________________________________________________
# 
# Second interface: the purpose is to present to the user the main information about the flight (distance to fullfil, fuel needed, time of arrival)

#Importations
from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox

import Classe
import math


def callback1():
    Mission_Parameters_2.destroy()

def callback2():
    Mission_Parameters_2.destroy()

#Function that implements the second interface
#Entering parameter : Data (class that contains all the general information concerning the flight)
def launch(Flight_Parameters_Data):
    #Opening of the second interface
    Mission_Parameters_2 = Tk()
    Mission_Parameters_2.title('Plan de vol')
    Mission_Parameters_2.geometry("750x400")
    
    #Font allows to choose the police, the size and the type of our text. We set two types that we will use
    font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
    font_aircraft = tkFont.Font(family='Helvetica', size=14)
    
    #We set the title of this interface
    Title1 = Label(Mission_Parameters_2, text='Plan de vol', pady=3, height=2, font=font1, fg='red')
    Title1.pack()
    
    #==============================================================================
    #This one concerns time of arrival
    frame_arrival = LabelFrame(Mission_Parameters_2, height=75, text="Informations concernant le vol")
    frame_arrival.grid_propagate(0)
    frame_arrival.pack(fill="both", expand="no", padx=125)
    
    #This one concerns the position of the map frame
    frame_map = LabelFrame(Mission_Parameters_2, height=200, text="Carte")
    frame_map.grid_propagate(0)
    frame_map.pack(fill="both", expand="no", padx=75)
    #==============================================================================
    
    #We set the label concerning the arrival time
    Arrival_Time = Label(frame_arrival, text="Heure prévue d'arrivée", font=font_aircraft).place(x=30, y=5)
    #We define a string containing the predicted time of arrival (ex: 1h10pm)
    string_1 = str(math.floor(Classe.Flight_Parameters_Class.get_arrival_hour(Flight_Parameters_Data)))+ ' ' + 'H' +' '+ str(math.floor(Classe.Flight_Parameters_Class.get_arrival_minute(Flight_Parameters_Data))) + ' ' + Classe.Flight_Parameters_Class.get_arrival_ampm(Flight_Parameters_Data)
    #We set the label containing the previous string defined
    Hour_Arrival_Time = Label(frame_arrival, text=string_1, font=font_aircraft, fg='blue').place(x=55, y=30)
    
    #We set the label concerning the distance to achieve
    Distance_1 = Label(frame_arrival, text="Distance à parcourir", font=font_aircraft).place(x=200, y=5)
    #We define a string containing the distance to achieve (ex: 100km)
    string_2 = str(math.floor(Classe.Flight_Parameters_Class.get_distance(Flight_Parameters_Data))) + ' ' + 'km'
    #We set the label containing the previous string defined
    Prediction_Distance = Label(frame_arrival, text=string_2, font=font_aircraft, fg='blue').place(x=238, y=30)

    #We set the label concerning the fuel needed
    Fuel_Needed = Label(frame_arrival, text="Fuel nécessaire", font=font_aircraft).place(x=350, y=5)
    #We define a string containing the fuel needed (ex: 10L)
    string_3 = str(math.floor(Classe.Flight_Parameters_Class.get_fuel_needed(Flight_Parameters_Data))) + ' ' + 'L'
    #We set the label containing the previous string defined
    Prediction_Fuel_Needed = Label(frame_arrival, text=string_3, font=font_aircraft, fg='blue').place(x=385, y=30)
    #==============================================================================
    
    Departure_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport de départ', fg='green', command=callback1).place(x=150, y=373)
    Trajectory_Map = Button(Mission_Parameters_2, text = 'Trajectoire', fg='green', command=callback1).place(x=350, y=373)
    Arrival_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport d''arrivée', fg='green', command=callback2).place(x=500, y=373)
    
    Mission_Parameters_2.mainloop()
