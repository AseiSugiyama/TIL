# -*- coding: utf-8 -*-
N = int(input())
cards = map(int, input().split())


def calcDifference(cards):
    sortedCards = sorted(cards, reverse=True)

    turn = 0
    scoreOfAlice = 0
    scoreOfBob = 0

    for card in sortedCards:
        if turn == 0:
            scoreOfAlice += card
        if turn == 1:
            scoreOfBob += card
        turn = (turn + 1) % 2

    return scoreOfAlice - scoreOfBob


print(calcDifference(cards))
