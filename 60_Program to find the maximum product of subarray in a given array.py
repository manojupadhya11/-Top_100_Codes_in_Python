#Python program to find the maximum product of sub array in a given array 


def maxsubarra(array,n):
    
    result = array[0]
    
    
    for i in range(n):
        
        mul = array[i]
        
        for j in range(i+1, n):
            result = max(result, mul)
            mul *= array[j]
            
        result = max (result, mul)
        
    return result
        


array = [ 1, -2, -3, 0, 7, -8, -2 ]
# [1,2,3,4,5,6,7,8,9,10]
n = len(array)

print(maxsubarra(array,n))