# -*- coding: utf-8 -*-
'''

It iss not necessary to write *args or **kwargs(these are just conventions). Only *(asterisk) is important. 
	Examples: *<valiable_name>, **<valiable_name>
	
These are mostly used in function defenitions.

Note:
	1. *args is used to send a non-keyworded variable length argument list to the function.
	2. **kwargs allows you to pass keyworded variable length of arguments to a function(handles named arguments).
	3. The most common use case is when making function decorators. Moreover it can be used in monkey patching as well.
	
'''

def main():
	# *args
	def testing_args(name, *aliases):
		print 'First argument is:', str(name)
		for alias in aliases:
			print 'Aka', str(alias)
	
	testing_args('I\'am', 'Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob', 'Lucas', 'Michael', 'Alexander', 'Ethan', 'Daniel', 'Matthew')
	
	# **kwargs
	def testing_kwargs(**kwargs):
		print kwargs.items()
		for key, value in kwargs.items():
			print '{0} = {1}'.format(key, value if value.strip() is not '' else 'Invalid!!')
			
	testing_kwargs(first_name='Anil', middle_name = 'A', last_name = 'Adhikari') # result will be sorted (by key in this example)
	
	# For more information
	print 'Python'



# Practice excercise
def excercise():
	print 'Write a program to :?';

if __name__ == '__main__':
    main();
	excercise();
