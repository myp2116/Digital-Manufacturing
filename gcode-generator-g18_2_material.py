#gcode generator
#Group 18

#import Libraries
#import numpy as np
import math
#import random

#Initiate Parameters
print("Please physically move extrusion head to 0,0,0 and reset syringe on CNC machine prior to print")

#Triangle Cross Section Parameters (User Preference)
height = 100 #Object total height (mm) [USER INPUT PARAMETER, USER PREFERENCE]
tri_b = 50.8 #Triangle cross section base dimension (mm) [USER INPUT PARAMETER, USER PREFERENCE]
tri_h = 50.8 #Triangle cross section height dimension (mm) [USER INPUT PARAMETER, USER PREFERENCE]

#Machine Parameters (Intrinsic Properites)
nzl_dia = 0.89 #mm diameter of extrusion nozzle, assumes 18 gauge [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_w = 254 #mm width (left to right) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_l = 254 #mm length (front to back) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]

#Material Properties (EXPERIMENTAL)
#Material 1
e_rate_1 = float(input("Enter the extrusion distance of material 1 in mm: ")) #Extrusion Distance, originally 2 mm extrusion of syringe for Material 1 [EXPERIMENTAL PARAMETER, Toggle as Needed]
f1 = float(input("Enter the feedrate of material 1 in mm/s: ")) #Feedrate, originally 120 mm/min [EXPERIMENTAL PARAMETER, Toggle as Needed]
layer_h1= float(input("Enter the layer height of material 1 in mm: ")) #layer height, originally 2mm [EXPERIMENTAL PARAMETER, Toggle as Needed]
#Material 2
e_rate_2 = float(input("Enter the extrusion distance of material 2 in mm: ")) #Extrusion Distance, originally 2 mm extrusion of syringe for Material 1 [EXPERIMENTAL PARAMETER, Toggle as Needed]
f2 = float(input("Enter the feedrate of material 2 in mm/s: ")) #Feedrate, originally 120 mm/min [EXPERIMENTAL PARAMETER, Toggle as Needed]
layer_h2= float(input("Enter the layer height of material 2 in mm: ")) #layer height, originally 2mm [EXPERIMENTAL PARAMETER, Toggle as Needed]

steps = round((2*height)/(layer_h1+layer_h2)) #Total number of layers, rounds to the nearest interger
#layer_height = height/steps #layer height print based upon parameters

#Define g Code Write Function
def write_gcode(file, gcode_data):
    with open(file, 'w') as f:
        for command in gcode_data:
            f.write(command + '\n')

#Write g code data
#Initial Block
data = [";Group 18 gcode Generator", #Header text
        "G21", #Switch to metric units
        "G90", #Switch to absolute units
        "M106 S255", #Starts fan on printer
        "G92 X0 Y0 Z0 E0", #Set current extrusion head position to 0,0,0 and extrusion head to 0
        "M83", #Extruder head set to relative mode
        ]
#Position extruder to initial position relative to 0,0,0 in prep for triangle outline
x=(bed_w/2)-(tri_b/2) 
y=(bed_l/2)-(tri_h/2)
z=layer_h1 

#Loop to build object
for i in range(steps):
    if i % 2 == 0: #Material 1 extrusion operation, this checks to see if iteration is an even number 
        data += ["G0 X{} Y{} Z{}".format(x,y,z),] #moves extruder to next point
        
        #side 1
        x+=tri_b
        y+=0
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrude Step
        
        #side 2
        x-=tri_b/2
        y+=tri_h
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrude Step
        
        #side 3
        x-=tri_b/2
        y-=tri_h
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrue Step
        #Raise up to next layer
        z+=layer_h2
        #dwell for 20 seconds between materials
        data += ["G4 S20"]

    else: #Material 2 extrusion operation
        data += ["G0 X{} Y{} Z{}".format(x,y,z),] #moves extruder to next point
        #side 1
        x+=tri_b
        y+=0
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_2, f2),] #Extrude Step
        
        #side 2
        x-=tri_b/2
        y+=tri_h
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_2, f2),] #Extrude Step
        
        #side 3
        x-=tri_b/2
        y-=tri_h
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_2, f2),] #Extrue Step
        #Raise up to next layer
        z+=layer_h1
        #dwell for 20 seconds between materials
        data += ["G4 S20"]
        #Iterate angle of rotation

data+=["G0 X0 Y0 Z0",] #Return to origin after print
data+=["M106 S0"] #turn printer fan off
##################

#Generate G Code
write_gcode("Food_Print_G18.gcode", data)