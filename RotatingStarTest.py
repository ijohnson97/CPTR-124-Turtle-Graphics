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
radius = 100 ## Radius of ball
x = -275    ## Inital 'x' position
y = -275     ## Inital 'y' position
roll = 0
arc = 0
circX = x - 35
circY = y + 30

tracer(0)       ## Draw instantly
hideturtle()    ## Do not show the pen

while(x <= 300):       ## Animation of ball
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
    pensize(16)
    setposition(x,y)    ## Set new Turtle position
    pendown()
    begin_fill()        ## Define shape that will be filled
    circle(radius)      ## Draw a circle with the user-defined radius
    end_fill()          ## End defining shapes that will be filled    
    
    #  Draw a star
    penup()                             ## Allows pen to be positioned
    setposition(x, y + 30)              ## Set start postion to center star
    circle(radius - 25, -arc)            # Draw an arc    
    setheading(heading()+112)  ## Set direction of turtle
    pendown()                           ## Prepare pen for drawing    
    fillcolor(red)                      ## Set fill color
    begin_fill()                        ## Begin defining shape to fill with color
    for i in range(0,5):                ## Draws star
        pensize(1)
        pencolor(red)
        forward(50)        
        left(72)    
        forward(50)        
        right(144)
    end_fill()          ## End defining shape to fill
    
    update()            ## Update drawings
    
    prevX = x
    prevY = y
    x += 1              ## Change x and y values so next rendering is moved
    #roll += 2.75
    arc += 2