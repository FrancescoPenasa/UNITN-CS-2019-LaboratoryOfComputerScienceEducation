"""
In base al giorno in cui eseguiamo questo programma 
la tartaruga sara' piu' o meno veloce e produttiva
"""


# import
import turtle
import datetime

# inizializzazione
s = turtle.getscreen() # finestra
t = turtle.Turtle() # tartaruga


today = datetime.datetime.today()
today = today.weekday()
print("Oggi e' " + today)

if (today < 0):
	print("Ma e' impossibile")
if (today >= 0 && today < 4):	
	t.speed(0) # velocita' massima
if (today >= 4 && today < 5):
	t.speed(5) # velocita' media
if (today >= 5):
	t.speed(1) # velocita' bassissima



t.forward(100)
t.right(90)

t.forward(100)
t.right(90)

t.forward(100)
t.right(90)

t.forward(100)
t.right(90)



turtle.done()