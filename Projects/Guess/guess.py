# -*- coding: utf-8 -*-

#import statements
import random as rand

def isNumberInRange(number, num_from, num_till):
	if(num_from<=number>=num_till):
		print 'You have entered {0}'.format(number);
		return number;
	else:
		print 'You have entered not {0}'.format(number);

def main():
	#Variables
	range_from = 1;
	range_till = 6;
	num = rand.randint(range_from, range_till);
	guessCount = 0;
	print(num);
	print 'You may get number of chances between 1 and 5. Choose your number carefully';

	while guessCount<rand.randint(1, 5):
	  guessedNum = isNumberInRange(int(input('Guess a number between {0} and {1}: '.format(range_from, range_till))), range_from, range_till);
	  guessCount = guessCount+1;
	  
	  if guessedNum < num:
		print 'Go higher';
	  
	  if guessedNum > num:
		print 'Go lower';

	  if guessedNum == num:
		break;

	if guessedNum == num:
	  print 'Correct!! You have guessed number in {0} chances'.format(str(guessCount)) ;

	if guessedNum != num:
	  print 'NOPE!!!! I was thinking of number {0}'.format(str(num));
  

if __name__ == '__main__':
	main();