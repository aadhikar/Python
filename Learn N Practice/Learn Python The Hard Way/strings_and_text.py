# -*- coding: utf-8 -*-

#imports
import time as t;

def main():
	#Variables
	my_name = "Anilkumar Adhikari";
	height = 5.11;
	num_of_times = 10;
	people = 10;
	language = "Pyhton";
	do_not = "don't";
	hilarious = False;
	new_line = "\n";
	tab_space = "\t";

	# The %r is best for debugging, and the other formats are for actually displaying variables to users.
	count_people = "There are %d types of people." % people;
	# if you print both about_people and about_people_pythonic_way_syntax, both end uo in same result.
	about_people = "Those who know %s and those who %s." %(language, do_not);
	about_people_pythonic_way_syntax = "Those who know {0} and those who {1}.".format(language, do_not);
	joke_evaluation = "Isn't that joke so funny?!! %r.";

	myself = "I'am {0} and am {1:0.2f} foot tall".format(my_name, height); 

	print count_people;
	print about_people_pythonic_way_syntax;
	print "I said: {0}".format(count_people);
	print "I also said: {0}".format(about_people);
	print joke_evaluation % hilarious;

	# The intersting thing is if you multiply string with number, it prints string repeatedly number times.
	print (myself + new_line) * num_of_times;

	# With the three double- quotes we'll be able type as much as we like as below
	print """
	Hi,
	As you know already my name is Anilkumar Adhikari
	and am 5.11 foot tall
	""";

	# Other way of printing
	print """
	Hi,
	As you know already my name is %s
	and am %0.2f foot tall
	""" %(my_name, height);

	# Pythonically printing
	print """
	Hi,
	{2}As you know already my name is {0}
	{2}and am {1:0.2f} foot tall
	""".format(my_name, height, tab_space); 

	while True:
		for i in ["/","- ","|","\\","|"]:
			print "%s\r" % i,
			t.sleep(1);


	'''
	Escape 			What it does.
	\\				Backslash (\)
	\'				Single- quote (')
	\"				Double- quote (")
	\a				ASCII bell (BEL)
	\b				ASCII backspace (BS)
	\f				ASCII formfeed (FF)
	\n				ASCII linefeed (LF)
	\N{name}		Character named name in the Unicode database (Unicode only)
	\r				ASCII carriage return (CR)
	\t				ASCII horizontal tab (TAB)
	\uxxxx 			Character with 16- bit hex value xxxx (Unicode only)
	\Uxxxxxxxx 		Character with 32- bit hex value xxxxxxxx (Unicode only)
	\v 				ASCII vertical tab (VT)
	\ooo 			Character with octal value oo
	\ xhh 			Character with hex value hh
	'''
	
if __name__ == '__main__':
	main();