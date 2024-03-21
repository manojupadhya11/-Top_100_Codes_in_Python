#Python Program to calculate the power of a number using recursion


def power(a,b):
    if b!=0:
        return a*power(a, b-1)
    else:
        return 1
        
        
        
a  =  int(input("Enter the value for a "))
b = int(input("Enter the value for b "))

power_value = power(a,b)
print(a, "to the power",b," is :- ",power_value)