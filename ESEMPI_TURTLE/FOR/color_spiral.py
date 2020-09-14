import turtle
t = turtle.Turtle()
s = turtle.getscreen()

s.bgcolor("black")
sides = 6

for x in range(0, 360, 10):
	t.width(x*sides/200)

	if(x < 120):
		t.pencolor("yellow")
	elif(x < 240):
		t.pencolor("orange")
	else:
		t.pencolor("red")

	t.forward(x * 3/sides + x)
	t.left(360/sides + 1)


turtle.done()