#Python program to print all the non repeating characters in user inputted string 

string = input("Enter a String ")

count = 0

for i in string:
    count = 0
    for j in string:
        if i == j:
            count += 1 
        if count > 1:
            break;
    if count == 1:
        print(i)