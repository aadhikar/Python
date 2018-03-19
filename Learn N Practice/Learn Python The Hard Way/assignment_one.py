# write a python program that prints all the numbers between 2000 and 3500 which are divisible by 7 and not the multiples of 5. the output should be printed in a single line separated by commas

# -*- coding: utf-8 -*-
#import statements
from sys import argv as argv;

# Method to validate number is divisible 7 or not
def isdivisibleBy7(number):
	return number%7==0;

# Method to validate number is divisible 5 or not
def isdivisibleBy5(number):
	return number%5==0;
	
def main():
	result = '';
	script, range_from, range_to, file_name = argv;
	for num in range(int(range_from), int(range_to)):
		if isdivisibleBy7(num) and (not isdivisibleBy5(num)):
			result += "Anil: " +str(num) + " ";
	print result[:-1];
	
	
	target = open(file_name, 'w');
	target.truncate();
	target.write("{0}".format(result[:-2]));
	target.close();




if __name__ == '__main__':
	main();