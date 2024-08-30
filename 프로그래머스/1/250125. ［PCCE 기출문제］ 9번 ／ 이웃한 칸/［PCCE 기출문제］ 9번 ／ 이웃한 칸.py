def solution(board, h, w):
    answer = 0
    
    curColor = board[h][w]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(0, 4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
            continue
        
        if board[nx][ny] == curColor:
            answer += 1
    
    return answer