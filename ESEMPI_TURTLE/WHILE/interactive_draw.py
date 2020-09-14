### da fare con shell interattiva e poi con l'esecuzione di file ###

# importiamo il package turtle
import turtle

# inizializzazione
s = turtle.getscreen() # mostra la finestra
t = turtle.Turtle() # inizializzamo la tartaruga
t.speed(1) # facciamo andare la tartaruga piano

while True:
	input_var = input("In che direzione andiamo? (FORWARD, BACKWARD, LEFT, RIGHT)")
	if (input_var == "FORWARD"):
		t.forward(100) 
	if (input_var == "LEFT"):
		t.left(90) 
	if (input_var == "RIGHT"):
		t.right(90) 
	if (input_var == "BACKWARD"):
		t.backward(100) 
