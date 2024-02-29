#Program to determine the quadrants of user inputted coordinates.

#user input for coordinates


x = int(input("Enter the value of X "))
y = int(input("Enter the value of Y "))


#Checking on which quadrants the coordinates present

if( x == 0 ) and (y == 0):
    print("(",x,y,") falls on origin" )
elif (x>0 ) and ( y>0 ):
    print("(",x,y,") present in First Quadrants")
elif(x>0) and (y<0):
    print("(",x,y,") present in Second Quadrant")
elif(x<0) and (y<0):
    print("(",x,y,") present in Third Quadrant")
else:
    print("(",x,y,") Present in Fourth Quadrant")
    