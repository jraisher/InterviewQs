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

# (Jordan): This would work, (and great job with using the 'enumerate' builtin)
# but it's not quite optimal.  The reason for this is that the 'in' keyword
# iterates over the string to check for the existence of that character.  This
# algorithm, therefore, is O(n^2) rather than the optimal solution which is
# O(nlogn).
#
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

# using a dict to store chars
def is_permute(str1, str2):
    # length check
    if len(str1) != len(str2):
        return False
    
    letters = {} 
    
    # loop through first string
    for letter in str1:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    # loop through second string
    for letter in str2:
        if letter in letters:
            letters[letter] -= 1
            if letters[letter] < 0:
                return False
        else:
            return False
    
    # all 0 => permutation
    for val in letters.values():
        if val != 0:
            return False
			
    return True


# PROBLEM 4
# Write a method to replace all spaces in a string with %20

# (Jordan): Try doing this one again without any python built-ins like 'join'
# or 'replace'.  Also, I'd suggest making a note of both the time and space
# complexity for these since the extra space used for join(split) is
# non-negligible.

def replace_space1(my_string):
	return '%20'.join(my_string.split())
	
def replace_space2(my_string):
    return my_string.replace(' ', '%20')

# PROBLEM 5
# Implement a method to perform basic string concatenation using the counts of
# repeated characters, e.g. aabcccccaaa -> a2b1c5a3.  Assuming only upper and 
# lower case letters.  Return original string if compressed list is not shorter.

# (Jordan): The solution is good, but has some stylistic and performance
# issues:
#     'cache' really isn't doing the job of a cache, and is more of a string
#         builder.
#     'range' is somewhat inefficient to use and should be xrange instead.
#     The logical statement you have is a bit confusing and could be more
#         readable with a different starting condition.
#
# def string_compression(my_string):
#   if not my_string:
#     return my_string
#
#   builder = []
#   character = my_string[0]
#   count = 1
#   
#   for char in my_string[1:]:
#     if char == character:
#       count += 1
#     else:
#       builder.append(character)
#       builder.append(count)
#       character = char
#       count = 1
#   return my_string if len(builder) > len(my_string) else ''.join(builder)

def string_compression(my_string):
    cache = []
    counter = 0
    for i in range(len(my_string)):
        
        # if char not repeated - add to cache and reset counter
        if i != 0 and my_string[i-1] != my_string[i]:
            cache.append(my_string[i-1] + str(counter))
            counter = 0
        # if char was repeated, or first element 
        counter += 1
    
    # add last element
    cache.append(my_string[-1] + str(counter))
    compressed_string = ''.join(cache)
    
    # compression length check
    if len(compressed_string) >= len(my_string):
        return my_string
   
    return compressed_string

    
# PROBLEM 6
# Given an image represented by an NxN matrix, where each pixel in the image 
# is 4 bytes, write a method to rotate the image by 90 degrees.  Can you do this
# in place?

def rotate_matrix1(my_matrix):
	n = len(my_matrix) 
	
	# start at outter layer and move inwards
	for layer in range(0, n/2):
		first = layer
		last = n - 1 - layer
		for i in range(first, last):
			
			# left -> top
			temp = my_matrix[first][first + i]
			my_matrix[first][first + i] = my_matrix[last - i][first]
			
			# bottom -> left
			my_matrix[last - i][first] = my_matrix[last][last - i]
			
			# right -> bottom
			my_matrix[last][last - i] = my_matrix[first + i][last]
			
			# top -> right
			my_matrix[first + i][last] = temp
			
	return my_matrix

# one-liner
def rotate_matrix2(my_matrix):
	return [list(x) for x in zip(*my_matrix[::-1])]


# PROBLEM 7
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

def set_zero(mat, rind, cind):
	m = len(mat) # number of rows
	n = len(mat[0]) # number of cols

	# set col to 0
  # (Jordan) When it comes to iteration, use xrange rather than range.
	for i in range(m):
		mat[rind][i] = 0
		
	# set row to 0
	for i in range(n):
		mat[i][cind] = 0
		
	return mat
	
def zero_matrix(mat):
	# need a way to store zero locations
	zero_locs = [] # list of tuples (row_index, col_index)
	
	for rind, row in enumerate(mat):
		for cind, val in enumerate(row):
			if val == 0:
				zero_locs.append((rind, cind))
	
	for rind, cind in zero_locs: 
		mat = set_zero(mat, rind, cind)
		
	return mat
	

# PROBLEM 8
# Given two strings s1 and s2, write code to check if s2 is a rotation of s1.  	

def is_rotation(s1, s2):
	
	if len(s1) != len(s2):
		return False
	
	ds1 = ''.join([s1, s1])
	if s2 in ds1:
		return True
	else: 
		return False
	


