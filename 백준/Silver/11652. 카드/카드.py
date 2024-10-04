import sys

N = int(sys.stdin.readline().rstrip())

cards = {}

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

cards = sorted(cards.items(), key=lambda x: (-x[1], x[0]))

print(cards[0][0])