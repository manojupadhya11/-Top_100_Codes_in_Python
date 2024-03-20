#Program to print all the prime numbers in between 1 and n

def checkprime(num):
    if num < 2:
        return 0
    else:
        x = num//2
        for i in range (2, x+1):
            if (num%i ==0):
                return 0
    
    
    return 1 
    
print("Program to Print Prime numbers between 1 and N")

number  = int(input("Enter the value of n "))
print("The prime numbers between 1 and ",number, " are :- ")
print()
for x in range(1, number):
    if checkprime(x):
        print(x, end = " ")
        
        