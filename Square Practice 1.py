import turtle       #import the turtle method
t=turtle.Turtle()   #intialize the turtle

length = 100        # declaring the length of the square

for x in range(4):       # for loop to active 4 times
    t.forward(length)    # moving the pen forward with particular length
    t.left(90)           # turn the pen angle 90 degree
turtle.done()           # keep the screen on