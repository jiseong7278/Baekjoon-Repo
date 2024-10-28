import sys


def div(y, x, n):
    global result

    color = video[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if color != video[i][j]:
                result += '('
                m = n//2
                div(y, x, m)
                div(y, x+m, m)
                div(y+m, x, m)
                div(y+m, x+m, m)
                result += ')'

                return

    result += video[y][x]


N = int(sys.stdin.readline())

video = [list(sys.stdin.readline().rstrip()) for i in range(N)]

result = ''

div(0, 0, N)

print(result)