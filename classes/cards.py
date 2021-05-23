from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return "{0} of {1}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, n) for s in suits for n in values]

        shuffle(self.cards)

    def __repr__(self):
        return "Deck of {0} cards".format(self.count())

    def _deal(self, number_of_cards):
        deal_cards = []
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif number_of_cards >= len(self.cards):
            deal_cards = self.cards
            self.cards = []
        else:
            deal_cards = self.cards[self.count() - number_of_cards : :]
            self.cards = self.cards[: self.count() - number_of_cards]
        return deal_cards

    def shuffle(self):
        if self.count() == 52:
            return shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    def count(self):
        return len(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)


deck = Deck()

print(deck.cards)
print(deck.shuffle())
print(deck)
deck._deal(4)
print(deck)
deck._deal(50)
print(deck)
# deck._deal(1)
# print(deck)
# deck.shuffle()

deck = Deck()
print(deck.deal_card())
print(deck.deal_hand(5))