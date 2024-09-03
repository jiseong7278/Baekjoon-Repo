import sys
import heapq

N = int(sys.stdin.readline())

lessons = []
temp = []

for _ in range(N):
    lessons.append(list(map(int, sys.stdin.readline().split())))

lessons.sort()
heapq.heappush(temp, lessons[0][1])

for i in range(1, N):
    if lessons[i][0] < temp[0]:
        heapq.heappush(temp, lessons[i][1])
    else:
        heapq.heappop(temp)
        heapq.heappush(temp, lessons[i][1])

print(len(temp))