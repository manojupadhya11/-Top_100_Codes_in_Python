#Python program to find the length of user inputted character without using builtin function (len())

str = input("Enter a String  ")
count = 0
for i in str:
    count = count+1 
    
    
    
print("The length or number of characters in the string", str, " is ",count)