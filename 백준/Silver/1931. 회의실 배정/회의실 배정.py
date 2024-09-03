import sys

N = int(sys.stdin.readline())

lessons = []

for _ in range(N):
    lessons.append(list(map(int, sys.stdin.readline().split())))

lessons.sort(key=lambda x: x[0])
lessons.sort(key=lambda x: x[1])

endTime = lessons[0][1]

answer = 1

for i in range(1, len(lessons)):
    if lessons[i][0] >= endTime:
        endTime = lessons[i][1]
        answer += 1

print(answer)