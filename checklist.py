#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:03:38 2018

@author: alixjanicaud
"""

# COPILOTE VIRTUEL
# Static model
# ________________________________________________________________________________
#
# First interface: the purpose is to set all the parameters of the mission (type of the aircraft, number of passsengers, airport of departure, airport of arrival, departure time)


#Importation
from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox

def callback():
    a = aircraft.get()
    b = departure.get()
    c = arrival.get()
    d = hour.get()
    e = min.get()
    f = ampm.get()

#Opening of the first interface
Mission_Parameters = Tk()
Mission_Parameters.title('Copilote virtuel')
Mission_Parameters.geometry("750x400")

#Font allows to choose the police, the size and the type of our text. We set two types that we will use
font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
font_aircraft = tkFont.Font(family='Helvetica', size=14)

#We set the title of this interface
Title1 = Label(Mission_Parameters, text='Paramétrage de la mission', pady=3, height=2, font=font1, fg='red')
Title1.pack()

#===============================================================================
#We set all the names and the position of all the Labelframe (small frame)

#This one concerns Aircraft parameters
frame_aircraft = LabelFrame(Mission_Parameters, height=100, text="Paramètres avion")
frame_aircraft.grid_propagate(0)
frame_aircraft.pack(fill="both", expand="no", padx=100)

#This one concerns Airport parameters
frame_airport = LabelFrame(Mission_Parameters, height=100, text="Paramètres aéroports")
frame_airport.grid_propagate(0)
frame_airport.pack(fill="both", expand="no", padx=100)

#This one concerns Flight parameters
frame_flight = LabelFrame(Mission_Parameters, height=60, text="Paramètres du vol")
frame_flight.grid_propagate(0)
frame_flight.pack(fill="both", expand="no", padx=100)
#===============================================================================

#Inside the Aircraft Parameters

Aircraft_model = Label(frame_aircraft, text="Modèle de l'avion", font=font_aircraft).place(x=30, y=5)
#We create the list of all the aircrafts we can use
Aircraft_List = ["DR400", "Rafale", "A380"]
#We create the list-down box linked to the aircrafts
aircraft = StringVar()
Combo_Aircraft = Combobox(frame_aircraft, values=Aircraft_List, textvariable=aircraft).place(x=190, y=5)

Crew = Label(frame_aircraft, text="Nombre de passagers", font=font_aircraft).place(x=20, y=40)
#Spinbox that allows us to specify the number of passengers for the flight
s = Spinbox(frame_aircraft, from_=1, to=10, font=font_aircraft).place(x=190, y=37)
#===============================================================================

#Inside the Airport Parameters

Airport_departure = Label(frame_airport, text="Aéroport de départ", font=font_aircraft).place(x=30, y=5)
Airport_arrival = Label(frame_airport, text="Aéroport d'arrivée", font=font_aircraft).place(x=30, y=40)
#We create the list of all the airports we can use
Airport_List = ["Lasbordes", "Blagnac", "CDG", "Orly"]
#We create two list-down boxes (une for the departure and one for the arrival) linked to the airports
departure = StringVar()
Combo_Departure = Combobox(frame_airport, values=Airport_List, textvariable=departure).place(x=190, y=5)
arrival = StringVar()
Combo_Arrival = Combobox(frame_airport, values=Airport_List, textvariable=arrival).place(x=190, y=40)
#===============================================================================

#Inside the Flight Parameters

Flight_time = Label(frame_flight, text="Heure de départ", font=font_aircraft).place(x=30, y=5)
h = Label(frame_flight, text="h", font=font_aircraft).place(x=240, y=5)
min = Label(frame_flight, text="min", font=font_aircraft).place(x=310, y=5)
#Spinboxes that allow us to specify the time of departure
hour = StringVar()
Combo_Hour = Spinbox(frame_flight, from_=0, to=12, textvariable=hour, width=3).place(x=190, y=3)
min = StringVar()
Combo_Minute = Spinbox(frame_flight, from_=0, to=59, textvariable=min, width=3).place(x=260, y=3)
#We create the list-down box in order to specify am or pm time
Time_List = ["am","pm"]
ampm = StringVar()
Time = Combobox(frame_flight, values=Time_List, textvariable=ampm, width=3).place(x=340, y=3)
#===============================================================================



Validate = Button(Mission_Parameters, text = 'Valider', fg='green', command=callback).place(x=350, y=363)



Mission_Parameters.mainloop()