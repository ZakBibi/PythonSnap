import pytest
from code.Snap import Snap
from code.Card import Card


@pytest.fixture
def snap():
    return Snap(2)


def test_01_can_check_player_hand_length(snap):
    player_hand = [1, 2, 3]
    assert snap.is_player_hand_empty(player_hand) == 3


def test_02_can_play_card(snap):
    player_hand = [1, 2, 3]
    snap.play_card(player_hand)
    assert snap.pile == [1] and player_hand == [2, 3]


def test_03_can_match_card(snap):
    pile = [Card("Ace", "Hearts"), Card("Ace", "Clubs")]
    assert snap.match_card(pile)


def test_04_if_pile_is_empty_return_false(snap):
    pile = []
    assert not snap.match_card(pile)


def test_05_if_pile_has_one_card(snap):
    pile = [Card("Ace", "Hearts")]
    assert not snap.match_card(pile)


def test_06_can_pick_up(snap):
    player_hand = [1, 2, 3]
    pile = [4, 5, 6]
    assert snap.pick_up(pile, player_hand) == [1, 2, 3, 4, 5, 6] \
           and pile == []
