#Python Program to calculate the frequency of characters in the user inputted String 

string = input("Enter a string " )

for i in string:
    frequency = string.count(i)
    print(str(i)," occurs ",str(frequency),"time in the ", string)