from art import logo
print(logo)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def calculate():
    print(logo)
    end = False
    first_number = float(input("Enter the First Number : "))
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    for x in ops:
        print(x)

    while not end:
        operation = str(input("Pick an Operation "))
        second_number = float(input("Enter the Next Number : "))
        check = ops[operation]
        first_result = check(first_number, second_number)
        print(first_result)
        choice = input(
            "Type 'y' to continue , or Type 'n' to start from beginning : ")
        if choice == "y":
            first_number = first_result
        else:
            end = True
            calculate()


calculate()
