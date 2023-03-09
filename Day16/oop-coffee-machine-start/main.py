from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu = Menu()
myCoffee = CoffeeMaker()
# myItem = MenuItem()
Money = MoneyMachine()
off = False
while not off:
    myChoice = input(f"What Would you Like {myMenu.get_items()} : ")
    if myChoice == "off":
        off = True
    elif myChoice == "report":
        myCoffee.report()
        Money.report()
    else:
        drink = myMenu.find_drink(myChoice)
        # check resource
        if myCoffee.is_resource_sufficient(drink):
            # Payment Part
            if Money.make_payment(drink.cost):
                myCoffee.make_coffee(drink)
