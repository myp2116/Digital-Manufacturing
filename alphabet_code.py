
#Initiate code vector
stitch = [128, 2, # 128 = escape_character , 2=Move
            0, 0, # followed by 8 bit displacement X,Y
          2, 2,] # followed by 8 bit displacement X,Y

# Function to draw words in jef format
def word_func(stitch_let, text):
#line path of each letter is shown below
    space = 10 #defines space between letters
    for i in range(len(text)):
        if text[i] == "A":
            stitch_let += [0, 0,]
            stitch_let += [50, 100,]
            stitch_let += [50, 156,] 
            stitch_let += [231, 50,]  
            stitch_let += [206, 0,]
            stitch_let += [128,2,] #return to zero
            stitch_let += [0,0,] #return to zero
            stitch_let += [231,206,] #return to zero  
        elif text[i] == "B":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 231,] 
            stitch_let += [156, 231,]  
            stitch_let += [100, 231,]
            stitch_let += [156, 231,] #returned to zero  
        elif text[i] == "C":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,] 
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 156,]
            stitch_let += [100,0,]  
            stitch_let += [128,2,] #return to zero 
            stitch_let += [0,0,] #return to zero 
            stitch_let += [156,0,] #return to zero 
        elif text[i] == "D":
            stitch_let += [0, 0,]
            stitch_let += [0,100,]
            stitch_let += [100, 206,] 
            stitch_let += [156, 206,] #returned to zero
        elif text[i] == "E":
            stitch_let += [0, 0,]
            stitch_let += [0, 50,]
            stitch_let += [100, 0,] 
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 0,]
            stitch_let += [0, 50,]
            stitch_let += [100, 0,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 156,]
            stitch_let += [100, 0,]
            stitch_let += [128,2,] #return to zero
            stitch_let += [0,0,]  #return to zero
            stitch_let += [156,0,]  #return to zero
        elif text[i] == "F":
            stitch_let += [0, 0,]
            stitch_let += [0, 50,]
            stitch_let += [100, 0,] 
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 0,]
            stitch_let += [0, 50,]
            stitch_let += [100, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zero
        elif text[i] == "G":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,] 
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 156,]
            stitch_let += [100, 0,]
            stitch_let += [0, 50,]
            stitch_let += [206, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [206, 206,] #return to zero
        elif text[i] == "H":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [100, 156,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 206,]
            stitch_let += [156, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 206,] #return to zero
        elif text[i] == "I":
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [50, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128,2]  #return to zero
            stitch_let += [0,0]  #return to zero
            stitch_let += [206,156]  #return to zero
        elif text[i] == "J":
            stitch_let += [0, 0,]
            stitch_let += [0, 25,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 231,]
            stitch_let += [100, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zero
        elif text[i] == "K":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 206,]
            stitch_let += [100, 50,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 206,]
            stitch_let += [100, 206,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 0,] #return to zero
        elif text[i] == "L":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 156,]
            stitch_let += [100, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 0,] #return to zero
        elif text[i] == "M":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [50, 156,]
            stitch_let += [50, 100,]
            stitch_let += [0, 156,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 0,] #return to zero 
        elif text[i] == "N":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 156,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zero
        elif text[i] == "O":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,]
            stitch_let += [0, 156,]
            stitch_let += [156, 0,] #returned to zero
        elif text[i] == "P":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,]
            stitch_let += [0, 206,]
            stitch_let += [156, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 206,] #return to zero
        elif text[i] == "Q":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,]
            stitch_let += [0, 156,]
            stitch_let += [156, 0,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [100, 0,]
            stitch_let += [231, 25,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [181, 231,] #return to zero
        elif text[i] == "R":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [100, 0,]
            stitch_let += [0, 206,]
            stitch_let += [156, 0,]
            stitch_let += [100, 206,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 0,] #return to zero 
        elif text[i] == "S":
            stitch_let += [0, 0,]
            stitch_let += [100, 0,]
            stitch_let += [0, 50,]
            stitch_let += [156, 0,]
            stitch_let += [0, 50,]
            stitch_let += [100, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zero
        elif text[i] == "T":
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [50, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [50, 0,]
            stitch_let += [156, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 156,] #return to zero 
        elif text[i] == "U":
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 156,]
            stitch_let += [100, 0,]
            stitch_let += [0, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zerO
        elif text[i] == "V":
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [50, 0,]
            stitch_let += [50, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [206, 156,]
            stitch_let += [206, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 156,] #return to zero 
        elif text[i] == "W":
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 100,]
            stitch_let += [25, 156,]
            stitch_let += [25, 100,]
            stitch_let += [25, 156,]
            stitch_let += [25, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [156, 156,] #return to zero
        elif text[i] == "X":
            stitch_let += [0, 0,]
            stitch_let += [100, 100,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [0, 156,]
            stitch_let += [156, 100,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 156,] #return to zero 
        elif text[i] == "Y":
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [50, 0,]
            stitch_let += [0, 50,]
            stitch_let += [50, 50,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [206, 206,]
            stitch_let += [206, 50,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 156,] #return to zero
        elif text[i] == "Z":
            stitch_let += [0, 0,]
            stitch_let += [100, 0,]
            stitch_let += [128, 2,]
            stitch_let += [0, 0,]
            stitch_let += [156, 0,]
            stitch_let += [100, 100,]
            stitch_let += [156, 0,]
            stitch_let += [128, 2,] #return to zero
            stitch_let += [0, 0,] #return to zero
            stitch_let += [0, 156,] #return to zero 
        elif text[i] ==" ":
            stitch_let += [128,2,]
            stitch_let += [0,0,]
            stitch_let += [100,0,]
        else:
            return print("ERROR, PLEASE ENTER A LETTER FROM A-Z ")
        #Add space between letters
        stitch_let += [128,2,]
        stitch_let += [0,0,]
        stitch_let += [100 + space, 0,]

    return stitch_let

#Test code
usertext = input("Insert your name (in all caps): ")
word_func(stitch, usertext)

stitch += [128, 16] #"Last stitch" command code

#Commands to condition file format 
jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
            10, 0, 0, 0,    # Unknown number
            ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
            ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
            ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
            ord("0"), ord("0"), 99, 0,  # SS00
                2, 0, 0, 0, # Number of physical thread colors (2) (can change this)
            (len(stitch)//2) & 0xff, (len(stitch)//2) >> 8 & 0xff, 0, 0, # Number of stitches
            3, 0, 0, 0,    # Sewing machine hoop (3 = F Spring Loaded)           
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
            2, 0, 0, 0,    # Thread Color (white)
            5, 0, 0, 0,    # Thread Color (Green Dust)
            13, 0, 0, 0,   # Unknown number
            ] + stitch

jefBytes = bytes(jefBytes)
with open("WORD_TEST.jef", "wb") as f:
    f.write(jefBytes)