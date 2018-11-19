"""
Here is made an example of a trajectory between Lasbordes-Gaillac.
Lasbordes: lat: 43.588º; long: 1.499º
Gaillac: lat: 43.883º; long: 1.874º 
speed: considered constant and equal to 150 km/h.
"""
import aircraft_position
def trajectoire(pos_depart,pos_arrival):
    while finish(pos,pos_depart,pos_arrival)==False:
    
#It is determined if the pos_arrival is reached
def finish(pos,pos_depart,pos_arrival):
    if departure[0]>=arrival[0]:
        lat=True
    else:
        lat=False
    if departure[1]>=arrival[1]:
        lon=True
    else:
        lon=False
    
    if coord[0]<=arrival[0]:
        lat_coord=True
    else:
        lat_coord=False
    
    if coord[1]<=arrival[1]:
        lon_coord=True
    else:
        lon_coord=False

    if lat==lat_coord & lon==lon_coord:
        return True
    else:
        return False