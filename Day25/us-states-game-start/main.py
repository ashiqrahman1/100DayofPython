import turtle
import pandas as pd
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US state Game")
screen.addshape(image)
turtle.shape(image)
guess_states = []
data = pd.read_csv("50_states.csv")
newdata = data.state.to_list()
while len(guess_states) < 50:
    answer = screen.textinput(
        "Guess the State", "Enter the state name ").title()
    print(answer)

    if answer == "Exit":
        missed_state = []
        for i in newdata:
            if i not in guess_states:
                missed_state.append(i)
        new_data = pd.DataFrame(missed_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer in newdata:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

# def get_mouse_click_coor(x, y):
#     print(x, y)


# # add_dot(xcor, ycor)
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
# # screen.exitonclick()
