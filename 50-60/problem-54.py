## Problem 54
## Poker hands

def gethands():
    import requests
    url = "https://projecteuler.net/project/resources/p054_poker.txt"

    response = requests.get(url)
    hands = response.text.split("\n")

    player1 = [hand.split()[:5] for hand in hands]
    player2 = [hand.split()[5:] for hand in hands]

    return player1, player2

player1, player2 = gethands()

class Hand(object):
    suits = ["H", "D", "C", "S"]
    cardranks = ["1", "2", "3", "4", "5", 
            "6", "7", "8", "9", "T", "J", 
            "Q", "K", "A"]

    def __init__(self, hand):
        self.hand = hand

    @property
    def suits(self):
        return [card[1] for card in self.hand]
    
    @property
    def numbers(self):
        return [card[0] for card in self.hand]

    def highest_card(self):
        return sorted(self.numbers, key=lambda x: self.cardranks.index(x))[-1]

    def is_straight(self):
        s = sorted(self.numbers, key=lambda x: self.cardranks.index(x))

        if self.cardranks.index(s[-1]) - self.cardranks.index(s[0]) == 4:
            return True
        elif self.numbers == ["2", "3", "4", "5", "A"]:
            return True
        else:
            return False

    def is_straightflush(self):
        return len(self.suits) == 1 and self.is_straight()

    def is_fourofakind(self):
        for number in set(self.numbers):
            if self.numbers.count(number) == 4:
                return True
        return False

    def is_flush(self):
        if len(set(self.suits)) == 1:
            return True
        return False

    def is_threeofakind(self):
        for number in set(self.numbers):
            if self.numbers.count(number) == 3:
                return True
        return False

    def is_onepair(self):
        for number in set(self.numbers):
            if self.numbers.count(number) == 2:
                return True
        return False

    def is_twopairs(self):
        for number in set(self.numbers):
            if self.numbers.count(number) == 2 and len(set(numbers)) == 3:
                return True
        return False

    def is_fullhouse(self):
        return self.is_threeofakind() and self.is_onepair()

    ranking = ["High Card", 
    "One Pair", 
    "Two Pairs", 
    "Three of a Kind", 
    "Straight", 
    "Flush", 
    "Full House", 
    "Four of a Kind", 
    "Straight Flush", 
    "Royal Flush"]

    def rank(self):
        if self.is_straightflush():
            return (1, self.highest_card())
        if self.is_fourofakind():
            a, b = set(self.numbers)
            if self.numbers.count(a) == 4:
                return (2, a)
            else:
                return (2, b)
        if self.is_fullhouse():


        

    

    

    def rank(self):



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



ranking = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

hand = "5H 5C 6S 7S KD"
hand = hand.split(" ")



def all_suits_same(hand):
    return all([hand_suits(hand)[0] == suit for suit in hand_suits(hand)])

def is_straight(hand):
    pass