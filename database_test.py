#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:16:11 2018

@author: alixjanicaud

TEST
"""

from tkinter import *
from functools import partial
import tkinter.font as tkFont


def callback(i):
    a = Label(prev_task, text=' ', font=font_aircraft).place(x=30, y=5)
    b = Label(current_task, text=' ', font=font_aircraft).place(x=30, y=5)
    c = Label(current_task, text=" ", font=font_aircraft).place(x=30, y=40)
    d = Label(current_task, text=' ', font=font_aircraft).place(x=100, y=60)
    e = Label(next_task, text=' ', font=font_aircraft).place(x=30, y=5)
    i = i + 1


#Opening of the first interface
test = Tk()
test.title('Copilote virtuel')
test.geometry("750x400")

#Font allows to choose the police, the size and the type of our text. We set two types that we will use
font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
font_aircraft = tkFont.Font(family='Helvetica', size=14)

#We set the title of this interface
Title1 = Label(test, text='test', pady=3, height=2, font=font1, fg='red')
Title1.pack()

#===============================================================================
#We set all the names and the position of all the Labelframe (small frame)

#Prevous task
prev_task = LabelFrame(test, height=60, text="Tâche précédente")
prev_task.grid_propagate(0)
prev_task.pack(fill="both", expand="no", padx=100)

#Current task
current_task = LabelFrame(test, height=120, text="Tâche en cours")
current_task.grid_propagate(0)
current_task.pack(fill="both", expand="no", padx=100)

#Next task
next_task = LabelFrame(test, height=60, text="Tâche suivante")
next_task.grid_propagate(0)
next_task.pack(fill="both", expand="no", padx=100)

i = 1
while i < 5 :
    
    # Previous task
    a = Label(prev_task, text=i, font=font_aircraft).place(x=30, y=5)
    
    
    #Current Task
    b = Label(current_task, text=i, font=font_aircraft).place(x=30, y=5)
    
    c = Label(current_task, text="To do", font=font_aircraft).place(x=30, y=40)
    
    d = Label(current_task, text=i, font=font_aircraft).place(x=100, y=60)
    
    
    #Next task
    e = Label(next_task, text=i, font=font_aircraft).place(x=30, y=5)
    
    
    
    # When validation button hit, erase all, i = i +1
    Validate = Button(test, text = '  OK  ', fg='green', command=callback(i)).place(x=350, y=363)
    #  i = i + 1
    #  print("i après validate",i)    
    

test.mainloop()