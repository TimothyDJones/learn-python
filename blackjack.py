# blackjack.py
# Python blackjack game

import random
#suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
print(suits)

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for k, v in suits.items():
            for rank in ranks:
                self.deck.append(Card(v, rank))

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += '\n\t' + card.__str__()
        return 'The deck contains:' + deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []     # Start with empty hand/list.
        self.value = 0
        self.aces = 0       # Attribute to count number of aces in hand.

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            print("You have {0} chips.".format(chips.total))
            chips.bet = int(input("How many chips do you want bet? "))
        except (ValueError):
            print("Sorry. Your bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry. Your bet can't exceed {}.".format(chips.total))
            elif chips.bet < 0:
                print("Nice try, but negative bets aren't allowed.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    
    while True:
        x = input("Hit (h) or Stand (s)? ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Unknown input. Try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print("\t<card hidden> ")
    print("\t", dealer.cards[1])
    print("\nPlayer's hand: ", *player.cards, sep=" ", end="")
    print(" ({0})".format(player.value))

def show_all(player, dealer):
    print("\nDealer's hand:", *dealer.cards, sep=" ")
    print("\tDealer's hand = {0}".format(dealer.value))
    print("\nPlayer's hand: ", *player.cards, sep=" ")
    print("\tPlayer's hand = {0}".format(player.value))

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.lose_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player tie! It's a push.")


# Set up player's chips
player_chips = Chips()      # Use default of 100 to start

while True:
    print("Welcome to Blackjack! Get as close to 21 without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.")
    
    # Create and shuffle deck and deal two cards to each player.
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Prompt player for bet
    take_bet(player_chips)
    
    # Show cards, but keep one of dealer's cards hidden.
    show_some(player_hand, dealer_hand)
    
    while playing:
        # Prompt for 'hit' or 'stand'
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, player busts.
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If player hasn't busted, play dealer's hand until 17.
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        # Show all cards
        show_all(player_hand, dealer_hand)
        
        # Resolve outcome of game
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    
    # Inform player of current chip total
    print("\nPlayer's winnings stand at {0} chips.".format(player_chips.total))
    
    # Ask player if they want to play again
    new_game = input("Play again (y/n)? ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing! Goodbye.")
        break

