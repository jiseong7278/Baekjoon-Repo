def solution(numbers):
    answer = 0
    
    allNums = [i for i in range(10)]
    
    for n in numbers:
        allNums.remove(n)
    
    for a in allNums:
        answer += a
    
    return answer