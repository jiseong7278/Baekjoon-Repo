import sys
from collections import deque

input = sys.stdin.readline

K = int(input())


def BFS(v, group):
    queue = deque()
    queue.append(v)
    visited[v] = group

    while queue:
        cur = queue.popleft()

        for k in graph[cur]:
            if not visited[k]:
                queue.append(k)
                visited[k] = -1 * visited[cur]
            elif visited[k] == visited[cur]:
                return False
    return True


for i in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for j in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for j in range(1, V+1):
        if not visited[j]:
            result = BFS(j, 1)
            if not result:
                break

    print("YES" if result else "NO")