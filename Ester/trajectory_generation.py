"""
Here are described the different functions that determine a trajectory between two airfields given.
"""
import math
import aircraft_position
import finish
def trajectory(af_dep,af_arr):
    """ 
    The function determines the trajectory that should do the aircraft between two airfields given. The velocity is considered constant and equal to 150 km/h.
    Param:
    1) af_dep (list of two terms, º): [long, lat] of the departure airfield.
    2) af_arr (list of two terms, º): [long, lat] of the arrival airfield.
    Return: list of the different positions of the aircraft to perform the trajectory.
    """
    v=150
    pos=af_dep
    l_pos=[pos]
    while True:
        dir=aircraft_position.direction(pos,af_arr)
        pos=aircraft_position.position(pos,dir,v)
        if finish.finish(pos,af_dep,af_arr)==True:
            l_pos.append(af_arr)
            break
        l_pos.append(pos)
    return l_pos