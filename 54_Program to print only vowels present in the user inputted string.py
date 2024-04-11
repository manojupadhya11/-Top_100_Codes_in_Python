#Python program to remove the all consonants from the user inputted string

str_1 = input("Enter a String ")
str_2 = ' '

for i in str_1:
    #if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
        str_2+=i
        

print(str_2)

    
