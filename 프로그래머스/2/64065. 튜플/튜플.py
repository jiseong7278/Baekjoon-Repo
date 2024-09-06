def solution(str):
    num_dict = {}
    
    str = map(int, str.replace("{", "").replace("}", "").split(","))
    
    for s in str:
        num_dict[s] = num_dict.setdefault(s, 0) + 1
    
    answer = sorted(num_dict, key=lambda x: num_dict[x], reverse=True)
    
    return answer