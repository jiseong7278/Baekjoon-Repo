def solution(park, routes):
    moving = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    r_i, r_j = 0, 0
    
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == 'S':
                r_i = i
                r_j = j
    
    for route in routes:
        direct, distance = route.split(' ')
        distance = int(distance)
        di, dj = moving[direct]
        
        isValid = True
        ni, nj = r_i, r_j
        
        for _ in range(distance):
            ni += di
            nj += dj
            
            if ni < 0 or nj < 0 or ni >= len(park) or nj >= len(park[0]) or park[ni][nj] == 'X':
                isValid = False
                break
            
        if isValid:
            r_i, r_j = ni, nj
    
    answer = [r_i, r_j]
    
    return answer