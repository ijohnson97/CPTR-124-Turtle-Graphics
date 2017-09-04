## Name: Ian Johnson
## Date Last Modified: 9.15.16
## Program: Twinkle, Twinkle Little Star
## Purpose: Draws a star with alternating fill on the screen
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.

from turtle import *  # Make all the Turtle graphics functions available

tracer(0)
hideturtle()    ## Do not show the pen

# Define colors
purple = (1,0,1)
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)
yellow = (1,1,0)
azure = (0,1,1)
black = (0,0,0)
white = (1,1,1)

#  Draw a star
penup()                 ## Allows pen to be positioned
setposition(-99,-120)   ## Set start postion to center star
setheading(72)          ## Set direction of turtle
fillcolor(purple)       ## Set fill color
pendown()               ## Prepare pen for drawing
begin_fill()            ## Begin defining shape to fill with color
for i in range(1,6):    ## Draws star
    pensize(i)
    pencolor(azure)
    forward(300)        
    right(144)
end_fill()              ## End defining shape to fill

update()        ## Refresh window
done()          ## Wait for the user to close the window