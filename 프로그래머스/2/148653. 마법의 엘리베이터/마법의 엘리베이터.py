def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10
        storey = storey // 10
        
        if digit > 5:
            answer += 10 - digit
            storey += 1
        elif digit == 5 and storey % 10 >=5 :
            answer += digit
            storey += 1
        else:
            answer += digit
        
    return answer