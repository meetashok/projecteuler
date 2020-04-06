## Problem 54
## Poker hands

from urllib2 import urlopen 

# connection = urlopen("https://projecteuler.net/project/resources/p054_poker.txt")
# data = connection.read()
# connection.close()

# data = data.split("\n")
# data.pop()

# data = [hands.split(" ") for hands in data]
# data = [[(hand[:5], hand[5:]) for card in hand] for hand in data]
    
# sample_hand = data[0][0][0]
print sample_hand

def hand_suits(hand):
    return [card[-1] for card in hand]

def hand_numbers(hand):
    numbers = [card[0] for card in hand]
    
def count_cards(hand):
    numbers = hand_numbers(hand)
    
    for number in numbers:
        if 

def hand_rank(hand):
    suits = hand_suits(hand)
    numbers = hand_numbers(hand)
    
    same_suit = (len(np.unique(np.array(suits))) == 1)
    straight = False
    royal_straight = False
    n_pair = False
    triplet = False
    four_of_a_kind = (len(np.unique(np.array(numbers))) == 2)
    highest_card = (len(np.unique(np.array(numbers))) == 5)
    
    if same_suit & royal_straight:
        return (1, "Royal Flush")
    elif same_suit & straight:
        return (2, max(numbers), "Straight Flush")
    elif four_of_a_kind:
        return (3, "Four of a Kind")
    elif (n_pair == 1) & (triplet):
        return ()
    
hand_rank(sample_hand):
    
    if len(np.unique(np.array))

suits = ["H", "D", "C", "S"]
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

ranking = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

hand = "5H 5C 6S 7S KD"
hand = hand.split(" ")



def all_suits_same(hand):
    return all([hand_suits(hand)[0] == suit for suit in hand_suits(hand)])

def is_straight(hand):
    pass