#Program to reverse and print the user inputted array  
arr = [1,2,3,4,5,6,7,8,9,10]


print("The reverse of given user Inputted array" )


print(arr[::-1])


#Second Approach

def reverseList(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        
        start = start+1 
        end = end-1 

reverseList(arr,0, len(arr)-1)
print(arr)

