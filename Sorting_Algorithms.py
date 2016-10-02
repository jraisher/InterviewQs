# Selection Sort
def selection_sort(my_list):
	ind = 0
	
	while ind < len(my_list):
		# need to find min value that
		# hasn't been found before
		mindex = ind + my_list[ind:].index(min(my_list[ind:]))
		
		# do the swap
		temp = my_list[mindex]
		my_list[mindex] = my_list[ind]
		my_list[ind] = temp
		
		# increment ind
		ind += 1
		
	return my_list
	
	
# Merge Sort
def merge(list1, list2):
	ind1, ind2 = 0, 0
	sorted_list = []
	while ind1 < len(list1) and ind2 < len(list2):
		if list1[ind1] < list2[ind2]:
			sorted_list.append(list1[ind1])
			ind1 += 1
		else:
			sorted_list.append(list2[ind2])
			ind2 += 1
	
	sorted_list.extend(list1[ind1:])
	sorted_list.extend(list2[ind2:])
	
	return sorted_list

def merge_sort(my_list):
	n = len(my_list)
	
	# base case
	if n <= 1:
		return my_list
	
	left = merge_sort(my_list[:n/2])
	right = merge_sort(my_list[n/2:])
	
	return merge(left, right)
	
	
# Insertion Sort
def insertion_sort(my_list):
	key = 1
	while key < len(my_list):
		ind = key
		while ind > 0:
			if my_list[ind] < my_list[ind - 1]:
				# swap 
				temp = my_list[ind]
				my_list[ind] = my_list[ind - 1]
				my_list[ind - 1] = temp
			else:
				break
			ind -= 1
		key += 1
	
	return my_list

# (Jordan): Make sure you also understand quicksort.  It's an O(nlogn) sort in place.