import sys


def div(y, x, n):
    color = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != paper[i][j]:
                m = n//3
                div(y, x, m)
                div(y, x+m, m)
                div(y, x+m+m, m)
                div(y+m, x, m)
                div(y+m+m, x, m)
                div(y+m, x+m, m)
                div(y+m, x+m+m, m)
                div(y+m+m, x+m, m)
                div(y+m+m, x+m+m, m)
                return
    if color == -1:
        result[0] += 1
    elif color == 0:
        result[1] += 1
    else:
        result[2] += 1


N = int(sys.stdin.readline().rstrip())

paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
result = [0, 0, 0]
div(0, 0, N)
print(result[0])
print(result[1])
print(result[2])