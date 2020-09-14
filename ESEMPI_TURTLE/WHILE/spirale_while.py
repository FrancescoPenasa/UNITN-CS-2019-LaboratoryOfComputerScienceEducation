import turtle

t = turtle.Pen() # inizializzamo la tartaruga
t.speed(6)

step = -1
while step < 300:
	t.forward(step*3) # x aumenta il suo valore di uno, cosa succede se usiamo x+3 e x*3 e x^3?
	t.left(90)
	step = step + 1

turtle.done()