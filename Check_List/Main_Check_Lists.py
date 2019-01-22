#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# COPILOTE VIRTUEL
# Static model
# ________________________________________________________________________________
#
# Databases retrieval and displaying
#
# ________________________________________________________________________________

# Importation
import xlrd
import xlwt
from tkinter import *
from functools import partial
import tkinter.font as tkFont
import Check_List


# Import the excel files containing the databases
Check_Lists = xlrd.open_workbook('../Databases/Check_Lists_DR400.xlsx') # Flight Check lists

# Get the names of the tabs
names_cl = Check_Lists.sheet_names()

"""
['Visite_Prevol_Cabine',  
'Visite_Prevol_Exterieure', 
 'Avant_Mise_En_Route', 
 'Mise_En_Route', 
 'Apres_Mise_En_Route', 
 'Roulage', 
 'Point_D_Arret',
 'Avant_Alignement', 
 'Aligne', 
 'Decollage', 
 'A_300ft_Obstacles_Degages', 
 'Descente', 
 'Vent_Arriere', 
 'Finale', 
 'Piste_Degagee', 
 'Au_Parking', 
 'Apres_Arret_Moteur']
"""



"""
cl = 0 # represents the current check list
over = False

over = Check_List.Print_Check_List(names_cl[cl], over, "DR400-1") # 'Visite_Prevol_Cabine'

if (over == True ) :
    #over = False
    cl += 1
    Check_List.Print_Check_List(names_cl[cl], over,"DR400-1")
    


over = True
Check_List.Print_Check_List(names_cl[0], over, "DR400-1")
Check_List.Print_Check_List(names_cl[1], over, "DR400-1")
Check_List.Print_Check_List(names_cl[2], over, "DR400-1")
Check_List.Print_Check_List(names_cl[3], over, "DR400-1")

"""
    
    
#Prints CL from start to end
def print_CL(start,end):
    over = True # TO BE DELETED
    assert start < end # The checklists have to be printed in a certain order
    if (start < 11):
        for i in range (start,end):
            Check_List.Print_Check_List(names_cl[i], over, "DR400-1")
    else :
        for i in range (start,end):
            Check_List.Print_Landing_Check_List(names_cl[i], over, "DR400-1")

    
print_CL(0,4)


def print_CL_landing():
    over = True
    for i in range (start,end):
        Check_List.Print_Check_List(names_cl[i], over, "DR400-1")






