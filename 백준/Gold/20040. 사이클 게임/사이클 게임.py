import sys

sys.setrecursionlimit(10**8)

N, M = map(int, sys.stdin.readline().rstrip().split())

parents = [i for i in range(N)]
answer = 0


def find(a):
    if a == parents[a]:
        return a
    else:
        b = find(parents[a])
        parents[a] = b
        return b


def union(a, b, idx):
    global answer
    a = find(a)
    b = find(b)

    if a != b:
        parents[max(a, b)] = min(a, b)
    elif answer == 0:
        answer = idx


for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b, i + 1)

print(answer)