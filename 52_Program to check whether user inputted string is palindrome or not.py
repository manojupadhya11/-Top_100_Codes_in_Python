#Python program to check whether the user inputted string is palindrome or not

str_1 = input("Enter a String ")

rev_str = str_1[::-1]

if str_1 == rev_str:
    print(str_1, "is a palindrome string")
else:
    print(str_1," is not a palindrome string")
    
