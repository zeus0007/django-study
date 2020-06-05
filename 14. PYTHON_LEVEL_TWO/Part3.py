#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split(' ')  # heart dia spade clover
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

    def create(self):
        cards = []
        for suit in self.suits:
            for rank in self.ranks:
                cards.append(suit + rank)
        self.cards = cards
        print(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def splitting(self):
        player1 = self.cards[:len(self.cards/2)]
        player2 = self.cards[len(self.cards/2):]
        playerDeck = {"player1": player1, "player2": player2}
        return playerDeck
    pass


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, deck):
        self.deck = deck

    def add(self, card):
        self.deck.append(card)

    def remove(self, card):
        self.deck.remove(card)
    pass


# class Player:
#     """
#     This is the Player class, which takes in a name and an instance of a Hand
#     class object. The Payer can then play cards and check if they still have cards.
#     """
#     pass


# ######################
# #### GAME PLAY #######
# ######################
print("Welcome to War, let's begin...")

# # Use the 3 classes along with some logic to play a game of war!
d = Deck(SUITE, RANKS)
d.create()
d.shuffle()
deck = d.splitting()

hand1 = Hand(deck["player1"])
hand2 = Hand(deck["player2"])
if(hand1.deck[0][1] == hand2.deck[0][1])

# 중단
# 양쪽 덱 비교 필요 (숫자 비교)
# 비교 후 이긴 쪽 덱 맨 위에 카드 넣기
# 위 과정 반복
# (숫자가 같을 시)
# 세장 카드 비교 후 승리 횟수 누적
# 승자 판별 후 승자 덱에 카드 추가
# 반복
