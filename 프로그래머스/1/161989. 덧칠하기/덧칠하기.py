from collections import deque

def solution(n, m, section):
    answer = 0
    
    temp = section[0] + m
    
    for i in range(len(section)):
        if section[i] >= temp:
            answer += 1
            temp = section[i] + m
    
    return answer+1