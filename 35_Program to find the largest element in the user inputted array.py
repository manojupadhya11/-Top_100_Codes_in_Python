#Python Program to find the largest element in the user inputted array
''' In Python we can use List data structure instead of array as we dont have array in python'''


array = [10,20,30,40,80,50,100,1,2,3,4]
max = 0
for i in range(1, len(array)):
    if array[i] > max:
        max = array[i]

print("The largest value in the given array is ",max)
    