def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        temp = i
        sum = 0
        
        while sum < n:
            sum += temp
            temp += 1
            
            if sum == n:
                answer += 1
                break
    
    return answer