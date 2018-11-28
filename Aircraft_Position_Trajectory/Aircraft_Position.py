"""
Here are described the different functions that determine the position of the aircraft.
"""
import math
import sys
sys.path.insert(0,'../Useful_Functions')
import Distance

def direction (pos_ant, pos_dest):
    """ 
    The function determines the direction of the aircraft in every new position.
    Param:
    1) pos_ant (list of two terms, º): [long, lat] of the last position.
    2) pos_dest (list of two terms, º): [long, lat] of the destination.
    Return: direction in degrees of the aircraft.
    """
    lat1=math.radians(pos_ant[0])
    long1=math.radians(pos_ant[1])
    lat2=math.radians(pos_dest[0])
    long2=math.radians(pos_dest[1])
    Dlong=long2-long1
    x=math.cos(lat2)*math.sin(Dlong)
    y=math.cos(lat1)*math.sin(lat2)-math.sin(lat1)*math.cos(lat2)*math.cos(Dlong)
    direction=math.atan2(x,y)*180/math.pi
    direction=(direction+360)%360
    return direction

def position (pos_ant,dir,v):
    """ 
    The function calculates the position (long, lat) of the aircraft every 1s.
    Param:
    1) pos_ant (list of two terms, º): [long, lat] of the last position.
    2) dir (float, º): direction of the aircraft.
    3) v (float, km/h): velocity of the aircraft.
    Return: [long, lat] of the aircraft.
    """
    dt=1
    dist=v*dt/3600
    long_ant=math.radians(pos_ant[1])
    lat_ant=math.radians(pos_ant[0])
    dist=float(dist)/6371.0
    dir=math.radians(dir)
    lat=math.asin(math.sin(lat_ant)*math.cos(dist)+math.cos(lat_ant)*math.sin(dist)*math.cos(dir))
    long=long_ant+math.atan2(math.sin(dir)*math.sin(dist)*math.cos(lat_ant),math.cos(dist)-math.sin(lat_ant)*math.sin(lat))
    lat=math.degrees(lat)
    long=math.degrees(long)
    return [lat,long]

def save_position(l_pos,pos):
    """ 
    The function saves a new position of the aircraft in the position list "l_pos"
    Param: pos: [long,lat] of the new position of the aircraft.
    Return: the list refreshed with the new position.
    """
    l_pos.append(pos)
    return l_pos
    
def mean_time_travel(af_dep,af_arr,v):
    """ 
    The function determines the time between two coordinates knowing the velocity
    Param:  
    1) af_dep: [long,lat] of the departure airfield.
    2) af_arr: [long,lat] of the arrival airfield.
    3) v: float of the aircraft velocity in km/h.
    Return: the time between the two coordinates in hours.
    """
    distance=Distance.distance(af_dep,af_arr)
    return distance/v #in hours
            