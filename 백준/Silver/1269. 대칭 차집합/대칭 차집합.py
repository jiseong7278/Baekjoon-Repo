import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = set(map(int, sys.stdin.readline().rstrip().split()))
B = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(B-A) + len(A-B))