# -*- coding: utf-8 -*-
'''

Logical Operators

'''
def main():
	x = False
	if not x :
		print("condition satisfied")
	else:
		print("condition not satisfied")
	
	
	if 1 < 2 and 4 > 2:
    print("condition satisfied")

	if 1 > 2 and 4 < 10:
		print("condition not satisfied")

	if 4 < 10 or 1 < 2:
		print("condition satisfied")

	if not (1 > 2 and 4 < 10):
		print("condition satisfied")
		
# Practice excercise
def excercise():
	print 'Write a program to display smallest in given three numbers';

if __name__ == '__main__':
    main();