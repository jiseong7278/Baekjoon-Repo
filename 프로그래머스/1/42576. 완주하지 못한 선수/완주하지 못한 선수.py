def solution(participant, completion):
    answer = ''
    
    runner = {}
    
    for i in range(len(participant)):
        runner[participant[i]] = runner.setdefault(participant[i], 0) + 1
    
    for c in completion:
        runner[c] -= 1
    
    for p in participant:
        if runner[p] == 1:
            answer = p
    
    return answer