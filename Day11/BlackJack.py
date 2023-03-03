import random


def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_total, computer_total):
    if user_total == computer_total:
        return "Draw"
    elif computer_total == 0:
        return "You Lose"
    elif user_total == 0:
        return "You Win"
    elif user_total > 21:
        return "You Lose"
    elif computer_total > 21:
        return "You Win"
    elif user_total > computer_total:
        return "You Win"
    else:
        return "You Lose"


user_card = []
computer_card = []
is_over = False

while not is_over:
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    user_sum = calculate(user_card)
    computer_sum = calculate(computer_card)
    print(f"Your Card : {user_card} and your sum is {user_sum}")
    print(f"Computer First Card : {computer_card[0]}")
    if user_sum == 0 or computer_sum == 0 or user_sum > 21:
        is_over = True
    else:
        choice = input("Type 'y' get another card, type 'n' to Pass: ")
        if choice == 'y':
            user_card.append(deal_card())
        else:
            is_over = True

while computer_sum != 0 and computer_sum < 17:
    computer_card.append(deal_card())
    computer_sum = calculate(computer_card)

print(f"   Your final hand: {user_card}, final score: {user_sum}")
print(
    f"   Computer's final hand: {computer_card}, final score: {computer_sum}")
print(compare(user_sum, computer_sum))
# print(compare(user_sum, computer_sum))
