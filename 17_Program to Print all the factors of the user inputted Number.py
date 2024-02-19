#Program to find the Factors of a Number 

number = int(input("Enter a Number "))
i = 1
print("The Factors of ",number," is:-")
while i<=number:
    if(number % i == 0):
        print(i, end = " ")
    i = i+1


