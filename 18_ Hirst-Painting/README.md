# 🐢 Turtle Mini Challenges + Hirst Painting
> A fun Python project using the turtle graphics module to explore shapes, randomness, patterns, and color extraction.
This project contains three mini-challenges followed by a main Hirst-style painting project, all built using Python’s turtle module.

---
 
## 🐢 What Is the Turtle Module?
The turtle module is a built-in Python library used to create graphics, drawings, and animations using a virtual “turtle” that moves around the screen.
You can control the turtle’s movement, direction, color, and pen size, which makes it perfect for learning programming concepts visually.

General Uses of Turtle:
- Drawing shapes and patterns
- Creating simple animations
- Teaching loops and functions
- Building visual projects like spirographs, random walks, or dot paintings
- Helping beginners understand programming with instant visual feedback

---

## 🎨 Background on Hirst Painting
The main project is inspired by Damien Hirst, a British contemporary artist known for his colorful dot artworks. His famous Spot Paintings feature rows of perfectly spaced, brightly colored dots arranged in a grid.

In the turtle version of the Hirst painting:
- You create a 10 × 10 grid of evenly spaced dots
- Each dot uses a color extracted from a reference image (using the colorgram library)
- The project recreates the clean, vibrant, and repetitive style of Hirst’s dot paintings using code

It’s a great exercise in:
- Loops
- Grid movement
- Working with RGB colors
- Using external libraries to extract color palettes

---

## 📌 Mini Challenge 1 – Polygon Drawer
Goal: Draw the following shapes using Turtle:triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.  

Requirements:
- Each shape must have 100-unit sides.
- Each polygon should be drawn in a random color.
  
---

## 📌 Mini Challenge 2 – Random Walk
Goal: Create a “drunk turtle” random walk.

Requirements:
- Turtle moves in random directions: North, East, South, West.
- Each movement uses a random color.
  
---

## 📌 Mini Challenge 3 – Spirograph
Goal: Draw a spirograph-style circular pattern.

Requirements:
- Draw multiple circles of radius 100.
- Number of rotations determines pattern complexity.

---

## 🎨 Main Project – Hirst Painting  
Requirements:
- Canvas of 10 × 10 dots (100 dots total)
- Each dot:
  - Size: 20
  - Spacing: 50 units
- Colors are extracted using the colorgram library
  - colorgram module is an external module that extracts dominant colors from an input image

Note: There are two example images used to extract the color palette, refer to extract_colors_from_image.py to understand more on how colors are extracted from images and converted to r,g,b format list. 

---

## 📦 External Library Used

[colorgrag.py](https://pypi.org/project/colorgram.py/) : Used to extract colors from an inspiration image.
- Refer the main README.md file to know more on how to insatll the external library package to the environment.
