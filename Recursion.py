
# Collatz Conjecture
def hail(num):
	print num
	if num == 1:
		return
	
	if num % 2 == 0:
		hail(num / 2)
	else:
		hail(num * 3 + 1)
		
		
# Binary Search - Recursive
def binary_search(sorted_list, val):
	def recurse(first, last):
		mid = (first + last) / 2
		if first > last:
			return None
		elif sorted_list[mid] < val:
			return recurse(mid + 1, last)
		elif sorted_list[mid] > val:
			return recurse(first, mid - 1)
		else:
			return mid
	
	return recurse(0, len(sorted_list) - 1)
	
