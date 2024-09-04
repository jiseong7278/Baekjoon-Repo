def solution(n):
    answer = 0
    
    def convert(n, q):
        result = ''
        
        while n > 0:
            n, mod = divmod(n, q)
            result += str(mod)
        
        return result[::-1]
    
    converted = convert(n, 3)
    
    for i in range(len(converted)):
        answer += int(converted[i]) * (3 ** i)
    
    return answer