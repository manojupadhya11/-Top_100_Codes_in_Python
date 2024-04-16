#Python Porgram to find non repeating elements in the user inputted array

arr = [1,2,3,4,5,6,5,4,7,8,9,10,19,10,10,10]

print("The non repeating element in an array are: -")
for i in arr:
    if arr.count(i) == 1:
        print(i)