# -*- coding: utf-8 -*-

#import statements
from sys import argv as argv;
from os.path import exists;

def main():
	#Variables
	script, filename = argv;
	new_line = "\n";
	print script;
	
	# opening file
	test_file = open(script);
	test_file_read_data = test_file.read(); # test_file.read() -- reading file
	
	print "This is your file name to be read {0}".format(script), test_file_read_data;
	
	another_test_file = open(raw_input("Type file name to be read > "));
	
	print another_test_file.read(); # opening and reading file in same line		
	print "File {0} is going to be errased".format(filename);
	print "Does the output file exist? {0}".format(exists(filename));
	if not (exists(filename)):
		print "If you don't want that, hit CTRL- C (^C).";
		raw_input("?");
	print "If you do want that, hit RETURN.";
	
	raw_input("?");
	print "Ready, hit RETURN to continue, CTRL- C to abort."
	print "Opening the file...";
	
	target = open(filename, 'w');
	
	print "Truncating the file {0}. Gooooodbye!!".format(filename);
	
	target.truncate();
	
	print "Now enter 3 lines of data to be saved."
	
	# line1 = raw_input("Enter line 0ne: ");
	# line2 = raw_input("Enter line Two: ");
	# line3 = raw_input("Enter line Three: ");
	
	print "Writing these line to file now.";
	
	# target.write(line1);
	# target.write(new_line);
	# target.write(line2);
	# target.write(new_line);
	# target.write(line3);
	# target.write(new_line);
	target.write("{0}{3}{1}{3}{2}{3}".format(raw_input("Enter line 0ne: "), raw_input("Enter line Two: "), raw_input("Enter line Three: "), new_line));
	target.write("# Your Pyhton code starts here!! \n \n");
	target.write(test_file_read_data); # Writing Pyhton script to file
	
	print "Finally, closing files";
	
	# Closing files
	test_file.close();
	another_test_file.close();
	test_file.close();
	
	
	
	
	
	
	
	
if __name__ == '__main__':
	main();