times = list(map(int, input().split()))
D = int(input())

times[2] += D % 60
D = D // 60
if times[2] >= 60:
    times[2] -= 60
    times[1] += 1

times[1] += D % 60
D = D // 60
if times[1] >= 60:
    times[1] -= 60
    times[0] += 1

times[0] += D % 24
if times[0] >= 24:
    times[0] -= 24

print(times[0], times[1], times[2])
