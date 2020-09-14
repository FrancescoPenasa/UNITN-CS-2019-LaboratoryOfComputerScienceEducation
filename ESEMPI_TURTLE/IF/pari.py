# import
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga

# input
n = int(turtle.textinput("Inserisci un numero", "che numero scegli?"))


if (n == 0 or n == 2 or n == 4):
	t.write("SICURAMENTE PARI!")
else:
	t.write("PROBABILMENTE NON PARI!")

turtle.done()