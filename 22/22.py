#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    original_deck1, original_deck2 = list(map(lambda t: list(map(int, t.split('\n')[1:])), f.read().strip().split('\n\n')))

def score(d):
    return sum(map(lambda p: (1+p[0]) * p[1], enumerate(d[::-1])))

# Part 1

deck1, deck2 = original_deck1[:], original_deck2[:]
while deck1 and deck2:
    card1, card2 = deck1[0], deck2[0]
    deck1, deck2 = deck1[1:], deck2[1:]
    if card1 > card2:
        deck1 = deck1 + [card1, card2]
    else:
        deck2 = deck2 + [card2, card1]

print(score(deck1 or deck2))

# Part 2

def play_game(deck1, deck2):
    seen = set()

    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in seen:
            return (True, deck1)

        seen.add((tuple(deck1), tuple(deck2)))

        card1, card2 = deck1[0], deck2[0]
        deck1, deck2 = deck1[1:], deck2[1:]

        if len(deck1) >= card1 and len(deck2) >= card2:
            p1_wins, _ = play_game(deck1[:card1], deck2[:card2])
        else:
            p1_wins = card1 > card2

        if p1_wins:
            deck1 = deck1 + [card1, card2]
        else:
            deck2 = deck2 + [card2, card1]

    return (True, deck1) if deck1 else (False, deck2)

deck1, deck2 = original_deck1[:], original_deck2[:]
_, winning_deck = play_game(deck1, deck2)
print(score(winning_deck))
