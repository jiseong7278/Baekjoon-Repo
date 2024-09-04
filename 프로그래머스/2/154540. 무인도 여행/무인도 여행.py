from collections import deque

def solution(maps):
    answer = []
    
    maps = [[c for c in maps[i]] for i in range(len(maps))]
    
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    def BFS(x, y):
        sum = 0
        sum += int(maps[x][y])
        queue = deque()
        queue.append([x, y])
        maps[x][y] = -1
        
        while queue:
            cur_position = queue.popleft()
            
            for i in range(4):
                nx = cur_position[0] + dx[i]
                ny = cur_position[1] + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                    
                if maps[nx][ny] == 'X' or maps[nx][ny] == -1:
                    continue
                    
                sum += int(maps[nx][ny])
                queue.append([nx, ny])
                maps[nx][ny] = -1
        
        return sum
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and maps[i][j] != -1:
                answer.append(BFS(i, j))
    
    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer