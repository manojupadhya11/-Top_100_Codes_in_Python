#Python Program to replace all the 0's with 1's in the inserted number
import math
num = int(input("Enter the number "))
num2 = 0

#used if the entered number is 0
if num == 0:
    num2 = 1 

#while loop to find all zeros and replace it with 1
while num > 0:
    rem = int(num%10)
    if rem == 0:
        rem = 1
    num = num//10
    num2 = num2*10+rem  #here note that num2 is in reversed order of num1

#code to reverse the number   
reversed_num = num2
num2 = 0
while reversed_num!=0:
    rem = reversed_num%10
    num2 = num2*10+rem
    reversed_num = reversed_num//10
 
print(num2)