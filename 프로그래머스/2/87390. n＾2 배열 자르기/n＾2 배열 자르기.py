def solution(n, left, right):
    answer = []
    
    y = left // n
    x = (left % n)
    
    for i in range(0, right - left + 1):
        answer.append(max(y, x)+1)
        x += 1
        if x > n-1:
            x = 0
            y += 1
    
    return answer