#Importation
import sys
sys.path.insert(0,'../Useful_Functions')
import Distance
import math
from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox

#Two functions that we need :
#Time that computes the time needed in order to go from airport a to airport b
def Time(h0,m0,am0):
    v = 225.
    #v = cruise_speed #vitesse de croisière en km/h
    d = Distance.distance([1,1],[1,1]) #distance entre les aéroports en km
    print(d)
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
    return [h0,m0,am0,h,m,am]

#Fuel that computes the fuel needed in order to go from airport a to airport b
def Fuel(h0,m0,am0):
    f_h = 35.
    [h0,m0,am0,h,m,am] = Time(h0,m0,am0)
    f = f_h*h + (m+1)*(f_h/60)
    f = math.floor(f)+1
    return (f)

    
    