#Python progra, to find the inputted number is Automorphic number or not 
'''
Automorphic Number
A number whose square ends with the same number is known as an Automorphic number.
Let's try and understand it even better using an example ,

Example
Input : number = 5
Output : It's an Automorphic number.
Explanation : Number = 5
Square of number = 25
as the square of the number ends with the number itself, It's an Automorphic number.
Therefore, for a number to be Automorphic it number have a square that ends with the number itself.
'''

num = int(input("Enter a Nummber to check whether the inutted Number is Auromorphic Number or not "))
square = pow(num, 2)

#Modulus Operator
mod = pow(10, len(str(num)))

if square%mod == num:
    print(num,"is an Auromorphic Number ")
else:
    print(num, "is not an Automorphic Number")