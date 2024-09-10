from itertools import combinations
import sys

heights = []

for _ in range(9):
    heights.append(int(sys.stdin.readline().rstrip()))

heights = list(combinations(heights, 7))

answer = []

for h in heights:
    if sum(h) == 100:
        answer = h

answer = sorted(answer)

for a in answer:
    print(a)
