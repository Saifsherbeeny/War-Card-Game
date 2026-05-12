#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`war` game

:author: `FIL - Faculté des Sciences et Technologies -
         Univ. Lille <http://portail.fil.univ-lille1.fr>`

:date: 2021, april.
:last revision: 2024, march.
"""

from card import Card
from apqueue import *
from apstack import *


def distribute(n_card: int) -> tuple[ApQueue, ApQueue]:
    """
    renvoie un couple (m1, m2) constitué de deux files,
    contenant pour chacune `n_card` cartes

    precondition : n_card > 0
    exemples :

    $$$ m1, m2 = distribute( 4 )
    $$$ len(m1) == 4
    True
    $$$ len(m2) == 4
    True
    $$$ type(m1) == ApQueue
    True
    $$$ type(m2) == ApQueue
    True
    $$$ carte = m1.dequeue()
    $$$ isinstance(carte, Card)
    True
    """
    cards= Card.deck(2* n_card)
    m1= ApQueue()
    m2 = ApQueue()
    for i in range(n_card):
        m1.enqueue(cards[i])
        m2.enqueue(cards[i + n_card])
    return (m1, m2)

def gather_stack(main: ApQueue, pile: ApStack) -> None:
    """
    ajoute les carte de la pile dans la main

    exemples :

    $$$ cartes = Card.deck(4)
    $$$ main = ApQueue()
    $$$ pile = ApStack()
    $$$ for c in cartes: pile.push(c)
    $$$ gather_stack( main, pile )
    $$$ len( main ) == 4
    True
    $$$ all( main.dequeue() == cartes[ 3 - i ] for i in range(3))
    True
    """
    while not pile.is_empty():
        main.enqueue(pile.pop())

def play_one_round(m1: ApQueue, m2: ApQueue, pile: ApStack) -> None:
    """
    Simule une étape du jeu :
    `j1`` et ``j2`` prennent la première carte de leur
    main. On compare les deux cartes :

    * Si la carte de ``j1`` est supérieure à celle de ``j2``, alors
    ``j1`` remporte toutes les cartes de la pile ;
    * Si la carte de ``j1`` est inférieure à celle de ``j2``, alors
    ``j2`` remporte toutes les cartes de la pile ;
    * Si les cartes sont égales, alors elles sont *empilées* sur la
      pile.

    precondition : m1 et m2 ne sont pas vides
    """
    c1 = m1.dequeue()
    c2 = m2.dequeue()
    print(f"joueur 1 joue {c1} et joueur 2 joue {c2}")
    result = c1.compare(c2)
    if result > 0:
        print("joueur 1 gagne")
        m1.enqueue(c1)
        m1.enqueue(c2)
        gather_stack(m1, pile)
    elif result < 0:
        print("joueur 2 gagne")
        m2.enqueue(c1)
        m2.enqueue(c2)
        gather_stack(m2, pile)
    else:
        print("Bataille ! ")
        pile.push(c2)
        pile.push(c1)
        print(f"{len(pile)} cartes sur la table")

def play(n_card: int, n_round: int) -> None:
    """
    simule une partie de bataille

    n_card: le nombre de cartes à distribuer à chaque joueur.
    n_round: le nombre maximal de tours
    """
    m1, m2 = distribute(n_card)
    pile = ApStack()
    current_round = 1    
    while not m1.is_empty() and not m2.is_empty() and current_round <= n_round:
        print(f"------ Tour {current_round} --------")
        play_one_round(m1, m2, pile)
        print(f"Le joueur 1 a {len(m1)} cartes et joueur 2 {len(m2)} cartes")
        current_round += 1    
        len1, len2 = len(m1), len(m2)
    if len1 > len2:
        print("Le joueur 1 a gagné")
    elif len2 > len1:
        print("Le joueur 2 a gagné")
    else:
        print("égalité")


if __name__ == "__main__":
    import l1test
    l1test.testmod("war.py")

