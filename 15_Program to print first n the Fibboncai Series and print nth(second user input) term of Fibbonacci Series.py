#Program to print first n Fibbonaci Series numbers where n is user inputted number

number = int(input("Enter a Number "))
arr = []
num1 = 0
num2 = 1
arr.append(num1)
arr.append(num2)
print(arr)
print("The Fibbonaci Series is:-")
for i in range (2, number):
    num3 = num2+num1
    num1 = num2
    num2 = num3
    arr.append(num3)
print(arr)
    
num = int(input("Enter the value of n to find Nth term in fibbonaci Series "))
print(arr[num-1])
    
