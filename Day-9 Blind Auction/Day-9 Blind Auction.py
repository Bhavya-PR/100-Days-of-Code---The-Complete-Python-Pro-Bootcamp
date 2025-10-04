import art
print(art.logo)
print("Welcome to the secret auction program.")
auction = {}
next_user = True
while next_user:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    next_user_presence = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if next_user_presence == "no":
        next_user = False
    else:
        print("\n" * 100)
# max_bid_name = max(auction,key=auction.get)
# max_bid = auction[max_bid_name]
max_bid_name = ""
max_bid = 0
for key in auction:
    if auction[key] > max_bid:
        max_bid_name = key
        max_bid = auction[key]
print(f"The winner is {max_bid_name} with a bid of {max_bid}.")