# Linked List Implementation
class Node:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next
		
class LinkedList:
	def __init__(self, head):
		self.head = head
		
	# append to tail of LL
	def append(self, value):
		end = Node(value)
		node = self.head
		
		while node.next is not None:
			node = node.next
		
		node.next = end

	# delete a value/values from a LL
	def delete_value(self, value):
		prev = self.head
		cursor = prev.next
		while cursor is not None:
			if cursor.value == value:
				prev.next = cursor.next
			else:
				prev = cursor
			
			cursor = cursor.next
			
		# check head
		if self.head.value == value:
			self.head = self.head.next
	
	# delete based on index
	def delete_index(self, i):
		# check head
		if i == 0:
			self.head = self.head.next
			return 
			
		prev = self.head
		cursor = prev.next
		counter = 1
		
		while cursor is not None:
			if i == counter:
				prev.next = cursor.next
				return
			else:
				prev = cursor
				
			cursor = cursor.next
			counter += 1
	
	# print the LL
	def print_list(self):
		node = self.head
		vals = []
		while node is not None:
			vals.append(str(node.value))
			node = node.next
			
		vals.append('None')
		print ' --> '.join(vals)
		
# PROBLEM 1
# Write code to remove duplicates from an unsorted linked list

	def remove_duplicates(self):
		cache = {self.head.value: 1}
		prev = self.head
		cursor = prev.next
		while cursor is not None:
			if cursor.value not in cache:
				cache[cursor.value] = 1
				prev = cursor
			else:
				prev.next = cursor.next
			
			cursor = cursor.next
		
# What if no temporary buffer is allowed?

	def remove_dups_nobuffer(self):
		# cursor and runner that runs ahead
		cursor = self.head
		while cursor is not None:
			runner = cursor
			while runner.next is not None:
				if runner.next.value == cursor.value:
					runner.next = runner.next.next
				else:
					runner = runner.next
			cursor = cursor.next		
		

# PROBLEM 2
# Implement an algorithm to find the kth to last element of a singly linked list

	# recursive solution, print value
	def kth_to_last1(self, node, k):
		if node is None:
			return 0
		
		i = self.kth_to_last1(node.next, k) + 1
		
		if i == k:
			print node.value

		return i

	# iterative solution
	def kth_to_last2(self, k):
		p = self.head
		q = p
		for i in range(k):
			q = q.next
		# q and p are separated by k nodes
		
		while q is not None:
			q = q.next
			p = p.next
			
		print p.value
		
		
# PROBLEM 4
# Write code to partition a linked list around a value x, such that all nodes less 
# than x come before all nodes greater than or equal to x

	def partition1(self, x):
		cursor = self.head
		lt = []
		gt = []
		
		while cursor is not None:
			if cursor.value < x:
				lt.append(cursor)
			else:
				gt.append(cursor)
			cursor = cursor.next

		for i in range(len(lt) - 1):
			lt[i].next = lt[i+1]
			
		for i in range(len(gt) - 1):
			gt[i].next = gt[i+1]
			
		lt[-1].next = gt[0]
		gt[-1].next = None
		self.head = lt[0]
		
	# without lists
	def partition2(self, x):
		cursor = self.head
		head = cursor
		tail = cursor
		
		while cursor is not None:
			next = cursor.next
			if cursor.value < x:
				cursor.next = head
				head = cursor
			else:
				tail.next = cursor
				tail = cursor
			cursor = next
		tail.next = None
		self.head = head
			
			
# PROBLEM 3
# Implement an algorithm to delete a node in the middle of a singly linked list
# given only access to that node.

def delete_node(node):
	#if node is the end node, can't delete it
	if node.next is None:
		node.value = None
	else:			
		# copy value and next info from node.next
		node.value = node.next.value
		node.next = node.next.next
		

# PROBLEM 5
# You have two numbers represented by linked lists, where each node contains
# a single digit.  The digits are stored in reverse order, such that the 1's digit
# is at the head of the list.  Write a function that adds the two numbers and 
# returns the sum as a linked list.
def add(p, q):
	carry_digit = 0
	dummy = LinkedList(Node(0))
	cursor = dummy.head
	while p is not None or q is not None:
		if p is None:
			pval = 0
		else:
			pval = p.value
			p = p.next
			
		if q is None:
			qval = 0
		else:
			qval = q.value
			q = q.next
			
		s = pval + qval
		cursor.next = Node(s % 10 + carry_digit)
		carry_digit = s / 10
		cursor = cursor.next
	
	if carry_digit == 1:
		cursor.next = Node(1)
		
	return LinkedList(dummy.head.next) 
		
# Suppose the digits are stored in forward order.

#def add_forward(p, q):
	
		
		
	
	
p = LinkedList(Node(7))
p.append(1)
p.append(6)
p.append(9)
p.append(5)
p.append(3)
p.append(4)
p.print_list()
p.partition2(5)
p.print_list()
