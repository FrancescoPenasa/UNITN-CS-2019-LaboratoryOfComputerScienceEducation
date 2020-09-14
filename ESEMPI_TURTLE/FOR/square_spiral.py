import turtle

t = turtle.Pen() # inizializzamo la tartaruga

for x in range(100):
	t.forward(x*3) # x aumenta il suo valore di uno, cosa succede se usiamo x+3 e x*3 e x^3?
	t.left(90)

	print("il valore di x = " + str(x))

turtle.done()