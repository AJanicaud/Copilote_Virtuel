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

#
import Classe
import math




    # dicimg = {}
    # im=Image.open("Montauban.jpg") 
    # photo = ImageTk.PhotoImage(im) 
    # dicimg['img1'] = photo
    # item = cadre.create_image(320,240,image =photo)


#Function that implements the second interface
#Entering parameter : Data (class that contains all the general information concerning the flight)
def launch(Flight_Parameters_Data):
    
    def callback1(Flight_Parameters_Data):
        str ="../Databases/"+ Classe.Flight_Parameters_Class.get_departure_airport(Flight_Parameters_Data)+".jpg"
        cadre.delete(ALL)
        im2=Image.open(str)
        im2 = resizeimage.resize_contain(im2, [450,350])
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        item = cadre.create_image(300,180, image =photo2) 
        
    def callback2(Flight_Parameters_Data):
        str = "../Databases/Montauban.jpg"
        cadre.delete(ALL)
        im2=Image.open(str)
        im2 = resizeimage.resize_contain(im2, [450,350])
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        item = cadre.create_image(300,180, image =photo2) 

    def callback3(Flight_Parameters_Data):
        str ="../Databases/"+ Classe.Flight_Parameters_Class.get_arrival_airport(Flight_Parameters_Data)+".jpg"
        cadre.delete(ALL)
        im2=Image.open(str)
        im2 = resizeimage.resize_contain(im2, [450,350])
        photo2 = ImageTk.PhotoImage(im2) 
        dicimg['img1'] = photo2
        item = cadre.create_image(300,180, image =photo2) 
    
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
    
    #==============================================================================
    #This one concerns time of arrival
    frame_arrival = LabelFrame(Mission_Parameters_2, height=75, text="Informations concernant le vol")
    frame_arrival.grid_propagate(0)
    frame_arrival.pack(fill="both", expand="no", padx=125)
    
    #This one concerns the position of the map frame
    frame_map = LabelFrame(Mission_Parameters_2, height=370, text="Carte")
    frame_map.grid_propagate(0)
    frame_map.pack(fill="both", expand="no", padx=75)
    #width=640,height=480
    
    cadre=Canvas(frame_map,width=600,height=370,bg="white")
    cadre.pack()
    
    dicimg = {}
    im=Image.open("../Databases/Montauban.jpg")
    im = resizeimage.resize_contain(im, [450,350])
    photo = ImageTk.PhotoImage(im) 
    dicimg['img1'] = photo
    item = cadre.create_image(300,180, image =photo) 

    #==============================================================================
    
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
    #==============================================================================
    
    Departure_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport de départ', fg='green', command=lambda :callback1(Flight_Parameters_Data)).place(x=150, y=573)
    Trajectory_Map = Button(Mission_Parameters_2, text = 'Trajectoire', fg='green', command=lambda :callback2(Flight_Parameters_Data)).place(x=350, y=573)
    Arrival_Airport_Map = Button(Mission_Parameters_2, text = 'Aéroport d''arrivée', fg='green', command=lambda :callback3(Flight_Parameters_Data)).place(x=500, y=573)
    
    Mission_Parameters_2.mainloop()
