from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    s_to_l = -1
    l_to_e = -1
    
    def BFS(x, y, target):
        queue = deque()
        queue.append([x, y, 0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        while queue:
            cur_index = queue.popleft()
            
            for i in range(4):
                nx = cur_index[0] + dx[i]
                ny = cur_index[1] + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                
                if visited[nx][ny] or maps[nx][ny] == 'X':
                    continue
                
                visited[nx][ny] = True
                queue.append([nx, ny, cur_index[2] +1])
                
                if maps[nx][ny] == target:
                    return cur_index[2]+1
        return -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s_to_l = BFS(i, j, 'L')
            elif maps[i][j] == 'L':
                l_to_e = BFS(i, j, 'E')
    
    if s_to_l == -1 or l_to_e == -1:
        return -1
    else:
        answer = s_to_l + l_to_e
    
    return answer