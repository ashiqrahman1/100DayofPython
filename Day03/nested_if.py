height = int(input("Enter Your Height : "))
if height >= 120:
    print("You can Ride")
    age = int(input("Enter your age "))
    if age <= 12:
        print("You need to Pay $5")
    elif age > 12 and age <= 18:
        print("You need to Pay $7")
    elif age > 18 and age < 45:
        print("You need to pay $12")
    elif age >= 45 and age <= 55:
        print("You dont need to pay")
else:
    print("You can't Ride")
