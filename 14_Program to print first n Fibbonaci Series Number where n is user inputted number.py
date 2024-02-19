#Program to print first n Fibbonaci Series numbers where n is user inputted number

number = int(input("Enter a Number "))

num1 = 0
num2 = 1
print("The Fibbonaci Series is:-", num1, num2, end = " ")
for i in range (2, number):
    num3 = num2+num1
    num1 = num2
    num2 = num3
    print(num3, end = " ")
    
    
