import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = [sys.stdin.readline() for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 0

def BFS(x, y):
    global count
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        q = queue.popleft()

        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]

            if nx < 0 or ny < 0 or N <= nx or M <= ny:
                continue

            if visited[nx][ny] or A[nx][ny] == "X":
                continue

            if A[nx][ny] == "P":
                count+=1

            queue.append([nx, ny])
            visited[nx][ny] = True

for i in range(N):
    for j in range(M):
        if A[i][j] == "I":
            BFS(i, j)

if count == 0:
    print("TT")
else:
    print(count)