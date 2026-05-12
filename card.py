#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module 

:author: `FIL - Faculté des Sciences et Technologies - 
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2017, september.
:last revision: 2024, march

"""
from __future__ import annotations
import random



class Card(object):
    """
    Cards are defined by a value and a color.
    Possible values and colors are listed in ``Card.VALUES`` and ``Card.COLORS``.

    $$$ c1 = Card("Ace", "heart")
    $$$ c1.color
    'heart'
    $$$ c1.value
    'Ace'
    $$$ c1
    Card("Ace", "heart")
    $$$ c2 = Card("King", "spade")
    $$$ c2.value in Card.VALUES
    True
    $$$ c2.color in Card.COLORS
    True
    $$$ c1 == c1
    True
    $$$ c1 != c1
    False
    $$$ c1 < c1
    False
    $$$ c1 <= c1
    True
    """
    
    ## tuple of possible values and colors in ascending order
    VALUES = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Knight", "Queen", "King")
    COLORS = ("spade", "heart", "diamond", "club")

    def __init__(self, value: str, color: str):
        """
        creates a card with value and color

        précondition : value in VALUES and color in COLORS
        """
        self.value = value
        self.color = color


    def __hash__(self) -> int:
        """
        Renvoie un haché de self.
        """
        return hash((self.value, self.color))

    def __repr__(self) -> str:
        """
        return a string representation of the card
    
        $$$ repr(Card('Ace', 'heart'))
        'Card("Ace", "heart")'
        """
        return f'Card("{self.value}", "{self.color}")'

    def __str__(self) -> str:
        """
        return a string representation of the card
    
        $$$ str(Card('Ace', 'heart'))
        'Ace of heart'
        """
        return f'{self.value} of {self.color}'


    def compare(self, card: Card) -> int:
        """
        compares cards.

        Order on cards is defined  by order on values

        return: 
          
           * a positive number if self is greater than card
           * a negative number if self is lower than card
           * 0 if self is the same than card

        précondition: none
        exemples: 

        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('King', 'heart')
        $$$ c3 = Card('Ace','spade')
        $$$ c1bis = Card('Ace','heart')
        $$$ c1.compare(c2) < 0
        True
        $$$ c2.compare(c1) > 0
        True
        $$$ c1.compare(c3) == 0
        True
        """
        v1 = Card.VALUES.index(self.value)
        v2 = Card.VALUES.index(card.value)
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0

    @staticmethod
    def deck(n_card: int) -> list[Card]:
        """
        return a list of `n_card` randomly chosen cards

        precondition: n_card > 0 and n_card <= 4*13

        Exemples:

        $$$ cartes = Card.deck( 10 )
        $$$ len(cartes) == 10
        True
        $$$ all( isinstance(c, Card) for c in cartes)
        True
        $$$ len(set(cartes))
        len(cartes)
        """
        full_deck = [Card(v, c) for v in Card.VALUES for c in Card.COLORS]
        random.shuffle(full_deck)
        return full_deck[:n_card]

    def __eq__(self, card: Card) -> bool:
        """
        return True if self equals card
               False otherwise
        """
        return self.compare(card) == 0

    def __neq__(self, card: Card) -> bool:
        """
        return True if self don't equal card
               False otherwise
        """
        return self.compare(card) != 0

    def __lt__(self, card: Card) -> bool:
        """
        return True if self is strictly inferior to card
               False otherwise
        """
        return self.compare(card) <0

    def __le__(self, card: Card) -> bool:
        """
        return True if self is inferior or equal to card
               False otherwise
        """
        return self.compare(card) <= 0

    def __gt__(self, card: Card) -> bool:
        """
        return True if self is strictly superior to card
               False otherwise
        """
        return self.compare(card) > 0

    def __ge__(self, card: Card) -> bool:
        """
        return True if self is superior or equal to card
               False otherwise
        """
        return self.compare(card) >=0


if __name__ == '__main__':
    import l1test
    l1test.testmod('card.py')

