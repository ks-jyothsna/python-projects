# Hirst Painting - Painting of dots.
# 10 X 10 rows of spots
# Each dot is 20 in size and spaced 50 paces
# Refer to extract_colors_from_image.py to check how color palette are extracted from an image

import turtle
import random

color_list = [(185, 176, 5), (186, 3, 69), (5, 143, 36), (243, 22, 152), (198, 5, 2),
              (241, 66, 4), (43, 195, 237), (88, 2, 91), (5, 130, 207), (248, 69, 14), (234, 155, 52),
              (234, 12, 135), (240, 224, 59), (10, 169, 130), (250, 229, 0), (216, 129, 180)]

color_list2 = [(202, 164, 110), (236, 239, 243),(149, 75, 50), (222, 201, 136),
               (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
               (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),(160, 142, 158), (54, 45, 50),
               (101, 75, 77)]

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed("fast")


# Starting position
x_position = -240
y_position = -240

for _ in range(10):
    timmy.teleport(x_position, y_position)
    for _ in range(10):
        timmy.pencolor(random.choice(color_list2)) # Choose color_list2 or color_list for different colors
        timmy.dot(20)
        timmy.forward(50)

    y_position += 50


screen = turtle.Screen()
screen.exitonclick()