from art import logo
print(logo)

auction_list = []
auction_end = False


def add_auction_info(username, bid_amount):
    data = {
        "username": username,
        "bid": bid_amount
    }

    auction_list.append(data)


print("Welcome to the Secret Auction Program")
while not auction_end:
    user_name = input("What is your name? :")
    user_bid = int(input("what is your bid? : "))
    add_auction_info(user_name, user_bid)
    play_again = input(
        "Are there any Other bidders? Type 'yes' or 'No' ").lower()
    if play_again == "no":
        auction_end = True

num = 0
user = 0
for i in range(len(auction_list)):
    if auction_list[i]['bid'] > num:
        num = auction_list[i]['bid']
        user = i
print(f"{auction_list[user]['username']} have won")
