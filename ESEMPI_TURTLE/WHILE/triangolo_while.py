# importiamo il package turtle
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga


lato = 1
while lato <= 3:
	print("disegno lato" + str(lato))
	t.forward(100)
	t.right(120)
	lato = lato+1 # stepper

# e se invertiamo l'ordine di forward() e right() ??

turtle.done()