# import
import turtle

# inizializzazione
s = turtle.getscreen() # finestra
t1 = turtle.Turtle() # tartaruga 1
t2 = t1.clone() # tartaruga 2

t1.goto(0, 100)

t2.pencolor("red")
t2.goto(0, -100)

# costanti
CARTA = 0
FORBICE = 1
SASSO = 2

p1_value = int(turtle.textinput("Inserisci la tua mossa", "Giocatore1: Carta(0), forbice(1) o sasso(2)? "))
p2_value = int(turtle.textinput("Inserisci la tua mossa", "Giocatore2: Carta(0), forbice(1) o sasso(2)? "))

if (p1_value == p2_value):
	t1.write("Parita'!")
	t2.write("Parita'!")
elif (p1_value == ((p2_value + 1) % 3))
	t1.write("Sono il player 1 e ho vinto!")
elif (p2_value == ((p1_value + 1) % 3)):
	t2.write("Sono il player 2 e ho vinto!")


turtle.done()