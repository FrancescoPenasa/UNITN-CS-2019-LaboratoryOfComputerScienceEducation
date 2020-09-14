import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga
t.speed(0)

for x in range(360):
	t.forward(3)
	t.left(1)


turtle.done()