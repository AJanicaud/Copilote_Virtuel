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
# Databases

# ________________________________________________________________________________


# Importation
import xlrd
#import pandas as pd

from tkinter import *
from functools import partial
import tkinter.font as tkFont

#from tkinter.ttk import Combobox

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

# Import the excel files containing the databases
check_lists = xlrd.open_workbook('../Databases/Check_lists_DR400.xlsx') # Flight Check lists

airfields_database = xlrd.open_workbook('../Databases/airfields_database.xlsx') # Airfields databases

 
# Get the names of the tabs
names_cl = check_lists.sheet_names()




def callback ():
    print('good')


# ________________________________________________________________________________
"""
Function : print_check_list
        prints the tasks of the check list on the interface
@param : string - current_check_list
        name of check list considered
        is an element of names_cl
@return : void
        prints on the interface
"""
def print_check_list(current_check_list) :
    # The check list considered must be defined in the database
    if (current_check_list not in names_cl): 
        return "Error" 
    
    # We go in the correct tab
    current_cl = check_lists.sheet_by_name(current_check_list)    
    
    # Name of the checklist
    title = current_cl.col_values(0)[0]
    
    # Number of tasks in the checklist
    ##########
        
    i = 2
    
    
    #Opening of the first interface
    Check_list = Tk()
    Check_list.title('Copilote virtuel')
    Check_list.geometry("750x400")
    
    #Font allows to choose the police, the size and the type of our text. We set two types that we will use
    font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
    font2 = tkFont.Font(family='Helvetica', size=14)
    
    #We set the title of this interface
    Title1 = Label(Check_list, text=title, pady=3, height=2, font=font1, fg='red')
    Title1.pack()
    

    #===============================================================================
    #We set all the names and the position of all the Labelframe (small frame)
    
    #Prevous task
    prev_task = LabelFrame(Check_list, height=60, text="Tâche précédente")
    prev_task.grid_propagate(0)
    prev_task.pack(fill="both", expand="no", padx=100)
    
    #Current task
    current_task = LabelFrame(Check_list, height=120, text="Tâche en cours")
    current_task.grid_propagate(0)
    current_task.pack(fill="both", expand="no", padx=100)
    
    #Next task
    next_task = LabelFrame(Check_list, height=60, text="Tâche suivante")
    next_task.grid_propagate(0)
    next_task.pack(fill="both", expand="no", padx=100)
    


    
    
    
    
    while i<5 :

        #===============================================================================

         # for i in range (1, 9) :
        
        # Previous task
        label1 = Label(prev_task, text=current_cl.col_values(2)[i-1], font=font2).place(x=30, y=5)
        label1.pack()
        
        #Current Task
        label2 = Label(current_task, text=current_cl.col_values(2)[i], font=font2).place(x=30, y=5)
        label3 = Label(current_task, text="To do", font=font2).place(x=30, y=40)
        label4 = Label(current_task, text=current_cl.col_values(3)[i], font=font2).place(x=100, y=60)
        
        #Next task
        label5 = Label(next_task, text=current_cl.col_values(2)[i+1], font=font2).place(x=30, y=5)
  
    
        # When validation button hit, erase all, i = i +1
        Validate = Button(Check_list, text = '  OK  ', fg='green', command=Check_list.quit).place(x=350, y=363)

        i+=1
        
    
    Check_list.mainloop()
 # ________________________________________________________________________________   
    
  
print_check_list('Visite_Prevol_Cabine')








# ________________________________________________________________________________
"""
Function : get_check_list
        gets the elements of the check list, ready to be printed
@param : string - current_check_list
        name of check list considered
        is an element of names_cl
@return : 
       number : list of int 
       priority : list of int
       description : list of string
       to_do : list of string
       comments : list of string
"""
#def get_check_list(current_check_list) :
#    # The check list considered must be defined in the database
#    if (current_check_list not in names_cl): 
#        return "Error" 
#    
#    # We go in the correct tab
#    current_cl = check_lists.sheet_by_name(names_cl == current_check_list)
#    
#    number = current_cl[:,0]  # order of the task
#    priority = current_cl[:,1] #importance of the task
#    description = current_cl[:,2] # description of the task
#    to_do = current_cl[:,3] # action to realize
#    comments = current_cl[:,4] # optional comments on the task
#
#    return number, priority, description, to_do, comments
# ________________________________________________________________________________
