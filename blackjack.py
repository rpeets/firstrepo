"""
Black Jack Game:

1 deck, 52 Cards
type of cards don't matter, so you have 4 2's, 4 3's etc etc Each card
has a face value and actual value. i.e. properites Most of the time, face
value is the same as actual value, for example, face value 2, actual value
is 2 However, there are special cases
 1. ALL cards with face value over 10 have actual value 10, for example,
    K's acual value is 10, Q's actual value is 10, etc etc
 2. A's actual value can be ether 1 or 11

Game rules:

1. one player and one dealer
2. game begins
    each gets two cards
    they sum up the two cards' actual values
    if total sum is less than 21, they can call "hit". means
     give me another card.
         - they sum up again, if less than 21, they can continue to "hit"
         - Or, they can choose to "stop"
         - If sum is above 21 lose the game automatically
     when one side says "stop" the total sum of card values are final. It
     is the other party's turn to do the same

3. When both parties say "stop" it is time to compare the total sums.
    Whoever has the greater sum wins the game

"""

import sys
from random import shuffle, randrange


class Table():
    """Creating a table class and other object for the game"""

    def __init__(self, player):
        self.dealer = Dealer()
        self.player = Player(player)
        self.deck = Deck()

        """call table_setup() method to shuffle and deal first cards"""
        self.table_setup()


    def table_setup(self):
        """shuffle the deck before dealing"""
        self.deck.shuffle()

        # Deal a card to the player, then the dealer, then
        # the player to start the game
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)

        # Find out initial BlackJack
        self.calculate_score(self.player)
        self.calculate_score(self.dealer)

        # recurring hit/stick prompt and deal cards
        self.main()


    def main(self):
        """main methord for looping"""
        while True:
            print()
            print(self)
            player_move = self.player.hit_or_stick()
            if player_move:
                self.deal_card(self.player)
                self.calculate_score(self.player)
            else:
                self.calculate_score(self.player)
                self.dealer_hit()


    def dealer_hit(self):
        """Dealer hits for cards and stops between 15, 21"""
        score = self.dealer.score
        while score < self.dealer.stop:
            # Dealer may stops anytime between 15, 21
            if score < self.dealer.stop:
                self.deal_card(self.dealer)
                self.calculate_score(self.dealer)
                print(self)
            else:
                self.calculate_score(self.dealer)


    def __str__(self):
        """Print the progress of the game!"""
        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print("Dealer's hand  : {}".format(dealer_hand))
        print("Dealer's score : {}".format(self.dealer.score))
        print()
        print("{}'s hand  : {}".format(self.player.name, player_hand))
        print("{}'s score : {}".format(self.player.name, self.player.score))
        print()
        print("-" * 40)
        return ''


    def deal_card(self, player):
        """Pull card form the deck and add to player"""
        card = self.deck.stack.pop()
        player.hand.append(card)


    def calculate_score(self, player):
        """Find out if ace in hand and calculate the score"""
        ace = False
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -= 10
            score = player.score
        self.check_win(score, player)


    def check_win(self, score, player):
        """Check score and report the winner!"""
        if score > 21:
            print(self)
            print("{} Busts!!!".format(player.name))
            print()
            self.end_game()
        elif score == 21:
            print(self)
            print("**** {} BlackJack!!! ****".format(player.name))
            print()
            self.end_game()


    def end_game(self):
        """End the game or continue playing!!!"""
        print("-" * 40)
        again = input("Do you want to play again (Y/N)? ")
        if again.lower().startswith('y'):
            self.__init__(self.player.name)
        else:
            sys.exit()


class Dealer():
    """Setup Dealer"""

    def __init__(self):
        """Setup Dealer name score and hand"""
        self.name = "Dealer"
        self.score = 0
        self.hand = []
        self.stop = randrange(15, 21)


class Player(Dealer):
    """Setup Player"""

    def __init__(self, name):
        """Setup the player name score and hand"""
        super().__init__()
        self.name = name


    @staticmethod
    def hit_or_stick():
        """Ask for another card"""
        while True:
            choice = input("Do you want another card (Y/N)? ")
            if choice.lower().startswith('y'):
                return True
            elif choice.lower().startswith('n'):
                return False
            else:
                print("Please Enter (Y/N)!")
                continue


class Deck():
    """Creating One stack of cards & shuffle"""

    def __init__(self):
        """Setup the stack"""
        self.stack = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4
        self.shuffle()


    def shuffle(self):
        """Shuffle the cards"""
        shuffle(self.stack)


    def deal_card(self):
        """Deal the card"""
        card = self.stack.pop()
        return card


def main():
    """Main Function, Ask for name and Setup Table!"""
    player_name = input("Please Enter Your Name: ")
    Table(player_name)


if __name__ == '__main__':
    main()
