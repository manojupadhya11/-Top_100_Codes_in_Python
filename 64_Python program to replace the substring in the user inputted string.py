#Python program to replace a substring in a user inputted string 
#Replace a substring in a string

string1 = input("Enter a the string  ")

replacing_string = input("Enter the sub string to be replaced  ")
substring = input("Enter the substring to replace in the substring place  ")

string1 = string1.replace(replacing_string, substring)

print("string after replacement")
print(string1)