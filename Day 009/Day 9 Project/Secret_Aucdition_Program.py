import os
import visual_resources

print(visual_resources.logo)
print("Welcome to the secret auction program.")
other_bidders = 'yes'

bidders_data = {}

while other_bidders == 'yes':
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))
    bidders_data[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or  'no'.\n").lower()
    if other_bidders == 'yes':
        os.system('cls')

# Using programming logic
# highest_bid = 0
# highest_bidder = ""
# for bidder in bidders_data:
#     if bidders_data[bidder] >highest_bid:
#         highest_bid = bidders_data[bidder]
#         highest_bidder = bidder
# print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

# Using python inbemded functions
print(f"The winner is {max(bidders_data)} with a bid of ${bidders_data[max(bidders_data)]}")