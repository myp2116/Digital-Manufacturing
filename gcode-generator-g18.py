#gcode generator
#Group 18

#import Libraries
import numpy as np
import math
#import random

#Initiate Parameters
print("Please physically move extrusion head to 0,0,0 and reset syringe on CNC machine prior to print")

#Triangle Cross Section Parameters (User Preference)
height = 100 #Object total height (mm) [USER INPUT PARAMETER, USER PREFERENCE]
tri_h = 50.8 #Triangle cross section height dimension (mm) [USER INPUT PARAMETER, USER PREFERENCE]
tri_b = tri_h #base equals the triangle base (ASSUMPTION OF AN EQUALATERAL TRIANGLE)

#Angle Twist Parameters
angle_t = 5 * (math.pi/180) #twist angle of triangle (Rad.)
t_hypo = np.sqrt(((tri_b**2)/4) + ((tri_h**2)/4)) #Distance from the center of the triangle to a vertex

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

steps = round((2*height)/(layer_h1+layer_h2)) #Total number of layers, rounds to the nearest integer
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
        "G92 X0 Y0 Z0 E0", #Set current extrusion head position to 0,0,0 and extrusion head to 0]] #moves extruder to next point
        "M83", #Extruder head set to relative mode
        ]
#Position extruder to initial position relative to 0,0,0 in prep for triangle outline
xcenter = (bed_w/2)
ycenter = (bed_l/2)

#x = (bed_w/2)-(tri_b/2)
#y = (bed_l/2)-(tri_h/2)
z = layer_h1 

#Loop to build object
for i in range(steps):
    if i % 2 == 0: #Material 1 extrusion operation, this checks to see if iteration is an even number 
        
        #side 1
        theta1 = 210 * (math.pi/180) + angle_t*i #Iterated angle
        x1 = xcenter + t_hypo * math.cos(theta1)
        y1 = ycenter + t_hypo * math.sin(theta1)
        data += ["G0 X{} Y{} Z{}".format(x1,y1,z),] #moves extruder to next point with extrusion

        #data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrude Step
        
        #side 2
        theta2 = 330 * (math.pi/180) + angle_t*i #Iterated angle
        x2 = xcenter + t_hypo * math.cos(theta2)
        y2 = ycenter + t_hypo * math.sin(theta2)
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x2,y2,z,e_rate_1, f1),] #Extrude Step
        
        #side 3
        theta3 = 90 * (math.pi/180) + angle_t*i #Iterated angle
        x3 = xcenter + t_hypo * math.cos(theta3)
        y3 = ycenter + t_hypo * math.sin(theta3)
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x3,y3,z,e_rate_1, f1),] #Extrude Step

        data+= ["G1 X{} Y{} Z{} E{} F{}".format(x1,y1,z,e_rate_1, f1),] #Extrude Step (to complete the triangle)

        #Raise up to next layer
        z += layer_h2
        #dwell for 20 seconds between materials
        data += ["G4 S20"]

    else: #Material 2 extrusion operation

         #side 1
        theta1 = 210 * (math.pi/180) + angle_t*i #Iterated angle
        x1 = xcenter + t_hypo * math.cos(theta1)
        y1 = ycenter + t_hypo * math.sin(theta1)
        data += ["G0 X{} Y{} Z{} E{} F{}".format(x1,y1,z,e_rate_2, f2),] #Extrude Step
        
        #side 2
        theta2 = 330 * (math.pi/180) + angle_t*i #Iterated angle
        x2 = xcenter + t_hypo * math.cos(theta2)
        y2 = ycenter + t_hypo * math.sin(theta2)
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x2,y2,z,e_rate_2, f2),] #Extrude Step
        
        #side 3
        theta3 = 90 * (math.pi/180) + angle_t*i #Iterated angle
        x3 = xcenter + t_hypo * math.cos(theta3)
        y3 = ycenter + t_hypo * math.sin(theta3)
        data += ["G1 X{} Y{} Z{} E{} F{}".format(x3,y3,z,e_rate_2, f2),] #Extrude Step

        data += ["G1 X{} Y{} Z{} E{} F{}".format(x1,y1,z,e_rate_1, f1),] #Extrude Step (to complete the triangle)

        #Raise up to next layer
        z += layer_h1
        #dwell for 20 seconds between materials
        data += ["G4 S20"]

data+=["G0 X0 Y0 Z0",] #Return to origin after print
data+=["M106 S0"] #turn printer fan off
##################

#Generate G Code
write_gcode("Food_Print_G18.gcode", data)