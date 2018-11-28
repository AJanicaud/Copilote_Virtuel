#Importation
import sys
sys.path.insert(0,'../Ester/Useful_Functions')
import Distance
import math
from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox


#Two functions that we need :
#Time that computes the time needed in order to go from airport a to airport b
def Time(h0,m0,am0):
    v = 150.
    #v = cruise_speed #vitesse de croisière en km/h
    d = Distance.distance([1,1],[1,1]) #distance entre les aéroports en km
    t = (d/v)*3600
    ds = t%60
    t = t//60
    dm = t%60
    dh = t//60
    h = h0 + dh
    m = m0 + dm
    if (m>60):
        h = h + 1
        m = m - 60
    if (h>11):
        h = h-12
        if (am0 == 'am'):
            am = 'pm'
        else:
            am = 'am'
    else:
        am = am0
    return [h0,m0,am0,h,m,am,d]

#Fuel that computes the fuel needed in order to go from airport a to airport b
def Fuel(h0,m0,am0):
    f_h = 35.
    [h0,m0,am0,h,m,am,dis] = Time(h0,m0,am0)
    f = f_h*h + (m+1)*(f_h/60)
    f = math.floor(f)+1
    return (f)


class Donnees:
    
    def __init__(self,a,b,c,d,h0,m0,am0,h,m,am,f,dis):
        Donnees.distance = dis
        Donnees.aircraft = a
        Donnees.passengers = b
        Donnees.departure_airport = c
        Donnees.arrival_airport = d
        Donnees.departure_hour = h0
        Donnees.departure_minute = m0
        Donnees.departure_ampm = am0
        Donnees.arrival_hour = h
        Donnees.arrival_minute = m
        Donnees.arrival_ampm = am
        Donnees.fuel_needed = f
        
    
    def modify_distance(self,d):
        self.distance = d
        return
        
    def get_distance(self):
        return self.distance
    
    def get_aircraft(self):
        return self.aircraft
    
    def get_passengers(self):
        return self.passengers
        
    def get_departure_airport(self):
        return self.departure_airport
    
    def get_arrival_airport(self):
        return self.arrival_airport
    
    def get_departure_hour(self):
        return self.departure_hour
        
    def get_departure_minute(self):
        return self.departure_minute
    
    def get_departure_ampm(self):
        return self.departure_ampm
    
    def get_arrival_hour(self):
        return self.arrival_hour
        
    def get_arrival_minute(self):
        return self.arrival_minute
    
    def get_arrival_ampm(self):
        return self.arrival_ampm
        
    def get_fuel_needed(self):
        return self.fuel_needed