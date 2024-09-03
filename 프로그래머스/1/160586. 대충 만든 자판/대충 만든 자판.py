def solution(keymap, targets):
    answer = []
    
    totalKeyMap = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            totalKeyMap[keymap[i][j]] = min(totalKeyMap.setdefault(keymap[i][j], 99), j+1)
            
    for i in range(len(targets)):
        result = 0
        for j in range(len(targets[i])):
            temp = totalKeyMap.setdefault(targets[i][j], -1)
            if temp == -1:
                result = -1
                break
            result += temp
        
        answer.append(result)
    
    return answer