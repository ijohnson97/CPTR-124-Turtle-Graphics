## Name: Ian Johnson
## Date Last Modified: 9.16.16
## Program: Turtle Animation
## Purpose: Simple animation of a ball falling and bouncing
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.
##
## END GOAL: Animate the Pixar ball falling, then bouncing across the screen.

from turtle import *
import math as m

# Define colors
purple = (1,0,1)
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)
yellow = (1,1,0)
azure = (0,1,1)
black = (0,0,0)
white = (1,1,1)

# Define a few variables for future reference
radius = 25 ## Radius of ball
x = -275    ## Inital 'x' position
y = 100     ## Inital 'y' position

tracer(0)       ## Draw instantly
hideturtle()    ## Do not show the pen

def ballArc(xSpeed, ySpeed, direction, height):
    global x, y, vi, theta, g, t
    if direction == up:
        while y <= height:      ## Animation of ball falling
            clear()             ## Clear previous drawings (after first iteration)
            
            # Draw 'floor'
            penup()
            pensize(3)
            setposition(-400,-275)
            setheading(0)
            pencolor(black)
            pendown()
            forward(750)
        
            penup()
            pensize(1)
            pencolor(red)
            setposition(0,-800)
            setheading(90)
            pendown()
            forward(1600)
            
            penup()
            setposition(-800,0)
            setheading(0)
            pendown()
            forward(1600)
            
            # Draw circle
            penup()
            fillcolor(yellow)
            pencolor(blue)
            pensize(4)
            setposition(x,y)    ## Set new Turtle position
            pendown()
            begin_fill()        ## Define shape that will be filled
            circle(radius)      ## Draw a circle with the user-defined radius
            end_fill()          ## End defining shapes that will be filled
            
            #  Draw a star
            penup()                 ## Allows pen to be positioned
            setposition(x-8,y+15)     ## Set start postion to center star
            setheading(72)          ## Set direction of turtle
            fillcolor(red)          ## Set fill color
            pendown()               ## Prepare pen for drawing
            begin_fill()            ## Begin defining shape to fill with color
            for i in range(1,6):    ## Draws star
                pensize(1)
                pencolor(red)
                forward(10)        
                left(72)    
                forward(10)        
                right(144)
            end_fill()          ## End defining shape to fill
            
            update()            ## Update drawings
            x += xSpeed        ## Change x and y values so next rendering is moved
            y += ySpeed

# THIS SECTION DOESN'T WORK
    else:
        while y >= height:        ## Animation of ball falling
            clear()             ## Clear previous drawings (after first iteration)
            
            # Draw 'floor'
            penup()
            pensize(3)
            setposition(-400,-275)
            setheading(0)
            pencolor(black)
            pendown()
            forward(750)
            
            penup()
            pensize(1)
            pencolor(red)
            setposition(0,-800)
            setheading(90)
            pendown()
            forward(1600)
            
            penup()
            setposition(-800,0)
            setheading(0)
            pendown()
            forward(1600)
                        
            # Draw circle
            penup()
            fillcolor(yellow)
            pencolor(blue)
            pensize(4)
            setposition(x,y)    ## Set new Turtle position
            pendown()
            begin_fill()        ## Define shape that will be filled
            circle(radius)      ## Draw a circle with the user-defined radius
            end_fill()          ## End defining shapes that will be filled
            
            #  Draw a star
            penup()                 ## Allows pen to be positioned
            setposition(x-8,y+15)     ## Set start postion to center star
            setheading(72)          ## Set direction of turtle
            fillcolor(red)          ## Set fill color
            pendown()               ## Prepare pen for drawing
            begin_fill()            ## Begin defining shape to fill with color
            for i in range(1,6):    ## Draws star
                pensize(1)
                pencolor(red)
                forward(10)        
                left(72)    
                forward(10)        
                right(144)
            end_fill()          ## End defining shape to fill
            
            update()            ## Update drawings
            x += xSpeed        ## Change x and y values so next rendering is moved
            y -= ySpeed
            
# Animation happens here

ballArc(.25,4,down,-275)
ballArc(1.25,4,up,-100)
ballArc(.75,4,down,-275)    
ballArc(1,4,up,-150)
ballArc(.75,4,down,-275)
ballArc(1,4,up,-175)
ballArc(1,4,down,-275)

done()