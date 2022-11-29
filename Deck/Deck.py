from Cards.card import Card
import random

class Deck():
    def __init__(self):
        self.__faces = ['heart','spade','diamond','club']
        self.__royal_card = ['joker','queen','king','ace']
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for face in self.__faces:
            for num in range(2,11):
                self.deck.append(Card(num, face))
            for roy in self.__royal_card:
                self.deck.append(Card(roy, face))

    def shuffle(self):
        random.shuffle(self.deck)

    def remove_top(self):
        if len(self.deck) == 0:
            print('deck is empty')
        return self.deck.pop()


    def __len__(self):
        return len(self.deck)

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += f'{card.get_face()} : {card.get_number()}\n'

        return deck_str

