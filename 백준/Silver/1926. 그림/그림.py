from collections import deque

N, M = map(int, input().split())

visited = [[False for _ in range(M)] for _ in range(N)]

paper = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    paper.append(list(map(int, input().split())))


def BFS(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    count = 0

    while queue:
        cur_index = queue.pop()
        count += 1
        for j in range(4):
            nx = cur_index[0] + dx[j]
            ny = cur_index[1] + dy[j]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if visited[nx][ny] or paper[nx][ny] == 0:
                continue

            queue.append([nx, ny])
            visited[nx][ny] = True

    return count


amount = 0
breadth = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and paper[i][j] == 1:
            amount += 1
            breadth = max(breadth, BFS(i, j))

print(amount)
print(breadth)
