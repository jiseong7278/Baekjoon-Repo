from sys import stdin

N = int(stdin.readline())

answer = 0

p_arr = []  # positive arr (1 ~ 1,000)
n_arr = []  # negative arr (-1,000 ~ 0)

for _ in range(N):
    num = int(stdin.readline())
    if num > 0:
        p_arr.append(num)
    else:
        n_arr.append(num)

p_arr.sort()
n_arr.sort(reverse=True)

while len(p_arr) > 1:
    p1 = p_arr.pop()
    p2 = p_arr.pop()

    if p1 > 1 and p2 > 1:
        answer += p1 * p2
    elif p1 == 1 or p2 == 1:
        answer += p1 + p2

if len(p_arr) == 1:
    answer += p_arr.pop()

while len(n_arr) > 1:
    answer += n_arr.pop() * n_arr.pop()

if len(n_arr) == 1:
    answer += n_arr.pop()

print(answer)
