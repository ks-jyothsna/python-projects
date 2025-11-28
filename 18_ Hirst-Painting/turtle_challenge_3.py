# Make a Spirograph - Draw number of circles, each with radius 100

from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.pensize(3)
timmy.speed("fastest")

def random_turtle_color():
    # r, g, and b represent an RGB color, and each of r, g, and b are in the range 0.0 to 1
    r_color = random.random()
    g_color = random.random()
    b_color = random.random()
    # pencolor takes a tuple (r, g, b)
    timmy.pencolor(r_color, g_color, b_color)

def draw_spirograph(size_of_the_gap):
    number_of_circle = int(360/size_of_the_gap)
    print(number_of_circle)
    for _ in range(number_of_circle):
        random_turtle_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_the_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()