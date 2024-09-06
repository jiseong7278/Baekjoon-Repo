import sys

N = int(sys.stdin.readline())

words = []

for _ in range(N):
    temp_str = sys.stdin.readline().replace('\n', '')
    words.append(temp_str)

words = list(set(words))

words.sort()
words.sort(key=lambda word: len(word))

for w in words:
    print(w)