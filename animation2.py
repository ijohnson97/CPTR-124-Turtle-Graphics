## Name: Ian Johnson
## Date Last Modified: 9.16.16
## Program: Turtle Animation
## Purpose: Simple animation of a ball falling and bouncing
## Honesty Statement: I neither gave nor recieved unauthorized help on this code.
##
## END GOAL: Animate the Pixar ball falling, then bouncing across the screen.

from turtle import *

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
roll = 0
arc = 0

tracer(0)       ## Draw instantly
hideturtle()    ## Do not show the pen

def ballArc(h, k, a):       ## (h, k) specifies vertex; 'a' is shape of parabola
    global x, y, roll, arc
    while(True):
        if y >=  -280:       ## Animation of ball
            clear()             ## Clear previous drawings (after first iteration)
            
            # Draw 'floor'
            penup()
            pensize(3)
            setposition(-400,-275)
            setheading(0)
            pencolor(black)
            pendown()
            forward(750)
        
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
            penup()                             ## Allows pen to be positioned
            setposition(x, y + 6)               ## Set start postion to center star
            circle(radius - radius/4, -arc)     # Draw an arc
            pendown()                           ## Prepare pen for drawing            
            setheading(heading()+112)       ## Set direction of turtle
            fillcolor(red)                      ## Set fill color
            begin_fill()                        ## Begin defining shape to fill with color
            for i in range(0,5):                ## Draws star
                pensize(1)
                pencolor(red)
                forward(12)        
                left(72)    
                forward(12)        
                right(144)
            end_fill()          ## End defining shape to fill
            
            update()            ## Update drawings
            
            prevX = x
            prevY = y
            x += .25              ## Change x and y values so next rendering is moved
            y = a * (x-h)**2 + k  ## Creates a parabolic shape for the ball
            roll -= 1
            arc += 2
            
        else:
            currentX = x
            currentY = y
            #print('Current Y:',y)
            x = prevX
            y = prevY
            break
    
# All the magic happens here
ballArc(-275,100,-.5)       ## First bounce
print('1')
ballArc(-225,50,-.5)        ## Second bounce
print('2')
ballArc(-175, 25, -.5)      ## Third bounce
print('3')
ballArc(-130, 25, -.5)     ## Fourth bounce
print('4')
ballArc(-80, 0, -.25)       ## Fifth bounce
print('5')
ballArc(-20, -25, -.25)     ## Sixth bounce
print('6')
ballArc(30, -50, -.25)     ## Seventh bounce
print('7')
ballArc(80, -75, -.25)      ## Eighth bounce
print('8')
ballArc(120, -100, -.25)     ## Ninth bounce
print('9')
ballArc(150, -125, -.25)     ## Tenth bounce
print('10')
ballArc(170, -150, -.25)     ## Eleventh bounce
print('11')
ballArc(180, -175, -.25)    ## Twelfth bounce
print('12')
ballArc(125, -200, -.25)    ## Thirteenth bounce
print('13')
ballArc(150, -225, -.25)    ## Fourteenth bounce
print('14')
ballArc(175, -250, -.25)    ## Fifteenth bounce
print('15')

# Make the ball roll off screen
while(x <=  350):           ## While ball is on screen
        clear()             ## Clear previous drawings (after first iteration)
        
        # Draw 'floor'
        penup()
        pensize(3)
        setposition(-400,-275)
        setheading(0)
        pencolor(black)
        pendown()
        forward(750)
    
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
        penup()                             ## Allows pen to be positioned
        setposition(x, y + 6)               ## Set start postion to center star
        circle(radius - radius/4, -arc)     ## Draw an arc
        pendown()                           ## Prepare pen for drawing            
        setheading(heading()+112)           ## Set direction of turtle
        fillcolor(red)                      ## Set fill color
        begin_fill()                        ## Begin defining shape to fill with color
        for i in range(0,5):                ## Draws star
            pensize(1)
            pencolor(red)
            forward(12)        
            left(72)    
            forward(12)        
            right(144)
        end_fill()          ## End defining shape to fill
        
        update()            ## Update drawings
        
        x += 1              ## Change x and y values so next rendering is moved
        arc += 2            ## Change arc length

done()