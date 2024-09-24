from sys import stdin as st

for _ in range(int(st.readline().rstrip())):
    print(sum(map(int, st.readline().rstrip().split(","))))