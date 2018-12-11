# -*- coding: utf-8 -*-
'''

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

In other words, list comprehension is an alternative for filter(), map() and reduce() approach to create new list.
	
'''

def main():
	# Approach 1 to create a list of cubes
	cubes_approach_1 = []
	for num in range(10):
		print str(num)+'^3', num**3
		cubes_approach_1.append(num**3)
	print cubes_approach_1
	
	# Approach 2 to create a list of cubes
	print [num**3 for num in range(0, 10)]

	# Equivalent approach to create a list of cubes using lambda and  map()
	print map(lambda num: num**3, range(10))
	
	'''
	A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
	'''
	# Example one
	print [(x,y) for x in range(1, 4) for y in range(-4, -1) if x != y]
	
	# Equivalent to example one
	combinations = []
	for x in range(1,4):
		for y in range(-4, -1):
			if x != y:
				combinations.append((x,y))
	print combinations
	
	# For more information
	print 'Python'



# Practice excercise
def excercise():
	print 'Write a program to :?';

if __name__ == '__main__':
    main();
