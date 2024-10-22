import sys

sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().rstrip().split())

nodes = [[] for i in range(N+1)]
visited = [False] * len(nodes)
answer = [0 for _ in range(N+1)]

visit_order = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append(v)
    nodes[v].append(u)

for i in range(N+1):
    nodes[i].sort()

def DFS(start):
    global visit_order

    visited[start] = True
    answer[start] = visit_order
    visit_order += 1

    for n in nodes[start]:
        if not visited[n]:
            DFS(n)

DFS(R)

for i in range(1, N+1):
    print(answer[i])