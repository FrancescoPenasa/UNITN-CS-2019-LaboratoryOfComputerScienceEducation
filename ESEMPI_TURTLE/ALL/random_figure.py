# importiamo i package necessari
import turtle
import random 

# inizializzazione
s = turtle.getscreen() # mostra la finestra
t = turtle.Turtle() # inizializzamo la tartaruga


random_number = random.randint(0,4)
print("il numero casuale e'" + str(random_number))

if (random_number == 0):
	for lato in range(3):
		t.forward(100)
		t.left(180 + 60)

elif(random_number == 1):
	for lato in range(4):
		t.forward(100)
		t.left(90)

elif(random_number == 2):
	for lato in range(2):
		t.forward(100)
		t.left(90)
		t.forward(200)
		t.left(90)

elif(random_number == 3):
	for i in range(360):
		t.forward(1)
		t.left(1)
else:
	print("c'e' qualcosa che non va")

# per fare in modo che non si chiuda il programma
input("")