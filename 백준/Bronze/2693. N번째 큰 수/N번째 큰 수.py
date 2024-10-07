import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    print(sorted(list(map(int, sys.stdin.readline().rstrip().split())))[-3])