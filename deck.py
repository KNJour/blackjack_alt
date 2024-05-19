import card

import random

class Deck:
    def __init__(self):
        self.all_cards = []
        for x in card.suits:
            for y in card.ranks:
                # adds a card to the deck "all_cards" for each suit and rank
                self.all_cards.append(card.Card(y, x))

    # shuffles the dec. first it empties the deck, then shuffles the deck, then returns the deck.
    def shuffle_the_deck(self):
        self.all_cards.clear()
        for x in card.suits:
            for y in card.ranks:
                self.all_cards.append(card.Card(y, x))
        # shuffles the deck after repopulating with new deck
        random.shuffle(self.all_cards)

    # deals a card from the deck. returns the last card "popped" from the deck
    def deal(self):
        return self.all_cards.pop()
    
    # returns the number of cards left in the deck. idk if this is useful or not.
    def __str__(self):
        return f'the deck has {len(self.all_cards)} cards remaining'
