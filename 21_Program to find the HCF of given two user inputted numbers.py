#Python program to find the HCF of given two numbers


num1 = int(input("Enter a Nummber 1 "))
num2 = int(input("Enter a Nummber 2 "))

hcf  = 1

for i in range (1, min(num1,num2)):
    if num1%i==0 and num2%i==0:
        hcf = i

print("HCF of ",num1, " and ", num2, " is ",hcf)
