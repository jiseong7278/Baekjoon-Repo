from itertools import permutations

def solution(numbers): 
    data = list(permutations(numbers, 2))
    
    answer = [sum(d) for d in data]
    
    answer = list(set(answer))
    
    answer.sort()
    
    return answer