from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.pencolor("purple")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
   tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear() #delete the drawing
    tim.penup() #bring turtle back to starting point
    tim.home()
    tim.pendown()

screen.listen() #to listen the keyboard strokes and clicks

screen.onkey(key= "w", fun=move_forward) #higher order function - function called in a function
screen.onkey(key= "s", fun=move_backward)
screen.onkey(key= "a", fun=turn_left)
screen.onkey(key= "d", fun=turn_right)
screen.onkey(key= "c", fun=clear_screen)


screen.exitonclick()