from collections import deque

def solution(board):
    answer = -1
    W, H = len(board[0]), len(board)
    
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    
    boards = []
    visited = [list(False for _ in range(W)) for _ in range(H)]
    
    # robot index
    r_i, r_j = 0, 0
    
    # initialize boards and find index of R
    for i, row in enumerate(board):
        boards.append(list(board[i]))
        for j, element in enumerate(row):
            if element == 'R':
                r_i = i
                r_j = j
    
     # 벽 또는 보드 끝까지 이동하는 함수
    def move(move_i, move_j, direct):
        # 특정 방향으로 계속 이동
        while True:
            move_i += di[direct]
            move_j += dj[direct]
            
            # 현재 위치가 벽 또는 보드 끝을 넘어가면 반복문 종료
            if move_i < 0 or move_j < 0 or move_i >= H or move_j >= W:
                break
            
            if boards[move_i][move_j] == 'D':
                break
        
        # 뒤로 한칸 이동
        move_i -= di[direct]
        move_j -= dj[direct]
        return [move_i, move_j] # 현재 좌표 return [di, dj]
    
    queue = deque()
    queue.append([r_i, r_j, 0])
    visited[r_i][r_j] = True
    
    while queue:
        ni, nj, count = queue.pop()
        
        for i in range(4):
            a_i, a_j = move(ni, nj, i)
            
            if visited[a_i][a_j]:
                continue
            elif boards[a_i][a_j] == 'G':
                return count + 1
            else:
                visited[a_i][a_j] = True
                queue.appendleft([a_i, a_j, count+1])
    
    return answer