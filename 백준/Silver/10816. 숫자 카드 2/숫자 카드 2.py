import sys

N = int(sys.stdin.readline().rstrip())

cards_list = list(map(int, sys.stdin.readline().rstrip().split()))

cards = {}

for c in cards_list:
    cards[c] = cards.setdefault(c, 0) + 1

M = int(sys.stdin.readline().rstrip())

wonder = list(map(int, sys.stdin.readline().rstrip().split()))

for w in wonder:
    print(cards.setdefault(w, 0), end=' ')
