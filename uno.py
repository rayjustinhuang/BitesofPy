from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    
    deck = []
    
    for suit in SUITS:
        zeroes = UnoCard(suit, 0)
        numbers = [UnoCard(suit, x) for x in range(1, 10)]
        deck.append(zeroes)
        deck += numbers
        deck += numbers
        
    draw_two = UnoCard(suit, 'Draw Two')
    skip = UnoCard(suit, 'Skip')
    reverse = UnoCard(suit, 'Reverse')
        
    deck.append(draw_two)
    deck.append(skip)
    deck.append(reverse)
    deck.append(draw_two)
    deck.append(skip)
    deck.append(reverse)
    
    deck += 4*[UnoCard(None, 'Wild'), UnoCard(None, 'Wild Draw')]
    
    return deck
    pass

deck = create_uno_deck()
print(deck)