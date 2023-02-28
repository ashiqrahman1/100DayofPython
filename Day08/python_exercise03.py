# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
import math


def paint_calc(height, width, coverage):
    result = (height * width) / coverage
    # print(result)
    print(f"You need {math.ceil(result)}")


test_h = int(input("Enter the Height of Wall : "))
test_w = int(input("Enter the Width of Wall : "))
coverage = 5
paint_calc(height=test_h, width=test_w, coverage=coverage)
