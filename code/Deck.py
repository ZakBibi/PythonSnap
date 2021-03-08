import random
from code.Card import *


class Deck:

    def __init__(self):
        self.deck = []
        self.construct_deck()

    def construct_deck(self):
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        return random.sample(self.deck, len(self.deck))

    def show_card(self):
        for card in self.deck:
            return card.__str__()

    @staticmethod
    def deal(deck, number_of_players):
        return [deck[card::number_of_players]
                for card in range(number_of_players)]

    @staticmethod
    def _deal_hands(hand, number_of_players):
        return [hand[card::number_of_players]
                for card in range(number_of_players)]
