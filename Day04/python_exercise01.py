# import random
# name = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# rand = random.randint(0, 4)
# print(f"{name[rand]} is going to buy the meal today!")

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(names)
# 🚨 Don't change the code above 👆
len = int(len(names)) - 1
r = random.randint(0, len)
print(f"{names[r]} is going to buy the meal today!")
