print("Welcome to Treasure Island")
print("Your Missin is Find the trasure")
direction = input(
    'Your at a cross road, where do you want to go? Type "left" or "right" ').lower()

if direction == "left":
    action = input(
        "You come to a lake. there is a island in the middle of the lake, type wait to wait boat, of type swim to swim ").lower()
    if action == "wait":
        door = input(
            "You arrive at the islan unharmed, there is a house with 3 door, blue yello and red which one you choose ").lower()
        if door == "yellow":
            print("winner")
        elif door == "red":
            print("Game Over")
        elif door == "red":
            print("Game over")
    else:
        print("game over")
else:
    print("Game over")
