MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def report():
    for x in resources:
        print(f"{x} {resources[x]}")


def calc(quarters, dime, nickel, penny):

    return round((quarters * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01), 2)


def check(user_total, coffe_price):
    if user_total >= coffe_price:
        change = user_total - coffe_price
        print(f"Here your exchange {change}")
        global profit
        profit += coffe_price
        return True
    else:
        print("You Dont have enough money to buy drink")
        return False


def check_resource(user_resource):
    for x in user_resource:
        if user_resource[x] > resources[x]:
            print(f"{x} not enough")
            return False
    else:
        return True


def makecoffee(choice, ingredients):
    for x in ingredients:
        resources[x] -= ingredients[x]
    print(f"Here you {choice} Enjoy")


machine_off = False
while not machine_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        machine_off = True
    elif user_input == "report":
        report()
    else:
        user_drink = MENU[user_input]
        # check resource availability
        if check_resource(user_drink['ingredients']):
            # payment Part
            quarters = int(input("How Many quarters "))
            dime = int(input("How many dimes "))
            nickel = int(input("How many nickel "))
            penny = int(input("How many penny "))
            total = calc(quarters, dime, nickel, penny)
            # check user input price and drink price
            if check(total, user_drink["cost"]):
                makecoffee(user_input, user_drink["ingredients"])
