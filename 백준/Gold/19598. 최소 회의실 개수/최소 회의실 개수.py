import heapq
import sys

N = int(sys.stdin.readline().rstrip())

times = []

for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().rstrip().split())))

times.sort(key=lambda x: (x[0], x[1]))

heap = []

for s, e in times:
    if len(heap) == 0:
        heapq.heappush(heap, e)
    else:
        if heap[0] <= s:
            heapq.heappop(heap)
            heapq.heappush(heap, e)
        else:
            heapq.heappush(heap, e)

print(len(heap))