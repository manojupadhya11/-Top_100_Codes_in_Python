#Program to find the sum of elements present in array
arr = [1,2,3,4,5,6,7,8,9,10]


sum_array = 0;

for i in range(0,len(arr)):
    sum_array = sum_array+arr[i]
        
print("The Sum of the element present in array is :- ", sum_array)