# -*- coding: utf-8 -*-
'''

lambda operator/function
	It is a way to create anonymous functions.
	These are throw-away functions.
	Mainly used with the functions filter(), map() and reduce().

There are three built-in functions that are very useful when used with lists: 
	1) filter(),
	2) map(), and 
	3) reduce().
	
	Note:
		If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list.

'''
def main():
	# lambda syntax --> lambda argument: manipulate(argument)
	is_div_by_3_and_5 = lambda num: num%3 == 0 and num%5 == 0
	
	cube = lambda num: num**3
	
	def add(a, b):
		print str(a), str(b) # For debugging purppose
		return a+b if isinstance(a, int) and isinstance(b, int) else 'Null'

	seq = lambda num: range(num)
	
	def seq2(a, b, c):
		return range(a, b, c)
	
	# filter syntax --> filter(function, sequence)
	'''
	
	filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list.
	
	'''
	print 'Filter function starts here'
	print filter(is_div_by_3_and_5, range(0,100)) # Generates a list with numbers which are divisible by both 3 and 5
	print 'Filter function ends here \n'
		
	# map syntax --> map(function, sequence)
	'''
	map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values.
	Also more than one sequence may be passed; the function must then have as many arguments as there are sequences and is called with the corresponding item from each sequence (or None if some sequence is shorter than another).
	'''
	print 'map function starts here'
	print map(cube, range(0,100))
	print 'map function ends here \n'
		
	print 'map function with multiple arguments starts here'
	print map(add, seq(10), seq2(0, 20, 2))
	print 'map function with multiple arguments ends here \n'
	
	# reduce syntax --> reduce(function, sequence)
	'''
	reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on.
	'''
	print 'Reduce function starts here'
	print reduce(add, range(0,10)) # Generates a list with numbers which are divisible by both 3 and 5
	print 'Reduce function ends here \n'


	
	# For more information
	print 'Python'



# Practice excercise
def excercise():
	print 'Write a program to :?';

if __name__ == '__main__':
    main();
