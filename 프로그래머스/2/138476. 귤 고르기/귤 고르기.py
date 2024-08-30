from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    tanList = Counter(tangerine).most_common()
    
    for size in tanList:
        k -= size[1]
        answer += 1
        if k <= 0:
            break
    
    return answer