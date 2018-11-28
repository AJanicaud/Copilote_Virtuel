"""
Here are described the different functions that determine a trajectory between two airfields given.
"""
import Aircraft_Position

def trajectory(af_dep,af_arr,v):
    """ 
    The function determines the trajectory that should do the aircraft between two airfields given. 
    Param:
    1) af_dep (list of two terms, º): [long, lat] of the departure airfield.
    2) af_arr (list of two terms, º): [long, lat] of the arrival airfield.
    3) v (float): velocity of the aircraft in km/h (considered constant during the travel).
    Return: list of the different positions of the aircraft to perform the trajectory.
    """
    pos=af_dep
    l_pos=[pos]
    while True:
        dir=Aircraft_Position.direction(pos,af_arr)
        pos=Aircraft_Position.position(pos,dir,v)
        if finish(pos,af_dep,af_arr)==True:
            l_pos.append(af_arr)
            break
        l_pos.append(pos)
    return l_pos

def finish(pos,af_dep,af_arr):
    """ 
    The function determines if the aricraft has arrived in the airfield. 
    Param:
    1) pos (list of two terms, º): [long, lat] of the position airfield.
    2) af_dep (list of two terms, º): [long, lat] of the departure airfield.
    3) af_arr (list of two terms, º): [long, lat] of the arrival airfield.
    Return: True if the arrival airfield is reached, False if not.
    """
    if af_dep[0]>=af_arr[0]:
        lat=True
    else:
        lat=False
    if af_dep[1]>=af_arr[1]:
        lon=True
    else:
        lon=False
    
    if pos[0]<=af_arr[0]:
        lat_coord=True
    else:
        lat_coord=False
    
    if pos[1]<=af_arr[1]:
        lon_coord=True
    else:
        lon_coord=False

    if lat==lat_coord:
        if lon==lon_coord:
            return True
    else:
        return False