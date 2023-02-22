# Tip Calculator
print("Welcom to the tip calculator")
amount = float(input("What was the total bill? $"))
percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

amount_percentage = amount + (amount * percentage / 100)
total = amount_percentage / number_of_people
print(f"each person should pay {round(total, 2)}")
