import heapq

def solution(book_time):
    
    for i in range(len(book_time)):
        for j in range(2):
            times = book_time[i][j].split(":")
            
            book_time[i][j] = int(times[0]) * 60 + int(times[1])
    
    book_time.sort()
    
    heap = []
    
    heapq.heappush(heap, book_time[0][1])
    
    for i in range(1, len(book_time)):
        if book_time[i][0] < heap[0] + 10:
            heapq.heappush(heap, book_time[i][1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, book_time[i][1])
    
    return len(heap)