#Program to find sum of numbers in given range


lowrange = int(input("Enter Lower Range Value "))
highrange =  int(input("Enter Higher Range Value "))
sum = 0
for i in range(lowrange, highrange+1):
    sum = sum+i
    
print(sum)
