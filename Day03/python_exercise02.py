print("Welcome")
person_1 = input("Enter your name ").lower()
person_2 = input("Enter their name ").lower()

# checking true
true_count_person1 = 0
true_count_person1 += person_1.count("t")
true_count_person1 += person_1.count("r")
true_count_person1 += person_1.count("u")
true_count_person1 += person_1.count("e")

true_count_person2 = 0
true_count_person2 += person_2.count("t")
true_count_person2 += person_2.count("r")
true_count_person2 += person_2.count("u")
true_count_person2 += person_2.count("e")

total_true = true_count_person1 + true_count_person2

# check love
love_count_person1 = 0
love_count_person1 += person_1.count("l")
love_count_person1 += person_1.count("o")
love_count_person1 += person_1.count("v")
love_count_person1 += person_1.count("e")

love_count_person2 = 0
love_count_person2 += person_2.count("l")
love_count_person2 += person_2.count("o")
love_count_person2 += person_2.count("v")
love_count_person2 += person_2.count("e")

total_love = love_count_person1 + love_count_person2

total = str(total_true) + str(total_love)
if int(total) < 10 and int(total_love) > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif int(total) >= 40 and int(total) <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
