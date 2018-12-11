# -*- coding: utf-8 -*-
'''
Numbers:

Integers
You can use an integer represent numeric data, and more specifically, whole numbers from negative infinity to infinity, like 4, 5, or -1.


Float
"Float" stands for 'floating point number'. You can use it for rational numbers, usually ending with a decimal figure, such as 1.11 or 3.14.
'''
def main():
	# Integers
	a = 21
	b = 10
	c = 0
	
	# Floats
	x = 4.0
	y = 2.0

	# Addition
	print(x + y)

	# Subtraction
	print(x - y)

	# Multiplication
	print(x * y)

	# Returns the quotient
	print(x / y)
	
	# Returns the rounded away from zero (towards negative infinity)
	print(x // y)

	# Returns the remainder
	print(x % y) 

	# Absolute value
	print(abs(x))

	# x to the power y
	print(x ** y)
	
# Practice excercise
def excercise():
	print 'Write a program to print a piramid using numbers';

if __name__ == '__main__':
    main();
