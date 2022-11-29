from Deck.Deck import Deck
from Player import Player


def player_amount():
    players = []
    while True:
        num = input('How many players')
        if num.isdigit():
            num = int(num)
            if 2 <= num <= 4:
                for i in range(num):
                    players.append(Player(F'Player {i}'))
                return players
            else:
                res = 'please enter a number between 2 and 4'
                print(res)
        else:
            res = 'please enter a digit'
            print(res)

def deal_cards(players,deck):
    for _ in range(7):
        for player in players:
            player.draw_card(deck.remove_top())

def main():
    deck = Deck()
    deck.shuffle()
    players = player_amount()
    deal_cards(players,deck)
    players[0].show_hand()



if __name__ == '__main__':
    main()