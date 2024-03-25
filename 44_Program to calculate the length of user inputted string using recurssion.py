#Program to calculate the length of a string using recursion

def length(str):
    if str == "":
        return 0
    return 1 + length(str[1:])
        

str = input("Enter a String ")
print(length(str))
