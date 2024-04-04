#Python program to check whether user inputted character is an alphabet or not 
#general programming

ch = input("Enter a character ")

if  "a" <= ch <= "z" or "A" <= ch <= "Z":
    print(ch," is an alphabet")
else:
    print(ch, " is not an alphabet")