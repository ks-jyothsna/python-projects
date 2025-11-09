from art import logo

print(logo)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        if bidding_dictionary[bidder] > highest_bid:
            highest_bid = bidding_dictionary[bidder]
            winner = bidder

    print("\n" * 50)
    print(f"The winner is {winner} with a bid of ${highest_bid}")


continue_bidding = True
bids = {}
while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_amount = float(input("What is your bid?: $"))
    bids[bidder_name] = bid_amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        print("\n" * 50)
    else:
        exit()


