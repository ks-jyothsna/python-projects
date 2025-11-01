def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Workaround to solve exceptions of infinite loop, Solution: make sure there is a wall in front, and turn left to start.
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
