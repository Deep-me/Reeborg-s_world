def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
for i in range (0,6):
    move()
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
     
