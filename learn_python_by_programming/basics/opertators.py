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
	
	# Comparison Operators
	if ( a == b ):
	   print "a is equal to b"
	else:
	   print "a is not equal to b"

	if ( a != b ):
	   print "a is not equal to b"
	else:
	   print "a is equal to b"

	if ( a <> b ):
	   print "a is not equal to b"
	else:
	   print "a is equal to b"

	if ( a < b ):
	   print "a is less than b" 
	else:
	   print "a is not less than b"

	if ( a > b ):
	   print "a is greater than b"
	else:
	   print "a is not greater than b"

	a = 5;
	b = 20;
	
	if ( a <= b ):
	   print " is either less than or equal to  b"
	else:
	   print "a is neither less than nor equal to  b"

	if ( b >= a ):
	   print "b is either greater than  or equal to b"
	else:
	   print "b is neither greater than  nor equal to b"
	   
	# Assignment Operators   
	c = a + b
	print "Value of c is ", c

	c += a
	print "Value of c is ", c 

	c *= a
	print "Value of c is ", c 

	c /= a 
	print "Value of c is ", c 

	c  = 2
	c %= a
	print "Value of c is ", c

	c **= a
	print "Value of c is ", c

	c //= a
	print "Value of c is ", c


# Practice excercise
def excercise():
	print 'Write a program to Hmmmmm!!';

if __name__ == '__main__':
    main();