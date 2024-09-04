import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

heapq.heapify(cards)

for i in range(M):
    cards_sum = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, cards_sum)
    heapq.heappush(cards, cards_sum)

print(sum(cards))