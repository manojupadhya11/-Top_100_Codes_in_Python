#Program to check whether the inputted number is Armstrong number or not
#example 371 == 3^3 + 7^3 + 1^3

num = int(input("Enter a Number to check whether it is Armstrong or Not "))
num2 = num
digit = 0
Armstrong_num = 0

size = len(str(num))

while num > 0:
    remainder  = num%10
    num = num//10
    Armstrong_num +=  pow(remainder,size) 


if Armstrong_num == num2:
    print("The inputted number ", num2, " is Armstrong Number ")
else: 
    print("The inputted number ", num2, " is not an Armstrong Number ")