import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Enter the 0 for Rock, 1 for Papper, 2 for Scissors "))
asci_list = [rock, paper, scissors]
random_number = random.randint(0, 2)
print(asci_list[choice])
print("computer Chose :")
print(asci_list[random_number])

if choice == random_number:
    print("Draw")
elif choice == 0 and random_number == 1:
    print("you Lose")
elif choice == 0 and random_number == 2:
    print("you Won")
elif choice == 1 and random_number == 0:
    print("You Won")
elif choice == 1 and random_number == 2:
    print("You Lose")
elif choice == 2 and random_number == 0:
    print("You Lose")
elif choice == 2 and random_number == 1:
    print("You Won")
