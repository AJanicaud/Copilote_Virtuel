import math
#Calculation of the distance between two coordinates
def distance(pos_dep,pos_arr):
    lat1=pos_dep[0]
    long1=pos_dep[1]
    lat2=pos_arr[0]
    long2=pos_arr[1]
    lat1=math.radians(lat1)
    long1=math.radians(long1)
    lat2=math.radians(lat2)
    long2=math.radians(long2)
    Dl=lat2-lat1
    DL=long2-long1
    a=(math.sin(Dl/2))**2.0+math.cos(lat1)*math.cos(lat2)*(math.sin(DL/2))**2.0
    c=2.0*math.atan2(math.sqrt(a),math.sqrt(1-a))
    d=6371.0*c
    return d #in km