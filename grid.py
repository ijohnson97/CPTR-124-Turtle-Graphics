## Name: Ian Johnson
## Date Last Modified: 9.15.16
## Program: Turtle Grid
## Purpose: Draws a grid centered on screen based on user's input
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.

from turtle import *

boxSize = int(input('Please enter desired size of box: '))
boxRows = int(input('Please entere desired number of rows: '))
boxPerRow = int(input('Please enter desired number of boxs per row: '))

print('Box Size:',boxSize,'\nColumns:',boxPerRow,'\nRows:',boxRows)

# Used to determine where the graph should be centered
x = -(boxSize*boxRows)/2
y = (boxSize*boxPerRow-boxSize)/2

print(x)        ## For test purposes
print(y)        ## For test purposes

tracer(0)       ## Do not animate the pen
hideturtle()    ## Do not show the pen

# Draws a small square at the center of the screen (for test purposes)
penup()
home()
setposition(-5, -5)
pendown()
forward(10)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
right(90)

# Set start position to center the grid (THIS DOES NOT ACTUALLY WORK!!!!)

penup()
setposition(x,y)
setheading(90)
pendown()

# Draw a box

for t in range(0,boxRows):          ## Handles row progession
    for n in range(0,boxPerRow):    ## Handles columns
        for i in range(0,4):        ## Draws each individual square
            forward(boxSize)
            right(90)            
        
        # Moves turtle to next sqaure
        penup()
        setposition(xcor()+boxSize,ycor())
        pendown()
    
    # Moves turtle to next column
    penup()
    setposition(xcor()-(boxSize*boxPerRow),ycor()-boxSize)
    pendown()

done()          ## Refreshes window