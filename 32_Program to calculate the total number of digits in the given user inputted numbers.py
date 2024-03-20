#Program to calculate number of digits in the user inputted number

def countdigit(number):
    digit = 0
    while(number!=0):
        digit += 1
        number = number // 10
    
    return digit
    


number = int(input("Enter the value for number "))

print("The number of digits present in the ", number, " is :- ", countdigit(number))