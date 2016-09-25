# PROBLEM 1
# Implement an algorithm to determine if a string has all unique characters.

# using a dictionary to cache characters
def is_unique1(my_string):   
    cache = {}
    
    # loop through string, checking cache for each char
    for char in my_string:
        if char in cache:
            return False
        else:
            cache[char] = 1

    return True
    
# using a set
def is_unique2(my_string):
    my_set = set(my_string)
    
    if len(my_string) != len(my_set): 
        return False
    
    return True
    
# What if you cannot use additional data structures?

# for each char, check chars to the right
def is_unique3(my_string):    
    for i, char in enumerate(my_string):
        if char in my_string[i+1:]:
            return False
    return True
    

# PROBLEM 2
# Implement a function to reverse a string

# work from the edges inwards
def reverse1(my_string):
    left = 0
    right = len(my_string) - 1
    
    # strings are immutable, so store elements in list and join later
    new_string = list(my_string) 

    while left < right:
        new_string[left] = my_string[right]
        new_string[right] = my_string[left]

        left += 1
        right -= 1
        
    return ''.join(new_string)

# using reversed
def reverse2(my_string):
    return ''.join(reversed(my_string))
    
# python way
def reverse3(my_string):
    return my_string[::-1]
    
    
# PROBLEM 3
# Given two strings, write a method to decide if one is a permutation of the other

def is_permute1(string1, string2):
        

TEST_DATA = [
    'Ryan',
    'Ryaaan',
    'ABCDE',
    'ABCDAAA',
    'AAB',
    'TESTING',
    'GOOGLE',
    'uniqe',
    'unique']
    
for test in TEST_DATA:
    print reverse1(test), reverse2(test), reverse3(test)
