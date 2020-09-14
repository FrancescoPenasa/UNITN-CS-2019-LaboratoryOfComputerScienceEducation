### da fare con shell interattiva e poi con l'esecuzione di file ###

# importiamo il package turtle
import turtle

# inizializzazione
s = turtle.getscreen() # mostra la finestra
t = turtle.Turtle() # inizializzamo la tartaruga
t.speed(1) # facciamo andare la tartaruga piano

# possibili movimenti
t.forward(100) # vai avanti di x pixel
t.left(90) # girati a sinistra di x gradi  # MISCONCEPTION (la tartaruga cosa fa? si muove?)
t.right(90) # girati a destra di x gradi
t.backward(100) # vai nella direzione contraria di x pixel

# sposta la tartaruga in una coordinata specifica
t.goto(0, 0) # MISCONCEPTION (la tartaruga cosa fa? rimane ferma o si sposta?)
t.goto(50, 100) # vai alle coordinate (x, y)

# per non chiudere immediatamente
turtle.done()
