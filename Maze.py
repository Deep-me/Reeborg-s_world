def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right()==False:
        turn_right()
        move()
    elif front_is_clear():
        move()
