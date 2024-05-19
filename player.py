import card, hand

#starts a player class. has a name, chips, goal, hand, bet amount, and a boolean for standing.s
class Player:
    def __init__(self, name, chips, goal):
        self.name = name
        self.player_hand = hand.Hand()
        try: 
            amount = float(chips)
        except:
            print("not a valid number for chips, starting chips set to 500")
            amount = 500
        finally: 
            self.chips = amount
        self.bet_amount = "none"
        self.goal = goal
        self.stood = False
    
    def bet(self):
        while True:
            the_bet = input(f"You have ${self.chips} chips, how much would you like to bet?")
            try:
                the_bet = float(the_bet)
                # checks if enough chips are available to bet, if so, removes chips and creates bet amount
                if self.chips >= the_bet:
                    self.chips -= the_bet
                    self.bet_amount = the_bet
                    break
                else:
                    print("You don't have enough chips to bet that.")
            except ValueError:
                print("That is not a valid betting amount.")
    
    #gets them chips. double the bet amount.
    def get_chips(self, bet):
        winnings = bet * 2
        self.chips += winnings
        print(f"{self.name} wins {winnings} chips.")

    def hit(self, card, isDealer=False):
         # Check if the player has stood. If they havent they can hit. 
        if not self.stood: 
            print(f'{self.name} HITS')
            self.player_hand.add_card(card, isDealer)
        else:
            print(f"{self.name} cannot hit after standing.")
    
    def stay(self):
        self.stood = True
        print(f'{self.name} STANDS')

    def reset(self):
        self.player_hand = hand.Hand()
        self.stood = False 

    def __str__(self):
        return f'{self.name} has {self.chips} total chips.'
        