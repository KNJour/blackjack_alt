
# gets the variables going for the class. suits, ranks, and values. suits and ranks are for reading the string of the card, values is for the actual value the card has in the game. 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10,
    'Ace' : 11
}

# class for the card. needs rank and suit. value is calculated from the values dictionary. 
class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
# returns the string of the card so it can be read.
    def __str__(self):
        return f'{self.rank} of {self.suit}'