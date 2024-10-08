def solution(data, ext, val_ext, sort_by):
    
    data_dict = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3
    }
    
    answer = []

    for d in data:
        if d[data_dict.get(ext)] < val_ext:
            answer.append(d)

    answer.sort(key=lambda x: x[data_dict.get(sort_by)])
    
    return answer