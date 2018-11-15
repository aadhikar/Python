# -*- coding: utf-8 -*-
'''
Variables are used to store values. A string is a series of characters, surrounded by single or double quotes.
'''
def main():
	# Hello world 
	print('Hello world!');
	
	# Hello world with a variable 
	greeting = 'Hello world!';
	print(greeting);
	
	# String Methods
	string_methods = '                 This string is not start with other because there are couple of old values needs to replaced by new ones but this string ends with other'
	print string_methods.lower(); 					# returns the lowercase version of the string
	print string_methods.upper(); 					# returns the uppercase version of the string
	print string_methods.strip(); 					# returns a string with whitespace removed from the start and end
	print string_methods.isalpha(); 				# tests if all the string chars are in the various character classes
	print string_methods.isdigit(); 				# tests if all the string chars are in the various character classes
	print string_methods.isspace(); 				# tests if all the string chars are in the various character classes
	print string_methods.startswith('other'); 		# tests if the string starts with the given other string
	print string_methods.endswith('other'); 		# tests if the string ends with the given other string
	print string_methods.find('other'); 			# searches for the given other string (not a regular expression) within string_value, and returns the first index where it begins or -1 if not found
	print string_methods.replace('old', 'new'); 	# returns a string where all occurrences of 'old' have been replaced by 'new'
	delim = ' ';
	print string_methods.split(delim); 				# returns a list of substrings separated by the given delimiter
	print delim.join(['l', 'i', 's', 't']); 		# opposite of split(), joins the elements in the given list together using the string as the delimiter
	
	# String Slices
	string_slices = ' H  e  l  l  o';
	print 'Below line is to demonsrate character\'s position in string';
	print string_slices;
	print ' 0  1  2  3  4'; 	# range(0, 5)
	print '-5 -4 -3 -2 -1'; 	# range(-5, 0)
	# Hint for slicing is s[start:end]
	
	# String formating using % operator
	text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down');
	
	# String formating using Format String Syntax
	print "First, thou shalt count to {0}"  # References first positional argument
	print "Bring me a {}"                   # Implicitly references the first positional argument
	print "From {} to {}"                   # Same as "From {0} to {1}"
	print "My quest is {name}"              # References keyword argument 'name'
	print "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
	print "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
	print '{0}, {1}, {2}'.format('a', 'b', 'c');
	print '{}, {}, {}'.format('a', 'b', 'c');
	print '{2}, {1}, {0}'.format('a', 'b', 'c');
	print '{2}, {1}, {0}'.format(*'abc');
	print '{0}{1}{0}'.format('abra', 'cad');   # arguments' indices can be repeated
	
	# Concatenation (combining strings) 
	first_name = 'Albert';
	last_name = 'Einstein'; 
	year_of_birth = 1879;
	full_name = 'My full name is ' + first_name + ' ' + last_name;
	print(full_name);
	# print 'I am' + first_name + ' ' + last_name + ' and I born in' + year_of_birth
	print 'I am {0} {1} and I born in {2}'.format(first_name, last_name, year_of_birth);

# Practice excercise
def excercise():
	print 'Write a program to print a piramid';

if __name__ == '__main__':
    main();