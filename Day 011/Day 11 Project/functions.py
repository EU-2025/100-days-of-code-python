import random

def ascii_card(value, suit):
    suits_symbols = {
        'spades':   '♠',
        'hearts':   '♥',
        'diamonds': '♦',
        'clubs':    '♣'
    }
    values = {
    1: "A",    # As
    2: "2",    # Two
    3: "3",    # Three
    4: "4",    # Four
    5: "5",    # Five
    6: "6",    # Six
    7: "7",    # Seven
    8: "8",    # Eight
    9: "9",    # Nine
    10: "10",  # Ten
    11: "J",   # Jack
    12: "Q",   # Queen
    13: "K"    # King
}

    val = values[value]
    sym = suits_symbols[suit.lower()]
    space = ' ' if len(val) == 1 else ''

    card = [
        "┌─────────┐",
        f"│{val}{space}       │",
        "│         │",
        f"│    {sym}    │",
        "│         │",
        f"│       {space}{val}│",
        "└─────────┘"
    ]
    return card

def print_cards_side_by_side(cards):
    card_lines = [ascii_card(val, suit) for val, suit in cards]
    for i in range(7):  # Cada carta tiene 7 líneas
        print('  '.join(card[i] for card in card_lines))


def random_card():
    symbols = ["spades", "hearts", "diamonds", "clubs"]
    card = (random.randint(1, 13),random.choice(symbols))
    return card

def sum_deck(cards):
    total = 0
    for card in cards:
        total += card[0]
    return total
