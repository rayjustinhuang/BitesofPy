from collections import namedtuple
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError
        elif not all([isinstance(card, Card) for card in cards]):
            raise ValueError
        elif len(cards) != 13:
            raise ValueError
        else:
            self.cards = cards
            
        self.cards_sorted = sorted(self.cards, key = lambda card: (card.suit.value, card.rank.value))
        
        self.dict_rep = {}
        
        for card in self.cards_sorted:
            self.dict_rep[card.suit.name] = "".join([i.rank.name for i in self.cards_sorted if i.suit.name == card.suit.name])

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        #cards_sorted = sorted(self.cards, key = lambda card: card.suit, reverse = True)
        
        #spades = [card for card in self.cards if card.suit == 'S']
        #hearts = [card for card in self.cards if card.suit == 'H']
        #diamonds = [card for card in self.cards if card.suit == 'D']
        #clubs = [card for card in self.cards if card.suit == 'C']
        
        #cards_sorted = sorted(self.cards, key = lambda card: (card.suit.value, card.rank.value))
        
        #output_dict = dict()
        
        #for card in cards_sorted:
        #    output_dict[card.suit.name] = "".join([i.rank.name for i in cards_sorted if i.suit.name == card.suit.name])
        
        output_string = ""
        
        for item in self.dict_rep:
            output_string += f'{item}:{self.dict_rep[item]} '
            
        return output_string.strip()
            

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """

        return sum(HCP[card.rank] for card in self.cards if card.rank in HCP)

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        
        #output_dict = dict()
        
        #for card in cards_sorted:
        #    output_dict[card.suit.name] = "".join([i.rank.name for i in cards_sorted if i.suit.name == card.suit.name])
        
        return sum(1 for tons in self.dict_rep.values() if len(tons) == 2)

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        
        #output_dict = dict()
        
        #for card in cards_sorted:
        #    output_dict[card.suit.name] = "".join([i.rank.name for i in cards_sorted if i.suit.name == card.suit.name])
        
        return sum(1 for tons in self.dict_rep.values() if len(tons) == 1)

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        
        #output_dict = dict()
        
        #for card in cards_sorted:
        #    output_dict[card.suit.name] = "".join([i.rank.name for i in cards_sorted if i.suit.name == card.suit.name])
            
        return 4-len(self.dict_rep)
        

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        output_dict = dict()
        
        for suit in 'SHDC':
            output_dict[suit] = len([i.rank.name for i in self.cards_sorted if i.suit.name == suit])
            
        ssp_total = 0
        
        for value in output_dict.values():
            if 2 >= value >= 0:
                ssp_total += SSP[value]
        
            
        return ssp_total
        

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        #output_dict = dict()
        
        #for card in cards_sorted:
        #    output_dict[card.suit.name] = "".join([i.rank.name for i in cards_sorted if i.suit.name == card.suit.name])
        
        ltc = 0
        
        for suit in 'SHDC':
            try:
                check = self.dict_rep[suit][:3]
                if len(check) == 0:
                    continue
                elif len(check) == 1:
                    if check == 'A':
                        continue
                    else:
                        ltc += 1
                elif len(check) == 2:
                    if check == 'AK':
                        continue
                    elif 'A' in check or 'K' in check:
                        ltc += 1
                    else:
                        ltc += 2
                else:
                    if check == 'AKQ':
                        continue
                    elif 'AK' in check or 'AQ' in check or 'KQ' in check:
                        ltc += 1
                    elif 'A' in check or 'K' in check or 'Q' in check:
                        ltc += 2
                    else:
                        ltc += 3
            except:
                continue
        
        return ltc

                
#def hand_generator(card_string):
#    """ Generate actual list of Card instances from card_string """
#    card_list = []
#    for suit_holding in card_string.split():
#        suit = Suit[suit_holding[0]]
#        for rank in suit_holding[2:]:
#            card = Card(suit, Rank[rank])
#            card_list.append(card)
#            
#    return card_list

"""    
test_hand = hand_generator("S:AKJ H:QJT9 D:5432 C:AK")

test = BridgeHand(test_hand)

print(str(test))

test_card = test_hand[0]

print(test_card.rank)
"""
#for letter in 'SHDC':
#    print(letter)
