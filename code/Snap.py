from code.Deck import *


class Snap:

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.deck = Deck()
        self.pile = []

    @staticmethod
    def is_player_hand_empty(player_hand):
        return len(player_hand)

    def play_card(self, player_hand):
        self.pile.append(player_hand.pop(0))

    @staticmethod
    def match_card(pile):
        if not pile:
            return False
        elif len(pile) == 1:
            return False
        else:
            return pile[-1].rank == pile[-2].rank

    @staticmethod
    def pick_up(pile, player_hand):
        player_hand.extend(pile)
        pile.clear()
        return player_hand
