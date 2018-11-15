# -*- coding: utf-8 -*-
'''

Operators Precedence

Operator					Description
**							Exponentiation (raise to the power)
~ + -						Complement, unary plus and minus (method names for the last two are +@ and -@)
* / % //					Multiply, divide, modulo and floor division
+ -							Addition and subtraction
>> <<						Right and left bitwise shift
&							Bitwise 'AND'
^ |							Bitwise exclusive `OR' and regular `OR'
<= < > >=					Comparison operators
<> == !=					Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not					Identity operators
in not in					Membership operators
not or and					Logical operators

'''
def main():
	# Values
	a = 20
	b = 10
	c = 15
	d = 5
	e = 0

	e = (a + b) * c / d       #( 30 * 15 ) / 5
	print "Value of (a + b) * c / d is ",  e

	e = ((a + b) * c) / d     # (30 * 15 ) / 5
	print "Value of ((a + b) * c) / d is ",  e

	e = (a + b) * (c / d);    # (30) * (15/5)
	print "Value of (a + b) * (c / d) is ",  e

	e = a + (b * c) / d;      #  20 + (150/5)
	print "Value of a + (b * c) / d is ",  e
		
# Practice excercise
def excercise():
	print 'Write a program to hmmmmm!!';

if __name__ == '__main__':
    main();