# import
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga

while(True):
	# input
	n = int(turtle.textinput("Inserisci un numero", "che numero scegli?"))
	#t.reset()
	if (n%2 == 0):
		t.write("SICURAMENTE PARI!")
	else:
		t.write("SICURAMENTE NON PARI!")

turtle.done()