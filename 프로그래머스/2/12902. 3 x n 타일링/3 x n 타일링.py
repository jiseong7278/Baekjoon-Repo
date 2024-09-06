def solution(n):
    tile = []
    
    tile.append(3)
    tile.append(11)
    
    if n % 2 != 0:
        return 0
    
    n = n // 2
    
    if n > 2:
        for i in range(2, n):
            tile.append((tile[i-1] * 4 - tile[i-2]) % 1000000007)
    
    return tile[n-1] 