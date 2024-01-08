#Program to find greatest of three Numbers


a = int(input("Enter value for a "))
b = int(input("Enter Value for b "))
c = int(input("Enter value for c "))
if a == b == c:
    print("All three inputted numbers are equal")
elif( a > b and a > c):
    print(a,"Value Present in a is greatest")
elif( b > a and b > c):
    print(b,"Value Present in b is greatest")
elif(c > a and c > b):
        print(c,"Value Present in c is greatest")
        
