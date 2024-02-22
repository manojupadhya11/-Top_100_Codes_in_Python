#Python program to find the LCM of given two numbers (Lowest common multiple)


num1 = int(input("Enter a Nummber 1 "))
num2 = int(input("Enter a Nummber 2 "))

hcf  = 1

for i in range (1, min(num1,num2)):
    if num1%i==0 and num2%i==0:
        hcf = i


lcm = num1*num2//hcf
print("LCM of ",num1, " and ", num2, " is ",lcm)
