#Program to calculate number of occurence of a user inputted digit in user inputted number

def findoccurence(num, digit):
    count = 0
    while(num>0):
        if(num%10 == digit):
            count += 1
        
        num = num//10
        
    
    return count
    
    
    
number  = int(input("Enter a number  "))

digit = int(input("Enter a digit whose occurence you want to find "))

print("The ",digit," occuring ", findoccurence(number, digit), "times in the number ", number)


