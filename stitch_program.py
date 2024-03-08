# Embroidery Code
# M. Plavcan

#Reference
# 246 is the usigned 8-bit version of -10

#import Libraries
import numpy as np
import math

#Initialize Stitch Code
stitch = [128, 2, # 128 = escape_character , 2=Move
            0, 0, # followed by 8 bit displacement X,Y
          206, 206,] # followed by 8 bit displacement X,Y

#User Inputs
#color = input('Input Color ')

#Commands to draw stitch pattern
#Shape Functions
def square(x):
    #Square function 
    x = [10, 0, 0, 10, 246, 0, 0, 246, 10, 0,]
    return x

'''
#Quadrant I [-x, +y]
for i in range(0, iter):
    x1q1=r*math.cos(theta*i)
    x2q1=r*math.cos(theta*(i+1))
    y1q1=r*math.sin(theta*i)
    y2q1=r*math.sin(theta*(i+1))
    stitch += [abs(round(256-(x1q1-x2q1))), abs(round(y1q1-y2q1)),]
print(stitch)

#Quadrant II [-x, -y]
for i in range(0, iter):
    x1q2=r*math.cos(theta*i)
    x2q2=r*math.cos(theta*(i+1))
    y1q2=r*math.sin(theta*i)
    y2q2=r*math.sin(theta*(i+1))
    stitch += [abs(round((x1q2-x2q2))), abs(round((y1q2-y2q2))),]
'''

stitch += square(stitch)
stitch += [128, 1] #128 = escape_character -> 1 = Change to next thread in list (see lines 81, 104 & 105)
stitch += [128, 2] #128 = escape_character , 2 = Move
stitch += [100, 100] #followed by 8 bit displacement X,Y
stitch += square(stitch)
stitch += [128, 16] #"Last stitch" command code
print(stitch)

'''
#Quadrant III [+x, -y]
for i in range(0, 10):
    stitch += [abs(round(r*math.cos(theta*i))), abs(round(r*math.sin(theta*i)-256)),]

#Quadrant IV [+x, +y]
for i in range(0, 10):
    stitch += [abs(round(r*math.cos(theta*i))), abs(round(r*math.sin(theta*i))),]
print(stitch)

#Commands to stitch square
#for i in range(0, 10):
    #stitch += [10, 0,]
#for i in range(0, 10):
    #stitch += [0, 10,]
#for i in range(0, 10):
    #stitch += [246, 0,]
#for i in range(0, 10):
    #stitch += [0, 246,]
'''

#Commands to condition file format 
jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
            10, 0, 0, 0,    # Unknown number
            ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
            ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0,  # SS00
                2, 0, 0, 0, # Number of physical thread colors (2) (can change this)
            (len(stitch)//2) & 0xff, (len(stitch)//2) >> 8 & 0xff, 0, 0, # Number of stitches
            3, 0, 0, 0,     # Sewing machine hoop (3 = F Spring Loaded)           
			50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
            50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
            5, 0, 0, 0,    # Thread Color (Green Dust)
            2, 0, 0, 0,    # Thread Color (white)
            13, 0, 0, 0,   # Unknown number
            ] + stitch

jefBytes = bytes(jefBytes)
with open("stitch_pattern.jef", "wb") as f:
    f.write(jefBytes)