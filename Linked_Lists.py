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
		prev = self.head
		cursor = prev.next
		counter = 1
		
		while cursor is not None:
			if i == counter:
				prev.next = cursor.next
			else:
				prev = cursor
				
			cursor = cursor.next
			counter += 1
	
		# check head
		if i == 0:
			self.head = self.head.next
			
	# print the LL
	def print_list(self):
		node = self.head
		vals = []
		while node is not None:
			vals.append(node.value)
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
		