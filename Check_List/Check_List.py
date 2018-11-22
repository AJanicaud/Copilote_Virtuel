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
# Gets the databases from excel files
# ________________________________________________________________________________


# Import the excel files containing the databases
Check_Lists = xlrd.open_workbook('../Databases/Check_Lists_DR400.xlsx') # Flight Check lists

# Get the names of the tabs
names_cl = Check_Lists.sheet_names()

# ________________________________________________________________________________
#
# Displays the tasks on the interface for the pilote to see
# ________________________________________________________________________________


"""
Function : next_window
           Allows the interface to switch to the next task when the current task is completed
           Is called by hitting the ok-button
@param : IntVar counter
         int n
         tkinter.Tk Check_list
         Labels prev_task, current_task, action and next_task
         xlrd.sheet.Sheet current_cl
@return : void
        increments the counter of one
        displays the next task in the check list
"""
def next_window(counter,n, Check_list, prev_task, current_task, action, next_task, current_cl):
    counter.set(counter.get()+1) # Increments the counter of one
    i = int(counter.get()) # Transforms the counter from an IntVar to and int 
    # Modify tasks displayed
    if (counter.get()<n-1):
         prev_task.set(current_cl.col_values(2)[i-1])
         current_task.set(current_cl.col_values(2)[i])
         action.set(current_cl.col_values(3)[i])
         next_task.set(current_cl.col_values(2)[i+1])
    elif (counter.get() == n-1):
         prev_task.set(current_cl.col_values(2)[i-1])
         current_task.set(current_cl.col_values(2)[i])
         action.set(current_cl.col_values(3)[i])
         next_task.set('') # When the last task has been reached, there is nothing else to do
    else :
         Check_list.destroy()  # Stop when last task has been displayed


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
    
    # Number of lines in the checklist
    n = current_cl.nrows
    
    #===============================================================================
    # Settings of the window
    
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
    
    #Previous task
    prev_task_frame = LabelFrame(Check_list, height=60, text="Tâche précédente")
    prev_task_frame.grid_propagate(0)
    prev_task_frame.pack(fill="both", expand="no", padx=100)
    
    #Current task
    current_task_frame = LabelFrame(Check_list, height=120, text="Tâche en cours")
    current_task_frame.grid_propagate(0)
    current_task_frame.pack(fill="both", expand="no", padx=100)
    
    #Next task
    next_task_frame = LabelFrame(Check_list, height=60, text="Tâche suivante")
    next_task_frame.grid_propagate(0)
    next_task_frame.pack(fill="both", expand="no", padx=100)


    #===============================================================================
    # Content of the frames

    counter = IntVar(value=2) # Counter that will keep track of the current task
    i = int(counter.get()) # Conversion of this counter to int to allow its use as list index
    
    # The content of the first window to be displayed
    prev_task = StringVar(value = '') 
    current_task = StringVar(value = current_cl.col_values(2)[i])
    action = StringVar(value = current_cl.col_values(3)[i])
    next_task = StringVar(value = current_cl.col_values(2)[i+1])
    
    # All the labels that will be displayed on the interface
    prev_task_label = Label(prev_task_frame, textvariable = prev_task, font=font2).place(x=30, y=5)
    current_task_label = Label(current_task_frame, textvariable = current_task, font=font2).place(x=30, y=5)
    to_do_label = Label(current_task_frame, text="To do", font=font2).place(x=30, y=40)
    action_label = Label(current_task_frame, textvariable = action, font=font2).place(x=100, y=60)
    next_task_label = Label(next_task_frame, textvariable = next_task, font=font2).place(x=30, y=5)
      
    #===============================================================================
    # Validation button :
        # is hit when current task is completed
        # calls the next_window function
    Validate = Button(Check_list, text = '  OK  ', fg='green', command=lambda :next_window(counter,n, Check_list, prev_task, current_task, action, next_task, current_cl)).place(x=350, y=363)
    
        
    # Runs the tkinter interface
    Check_list.mainloop()
  
    
  
print_check_list('Visite_Prevol_Cabine') # Test to see if functions work


 # ________________________________________________________________________________ 