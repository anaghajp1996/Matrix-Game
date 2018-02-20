import random
from game import Game
luck=0

game = [[random.randint(0,100) for e in range(8)] for e in range(8)]

mygame=Game(game,luck)

while True:
	choice=int(input("Do you want to play or no bro?(1 or 0)"))
	if choice==1:
		luck=int(input("Let's test your luck: "))
		mygame.play(game,luck)


	else:
		break