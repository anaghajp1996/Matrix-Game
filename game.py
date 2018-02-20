class Game(object):
	import random

	def __init__(self,game,luck):
		
		self.game=game
		self.luck=int(luck)

	# game = [[random.randint(0,10) for e in range(8)] for e in range(8)]
	# while True:
	# 	luck=int(input("Do you want to play or no bro?(1 or 0)"))
	# 	if luck==1:


	def play(self,game,luck):
			# num=int(input("Let's test your luck: "))

		for i in range(8):
			for j in range(8):
				if self.luck==self.game[i][j]:
					print("LOSER!!")
					break
					
				else:
					print("Your are not a loser....yet.")
					break
			break

		# else:
		# 	break




