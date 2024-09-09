def solution(n):
    answer = 0
    
    count_1 = bin(n)[2:].count("1")
    
    m = n
    
    while True:
        m += 1
        
        next_num_count = bin(m)[2:].count("1")
        
        if count_1 == next_num_count:
            answer = m
            break
    
    return answer