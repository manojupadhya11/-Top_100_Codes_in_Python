#Program to Calculate Sum of DIgits of a Number

num = int(input("Enter a Number- "))

value_sum = 0;
while(num!=0):
    rem = num%10
    value_sum = value_sum+rem
    num = int(num/10)
    
    
print("The sum of Digits is ", value_sum)