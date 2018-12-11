# -*- coding: utf-8 -*-
'''

Set 
	It is an unordered collection with no duplicate elements.
	Basic uses include membership testing and eliminating duplicate entries.
	Set object also support mathematical operations like union, intersection, difference, and symmetric difference.
	Curly braces or the set() function can be used to create sets
	
Note:
	To create an empty set you have to use set(), not {}.

'''
def main():
	# Sets
	basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
	fruit =set(basket) # create a set without duplicates
	print fruit # fruit does not have duplicate values
	
	# fast membership testing
	print 'Does orange exists in fruit?','orange' in fruit
	
	# Demonstrate set operations on unique letters from two words
	a = set('abracadabra')
	b = set('alacazam')
	print 'Unique letters in \'abracadabra\' -->', a
	print 'Unique letters in \'alacazam\' -->', b
	
	# letters in a but not in b
	print 'Letters in a but not in b -->', a - b
	
	# letters in either a or b
	print 'Letters in either a or b -->', a | b
	
	# letters in both a and b
	print 'Letters in both a and b -->', a & b
	
	# letters in a or b but not both
	print 'Letters in a or b but not both -->', a ^ b
	
	# set comprehensions
	'''
	Similarly to list comprehensions, set comprehensions are also supported.
	'''
	print {x for x in 'abracadabra' if x not in 'abc'}
	
	print 'Python'


def excercise():
	print 'Write a programm to :?'
	
if __name__ == '__main__':
	main();
	excercise();
