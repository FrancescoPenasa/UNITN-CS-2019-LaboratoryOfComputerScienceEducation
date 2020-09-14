# importiamo il package turtle
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga

for lato in range(4):
	print("disegno lato" + str(lato))
	t.forward(100)
	t.right(90)


turtle.done()