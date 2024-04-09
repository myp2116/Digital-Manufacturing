#gcode generator
#Group 18

#import Libraries
#import numpy as np
#import math
#import random

#Initiate Parameters
print("Please physically move extrusion head to 0,0,0 and reset syringe on CNC machine prior to print")
#USER INPUTs (update variables as needed)
height= 100 #mm Object total height [USER INPUT PARAMETER, USER PREFERENCE]
tri_b = 50.8 #mm Triangle cross section base dimension [USER INPUT PARAMETER, USER PREFERENCE]
tri_h = 50.8 #mm Triangle cross section height dimension [USER INPUT PARAMETER, USER PREFERENCE]

#Constants, obtained through experimentation
steps = 20 #Total number of layers [EXPERIMENTAL PARAMETER, Toggle as Needed]
nzl_dia = 0.89 #mm diameter of extrusion nozzle, assumes 18 gauge [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_w = 254 #mm width (left to right) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_l = 254 #mm length (front to back) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]
e_rate = 2 #mm/s? (extrusion rate of syringe, this may end up being be non-linear) [EXPERIMENTAL PARAMETER, Toggle as Needed]

layer_height = height/steps #layer height print based upon parameters
#Define G Code Write Function
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
        "M82", #Extruder head set to absolute mode
        ]
#Position extruder to initial position relative to 0,0,0 in prep for triangle outline
x=(bed_w/2)-(tri_b/2) 
y=(bed_l/2)-(tri_h/2)
z=layer_height

#Loop to build object
for i in range(steps):
    data += ["G0 X{} Y{} Z{}".format(x,y,z),]
    #side 1
    x+=tri_b
    y+=0
    data += ["G1 X{} Y{} Z{} E{}".format(x,y,z,e_rate),]
    #side 2
    x-=tri_b/2
    y+=tri_h
    data += ["G1 X{} Y{} Z{} E{}".format(x,y,z,e_rate),]
    #side 3
    x-=tri_b/2
    y-=tri_h
    data += ["G1 X{} Y{} Z{} E{}".format(x,y,z,e_rate),]
    #Raise up to next layer
    z+=layer_height

data+=["G0 X0 Y0 Z0",] #Return to origin after print
data+=["M106 S0"] #turn printer fan off
##################

#Generate G Code
write_gcode("Food_Print_G18.gcode", data)