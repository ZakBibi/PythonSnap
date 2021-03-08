from code.Card import Card


def test_01_can_make_card():
    ace_of_hearts = Card("Ace", "Heart")
    assert ace_of_hearts == Card("Ace", "Heart")


def test_02_can_display_card():
    assert Card("Ace", "Hearts").__str__() == "Ace of Hearts"
