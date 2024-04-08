#Python Program to take user input String and calculate the number of vowels present in the String

#User input
 
user_str = input("Enter a String ")

count = 0

#to check less conditions make string to lower case 
user_str = user_str.lower()

#checcking conditions
for i in user_str:
    if i == 'a' or i =='e' or i =='o' or i== 'u':
        count = count+1 
        

if count == 0:
    print("No vowel presnet in the given string")
else:
    print("The number of vowel present in user inputted string is :- ", count)