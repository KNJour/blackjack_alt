
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.ace_reduced = False
    
    def add_card(self, new_card, isDealer):
        self.value += new_card.value
        self.cards.append(new_card)
        # dealer logic. Checks if dealer has less than 2 cards, if so, it plays the card face down.
        if isDealer:
            if len(self.cards) < 2:
                print("Dealer plays face down card")
            else:
                print(f'Dealer is dealt {new_card.rank} of {new_card.suit} -- {new_card.value}')
        #player logic. announces card, checks if card is ace to raise ace count. 
        else:
            print(f'Player dealt {new_card.rank} of {new_card.suit} -- {new_card.value}')
        if new_card.rank == 'Ace':
            self.aces += 1
    #first deal of the round. adds cards to the player's hand, and adjusts the value of the hand.
    def starting_deal(self, new_cards):
        for card in new_cards:
            self.cards.append(card)
            self.value += card.value
            if card.rank == "Ace":
                self.aces += 1
    
    #adjusts the value of the hand if the player has an ace and is over 21.S
    def ace_adjust(self):
        if self.aces > 0 and self.value > 21 and not self.ace_reduced:
            self.value -= 10
            print(f'Over 21 but has Ace, Ace Value Reduced, new amount: {self.value}')
            self.ace_reduced = True
        
    def __str__(self):
        for card in self.cards:
            print(f'{card.rank} of {card.suit} -- {card.value} points')
        return f'Player has {len(self.cards)} cards in hand, total value: {self.value}'
