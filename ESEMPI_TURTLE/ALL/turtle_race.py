# importiamo il package turtle
import turtle
import random 

# inizializzazione
s = turtle.getscreen() # mostra la finestra

# finish line
t = turtle.Turtle()
t.color("white")
t.setpos(300, 200)
t.color("black")
t.stamp()
t.goto(300, -200)

# proprieta' dei giocatori
player_one = turtle.Pen() 
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)


# comincia il gioco
for i in range(20):
	# controllo se p1 ha vinto
	if player_one.pos() >= (300,100):
		print("Player One Wins!")
		exit()

	# altrimenti controllo se p2 ha vinto
	elif player_two.pos() >= (300,-100):
		print("Player Two Wins!")
		exit()

	# altrimenti avanzo con il gioco
	else:
		player_one_turn = input("Press 'Enter' to roll the die ")
		die_player_1 = random.randint(1,6)
		print("The result of the die roll is: ")
		print(die_player_1)
		print("The number of steps will be: ")
		print(20*die_player_1)
		player_one.fd(20*die_player_1)

		player_two_turn = input("Press 'Enter' to roll the die ")
		die_player_2 = random.randint(1,6)
		print("The result of the die roll is: ")
		print(die_player_2)
		print("The number of steps will be: ")
		print(20*die_player_2)
		player_two.fd(20*die_player_2)