import sys

N = int(sys.stdin.readline().rstrip())

ranks = []

for _ in range(N):
    ranks.append(int(sys.stdin.readline().rstrip()))

ranks.sort()

answer = 0

for i, r in enumerate(ranks):
    answer += abs(i+1-r)

print(answer)