# -*- coding: utf-8 -*-
'''

Control Flow

'''
def main():
	# Variable
	x = 21
	
	# if, elif and else Statement
	if x < 0:
		print "x is negative"
	elif x % 2:
		print "x is positive and odd"
	else:
		print "x is even and non-negative"
	
	# For loop
	words = ['cat', 'window', 'defenestrate']
	for w in words:
		print w, len(w)

	# break and continue Statements, and else Clauses
	# below code searches for prime numbers
	for n in range(2, 10): 
		for x in range(2, n):
			if n % x == 0:
				print n, 'equals', x, '*', n/x
				break
			else:
				# loop fell through without finding a factor
				print n, 'is a prime number'
	
	# Access every 3rd element in a list using while loop
	i = 0
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
	while i < len(a):
		print a[i]
		i = i + 3
	
	# pass Statements
	while True:
		pass  # Busy-wait for keyboard interrupt (Ctrl+C)
		
# Practice excercise
def excercise():
	print 'Write a program to validate given person\'s age is 18 or not. If yes, print DOB';

if __name__ == '__main__':
    main();