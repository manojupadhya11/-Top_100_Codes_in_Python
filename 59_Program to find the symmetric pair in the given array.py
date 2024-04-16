#Python program to find the symmetric pair *in the given array of pairs
'''
We are given with pairs, some symmetric pairs are exists in the given set of pairs. The problem statement says that we have to find all symmetric pairs that exist
Example,
Input : arr[5][2] = {{10,20}, {30,40}, {50,60}, {20,10}, {40,30}, {90, 100}, {1, 9}, {100, 90}}
Output : (10,20) (30,40) (90, 100)

(10,20) and (20,10) presen in the given array then it is a symmeteric pair


Set in Python
Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
Python's set class represents the mathematical notion of a set.
'''

def findpair(pairs):
    s = set()
    
    for (x,y) in pairs:
        
        s.add((x,y))
        
        if (y,x) in s:
            print((x,y))
        
# pairs = [(10,20),(20,30),(20,10)]
pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
findpair(pairs)
    
    
    