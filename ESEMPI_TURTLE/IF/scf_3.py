# import
import turtle
import random 

# inizializzazione
# s = turtle.getscreen() # finestra
# t = turtle.Turtle() # tartaruga

# costanti
CARTA = 0
FORBICE = 1
SASSO = 2

cpu_value = -1
p1_value = int(input("Giocatore1: Carta(0), forbice(1) o sasso(2)? "))

if p1_value == 0:
	cpu_value = 1
elif p1_value == 1:
	cpu_value = 2
else:
	cpu_value = 0

print("cpu ha selezionato: " + str(cpu_value))

if (p1_value == cpu_value):
	print("Parita'!")
else:
	if (p1_value == ((cpu_value + 1) % 3)):
		print("Giocatore1 vince!")
	elif (cpu_value == ((p1_value + 1) % 3)):
		print("CPU vince!")


# turtle.done()