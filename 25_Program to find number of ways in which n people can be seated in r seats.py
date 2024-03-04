#Python Program to find in how many ways n people can occupy r seats in a classroom

def factorial(num):
    fact = 1 
    for i in range(num, 1, -1):
        fact = fact*i
    return fact    

n = int(input("Enter the number of people "))
r = int(input("Enter total number of available seats "))

num = factorial(n)//factorial(n-r)
print(n," people can occupy ",r," seats in ",num, " Ways")