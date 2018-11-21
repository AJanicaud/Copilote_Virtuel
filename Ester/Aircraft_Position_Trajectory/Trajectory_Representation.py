# -*- coding: utf-8 -*-
"""
Representation of the aircraft trajectory given by a list of coordinates.
"""
import matplotlib.pyplot as plt
def represent(l_pos):
    """ 
    The function represents the different positions of the aircraft in red and the last one in black. 
    Param: l_pos: list of [long,lat] of the different positions of the aircraft.
    Return: the plot with the different positions of the aircraft.
    """
    x=[]
    y=[]
    for pos in l_pos[:-1]:
        x.append(pos[1])
        y.append(pos[0])
    plt.plot(x,y,'go')
    n_x=l_pos[len(l_pos)-1][1]
    n_y=l_pos[len(l_pos)-1][0]
    plt.plot(n_x,n_y,'ro')
    plt.show()