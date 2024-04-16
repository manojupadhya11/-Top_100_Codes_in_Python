#Python Porgram count the number of even and odd elements in the given  array 

array = [10,20,35,6,7,8,9,1,3,44,56,7,9]
n = len(array)
count1 = count2 = 0 
for i in range(0,n):
    if array[i] % 2 == 0:
        count1 = count1+1
        
    else:
        count2 = count2+1 

print("The total count of odd number in array is : - ", count2)
print("Thw total count of even number in array is :- ", count1)