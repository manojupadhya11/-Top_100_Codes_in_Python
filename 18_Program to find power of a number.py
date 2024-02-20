#Program to find power of Given number 
number =  int(input("Enter a number "))
power = int(input("Enter the power "))

sum = pow(number, power)
print(sum)
print(" ")


output_sum = 1 
for i in range(power):
    output_sum*=number
print("Output Using Iterator")
print(output_sum)

#using python operator
print("Output using python operator")
print(number**power)