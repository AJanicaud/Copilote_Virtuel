"""
It is determined if the aircraft has arrived in the arrival airfield
"""
def finish(pos,af_dep,af_arr):
    """ 
    The function determines if the arrival airfield is achieved.
    Param:
    1) pos (list of two terms, º): [long, lat] of the position of the aircraft.
    2) af_dep (list of two terms, º): [long, lat] of the departure airfield.
    3) af_arr (list of two terms, º): [long, lat] of the arrival airfield.
    Return: list of the different positions of the aircraft to perform the trajectory.
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
