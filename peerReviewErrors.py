# This is a header for the application.
# You should read this header and insert your name and your date below as part of the peer review.
# This is a typical part of any program.
# Author: Adam Coleman
# Creation Date: 5/10/2021
# Below is a simple program with 10 issues (some are syntax errors, and some are logic errors).  You need to identify the issues and correct them.

import random
import time

def display_intro():
	"""Function to display an intro"""
	print('''	You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def choose_cave():
	"""Function to choose a cave"""
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave

def check_cave(chosen_cave):
	"""Function to check if the chosen cave is good or bad"""
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 3 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendly_cave = random.randint(1, 2)

	if chosen_cave == str(friendly_cave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
	display_intro()
	cave_number = choose_cave()
	check_cave(cave_number)
    
	print('Do you want to play again? (yes or no)')
	play_again = input().lower()
	if play_again == "no" or play_again == "n":
		print("Thanks for playing")

