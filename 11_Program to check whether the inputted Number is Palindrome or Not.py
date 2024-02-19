#Program to check whether the inputted number is palindrome or not
num = int(input(" Enter a Number "))
num2 = num
reversed_num = 0

while num > 0:
    remainder  = num%10
    reversed_num = reversed_num*10 + remainder
    num = num//10

if reversed_num == num2:
    print("The inputted number ", num2, " is Palindrome Number ")
else: 
    print("The inputted number ", num2, " is not palindrome")