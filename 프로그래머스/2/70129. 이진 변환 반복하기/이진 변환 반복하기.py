def solution(s):
    answer = []
    
    convert = 0
    zeroCount = 0
    
    while s != "1":
        amount = s.count("0")
        
        if amount > 0:
            zeroCount += amount
        
        convert += 1
        s = str(bin(s.count("1"))[2:])
    
    answer.append(convert)
    answer.append(zeroCount)
    
    return answer