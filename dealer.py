import random
import hand


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.player_hand = hand.Hand()
    #dealer logic for hitting or staying. if less than 17 hits. 
    def hit_or_stay(self, deck, isDealer=True):
        while self.player_hand.value < 17:
            new_card = deck.deal()
            self.player_hand.add_card(new_card, isDealer) 
            print("Dealer HITS")
        print("Dealer STAYS")
        return True
            
        #string for the dealer's hand. if reveal_first_card is true, it shows the dealer's full hand. normally you dont want this so it to show the face down card while player is choosing to bet. 
    def __str__(self, reveal_first_card=False):
        if reveal_first_card:
            dealer_hand = "Dealer's cards:\n"
            for card in self.player_hand.cards:
                dealer_hand += f'{card.rank} of {card.suit} -- {card.value} points\n'
            dealer_hand += f'Total dealer points = {self.player_hand.value}'
        else:
            dealer_hand = "Dealer's cards:\nDealer has one face down card\n"
            for card in self.player_hand.cards[1:]:
                dealer_hand += f'{card.rank} of {card.suit} -- {card.value} points\n'
            dealer_hand += 'Total visible dealer points = ' + str(sum(card.value for card in self.player_hand.cards[1:]))
        return dealer_hand