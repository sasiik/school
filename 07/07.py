import random

# -----------------------
# Task 1: Dictionary Manipulation and Functions
# -----------------------

# Initial dictionaries
inventory = {
    "potato": 15,
    "apple": 10,
    "kiwi": 13,
    "turnip": 7
}

price = {
    "potato": 1,
    "apple": 2,
    "kiwi": 1.5,
    "turnip": 0.5
}

# (a) Adjust the dictionaries:
# - Add 10 new potatoes
# - Add 5 pears (priced at 1.5)
inventory["potato"] += 10
inventory["pear"] = 5
price["pear"] = 1.5

print("After updating inventory and price:")
print("Inventory:", inventory)
print("Price:", price)

# (b) Function that raises all prices by 10


def raise_prices(price_dict):
    for key in price_dict:
        price_dict[key] += 10


# Testing the raise_prices function
raise_prices(price)
print("\nAfter raising prices by 10:")
print("Price:", price)

# (c) Function that calculates the total worth of the inventory


def total_worth(inventory_dict, price_dict):
    total = 0
    for item in inventory_dict:
        # Multiply quantity by price if the item exists in the price dictionary
        if item in price_dict:
            total += inventory_dict[item] * price_dict[item]
    return total


print("\nTotal inventory worth:", total_worth(inventory, price))


# -----------------------
# Task 2: Swap Dictionary Keys and Values
# -----------------------

def convert_dict(d):
    # Create a new dictionary with keys and values swapped
    swapped = {v: k for k, v in d.items()}
    # Clear the original dictionary and update it with swapped pairs
    d.clear()
    d.update(swapped)


# Example dictionary where original keys are integers and values are strings
example = {100: "velocity", 101: "humidity", 102: "SNR", 103: "RSSI"}
convert_dict(example)
print("\nSwapped dictionary:", example)


# -----------------------
# Task 3: Count String Appearances in a List
# -----------------------

# (a) Using nested loops (here, the count() method is used, which under the hood loops over the list)
def max_count_nested(strings):
    max_count = 0
    for s in strings:
        count = strings.count(s)
        if count > max_count:
            max_count = count
    return max_count

# (b) Using a dictionary to keep track of counts


def max_count_dict(strings):
    counts = {}
    for s in strings:
        counts[s] = counts.get(s, 0) + 1
    return max(counts.values()) if counts else 0


# Testing with a sample list
test_list = ["aaaa", "bbbb", "aaaa", "cccc", "cccc", "bbbb", "cccc"]
print("\nMax count (nested loops):", max_count_nested(test_list))
print("Max count (dictionary):", max_count_dict(test_list))

print("\nNote: The dictionary approach (O(n)) is more efficient than using nested loops (O(n²)) for large lists.")


# -----------------------
# Task 4: Working with a Deck of Cards
# -----------------------

# Define suits and card values
suits = ['clubs', 'diamonds', 'hearts', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(s, v) for s in suits for v in values]

# (a) Calculate the number of cards in the deck
print("\nTotal cards in deck:", len(deck))  # Expected output: 52

# (b) Change the suit of the second card ('clubs', '3') to ('spades', '3')
# Since tuples are immutable, we create a new tuple and replace it in the list.
deck[1] = ('spades', deck[1][1])
print("Second card after suit change:", deck[1])
# Notion: You can’t modify an immutable tuple in place; you replace the entire tuple in the list.

# (c) Shuffle the deck
random.shuffle(deck)
print("\nDeck after shuffling:")
print(deck)

# (d) Take one random card and print it in the form "suit value"
card = random.choice(deck)
print("\nRandom card:", f"{card[0]} {card[1]}")

# (e) Deal the cards for 4 players (evenly, each gets 13 cards)
players = [[], [], [], []]
for i, card in enumerate(deck):
    players[i % 4].append(card)

print("\nCards dealt for 4 players:")
for i, hand in enumerate(players):
    print(f"Player {i+1}'s hand: {hand}")


# -----------------------
# Task 5: Deal a Five-Card Hand and Check for a Straight
# -----------------------

def is_straight(hand):
    """
    Determines if the hand is a straight.
    Converts card values to integers, sorts them, and checks for consecutive numbers.
    """
    # Map card values to integers
    value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    # Extract and sort the numeric values from the hand
    nums = [value_map[card[1]] for card in hand]
    nums.sort()

    # Check for consecutive values using a loop
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] != 1:
            return False
    return True


# Deal a five-card hand from the shuffled deck (for simplicity, take the first five cards)
hand = deck[:5]
print("\nFive-card hand:", hand)
if is_straight(hand):
    print("The hand is a straight.")
else:
    print("The hand is not a straight.")
