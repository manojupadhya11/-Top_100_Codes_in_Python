#Program to print all the Armstrong Number in the user inputted Range
#example 371 == 3^3 + 7^3 + 1^3
print("----Program to Print all the Armstrong Number in the user inputted Range----")

num1 = int(input("Enter the Lower Range "))
num2 = int(input("Enter The Upper Range "))


for i in range (num1, num2):
    digit = 0
    Armstrong_num = 0
    num3 = i

    size = len(str(i))

    while i > 0:
        remainder  = i%10
        i= i//10
        Armstrong_num +=  pow(remainder,size) 


    if Armstrong_num == num3:
        print(num3," ")
