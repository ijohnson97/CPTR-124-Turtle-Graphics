## Name: Ian Johnson
## Date Last Modified: 9.15.16
## Program: Turtle Grid
## Purpose: Draws a grid centered on screen based on user's input
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.

from turtle import *

tracer(0)
hideturtle()

#boxSize = int(input('Please enter desired size of box: '))
#boxRows = int(input('Please entere desired number of rows: '))
#boxPerRow = int(input('Please enter desired number of boxs per row: '))

penup()
setposition(-125, 125)
pendown()

for i in range(11):
    forward(250)
    penup()
    setposition(-125, ycor() - 25)
    pendown()

penup()
setposition(-125, 125)
setheading(270)
pendown()

for n in range(11):
    forward(250)
    penup()
    setposition(xcor() + 25, 125)
    pendown()

update()
done()