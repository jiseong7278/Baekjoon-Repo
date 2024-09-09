from itertools import combinations
import sys

L, C = map(int, sys.stdin.readline().rstrip().split())

chars = list(sys.stdin.readline().rstrip().split())

chars.sort()

comb = list(combinations(chars, L))

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(comb)):
    vowel_cnt = 0
    crypt_str = ''
    for j in range(len(comb[i])):
        crypt_str += comb[i][j]
        for v in vowels:
            if comb[i][j] == v:
                vowel_cnt += 1

    if 1 <= vowel_cnt <= L - 2:
        print(crypt_str)
