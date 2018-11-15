# -*- coding: utf-8 -*-
'''

List is created by placing all the items (elements) inside a square bracket [ ], separated by commas.
It can have any number of items and they may be of different types (integer, float, string etc.).

To use Lists as Stacks(FILO):
	1) list.append() -- Adds element to list at the end
	2) list.pop() -- Removes LAST element from list 

To use Lists as Queues(FIFO):
	1) from collections import deque
	2) list.append() -- Adds element to list at the end
	3) list.popleft() -- Removes FIRST element from list 

Note:
	To perform del, remove and pop operations on list, list must have value or index.
	
	Examples:
		>>> my_list_1 = [4, 5, 6]
		>>> my_list_1.remove(7)
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		ValueError: list.remove(x): x not in list
		>>> del my_list_1[117]
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		IndexError: list assignment index out of range
		>>> my_list_1.pop(1000)
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		IndexError: pop index out of range
'''
def main():
	# empty list
	my_list = []

	# list of integers
	my_list = [1, 2, 3]

	# list with mixed datatypes
	my_list = [1, "Hello", 3.4]
	
	# Accessing Values in Lists
	my_list_1 = ['del --> removes the item at a specific index', 'remove() --> removes the first matching value, not a specific index', 'pop() --> removes the item at a specific index and returns it', 'physics', 'chemistry', 1997, 2000];
	my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
	print my_list_1[0]
	print my_list_1[1]
	print my_list_1[2]
	print my_list_2[len(my_list_2)-1]

	# Updating Lists
	my_list_2[2] = '19898'
	print my_list_2[2]

	# Delete List element
	print '\nmy_list_1 before del operation'
	print my_list_1[0]
	del my_list_1[0]
	del my_list # delete entire variable
	print 'my_list_1 after del operation'
	print my_list_1
	
	# Remove List element
	print '\nmy_list_1 before remove() operation'
	print my_list_1
	my_list_1.remove('remove() --> removes the first matching value, not a specific index')
	print 'my_list_1 after remove() operation'
	print my_list_1
	
	# Pop List element (index value is optional in pop(index = list[-1]))
	print '\nmy_list_1 before pop() operation'
	print my_list_1
	my_list_1.pop(0)
	print 'my_list_1 after pop() operation'
	print my_list_1
	
	# Appending (inserts at the end of the list) a element to large list
	my_list_1.append('List appended')
	print my_list_1
	
	# Insert List element (below example inserts element in 0th index)
	my_list_1.insert(len(my_list_1) - len(my_list_1), 'Inserted me')
	print my_list_1
	
	# Extending List or concanating 2 lists
	concanate_list_1 = ['I', 'am', 'not', 'Here']
	concanate_list_2 = ['Actually', 'I', 'am', 'Here']
	concatinate_string = 'Hello!!!'
	
	print concanate_list_1
	concanate_list_1.extend(concanate_list_2)
	print concanate_list_1
	
	print 'Extending list with String'
	concanate_list_1.extend(concatinate_string)
	print concanate_list_1
	
	# For more information
	print 'Python'

	


# Practice excercise
def excercise():
	print 'Write a program to :?';

if __name__ == '__main__':
    main();