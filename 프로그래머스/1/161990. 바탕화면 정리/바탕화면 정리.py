def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 51, 51, -1, -1
    
    for a in range(len(wallpaper)):
        for c in range(len(wallpaper[a])):
            if wallpaper[a][c] == '#':
                lux = min(lux, a)
                luy = min(luy, c)
                rdx = max(rdx, a+1)
                rdy = max(rdy, c+1)
    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)
    
    return answer