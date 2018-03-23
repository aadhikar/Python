# -*- coding: utf-8 -*-
'''
This code checks for profanity (curse words)
'''
#import statements
import urllib;




def main():
    #Variables
    curse_words = "Profanity Alert!!!";
    no_curse_words = "No curse words found";
    incomplete_scan = "Could not scan file";
    
    def read_text():
        quotes = open("D:\Git\Python\Learn N Practice\Udemy_Progeamming Fundamentals of python\data\movie_quotes.txt");
        contents_of_file = quotes.read();
##        print "{0}".format(contents_of_file);
        check_profanity(contents_of_file);

    def check_profanity(text_to_check):
        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check);
        output = connection.read();
##        print "{0}".format(output);
        connection.close();
        if output == 'true':
            print "{0}".format(curse_words);
        elif output == 'false':
            print "{0}".format(no_curse_words);
        else:
            print "{0}".format(incomplete_scan);



    read_text();




if __name__ == '__main__':
    main();
