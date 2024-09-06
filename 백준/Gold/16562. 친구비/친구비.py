import sys

N, M, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

relation = []

for i in range(M):
    V, W = map(int, sys.stdin.readline().split())
    relation.append([V, W])

parents = []

for i in range(N+1):
    parents.append(i)


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if A[a-1] < A[b-1]:
            parents[b] = a
        else:
            parents[a] = b


def find(a):
    if a == parents[a]:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]


for r in relation:
    union(r[0], r[1])

cost = 0

for i in range(1, N+1):
    if i == parents[i]:
        cost += A[i-1]

if cost <= K:
    print(cost)
else:
    print("Oh no")
