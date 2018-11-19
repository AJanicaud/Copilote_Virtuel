import Distance
import math
#Calculation of the time between two airports and the fuel needed

def Time():
    v = 225.
    #d = 550
    #v = cruise_speed #vitesse de croisière en km/h
    d = distance(pos_dep,pos_arr) #distance entre les aéroports en km
    t = (d/v)*3600
    s = t%60
    t = t//60
    m = t%60
    h = t//60
    return [h,m,s]

def Fuel():
    f_h = 35.
    [h,m,s] = Time()
    f = f_h*h + m*(f_h/60) + s*(f_h/3600)
    f = math.floor(f)+1
    return (f)
    
Fuel()