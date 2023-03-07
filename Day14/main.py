from game_data import data
import random
from art import logo, vs


def compare(data1, data2):
    if data1['follower_count'] > data2['follower_count']:
        return
    else:
        return


def get_data(data):
    return f"{data['name']}, a {data['description']}, {data['country']}"


def calc(choice, score_a, score_b):
    if score_a > score_b:
        return choice == "a"
    else:
        return choice == "b"


score = 0
end = False
account_b = random.choice(data)
while not end:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    account_a_score = account_a['follower_count']
    account_b_score = account_b['follower_count']
    print(logo)
    print(f"Compare A : {get_data(account_a)}")
    print(vs)
    print(f"Compare B : {get_data(account_b)}")

    user_choice = input("Enter your choice A or B ? : ").lower()
    if calc(user_choice, account_a_score, account_b_score):
        score += 1
        print(f"Your are correct, Your Score is {score}")
    else:
        end = True
        print(f"You are wrong, Current Score is {score}")
