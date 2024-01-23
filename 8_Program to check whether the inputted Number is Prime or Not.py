#Program to check whether the inputted Number is prime or not

num = int(input("Enter the Number "))
flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1
        break;
if flag == 1:
    print("Not Prime Number")
else:
    print("Prime number")
