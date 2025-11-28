# Draw a random walk, turtle making random movement north, east, south, west.
# Random color for each shift.

import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
# turtle.colormode(255) is done to use the range 0-255 instead of 0.0 - 1.0
turtle.colormode(255)

def random_turtle_color():
    # r, g, and b represent an RGB color, and each of r, g, and b are in the range 0 to 255
    r_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    # pencolor takes a tuple (r, g, b)
    timmy.pencolor((r_color, g_color, b_color))

direction = [0, 90, 180, 270]
timmy.pensize(10) # to increase the width of pen
timmy.speed("fastest") # to increase the speed of animation

for _ in range(200):
    random_turtle_color()
    timmy.setheading(random.choice(direction))
    timmy.forward(30)


screen = Screen()
screen.exitonclick()