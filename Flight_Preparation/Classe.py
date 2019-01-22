#Importation
#import sys
#sys.path.insert(0,'/Users/lancelotribot/documents/spider/Useful_Functions')
#import Distance

open('../Useful_Functions/Distance.py')
import Distance
import math
from tkinter import *
import xlrd
import xlwt
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox


#Two functions that we need :
#Time that computes the time needed in order to go from airport a to airport b
def Time(h0,m0,am0,Aircraft_Parameters_Data,Departure_Airport_Parameters_Data,Arrival_Airport_Parameters_Data):
    v = Aircraft_Parameters_Class.get_cruise_speed(Aircraft_Parameters_Data)
    latd = Departure_Airport_Parameters_Class.get_latitude(Departure_Airport_Parameters_Data)
    longd = Departure_Airport_Parameters_Class.get_longitude(Departure_Airport_Parameters_Data)
    lata = Arrival_Airport_Parameters_Class.get_latitude(Arrival_Airport_Parameters_Data)
    longa = Arrival_Airport_Parameters_Class.get_longitude(Arrival_Airport_Parameters_Data)
    pos_dep = [latd,longd]
    pos_arr = [lata,longa]
    d = Distance.distance(pos_dep,pos_arr) #distance entre les aéroports en km
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
        if (am0 == 'AM'):
            am = 'PM'
        else:
            am = 'AM'
    else:
        am = am0
    return [h0,m0,am0,h,m,am,d]

#Fuel that computes the fuel needed in order to go from airport a to airport b
def Fuel(h0,m0,am0,Aircraft_Parameters_Data,Departure_Airport_Parameters_Data,Arrival_Airport_Parameters_Data):
    f_h = 35.
    [h0,m0,am0,h,m,am,dis] = Time(h0,m0,am0,Aircraft_Parameters_Data,Departure_Airport_Parameters_Data,Arrival_Airport_Parameters_Data)
    f = f_h*h + (m+1)*(f_h/60)
    f = math.floor(f)+1
    return (f)


class Aircraft_Parameters_Class:
    
    def __init__(self,a):
        Aircraft_Parameters_Class.aircraft = a
        Aircraft_Parameters_Class.cruise_speed = 150.
        
    def get_aircraft(self):
        return self.aircraft
        
    def get_cruise_speed(self):
        return self.cruise_speed
        
class Departure_Airport_Parameters_Class:
    
    def __init__(self,airport):
        # Import the excel files containing the databases
        Airport_Lists = xlrd.open_workbook('../Databases/airfields_database.xlsx')             
        # Get the names of the tabs
        Airport_cl = Airport_Lists.sheet_names()
        #[MONTAUBAN,GAILLAC,LASBORDES]
        n = len(Airport_cl)
        j = 0
        for i in range (n):
            if (airport==Airport_cl[i]):
                j = i
                break
        current_cl = Airport_Lists.sheet_by_name(Airport_cl[j])  
        Departure_Airport_Parameters_Class.name = airport
        Departure_Airport_Parameters_Class.identification = current_cl.col_values(1)[1]
        Departure_Airport_Parameters_Class.codeOACI = current_cl.col_values(1)[2]
        Departure_Airport_Parameters_Class.exploitant = current_cl.col_values(1)[3]
        Departure_Airport_Parameters_Class.CAA = current_cl.col_values(1)[4]
        Departure_Airport_Parameters_Class.BRIA = current_cl.col_values(1)[5]
        Departure_Airport_Parameters_Class.CAP = current_cl.col_values(1)[6]
        Departure_Airport_Parameters_Class.VAR = current_cl.col_values(1)[7]
        Departure_Airport_Parameters_Class.altitude = current_cl.col_values(1)[8]
        
        latitude = int(current_cl.col_values(1)[9][0]+current_cl.col_values(1)[9][1]) + int(current_cl.col_values(1)[9][3]+current_cl.col_values(1)[9][4])/60.+int(current_cl.col_values(1)[9][6]+current_cl.col_values(1)[9][7])/3600.
        Departure_Airport_Parameters_Class.latitude = latitude
        longitude = int(current_cl.col_values(1)[10][0]+current_cl.col_values(1)[10][1]+current_cl.col_values(1)[10][2]) + int(current_cl.col_values(1)[10][4]+current_cl.col_values(1)[10][5])/60. + int(current_cl.col_values(1)[10][7]+current_cl.col_values(1)[10][8])/3600.
        Departure_Airport_Parameters_Class.longitude = longitude
        
        Departure_Airport_Parameters_Class.AA = current_cl.col_values(1)[13]
        Departure_Airport_Parameters_Class.direction = current_cl.col_values(1)[14]
        Departure_Airport_Parameters_Class.tel = current_cl.col_values(1)[15]
        Departure_Airport_Parameters_Class.mail = current_cl.col_values(1)[16]
        Departure_Airport_Parameters_Class.avt = current_cl.col_values(1)[21]
        p = Departure_Airport_Parameters_Class.num_pistes = current_cl.col_values(1)[26]
        Departure_Airport_Parameters_Class.RWY1_1 = current_cl.col_values(1)[28]
        Departure_Airport_Parameters_Class.RWY2_1 = current_cl.col_values(1)[29]
        Departure_Airport_Parameters_Class.preference_1 = current_cl.col_values(1)[30]
        Departure_Airport_Parameters_Class.QFU1_1 = current_cl.col_values(1)[31]
        Departure_Airport_Parameters_Class.QFU2_1 = current_cl.col_values(1)[32]
        Departure_Airport_Parameters_Class.dimensions_1 = current_cl.col_values(1)[33]
        Departure_Airport_Parameters_Class.nature_1 = current_cl.col_values(1)[34]
        Departure_Airport_Parameters_Class.TODA1_1 = current_cl.col_values(1)[36]
        Departure_Airport_Parameters_Class.TODA2_1 = current_cl.col_values(1)[37]
        Departure_Airport_Parameters_Class.ASDA1_1 = current_cl.col_values(1)[38]
        Departure_Airport_Parameters_Class.ASDA2_1 = current_cl.col_values(1)[39]
        Departure_Airport_Parameters_Class.LDA1_1 = current_cl.col_values(1)[40]
        Departure_Airport_Parameters_Class.LDA2_1 = current_cl.col_values(1)[41]
        if (p==2):
            Departure_Airport_Parameters_Class.dangers = [2,current_cl.col_values(1)[59],current_cl.col_values(1)[60]]
            Departure_Airport_Parameters_Class.consignes = [6,current_cl.col_values(1)[62],current_cl.col_values(1)[63],current_cl.col_values(1)[64],current_cl.col_values(1)[65],current_cl.col_values(1)[66],current_cl.col_values(1)[67]]
        else:
            if (current_cl.col_values(1)[43]==1):
                Departure_Airport_Parameters_Class.dangers = [1,current_cl.col_values(1)[44],0]
                Departure_Airport_Parameters_Class.consignes = [4,current_cl.col_values(1)[46],current_cl.col_values(1)[47],current_cl.col_values(1)[48],current_cl.col_values(1)[49],0,0]
            else:
                Departure_Airport_Parameters_Class.dangers = [0,0,0]
                Departure_Airport_Parameters_Class.consignes = [5,current_cl.col_values(1)[46],current_cl.col_values(1)[47],current_cl.col_values(1)[48],current_cl.col_values(1)[49],current_cl.col_values(1)[50],0]


    def get_name(self):
        return self.name
        
    def get_identification(self):
        return self.identification
        
    def get_codeOACI(self):
        return self.codeOACI
        
    def get_exploitant(self):
        return self.exploitant
        
    def get_CAA(self):
        return self.CAA
        
    def get_BRIA(self):
        return self.BRIA
        
    def get_CAP(self):
        return self.CAP
        
    def get_VAR(self):
        return self.VAR
        
    def get_altitude(self):
        return self.altitude
        
    def get_latitude(self):
        return self.latitude
        
    def get_longitude(self):
        return self.longitude
    
    def get_AA(self):
        return self.AA
    
    def get_direction(self):
        return self.direction
    
    def get_tel(self):
        return self.tel
    
    def get_mail(self):
        return self.mail
    
    def get_avt(self):
        return self.avt
    
    def get_num_pistes(self):
        return self.num_pistes
    
    def get_RWY1_1(self):
        return self.RWY1_1
    
    def get_RWY2_1(self):
        return self.RWY2_1
    
    def get_preference_1(self):
        return self.preference_1
    
    def get_QFU1_1(self):
        return self.QFU1_1
    
    def get_QFU2_1(self):
        return self.QFU2_1
    
    def get_dimensions_1(self):
        return self.dimensions_1
    
    def get_nature_1(self):
        return self.nature_1
    
    def get_TODA1_1(self):
        return self.TODA1_1
    
    def get_TODA2_1(self):
        return self.TODA2_1
    
    def get_ASDA1_1(self):
        return self.ASDA1_1
    
    def get_ASDA2_1(self):
        return self.ASDA2_1
    
    def get_LDA1_1(self):
        return self.LDA1_1
    
    def get_LDA2_1(self):
        return self.LDA2_1
    
    def get_dangers(self):
        return self.dangers
    
    def get_consignes(self):
        return self.consignes
    

class Arrival_Airport_Parameters_Class:
    
    def __init__(self,airport):
        # Import the excel files containing the databases
        Airport_Lists = xlrd.open_workbook('../Databases/airfields_database.xlsx')             
        # Get the names of the tabs
        Airport_cl = Airport_Lists.sheet_names()
        #[MONTAUBAN,GAILLAC,LASBORDES]
        n = len(Airport_cl)
        j = 0
        for i in range (n):
            if (airport==Airport_cl[i]):
                j = i
                break
        current_cl = Airport_Lists.sheet_by_name(Airport_cl[j])  
        Arrival_Airport_Parameters_Class.name = airport
        Arrival_Airport_Parameters_Class.identification = current_cl.col_values(1)[1]
        Arrival_Airport_Parameters_Class.codeOACI = current_cl.col_values(1)[2]
        Arrival_Airport_Parameters_Class.exploitant = current_cl.col_values(1)[3]
        Arrival_Airport_Parameters_Class.CAA = current_cl.col_values(1)[4]
        Arrival_Airport_Parameters_Class.BRIA = current_cl.col_values(1)[5]
        Arrival_Airport_Parameters_Class.CAP = current_cl.col_values(1)[6]
        Arrival_Airport_Parameters_Class.VAR = current_cl.col_values(1)[7]
        Arrival_Airport_Parameters_Class.altitude = current_cl.col_values(1)[8]
        
        latitude = int(current_cl.col_values(1)[9][0]+current_cl.col_values(1)[9][1]) + int(current_cl.col_values(1)[9][3]+current_cl.col_values(1)[9][4])/60.+int(current_cl.col_values(1)[9][6]+current_cl.col_values(1)[9][7])/3600.
        Arrival_Airport_Parameters_Class.latitude = latitude
        longitude = int(current_cl.col_values(1)[10][0]+current_cl.col_values(1)[10][1]+current_cl.col_values(1)[10][2]) + int(current_cl.col_values(1)[10][4]+current_cl.col_values(1)[10][5])/60. + int(current_cl.col_values(1)[10][7]+current_cl.col_values(1)[10][8])/3600.
        Arrival_Airport_Parameters_Class.longitude = longitude
        
        Arrival_Airport_Parameters_Class.AA = current_cl.col_values(1)[13]
        Arrival_Airport_Parameters_Class.direction = current_cl.col_values(1)[14]
        Arrival_Airport_Parameters_Class.tel = current_cl.col_values(1)[15]
        Arrival_Airport_Parameters_Class.mail = current_cl.col_values(1)[16]
        Arrival_Airport_Parameters_Class.avt = current_cl.col_values(1)[21]
        p = Arrival_Airport_Parameters_Class.num_pistes = current_cl.col_values(1)[26]
        Arrival_Airport_Parameters_Class.RWY1_1 = current_cl.col_values(1)[28]
        Arrival_Airport_Parameters_Class.RWY2_1 = current_cl.col_values(1)[29]
        Arrival_Airport_Parameters_Class.preference_1 = current_cl.col_values(1)[30]
        Arrival_Airport_Parameters_Class.QFU1_1 = current_cl.col_values(1)[31]
        Arrival_Airport_Parameters_Class.QFU2_1 = current_cl.col_values(1)[32]
        Arrival_Airport_Parameters_Class.dimensions_1 = current_cl.col_values(1)[33]
        Arrival_Airport_Parameters_Class.nature_1 = current_cl.col_values(1)[34]
        Arrival_Airport_Parameters_Class.TODA1_1 = current_cl.col_values(1)[36]
        Arrival_Airport_Parameters_Class.TODA2_1 = current_cl.col_values(1)[37]
        Arrival_Airport_Parameters_Class.ASDA1_1 = current_cl.col_values(1)[38]
        Arrival_Airport_Parameters_Class.ASDA2_1 = current_cl.col_values(1)[39]
        Arrival_Airport_Parameters_Class.LDA1_1 = current_cl.col_values(1)[40]
        Arrival_Airport_Parameters_Class.LDA2_1 = current_cl.col_values(1)[41]
        if (p==2):
            Arrival_Airport_Parameters_Class.dangers = [2,current_cl.col_values(1)[59],current_cl.col_values(1)[60]]
            Arrival_Airport_Parameters_Class.consignes = [6,current_cl.col_values(1)[62],current_cl.col_values(1)[63],current_cl.col_values(1)[64],current_cl.col_values(1)[65],current_cl.col_values(1)[66],current_cl.col_values(1)[67]]
        else:
            if (current_cl.col_values(1)[43]==1):
                Arrival_Airport_Parameters_Class.dangers = [1,current_cl.col_values(1)[44],0]
                Arrival_Airport_Parameters_Class.consignes = [4,current_cl.col_values(1)[46],current_cl.col_values(1)[47],current_cl.col_values(1)[48],current_cl.col_values(1)[49],0,0]
            else:
                Arrival_Airport_Parameters_Class.dangers = [0,0,0]
                Arrival_Airport_Parameters_Class.consignes = [5,current_cl.col_values(1)[46],current_cl.col_values(1)[47],current_cl.col_values(1)[48],current_cl.col_values(1)[49],current_cl.col_values(1)[50],0]
                
        
    def get_name(self):
        return self.name
        
    def get_identification(self):
        return self.identification
        
    def get_codeOACI(self):
        return self.codeOACI
        
    def get_exploitant(self):
        return self.exploitant
        
    def get_CAA(self):
        return self.CAA
        
    def get_BRIA(self):
        return self.BRIA
        
    def get_CAP(self):
        return self.CAP
        
    def get_VAR(self):
        return self.VAR
        
    def get_altitude(self):
        return self.altitude
        
    def get_latitude(self):
        return self.latitude
        
    def get_longitude(self):
        return self.longitude
    
    def get_AA(self):
        return self.AA
    
    def get_direction(self):
        return self.direction
    
    def get_tel(self):
        return self.tel
    
    def get_mail(self):
        return self.mail
    
    def get_avt(self):
        return self.avt
    
    def get_num_pistes(self):
        return self.num_pistes
    
    def get_RWY1_1(self):
        return self.RWY1_1
    
    def get_RWY2_1(self):
        return self.RWY2_1
    
    def get_preference_1(self):
        return self.preference_1
    
    def get_QFU1_1(self):
        return self.QFU1_1
    
    def get_QFU2_1(self):
        return self.QFU2_1
    
    def get_dimensions_1(self):
        return self.dimensions_1
    
    def get_nature_1(self):
        return self.nature_1
    
    def get_TODA1_1(self):
        return self.TODA1_1
    
    def get_TODA2_1(self):
        return self.TODA2_1
    
    def get_ASDA1_1(self):
        return self.ASDA1_1
    
    def get_ASDA2_1(self):
        return self.ASDA2_1
    
    def get_LDA1_1(self):
        return self.LDA1_1
    
    def get_LDA2_1(self):
        return self.LDA2_1
    
    def get_dangers(self):
        return self.dangers
    
    def get_consignes(self):
        return self.consignes

class Flight_Parameters_Class:
    
    def __init__(self,b,c,d,h0,m0,am0,h,m,am,f,dis):
        Flight_Parameters_Class.distance = dis
        Flight_Parameters_Class.passengers = b
        Flight_Parameters_Class.departure_airport = c
        Flight_Parameters_Class.arrival_airport = d
        Flight_Parameters_Class.departure_hour = h0
        Flight_Parameters_Class.departure_minute = m0
        Flight_Parameters_Class.departure_ampm = am0
        Flight_Parameters_Class.arrival_hour = h
        Flight_Parameters_Class.arrival_minute = m
        Flight_Parameters_Class.arrival_ampm = am
        Flight_Parameters_Class.fuel_needed = f
        
    
    def modify_distance(self,d):
        self.distance = d
        return
        
    def get_distance(self):
        return self.distance
    
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