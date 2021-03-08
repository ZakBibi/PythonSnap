import pytest
from code.Deck import Deck
from code.Card import Card


@pytest.fixture
def card_deck():
    return Deck()


def test_01_can_construct_deck(card_deck):
    assert len(card_deck.deck) == 52


def test_02_can_shuffle_deck(card_deck):
    shuffled_deck = Deck().shuffle()
    assert card_deck != shuffled_deck


def test_03_can_deal_cards(card_deck):
    dealt_cards = card_deck.deal(card_deck.deck, 2)
    assert dealt_cards[0][0] == Card("Ace", "Hearts")


def test_04_can_deal_correct_number_of_hands(card_deck):
    cards = [1, 2, 3, 4, 5, 6, 7, 8]
    dealt_cards = card_deck._deal_hands(cards, 2)
    assert len(dealt_cards) == 2


def test_05_deal_hands_order_preserved(card_deck):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dealt_cards = card_deck._deal_hands(cards, 2)
    assert dealt_cards[0] == [1, 3, 5, 7, 9] \
           and dealt_cards[1] == [2, 4, 6, 8]


def test_06_deal_hands_deal_three_hands(card_deck):
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dealt_cards = card_deck._deal_hands(cards, 3)
    assert dealt_cards[0] == [1, 4, 7] \
           and dealt_cards[1] == [2, 5, 8] \
           and dealt_cards[2] == [3, 6, 9]


def test_07_deal_hands_can_handle_too_many_players(card_deck):
    cards = [1]
    dealt_cards = card_deck._deal_hands(cards, 2)
    assert dealt_cards[0] == [1] \
           and dealt_cards[1] == []


def test_08_deal_hands_returns_empty_list_if_no_cards(card_deck):
    cards = []
    dealt_cards = card_deck._deal_hands(cards, 1)
    assert dealt_cards[0] == []
