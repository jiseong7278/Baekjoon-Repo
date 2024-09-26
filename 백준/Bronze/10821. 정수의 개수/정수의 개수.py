from sys import stdin as st

S = list(st.readline().rstrip().split(","))

count = 0

for s in S:
    if s.isdigit():
        count += 1

print(count)