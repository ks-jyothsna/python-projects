# colorgram is an external python library that lets you extract colors from images.

import colorgram

colors = colorgram.extract('image.jpg', 20)
rgb_colors =  []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_colors.append(rgb)
print(rgb_colors)

# manually remove the unnecessary white colors from the list rgb_colors
# The above is done by checking each color https://www.w3schools.com/colors/colors_rgb.asp and deleting the not required ones.
# I have deleted first four tuples that were close to white.

# colors from image_2.jpg
color_list = [(185, 176, 5), (186, 3, 69), (5, 143, 36), (243, 22, 152), (198, 5, 2),
              (241, 66, 4), (43, 195, 237), (88, 2, 91), (5, 130, 207), (248, 69, 14), (234, 155, 52),
              (234, 12, 135), (240, 224, 59), (10, 169, 130), (250, 229, 0), (216, 129, 180)]


# colors from image.jpg
color_list2 = [(202, 164, 110), (236, 239, 243),(149, 75, 50), (222, 201, 136),
               (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
               (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),(160, 142, 158), (54, 45, 50),
               (101, 75, 77)]

# This color_list is copied manually to the main.py.