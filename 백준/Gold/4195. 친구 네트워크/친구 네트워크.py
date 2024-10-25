import sys

sys.setrecursionlimit(10**6)


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    else:
        parents[y] = x
        visited[x] += visited[y]


def find(target):
    if target == parents[target]:
        return target
    else:
        parents[target] = find(parents[target])
        return parents[target]


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    F = int(sys.stdin.readline().rstrip())

    parents = dict()
    visited = dict()

    for _ in range(F):
        F1, F2 = sys.stdin.readline().rstrip().split()

        if F1 not in parents:
            parents[F1] = F1
            visited[F1] = 1

        if F2 not in parents:
            parents[F2] = F2
            visited[F2] = 1

        union(F1, F2)

        print(visited[find(F1)])