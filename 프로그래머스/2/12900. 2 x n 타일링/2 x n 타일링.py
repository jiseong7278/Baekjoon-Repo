def solution(n):
    tile = []
    
    tile.append(1)
    tile.append(2)
    
    if n > 2:
        for i in range(2, n):
            tile.append((tile[i-2] + tile[i-1]) % 1000000007)
    
    return tile[n-1] 