#Program to find the Factorial of a Number 

number = int(input("Enter a Number "))

factorial = 1
print("The Factoorial of ",number," is:-")
for i in range (1, number+1):
    factorial = factorial*i
    

print(factorial)

