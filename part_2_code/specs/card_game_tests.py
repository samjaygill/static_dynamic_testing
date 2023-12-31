import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def test_check_for_ace(self):
        game = CardGame()
        ace_card = Card(suit='Hearts', value=1)  
        non_ace_card = Card(suit='Diamonds', value=5) 

        self.assertEqual(game.check_for_ace(ace_card), True)
        self.assertEqual(game.check_for_ace(non_ace_card), False)

    def test_highest_card(self):
        game = CardGame()
        card1 = Card(suit='Spades', value=8)  
        card2 = Card(suit='Clubs', value=5)  

        self.assertEqual(game.highest_card(card1, card2), card1)

    def test_cards_total(self):
        game = CardGame()
        cards = [
            Card(suit='Hearts', value=3),
            Card(suit='Diamonds', value=7),
            Card(suit='Clubs', value=2)
        ]

        self.assertEqual(game.cards_total(cards), "You have a total of 12")
