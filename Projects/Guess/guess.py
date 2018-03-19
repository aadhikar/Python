# -*- coding: utf-8 -*-

#import statements
import random as rand
import time as time

def getName(userName):
	return str(userName);

	
def ordinal(num):
	numInStr = str(num);
	ordnl = numInStr[len(numInStr)-1];
	if ordnl==str(1):
		ordnl = ordnl+'st';
	elif ordnl==str(2):
		ordnl = ordnl+'nd';
	elif ordnl==str(3):
		ordnl = ordnl+'rd';
	else :
		ordnl = ordnl+'th';
	return numInStr.replace(numInStr[len(numInStr)-1], ordnl);
	
	

def appreciation(name, attemts, flag):
	congratz = 'Congratulations!!';
	if attemts==1 and flag:
		print '{2} Flying colors {0} and you got it in your {1} attempt'.format(name, ordinal(attemts), congratz);
	elif attemts==2 and flag:
		print '{2} Not bad {0} and you got it in your {1} attempts'.format(name, ordinal(attemts), congratz);
	elif attemts==3 and flag:
		print 'Oooo almost missed it {0} and you got it in your {1} attempts'.format(name, ordinal(attemts));
	else :
		print 'You missed it {0} and you took your {1} attempts'.format(name, ordinal(attemts));

def closeApplication():
	time.sleep(3);
	print 'Closing application now';
	time.sleep(2);

def isNumberInRange(number, num_from, num_till):
	if(num_from<=number>=num_till):
		print 'You have entered {0}'.format(number);
		return number;
	else :
		print 'You have entered {0}'.format(number);
		return number;

def main():
	#Variables
	range_from = 1;
	range_till = 6;
	isGuessCorrect = False;
	num = rand.randint(range_from, range_till);
	guessCount = 0;
	#generatedNumber = rand.randint(1, 5);
	generatedNumber = 3;
	#print(num);
	print 'You may get number of chances between 1 and 5. Choose your number carefully';

	while guessCount<generatedNumber:
	  #userName = input('Enter Your Name Here: ');
	  #userName = getName(input('Enter Your Name Here: '));
	  #print 'Hello {0}'.format(userName);
	  userName = 'Test User';
	  guessedNum = isNumberInRange(int(input('Guess a number between {0} and {1}: '.format(range_from, range_till))), range_from, range_till);
	  guessCount = guessCount+1;
	  
	  if guessedNum < num:
		print 'Go higher';
	  
	  if guessedNum > num:
		print 'Go lower';

	  if guessedNum == num:
		isGuessCorrect = True;
		appreciation(userName, guessCount, isGuessCorrect);
		closeApplication();
		break;

	if guessedNum != num:
	  appreciation(userName, guessCount, isGuessCorrect);
	  closeApplication();
  

if __name__ == '__main__':
	main();