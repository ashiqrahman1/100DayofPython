import colorgram
import turtle as turtle_module
import random
# color = colorgram.extract('image.jpg', 30)
# my_color = []
# for i in color:
#     my_color.append((i.rgb.r, i.rgb.g, i.rgb.b))
#     # my_color.append(mycolor.rgb.g)
#     # my_color.append(mycolor.rgb.b)
# print(my_color)
color_list = [(207, 158, 82), (54, 89, 130), (144, 91, 40), (139, 27, 50), (221, 207, 105), (132, 177, 202), (157, 47, 83), (45, 55, 104), (169, 160, 40), (130, 189, 143), (83, 20, 44), (38, 43, 65), (186, 93, 107),
              (186, 140, 171), (86, 118, 179), (58, 39, 32), (89, 156, 93), (79, 153, 164), (195, 80, 72), (79, 74, 44), (45, 74, 77), (59, 128, 120), (162, 202, 216), (44, 76, 76), (220, 175, 186), (178, 188, 213)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
# tim.pensize(10)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
# for y in range(10):


# ColorDot()
screen = turtle_module.Screen()
screen.exitonclick()
