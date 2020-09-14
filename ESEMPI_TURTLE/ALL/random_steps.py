# importiamo i package necessari
import turtle
import random 

# inizializzazione
s = turtle.getscreen() # mostra la finestra
t = turtle.Turtle() # inizializzamo la tartaruga

step = 0
while(step < 100):
	random_number = random.randint(0, 10)
	if (random_number == 0):
		t.forward(10)
	if (random_number == 1):
		t.forward(20)
	if (random_number == 2):
		t.forward(30)
	if (random_number == 3):
		t.forward(40)
	if (random_number == 4):
		t.left(120)
	if (random_number == 5):
		t.right(120)
	if (random_number == 6):
		t.left(45)
	if (random_number == 7):
		t.left(90)
	if (random_number == 8):
		t.right(45)
	if (random_number == 9):
		t.right(90)


# per fare in modo che non si chiuda il programma
input("")