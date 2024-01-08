#Program to find sum of first "n" Natural Numbers


num = int(input("Enter a Number "))
sum = 0
for i in range(num+1):
    sum = sum+i
    
print(sum)
