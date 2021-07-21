#Successful Code ----> Good Output
#DONT FORGET THE IDENTATION CONCEPT
import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(0)

# Function for draw a square
def square(length,angle):
 for i in range(4):
   my_turtle.forward(length)
   my_turtle.right(angle)

# For loop to draw circle with square
for i in range (5):
 square(100,90)
 my_turtle.right(11)