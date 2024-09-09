import math
import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers = sorted(numbers)

print(math.floor(sum(numbers)/N+0.5))
print(numbers[N//2])

counter = Counter(numbers).most_common()

if len(numbers) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(numbers[0])


print(numbers[N-1] - numbers[0])