#Laser Cut Box Project #1
#Max Plavcan

#Outline
#Input Parameters
    #1. Box Dimensions (l x w x h)
    #2. Material Thickness
    #3. Fastener diameter
    #4. Fastener length
    #5. Nut width
    #6. Nut thickness
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
        mat_thick = int(input("Enter your box wall thickness(mm): "))
        fast_dia = int(input("Enter your box fastener diameter(mm): "))
        fast_length = int(input("Enter your fastener length(mm): "))
        nut_width = int(input("Enter your fastener nut width(mm): "))
        nut_thick = int(input("Enter your fastener nut thickness(mm): "))
        #engrave = 
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

#Margins of Box Outline
w_marg = 40 #width margin
l_marg = 40 #length margin

#Positioning of Box Faces
BL = np.zeros((6,2)) #Matrix with all values
#Face 1
BL[0,0], BL[0,1] = width/2 + w_marg, length/2 + l_marg
#Face 2
BL[1,0], BL[1,1] = BL[0,0] + width + w_marg, BL[0,1]
#Face 3
BL[2,0], BL[2,1] = BL[1,0] + width + w_marg, BL[1,1]
#Face 4
BL[3,0], BL[3,1] = BL[0,0], BL[0,1] + length + l_marg
#Face 5 (TOP)
BL[4,0], BL[4,1] = 0, 0
#Face 6 (BOTTOM)
BL[5,0], BL[5,1] = 0, 0

#Box Face - Type I (Circumferential) (Qty:4)
def boxface_t1(x_t1, y_t1): 
    #Inputs are Length, Width, x location and y location
    #Output is svg code that geometrically represents a box face
    #Quadrant 1 (upper left)
    P_t1 = np.zeros((15, 2)) #Array of points that define 1 quadrant of a face
    P_t1[0,0], P_t1[0,1] = x_t1 - (width/2), y_t1
    P_t1[1,0], P_t1[1,1] = P_t1[0,0], P_t1[0,1] - (((length/2)-mat_thick)/3)
    P_t1[2,0], P_t1[2,1] = P_t1[1,0] + mat_thick, P_t1[1,1]
    P_t1[3,0], P_t1[3,1] = P_t1[2,0], P_t1[2,1] - (((length/2)-mat_thick)/3)
    P_t1[4,0], P_t1[4,1] = P_t1[3,0] - mat_thick, P_t1[3,1]
    P_t1[5,0], P_t1[5,1] = P_t1[4,0], P_t1[4,1] - (((length/2)-mat_thick)/3)
    P_t1[6,0], P_t1[6,1] = P_t1[5,0] + ((width/2)-(fast_dia/2))/3, P_t1[5,1]
    P_t1[7,0], P_t1[7,1] = P_t1[6,0], P_t1[6,1] - mat_thick
    P_t1[8,0], P_t1[8,1] = P_t1[7,0] + ((width/2)-(fast_dia/2))/3, P_t1[7,1]
    P_t1[9,0], P_t1[9,1] = P_t1[8,0], P_t1[8,1] + mat_thick
    P_t1[10,0], P_t1[10,1] = P_t1[9,0] + ((width/2)-(fast_dia/2))/3, P_t1[9,1]
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
    P_t1_q3[0,0], P_t1_q3[0,1] = x_t1 + (width/2) - mat_thick, y_t1
    P_t1_q3[1,0], P_t1_q3[1,1] = P_t1_q3[0,0], P_t1_q3[0,1] - (((length/2)-mat_thick)/3)
    P_t1_q3[2,0], P_t1_q3[2,1] = P_t1_q3[1,0] + mat_thick, P_t1_q3[1,1]
    P_t1_q3[3,0], P_t1_q3[3,1] = P_t1_q3[2,0], P_t1_q3[2,1] - (((length/2)-mat_thick)/3)
    P_t1_q3[4,0], P_t1_q3[4,1] = P_t1_q3[3,0] - mat_thick, P_t1_q3[3,1]
    P_t1_q3[5,0], P_t1_q3[5,1] = P_t1_q3[4,0], P_t1_q3[4,1] - (((length/2)-mat_thick)/3)
    P_t1_q3[6,0], P_t1_q3[6,1] = P_t1_q3[5,0] - ((width/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[5,1]
    P_t1_q3[7,0], P_t1_q3[7,1] = P_t1_q3[6,0], P_t1_q3[6,1] - mat_thick
    P_t1_q3[8,0], P_t1_q3[8,1] = P_t1_q3[7,0] - ((width/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[7,1]
    P_t1_q3[9,0], P_t1_q3[9,1] = P_t1_q3[8,0], P_t1_q3[8,1] + mat_thick
    P_t1_q3[10,0], P_t1_q3[10,1] = P_t1_q3[9,0] - ((width/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[9,1]
    P_t1_q3[11,0], P_t1_q3[11,1] = P_t1_q3[10,0], P_t1_q3[10,1] + (fast_length-mat_thick-nut_thick)
    P_t1_q3[12,0], P_t1_q3[12,1] = P_t1_q3[11,0] + ((nut_width/2)-(fast_dia/2)), P_t1_q3[11,1]
    P_t1_q3[13,0], P_t1_q3[13,1] = P_t1_q3[12,0], P_t1_q3[12,1] + nut_thick
    P_t1_q3[14,0], P_t1_q3[14,1] = P_t1_q3[13,0] - (nut_width/2), P_t1_q3[13,1]

    #Quadrant 4 (upper right)
    P_t1_q4 = np.zeros((15, 2)) #Array of points that define 4 quadrant of a face
    for i in range(len(P_t1_q4)):
        P_t1_q4[i,0] = P_t1_q3[i,0]
        P_t1_q4[i,1] = P_t1_q3[i,1] + 2 * abs(y_t1 - P_t1_q3[i,1])

    #Combine all quadrants
    P_t1_reshape = ' '.join([f"{', '.join(map(str, row))}" for row in P_t1])
    P_t1_q2_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q2]))
    P_t1_q3_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q3]))
    P_t1_q4_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q4]))

    q1 = f' <polyline points="{P_t1_reshape}" stroke="black" stroke-width="2" fill="none" /> \n'
    q2 = f' <polyline points="{P_t1_q2_reshape}" stroke="black" stroke-width="2" fill="none" /> \n'
    q3 = f' <polyline points="{P_t1_q3_reshape}" stroke="black" stroke-width="2" fill="none" /> \n'
    q4 = f' <polyline points="{P_t1_q4_reshape}" stroke="black" stroke-width="2" fill="none" /> \n'
    return q1+q2+q3+q4

#Box Face - Type II (Top & Bottom faces) (Qty:2)
#Drawing Each Box Face
#Face 1,2,3,4
f.write(boxface_t1(BL[0,0], BL[0,1]))
f.write(boxface_t1(BL[1,0], BL[1,1]))
f.write(boxface_t1(BL[2,0], BL[2,1]))
f.write(boxface_t1(BL[3,0], BL[3,1]))
#Face  5 & 6 (Top and Bottom)
#f.write(boxface_t2(BL[4,0], BL[4,1]))
#f.write(boxface_t2(BL[5,0], BL[5,1]))

#Close code string
f.write(f'</svg>')
f.close()