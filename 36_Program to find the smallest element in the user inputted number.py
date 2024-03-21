#Python Program to find the smallest element in the user inputted array
''' In Python we can use List data structure instead of array as we dont have array in python'''


array = [10,20,30,40,80,50,100,1,2,3,4]
min = array[0]
for i in range(1, len(array)):
    if array[i] < min:
        min = array[i]

print("The smallest value in the given array is ",min)
    