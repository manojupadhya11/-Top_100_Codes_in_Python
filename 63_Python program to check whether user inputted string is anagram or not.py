#Python program to check the two strings are anagram or not
"""
Anagram program in python is when strings share the same no of characters and also the same characters then strings are called anagrams. 
The rearrangement of similar characters or letters in a string even if they don’t have the same meanings are anagrams. 
Only one strict rule is followed if we create anagrams of a string ‘count of every character available in the 1st string should be equal 
to the count of characters in the 2nd string for the same character."""

string1 = input("Enter a first String ")
string2 = input("Enter a Second String ")

string1 = sorted(string1.lower())
string2 = sorted(string2.lower())

print("String 1 after Sorting", string1)
print("String 2 after Sorting", string2)


if string1 == string2:
    print("The both user inputted strings are anagram")
else:
    print("The user inputted strings are not an anagram")