#Python Program to check whether user inputted number is prime or not

def checkprime(n, i=2):
    if n <=1:
        return False
    if n==i:
        return True
    elif n%i == 0:
        return False
    
    return checkprime(n, i+1)


num = int(input("Enter a Number "))
if checkprime(num):
    print(num,"is a Prime Number ")
else:
    print(num, "is not a prime Number ")