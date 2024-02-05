#Laser Cut Box Project #1
#Max Plavcan

#Outline
#Input Parameters
    #1. Box Dimensions (l x w x h)
    #2. Material Thickness

#Output
    #SVG code of custom Box

#import Python Numpy to aid in array operations
import numpy as np

#Code for Input Criteria
while True:
    try:
        #Input Parameters for Box geometry
        length = int(input("Enter your box length(mm): "))
        width = int(input("Enter your box width(mm): "))
        height = int(input("Enter your box height(mm): "))
        
        break
    #Error message to display in case the input is not a whole integer
    except ValueError:
        print("!Invalid User input! Please try again with whole number integers for length, width and height")
        print("")

#Code to Generate SVG file for Box

f = open("boxfile.svg", "w") #Creates and Opens an svg file and enables write privileges
f.write(f'<?xml version=\"1.0\" encoding=\"UTF-8\" ?> \n') #Initiates svg format
f.write(f'<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"> \n') #Loads software

###Box Properties###
#Fastener Properties
fast_dia = 0.086 * 25.4 #Fastener diameter
fast_r = fast_dia/2 #Fastener radius
fast_length = 0.375 * 25.4 #Fastener length
nut_width = .188 * 25.4 # Nut width
nut_thick = .063 * 25.4 #Nut thickness

#Material Properties
mat_thick = .125 * 25.4 #Cardboard Thickness

#Margins of Box Outline
w_marg = 60 #width margin
h_marg = 60 #height margin
l_marg = 60 #length margin

#Positioning of Box Faces
BL = np.zeros((6,2)) #Matrix with all values
#First Row
#Face 1 (w x h)
BL[0,0], BL[0,1] = width/2 + w_marg, height/2 + h_marg
#Face 2 (w x h)
BL[1,0], BL[1,1] = BL[0,0] + width + w_marg, BL[0,1]

#Second Row
#Face 5 (TOP) (l x w)
BL[4,0], BL[4,1] = length/2 + l_marg, BL[0,1] + height/2 + width/2 + w_marg
#Face 6 (BOTTOM) (1 x w)
BL[5,0], BL[5,1] = BL[4,0] + length + l_marg, BL[4,1]

#Third Row
#Face 3 (l x h)
BL[2,0], BL[2,1] = length/2 + l_marg, BL[4,1] + width/2 + height/2  + h_marg
#Face 4 (l x h)
BL[3,0], BL[3,1] = BL[2,0] + length + l_marg , BL[4,1] + width/2 + height/2  + h_marg

#Box Face - Type I (Circumferential) (Qty:4) (faces using Width, Height and Length)
def boxface_t1(x_t1, y_t1, L1, L2): 
    #Inputs are x location and y location, L1 (Width or Length) and L2 (Height)
    #Output is svg code that geometrically represents a box face
    #Quadrant 1 (upper left)
    P_t1 = np.zeros((15, 2)) #Array of points that define 1 quadrant of a face
    P_t1[0,0], P_t1[0,1] = x_t1 - (L1/2), y_t1
    P_t1[1,0], P_t1[1,1] = P_t1[0,0], P_t1[0,1] - (((L2/2)-mat_thick)/3)
    P_t1[2,0], P_t1[2,1] = P_t1[1,0] + mat_thick, P_t1[1,1]
    P_t1[3,0], P_t1[3,1] = P_t1[2,0], P_t1[2,1] - (((L2/2)-mat_thick)/3)
    P_t1[4,0], P_t1[4,1] = P_t1[3,0] - mat_thick, P_t1[3,1]
    P_t1[5,0], P_t1[5,1] = P_t1[4,0], P_t1[4,1] - (((L2/2)-mat_thick)/3)
    P_t1[6,0], P_t1[6,1] = P_t1[5,0] + ((L1/2)-(fast_dia/2))/3, P_t1[5,1]
    P_t1[7,0], P_t1[7,1] = P_t1[6,0], P_t1[6,1] - mat_thick
    P_t1[8,0], P_t1[8,1] = P_t1[7,0] + ((L1/2)-(fast_dia/2))/3, P_t1[7,1]
    P_t1[9,0], P_t1[9,1] = P_t1[8,0], P_t1[8,1] + mat_thick
    P_t1[10,0], P_t1[10,1] = P_t1[9,0] + ((L1/2)-(fast_dia/2))/3, P_t1[9,1]
    P_t1[11,0], P_t1[11,1] = P_t1[10,0], P_t1[10,1] + (fast_length-mat_thick-nut_thick)
    P_t1[12,0], P_t1[12,1] = P_t1[11,0] - ((nut_width/2)-(fast_dia/2)), P_t1[11,1]
    P_t1[13,0], P_t1[13,1] = P_t1[12,0], P_t1[12,1] + nut_thick
    P_t1[14,0], P_t1[14,1] = P_t1[13,0] + (nut_width/2), P_t1[13,1]
    
    #Quadrant 2 (lower left)
    P_t1_q2 = np.zeros((15, 2)) #Array of points that define 2 quadrant of a face
    for i in range(len(P_t1)):
        P_t1_q2[i,0] = P_t1[i,0]
        P_t1_q2[i,1] = P_t1[i,1] + 2 * abs(y_t1 - P_t1[i,1])

    #Quadrant 3 (upper right)
    P_t1_q3 = np.zeros((15, 2)) #Array of points that define 3 quadrant of a face
    P_t1_q3[0,0], P_t1_q3[0,1] = x_t1 + (L1/2) - mat_thick, y_t1
    P_t1_q3[1,0], P_t1_q3[1,1] = P_t1_q3[0,0], P_t1_q3[0,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[2,0], P_t1_q3[2,1] = P_t1_q3[1,0] + mat_thick, P_t1_q3[1,1]
    P_t1_q3[3,0], P_t1_q3[3,1] = P_t1_q3[2,0], P_t1_q3[2,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[4,0], P_t1_q3[4,1] = P_t1_q3[3,0] - mat_thick, P_t1_q3[3,1]
    P_t1_q3[5,0], P_t1_q3[5,1] = P_t1_q3[4,0], P_t1_q3[4,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[6,0], P_t1_q3[6,1] = P_t1_q3[5,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[5,1]
    P_t1_q3[7,0], P_t1_q3[7,1] = P_t1_q3[6,0], P_t1_q3[6,1] - mat_thick
    P_t1_q3[8,0], P_t1_q3[8,1] = P_t1_q3[7,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[7,1]
    P_t1_q3[9,0], P_t1_q3[9,1] = P_t1_q3[8,0], P_t1_q3[8,1] + mat_thick
    P_t1_q3[10,0], P_t1_q3[10,1] = P_t1_q3[9,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[9,1]
    P_t1_q3[11,0], P_t1_q3[11,1] = P_t1_q3[10,0], P_t1_q3[10,1] + (fast_length-mat_thick-nut_thick)
    P_t1_q3[12,0], P_t1_q3[12,1] = P_t1_q3[11,0] + ((nut_width/2)-(fast_dia/2)), P_t1_q3[11,1]
    P_t1_q3[13,0], P_t1_q3[13,1] = P_t1_q3[12,0], P_t1_q3[12,1] + nut_thick
    P_t1_q3[14,0], P_t1_q3[14,1] = P_t1_q3[13,0] - (nut_width/2), P_t1_q3[13,1]

    #Quadrant 4 (bottom right)
    P_t1_q4 = np.zeros((15, 2)) #Array of points that define 4 quadrant of a face
    for i in range(len(P_t1_q4)):
        P_t1_q4[i,0] = P_t1_q3[i,0]
        P_t1_q4[i,1] = P_t1_q3[i,1] + 2 * abs(y_t1 - P_t1_q3[i,1])

    #Combine all quadrants
    P_t1_reshape = ' '.join([f"{', '.join(map(str, row))}" for row in P_t1])
    P_t1_q2_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q2]))
    P_t1_q3_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q3]))
    P_t1_q4_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q4]))

    q1 = f'   <polyline points="{P_t1_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q2 = f'   <polyline points="{P_t1_q2_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q3 = f'   <polyline points="{P_t1_q3_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q4 = f'   <polyline points="{P_t1_q4_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    return q1+q2+q3+q4

#Box Face - Type II (Top & Bottom faces) (Qty:2) (faces using Width and Length)
def boxface_t2(x_t2, y_t2): 
    #Inputs are x location and y location
    #Output is svg code that geometrically represents a box face
    
    #Quadrant 1 (upper left)
    P_t2_q1 = np.zeros((11, 2)) #Array of points that define 1 quadrant of a face

    P_t2_q1[0,0], P_t2_q1[0,1] = x_t2 - (length/2), y_t2
    P_t2_q1[1,0], P_t2_q1[1,1] = P_t2_q1[0,0], P_t2_q1[0,1] - width/6
    P_t2_q1[2,0], P_t2_q1[2,1] = P_t2_q1[1,0] + mat_thick, P_t2_q1[1,1]
    P_t2_q1[3,0], P_t2_q1[3,1] = P_t2_q1[2,0], P_t2_q1[2,1] - width/6
    P_t2_q1[4,0], P_t2_q1[4,1] = P_t2_q1[3,0] - mat_thick, P_t2_q1[3,1]
    P_t2_q1[5,0], P_t2_q1[5,1] = P_t2_q1[4,0], P_t2_q1[4,1] - width/6
    P_t2_q1[6,0], P_t2_q1[6,1] = P_t2_q1[5,0] + (length/6), P_t2_q1[5,1]
    P_t2_q1[7,0], P_t2_q1[7,1] = P_t2_q1[6,0], P_t2_q1[6,1] + mat_thick
    P_t2_q1[8,0], P_t2_q1[8,1] = P_t2_q1[7,0] + (length/6), P_t2_q1[7,1]
    P_t2_q1[9,0], P_t2_q1[9,1] = P_t2_q1[8,0], P_t2_q1[8,1] - mat_thick
    P_t2_q1[10,0], P_t2_q1[10,1] = P_t2_q1[9,0] + (length/6), P_t2_q1[9,1]
    
    #Quadrant 2 (bottom left)
    P_t2_q2 = np.zeros((11, 2)) #Array of points that define a quadrant face
    for i in range(len(P_t2_q1)):
        P_t2_q2[i,0] = P_t2_q1[i,0]
        P_t2_q2[i,1] = P_t2_q1[i,1] + 2 * abs(y_t2 - P_t2_q1[i,1])
    
    #Quadrant 3 (upper right)
    P_t2_q3 = np.zeros((11, 2)) #Array of points that define a quadrant face
    P_t2_q3[0,0], P_t2_q3[0,1] = x_t2 + (length/2), y_t2
    P_t2_q3[1,0], P_t2_q3[1,1] = P_t2_q3[0,0], P_t2_q3[0,1] - width/6
    P_t2_q3[2,0], P_t2_q3[2,1] = P_t2_q3[1,0] - mat_thick, P_t2_q3[1,1]
    P_t2_q3[3,0], P_t2_q3[3,1] = P_t2_q3[2,0], P_t2_q3[2,1] - width/6
    P_t2_q3[4,0], P_t2_q3[4,1] = P_t2_q3[3,0] + mat_thick, P_t2_q3[3,1]
    P_t2_q3[5,0], P_t2_q3[5,1] = P_t2_q3[4,0], P_t2_q3[4,1] - width/6
    P_t2_q3[6,0], P_t2_q3[6,1] = P_t2_q3[5,0] - (length/6), P_t2_q3[5,1]
    P_t2_q3[7,0], P_t2_q3[7,1] = P_t2_q3[6,0], P_t2_q3[6,1] + mat_thick
    P_t2_q3[8,0], P_t2_q3[8,1] = P_t2_q3[7,0] - (length/6), P_t2_q3[7,1]
    P_t2_q3[9,0], P_t2_q3[9,1] = P_t2_q3[8,0], P_t2_q3[8,1] - mat_thick
    P_t2_q3[10,0], P_t2_q3[10,1] = P_t2_q3[9,0] - (length/6), P_t2_q3[9,1]

    #Quadrant 4 (bottom right)
    P_t2_q4 = np.zeros((11, 2)) #Array of points that define a quadrant face
    for i in range(len(P_t2_q3)):
        P_t2_q4[i,0] = P_t2_q3[i,0]
        P_t2_q4[i,1] = P_t2_q3[i,1] + 2 * abs(y_t2 - P_t2_q3[i,1])

    #Hole Locations
    HL = np.zeros((4,2)) #Matrix with all hole locations
    EM = mat_thick/2 #Edge Margin of fastener hole to material edge 9this ensures holes are centered on material thickness
    HL[0,0], HL[0,1] = x_t2 - (length/2) + EM, y_t2
    HL[1,0], HL[1,1] = x_t2, y_t2 - (width/2) + EM
    HL[2,0], HL[2,1] = x_t2 + (length/2) - EM, y_t2
    HL[3,0], HL[3,1] = x_t2, y_t2 + (width/2) - EM
    
    #Combine all quadrants
    P_t2_q1_reshape = ' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q1])
    P_t2_q2_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q2]))
    P_t2_q3_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q3]))
    P_t2_q4_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q4]))
    
    q1_2 = f'   <polyline points="{P_t2_q1_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q2_2 = f'   <polyline points="{P_t2_q2_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q3_2 = f'   <polyline points="{P_t2_q3_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q4_2 = f'   <polyline points="{P_t2_q4_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc1 = f'   <circle cx="{HL[0,0]}" cy="{HL[0,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc2 = f'   <circle cx="{HL[1,0]}" cy="{HL[1,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc3 = f'   <circle cx="{HL[2,0]}" cy="{HL[2,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc4 = f'   <circle cx="{HL[3,0]}" cy="{HL[3,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'

    return q1_2+q2_2+q3_2+q4_2+Hole_loc1+Hole_loc2+Hole_loc3+Hole_loc4

#Drawing Each Box Face
#Face 1,2,3,4
f.write(boxface_t1(BL[0,0], BL[0,1], width, height ))
f.write(boxface_t1(BL[1,0], BL[1,1], width, height))
f.write(boxface_t1(BL[2,0], BL[2,1], length, height))
f.write(boxface_t1(BL[3,0], BL[3,1], length, height))
#Face  5 & 6 (Top and Bottom)
f.write(boxface_t2(BL[4,0], BL[4,1]))
f.write(boxface_t2(BL[5,0], BL[5,1]))

#Close code string
f.write(f'</svg>')
f.close()