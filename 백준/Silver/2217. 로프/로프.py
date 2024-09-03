import sys

N = int(sys.stdin.readline())

ropes = []

maxWeight = 0

for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

for i in range(N):
    maxWeight = max(maxWeight, ropes[i] * (i+1))


print(maxWeight)