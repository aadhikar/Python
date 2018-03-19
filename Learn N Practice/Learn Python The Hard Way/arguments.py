# -*- coding: utf-8 -*-

#import statements
from sys import argv as argv;

def main():
	#Variables
	script, first, second, third = argv
	print argv
	print "The script name your are in is {0} and your name is {1}".format( script, raw_input("Enter you name here "));
	print "Your first, second and third arguments are {0} {1} {2} respectively".format(first, second, third);
	# print "Your first argument is {0}".format(first);
	# print "Your second argument is {0}".format(second);
	# print "Your third argument is {0}".format(third);
	
if __name__ == '__main__':
	main();