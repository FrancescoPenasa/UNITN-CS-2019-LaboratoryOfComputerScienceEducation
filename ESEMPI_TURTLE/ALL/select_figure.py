# importiamo i package necessari
import turtle
import random 

# inizializzazione
s = turtle.getscreen() # mostra la finestra
t = turtle.Turtle() # inizializzamo la tartaruga

figura = input("Che figura vuoi vedere? (triangolo | quadrato | rettangolo | cerchio): ")
if (figura == "triangolo"):
	for lato in range(3):
		t.forward(100)
		t.left(180 + 60)

elif(figura == "quadrato"):
	for lato in range(4):
		t.forward(100)
		t.left(90)

elif(figura == "rettangolo"):
	for lato in range(2):
		t.forward(100)
		t.left(90)
		t.forward(200)
		t.left(90)

elif(figura == "cerchio"):
	t.speed(0)
	for i in range(360):
		t.forward(1)
		t.left(1)
else:
	print("Non capisco, riprova")


# per fare in modo che non si chiuda il programma
input("")