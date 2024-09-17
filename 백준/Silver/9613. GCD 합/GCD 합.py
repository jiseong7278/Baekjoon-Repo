import sys
import math
from itertools import combinations

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    test_case = list(map(int, sys.stdin.readline().rstrip().split()))

    N = test_case[0]

    gcd_sum = 0

    test_case.remove(N)

    comb_test = list(combinations(test_case, 2))

    for c in comb_test:
        gcd_sum += math.gcd(*c)

    print(gcd_sum)