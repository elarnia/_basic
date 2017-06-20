#!C:\Python34\python.exe

## chance.py
## A shell program for generating random numbers.
## Author: Samuel Patrick
## Date: 9/16/16

import random

#A function to generate random numbers
def generator():
    MAX_SEED = 10**10
    mynum = random.randint(0,MAX_SEED)
    return mynum

#A function to generate a die roll
def dice_roll(y):
    die = generator() % y + 1
    return die

#A function to generate change for a dollar
def rand_change():
    change = generator() % 100
    return change

#A function for guessing somethings weight
def weight_guess(x,y):
    weight = generator() % (y-x) + x
    return weight

#The Penny Jar Game
def penny_jar():
    user = input('How many pennies do you think are in the jar? (0-99) : ')
    pennies = rand_change()
	
	#Check guess
    if user != pennies:
        print('Good try, but there were ', pennies, ' in the jar.')
    else:
        print('How did you do that?! You got it right!')

#The Attack Dice Game
def attack_dice():
	attacker = [0,0,0]
	defender = [0,0]
	winner = 0

    #Roll the dice
	attacker[0] = dice_roll(6)
	attacker[1] = dice_roll(6)
	attacker[2] = dice_roll(6)
	defender[0] = dice_roll(6)
	defender[1] = dice_roll(6)

	#Sort from low to high
	attacker.sort()
	defender.sort()

    #Compare the highest dice
	if attacker[2] <= defender[1]:
		winner -= 1
	else:
		winner += 1
	if attacker[1] <= defender[0]:
		winner -= 1
	else:
		winner += 1
    
	print('Attacker: ', end = " ")
	for die in attacker:
		print(die, end= " ")
	else:
		print()
	
	print('Defender:', end = " ")
	for die in defender:
		print(die, end= " ")
	else:
		print()
	
    #Check who won
	if winner > 0:
		print('The attacker wins!')
	elif winner < 0:
		print('The defender wins!')
	else:
		print('It was a tie.')

#The Weight Guessing Game
def weight_game():
	#Get the persons age and height
	age = input('How old are you? (years) : ')
	age = int(age)
	height = input('How tall are you? (inches) : ')
	height = int(height)
	low = 50
	high = 200
	
	#Change the weight range based on height and age
	if age > 18:
		low += 20
		high += 50
	else:
		low -= 10
		high -= 40
		
	if height > 60:
		low += 20
		high += 50
	else:
		low -= 10
		high -= 40
		
	user = input('How much do you weigh? (pounds) : ')
	user = int(user)
	guess = weight_guess(low,high)
	print('I am going to guess your weight is between ', (guess - 10), ' and ' , (guess + 10))
		
		
	if user >= (guess - 10) and user <= (guess + 10):
		print('I was right!')
	else:
		print("Are you sure that's right?")
			
#The High/Low Game
def high_low():
	card = [0,0,0,0,0]
	winner = True
	position = 0
	
	#Get a random number for each card
	card[0] = weight_guess(1,10)
	card[1] = weight_guess(1,10)
	card[2] = weight_guess(1,10)
	card[3] = weight_guess(1,10)
	card[4] = weight_guess(1,10)
	
	print()
	print("Let's play the high low game. For each card guess if the next card is higher or lower.  Cards range in value from 1-10.  If you guess wrong the game is over.  If the cards are equal the correct guess is lower.")
	
	#Show the first card
	print('The first card is ', card[position])
	
	#Get the user's guess and check if it is correct
	while winner == True and position < 4:
		user = input('Is the next card higher or lower? (h/l) : ')
		if user == 'l' or user == 'L':
			if card[position] < card[position+1]:
				print('Aww man! The next card was actually ', card[position+1], '.')
				winner = False
			else:
				print('The next card was ',card[position+1], '. Good job!')
		elif user == 'h' or user == 'H':
			if card[position] >= card[position+1]:
				print('Aww man! The next card was actually ', card[position+1], '.')
				winner = False
			else:
				print('The next card was ',card[position+1], '. Good job!')
		else:
			print("That wasn't a choice.")
			winner == False
			
		position += 1 
	
	#Check if they won
	if winner == True:
		print('Very impressive! You won!')

#__main__
#Seed the random number generator
random.seed(a=None, version=2)

user = rand_num = -1

rand_num = generator()
lucky_die = dice_roll(6)
change_up = rand_change()
heavy_stuff = weight_guess(100, 300)

print('This is random ... ',rand_num)
print('Using my lucky die ... ',lucky_die)
print("This isn't the right change ... ",change_up)
print('Are you calling me fat ... ',heavy_stuff)

while user != '0':
	print()
	print('Select a game to play: ')
	print('1. Attack Dice')
	print('2. Jar of Change')
	print('3. Weight Guesser')
	print('4. High/Low')
	print('0. Exit')

	user = input('Option: ')

	#Check the user's choice from the menu
	if user == '1':
		attack_dice()
	elif user == '2':
		penny_jar()
	elif user == '3':
		weight_game()
	elif user == '4':
		high_low()
	elif user != '0':
		print('Not a valid input, try again...')

print('Thanks for playing.')
