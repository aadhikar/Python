# -*- coding: utf-8 -*-
'''

Tuples are similar to lists, but the items in a tuple can't be modified (immutable), and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing.
A tuple consists of a number of values separated by commas.

'''

def main():
	# Tuples
	tup = 12345, 54321, 'hello!'
	print tup
	print tup[1]
	
	# Tuples may be nested:
	tup_nested = tup, (1, 2, 3, 4, 5)
	print tup_nested
	print tup_nested[0]
	print tup_nested[1]
	
	# Tuples are immutable:
	tup_immutable = 68798797, 55554654, 'I am here!'
	print tup_immutable
	print 'Uncommenting below assignment statement will throw an error --> TypeError: \'tuple\' object does not support item assignment'
	# tup_immutable[0] = 88888
	
	# Tuples can contain mutable objects:
	tup_nested_mutable = ([1, 2, 3], [3, 2, 1])
	print tup_nested_mutable
	tup_nested_mutable[1][0] = 'Anil'
	print tup_nested_mutable
	
	# Create empty tuple
	tup_empty = ()
	print 'Length of tup_empty is',len(tup_empty)
	
	# Create tuple with single value
	tup_singleton = 'hello',    # <-- note trailing comma
	print tup_singleton
	print 'Length of tup_singleton is',len(tup_singleton)
	
	# tuple packing
	tup_packing = 12345, 54321, 'hello!'
	print tup_packing
	
	# tuple unpacking
	'''
	
	Sequence unpacking and works for any sequence on the right-hand side. Sequence unpacking requires the list of variables on the left to have the same number of elements as the length of the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
	
	'''
	a, b, c = tup_packing
	print a
	print b
	print c

	print 'Python'

def excercise():
	print 'Write program to :?'

if __name__ == '__main__':
	main();
	excercise();
