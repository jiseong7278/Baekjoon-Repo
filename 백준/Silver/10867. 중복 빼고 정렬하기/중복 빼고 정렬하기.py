import sys

N = int(sys.stdin.readline().rstrip())

A = sorted(list(set(map(int, sys.stdin.readline().rstrip().split()))))

print(*A)