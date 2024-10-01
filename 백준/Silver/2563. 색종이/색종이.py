import sys

S = [[0 for _ in range(100)] for _ in range(100)]

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            S[i][j] = 1

count = 0

for i in range(100):
    for j in range(100):
        if S[i][j] == 1:
            count += 1

print(count)