# Small $15
# Medium $20
# large $25

# pepperoni for small +$2
# pepperoni medium or large +$3
# extra cheese for any size +$1
print("Welcome to Pizza Shop")
size = input("What size pizza do you want S, M, or L : ")
add_pepperoni = input("Do you want pepperoni Y or N : ")
extra_cheese = input("Do you want extra cheese Y or N : ")
price_small = 15
price_medium = 20
price_large = 25
pepperoni_small = 2
pepperoni_medium_large = 3
extra_cheese_price = 1
if size == "S":
    bill = price_small
    if add_pepperoni == "Y":
        bill += pepperoni_small
    if extra_cheese == "Y":
        bill += extra_cheese_price
    print(f"Your bill is {bill}")

if size == "M":
    bill = price_medium
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
    if extra_cheese == "Y":
        bill += extra_cheese_price
    print(f"your bill is {bill}")

if size == "L":
    bill = price_large
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
    if extra_cheese == "Y":
        bill += extra_cheese_price
    print(f"Your bill is {bill}")
