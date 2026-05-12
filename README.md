# Jeu de Bataille (War Card Game) - Implementation in Python

This project is a simulation of the classic card game **"War" (Bataille)**, developed as part of my first-year Informatics studies project.

## 🛠 Features & Technical Concepts
- **Data Structures**: Utilizes custom implementations of **Stacks** for the table/pot and **Queues** for player hands to ensure O(1) efficiency for card movements.
- **Object-Oriented Programming**: Implements a Card class with custom comparison operators and string representations.
- **Unit Testing**: Fully tested using l1test and doctests to ensure logic accuracy for game rounds and distribution.
- **Game Logic**: Handles "Bataille" scenarios (ties) where cards are buffered in a stack until a player wins the round.

## 🚀 How to Run
Ensure you have Python 3 installed, then run:
```bash
python3 war.py
