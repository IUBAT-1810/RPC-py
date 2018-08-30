# Rock Paper Scissors game
# Version 1.0

import random

while True:
	cpu_point = 0
	player_point = 0

	print("Welcome in RPS game by IUBAT-1810\nWhat is your name: ", end='')
	name = input()

	print("Game point: ", end='')
	point = int(input())
	print("Choose between R, P, S.\nHere R represents Rock, P represents Paper, S represents Scissors,")

	while True:

		items = ['R', 'P', 'S']
		cpu_choice = random.choice(items)

		print("=> ", end='')
		player_choice = input()

		if (cpu_choice is 'R' and player_choice is 'R') or (cpu_choice is 'R' and player_choice is 'r'):
			cpu = 'Rock'
			player = 'Rock'
		elif (cpu_choice is 'P' and player_choice is 'P') or (cpu_choice is 'P' and player_choice is 'p'):
			cpu = 'Paper'
			player = 'paper'
		elif (cpu_choice is 'S' and player_choice is 'S') or (cpu_choice is 'S' and player_choice is 's'):
			cpu = 'Scissors'
			player = 'Scissors'
		elif (cpu_choice is 'R' and player_choice is 'P') or (cpu_choice is 'R' and player_choice is 'p'):
			player_point += 1
			cpu = 'Rock'
			player = 'Paper'
		elif (cpu_choice is 'R' and player_choice is 'S') or (cpu_choice is 'R' and player_choice is 's'):
			cpu_point += 1
			cpu = 'Rock'
			player = 'Scissors'
		elif (cpu_choice is 'P' and player_choice is 'R') or (cpu_choice is 'P' and player_choice is 'r'):
			cpu_point += 1
			cpu = 'Paper'
			player = 'Rock'
		elif (cpu_choice is 'P' and player_choice is 'S') or (cpu_choice is 'P' and player_choice is 's'):
			player_point += 1
			cpu = 'Paper'
			player = 'Scissors'
		elif (cpu_choice is 'S' and player_choice is 'R') or (cpu_choice is 'S' and player_choice is 'r'):
			player_point += 1
			cpu = 'Scissors'
			player = 'Rock'
		elif (cpu_choice is 'S' and player_choice is 'P') or (cpu_choice is 'S' and player_choice is 'p'):
			cpu_point += 1
			cpu = 'Scissors'
			player = 'Paper'
		else:
			print("Invalid input")

		print("CPU: %s \t\t %s: %s" %(cpu, name, player))
		print("Points: %s \t\t Points: %s" %(str(cpu_point), str(player_point)))

		if (cpu_point is point) or (player_point is point):
			break

	if player_point > cpu_point:
		print('\n')
		print('*' * 35)
		print("Congratualtions!!! Winner is %s" %name)
		print('*' * 35)
		print('')
	else:
		print('\n')
		print('*' * 35)
		print("You loose. Better luck next time")
		print('*' * 35)
		print('')

	print("Do you want to play again[y/N]: ", end='')
	ask = input()

	if (ask is 'Y' or ask is 'y'):
		print('\n')
	else:
		break

