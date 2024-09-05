import heapq

def solution(n, k, enemy):
    answer = 0

    heap = []
    
    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)
        if len(heap) > k:
            n -= heapq.heappop(heap)  # 제일 낮은 값을 뽑은 뒤 n에서 해당 값을 뺌
        if n < 0:  # 배열의 0 ~ i까지의 요소들 중 낮은 값들을 빼고 n < 0 이 되면 Game Over
            return i
    
    return len(enemy)
