#Python program to find the GCD of two numbers


num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

while num2:
    num1,num2 = num2, num1%num2

print("GCD:", num1)