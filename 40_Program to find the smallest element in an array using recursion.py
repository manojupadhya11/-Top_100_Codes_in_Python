#Python Program to find smallest element in the array using recurssion

def largest_element(A,n):
    if n==1:
        return A[0]
    else:
        return min(A[n-1], largest_element(A, n-1) )

A = [10,20,30,50,6,7,8,9,1,2,3,4]
n = len(A)
print(largest_element(A,n))