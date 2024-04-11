#Python program to calculate the sum of all numbers present in the user inputted String

str_1 = input("Enter a String containing numbers ")

sum = 0

for i in str_1:
    if ord(i) >= 48 and ord(i) <= 57:
        sum+= int(i)
        
        


print(sum)
        

    
