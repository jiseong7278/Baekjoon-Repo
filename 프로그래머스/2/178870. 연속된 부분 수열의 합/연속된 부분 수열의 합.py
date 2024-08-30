def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    
    tempSum = 0
    end = 0
    length = n
    
    for start in range(0, n):
        while tempSum < k and end < n:
            tempSum += sequence[end]
            end += 1
        
        if tempSum == k:
            answer.append([start, end-1, end - start - 1])
        
        tempSum -= sequence[start]
    
    answer.sort(key = lambda x:x[2])
    
    return answer[0][:2]