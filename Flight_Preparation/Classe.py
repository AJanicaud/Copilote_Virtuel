class Donnees:
    
    aircraft = "b"
    
    def __init__(self,a,b,c,d,h0,m0,am0,h,m,am,f):
        Donnees.aircraft = a
        Donnees.passengers = b
        Donnees.departure_airport = c
        Donnees.arrival_airport = d
        Donnees.departure_hour = h0
        Donnees.departure_minute = m0
        Donnees.departure_ampm = am0
        Donnees.arrival_hour = h
        Donnees.arrival_minute = m
        Donnees.arrival_ampm = am
        Donnees.fuel_needed = f
        
    
    def get_aircraft(self):
        return self.aircraft
    
    def get_passengers(self):
        return self.passengers
        
    def get_departure_airport(self):
        return self.departure_airport
    
    def get_arrival_airport(self):
        return self.arrival_airport
    
    def get_departure_hour(self):
        return self.departure_hour
        
    def get_departure_minute(self):
        return self.departure_minute
    
    def get_departure_ampm(self):
        return self.departure_ampm
    
    def get_arrival_hour(self):
        return self.arrival_hour
        
    def get_arrival_minute(self):
        return self.arrival_minute
    
    def get_arrival_ampm(self):
        return self.arrival_ampm
        
    def get_fuel_needed(self):
        return self.fuel_needed