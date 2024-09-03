def solution(players, callings):
    answer = []
    
    ranking = {}
    
    for i, p in enumerate(players):
        ranking[p] = i
        
    for c in callings:
        curRanking = ranking[c]
        curPlayer = players[curRanking]
        prevPlayer = players[curRanking-1]
        
        players[curRanking-1], players[curRanking] = curPlayer, prevPlayer
        
        ranking[prevPlayer] += 1
        ranking[curPlayer] -= 1
    
    return players