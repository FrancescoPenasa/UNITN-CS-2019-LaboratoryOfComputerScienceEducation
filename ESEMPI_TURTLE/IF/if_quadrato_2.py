# import
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga

t.speed(1) # velocita' bassa

# input variable
n = int(input("Inserisci un numero: "))


if (n % 2 == 0):	# se pari crea un rettangolo
	t.forward(100)
	t.right(90)

	t.forward(100)
	t.right(90)

	t.forward(100)
	t.right(90)

	t.forward(100)
	t.right(90)

else: 				# altrimenti crea un triangolo
	t.forward(100)
	t.left(120)

	t.forward(100)
	t.left(120)

	t.forward(100)
	t.left(120)



turtle.done()