#Python program to check whether user inputted character is an alphabet or not 
#programming using ascii values


ch = input("Enter a character ")

cha = ord(ch)

if  97 <= cha <= 122 or  65<= ch <= 90:
    print(ch," is an alphabet")
else:
    print(ch, " is not an alphabet")