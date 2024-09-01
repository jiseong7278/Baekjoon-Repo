def solution(board):
    answer = 1
    
    player = ['O', 'X']
    
    width = len(board[0])
    height = len(board)
    
    oCount = 0
    xCount = 0
    
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'O':
                oCount += 1
            elif board[i][j] == 'X':
                xCount += 1
    
    if xCount > oCount or oCount - xCount > 1:
        return 0
    
    def isWin():
        winList = [False, False]
        
        for i in range(2):
            # 가로 확인
            for j in range(height):
                count = board[j].count(player[i])
                if count == 3:
                    winList[i] = True
            
            # 세로 확인
            for j in range(width):
                count = 0
                for k in range(height):
                    if board[k][j] == player[i]:
                        count += 1
                if count == 3:
                    winList[i] = True
                    
            # 대각선 확인
            if board[0][0] == board[1][1] == board[2][2] == player[i]:
                winList[i] = True
            
            if board[0][2] == board[1][1] == board[2][0] == player[i]:
                winList[i] = True
        
        return winList
    
    winList = isWin()
    
    if winList[0] and winList[1]:
        return 0
    
    if winList[1] and oCount > xCount:
        return 0
    
    if winList[0] and oCount == xCount:
        return 0
    
    return answer