# -*- coding: utf-8 -*-

#import statements
from sys import argv as argv;
from os.path import exists;
import re;

def main():
	#Variables
	script, search_file, target_file = argv;
	new_line = "\n";
	result = "";
	print script;
	
	print "Does the input file exist? {0}".format(exists(search_file));
	if not (exists(search_file)):
		print "If you don't want that, hit CTRL- C (^C).";
		search_file = raw_input(" OR file name to be search: ");
	
	print "Does the output file exist? {0}".format(exists(target_file));
	if not (exists(target_file)):
		print "If you don't want that, hit CTRL- C (^C).";
		target_file = raw_input(" Or file name to store results: ");
	# opening file
	bible = open(search_file, "r");
	target = open(target_file, 'w');
	# regex = re.compile(r'\b\w{4}\b');
	# regex = re.compile(r'\d{4,5}');
	regex = re.compile(r'"ltReferralId":[\d]{0,6}');

	for line in bible:
		# print line;
		four_letter_words = regex.findall(line);
		for word in four_letter_words:
			print word[15:21];
			result +=str(word[15:21])+", ";
		
	
	print result[:-2];
	target.truncate();
	target.write("{0}".format(result[:-2]));
	target.close();
	bible.close();
	
	
	
	
	
	
	
	
if __name__ == '__main__':
	main();