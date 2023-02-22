print("Welcome to Atnafu's Game Center")
print("I am Tolosa,the most honest Rock/ Paper/ Scissor player")
input1 = input("Rock,Paper,Scissor?")

import random
poss = ["Rock","Paper","Scissor"]
draw = random.choice(poss)
choice = ["Rock","Paper","Scissor"]

print(f'{input1}/{draw}')
if input1 == draw:
	print("Draw!No one won!")
elif input1 == "Rock" and draw == "Paper":
	print("I win,where is my money at?")
elif input1 == "Paper" and draw == "Rock":
	print("You won,You lucky son of a bitch!")
elif input1 == "Scissor" and draw =="Rock":
	print("I win,where is my money at?")
elif input1 == "Rock" and draw == "Scissor":
	print("You won,You lucky son of a bitch!")
elif input1 == "Scissor" and draw == "Paper":
	print("You won,You lucky son of a bitch!")
elif input1 == "Paper" and draw == "Scissor":
	print("I win,where is my money at?")
	
	
