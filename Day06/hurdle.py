while not at_goal():
    if front_is_clear():
        move()
    elif wall_on_front():
        turn_left()
        if right_is_clear():
            move()
        else:
            barrier()
    else:
        move()
