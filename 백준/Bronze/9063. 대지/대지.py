import sys

N = int(sys.stdin.readline().rstrip())

min_x, min_y, max_x, max_y = 10001, 10001, -10001, -10001

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().rstrip().split())

    min_x = min(min_x, X)
    min_y = min(min_y, Y)
    max_x = max(max_x, X)
    max_y = max(max_y, Y)

print((max_x - min_x) * (max_y - min_y))