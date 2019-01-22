# ________________________________________________________________________________
#                     COPILOTE VIRTUEL
#                       Static model
# ________________________________________________________________________________
# 
# Second interface: the purpose is to present to the user the main information about the flight (distance to fullfil, fuel needed, time of arrival)

#Importations
from tkinter import *
from functools import partial
import tkinter.font as tkFont
from tkinter.ttk import Combobox
from resizeimage import resizeimage
from PIL import Image, ImageFont, ImageDraw, ImageTk
import datetime 

import Classe
import math
import requests

#
#import sys
#sys.path.insert(0,'/Users/lancelotribot/documents/spider/Aircraft_Position_Trajectory')
#import Trajectory

#Function that implements the second interface
#Entering parameter : Data (class that contains all the general information concerning the flight)
def launch(Flight_Parameters_Data,Departure_Airport_Parameters_Data,Arrival_Airport_Parameters_Data):
    
    #function called by the user when he pressed the button "Aéroport de départ"
    #Input : Flight_Parameters_Data : a classe that contains all the data concerning the flight
    def Departure_Airport(Flight_Parameters_Data,Departure_Airport_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure_P,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit,Weather_visibility_label,Weather_visibility_t0_label,Weather_visibility_unit_label):
        
        #We collect the name of the departure airport. We concatenate this string to get str = name_of_the_airport.jpg
        str ="../Databases/"+ Classe.Flight_Parameters_Class.get_departure_airport(Flight_Parameters_Data)+".jpg"
        #We delete the first canvas that contains the trajectory
        cadre.delete(ALL)
        #We open the picture
        im2=Image.open(str)
        #We change the size of the picture in order to adapt it to the canvas
        im2 = resizeimage.resize_contain(im2, [425,325])
        #We charge the picture
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        #We set the place of the picture
        item = cadre.create_image(300,180, image =photo2) 
        
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+Classe.Flight_Parameters_Class.get_departure_airport(Flight_Parameters_Data)+"&APPID=fe479539ff1c6744f5c9030f2c139e67")
        r2 = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="+Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data)+"&APPID=fe479539ff1c6744f5c9030f2c139e67")
        data=r.json()
        data2=r2.json()
        previsions = data2['list'][1]
        #We set the label concerning the distance to achieve
        font0 = tkFont.Font(family='Helvetica', size=14,underline = TRUE)
        
        #state = data['weather'][0]['main']
        temp = int(10*(data['main']['temp']-273.15))/10.
        pressure = int(data['main']['pressure'])
        visibility = int(data['visibility'])
        humidity = int(data['main']['humidity'])
        wind_speed = data['wind']['speed']
        if (len(data['wind'])>1):
            wind_deg = data['wind']['deg']
        else:
            wind_deg = 0
        sunrise = data['sys']['sunrise']
        converted_time_sunrise = datetime.datetime.fromtimestamp(int(sunrise)).strftime('%I:%M %p')
        sunset = data['sys']['sunset']
        converted_time_sunset = datetime.datetime.fromtimestamp(int(sunset)).strftime('%I:%M %p')
        
        Weather_departure_t0.set("Météo actuelle :")
        #State of the sky
        #Weather_state.set(state)
        #Pressure
        Weather_pressure_P.set("P = ")
        Weather_pressure_t0.set(pressure)
        Weather_pressure_unit.set("hPa")
        
        #Temperature
        Weather_temperature_T.set("T = ")
        Weather_temperature_t0.set(temp)
        Weather_temperature_unit.set("°C")
        
        #Visibility
        if(visibility>8000):
            color = 'lime green'
        elif(visibility>5000):
            color= 'forest green'
        elif(visibility>1500):
            color = 'orange'
        elif(visibility>800):
            color = 'orange red'
        else:
            color = 'red'
        Weather_visibility.set("Visu :")
        Weather_visibility_t0.set(visibility)
        Weather_visibility_unit.set("m")
        #Weather_visibility_label.config(fg=color)
        #Weather_visibility_t0_label.config(fg=color)
        #Weather_visibility_unit_label.config(fg=color)
        
        #Humidity
        Weather_humidity.set("Humidité :")
        Weather_humidity_t0.set(humidity)
        Weather_humidity_unit.set("%")
        
        #Wind_speed
        Weather_wind.set("Vent :")
        Weather_wind_t0.set(wind_speed)
        Weather_wind_unit.set("m/s")
        
        #Wind_direction
        Weather_wind_direction.set("Direction :")
        Weather_wind_direction_t0.set(wind_deg)
        Weather_wind_direction_unit.set("°")
        
        #We compute the time for the weather forecast
        prevision_hour = previsions['dt_txt']
        h = int(prevision_hour[11])*10+int(prevision_hour[12])
        m = int(prevision_hour[14])*10+int(prevision_hour[15])
        if (h>11):
            h = h-12
            str = 'PM'
        else:
            str = 'AM'
        
        #Time for the weather forecast
        Weather_departure_t3.set("Prévision")
        Weather_departure_t3h.set(h)
        Weather_departure_t3m.set(":00"+str)

        
        prevision_state=previsions['weather'][0]['main']
        prevision_temp = int(10*(previsions['main']['temp']-273.15))/10.
        prevision_pressure = int(previsions['main']['pressure'])
        #prevision_visibility = int(previsions['visibility'])
        prevision_humidity = int(previsions['main']['humidity'])
        prevision_wind_speed = int(10*previsions['wind']['speed'])/10.
        prevision_wind_deg = int(10*previsions['wind']['deg'])/10.
        
        #State of the sky
        Prevision_Weather_state.set(prevision_state)
        
        #Pressure
        Prevision_Weather_pressure_P.set("P = ")
        Prevision_Weather_pressure_t0.set(prevision_pressure)
        Prevision_Weather_pressure_unit.set("hPa")
        
        #Temperature
        Prevision_Weather_temperature_T.set("T = ")
        Prevision_Weather_temperature_t0.set(prevision_temp)
        Prevision_Weather_temperature_unit.set("°C")
        
        #Humidity
        Prevision_Weather_humidity.set("Humidité :")
        Prevision_Weather_humidity_t0.set(prevision_humidity)
        Prevision_Weather_humidity_unit.set("%")
        
        #Wind_speed
        Prevision_Weather_wind.set("Vent :")
        Prevision_Weather_wind_t0.set(prevision_wind_speed)
        Prevision_Weather_wind_unit.set("m/s")
        
        #Wind_direction
        Prevision_Weather_wind_direction.set("Direction :")
        Prevision_Weather_wind_direction_t0.set(prevision_wind_deg)
        Prevision_Weather_wind_direction_unit.set("°")
        
        Sunrise.set("Lever du soleil :")
        Sunrise_time.set(converted_time_sunrise)
        Sunset.set("Coucher du soleil :")
        Sunset_time.set(converted_time_sunset)
        
        Info_Airport = Button(Mission_Parameters_2, text = 'Infos Aéroport', fg='green', command=lambda :Infos_Departure_Airport(Flight_Parameters_Data,Departure_Airport_Parameters_Data)).place(x=340, y=533)
    
    #function called by the user when he pressed the button "Trajectoire"
    #Input : Flight_Parameters_Data : a classe that contains all the data concerning the flight
    def Trajectory(Flight_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit):
        
        #We set all the previous weather data to none in order to clear the interface
        Weather_departure_t0.set('')
        Weather_state.set('')
        Weather_pressure.set('')
        Weather_pressure_t0.set('')
        Weather_pressure_unit.set('')
        Weather_temperature_T.set('')
        Weather_temperature_t0.set('')
        Weather_temperature_unit.set('')
        Weather_humidity.set('')
        Weather_humidity_t0.set('')
        Weather_humidity_unit.set('')
        Weather_wind.set('')
        Weather_wind_t0.set('')
        Weather_wind_unit.set('')
        Weather_wind_direction.set('')
        Weather_wind_direction_t0.set('')
        Weather_wind_direction_unit.set('')
        Weather_departure_t3.set('')
        Weather_departure_t3h.set('')
        Weather_departure_t3m.set('')
        Prevision_Weather_state.set('')
        Prevision_Weather_pressure_P.set('')
        Prevision_Weather_pressure_t0.set('')
        Prevision_Weather_pressure_unit.set('')
        Prevision_Weather_temperature_T.set('')
        Prevision_Weather_temperature_t0.set('')
        Prevision_Weather_temperature_unit.set('')
        Prevision_Weather_humidity.set('')
        Prevision_Weather_humidity_t0.set('')
        Prevision_Weather_humidity_unit.set('')
        Prevision_Weather_wind.set('')
        Prevision_Weather_wind_t0.set('')
        Prevision_Weather_wind_unit.set('')
        Prevision_Weather_wind_direction.set('')
        Prevision_Weather_wind_direction_t0.set('')
        Prevision_Weather_wind_direction_unit.set('')
        Sunrise.set('')
        Sunrise_time.set('')
        Sunset.set('')
        Sunset_time.set('')
        Weather_visibility.set('')
        Weather_visibility_t0.set('')
        Weather_visibility_unit.set('')
        
        #We collect the name of the departure airport. We concatenate this string to get str = trajectory.jpg
        str = "../Databases/Global_Trajectory.jpg"
        #We delete the first canvas that contains the previous picture
        cadre.delete(ALL)
        #We open the picture
        im2=Image.open(str)
        #We change the size of the picture in order to adapt it to the canvas
        im2 = resizeimage.resize_contain(im2, [425,325])
        #We charge the picture
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        #We set the place of the picture
        item = cadre.create_image(300,180, image =photo2) 
        
        
        
    #function called by the user when he pressed the button "Aéroport d'arrivée"
    #Input : Flight_Parameters_Data : a classe that contains all the data concerning the flight
    def Arrival_Airport(Flight_Parameters_Data,Arrival_Airport_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure_P,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit,Weather_visibility_label,Weather_visibility_t0_label,Weather_visibility_unit_label):
        
        #We collect the name of the departure airport. We concatenate this string to get str = name_of_the_airport.jpg
        
        str ="../Databases/"+ Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data)+".jpg"
        #We delete the first canvas that contains the previous picture
        cadre.delete(ALL)

        #cadre.delete(ALL)
        #We open the picture
        im2=Image.open(str)
        #We change the size of the picture in order to adapt it to the canvas
        im2 = resizeimage.resize_contain(im2, [425,325])
        #We charge the picture
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        #We set the place of the picture
        item = cadre.create_image(300,180, image =photo2) 
        
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data)+"&APPID=fe479539ff1c6744f5c9030f2c139e67")
        r2 = requests.get("http://api.openweathermap.org/data/2.5/forecast?q="+Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data)+"&APPID=fe479539ff1c6744f5c9030f2c139e67")
        data=r.json()
        data2=r2.json()
        previsions = data2['list'][1]
        font0 = tkFont.Font(family='Helvetica', size=14,underline = TRUE)
        #state=data['weather'][0]['main']
        temp = int(10*(data['main']['temp']-273.15))/10.
        pressure = int(data['main']['pressure'])
        visibility = int(data['visibility'])
        humidity = int(data['main']['humidity'])
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        sunrise = data['sys']['sunrise']
        converted_time_sunrise = datetime.datetime.fromtimestamp(int(sunrise)).strftime('%I:%M %p')
        sunset = data['sys']['sunset']
        converted_time_sunset = datetime.datetime.fromtimestamp(int(sunset)).strftime('%I:%M %p')
       
       
        #State of the sky
        #Weather_state.set(state)
        #Pressure
        Weather_pressure_P.set("P = ")
        Weather_pressure_t0.set(pressure)
        Weather_pressure_unit.set("hPa")
        
        #Temperature
        Weather_temperature_T.set("T = ")
        Weather_temperature_t0.set(temp)
        Weather_temperature_unit.set("°C")
        
        #Visibility
        if(visibility>8000):
            color = 'lime green'
        elif(visibility>5000):
            color= 'forest green'
        elif(visibility>1500):
            color = 'orange'
        elif(visibility>800):
            color = 'orange red'
        else:
            color = 'red'
            
        Weather_visibility.set("Visu :")
        Weather_visibility_t0.set(visibility)
        Weather_visibility_unit.set("m")
        #Weather_visibility_label.config(fg=color)
        #Weather_visibility_t0_label.config(fg=color)
        #Weather_visibility_unit_label.config(fg=color)
        
        #Humidity
        Weather_humidity.set("Humidité :")
        Weather_humidity_t0.set(humidity)
        Weather_humidity_unit.set("%")
        
        #Wind_speed
        Weather_wind.set("Vent :")
        Weather_wind_t0.set(wind_speed)
        Weather_wind_unit.set("m/s")
        
        #Wind_direction
        Weather_wind_direction.set("Direction :")
        Weather_wind_direction_t0.set(wind_deg)
        Weather_wind_direction_unit.set("°")

        prevision_hour = previsions['dt_txt']
        h = int(prevision_hour[11])*10+int(prevision_hour[12])
        m = int(prevision_hour[14])*10+int(prevision_hour[15])
        if (h>11):
            h = h-12
            str = 'PM'
        else:
            str = 'AM'
        
        Weather_departure_t3.set("Prévision")
        Weather_departure_t3h.set(h)
        Weather_departure_t3m.set(":00"+str)

        
        prevision_state=previsions['weather'][0]['main']
        prevision_temp = int(10*(previsions['main']['temp']-273.15))/10.
        prevision_pressure = int(previsions['main']['pressure'])
        #prevision_visibility = int(previsions['visibility'])
        prevision_humidity = int(previsions['main']['humidity'])
        prevision_wind_speed = int(10*previsions['wind']['speed'])/10.
        prevision_wind_deg = int(10*previsions['wind']['deg'])/10.
        
        #State of the sky
        Prevision_Weather_state.set(prevision_state)
        
        #Pressure
        Prevision_Weather_pressure_P.set("P = ")
        Prevision_Weather_pressure_t0.set(prevision_pressure)
        Prevision_Weather_pressure_unit.set("hPa")
        
        #Temperature
        Prevision_Weather_temperature_T.set("T = ")
        Prevision_Weather_temperature_t0.set(prevision_temp)
        Prevision_Weather_temperature_unit.set("°C")
        
        #Humidity
        Prevision_Weather_humidity.set("Humidité :")
        Prevision_Weather_humidity_t0.set(prevision_humidity)
        Prevision_Weather_humidity_unit.set("%")
        
        #Wind_speed
        Prevision_Weather_wind.set("Vent :")
        Prevision_Weather_wind_t0.set(prevision_wind_speed)
        Prevision_Weather_wind_unit.set("m/s")
        
        #Wind_direction
        Prevision_Weather_wind_direction.set("Direction :")
        Prevision_Weather_wind_direction_t0.set(prevision_wind_deg)
        Prevision_Weather_wind_direction_unit.set("°")
        
        Sunrise.set("Lever du soleil :")
        Sunrise_time.set(converted_time_sunrise)
        Sunset.set("Coucher du soleil :")
        Sunset_time.set(converted_time_sunset)
        
        Info_Airport = Button(Mission_Parameters_2, text = 'Infos Aéroport', fg='green', command=lambda :callback5(Flight_Parameters_Data,Arrival_Airport_Parameters_Data)).place(x=340, y=533)
        
    def Infos_Departure_Airport(Flight_Parameters_Data,Departure_Airport_Parameters_Data):
        
        #We set a new page of the interface that will pop up with all the information needed for the departure airport
        
        #We set the interface
        Infos = Tk()
        Infos.title("Informations concernant l'aéroport de départ")
        Infos.geometry("750x800")
        font_infos = tkFont.Font(family='Helvetica', size=24, weight='bold')
        
        #______________________________________________________________________
        #We set the frame that will contain all the general information about the airport
        frame_general_info = LabelFrame(Infos, height=180, text="Aéroport de  "+Classe.Flight_Parameters_Class.get_departure_airport(Flight_Parameters_Data), fg='red')
        frame_general_info.grid_propagate(0)
        frame_general_info.pack(fill="both", expand="no", padx=50)
        
        #We set all the general information about the airport belonging to the previous frame
        
        #Name of the airport
        Name = Label(frame_general_info, text="Nom : "+Classe.Departure_Airport_Parameters_Class.get_name(Departure_Airport_Parameters_Data), font=font_infos)
        Name.place(x=10,y=10)
        #The identification code of the airport
        Identification = Label(frame_general_info, text="Code d'identification : "+Classe.Departure_Airport_Parameters_Class.get_identification(Departure_Airport_Parameters_Data), font=font_infos)
        Identification.place(x=360,y=10)
        #The OACI code of the airport
        CodeOACI = Label(frame_general_info, text="Code OACI : "+Classe.Departure_Airport_Parameters_Class.get_codeOACI(Departure_Airport_Parameters_Data), font=font_infos)
        CodeOACI.place(x=10,y=30)
        #Who is the owner of the airport
        Exploitant = Label(frame_general_info, text="Exploitant : "+Classe.Departure_Airport_Parameters_Class.get_exploitant(Departure_Airport_Parameters_Data), font=font_infos)
        Exploitant.place(x=430,y=30)
        #
        CAA = Label(frame_general_info, text="CAA : "+Classe.Departure_Airport_Parameters_Class.get_CAA(Departure_Airport_Parameters_Data), font=font_infos)
        CAA.place(x=10,y=50)
        #Information and flight support regional office (Bureau regional d'information et d'assistance au vol)
        BRIA = Label(frame_general_info, text="BRIA : "+Classe.Departure_Airport_Parameters_Class.get_BRIA(Departure_Airport_Parameters_Data), font=font_infos)
        BRIA.place(x=480,y=50)
        #Public air traffic (circulation aérienne publique)
        CAP = Label(frame_general_info, text="CAP : "+Classe.Departure_Airport_Parameters_Class.get_CAP(Departure_Airport_Parameters_Data), font=font_infos)
        CAP.place(x=10,y=70)
        VAR = Label(frame_general_info, text="VAR : "+Classe.Departure_Airport_Parameters_Class.get_VAR(Departure_Airport_Parameters_Data), font=font_infos)
        VAR.place(x=480,y=70)
        #At which altitude is the airport
        Altitude = Label(frame_general_info, text="Altitude : "+Classe.Departure_Airport_Parameters_Class.get_altitude(Departure_Airport_Parameters_Data), font=font_infos)
        Altitude.place(x=10,y=90)
        #Air to Air communications
        AA = Label(frame_general_info, text="A/A : "+str(Classe.Departure_Airport_Parameters_Class.get_AA(Departure_Airport_Parameters_Data)), font=font_infos)
        AA.place(x=480,y=90)
        Direction = Label(frame_general_info, text="Direction : "+Classe.Departure_Airport_Parameters_Class.get_direction(Departure_Airport_Parameters_Data), font=font_infos)
        Direction.place(x=10,y=130)
        #What is the phone numer of the airport
        Tel = Label(frame_general_info, text="Téléphone : "+str(int(Classe.Departure_Airport_Parameters_Class.get_tel(Departure_Airport_Parameters_Data))), font=font_infos)
        Tel.place(x=450,y=110)
        #The email adress of the airport
        Email = Label(frame_general_info, text="E-mail : "+Classe.Departure_Airport_Parameters_Class.get_mail(Departure_Airport_Parameters_Data), font=font_infos)
        Email.place(x=10,y=110)
        AVT = Label(frame_general_info, text="AVT : "+Classe.Departure_Airport_Parameters_Class.get_avt(Departure_Airport_Parameters_Data), font=font_infos)
        AVT.place(x=530,y=130)
        #______________________________________________________________________
        #We set the frame that will contain all the pist information about the airport
        frame_pistes_info = LabelFrame(Infos, height=200, text="Pistes", fg='red')
        frame_pistes_info.grid_propagate(0)
        frame_pistes_info.pack(fill="both", expand="no", padx=50)
        Num_pistes = Label(frame_pistes_info, text="Nombre de pistes : "+str(int(Classe.Departure_Airport_Parameters_Class.get_num_pistes(Departure_Airport_Parameters_Data))), font=font_infos)
        Num_pistes.place(x=250,y=10)
        RWY1 = Label(frame_pistes_info, text="RWY1 : "+str(Classe.Departure_Airport_Parameters_Class.get_RWY1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        RWY1.place(x=10,y=30)
        RWY2 = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Departure_Airport_Parameters_Class.get_RWY2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        RWY2.place(x=500,y=30)
        Preference = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Departure_Airport_Parameters_Class.get_preference_1(Departure_Airport_Parameters_Data)), font=font_infos)
        Preference.place(x=300,y=50)
        QFU1 = Label(frame_pistes_info, text="QFU1 : "+str(Classe.Departure_Airport_Parameters_Class.get_QFU1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        QFU1.place(x=10,y=70)
        QFU2 = Label(frame_pistes_info, text="QFU2 : "+str(Classe.Departure_Airport_Parameters_Class.get_QFU2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        QFU2.place(x=500,y=70)
        Dimensions = Label(frame_pistes_info, text="Dimensions : "+str(Classe.Departure_Airport_Parameters_Class.get_dimensions_1(Departure_Airport_Parameters_Data)), font=font_infos)
        Dimensions.place(x=10,y=90)
        Nature = Label(frame_pistes_info, text="Nature : "+str(Classe.Departure_Airport_Parameters_Class.get_nature_1(Departure_Airport_Parameters_Data)), font=font_infos)
        Nature.place(x=500,y=90)
        TODA1 = Label(frame_pistes_info, text="TODA1 : "+str(Classe.Departure_Airport_Parameters_Class.get_TODA1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        TODA1.place(x=10,y=110)
        TODA2 = Label(frame_pistes_info, text="TODA2 : "+str(Classe.Departure_Airport_Parameters_Class.get_TODA2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        TODA2.place(x=500,y=110)
        ASDA1 = Label(frame_pistes_info, text="ASDA1 : "+str(Classe.Departure_Airport_Parameters_Class.get_ASDA1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        ASDA1.place(x=10,y=130)
        ASDA2 = Label(frame_pistes_info, text="ASDA2 : "+str(Classe.Departure_Airport_Parameters_Class.get_ASDA2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        ASDA2.place(x=500,y=130)
        LDA1 = Label(frame_pistes_info, text="LDA1 : "+str(Classe.Departure_Airport_Parameters_Class.get_LDA1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        LDA1.place(x=10,y=150)
        LDA2 = Label(frame_pistes_info, text="LDA2 : "+str(Classe.Departure_Airport_Parameters_Class.get_LDA2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        LDA2.place(x=500,y=150)
        RWY1 = Label(frame_pistes_info, text="RWY1 : "+str(Classe.Departure_Airport_Parameters_Class.get_RWY1_1(Departure_Airport_Parameters_Data)), font=font_infos)
        RWY1.place(x=10,y=150)
        RWY2 = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Departure_Airport_Parameters_Class.get_RWY2_1(Departure_Airport_Parameters_Data)), font=font_infos)
        RWY2.place(x=500,y=150)
        
        p = int(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[0])
        print(p)
        if (p==2):
            frame_dangers_info = LabelFrame(Infos, height=110, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Nombre de dangers : "+str(Classe.Departure_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[0]), font=font_infos)
            Nombre.place(x=10,y=10)
            Danger_1 = Label(frame_dangers_info, text="1. "+str(Classe.Departure_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[1]), font=font_infos)
            Danger_1.place(x=10,y=30)
            Danger_2 = Label(frame_dangers_info, text="2. "+str(Classe.Departure_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[2]), font=font_infos)
            Danger_2.place(x=10,y=50)
            Danger_2.configure(wraplength=600)
            
            frame_consignes_info = LabelFrame(Infos, height=240, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=50)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=90)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=130)
            Consigne_4.configure(wraplength=600)
            Consigne_5 = Label(frame_consignes_info, text="5. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[5]), font=font_infos)
            Consigne_5.place(x=10,y=170)
            Consigne_5.configure(wraplength=600)
            Consigne_6 = Label(frame_consignes_info, text="6. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[6]), font=font_infos)
            Consigne_6.place(x=10,y=210)
            Consigne_6.configure(wraplength=600)
        elif (p==1):
            frame_dangers_info = LabelFrame(Infos, height=80, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Nombre de dangers : "+str(Classe.Departure_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[0]), font=font_infos)
            Nombre.place(x=10,y=10)
            Danger_1 = Label(frame_dangers_info, text="1. "+str(Classe.Departure_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[1]), font=font_infos)
            Danger_1.place(x=10,y=30)
            
            frame_consignes_info = LabelFrame(Infos, height=200, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=50)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=90)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=130)
            Consigne_4.configure(wraplength=600)

        else:
            frame_dangers_info = LabelFrame(Infos, height=60, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Aucun danger", font=font_infos)
            Nombre.place(x=10,y=10)
            
            frame_consignes_info = LabelFrame(Infos, height=160, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=30)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=50)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=70)
            Consigne_4.configure(wraplength=600)
            Consigne_5 = Label(frame_consignes_info, text="5. "+str(Classe.Departure_Airport_Parameters_Class.get_consignes(Departure_Airport_Parameters_Data)[5]), font=font_infos)
            Consigne_5.place(x=10,y=90)
            Consigne_5.configure(wraplength=600)
            
    
    def callback5(Flight_Parameters_Data,Arrival_Airport_Parameters_Data):
        Infos = Tk()
        Infos.title("Informations concernant l'aéroport d'arrivée")
        Infos.geometry("750x800")
        font_infos = tkFont.Font(family='Helvetica', size=24, weight='bold')
        frame_general_info = LabelFrame(Infos, height=180, text="Aéroport de  "+Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data), fg='red')
        frame_general_info.grid_propagate(0)
        frame_general_info.pack(fill="both", expand="no", padx=50)
        Name = Label(frame_general_info, text="Nom : "+Classe.Arrival_Airport_Parameters_Class.get_name(Arrival_Airport_Parameters_Data), font=font_infos)
        Name.place(x=10,y=10)
        Identification = Label(frame_general_info, text="Code d'identification : "+Classe.Arrival_Airport_Parameters_Class.get_identification(Arrival_Airport_Parameters_Data), font=font_infos)
        Identification.place(x=360,y=10)
        CodeOACI = Label(frame_general_info, text="Code OACI : "+Classe.Arrival_Airport_Parameters_Class.get_codeOACI(Arrival_Airport_Parameters_Data), font=font_infos)
        CodeOACI.place(x=10,y=30)
        Exploitant = Label(frame_general_info, text="Exploitant : "+Classe.Arrival_Airport_Parameters_Class.get_exploitant(Arrival_Airport_Parameters_Data), font=font_infos)
        Exploitant.place(x=430,y=30)
        CAA = Label(frame_general_info, text="CAA : "+Classe.Arrival_Airport_Parameters_Class.get_CAA(Arrival_Airport_Parameters_Data), font=font_infos)
        CAA.place(x=10,y=50)
        BRIA = Label(frame_general_info, text="BRIA : "+Classe.Arrival_Airport_Parameters_Class.get_BRIA(Arrival_Airport_Parameters_Data), font=font_infos)
        BRIA.place(x=500,y=50)
        CAP = Label(frame_general_info, text="CAP : "+Classe.Arrival_Airport_Parameters_Class.get_CAP(Arrival_Airport_Parameters_Data), font=font_infos)
        CAP.place(x=10,y=70)
        VAR = Label(frame_general_info, text="VAR : "+Classe.Arrival_Airport_Parameters_Class.get_VAR(Arrival_Airport_Parameters_Data), font=font_infos)
        VAR.place(x=500,y=70)
        Altitude = Label(frame_general_info, text="Altitude : "+Classe.Arrival_Airport_Parameters_Class.get_altitude(Arrival_Airport_Parameters_Data), font=font_infos)
        Altitude.place(x=10,y=90)
        AA = Label(frame_general_info, text="A/A : "+str(Classe.Arrival_Airport_Parameters_Class.get_AA(Arrival_Airport_Parameters_Data)), font=font_infos)
        AA.place(x=500,y=90)
        Direction = Label(frame_general_info, text="Direction : "+Classe.Arrival_Airport_Parameters_Class.get_direction(Arrival_Airport_Parameters_Data), font=font_infos)
        Direction.place(x=10,y=130)
        Tel = Label(frame_general_info, text="Téléphone : "+str(int(Classe.Arrival_Airport_Parameters_Class.get_tel(Arrival_Airport_Parameters_Data))), font=font_infos)
        Tel.place(x=450,y=110)
        Email = Label(frame_general_info, text="E-mail : "+Classe.Arrival_Airport_Parameters_Class.get_mail(Arrival_Airport_Parameters_Data), font=font_infos)
        Email.place(x=10,y=110)
        AVT = Label(frame_general_info, text="AVT : "+Classe.Arrival_Airport_Parameters_Class.get_avt(Arrival_Airport_Parameters_Data), font=font_infos)
        AVT.place(x=530,y=130)
        
        frame_pistes_info = LabelFrame(Infos, height=200, text="Pistes", fg='red')
        frame_pistes_info.grid_propagate(0)
        frame_pistes_info.pack(fill="both", expand="no", padx=50)
        Num_pistes = Label(frame_pistes_info, text="Nombre de pistes : "+str(int(Classe.Arrival_Airport_Parameters_Class.get_num_pistes(Arrival_Airport_Parameters_Data))), font=font_infos)
        Num_pistes.place(x=250,y=10)
        RWY1 = Label(frame_pistes_info, text="RWY1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_RWY1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        RWY1.place(x=10,y=30)
        RWY2 = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_RWY2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        RWY2.place(x=500,y=30)
        Preference = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_preference_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        Preference.place(x=300,y=50)
        QFU1 = Label(frame_pistes_info, text="QFU1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_QFU1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        QFU1.place(x=10,y=70)
        QFU2 = Label(frame_pistes_info, text="QFU2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_QFU2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        QFU2.place(x=500,y=70)
        Dimensions = Label(frame_pistes_info, text="Dimensions : "+str(Classe.Arrival_Airport_Parameters_Class.get_dimensions_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        Dimensions.place(x=10,y=90)
        Nature = Label(frame_pistes_info, text="Nature : "+str(Classe.Arrival_Airport_Parameters_Class.get_nature_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        Nature.place(x=500,y=90)
        TODA1 = Label(frame_pistes_info, text="TODA1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_TODA1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        TODA1.place(x=10,y=110)
        TODA2 = Label(frame_pistes_info, text="TODA2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_TODA2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        TODA2.place(x=500,y=110)
        ASDA1 = Label(frame_pistes_info, text="ASDA1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_ASDA1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        ASDA1.place(x=10,y=130)
        ASDA2 = Label(frame_pistes_info, text="ASDA2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_ASDA2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        ASDA2.place(x=500,y=130)
        LDA1 = Label(frame_pistes_info, text="LDA1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_LDA1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        LDA1.place(x=10,y=150)
        LDA2 = Label(frame_pistes_info, text="LDA2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_LDA2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        LDA2.place(x=500,y=150)
        RWY1 = Label(frame_pistes_info, text="RWY1 : "+str(Classe.Arrival_Airport_Parameters_Class.get_RWY1_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        RWY1.place(x=10,y=150)
        RWY2 = Label(frame_pistes_info, text="RWY2 : "+str(Classe.Arrival_Airport_Parameters_Class.get_RWY2_1(Arrival_Airport_Parameters_Data)), font=font_infos)
        RWY2.place(x=500,y=150)
        
        p = int(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[0])
        if (p==2):
            frame_dangers_info = LabelFrame(Infos, height=100, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Nombre de dangers : "+str(Classe.Arrival_Airport_Parameters_Class.get_dangers(Departure_Airport_Parameters_Data)[0]), font=font_infos)
            Nombre.place(x=10,y=10)
            Danger_1 = Label(frame_dangers_info, text="1. "+str(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[1]), font=font_infos)
            Danger_1.place(x=10,y=30)
            Danger_2 = Label(frame_dangers_info, text="2. "+str(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[2]), font=font_infos, height = 50)
            Danger_2.place(x=10,y=50)
            
            frame_consignes_info = LabelFrame(Infos, height=240, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=50)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=90)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=130)
            Consigne_4.configure(wraplength=600)
            Consigne_5 = Label(frame_consignes_info, text="5. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[5]), font=font_infos)
            Consigne_5.place(x=10,y=170)
            Consigne_5.configure(wraplength=600)
            Consigne_6 = Label(frame_consignes_info, text="6. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[6]), font=font_infos)
            Consigne_6.place(x=10,y=210)
            Consigne_6.configure(wraplength=600)
        elif (p==1):
            frame_dangers_info = LabelFrame(Infos, height=80, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Nombre de dangers : "+str(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[0]), font=font_infos)
            Nombre.place(x=10,y=10)
            Danger_1 = Label(frame_dangers_info, text="1. "+str(Classe.Arrival_Airport_Parameters_Class.get_dangers(Arrival_Airport_Parameters_Data)[1]), font=font_infos)
            Danger_1.place(x=10,y=30)
            
            frame_consignes_info = LabelFrame(Infos, height=200, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=50)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=90)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=130)
            Consigne_4.configure(wraplength=600)
        else:
            frame_dangers_info = LabelFrame(Infos, height=60, text="Dangers", fg='red')
            frame_dangers_info.grid_propagate(0)
            frame_dangers_info.pack(fill="both", expand="no", padx=50)
            Nombre = Label(frame_dangers_info, text="Aucun danger", font=font_infos)
            Nombre.place(x=10,y=10)
            
            frame_consignes_info = LabelFrame(Infos, height=160, text="Consignes", fg='red')
            frame_consignes_info.grid_propagate(0)
            frame_consignes_info.pack(fill="both", expand="no", padx=50)            
            
            Consigne_1 = Label(frame_consignes_info, text="1. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[1]), font=font_infos)
            Consigne_1.place(x=10,y=10)
            Consigne_1.configure(wraplength=600)
            Consigne_2 = Label(frame_consignes_info, text="2. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[2]), font=font_infos)
            Consigne_2.place(x=10,y=30)
            Consigne_2.configure(wraplength=600)
            Consigne_3 = Label(frame_consignes_info, text="3. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[3]), font=font_infos)
            Consigne_3.place(x=10,y=50)
            Consigne_3.configure(wraplength=600)
            Consigne_4 = Label(frame_consignes_info, text="4. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[4]), font=font_infos)
            Consigne_4.place(x=10,y=70)
            Consigne_4.configure(wraplength=600)
            Consigne_5 = Label(frame_consignes_info, text="5. "+str(Classe.Arrival_Airport_Parameters_Class.get_consignes(Arrival_Airport_Parameters_Data)[5]), font=font_infos)
            Consigne_5.place(x=10,y=90)
            Consigne_5.configure(wraplength=600)

    
    def get_consignes(self):
        return self.consignes
        
    #Opening of the second interface
    Mission_Parameters_2 = Tk()
    Mission_Parameters_2.title('Plan de vol')
    Mission_Parameters_2.geometry("750x600")
    
    #Font allows to choose the police, the size and the type of our text. We set two types that we will use
    font1 = tkFont.Font(family='Helvetica', size=36, weight='bold')
    font_aircraft = tkFont.Font(family='Helvetica', size=14)
    
    #We set the title of this interface
    Title1 = Label(Mission_Parameters_2, text='Plan de vol', pady=3, height=2, font=font1, fg='red')
    Title1.pack()
    
    #==========================================================================
    
    #This one concerns time of arrival
    frame_arrival = LabelFrame(Mission_Parameters_2, height=75, text="Informations concernant le vol")
    frame_arrival.grid_propagate(0)
    frame_arrival.pack(fill="both", expand="no", padx=125)
    
    #This one concerns the position of the map frame
    frame_map = LabelFrame(Mission_Parameters_2, height=370, text="Carte")
    frame_map.grid_propagate(0)
    frame_map.pack(fill="both", expand="no", padx=75)
    #==========================================================================

    #we set the position of the canvas that will contain the picture we want to show
    cadre=Canvas(frame_map,width=600,height=370,bg="white")
    cadre.pack()
    
    
    #We charge and show the picture we want (here the trajectory)
    dicimg = {}
    im=Image.open("../Databases/Global_Trajectory.jpg")
    #We change the size of the picture in order to fit the size of the canvas
    im = resizeimage.resize_contain(im, [425,325])
    photo = ImageTk.PhotoImage(im) 
    dicimg['img1'] = photo
    #We set the place of the picture
    item = cadre.create_image(300,180, image =photo) 

    #==========================================================================   
    
    #We set the label concerning the arrival time
    Arrival_Time = Label(frame_arrival, text="Heure prévue d'arrivée", font=font_aircraft).place(x=30, y=5)
    #We define a string containing the predicted time of arrival (ex: 1h10pm)
    string_1 = str(math.floor(Classe.Flight_Parameters_Class.get_arrival_hour(Flight_Parameters_Data)))+ ' ' + 'H' +' '+ str(math.floor(Classe.Flight_Parameters_Class.get_arrival_minute(Flight_Parameters_Data))) + ' ' + Classe.Flight_Parameters_Class.get_arrival_ampm(Flight_Parameters_Data)
    #We set the label containing the previous string defined
    Hour_Arrival_Time = Label(frame_arrival, text=string_1, font=font_aircraft, fg='blue').place(x=55, y=30)
    
    #We set the label concerning the distance to achieve
    Distance_1 = Label(frame_arrival, text="Distance à parcourir", font=font_aircraft).place(x=200, y=5)
    #We define a string containing the distance to achieve (ex: 100km)
    string_2 = str(math.floor(Classe.Flight_Parameters_Class.get_distance(Flight_Parameters_Data))) + ' ' + 'km'
    #We set the label containing the previous string defined
    Prediction_Distance = Label(frame_arrival, text=string_2, font=font_aircraft, fg='blue').place(x=238, y=30)

    #We set the label concerning the fuel needed
    Fuel_Needed = Label(frame_arrival, text="Fuel nécessaire", font=font_aircraft).place(x=350, y=5)
    #We define a string containing the fuel needed (ex: 10L)
    string_3 = str(math.floor(Classe.Flight_Parameters_Class.get_fuel_needed(Flight_Parameters_Data))) + ' ' + 'L'
    #We set the label containing the previous string defined
    Prediction_Fuel_Needed = Label(frame_arrival, text=string_3, font=font_aircraft, fg='blue').place(x=385, y=30)
    #==========================================================================
    #We define a style of character that we will use for the weatherforecast
    font0 = tkFont.Font(family='Helvetica', size=14,underline = TRUE)

    #==========================================================================
    #We initiate all the data concerning the weather and the weatherforecast to empty value
    Weather_departure_t0 = StringVar(value = '') 
    #State of the sky
    Weather_state = StringVar(value = '') 
    #Pressure
    Weather_pressure_P = StringVar(value='')
    Weather_pressure_t0 = StringVar(value='')
    Weather_pressure_unit = StringVar(value='')
    #Temperature
    Weather_temperature_T = StringVar(value='')
    Weather_temperature_t0 = StringVar(value='')
    Weather_temperature_unit = StringVar(value='')
    #Humidity
    Weather_humidity = StringVar(value='')
    Weather_humidity_t0 = StringVar(value='')
    Weather_humidity_unit = StringVar(value='')
    #Wind strength
    Weather_wind = StringVar(value='')
    Weather_wind_t0 = StringVar(value='')
    Weather_wind_unit = StringVar(value='')
    #Wind direction
    Weather_wind_direction = StringVar(value='')
    Weather_wind_direction_t0 = StringVar(value='')
    Weather_wind_direction_unit = StringVar(value='')
    
    #________________________________________________________________________
    #Forecast
    #Time for the forecast
    Weather_departure_t3 = StringVar(value='')
    Weather_departure_t3h = StringVar(value='')
    Weather_departure_t3m = StringVar(value='')
    #State of the sky 
    Prevision_Weather_state = StringVar(value='')
    #Pressure
    Prevision_Weather_pressure_P = StringVar(value='')
    Prevision_Weather_pressure_t0 = StringVar(value='')
    Prevision_Weather_pressure_unit = StringVar(value='')
    #temperature
    Prevision_Weather_temperature_T = StringVar(value='')
    Prevision_Weather_temperature_t0 = StringVar(value='')
    Prevision_Weather_temperature_unit = StringVar(value='')
    #Humidity
    Prevision_Weather_humidity = StringVar(value='')
    Prevision_Weather_humidity_t0 = StringVar(value='')
    Prevision_Weather_humidity_unit = StringVar(value='')
    #Wind strength
    Prevision_Weather_wind = StringVar(value='')
    Prevision_Weather_wind_t0 = StringVar(value='')
    Prevision_Weather_wind_unit = StringVar(value='')
    #Wind direction
    Prevision_Weather_wind_direction = StringVar(value='')
    Prevision_Weather_wind_direction_t0 = StringVar(value='')
    Prevision_Weather_wind_direction_unit = StringVar(value='')
    #Time of sunrise
    Sunrise = StringVar(value='')
    Sunrise_time = StringVar(value='')
    #Time of sunser
    Sunset = StringVar(value='')
    Sunset_time = StringVar(value='')
    #Visibility
    Weather_visibility = StringVar(value='')
    Weather_visibility_t0 = StringVar(value='')
    Weather_visibility_unit = StringVar(value='')
    
    #===========================================================================
    #We initiate the postion of all those labels
    
    
    Weather_departure_t0_label = Label(frame_map, textvariable= Weather_departure_t0, font=font0).place(x=13, y=20)
    #State of sky
    Weather_state_label = Label(frame_map, textvariable=Weather_state, font=font_aircraft).place(x=30, y=50)
    #Pressure
    Weather_pressure_label = Label(frame_map, textvariable=Weather_pressure_P, font=font_aircraft).place(x=18, y=70)
    Weather_pressure_t0_label = Label(frame_map, textvariable=Weather_pressure_t0, font=font_aircraft).place(x=45, y=70)
    Weather_pressure_unit_label = Label(frame_map, textvariable=Weather_pressure_unit, font=font_aircraft).place(x=80, y=70)
    #Temperature
    Weather_temperature_T_label = Label(frame_map, textvariable=Weather_temperature_T, font=font_aircraft).place(x=18, y=90)
    Weather_temperature_t0_label = Label(frame_map, textvariable=Weather_temperature_t0, font=font_aircraft).place(x=45, y=90)
    Weather_temperature_unit_label = Label(frame_map, textvariable=Weather_temperature_unit, font=font_aircraft).place(x=80, y=90)
    #Humidity
    Weather_humidity_label = Label(frame_map, textvariable=Weather_humidity, font=font_aircraft).place(x=10, y=130)
    Weather_humidity_t0_label = Label(frame_map, textvariable=Weather_humidity_t0, font=font_aircraft).place(x=80, y=130)
    Weather_humidity_unit_label = Label(frame_map, textvariable=Weather_humidity_unit, font=font_aircraft).place(x=100, y=130)
    #Wind strength
    Weather_wind_label = Label(frame_map, textvariable=Weather_wind, font=font_aircraft).place(x=15, y=150)
    Weather_wind_t0_label = Label(frame_map, textvariable=Weather_wind_t0, font=font_aircraft).place(x=65, y=150)
    Weather_wind_unit_label = Label(frame_map, textvariable=Weather_wind_unit, font=font_aircraft).place(x=90, y=150)
    #Wind direction
    Weather_wind_direction_label = Label(frame_map, textvariable=Weather_wind_direction, font=font_aircraft).place(x=8, y=170)
    Weather_wind_t0_label = Label(frame_map, textvariable=Weather_wind_t0, font=font_aircraft).place(x=80, y=170)
    Weather_wind_direction_unit_label = Label(frame_map, textvariable=Weather_wind_direction_unit, font=font_aircraft).place(x=100, y=170)
    Weather_departure_t3_label = Label(frame_map, textvariable=Weather_departure_t3, font=font0).place(x=467, y=20)
    
    #____________________________________________________________________________
    #Weather forecast
    
    Weather_departure_t3h_label = Label(frame_map, textvariable=Weather_departure_t3h, font=font0).place(x=528, y=20)
    Weather_departure_t3m_label = Label(frame_map, textvariable=Weather_departure_t3m, font=font0).place(x=543, y=20)
    #State of sky
    Prevision_Weather_state_label = Label(frame_map, textvariable=Prevision_Weather_state, font=font_aircraft).place(x=500, y=50)
    #Pressure
    Prevision_Weather_pressure_P_label = Label(frame_map, textvariable=Prevision_Weather_pressure_P, font=font_aircraft).place(x=475, y=70)
    Prevision_Weather_pressure_t0_label = Label(frame_map, textvariable=Prevision_Weather_pressure_t0, font=font_aircraft).place(x=500, y=70)
    Prevision_Weather_pressure_unit_label = Label(frame_map, textvariable=Prevision_Weather_pressure_unit, font=font_aircraft).place(x=535, y=70)
    #Temperature
    Prevision_Weather_temperature_T_label = Label(frame_map, textvariable=Prevision_Weather_temperature_T, font=font_aircraft).place(x=478, y=90)
    Prevision_Weather_temperature_t0_label = Label(frame_map, textvariable=Prevision_Weather_temperature_t0, font=font_aircraft).place(x=505, y=90)
    Prevision_Weather_temperature_unit_label = Label(frame_map, textvariable=Prevision_Weather_temperature_unit, font=font_aircraft).place(x=535, y=90)
    #Humidity
    Prevision_Weather_humidity_label = Label(frame_map, textvariable=Prevision_Weather_humidity, font=font_aircraft).place(x=465, y=130)
    Prevision_Weather_humidity_t0_label = Label(frame_map, textvariable=Prevision_Weather_humidity_t0, font=font_aircraft).place(x=540, y=130) 
    Prevision_Weather_humidity_unit_label = Label(frame_map, textvariable=Prevision_Weather_humidity_unit, font=font_aircraft).place(x=560, y=130) 
    #Wind strength
    Prevision_Weather_wind_label = Label(frame_map, textvariable=Prevision_Weather_wind, font=font_aircraft).place(x=470, y=150)
    Prevision_Weather_wind_t0_label = Label(frame_map, textvariable=Prevision_Weather_wind_t0, font=font_aircraft).place(x=515, y=150)   
    Prevision_Weather_wind_unit_label = Label(frame_map, textvariable=Prevision_Weather_wind_unit, font=font_aircraft).place(x=545, y=150)
    #Wind direction
    Prevision_Weather_wind_direction_label = Label(frame_map, textvariable=Prevision_Weather_wind_direction, font=font_aircraft).place(x=465, y=170)
    Prevision_Weather_wind_direction_t0_label = Label(frame_map, textvariable=Prevision_Weather_wind_direction_t0, font=font_aircraft).place(x=530, y=170)
    Prevision_Weather_wind_direction_unit_label = Label(frame_map, textvariable=Prevision_Weather_wind_direction_unit, font=font_aircraft).place(x=565, y=170)
    #Time of sunrise
    Sunrise_label = Label(cadre, textvariable=Sunrise, font=font0).place(x=13, y=250)
    Sunrise_time_label = Label(cadre, textvariable=Sunrise_time, font=font_aircraft).place(x=30, y=280)
    #Time of sunset
    Sunset_label = Label(cadre, textvariable=Sunset, font=font0).place(x=466, y=250)
    Sunset_time_label = Label(cadre, textvariable=Sunset_time, font=font_aircraft).place(x=495, y=280)
    #Visibility
    Weather_visibility_label = Label(frame_map, textvariable=Weather_visibility, font=font_aircraft).place(x=10, y=110)
    Weather_visibility_t0_label = Label(frame_map, textvariable=Weather_visibility_t0, font=font_aircraft).place(x=50, y=110)
    Weather_visibility_unit_label = Label(frame_map, textvariable=Weather_visibility_unit, font=font_aircraft).place(x=100, y=110)
    
    #==========================================================================
    
    #Button handling the departure airport presentation (map of the airport and weather at this place)
    Departure_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport de départ', fg='green', command=lambda :Departure_Airport(Flight_Parameters_Data,Departure_Airport_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure_P,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit,Weather_visibility_label,Weather_visibility_t0_label,Weather_visibility_unit_label)).place(x=150, y=573)
    
    #Button handling the presentation of the trajectory map
    Trajectory_Map = Button(Mission_Parameters_2, text = 'Trajectoire', fg='green', command=lambda :Trajectory(Flight_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure_P,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit)).place(x=350, y=573)
    
    #Button handling the presentation of the aiprot of arrival and the weather around this point
    Arrival_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport d''arrivée', fg='green', command=lambda :Arrival_Airport(Flight_Parameters_Data,Arrival_Airport_Parameters_Data,Weather_departure_t0,Weather_state,Weather_pressure_P,Weather_pressure_t0,Weather_pressure_unit,Weather_temperature_T,Weather_temperature_t0,Weather_temperature_unit,Weather_humidity,Weather_humidity_t0,Weather_humidity_unit,Weather_wind,Weather_wind_t0,Weather_wind_unit,Weather_wind_direction,Weather_wind_direction_t0,Weather_wind_direction_unit,Weather_departure_t3,Weather_departure_t3h,Weather_departure_t3m,Prevision_Weather_state,Prevision_Weather_pressure_P,Prevision_Weather_pressure_t0,Prevision_Weather_pressure_unit,Prevision_Weather_temperature_T,Prevision_Weather_temperature_t0,Prevision_Weather_temperature_unit,Prevision_Weather_humidity,Prevision_Weather_humidity_t0,Prevision_Weather_humidity_unit,Prevision_Weather_wind,Prevision_Weather_wind_t0,Prevision_Weather_wind_unit,Prevision_Weather_wind_direction,Prevision_Weather_wind_direction_t0,Prevision_Weather_wind_direction_unit,Sunrise,Sunrise_time,Sunset,Sunset_time,Weather_visibility,Weather_visibility_t0,Weather_visibility_unit,Weather_visibility_label,Weather_visibility_t0_label,Weather_visibility_unit_label)).place(x=500, y=573)
    
    Mission_Parameters_2.mainloop()
