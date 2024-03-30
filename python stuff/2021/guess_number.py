Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def guess(x);
SyntaxError: invalid syntax
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=input(f'"Guess a number between 1 and (x)")
			    
SyntaxError: EOL while scanning string literal
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=(input(f'Guess a number between 1 and (x): '))
		if guess <  random_number:
			print('Sorry guess again too low. ')
			elif guess>random_number:
				
SyntaxError: invalid syntax
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=(input(f'Guess a number between 1 and (x): '))
		if guess <  random_number:
			print('Sorry guess again too low. ')
			elif guess > random_number
			
SyntaxError: invalid syntax
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=(input(f'Guess a number between 1 and (x): '))
		if guess <  random_number:
			print('Sorry guess again too low. ')
			elif guess > random_number:
				
SyntaxError: invalid syntax
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=(input(f'Guess a number between 1 and (x): '))
		if guess <  random_number:
			print('Sorry guess again too low. ')
		elif guess > random_number:
			print('Sorry guess again too high. ')

			
>>> def guess(x):
	random_number=random.randint(1,x)
	guess=0
	while guess in random_number:
		guess=(input(f'Guess a number between 1 and (x): '))
		if guess <  random_number:
			print('Sorry guess again too low. ')
		elif guess > random_number:
			print('Sorry guess again too high. ')
	print(f'Yay, congrats, You have guessed the number (random_number)')

	
>>> guess(10)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    guess(10)
  File "<pyshell#18>", line 4, in guess
    while guess in random_number:
TypeError: argument of type 'int' is not iterable
>>> Traceback (most recent call last):