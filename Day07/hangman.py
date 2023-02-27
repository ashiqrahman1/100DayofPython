import random
from hangmanart import logo, stages
from hangmanwords import word_list

print(logo)
my_word = random.choice(word_list).lower()
print(my_word)
my_list = []

for i in my_word:
    my_list += "_"
end_of_game = False
live = 7
while not end_of_game:
    guess = input("Enter the Letter : ")

    for i in range(len(my_word)):
        letter = my_word[i]
        if letter == guess:
            my_list[i] = letter

    print(' '.join(my_list))
    # print(my_list)
    if guess not in my_word:
        live -= 1
        print(stages[live])
        if live == 0:
            end_of_game = True
            print("You Lose")

    if "_" not in my_list:
        end_of_game = True
        print("You Win")
