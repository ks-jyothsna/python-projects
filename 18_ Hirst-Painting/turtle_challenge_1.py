# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
# All the shapes should be random colors. Each side should be 100 in length.

from turtle import Turtle, Screen
import random

timmy = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

def random_turtle_color():
    # r, g, and b represent an RGB color, and each of r, g, and b are in the range 0.0 to 1
    r_color = random.random()
    g_color = random.random()
    b_color = random.random()
    # pencolor takes a tuple (r, g, b)
    timmy.pencolor(r_color, g_color, b_color)

for shape_side_n in range(3,11):
    random_turtle_color()
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
