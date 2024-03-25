#Program to find second smallest in the user inputted array
arr = [10,20,30,4,5,7,3,7,8,9,13,122,456,789]


sec_smallest  = arr[1]
smallest = arr[1]

for i in range(1,len(arr)):
        if arr[i] < smallest:
            sec_smallest = smallest
            smallest = arr[i]
        
print("The Second Smallest element in the given array is :",sec_smallest)        
print("The smallest element in the array is :",smallest)
        