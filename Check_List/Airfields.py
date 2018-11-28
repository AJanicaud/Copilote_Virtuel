#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 19:04:28 2018

@author: alixjanicaud
"""

# COPILOTE VIRTUEL
# Static model
# ________________________________________________________________________________
#
# Databases retrieval and displaying
#
# ________________________________________________________________________________


# Importation
import xlrd
from tkinter import *
from functools import partial
import tkinter.font as tkFont

# ________________________________________________________________________________
#
# Defines the data not accessible yet
# ________________________________________________________________________________

# Aicraft data - not contained in the databases
# To be retrieved from the aircraft
take_off_speed = 2
cruise_speed = 2 # in XX per hour
landing_speed = 2
course = 2 # in XX 
altitude = 2 # in XX
gaz = 2 # in XX - gaz remaining in the airplane



# ________________________________________________________________________________
#
# Gets the databases from excel files
# ________________________________________________________________________________


# Import the excel files containing the databases
Airfields_Database = xlrd.open_workbook('../Databases/Airfields_Database.xlsx') # Airfields databases

 
# Get the names of the tabs
names_airfields = Airfields_Databases.sheet_names()



class Airfields():
    
    
    
    
    


# ________________________________________________________________________________ 
 