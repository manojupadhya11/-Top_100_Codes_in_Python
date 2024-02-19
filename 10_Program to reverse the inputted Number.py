#Program to print reverse of inpuitted Numbers.
num = int(input(" Enter a Number "))
reversed_num = 0

while num > 0:
    remainder  = num%10
    reversed_num = reversed_num*10 + remainder
    num = num//10
    
print("The reversed num of inputted number is ", reversed_num)