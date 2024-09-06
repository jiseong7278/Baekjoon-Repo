def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = ''
        
        str_1 = str(bin(arr1[i])[2:].zfill(n))
        str_2 = str(bin(arr2[i])[2:].zfill(n))
        
        for j in range(len(str_1)):
            if str_1[j] == '1' or str_2[j] == '1':
                temp += '#'
            else:
                temp += ' '
                
        answer.append(temp)
    
    return answer