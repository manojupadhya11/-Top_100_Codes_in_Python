#Program to find whether inputted number is perfect number or not
number =  int(input("Enter a number "))
sum = 0
num = number
for i in range(1, num):
    if num% i ==0:
        sum = sum+i
        
if sum == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")