# importiamo il package turtle
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga


x = 1
y = 1
while x <= 6:
	t.circle(30)
	while y < 3:
		t.forward(y) 
		y = y + 1
	y = 1
	x = x + 1


turtle.done()