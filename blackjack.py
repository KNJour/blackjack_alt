import dealer, player, deck, hand


# GAME SETUP
#Gets the name, the amount of chips, and the goal chips as variables then greats the player.
name = str(input("What is your name?"))
try:
    chips = int(input("How many chips would you like to start with?"))
except ValueError:
    print("Invalid amount of chips, starting with 100 chips.")
    chips = 100

try:
    goal = int(input("How many chips to win?"))
    if goal <= chips:
        print(f"Invalid amount of chips, setting default chips of {chips * 3}")
        goal = chips * 3
except ValueError:
    print("Invalid amount of chips, setting default 300 chips to win")
    goal = 300

#creates player, dealer, deck and round variables
player1 = player.Player(name, chips, goal)

the_dealer = dealer.Dealer()
game_deck = deck.Deck()
game_on = True
round = 0
#functions to check if the player busted, and to reset the hand and player variables between rounds. 
def bust_check(player):
    player.player_hand.ace_adjust()
    if player.player_hand.value > 21:
        print(f"{player.name} has {player.player_hand.value} points and BUSTS!!")
        return True
    else: return False
    
def reset(player, dealer, game_deck):
    player.reset()
    player.player_hand = hand.Hand()
    dealer.player_hand = hand.Hand()
    game_deck.shuffle_the_deck()
    
#checks if someone won the game by reaching their goal.
def win_check(player):
    if player.chips >= player.goal:
        print(f'{player.name} has reached their goal of {player.goal} chips!')
        return True
    else:
        return False
    
    #while loop that starts the game
while game_on:
    #starts by calling reset, to make sure everythign starts squeaky clean.s
    reset(player1, the_dealer, game_deck)
    round += 1
    round_on = True
    print(f'Round {round}... START!')
    game_deck.shuffle_the_deck()
    #player bets
    player1.bet()
    #deals to player and the dealer
    print("---------------DEALING----------------")
    print("----DEALER CARDS---")
    the_dealer.player_hand.starting_deal([game_deck.deal(), game_deck.deal()])
    print(the_dealer)
    print("----PLAYER CARDS---")
    player1.player_hand.starting_deal([game_deck.deal(), game_deck.deal()])
    print(player1.player_hand)
    #initiates the start of a round. 
    while round_on:
        #checks if player has blackjackS
        if player1.player_hand.value == 21:
            player1.get_chips(player1.bet_amount)
            round_on = False
            break
            #asks player to hit or stay
        player_choice = input("Hit or Stay? H/S").lower()
        if player_choice == "h":
            player1.hit(game_deck.deal())
            print(f'{player1.name} has {player1.player_hand.value} points')
            if bust_check(player1):
                round_on = False
                print("DEALER WINS")
                break
            #if player stays, dealer plays. 
        elif player_choice == "s":
            player1.stay()
            print("Dealer reveals hidden card")
            #sets reveal card to true so the dealer shows the full hand.
            print(the_dealer.__str__(reveal_first_card=True))
            while the_dealer.hit_or_stay(game_deck) == False:
                pass
            print("-------Final Dealer Hand-------")
            print(the_dealer.__str__(reveal_first_card=True))
            round_on = False
            #checks who wins the round.
            if bust_check(the_dealer):
                print(f"Dealer BUSTS at {the_dealer.player_hand.value} points!")
                player1.get_chips(player1.bet_amount)
            else:
                if the_dealer.player_hand.value > player1.player_hand.value:
                    print("DEALER WINS")
                elif the_dealer.player_hand.value < player1.player_hand.value:
                    player1.get_chips(player1.bet_amount)
                else:
                    #if tie, you get the back back.
                    print("It's a TIE")
                    player1.chips += player1.bet_amount 

            print(f'{player1.name} now has {player1.chips} chips.')
    #checks if player has reached their goal, if so, it ends the game.
    if win_check(player1):
        print("Congratulations, you've reached your goal! You win!")
        print("thanks for playing")
        game_on = False
    else:
        keep_playing = input("Do you want to play another round?? Y/N").lower()
        if keep_playing != "y":
            print(f'You ended with {player1.chips} Chips! Thanks for playing!')
            game_on = False
        else:
            print("---------------NEW ROUND----------------")