"""
Player class
Created: 15/01/2019
Author: Borislav Kolev
"""


from Deck import Deck


class Player(object):
    def __init__(self, name, age):
        self.hand = []
        self.name = name
        self.age = age

    def draw(self, deck):
        # The argument we are passing is a deck created from the deck class and we are withdrawing a card
        # using the deck method draw_card(). Then we are appending the returned value into the self.hand[]
        self.hand.append(Deck.draw_card(deck))
        # returning the instance object and allowing me to draw again
        return self

    def show_hand(self):
        for card in self.hand:
            # Showing each card the player has
            print(card.show_card())

    def evaluate_hand_points(self):
        points = 0
        for i in self.hand:
            points += i.evaluate_points()
        return "Total hand points:: " + str(points)


# Creating the deck
f_deck = Deck()
# Creating the player
Bobby = Player("Bobby", 20)
# Drawing the cards from the deck
Bobby.draw(f_deck).draw(f_deck).draw(f_deck)
# Printing the cards to the user
Bobby.show_hand()
# Evaluating the cards
print(Bobby.evaluate_hand_points())
