import Cards


class Player():
    def __init__(self, name='Player'):
        self.name = name
        self.hand = []

    def draw_card(self,card):
        #print(type(card))
        if type(card) == Cards.card.Card:
            self.hand.append(card)
            return True
        else:
            return False

    def show_hand(self):
        for card in self.hand:
            print(card)

    def __str__(self):
        return f'{self.name} hand : {len(self.hand)}'