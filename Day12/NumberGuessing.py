import random
random_number = random.randint(0, 100)
print(random_number)


def guess_number(number):
    if number == random_number:
        return "You Won"
    elif number > random_number:
        return "Too High"
    else:
        return "Too Low"


def calc():
    user_input = int(input("Make a Guess: "))
    return guess_number(user_input)


print("Welcome to Number Guessing Game!")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
end = False
attempt_easy = 10
attempt_hard = 5
while not end:
    if level == 'easy':
        print(f"You have {attempt_easy} remaining to gues the number ")
        result = calc()
        print(result)
        if result == "You Won":
            # print("You Find the Correct Number")
            end = True
        else:
            attempt_easy -= 1

        if attempt_easy == 0:
            print("Ran out of gas ")
            end = True

    elif level == 'hard':
        print(f"You have {attempt_hard} remaining to gues the number ")
        result = calc()
        print(result)
        if result == "You Won":
            # print("You Find the Correct Number")
            end = True
        else:
            attempt_hard -= 1

        if attempt_hard == 0:
            print("Ran out of gas ")
            end = True

    else:
        print("Wrong Choice.. Exiting")
        end = True
